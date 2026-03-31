from __future__ import annotations

import json
import shutil
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from runtime_ops import refresh_live_intake_ops_mirror

ROOT = Path('/home/openclaw/.openclaw/workspace/parallel-sapho')
LIVE_WEBSITE_ROOT = Path('/home/openclaw/.openclaw/workspace/website')
LOCAL_PUBLIC_DIR = ROOT / 'public' / 'site'
RECEIPTS_DIR = ROOT / 'state' / 'receipts'


def now_utc() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat().replace('+00:00', 'Z')


def ts_slug() -> str:
    return datetime.now(UTC).strftime('%Y%m%dT%H%M%SZ')


def _copy_if_exists(src: Path, dst: Path) -> bool:
    if not src.exists():
        return False
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    return True


def sync_local_public_ops_mirror() -> dict[str, Any]:
    copied: list[str] = []
    for rel in [
        Path('artifacts/ops/factory-checkin-latest.json'),
        Path('artifacts/ops/assignment-status.md'),
        Path('artifacts/ops/index.json'),
        Path('data/ops-latest.json'),
    ]:
        src = LIVE_WEBSITE_ROOT / rel
        dst = LOCAL_PUBLIC_DIR / rel
        if _copy_if_exists(src, dst):
            copied.append(str(rel))
    return {
        'returncode': 0,
        'copied': copied,
    }


def sync_runtime_ops() -> dict[str, Any]:
    refresh: dict[str, Any]
    try:
        refresh_live_intake_ops_mirror()
        refresh = {
            'returncode': 0,
            'stdout': '',
            'stderr': '',
        }
    except Exception as exc:
        refresh = {
            'returncode': 1,
            'stdout': '',
            'stderr': str(exc),
        }
    return {
        'refresh': refresh,
        'localPublicMirror': sync_local_public_ops_mirror(),
    }


def parse_key_values(text: str) -> dict[str, str]:
    parsed: dict[str, str] = {}
    for token in (text or '').replace('\n', ' ').split():
        if '=' not in token:
            continue
        key, value = token.split('=', 1)
        parsed[key.strip()] = value.strip()
    return parsed


def write_receipt(job_name: str, payload: dict[str, Any]) -> Path:
    RECEIPTS_DIR.mkdir(parents=True, exist_ok=True)
    stamped = RECEIPTS_DIR / f'{job_name}-{ts_slug()}.json'
    latest = RECEIPTS_DIR / f'{job_name}-latest.json'
    body = json.dumps(payload, indent=2, ensure_ascii=False) + '\n'
    stamped.write_text(body, encoding='utf-8')
    latest.write_text(body, encoding='utf-8')
    return stamped
