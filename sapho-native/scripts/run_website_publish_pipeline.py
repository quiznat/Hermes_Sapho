from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

from common import ARTICLES_DIR, article_artifact_publication_current, read_markdown

ROOT = Path(__file__).resolve().parents[1]
PUBLISH_SCRIPT = ROOT / "scripts" / "run_micro_artifact_publish.py"
DEFAULT_BASE_URL = "https://research.quiznat.com"
DEFAULT_CUSTOM_DOMAIN = "research.quiznat.com"


def website_env() -> dict[str, str]:
    env = os.environ.copy()
    env.setdefault("SAPHO_SITE_MODE", "github-pages")
    env.setdefault("SAPHO_SITE_BASE_URL", DEFAULT_BASE_URL)
    env.setdefault("SAPHO_SITE_CUSTOM_DOMAIN", DEFAULT_CUSTOM_DOMAIN)
    return env


def article_path(article_id: str) -> Path:
    return ARTICLES_DIR / article_id / "article.md"


def is_publishable_candidate(meta: dict) -> bool:
    status = str(meta.get("publication_status") or "").strip()
    minted_at = str(meta.get("artifact_minted_at_utc") or "").strip()
    return status == "ready-for-daily" and bool(minted_at) and not article_artifact_publication_current(meta)


def stale_candidates(limit: int | None = None) -> list[str]:
    rows: list[tuple[str, str]] = []
    for path in sorted(ARTICLES_DIR.glob("*/article.md")):
        meta, _body = read_markdown(path)
        if not is_publishable_candidate(meta):
            continue
        rows.append((str(meta.get("artifact_minted_at_utc") or ""), str(meta.get("article_id") or path.parent.name)))
    rows.sort(reverse=True)
    article_ids = [article_id for _minted_at, article_id in rows]
    if limit is not None:
        article_ids = article_ids[:limit]
    return article_ids


def validate_requested_articles(article_ids: list[str]) -> list[str]:
    validated: list[str] = []
    for article_id in article_ids:
        path = article_path(article_id)
        if not path.exists():
            raise RuntimeError(f"article_missing:{article_id}")
        meta, _body = read_markdown(path)
        if not is_publishable_candidate(meta):
            raise RuntimeError(f"article_not_publishable:{article_id}")
        validated.append(article_id)
    return validated


def publish_article(article_id: str, *, dry_run: bool = False) -> dict[str, object]:
    cmd = [sys.executable, str(PUBLISH_SCRIPT), "--article-id", article_id]
    if dry_run:
        cmd.append("--dry-run")
    proc = subprocess.run(
        cmd,
        cwd=str(ROOT),
        text=True,
        capture_output=True,
        env=website_env(),
    )
    result = {
        "article_id": article_id,
        "returncode": proc.returncode,
        "stdout": (proc.stdout or "").strip(),
        "stderr": (proc.stderr or "").strip(),
    }
    if proc.returncode != 0:
        detail = result["stderr"] or result["stdout"] or "publish_failed"
        raise RuntimeError(f"publish_failed:{article_id}:{detail}")
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--article-id", action="append", default=[])
    parser.add_argument("--limit", type=int, default=8)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    article_ids = list(args.article_id or [])
    if article_ids:
        selected = validate_requested_articles(article_ids)
    else:
        limit = None if args.limit <= 0 else args.limit
        selected = stale_candidates(limit=limit)

    if not selected:
        print(json.dumps({"status": "no_work", "selected": []}, indent=2))
        return 0

    results = [publish_article(article_id, dry_run=args.dry_run) for article_id in selected]
    print(
        json.dumps(
            {
                "status": "dry_run" if args.dry_run else "published",
                "selected": selected,
                "count": len(selected),
                "site_mode": website_env().get("SAPHO_SITE_MODE"),
                "site_base_url": website_env().get("SAPHO_SITE_BASE_URL"),
                "custom_domain": website_env().get("SAPHO_SITE_CUSTOM_DOMAIN"),
                "results": results,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
