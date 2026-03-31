from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

from common import ARTICLES_DIR, article_artifact_publication_current, read_markdown

ROOT = Path(__file__).resolve().parents[1]


def candidate_sort_key(path: Path) -> tuple[str, str]:
    meta, _body = read_markdown(path)
    return str(meta.get("artifact_minted_at_utc") or ""), path.parent.name


def needs_artifact_publish(meta: dict) -> bool:
    if str(meta.get("publication_status") or "") != "ready-for-daily":
        return False
    minted_at = str(meta.get("artifact_minted_at_utc") or "").strip()
    if not minted_at:
        return False
    return not article_artifact_publication_current(meta)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-items", type=int, default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--skip-deploy", action="store_true")
    args = parser.parse_args()

    max_items = None if args.max_items is None else max(args.max_items, 0)
    processed = 0
    pending = 0
    for article_path in sorted(ARTICLES_DIR.glob("*/article.md"), key=candidate_sort_key):
        meta, _body = read_markdown(article_path)
        if not needs_artifact_publish(meta):
            continue
        pending += 1
        if max_items is not None and processed >= max_items:
            continue
        article_id = article_path.parent.name
        if args.dry_run:
            print(f"candidate {article_id} minted={meta.get('artifact_minted_at_utc')}")
            processed += 1
            continue
        cmd = [
            sys.executable,
            str(ROOT / "scripts" / "run_micro_artifact_publish.py"),
            "--article-id",
            article_id,
        ]
        if args.skip_deploy:
            cmd.append("--skip-deploy")
        proc = subprocess.run(cmd, cwd=str(ROOT), text=True)
        if proc.returncode != 0:
            raise SystemExit(proc.returncode)
        processed += 1

    print(f"processed={processed} pending={pending}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
