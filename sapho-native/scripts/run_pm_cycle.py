from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run_step(*parts: str) -> None:
    proc = subprocess.run([sys.executable, *parts], cwd=str(ROOT), text=True)
    if proc.returncode != 0:
        raise SystemExit(proc.returncode)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--replay-date")
    parser.add_argument("--date")
    args = parser.parse_args()
    replay_date = args.replay_date or args.date
    if not replay_date:
        raise ValueError("missing_replay_date")
    run_step(str(ROOT / "scripts" / "run_micro_daily.py"), "--replay-date", replay_date)
    print(ROOT / "daily" / replay_date)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
