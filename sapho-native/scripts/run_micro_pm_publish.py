from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path

from common import ARTICLES_DIR, article_published_for_daily_on_date, article_ready_for_pm_on_date, read_markdown, utc_date
from render_site import PUBLIC_SEED_ENV_VAR, render_daily_briefing_site
from runtime_ops import refresh_live_intake_ops_mirror

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PUBLIC_SEED_DIR = "/home/openclaw/.openclaw/workspace/website"


def article_counts_for_date(date: str) -> tuple[int, int]:
    ready_count = 0
    published_count = 0
    for path in ARTICLES_DIR.glob("*/article.md"):
        meta, _ = read_markdown(path)
        if article_ready_for_pm_on_date(meta, date):
            ready_count += 1
        elif article_published_for_daily_on_date(meta, date):
            published_count += 1
    return ready_count, published_count


def run_step(*parts: str) -> int:
    proc = subprocess.run([sys.executable, *parts], cwd=str(ROOT), text=True, env=os.environ.copy())
    return proc.returncode


def deploy_daily_surfaces(daily_date: str) -> int:
    paths = [
        f"briefs/{daily_date}",
        "briefs/latest",
        f"daily/{daily_date}.html",
        "daily/latest.html",
        "daily-briefing-archive.html",
        "daily.xml",
        "site-files.txt",
        "site-files.json",
        "index.json",
        "agents-start-here.html",
    ]
    cmd = [sys.executable, str(ROOT / "scripts" / "deploy_live_site.py"), "--skip-render"]
    for rel in paths:
        cmd.extend(["--path", rel])
    proc = subprocess.run(cmd, cwd=str(ROOT), text=True, env=os.environ.copy())
    return proc.returncode


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--replay-date")
    parser.add_argument("--date", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--public-seed-dir", default=None)
    args = parser.parse_args()
    target_date = args.replay_date or args.date or utc_date()
    os.environ[PUBLIC_SEED_ENV_VAR] = args.public_seed_dir or os.environ.get(PUBLIC_SEED_ENV_VAR, "") or DEFAULT_PUBLIC_SEED_DIR

    ready_count, published_count = article_counts_for_date(target_date)
    if ready_count == 0 and published_count == 0:
        print(f"no_work {target_date}")
        return 0

    if args.dry_run:
        if ready_count > 0:
            print(f"ready_for_publish {target_date} ready={ready_count}")
        else:
            print(f"already_published {target_date} published={published_count}")
        return 0

    if ready_count > 0:
        cycle_rc = run_step(str(ROOT / "scripts" / "run_pm_cycle.py"), "--replay-date", target_date)
        if cycle_rc != 0:
            conclave_path = ROOT / "daily" / target_date / "conclave.md"
            if conclave_path.exists():
                conclave_meta, _ = read_markdown(conclave_path)
                verdict = str(conclave_meta.get("verdict") or "")
                if verdict and verdict != "pass":
                    print(f"blocked {target_date} {verdict}")
                    return 2
            raise SystemExit(cycle_rc)

        conclave_meta, _ = read_markdown(ROOT / "daily" / target_date / "conclave.md")
        verdict = str(conclave_meta.get("verdict") or "")
        if verdict != "pass":
            print(f"blocked {target_date} {verdict}")
            return 2

    refresh_live_intake_ops_mirror()
    current_brief = render_daily_briefing_site()
    deploy_rc = deploy_daily_surfaces(current_brief["date"])
    if deploy_rc != 0:
        raise SystemExit(deploy_rc)
    if ready_count > 0:
        print(f"published {target_date}")
    else:
        print(f"already_published {target_date}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
