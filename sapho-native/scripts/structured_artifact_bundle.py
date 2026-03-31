from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from article_law_reviews import CONTRADICTION_REVIEW_FILE, MECHANISM_REVIEW_FILE, load_review_artifacts
from common import article_dir, markdown_section, utc_now
from micro_common import bullet_lines, clean_loose_text, parse_keep_discard

CURATOR_FILE = "curator.json"
FINDINGS_FILE = "findings.jsonl"
FACTS_FILE = "facts.jsonl"
CLAIMS_FILE = "claims.jsonl"
EVIDENCE_FILE = "evidence.jsonl"
LINEAGE_FILE = "lineage.json"
VALIDATION_FILE = "validation.json"

LOW = "low"
MEDIUM = "medium"
HIGH = "high"


def structured_path(article_id: str, filename: str) -> Path:
    return article_dir(article_id) / filename


def _write_json(path: Path, payload: dict[str, Any]) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return path


def _write_jsonl(path: Path, rows: list[dict[str, Any]]) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return path
    rendered = "\n".join(json.dumps(row, ensure_ascii=False) for row in rows) + "\n"
    path.write_text(rendered, encoding="utf-8")
    return path


def _clean(text: Any) -> str:
    return clean_loose_text(str(text or "")).strip()


def _slug(text: str, fallback: str) -> str:
    cleaned = re.sub(r"[^a-z0-9]+", "-", _clean(text).lower()).strip("-")
    return cleaned or fallback


def _source_span_ref(article_id: str, label: str) -> str:
    return f"articles/{article_id}/source.md#{label}"


def _article_section_ref(article_id: str, section: str) -> str:
    return f"articles/{article_id}/article.md#{section}"


def _metric_parts(text: str) -> tuple[str | None, str | None]:
    match = re.search(r"(?P<value>\d+(?:\.\d+)?)\s*(?P<unit>%|x|ms|s|sec(?:onds?)?|minutes?|hours?)\b", text, re.I)
    if not match:
        return None, None
    return match.group("value"), match.group("unit")


def _confidence_from_text(text: str, default: str = MEDIUM) -> str:
    lowered = _clean(text).lower()
    if not lowered:
        return default
    if any(token in lowered for token in ["maybe", "may", "appears", "suggest", "possible", "unclear"]):
        return LOW
    if any(token in lowered for token in ["significant", "demonstrate", "shows", "improves", "outperforms", "measured"]):
        return HIGH
    return default


def _qualified_by(reason: str, decision: str) -> str:
    lowered = reason.lower()
    if decision != "kept":
        return "none"
    if "novel" in lowered and "synthesis" in lowered:
        return "novel_synthesis"
    if "novel" in lowered and any(token in lowered for token in ["finding", "result", "benchmark", "experiment"]):
        return "novel_findings"
    if "production" in lowered:
        return "production_blog"
    if any(token in lowered for token in ["survey", "comparative"]):
        return "comparative_survey"
    if any(token in lowered for token in ["vendor", "framework", "technical"]):
        return "vendor_technical_results"
    if any(token in lowered for token in ["experiment", "benchmark", "paper", "study"]):
        return "experimental_blog"
    return "novel_synthesis"


def _evidence_basis(reason: str, findings: list[str], facts: list[str]) -> str:
    lowered = "\n".join([reason, *findings, *facts]).lower()
    kinds = set()
    if any(token in lowered for token in ["benchmark", "single-shot", "%", "accuracy", "reliability", "outperform"]):
        kinds.add("benchmark")
    if any(token in lowered for token in ["experiment", "measured", "evaluation", "tested"]):
        kinds.add("experiment")
    if any(token in lowered for token in ["production", "repository", "real-world"]):
        kinds.add("production")
    if any(token in lowered for token in ["survey", "compare", "synthesis", "framework"]):
        kinds.add("synthesis")
    if not kinds:
        return "none"
    if len(kinds) > 1:
        return "mixed"
    return next(iter(kinds))


def build_curator_record(article_id: str, worthiness_text: str, mode: str) -> dict[str, Any]:
    cleaned = _clean(worthiness_text)
    reason = ""
    try:
        decision, remainder = parse_keep_discard(cleaned)
        reason = _clean(remainder)
    except ValueError:
        decision = "discarded" if "discard" in cleaned.lower() else "kept"
        reason = cleaned
    limits = ""
    if "limits:" in reason.lower():
        prefix, suffix = re.split(r"limits:\s*", reason, maxsplit=1, flags=re.I)
        reason = _clean(prefix)
        limits = _clean(suffix)
    excerpt_sufficiency = "partial" if limits else "sufficient"
    if any(token in (reason + "\n" + limits).lower() for token in ["abstract-only", "metadata only", "partial", "not contain the full", "consult the full paper"]):
        excerpt_sufficiency = "partial"
    if any(token in (reason + "\n" + limits).lower() for token in ["insufficient", "unusable", "no usable"]):
        excerpt_sufficiency = "insufficient"
    novelty_strength = _confidence_from_text(reason, default=MEDIUM)
    return {
        "version": "curator-decision.v1",
        "article_id": article_id,
        "decision": decision,
        "qualified_by": _qualified_by(reason, decision),
        "evidence_basis": "none",
        "novelty_strength": novelty_strength,
        "excerpt_sufficiency": excerpt_sufficiency,
        "reason": reason,
        "limits": limits,
        "confidence": _confidence_from_text(cleaned, default=MEDIUM),
        "generated_at_utc": utc_now(),
        "mode": mode or "agent",
    }


def build_findings_records(article_id: str, findings_text: str) -> list[dict[str, Any]]:
    findings = bullet_lines(findings_text)
    rows: list[dict[str, Any]] = []
    for index, finding in enumerate(findings, start=1):
        lowered = finding.lower()
        if any(token in lowered for token in ["limit", "caveat", "however", "but "]):
            finding_type = "caveat"
        elif any(token in lowered for token in ["because", "via", "through", "mechanism", "workflow"]):
            finding_type = "mechanism_hint"
        elif any(token in lowered for token in ["could", "may", "implication", "suggests", "shift how"]):
            finding_type = "implication"
        else:
            finding_type = "result"
        rows.append(
            {
                "finding_id": f"finding-{index:03d}",
                "article_id": article_id,
                "finding_text": finding,
                "finding_type": finding_type,
                "priority": HIGH if index == 1 else MEDIUM,
                "source_span_ref": _source_span_ref(article_id, f"finding-{index:03d}"),
                "confidence": _confidence_from_text(finding, default=MEDIUM),
            }
        )
    return rows


def build_fact_records(article_id: str, facts_text: str) -> list[dict[str, Any]]:
    facts = bullet_lines(facts_text)
    rows: list[dict[str, Any]] = []
    for index, fact in enumerate(facts, start=1):
        lowered = fact.lower()
        if any(token in lowered for token in ["benchmark", "accuracy", "success rate", "outperform", "%", "x", "f1", "auc"]):
            fact_type = "benchmark_result"
        elif any(token in lowered for token in ["experiment", "tested", "evaluation"]):
            fact_type = "experiment_result"
        elif any(token in lowered for token in ["repository", "production", "deployed", "real-world"]):
            fact_type = "production_observation"
        elif any(token in lowered for token in ["dataset", "corpus"]):
            fact_type = "dataset_detail"
        elif any(token in lowered for token in ["model", "llm", "gpt", "claude"]):
            fact_type = "model_detail"
        elif any(token in lowered for token in ["method", "workflow", "pipeline", "uses", "combines"]):
            fact_type = "methodological_detail"
        elif any(token in lowered for token in ["limit", "caveat", "however"]):
            fact_type = "caveat"
        else:
            fact_type = "other"
        metric_value, metric_unit = _metric_parts(fact)
        caveat = fact if fact_type == "caveat" else None
        rows.append(
            {
                "fact_id": f"fact-{index:03d}",
                "article_id": article_id,
                "fact_text": fact,
                "fact_type": fact_type,
                "metric_value": metric_value,
                "metric_unit": metric_unit,
                "source_span_ref": _source_span_ref(article_id, f"fact-{index:03d}"),
                "confidence": _confidence_from_text(fact, default=MEDIUM),
                "caveat": caveat,
            }
        )
    return rows


def build_claim_records(article_id: str, findings: list[dict[str, Any]], facts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    fact_ids = [row["fact_id"] for row in facts]
    for index, finding in enumerate(findings, start=1):
        finding_type = finding["finding_type"]
        if finding_type == "caveat":
            claim_kind = "limitation_claim"
        elif finding_type == "mechanism_hint":
            claim_kind = "mechanism_claim"
        elif finding_type == "implication":
            claim_kind = "implication_claim"
        elif any(token in finding["finding_text"].lower() for token in ["compare", "baseline", "outperform"]):
            claim_kind = "comparative_claim"
        elif index == 1:
            claim_kind = "topline_judgment"
        else:
            claim_kind = "empirical_claim"
        linked_fact_ids = []
        if fact_ids:
            linked_fact_ids.append(fact_ids[min(index - 1, len(fact_ids) - 1)])
        rows.append(
            {
                "claim_id": f"claim-{index:03d}",
                "article_id": article_id,
                "claim_text": finding["finding_text"],
                "claim_kind": claim_kind,
                "supporting_fact_ids": linked_fact_ids,
                "supporting_evidence_ids": [],
                "source_span_refs": [finding["source_span_ref"]],
                "caveats": [finding["finding_text"]] if claim_kind == "limitation_claim" else [],
                "confidence": finding["confidence"],
            }
        )
    return rows


def build_evidence_records(article_id: str, facts: list[dict[str, Any]], claims: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    claim_by_fact: dict[str, list[str]] = {}
    for claim in claims:
        for fact_id in claim.get("supporting_fact_ids", []):
            claim_by_fact.setdefault(fact_id, []).append(claim["claim_id"])

    for index, fact in enumerate(facts, start=1):
        fact_type = fact["fact_type"]
        if fact_type in {"benchmark_result", "experiment_result"}:
            evidence_type = "result"
        elif fact_type == "methodological_detail":
            evidence_type = "method"
        elif fact_type == "caveat":
            evidence_type = "caveat"
        elif fact_type == "other" and fact.get("metric_value"):
            evidence_type = "metric"
        else:
            evidence_type = "quote"
        rows.append(
            {
                "evidence_id": f"evidence-{index:03d}",
                "article_id": article_id,
                "evidence_type": evidence_type,
                "evidence_text": fact["fact_text"],
                "source_span_ref": fact["source_span_ref"],
                "supports_claim_ids": claim_by_fact.get(fact["fact_id"], []),
                "confidence": fact["confidence"],
            }
        )
    return rows


def attach_evidence_ids(claims: list[dict[str, Any]], evidence: list[dict[str, Any]]) -> list[dict[str, Any]]:
    evidence_by_claim: dict[str, list[str]] = {}
    for row in evidence:
        for claim_id in row.get("supports_claim_ids", []):
            evidence_by_claim.setdefault(claim_id, []).append(row["evidence_id"])
    patched: list[dict[str, Any]] = []
    for claim in claims:
        updated = dict(claim)
        updated["supporting_evidence_ids"] = evidence_by_claim.get(claim["claim_id"], [])
        patched.append(updated)
    return patched


def build_lineage(article_id: str, article_body: str, claims: list[dict[str, Any]], facts: list[dict[str, Any]], evidence: list[dict[str, Any]]) -> dict[str, Any]:
    claim_ids = [row["claim_id"] for row in claims]
    limitation_claim_ids = [row["claim_id"] for row in claims if row["claim_kind"] == "limitation_claim"]
    mechanism_claim_ids = [row["claim_id"] for row in claims if row["claim_kind"] == "mechanism_claim"]
    key_findings_text = markdown_section(article_body, "## Key Findings")
    limits_text = markdown_section(article_body, "## Limits")
    summary_sections = {
        "core_thesis": claim_ids[:1],
        "why_it_matters": claim_ids[:1],
        "key_findings": claim_ids if key_findings_text else [],
        "limits": limitation_claim_ids if limitation_claim_ids else ([claim_ids[-1]] if claim_ids and limits_text else []),
    }
    unresolved_gaps: list[str] = []
    if not markdown_section(article_body, "## Core Thesis"):
        unresolved_gaps.append("missing_core_thesis_section")
    if not markdown_section(article_body, "## Why It Matters"):
        unresolved_gaps.append("missing_why_it_matters_section")
    if not key_findings_text:
        unresolved_gaps.append("missing_key_findings_section")
    if not limits_text:
        unresolved_gaps.append("missing_limits_section")
    if not mechanism_claim_ids:
        unresolved_gaps.append("missing_explicit_mechanism_claim")
    return {
        "version": "article-lineage.v1",
        "article_id": article_id,
        "summary_sections": summary_sections,
        "claim_ids": claim_ids,
        "fact_ids": [row["fact_id"] for row in facts],
        "evidence_ids": [row["evidence_id"] for row in evidence],
        "unresolved_gaps": unresolved_gaps,
    }


def _check(status: str, detail: str, **extra: Any) -> dict[str, Any]:
    payload = {"status": status, "detail": detail}
    payload.update(extra)
    return payload


def build_validation(article_id: str, article_meta: dict[str, Any], article_body: str, curator: dict[str, Any], findings: list[dict[str, Any]], facts: list[dict[str, Any]], claims: list[dict[str, Any]], evidence: list[dict[str, Any]], lineage: dict[str, Any]) -> dict[str, Any]:
    publication_state = str(article_meta.get("publication_status") or "")
    is_kept = curator["decision"] == "kept"
    requires_full_bundle = is_kept and publication_state not in {"discarded", "capture-blocked", "duplicate-rejected"}
    required_sections = [
        "## Core Thesis",
        "## Why It Matters",
        "## Key Findings",
        "## Limits",
    ]
    missing_sections = [section for section in required_sections if section not in article_body]
    completeness_failures: list[str] = []
    if requires_full_bundle and not findings:
        completeness_failures.append("missing_findings")
    if requires_full_bundle and not facts:
        completeness_failures.append("missing_facts")
    if requires_full_bundle and not claims:
        completeness_failures.append("missing_claims")
    if requires_full_bundle and not evidence:
        completeness_failures.append("missing_evidence")
    if requires_full_bundle and missing_sections:
        completeness_failures.append("missing_article_sections")
    if completeness_failures:
        completeness = _check("fail", ", ".join(completeness_failures), missing_sections=missing_sections)
    else:
        completeness = _check("pass", "required structured bundle outputs present", missing_sections=[])

    publication_state = str(article_meta.get("publication_status") or "")
    if publication_state == "duplicate-rejected":
        duplicate_conflict = _check(
            "pass",
            "duplicate conflict explicitly recorded and package blocked from publication",
            duplicate_of_article_id=str(article_meta.get("duplicate_of_article_id") or ""),
        )
    else:
        duplicate_conflict = _check("pass", "no duplicate conflict recorded")

    linkage_failures: list[str] = []
    fact_ids = {row["fact_id"] for row in facts}
    evidence_ids = {row["evidence_id"] for row in evidence}
    for claim in claims:
        if any(fact_id not in fact_ids for fact_id in claim.get("supporting_fact_ids", [])):
            linkage_failures.append(f"claim_missing_fact_ref:{claim['claim_id']}")
        if any(evidence_id not in evidence_ids for evidence_id in claim.get("supporting_evidence_ids", [])):
            linkage_failures.append(f"claim_missing_evidence_ref:{claim['claim_id']}")
        if not claim.get("source_span_refs"):
            linkage_failures.append(f"claim_missing_source_ref:{claim['claim_id']}")
    for row in evidence:
        if not row.get("source_span_ref"):
            linkage_failures.append(f"evidence_missing_source_ref:{row['evidence_id']}")
    citation_linkage = _check("fail", ", ".join(linkage_failures)) if linkage_failures else _check("pass", "claim and evidence references resolve")

    lineage_failures: list[str] = []
    claim_ids = {row["claim_id"] for row in claims}
    for section_name, section_claim_ids in lineage.get("summary_sections", {}).items():
        if any(claim_id not in claim_ids for claim_id in section_claim_ids):
            lineage_failures.append(f"unknown_claim_in_section:{section_name}")
    if requires_full_bundle and not lineage.get("summary_sections", {}).get("key_findings"):
        lineage_failures.append("missing_key_findings_lineage")
    lineage_baseline = _check("fail", ", ".join(lineage_failures)) if lineage_failures else _check("pass", "lineage summary resolves to known claim ids")

    review_artifacts = load_review_artifacts(article_id)
    contradiction_review = review_artifacts.get(CONTRADICTION_REVIEW_FILE) or {}
    if requires_full_bundle:
        if contradiction_review:
            contradiction_baseline = _check(
                "pass",
                "contradiction review artifact present",
                contradiction_count=int(contradiction_review.get("contradiction_count") or 0),
                review_status=str(contradiction_review.get("status") or ""),
            )
        else:
            contradiction_baseline = _check("fail", "contradiction review artifact missing for eligible package")
    else:
        contradiction_baseline = _check("pass", "not applicable for blocked/discarded package")

    mechanism_review = review_artifacts.get(MECHANISM_REVIEW_FILE) or {}
    if requires_full_bundle:
        if mechanism_review:
            mechanism_baseline = _check(
                "pass",
                "mechanism review artifact present",
                mechanism_count=int(mechanism_review.get("mechanism_count") or 0),
                bounded_claim_count=int(mechanism_review.get("bounded_claim_count") or 0),
                review_status=str(mechanism_review.get("status") or ""),
            )
        else:
            mechanism_baseline = _check("fail", "mechanism review artifact missing for eligible package")
    else:
        mechanism_baseline = _check("pass", "not applicable for blocked/discarded package")

    checks = {
        "completeness": completeness,
        "duplicate_conflict": duplicate_conflict,
        "citation_linkage": citation_linkage,
        "lineage_baseline": lineage_baseline,
        "contradiction_baseline": contradiction_baseline,
        "mechanism_baseline": mechanism_baseline,
    }
    statuses = [row["status"] for row in checks.values()]
    overall_status = "fail" if "fail" in statuses else "warn" if "warn" in statuses else "pass"
    return {
        "version": "article-validation.v1",
        "article_id": article_id,
        "validated_at_utc": utc_now(),
        "checks": checks,
        "overall_status": overall_status,
    }


def materialize_article_structured_bundle(*, article_id: str, article_meta: dict[str, Any], article_body: str, worthiness_text: str, findings_text: str = "", facts_text: str = "", claims_records: list[dict[str, Any]] | None = None, evidence_records: list[dict[str, Any]] | None = None) -> dict[str, Any]:
    curator = build_curator_record(article_id, worthiness_text, str(article_meta.get("curator_mode") or "agent"))
    findings = build_findings_records(article_id, findings_text) if curator["decision"] == "kept" else []
    facts = build_fact_records(article_id, facts_text) if curator["decision"] == "kept" else []
    curator["evidence_basis"] = _evidence_basis(curator.get("reason", ""), [row["finding_text"] for row in findings], [row["fact_text"] for row in facts])
    claims = [dict(row) for row in claims_records] if claims_records is not None else (build_claim_records(article_id, findings, facts) if curator["decision"] == "kept" else [])
    evidence = [dict(row) for row in evidence_records] if evidence_records is not None else (build_evidence_records(article_id, facts, claims) if curator["decision"] == "kept" else [])
    if claims_records is None:
        claims = attach_evidence_ids(claims, evidence)
    lineage = build_lineage(article_id, article_body, claims, facts, evidence)
    validation = build_validation(article_id, article_meta, article_body, curator, findings, facts, claims, evidence, lineage)

    paths = {
        CURATOR_FILE: str(_write_json(structured_path(article_id, CURATOR_FILE), curator)),
        FINDINGS_FILE: str(_write_jsonl(structured_path(article_id, FINDINGS_FILE), findings)),
        FACTS_FILE: str(_write_jsonl(structured_path(article_id, FACTS_FILE), facts)),
        CLAIMS_FILE: str(_write_jsonl(structured_path(article_id, CLAIMS_FILE), claims)),
        EVIDENCE_FILE: str(_write_jsonl(structured_path(article_id, EVIDENCE_FILE), evidence)),
        LINEAGE_FILE: str(_write_json(structured_path(article_id, LINEAGE_FILE), lineage)),
        VALIDATION_FILE: str(_write_json(structured_path(article_id, VALIDATION_FILE), validation)),
    }
    return {
        "article_id": article_id,
        "paths": paths,
        "claim_count": len(claims),
        "evidence_count": len(evidence),
        "finding_count": len(findings),
        "fact_count": len(facts),
        "validation_status": validation["overall_status"],
    }
