from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from common import (
    DUPLICATE_REJECTED_STATUS,
    article_dir,
    article_file,
    canonicalize_article_url,
    find_kept_canonical_conflict,
    read_markdown,
    source_body_text,
    source_file,
    ticket_path,
    timestamp_for_date,
    utc_now,
    write_article_markdown,
    write_markdown,
)
from micro_common import (
    article_stage_path,
    assert_no_visible_internal_ids,
    clean_loose_text,
    parse_keep_discard,
    head_tail_source_excerpt,
)
from article_job_runtime import (
    JobContractError,
    apply_claim_links,
    claim_records_to_findings_lines,
    compact_source_for_extractor,
    evidence_files_to_fact_lines,
    evidence_files_to_records,
    run_curator_admission,
    run_extractor_evidence,
    run_synthesist_article_write,
    run_synthesist_claims,
)
from article_law_reviews import write_contradiction_review, write_mechanism_review
from pdf_markdown_local import fetch_arxiv_best_markdown, parse_arxiv_id
from structured_artifact_bundle import materialize_article_structured_bundle

CURATOR_TIMEOUT_SECONDS = 120
FINDINGS_TIMEOUT_SECONDS = 120
FACTS_TIMEOUT_SECONDS = 180
SUMMARY_TIMEOUT_SECONDS = 300
ABSTRACT_ONLY_GATE_REASON = "abstract-only-paper-source"
PAPER_SOURCE_HINTS = (
    "openreview.net",
    "doi.org",
    "aclanthology.org",
    "papers.nips.cc",
    "proceedings.mlr.press",
)


def write_stage(article_id: str, stage: str, text: str) -> Path:
    path = article_stage_path(article_id, stage)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(clean_loose_text(text) + "\n", encoding="utf-8")
    return path


def article_body_from_summary(summary_text: str, fallback_title: str) -> str:
    body = clean_loose_text(summary_text)
    if not body.startswith("# "):
        body = f"# {fallback_title}\n\n{body}"
    assert_no_visible_internal_ids(body, label="article-summary")
    return body


def markdown_section_text(body: str, heading: str) -> str:
    match = re.search(rf"^##\s+{re.escape(heading)}\s*(?P<section>.*?)(?:\n##\s+|\Z)", body, re.MULTILINE | re.DOTALL)
    if not match:
        return ""
    return match.group("section").strip()


def legacy_worthiness_text(curator_meta: dict, curator_body: str) -> str:
    decision = "KEEP" if str(curator_meta.get("decision") or "") == "kept" else "DISCARD"
    reason = str(curator_meta.get("reason") or "").strip()
    limits = markdown_section_text(curator_body, "Limits")
    parts = [decision]
    if reason:
        parts.append(reason)
    if limits:
        parts.append(f"Limits: {limits}")
    return "\n\n".join(part for part in parts if part)


def strip_generated_capture_wrapper(markdown: str) -> str:
    blocks = [block.strip() for block in str(markdown or "").split("\n\n") if block.strip()]
    while blocks and (
        blocks[0].startswith("# ")
        or blocks[0].startswith("Source:")
        or blocks[0].startswith("Generated:")
        or blocks[0].startswith("> Note:")
    ):
        blocks.pop(0)
    return "\n\n".join(blocks).strip()


def _is_generic_arxiv_stub(title: str) -> bool:
    cleaned = str(title or "").strip()
    if not cleaned:
        return False
    return bool(re.fullmatch(r"arxiv\s+\d{4}\.\d{4,5}(?:v\d+)?", cleaned, re.I))


def _descriptive_title_from_source_body(source_body: str) -> str:
    body = source_body_text(source_body)
    for raw_line in body.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line.startswith(("#", "Source:", "Generated:", "> Note:")):
            continue
        if _is_generic_arxiv_stub(line):
            continue
        if re.match(r"^(?:\d+\.?\s+)?Introduction\b", line, re.I):
            continue
        if len(line.split()) >= 4:
            return line
    return ""


def source_title(article_meta: dict, source_meta: dict, source_body: str = "") -> str:
    article_title = str(article_meta.get("source_title") or "").strip()
    source_meta_title = str(source_meta.get("source_title") or "").strip()
    if article_title and not _is_generic_arxiv_stub(article_title):
        return article_title
    if source_meta_title and not _is_generic_arxiv_stub(source_meta_title):
        return source_meta_title
    body_title = _descriptive_title_from_source_body(source_body)
    if body_title:
        return body_title
    if source_meta_title:
        return source_meta_title
    if article_title:
        return article_title
    return str(article_meta.get("source_url") or source_meta.get("source_url") or "Untitled")


def is_paper_like_source(article_meta: dict, source_meta: dict) -> bool:
    url = str(article_meta.get("canonical_url") or article_meta.get("source_url") or source_meta.get("canonical_url") or source_meta.get("source_url") or "")
    low = url.lower()
    if parse_arxiv_id(low):
        return True
    if any(hint in low for hint in PAPER_SOURCE_HINTS):
        return True
    stitle = str(source_meta.get("source_title") or "")
    if re.match(r"^\[\d{4}\.\d{4,5}\]", stitle):
        return True
    return False


def source_has_full_paper_text(source_meta: dict, source_body: str) -> bool:
    body = source_body_text(source_body)
    low = body.lower()
    capture_kind = str(source_meta.get("capture_kind") or "").lower()
    content_type = str(source_meta.get("content_type") or "").lower()
    if content_type == "application/pdf":
        return True
    if "source: https://arxiv.org/pdf/" in low or "source: https://arxiv.org/html/" in low:
        return True
    if capture_kind.startswith("pdf") or capture_kind == "arxiv_html":
        if re.search(r"(^|\n)(?:#+\s*)?(?:1\.?\s+)?introduction\b", body, re.I):
            return True
    if len(body) >= 20000 and re.search(r"\bintroduction\b", low):
        return True
    return False


def needs_full_paper_remediation(article_meta: dict, source_meta: dict, source_body: str) -> bool:
    if not is_paper_like_source(article_meta, source_meta):
        return False
    if source_has_full_paper_text(source_meta, source_body):
        return False
    body = source_body_text(source_body).lower()
    if "skip to main content" in body:
        return True
    if re.search(r"(^|\n)(?:#+\s*)?abstract\b", body, re.I) and not re.search(r"\bintroduction\b", body, re.I):
        return True
    return len(body) < 12000


def remediate_paper_source(article_id: str, ticket_id: str, article_meta: dict, source_meta: dict) -> tuple[dict, str]:
    url = str(article_meta.get("canonical_url") or article_meta.get("source_url") or source_meta.get("canonical_url") or source_meta.get("source_url") or "")
    arxiv_id = parse_arxiv_id(url)
    if not arxiv_id:
        raise RuntimeError("no_fulltext_remediator")
    converted = fetch_arxiv_best_markdown(arxiv_id, allow_abs_fallback=False)
    title = str(converted.get("title") or source_title(article_meta, source_meta))
    body_text = strip_generated_capture_wrapper(str(converted.get("markdown") or ""))
    if not body_text:
        raise RuntimeError("empty_fulltext_capture")
    capture_kind = str(converted.get("method") or "arxiv")
    content_type = "application/pdf" if capture_kind.startswith("pdf") else "text/html"
    captured_at = utc_now()
    new_meta = {
        "version": "source-capture.v1",
        "article_id": article_id,
        "ticket_id": ticket_id,
        "source_url": article_meta.get("source_url") or source_meta.get("source_url") or url,
        "canonical_url": article_meta.get("canonical_url") or source_meta.get("canonical_url") or url,
        "source_title": title,
        "capture_kind": capture_kind,
        "http_status": 200,
        "content_type": content_type,
        "captured_at_utc": captured_at,
        "linked_paper_urls": list(source_meta.get("linked_paper_urls") or source_meta.get("linkedPaperUrls") or []),
    }
    write_markdown(
        source_file(article_id),
        new_meta,
        f"# Source Capture\n\n## Title\n\n{title}\n\n## Body\n\n{body_text.strip()}\n",
    )
    article_meta["captured_at_utc"] = captured_at
    article_meta["source_title"] = title
    return read_markdown(source_file(article_id))


def prompt_budgets(article_meta: dict, source_meta: dict, source_body: str) -> tuple[int, int, int, int, int, int, int]:
    if is_paper_like_source(article_meta, source_meta) and source_has_full_paper_text(source_meta, source_body):
        return (180, 300, 420, 600, 9000, 16000, 24000)
    return (CURATOR_TIMEOUT_SECONDS, FINDINGS_TIMEOUT_SECONDS, FACTS_TIMEOUT_SECONDS, SUMMARY_TIMEOUT_SECONDS, 4200, 1200, 1800)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--article-id", required=True)
    parser.add_argument("--replay-date")
    parser.add_argument("--curator-agent", default="curator")
    parser.add_argument("--findings-agent", default="extractor")
    parser.add_argument("--extractor-agent", default="extractor")
    parser.add_argument("--synthesist-agent", default="synthesist")
    args = parser.parse_args()

    article_meta, article_body = read_markdown(article_file(args.article_id))
    source_meta, source_body = read_markdown(source_file(args.article_id))
    ticket_meta, ticket_body = read_markdown(ticket_path(article_meta["ticket_id"]))
    article_meta["canonical_url"] = canonicalize_article_url(str(article_meta.get("canonical_url") or article_meta.get("source_url") or ""))

    if needs_full_paper_remediation(article_meta, source_meta, source_body):
        try:
            source_meta, source_body = remediate_paper_source(args.article_id, article_meta["ticket_id"], article_meta, source_meta)
            article_meta["source_remediation_status"] = "completed"
            article_meta["source_remediated_at_utc"] = source_meta.get("captured_at_utc") or utc_now()
        except Exception as exc:
            article_meta["publication_status"] = "capture-blocked"
            article_meta["source_capture_gate_reason"] = ABSTRACT_ONLY_GATE_REASON
            article_meta["source_remediation_required"] = True
            article_meta["source_remediation_error"] = str(exc)
            ticket_meta["status"] = "capture-blocked"
            ticket_meta["source_capture_gate_reason"] = ABSTRACT_ONLY_GATE_REASON
            write_article_markdown(
                article_file(args.article_id),
                article_meta,
                (
                    "# Source Remediation Needed\n\n"
                    "This paper source is still abstract-only. Pull full text before Curator, findings, facts, or summary can proceed.\n"
                ),
            )
            write_markdown(ticket_path(article_meta["ticket_id"]), ticket_meta, ticket_body)
            print(article_file(args.article_id))
            return 0

    curator_timeout, findings_timeout, facts_timeout, summary_timeout, curator_chars, _findings_chars, _facts_chars = prompt_budgets(article_meta, source_meta, source_body)
    curator_excerpt = head_tail_source_excerpt(
        source_body,
        max_chars=curator_chars if curator_chars > 4200 else 4200,
        tail_chars=(curator_chars // 3) if curator_chars > 4200 else 1200,
    )

    source_name = source_title(article_meta, source_meta, source_body)
    curator_result = run_curator_admission(
        article_id=args.article_id,
        ticket_id=article_meta["ticket_id"],
        source_title=source_name,
        source_url=article_meta["source_url"],
        source_excerpt=curator_excerpt,
        agent_id=args.curator_agent,
        timeout=curator_timeout,
    )
    worthiness_text = legacy_worthiness_text(curator_result["meta"], curator_result["body"])
    write_stage(args.article_id, "worthiness", worthiness_text)
    try:
        decision, remainder = parse_keep_discard(worthiness_text)
        curator_mode = "agent"
    except ValueError as exc:
        raise JobContractError(f"curator_receipt_unusable:{exc}") from exc
    reason = str(curator_result["meta"].get("reason") or "").strip() or (remainder.split("\n\n", 1)[0].strip() if remainder else "")

    article_meta["curator_decision"] = decision
    article_meta["curator_reason"] = reason
    article_meta["curated_at_utc"] = timestamp_for_date(args.replay_date)
    article_meta["curator_mode"] = curator_mode
    ticket_meta["status"] = decision

    if decision == "discarded":
        article_meta["publication_status"] = "discarded"
        article_meta["evidence_count"] = 0
        article_meta["claim_count"] = 0
        discard_body = "# Discarded Article\n\nThis source was discarded by Curator.\n"
        materialize_article_structured_bundle(
            article_id=args.article_id,
            article_meta=article_meta,
            article_body=discard_body,
            worthiness_text=worthiness_text,
        )
        write_article_markdown(article_file(args.article_id), article_meta, discard_body)
        write_markdown(ticket_path(article_meta["ticket_id"]), ticket_meta, ticket_body)
        print(article_dir(args.article_id) / "micro-worthiness.md")
        return 0

    conflict = find_kept_canonical_conflict(
        article_meta["canonical_url"],
        exclude_article_id=args.article_id,
        title=str(source_meta.get("source_title") or article_meta.get("source_title") or ""),
        text=source_body,
        related_urls=list(source_meta.get("linked_paper_urls") or source_meta.get("linkedPaperUrls") or []),
    )
    if conflict:
        existing = conflict["existing_article"]
        article_meta["publication_status"] = DUPLICATE_REJECTED_STATUS
        article_meta["duplicate_of_article_id"] = existing["article_id"]
        article_meta["duplicate_match_signature"] = conflict["matched_signature"]
        article_meta["duplicate_rejected_at_utc"] = timestamp_for_date(args.replay_date)
        ticket_meta["status"] = DUPLICATE_REJECTED_STATUS
        ticket_meta["canonical_url"] = article_meta["canonical_url"]
        ticket_meta["duplicate_of_article_id"] = existing["article_id"]
        ticket_meta["duplicate_match_signature"] = conflict["matched_signature"]
        write_article_markdown(
            article_file(args.article_id),
            article_meta,
            (
                "# Duplicate Rejected\n\n"
                "This source passed worthiness but was blocked at the keep gate because the same work already exists in the institute.\n"
            ),
        )
        write_markdown(ticket_path(article_meta["ticket_id"]), ticket_meta, ticket_body)
        print(article_file(args.article_id))
        return 0

    extractor_result = run_extractor_evidence(
        article_id=args.article_id,
        source_title=source_name,
        source_url=article_meta["source_url"],
        source_markdown=compact_source_for_extractor(source_body),
        agent_id=args.extractor_agent,
        timeout=facts_timeout,
    )
    evidence_records = evidence_files_to_records(args.article_id, extractor_result["evidence_files"])
    facts = evidence_files_to_fact_lines(extractor_result["evidence_files"])
    facts_text = "\n".join(f"- {line}" for line in facts)
    write_stage(args.article_id, "facts", facts_text)
    if not facts:
        raise ValueError("missing_facts")

    claims_result = run_synthesist_claims(
        article_id=args.article_id,
        source_title=source_name,
        source_url=article_meta["source_url"],
        findings_lines=facts[:4],
        facts_lines=facts,
        evidence_records=evidence_records,
        agent_id=args.synthesist_agent,
        timeout=findings_timeout,
    )
    claims, evidence_records = apply_claim_links(claims_result["claims"], evidence_records)
    findings = claim_records_to_findings_lines(claims)
    findings_text = "\n".join(f"- {line}" for line in findings)
    write_stage(args.article_id, "findings", findings_text)
    if not findings:
        raise ValueError("missing_findings")

    article_write = run_synthesist_article_write(
        article_id=args.article_id,
        source_title=source_name,
        source_url=article_meta["source_url"],
        queued_at_utc=str(article_meta.get("queued_at_utc") or ""),
        captured_at_utc=str(article_meta.get("captured_at_utc") or source_meta.get("captured_at_utc") or ""),
        artifact_minted_at_utc=timestamp_for_date(args.replay_date),
        claims=claims,
        evidence_records=evidence_records,
        agent_id=args.synthesist_agent,
        timeout=summary_timeout,
    )
    write_stage(args.article_id, "summary", article_write["body"])
    body = article_write["body"]

    article_meta["source_title"] = source_name
    article_meta["evidence_count"] = len(facts)
    article_meta["claim_count"] = len(findings)
    article_meta["extracted_at_utc"] = timestamp_for_date(args.replay_date)
    article_meta["extractor_mode"] = "agent"
    article_meta["findings_mode"] = "agent"
    article_meta["summary_mode"] = "agent"
    article_meta["artifact_minted_at_utc"] = timestamp_for_date(args.replay_date)
    article_meta["publication_status"] = "ready-for-daily"
    article_meta.pop("source_capture_gate_reason", None)
    article_meta.pop("source_remediation_required", None)
    article_meta.pop("source_remediation_error", None)
    write_contradiction_review(
        args.article_id,
        article_meta,
        body,
        findings_text,
        facts_text,
        claims,
        evidence_records,
    )
    write_mechanism_review(
        args.article_id,
        article_meta,
        body,
        findings_text,
        facts_text,
        claims,
        evidence_records,
    )
    bundle_result = materialize_article_structured_bundle(
        article_id=args.article_id,
        article_meta=article_meta,
        article_body=body,
        worthiness_text=worthiness_text,
        findings_text=findings_text,
        facts_text=facts_text,
        claims_records=claims,
        evidence_records=evidence_records,
    )
    article_meta["evidence_count"] = bundle_result["evidence_count"]
    article_meta["claim_count"] = bundle_result["claim_count"]
    write_article_markdown(article_file(args.article_id), article_meta, body)
    write_markdown(ticket_path(article_meta["ticket_id"]), ticket_meta, ticket_body)
    print(article_file(args.article_id))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
