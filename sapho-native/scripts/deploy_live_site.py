from __future__ import annotations

import argparse
import hashlib
import json
import os
import pwd
import shutil
import subprocess
from datetime import UTC, datetime
from pathlib import Path

from render_site import PUBLIC_DIR, latest_daily_date, render_site

ROOT = Path(__file__).resolve().parents[1]
LIVE_REPO = Path("/home/openclaw/.openclaw/workspace")
LIVE_SITE = LIVE_REPO / "website"
RESTORE_ROOT = ROOT / ".restore-points" / "site"
LATEST_RESTORE_META = RESTORE_ROOT / "latest.json"


def run_cmd(parts: list[str], capture: bool = False) -> str:
    proc = subprocess.run(parts, text=True, capture_output=capture)
    if proc.returncode != 0:
        stderr = (proc.stderr or "").strip()
        raise RuntimeError(stderr or "command_failed")
    return (proc.stdout or "").strip()


def run_as_live_user(parts: list[str]) -> list[str]:
    try:
        if pwd.getpwuid(os.geteuid()).pw_name == "openclaw":
            return parts
    except KeyError:
        pass
    return ["sudo", "-n", "-H", "-u", "openclaw", *parts]


def website_status() -> str:
    return run_cmd(["git", "-C", str(LIVE_REPO), "status", "--porcelain", "--", "website"], capture=True)


def now_slug() -> str:
    return datetime.now(UTC).replace(microsecond=0).strftime("%Y%m%dT%H%M%SZ")


def ensure_restore_root() -> None:
    RESTORE_ROOT.mkdir(parents=True, exist_ok=True)


def ensure_live_site_dir() -> None:
    LIVE_SITE.mkdir(parents=True, exist_ok=True)


def live_site_exists() -> bool:
    return LIVE_SITE.is_dir()


def tree_manifest(path: Path) -> dict[str, object]:
    if not path.exists():
        return {
            "path": str(path),
            "exists": False,
            "fileCount": 0,
            "digest": "",
            "sampleFiles": [],
        }
    files = sorted(str(item.relative_to(path)).replace("\\", "/") for item in path.rglob("*") if item.is_file())
    digest = hashlib.sha1("\n".join(files).encode("utf-8")).hexdigest() if files else ""
    return {
        "path": str(path),
        "exists": True,
        "fileCount": len(files),
        "digest": digest,
        "sampleFiles": files[:20],
    }


def create_restore_point(dry_run: bool = False) -> dict[str, str]:
    ensure_restore_root()
    head = run_cmd(["git", "-C", str(LIVE_REPO), "rev-parse", "HEAD"], capture=True)
    restore_id = f"{now_slug()}-{head[:12]}"
    snapshot_dir = RESTORE_ROOT / restore_id / "website"
    manifest_path = RESTORE_ROOT / restore_id / "manifest.json"
    status_before = website_status()
    meta = {
        "restorePointId": restore_id,
        "createdAtUtc": now_slug(),
        "sourceCommit": head,
        "snapshotDir": str(snapshot_dir),
        "manifestPath": str(manifest_path),
        "websiteStatusBefore": status_before,
        "sourceTree": tree_manifest(LIVE_SITE),
    }
    if dry_run:
        return meta
    snapshot_dir.parent.mkdir(parents=True, exist_ok=True)
    if live_site_exists():
        shutil.rmtree(snapshot_dir, ignore_errors=True)
        shutil.copytree(LIVE_SITE, snapshot_dir)
    else:
        snapshot_dir.mkdir(parents=True, exist_ok=True)
    snapshot_manifest = tree_manifest(snapshot_dir)
    manifest = {**meta, "snapshotTree": snapshot_manifest}
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    LATEST_RESTORE_META.write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    return meta


def load_latest_restore_point() -> dict[str, str]:
    if not LATEST_RESTORE_META.exists():
        raise RuntimeError("missing_latest_restore_point")
    return json.loads(LATEST_RESTORE_META.read_text(encoding="utf-8"))


def sync_path(rel: str, dry_run: bool = False) -> None:
    rel_path = Path(rel)
    source = PUBLIC_DIR / rel_path
    target = LIVE_SITE / rel_path
    if not source.exists():
        raise RuntimeError(f"missing_public_path:{rel}")
    if dry_run:
        return
    if source.is_dir():
        if target.is_symlink() or target.is_file():
            target.unlink(missing_ok=True)
        target.mkdir(parents=True, exist_ok=True)
        run_cmd(["rsync", "-a", "--delete", f"{source}/", f"{target}/"])
        return
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)


def sync_public_site(paths: list[str] | None = None, dry_run: bool = False) -> None:
    ensure_live_site_dir()
    if not paths:
        cmd = ["rsync", "-a", "--delete", f"{PUBLIC_DIR}/", f"{LIVE_SITE}/"]
        if dry_run:
            cmd.insert(3, "--dry-run")
        run_cmd(cmd)
        return
    for rel in paths:
        sync_path(rel, dry_run=dry_run)


def restore_site(meta: dict[str, str], dry_run: bool = False) -> str:
    snapshot_dir = Path(meta["snapshotDir"])
    if not snapshot_dir.exists():
        raise RuntimeError("restore_snapshot_missing")
    ensure_live_site_dir()
    if not dry_run:
        shutil.rmtree(LIVE_SITE, ignore_errors=True)
        shutil.copytree(snapshot_dir, LIVE_SITE)
    status = website_status()
    if not status:
        return "site_already_matches_restore_point"
    if dry_run:
        return status
    restore_id = meta["restorePointId"]
    run_cmd(run_as_live_user(["git", "-C", str(LIVE_REPO), "add", "--", "website"]))
    run_cmd(run_as_live_user(["git", "-C", str(LIVE_REPO), "commit", "--only", "-m", f"Restore site from proving restore point {restore_id}", "--", "website"]))
    run_cmd(run_as_live_user(["git", "-C", str(LIVE_REPO), "push", "origin", "main"]))
    return run_cmd(run_as_live_user(["git", "-C", str(LIVE_REPO), "rev-parse", "--short", "HEAD"]), capture=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--skip-render", action="store_true")
    parser.add_argument("--restore-last", action="store_true")
    parser.add_argument("--path", action="append", default=[])
    args = parser.parse_args()

    if args.restore_last:
        result = restore_site(load_latest_restore_point(), dry_run=args.dry_run)
        print(result)
        return 0

    if not args.skip_render:
        render_site()

    restore_meta = create_restore_point(dry_run=args.dry_run)
    sync_public_site(paths=args.path or None, dry_run=args.dry_run)

    status = website_status()
    if not status:
        if not args.dry_run:
            print(f"no_site_changes restore_point={restore_meta['restorePointId']}")
        else:
            print("no_site_changes")
        return 0
    if args.dry_run:
        print(f"restore_point={restore_meta['restorePointId']}")
        print(status)
        return 0

    try:
        date = latest_daily_date()
        message = f"Publish {date} parallel Sapho site update"
    except Exception:
        message = "Publish parallel Sapho site update"
    run_cmd(run_as_live_user(["git", "-C", str(LIVE_REPO), "add", "--", "website"]))
    run_cmd(run_as_live_user(["git", "-C", str(LIVE_REPO), "commit", "--only", "-m", message, "--", "website"]))
    run_cmd(run_as_live_user(["git", "-C", str(LIVE_REPO), "push", "origin", "main"]))
    head = run_cmd(run_as_live_user(["git", "-C", str(LIVE_REPO), "rev-parse", "--short", "HEAD"]), capture=True)
    print(f"{head} restore_point={restore_meta['restorePointId']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
