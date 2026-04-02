from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

import yaml

from common import article_dir, compose_persona_job_prompt, utc_now
from micro_common import bullet_lines, clean_loose_text, run_loose_agent

CONTRADICTIONS_FILE = "contradictions.jsonl"
MECHANISMS_FILE = "mechanisms.jsonl"
CONTRADICTION_REVIEW_FILE = "contradiction-review.json"
MECHANISM_REVIEW_FILE = "mechanism-review.json"


def _known_evidence_ids(evidence_records: list[dict[str, Any]] | None) -> set[str]:
    return {
        str(row.get("evidence_id") or "").strip()
        for row in (evidence_records or [])
        if str(row.get("evidence_id") or "").strip()
    }


def _clean(text: Any) -> str:
    return clean_loose_text(str(text or "")).strip()


def _write_json(path: Path, payload: dict[str, Any]) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return path


def _write_jsonl(path: Path, rows: list[dict[str, Any]]) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return path
    path.write_text("\n".join(json.dumps(row, ensure_ascii=False) for row in rows) + "\n", encoding="utf-8")
    return path


def _quote_yaml_scalar_values(text: str) -> str:
    rendered: list[str] = []
    scalar_patterns = [
        re.compile(r"^(\s*[A-Za-z0-9_]+:\s)(.+)$"),
        re.compile(r"^(\s*-\s*[A-Za-z0-9_]+:\s)(.+)$"),
    ]
    for line in text.splitlines():
        match = None
        for pattern in scalar_patterns:
            match = pattern.match(line)
            if match:
                break
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


def _load_yaml_payload(text: str) -> dict[str, Any]:
    cleaned = _clean(text)
    try:
        payload = yaml.safe_load(cleaned) or {}
    except yaml.YAMLError:
        payload = yaml.safe_load(_quote_yaml_scalar_values(cleaned)) or {}
    if not isinstance(payload, dict):
        raise ValueError("review_output_not_mapping")
    return payload


def _article_path(article_id: str, filename: str) -> Path:
    return article_dir(article_id) / filename


def _mission_context(
    article_id: str,
    article_meta: dict[str, Any],
    article_body: str,
    findings_text: str,
    facts_text: str,
    claims_records: list[dict[str, Any]] | None = None,
    evidence_records: list[dict[str, Any]] | None = None,
) -> str:
    findings = bullet_lines(findings_text)
    facts = bullet_lines(facts_text)
    findings_block = "\n".join(f"- {row}" for row in findings) if findings else "- none"
    facts_block = "\n".join(f"- fact-{index:03d}: {row}" for index, row in enumerate(facts, start=1)) if facts else "- none"
    claims = claims_records or []
    evidence = evidence_records or []
    claims_block = "\n".join(
        f"- {row.get('claim_id', 'claim-unknown')}: {_clean(row.get('claim_text'))} (supports={', '.join(str(item).strip() for item in (row.get('supporting_evidence_ids') or []) if str(item).strip()) or 'none'}; mechanism_or_bounds={_clean(row.get('mechanism_or_bounds')) or 'none'}; contradiction_note={_clean(row.get('contradiction_note')) or 'none'})"
        for row in claims
        if _clean(row.get('claim_text'))
    ) if claims else "- none"
    evidence_block = "\n".join(
        f"- {row.get('evidence_id', 'evidence-unknown')}: {_clean(row.get('evidence_text'))} (kind={_clean(row.get('evidence_type')) or 'quote'}; mechanism_relevance={_clean(row.get('mechanism_relevance')) or 'none'}; contradiction_relevance={_clean(row.get('contradiction_relevance')) or 'none'}; note={_clean(row.get('note')) or 'none'})"
        for row in evidence
        if _clean(row.get('evidence_text'))
    ) if evidence else "- none"
    return (
        f"Mission Context\n\n"
        f"article_id: {article_id}\n"
        f"source_title: {_clean(article_meta.get('source_title') or '')}\n"
        f"source_url: {_clean(article_meta.get('source_url') or '')}\n\n"
        f"Findings:\n{findings_block}\n\n"
        f"Facts:\n{facts_block}\n\n"
        f"Claims:\n{claims_block}\n\n"
        f"Evidence:\n{evidence_block}\n\n"
        f"Article Draft:\n\n{_clean(article_body)}\n"
    )


def _run_review(
    persona: str,
    job: str,
    article_id: str,
    article_meta: dict[str, Any],
    article_body: str,
    findings_text: str,
    facts_text: str,
    claims_records: list[dict[str, Any]] | None = None,
    evidence_records: list[dict[str, Any]] | None = None,
    *,
    timeout: int = 180,
) -> dict[str, Any]:
    prompt = compose_persona_job_prompt(persona, job, require_job=True)
    mission = _mission_context(article_id, article_meta, article_body, findings_text, facts_text, claims_records, evidence_records)
    raw = run_loose_agent(persona, f"{prompt}\n\n{mission}", timeout=timeout, thinking="off")
    return _load_yaml_payload(raw)


def write_contradiction_review(
    article_id: str,
    article_meta: dict[str, Any],
    article_body: str,
    findings_text: str,
    facts_text: str,
    claims_records: list[dict[str, Any]] | None = None,
    evidence_records: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    payload = _run_review("synthesist", "article-contradiction", article_id, article_meta, article_body, findings_text, facts_text, claims_records, evidence_records)
    contradictions = payload.get("contradictions") or []
    if not isinstance(contradictions, list):
        raise ValueError("contradictions_not_list")
    known_evidence_ids = _known_evidence_ids(evidence_records)
    rows: list[dict[str, Any]] = []
    for index, row in enumerate(contradictions, start=1):
        if not isinstance(row, dict):
            continue
        related_evidence_ids = [str(item).strip() for item in (row.get("related_evidence_ids") or []) if str(item).strip()]
        if any(item not in known_evidence_ids for item in related_evidence_ids):
            raise ValueError("unknown_related_evidence_id")
        rows.append(
            {
                "contradiction_id": f"contradiction-{index:03d}",
                "article_id": article_id,
                "contradiction_text": _clean(row.get("contradiction_text")),
                "related_claim_texts": [str(item).strip() for item in (row.get("related_claim_texts") or []) if str(item).strip()],
                "related_fact_refs": [str(item).strip() for item in (row.get("related_fact_refs") or []) if str(item).strip()],
                "related_evidence_ids": related_evidence_ids,
                "disposition": _clean(row.get("disposition") or "unresolved") or "unresolved",
                "disclosure": _clean(row.get("disclosure")),
                "confidence": _clean(row.get("confidence") or "medium") or "medium",
            }
        )
    review = {
        "version": "contradiction-review.v1",
        "article_id": article_id,
        "reviewed_at_utc": utc_now(),
        "reviewer_role": "Synthesist",
        "summary": _clean(payload.get("summary")),
        "review_confidence": _clean(payload.get("review_confidence") or "medium") or "medium",
        "contradiction_count": len(rows),
        "status": "clean" if not rows else "disclosed",
    }
    _write_json(_article_path(article_id, CONTRADICTION_REVIEW_FILE), review)
    _write_jsonl(_article_path(article_id, CONTRADICTIONS_FILE), rows)
    return {"review": review, "rows": rows}


def write_mechanism_review(
    article_id: str,
    article_meta: dict[str, Any],
    article_body: str,
    findings_text: str,
    facts_text: str,
    claims_records: list[dict[str, Any]] | None = None,
    evidence_records: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    payload = _run_review("synthesist", "article-mechanism", article_id, article_meta, article_body, findings_text, facts_text, claims_records, evidence_records)
    mechanisms = payload.get("mechanisms") or []
    bounded_claims = payload.get("bounded_claims") or []
    if not isinstance(mechanisms, list):
        raise ValueError("mechanisms_not_list")
    if not isinstance(bounded_claims, list):
        raise ValueError("bounded_claims_not_list")
    known_evidence_ids = _known_evidence_ids(evidence_records)
    rows: list[dict[str, Any]] = []
    for index, row in enumerate(mechanisms, start=1):
        if not isinstance(row, dict):
            continue
        evidence_ids = [str(item).strip() for item in (row.get("evidence_ids") or []) if str(item).strip()]
        if any(item not in known_evidence_ids for item in evidence_ids):
            raise ValueError("unknown_mechanism_evidence_id")
        rows.append(
            {
                "mechanism_id": f"mechanism-{index:03d}",
                "article_id": article_id,
                "claim_text": _clean(row.get("claim_text")),
                "evidence_ids": evidence_ids,
                "mechanism_text": _clean(row.get("mechanism_text")),
                "bounds": _clean(row.get("bounds")),
                "confidence": _clean(row.get("confidence") or "medium") or "medium",
            }
        )
    bounded_rows = []
    for row in bounded_claims:
        if not isinstance(row, dict):
            continue
        claim_text = _clean(row.get("claim_text"))
        bounds = _clean(row.get("bounds"))
        if claim_text or bounds:
            bounded_rows.append({"claim_text": claim_text, "bounds": bounds})
    review = {
        "version": "mechanism-review.v1",
        "article_id": article_id,
        "reviewed_at_utc": utc_now(),
        "reviewer_role": "Synthesist",
        "summary": _clean(payload.get("summary")),
        "review_confidence": _clean(payload.get("review_confidence") or "medium") or "medium",
        "mechanism_count": len(rows),
        "bounded_claim_count": len(bounded_rows),
        "status": "explained" if rows else "bounded" if bounded_rows else "missing",
        "bounded_claims": bounded_rows,
    }
    _write_json(_article_path(article_id, MECHANISM_REVIEW_FILE), review)
    _write_jsonl(_article_path(article_id, MECHANISMS_FILE), rows)
    return {"review": review, "rows": rows}


def load_review_artifacts(article_id: str) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for filename in [CONTRADICTION_REVIEW_FILE, MECHANISM_REVIEW_FILE]:
        path = _article_path(article_id, filename)
        if path.exists():
            try:
                result[filename] = json.loads(path.read_text(encoding="utf-8"))
            except Exception:
                result[filename] = None
    return result
