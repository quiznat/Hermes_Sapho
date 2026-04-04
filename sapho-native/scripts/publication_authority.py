from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from common import (
    ARTICLES_DIR,
    DAILY_DIR,
    article_artifact_publication_current,
    article_file,
    publication_status,
    read_markdown,
    timestamp_for_date,
    utc_now,
)

VALIDATION_FILE = "validation.json"
HISTORICAL_POLICY_FILE = "historical-policy.json"
ARTICLE_AUTHORITY_FILE = "publication-authority.json"
DAILY_AUTHORITY_FILE = "publication-authority.json"
ARTICLE_PUBLISHABLE_STATUSES = {"ready-for-daily", "published"}


def _read_json(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def evaluate_article_publication_authority(article_id: str) -> dict[str, Any]:
    article_root = ARTICLES_DIR / article_id
    article_meta, _article_body = read_markdown(article_file(article_id))
    validation = _read_json(article_root / VALIDATION_FILE)
    historical_policy = _read_json(article_root / HISTORICAL_POLICY_FILE)

    reasons: list[str] = []
    status = publication_status(article_meta)
    if status not in ARTICLE_PUBLISHABLE_STATUSES:
        reasons.append(f"publication_status_not_publishable:{status or 'missing'}")

    validation_status = str((validation or {}).get("overall_status") or "")
    if validation_status != "pass":
        reasons.append("validation_fail")

    if historical_policy and historical_policy.get("applies") is not False:
        if not bool(historical_policy.get("current_law_eligible")):
            reasons.append("historical_policy_ineligible")

    payload = {
        "version": "publication-authority.v1",
        "scope": "article",
        "article_id": article_id,
        "evaluated_at_utc": utc_now(),
        "publication_status": status,
        "validation_status": validation_status or "missing",
        "historical_policy_status": str((historical_policy or {}).get("policy_status") or "not_applicable"),
        "verdict": "pass" if not reasons else "block",
        "reasons": reasons,
    }
    _write_json(article_root / ARTICLE_AUTHORITY_FILE, payload)
    return payload


def assert_article_publication_authority(article_id: str) -> dict[str, Any]:
    payload = evaluate_article_publication_authority(article_id)
    if payload["verdict"] != "pass":
        raise RuntimeError("publication_authority_blocked:" + ",".join(payload["reasons"]))
    return payload


def evaluate_daily_publication_authority(*, replay_date: str, article_ids: list[str], conclave_verdict: str) -> dict[str, Any]:
    reasons: list[str] = []
    article_decisions: list[dict[str, Any]] = []
    for article_id in article_ids:
        article_decision = evaluate_article_publication_authority(article_id)
        article_decisions.append(
            {
                "article_id": article_id,
                "verdict": article_decision["verdict"],
                "reasons": list(article_decision["reasons"]),
            }
        )
        if article_decision["verdict"] != "pass":
            reasons.extend(f"article_authority_blocked:{article_id}:{reason}" for reason in article_decision["reasons"])
        article_meta, _article_body = read_markdown(article_file(article_id))
        if not article_artifact_publication_current(article_meta):
            reasons.append(f"artifact_publication_not_current:{article_id}")

    normalized_verdict = str(conclave_verdict or "").strip().lower()
    if normalized_verdict != "pass":
        reasons.append(f"conclave_verdict:{normalized_verdict or 'missing'}")

    payload = {
        "version": "publication-authority.v1",
        "scope": "daily",
        "date": replay_date,
        "evaluated_at_utc": timestamp_for_date(replay_date),
        "conclave_verdict": normalized_verdict or "missing",
        "article_ids": article_ids,
        "article_decisions": article_decisions,
        "verdict": "pass" if not reasons else "block",
        "reasons": reasons,
    }
    _write_json(DAILY_DIR / replay_date / DAILY_AUTHORITY_FILE, payload)
    return payload


def assert_daily_publication_authority(*, replay_date: str, article_ids: list[str], conclave_verdict: str) -> dict[str, Any]:
    payload = evaluate_daily_publication_authority(
        replay_date=replay_date,
        article_ids=article_ids,
        conclave_verdict=conclave_verdict,
    )
    if payload["verdict"] != "pass":
        raise RuntimeError("publication_authority_blocked:" + ",".join(payload["reasons"]))
    return payload
