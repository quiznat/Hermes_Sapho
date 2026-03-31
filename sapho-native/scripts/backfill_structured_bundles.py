#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from common import ARTICLES_DIR, read_markdown
from structured_artifact_bundle import materialize_article_structured_bundle


def _read_optional(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def backfill_article(article_id: str) -> dict:
    article_root = ARTICLES_DIR / article_id
    article_meta, article_body = read_markdown(article_root / "article.md")
    result = materialize_article_structured_bundle(
        article_id=article_id,
        article_meta=article_meta,
        article_body=article_body,
        worthiness_text=_read_optional(article_root / "micro-worthiness.md"),
        findings_text=_read_optional(article_root / "micro-findings.md"),
        facts_text=_read_optional(article_root / "micro-facts.md"),
    )
    return result


def iter_article_ids(limit: int | None = None) -> list[str]:
    article_ids = sorted(path.name for path in ARTICLES_DIR.glob("art-*") if path.is_dir() and (path / "article.md").exists())
    if limit is not None:
        return article_ids[:limit]
    return article_ids


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--article-id", action="append", dest="article_ids")
    parser.add_argument("--limit", type=int)
    args = parser.parse_args()

    article_ids = args.article_ids or iter_article_ids(limit=args.limit)
    results = []
    for article_id in article_ids:
        results.append(backfill_article(article_id))

    summary = {
        "article_count": len(results),
        "articles": results,
        "validation_status_counts": {
            "pass": sum(1 for row in results if row["validation_status"] == "pass"),
            "warn": sum(1 for row in results if row["validation_status"] == "warn"),
            "fail": sum(1 for row in results if row["validation_status"] == "fail"),
        },
    }
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
