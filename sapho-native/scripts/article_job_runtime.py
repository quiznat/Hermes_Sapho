from __future__ import annotations

import json
import re
from typing import Any

import yaml

from common import compose_persona_job_prompt, parse_markdown, source_body_text
from micro_common import assert_no_visible_internal_ids, bullet_lines, clean_loose_text, run_loose_agent


class JobContractError(ValueError):
    pass


_CODE_BLOCK_RE = re.compile(
    r"^###\s+file:\s+(?P<filename>[^\n]+)\n```markdown\n(?P<content>.*?)\n```\s*$",
    re.MULTILINE | re.DOTALL,
)


def _clean(text: Any) -> str:
    return clean_loose_text(str(text or "")).strip()


def _quote_yaml_scalar_values(text: str) -> str:
    rendered: list[str] = []
    scalar_pattern = re.compile(r"^(\s*[A-Za-z0-9_]+:\s)(.+)$")
    for line in text.splitlines():
        match = scalar_pattern.match(line)
        if not match:
            rendered.append(line)
            continue
        prefix, value = match.groups()
        stripped = value.strip()
        if not stripped or stripped.startswith(("-", "[", "{", "|", ">", "'", '"')):
            rendered.append(line)
            continue
        if re.fullmatch(r"(?:true|false|null|[-+]?\d+(?:\.\d+)?)", stripped, re.I):
            rendered.append(line)
            continue
        rendered.append(prefix + json.dumps(stripped, ensure_ascii=False))
    return "\n".join(rendered)


def _yaml_mapping(text: str) -> dict[str, Any]:
    cleaned = _clean(text)
    try:
        payload = yaml.safe_load(cleaned) or {}
    except yaml.YAMLError:
        payload = yaml.safe_load(_quote_yaml_scalar_values(cleaned)) or {}
    if not isinstance(payload, dict):
        raise JobContractError("yaml_output_not_mapping")
    return payload


def _markdown_sections(body: str) -> dict[str, str]:
    parts = re.split(r"^##\s+", body, flags=re.MULTILINE)
    result: dict[str, str] = {}
    for part in parts[1:]:
        heading, _, rest = part.partition("\n")
        result[heading.strip()] = rest.strip()
    return result


def _mission_header(article_id: str, source_title: str, source_url: str) -> str:
    return (
        "Mission Context\n\n"
        f"article_id: {article_id}\n"
        f"source_title: {_clean(source_title)}\n"
        f"source_url: {_clean(source_url)}\n"
    )


def run_curator_admission(*, article_id: str, ticket_id: str, source_title: str, source_url: str, source_excerpt: str, agent_id: str, timeout: int) -> dict[str, Any]:
    prompt = compose_persona_job_prompt("curator", "admission", require_job=True)
    mission = (
        f"Mission Context\n\n"
        f"article_id: {article_id}\n"
        f"ticket_id: {ticket_id}\n"
        f"source_title: {_clean(source_title)}\n"
        f"source_url: {_clean(source_url)}\n\n"
        "Captured source excerpt:\n\n"
        f"{_clean(source_excerpt)}\n"
    )
    raw = run_loose_agent(agent_id, f"{prompt}\n\n{mission}", timeout=timeout, thinking="off")
    meta, body = parse_markdown(raw)
    if str(meta.get("role") or "") != "Curator":
        raise JobContractError("curator_role_mismatch")
    if str(meta.get("article_id") or "") != article_id:
        raise JobContractError("curator_article_id_mismatch")
    if str(meta.get("ticket_id") or "") != ticket_id:
        raise JobContractError("curator_ticket_id_mismatch")
    decision = str(meta.get("decision") or "").strip()
    if decision not in {"kept", "discarded"}:
        raise JobContractError("curator_invalid_decision")
    return {"raw": raw, "meta": meta, "body": body}


def run_extractor_evidence(*, article_id: str, source_title: str, source_url: str, source_markdown: str, agent_id: str, timeout: int) -> dict[str, Any]:
    prompt = compose_persona_job_prompt("extractor", "evidence", require_job=True)
    mission = (
        f"{_mission_header(article_id, source_title, source_url)}\n"
        "Captured Source Markdown:\n\n"
        f"{_clean(source_markdown)}\n"
    )
    raw = run_loose_agent(agent_id, f"{prompt}\n\n{mission}", timeout=timeout, thinking="off")
    meta, body = parse_markdown(raw)
    if str(meta.get("role") or "") != "Extractor":
        raise JobContractError("extractor_role_mismatch")
    if str(meta.get("article_id") or "") != article_id:
        raise JobContractError("extractor_article_id_mismatch")
    evidence_files = parse_evidence_receipt_files(article_id, raw)
    declared_count = int(meta.get("evidence_count") or 0)
    if declared_count != len(evidence_files):
        raise JobContractError("extractor_evidence_count_mismatch")
    return {"raw": raw, "meta": meta, "body": body, "evidence_files": evidence_files}


def parse_evidence_receipt_files(article_id: str, receipt_markdown: str) -> list[dict[str, Any]]:
    _meta, body = parse_markdown(receipt_markdown)
    files: list[dict[str, Any]] = []
    seen_evidence_ids: set[str] = set()
    valid_mechanism_relevance = {"direct", "bounded", "none"}
    valid_contradiction_relevance = {"supports", "tension", "none"}
    for match in _CODE_BLOCK_RE.finditer(body):
        filename = match.group("filename").strip()
        content = match.group("content").strip()
        file_meta, file_body = parse_markdown(content)
        if str(file_meta.get("article_id") or "") != article_id:
            raise JobContractError("evidence_article_id_mismatch")
        evidence_id = str(file_meta.get("evidence_id") or "").strip()
        if not evidence_id:
            raise JobContractError("missing_evidence_id")
        if evidence_id in seen_evidence_ids:
            continue
        mechanism_relevance = str(file_meta.get("mechanism_relevance") or "").strip()
        contradiction_relevance = str(file_meta.get("contradiction_relevance") or "").strip()
        if not mechanism_relevance or not contradiction_relevance:
            raise JobContractError("missing_evidence_relevance_fields")
        if mechanism_relevance not in valid_mechanism_relevance:
            raise JobContractError("invalid_mechanism_relevance")
        if contradiction_relevance not in valid_contradiction_relevance:
            raise JobContractError("invalid_contradiction_relevance")
        sections = _markdown_sections(file_body)
        statement = file_body.split("\n## Source Excerpt\n", 1)[0].strip()
        if not statement:
            raise JobContractError("missing_evidence_statement")
        source_excerpt = sections.get("Source Excerpt", "")
        if not _clean(source_excerpt):
            raise JobContractError("missing_evidence_source_excerpt")
        note = sections.get("Note", "")
        if (mechanism_relevance == "bounded" or contradiction_relevance == "tension") and not _clean(note):
            raise JobContractError("bounded_or_tension_evidence_missing_note")
        seen_evidence_ids.add(evidence_id)
        files.append(
            {
                "filename": filename,
                "meta": file_meta,
                "body": file_body,
                "statement": statement,
                "source_excerpt": source_excerpt,
                "note": note,
            }
        )
    return files


def evidence_files_to_fact_lines(evidence_files: list[dict[str, Any]]) -> list[str]:
    return [row["statement"] for row in evidence_files if row.get("statement")]


def evidence_files_to_records(article_id: str, evidence_files: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for item in evidence_files:
        meta = item["meta"]
        note_text = _clean(item.get("note"))
        mechanism_relevance = str(meta.get("mechanism_relevance") or "none").strip() or "none"
        contradiction_relevance = str(meta.get("contradiction_relevance") or "none").strip() or "none"
        rows.append(
            {
                "evidence_id": str(meta.get("evidence_id") or "").strip(),
                "article_id": article_id,
                "evidence_type": str(meta.get("kind") or "quote").strip() or "quote",
                "evidence_text": item["statement"],
                "source_span_ref": f"articles/{article_id}/source.md#{str(meta.get('evidence_id') or '').strip()}",
                "supports_claim_ids": [],
                "confidence": str(meta.get("confidence") or "medium").strip() or "medium",
                "citation": _clean(meta.get("citation")),
                "source_url": _clean(meta.get("source_url")),
                "source_excerpt": _clean(item.get("source_excerpt")),
                "note": note_text,
                "mechanism_relevance": mechanism_relevance,
                "contradiction_relevance": contradiction_relevance,
                "caveat": note_text if note_text else None,
            }
        )
    return rows


def run_synthesist_claims(*, article_id: str, source_title: str, source_url: str, findings_lines: list[str], facts_lines: list[str], evidence_records: list[dict[str, Any]], agent_id: str, timeout: int) -> dict[str, Any]:
    prompt = compose_persona_job_prompt("synthesist", "article-claims", require_job=True)
    findings_block = "\n".join(f"- {line}" for line in findings_lines) if findings_lines else "- none"
    facts_block = "\n".join(f"- fact-{index:03d}: {line}" for index, line in enumerate(facts_lines, start=1)) if facts_lines else "- none"
    evidence_block = "\n".join(
        f"- {row['evidence_id']}: {row['evidence_text']} (kind={row['evidence_type']}; mechanism_relevance={row.get('mechanism_relevance', 'none')}; contradiction_relevance={row.get('contradiction_relevance', 'none')})"
        for row in evidence_records
    ) if evidence_records else "- none"
    claim_budget = max(1, min(4, len(evidence_records) or len(findings_lines) or 1))
    claim_ids = [f"claim-{index:03d}" for index in range(1, claim_budget + 1)]
    mission = (
        f"{_mission_header(article_id, source_title, source_url)}\n"
        f"Substep: final claim drafting\n"
        f"Use only these claim ids: {', '.join(claim_ids)}\n\n"
        f"Findings:\n{findings_block}\n\n"
        f"Facts:\n{facts_block}\n\n"
        f"Evidence:\n{evidence_block}\n"
    )
    payload = _yaml_mapping(run_loose_agent(agent_id, f"{prompt}\n\n{mission}", timeout=timeout, thinking="off"))
    claims = payload.get("claims") or []
    if not isinstance(claims, list) or not claims:
        raise JobContractError("claims_missing")
    seen: set[str] = set()
    normalized: list[dict[str, Any]] = []
    evidence_ids = {row["evidence_id"] for row in evidence_records}
    for row in claims:
        if not isinstance(row, dict):
            raise JobContractError("claim_row_not_mapping")
        claim_id = str(row.get("claim_id") or "").strip()
        if claim_id not in claim_ids or claim_id in seen:
            raise JobContractError("claim_id_invalid")
        seen.add(claim_id)
        claim_text = _clean(row.get("claim_text"))
        if not claim_text:
            raise JobContractError("claim_text_missing")
        supporting_evidence_ids = [str(item).strip() for item in (row.get("evidence_ids") or []) if str(item).strip()]
        if not supporting_evidence_ids:
            raise JobContractError("claim_evidence_missing")
        if any(item not in evidence_ids for item in supporting_evidence_ids):
            raise JobContractError("claim_unknown_evidence_id")
        mechanism_or_bounds = _clean(row.get("mechanism_or_bounds"))
        contradiction_note = _clean(row.get("contradiction_note"))
        normalized.append(
            {
                "claim_id": claim_id,
                "article_id": article_id,
                "claim_text": claim_text,
                "claim_kind": str(row.get("claim_kind") or infer_claim_kind(claim_text, mechanism_or_bounds)).strip() or infer_claim_kind(claim_text, mechanism_or_bounds),
                "supporting_fact_ids": [],
                "supporting_evidence_ids": supporting_evidence_ids,
                "source_span_refs": [f"articles/{article_id}/source.md#{evidence_id}" for evidence_id in supporting_evidence_ids],
                "caveats": [contradiction_note] if contradiction_note else [],
                "confidence": str(row.get("confidence") or "medium").strip() or "medium",
                "mechanism_or_bounds": mechanism_or_bounds,
                "contradiction_note": contradiction_note,
            }
        )
    return {"summary": _clean(payload.get("summary")), "claims": normalized}


def infer_claim_kind(claim_text: str, mechanism_or_bounds: str) -> str:
    lowered = f"{claim_text}\n{mechanism_or_bounds}".lower()
    if any(token in lowered for token in ["limit", "uncertain", "unknown", "bounded", "not clear"]):
        return "bounded_claim"
    if any(token in lowered for token in ["because", "via", "through", "workflow", "mechanism"]):
        return "mechanism_claim"
    if any(token in lowered for token in ["compare", "baseline", "outperform"]):
        return "comparative_claim"
    return "empirical_claim"


def apply_claim_links(claims: list[dict[str, Any]], evidence_records: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    evidence_index = {row["evidence_id"]: dict(row) for row in evidence_records}
    linked_claims: list[dict[str, Any]] = []
    claim_ids_by_evidence: dict[str, list[str]] = {}
    for claim in claims:
        linked_claims.append(dict(claim))
        for evidence_id in claim.get("supporting_evidence_ids", []):
            claim_ids_by_evidence.setdefault(evidence_id, []).append(claim["claim_id"])
    linked_evidence: list[dict[str, Any]] = []
    for evidence_id, row in evidence_index.items():
        updated = dict(row)
        updated["supports_claim_ids"] = claim_ids_by_evidence.get(evidence_id, [])
        linked_evidence.append(updated)
    return linked_claims, linked_evidence


def claim_records_to_findings_lines(claims: list[dict[str, Any]]) -> list[str]:
    return [row["claim_text"] for row in claims if row.get("claim_text")]


def extract_last_article_document(text: str) -> str:
    cleaned = _clean(text)
    marker = "---\nversion: article.v1"
    starts: list[int] = []
    if cleaned.startswith(marker):
        starts.append(0)
    start = 0
    while True:
        idx = cleaned.find(f"\n{marker}", start)
        if idx == -1:
            break
        starts.append(idx + 1)
        start = idx + 1
    if not starts:
        return cleaned
    return cleaned[starts[-1]:].strip()


def _contains_numeric_payload(text: str) -> bool:
    cleaned = _clean(text)
    if not cleaned:
        return False
    return bool(re.search(r"\b\d+(?:\.\d+)?\s*(?:%|x|k|m|ms|s|sec|seconds?|minutes?|hours?|turns?|instances?|repos?(?:itories)?)\b", cleaned, re.I) or re.search(r"\b(?:over|under|about|around|roughly|nearly|more than|less than)\s+\d", cleaned, re.I))


def validate_article_write_body(body: str, *, claims: list[dict[str, Any]], evidence_records: list[dict[str, Any]]) -> None:
    assert_no_visible_internal_ids(body, label="article-write")
    required_sections = [
        "## Core Thesis",
        "## Why It Matters for Sapho",
        "## Key Findings",
        "## Evidence and Findings",
        "## Contradictions and Tensions",
        "## Mechanism or Bounds",
        "## Limits",
    ]
    if any(section not in body for section in required_sections):
        raise JobContractError("article_write_missing_dense_sections")
    sections = _markdown_sections(body)
    evidence_and_findings = sections.get("Evidence and Findings", "")
    key_findings = sections.get("Key Findings", "")
    contradiction_section = sections.get("Contradictions and Tensions", "")
    mechanism_section = sections.get("Mechanism or Bounds", "")
    claims_text = "\n".join(_clean(row.get("claim_text")) for row in claims if _clean(row.get("claim_text")))
    evidence_text = "\n".join(_clean(row.get("evidence_text")) for row in evidence_records if _clean(row.get("evidence_text")))
    numeric_payload_present = _contains_numeric_payload(claims_text) or _contains_numeric_payload(evidence_text)
    numeric_payload_surface = _contains_numeric_payload(evidence_and_findings) or _contains_numeric_payload(key_findings)
    if numeric_payload_present and not numeric_payload_surface:
        raise JobContractError("article_write_missing_empirical_specificity")
    weak_tension_phrases = [
        "no direct empirical contradiction is reported",
        "no direct contradiction is visible",
    ]
    weak_mechanism_phrases = [
        "the supported mechanism is limited",
        "descriptive account",
    ]
    contradiction_low = contradiction_section.lower()
    mechanism_low = mechanism_section.lower()
    if any(phrase in contradiction_low for phrase in weak_tension_phrases) and not _contains_numeric_payload(contradiction_section):
        raise JobContractError("article_write_weak_tension_or_mechanism")
    if any(phrase in mechanism_low for phrase in weak_mechanism_phrases):
        raise JobContractError("article_write_weak_tension_or_mechanism")


def run_synthesist_article_write(*, article_id: str, source_title: str, source_url: str, queued_at_utc: str, captured_at_utc: str, artifact_minted_at_utc: str, claims: list[dict[str, Any]], evidence_records: list[dict[str, Any]], agent_id: str, timeout: int) -> dict[str, Any]:
    prompt = compose_persona_job_prompt("synthesist", "article-write", require_job=True)
    claims_block = "\n".join(
        f"- {row['claim_text']} (confidence={row['confidence']}; mechanism_or_bounds={row.get('mechanism_or_bounds', '') or 'none'}; contradiction_note={row.get('contradiction_note', '') or 'none'})"
        for row in claims
    ) if claims else "- none"
    evidence_block = "\n".join(
        f"- {row['evidence_text']} (supports={', '.join(row.get('supports_claim_ids', [])) or 'none'}; mechanism_relevance={row.get('mechanism_relevance', 'none')}; contradiction_relevance={row.get('contradiction_relevance', 'none')}; caveat={row.get('note') or 'none'})"
        for row in evidence_records
    ) if evidence_records else "- none"
    mission = (
        f"Mission Context\n\n"
        f"article_id: {article_id}\n"
        f"source_title: {_clean(source_title)}\n"
        f"source_url: {_clean(source_url)}\n"
        f"queued_at_utc: {_clean(queued_at_utc)}\n"
        f"captured_at_utc: {_clean(captured_at_utc)}\n"
        f"artifact_minted_at_utc: {_clean(artifact_minted_at_utc)}\n"
        f"evidence_count: {len(evidence_records)}\n"
        f"claim_count: {len(claims)}\n\n"
        f"Approved Claims:\n{claims_block}\n\n"
        f"Evidence Context:\n{evidence_block}\n"
    )
    raw = run_loose_agent(agent_id, f"{prompt}\n\n{mission}", timeout=timeout, thinking="off")
    article_output = extract_last_article_document(raw)
    meta, body = parse_markdown(article_output)
    if str(meta.get("article_id") or "") != article_id:
        raise JobContractError("article_write_article_id_mismatch")
    validate_article_write_body(body, claims=claims, evidence_records=evidence_records)
    return {"raw": raw, "meta": meta, "body": body}


def compact_source_for_extractor(source_markdown: str) -> str:
    return source_body_text(source_markdown)
