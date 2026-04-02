#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

from common import ARTICLES_DIR, QUEUE_DIR, ROOT, article_file, read_markdown, ticket_path, timestamp_for_date, utc_now

REPORTS_DIR = ROOT / "state" / "reports"
TARGET_POLICY_STATUSES = {"legacy_quarantined", "current_law_compliant"}


def _read_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def historical_policy_path(article_id: str) -> Path:
    return ARTICLES_DIR / article_id / "historical-policy.json"


def select_candidate_article_ids(limit: int | None = None) -> list[str]:
    candidates: list[str] = []
    for path in sorted(ARTICLES_DIR.glob("art-*/article.md")):
        article_id = path.parent.name
        meta, _body = read_markdown(path)
        if not str(meta.get("imported_from_runtime_article_id") or "").strip():
            continue
        policy = _read_json(historical_policy_path(article_id))
        policy_status = str(policy.get("policy_status") or "")
        if policy_status not in TARGET_POLICY_STATUSES:
            continue
        candidates.append(article_id)
        if limit is not None and len(candidates) >= limit:
            break
    return candidates


def remediation_command(article_id: str, replay_date: str | None = None) -> list[str]:
    cmd = [
        sys.executable,
        str(ROOT / "scripts" / "run_micro_article_lane.py"),
        "--article-id",
        article_id,
    ]
    if replay_date:
        cmd.extend(["--replay-date", replay_date])
    return cmd


def remediate_article(article_id: str, replay_date: str | None = None) -> dict[str, Any]:
    before_meta, _before_body = read_markdown(article_file(article_id))
    before_policy = _read_json(historical_policy_path(article_id))
    ticket_id = str(before_meta.get("ticket_id") or "")
    if ticket_id and not ticket_path(ticket_id).exists():
        raise FileNotFoundError(f"missing_ticket:{ticket_id}")

    cmd = remediation_command(article_id, replay_date=replay_date)
    completed = subprocess.run(cmd, check=False, cwd=str(ROOT), text=True, capture_output=True)

    after_meta, _after_body = read_markdown(article_file(article_id))
    after_policy = _read_json(historical_policy_path(article_id))
    status = "ok" if completed.returncode == 0 else "error"
    return {
        "article_id": article_id,
        "status": status,
        "command": cmd,
        "return_code": completed.returncode,
        "stdout": completed.stdout,
        "stderr": completed.stderr,
        "before_publication_status": str(before_meta.get("publication_status") or ""),
        "after_publication_status": str(after_meta.get("publication_status") or ""),
        "before_policy_status": str(before_policy.get("policy_status") or "missing"),
        "after_policy_status": str(after_policy.get("policy_status") or "missing"),
        "published_artifact": False,
    }


def write_report(summary: dict[str, Any]) -> Path:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    path = REPORTS_DIR / f"historical-remediation-{utc_now().replace(':', '').replace('-', '')}.json"
    path.write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return path


def remediate_articles(article_ids: list[str], replay_date: str | None = None) -> dict[str, Any]:
    rows = [remediate_article(article_id, replay_date=replay_date) for article_id in article_ids]
    summary = {
        "generated_at_utc": utc_now(),
        "replay_date": replay_date,
        "article_count": len(rows),
        "articles": rows,
        "status_counts": {
            "ok": sum(1 for row in rows if row["status"] == "ok"),
            "error": sum(1 for row in rows if row["status"] == "error"),
        },
    }
    report_path = write_report(summary)
    summary["report_path"] = str(report_path)
    report_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return summary


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--article-id", action="append", dest="article_ids")
    parser.add_argument("--limit", type=int)
    parser.add_argument("--replay-date")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    article_ids = args.article_ids or select_candidate_article_ids(limit=args.limit)
    if args.dry_run:
        print(json.dumps({"article_count": len(article_ids), "article_ids": article_ids}, indent=2))
        return 0
    summary = remediate_articles(article_ids, replay_date=args.replay_date)
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
