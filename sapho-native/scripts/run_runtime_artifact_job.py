from __future__ import annotations

import argparse
import json
import subprocess
import sys

from runtime_job_common import ROOT, now_utc, parse_key_values, sync_runtime_ops, write_receipt


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-items", type=int, default=1)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--skip-deploy", action="store_true")
    args = parser.parse_args()

    cmd = [
        sys.executable,
        str(ROOT / "scripts" / "run_micro_artifact_watch.py"),
        "--max-items",
        str(args.max_items),
    ]
    if args.dry_run:
        cmd.append("--dry-run")
    if args.skip_deploy:
        cmd.append("--skip-deploy")

    proc = subprocess.run(cmd, cwd=str(ROOT), text=True, capture_output=True)
    sync = sync_runtime_ops()
    parsed = parse_key_values(proc.stdout or "")
    sync_ok = all(step["returncode"] == 0 for step in sync.values())
    ok = proc.returncode == 0 and sync_ok
    receipt = {
        "job": "research-artifact-publish-poller",
        "generatedAtUtc": now_utc(),
        "status": "ok" if ok else "error",
        "command": cmd,
        "returncode": proc.returncode,
        "stdout": proc.stdout,
        "stderr": proc.stderr,
        "summary": parsed,
        "sync": sync,
    }
    path = write_receipt("research-artifact-publish-poller", receipt)
    print(json.dumps({"status": receipt["status"], "receipt": str(path), "summary": parsed}, ensure_ascii=False))
    if proc.returncode != 0:
        return proc.returncode
    if not sync_ok:
        return 3
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
