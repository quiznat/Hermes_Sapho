#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from common import ARTICLES_DIR, read_markdown
from structured_artifact_bundle import materialize_article_structured_bundle


VALIDATION_FILE = "validation.json"


def _read_optional(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def _load_validation(path: Path) -> dict | None:
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


def validate_article(article_id: str, *, refresh: bool = False) -> dict:
    article_root = ARTICLES_DIR / article_id
    article_meta, article_body = read_markdown(article_root / "article.md")
    validation_path = article_root / VALIDATION_FILE
    validation = _load_validation(validation_path)

    if refresh or validation is None:
        materialized = materialize_article_structured_bundle(
            article_id=article_id,
            article_meta=article_meta,
            article_body=article_body,
            worthiness_text=_read_optional(article_root / "micro-worthiness.md"),
            findings_text=_read_optional(article_root / "micro-findings.md"),
            facts_text=_read_optional(article_root / "micro-facts.md"),
        )
        validation = _load_validation(validation_path) or {
            "article_id": article_id,
            "overall_status": materialized["validation_status"],
            "checks": {},
        }

    checks = validation.get("checks", {})
    return {
        "article_id": article_id,
        "publication_status": str(article_meta.get("publication_status") or ""),
        "overall_status": validation.get("overall_status", "fail"),
        "warn_checks": sorted(name for name, row in checks.items() if row.get("status") == "warn"),
        "fail_checks": sorted(name for name, row in checks.items() if row.get("status") == "fail"),
    }


def iter_article_ids(limit: int | None = None) -> list[str]:
    article_ids = sorted(path.name for path in ARTICLES_DIR.glob("art-*") if path.is_dir() and (path / "article.md").exists())
    if limit is not None:
        return article_ids[:limit]
    return article_ids


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--article-id", action="append", dest="article_ids")
    parser.add_argument("--limit", type=int)
    parser.add_argument("--refresh", action="store_true")
    parser.add_argument("--fail-on-fail", action="store_true")
    args = parser.parse_args()

    rows = [validate_article(article_id, refresh=args.refresh) for article_id in (args.article_ids or iter_article_ids(limit=args.limit))]
    summary = {
        "mode": "report" if not args.fail_on_fail else "fail-on-fail",
        "article_count": len(rows),
        "status_counts": {
            "pass": sum(1 for row in rows if row["overall_status"] == "pass"),
            "warn": sum(1 for row in rows if row["overall_status"] == "warn"),
            "fail": sum(1 for row in rows if row["overall_status"] == "fail"),
        },
        "articles_with_warns": [row for row in rows if row["warn_checks"]],
        "articles_with_fails": [row for row in rows if row["fail_checks"]],
    }
    print(json.dumps(summary, indent=2))
    if args.fail_on_fail and summary["status_counts"]["fail"]:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
