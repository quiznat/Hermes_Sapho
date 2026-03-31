#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from article_law_reviews import write_contradiction_review, write_mechanism_review
from common import read_markdown


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--article-id", required=True)
    args = parser.parse_args()

    article_root = Path("articles") / args.article_id
    article_meta, article_body = read_markdown(article_root / "article.md")
    findings_text = (article_root / "micro-findings.md").read_text(encoding="utf-8") if (article_root / "micro-findings.md").exists() else ""
    facts_text = (article_root / "micro-facts.md").read_text(encoding="utf-8") if (article_root / "micro-facts.md").exists() else ""

    contradiction = write_contradiction_review(args.article_id, article_meta, article_body, findings_text, facts_text)
    mechanism = write_mechanism_review(args.article_id, article_meta, article_body, findings_text, facts_text)

    print(
        json.dumps(
            {
                "article_id": args.article_id,
                "contradiction_review": contradiction["review"],
                "mechanism_review": mechanism["review"],
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
