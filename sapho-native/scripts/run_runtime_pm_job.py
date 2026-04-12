from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys

from runtime_job_common import ROOT, now_utc, sync_runtime_ops, write_receipt

DEFAULT_PUBLIC_SEED_DIR = str(ROOT / "public" / "site")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", default=None)
    parser.add_argument("--replay-date", default=None)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    env = os.environ.copy()
    env.setdefault("SAPHO_PUBLIC_SEED_DIR", DEFAULT_PUBLIC_SEED_DIR)
    cmd = [
        sys.executable,
        str(ROOT / "scripts" / "run_micro_pm_publish.py"),
        "--public-seed-dir",
        env["SAPHO_PUBLIC_SEED_DIR"],
    ]
    target_date = args.replay_date or args.date
    if target_date:
        cmd.extend(["--date", target_date])
    if args.dry_run:
        cmd.append("--dry-run")

    proc = subprocess.run(cmd, cwd=str(ROOT), text=True, capture_output=True, env=env)
    sync = sync_runtime_ops()
    sync_ok = all(step["returncode"] == 0 for step in sync.values())
    ok = proc.returncode == 0 and sync_ok
    receipt = {
        "job": "research-pm-live-synthesis-shift",
        "generatedAtUtc": now_utc(),
        "status": "ok" if ok else "error",
        "command": cmd,
        "returncode": proc.returncode,
        "stdout": proc.stdout,
        "stderr": proc.stderr,
        "sync": sync,
    }
    path = write_receipt("research-pm-live-synthesis-shift", receipt)
    print(json.dumps({"status": receipt["status"], "receipt": str(path), "stdout": (proc.stdout or "").strip()}, ensure_ascii=False))
    if proc.returncode != 0:
        return proc.returncode
    if not sync_ok:
        return 3
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
