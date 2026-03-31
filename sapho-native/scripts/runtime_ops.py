from __future__ import annotations

import datetime as dt
import glob
import json
import os
import pwd
import shutil
import subprocess
import sys
from pathlib import Path

from common import parse_markdown

ROOT = Path(__file__).resolve().parents[1]
LIVE_RUNTIME_ROOT = Path('/home/openclaw/.openclaw/workspace')
LIVE_RUNTIME_ARTICLES = LIVE_RUNTIME_ROOT / 'research' / 'articles'
LIVE_FACTORY_CHECKIN_DIR = LIVE_RUNTIME_ROOT / 'research' / 'factory' / 'checkins'
LIVE_FACTORY_CHECKIN_LATEST = LIVE_FACTORY_CHECKIN_DIR / 'article-checkin-latest.json'
LIVE_ASSIGNMENT_STATUS = LIVE_RUNTIME_ROOT / 'research' / 'assignment-status.md'
LIVE_REPORTS_SHIFTS = LIVE_RUNTIME_ROOT / 'research' / 'reports' / 'shifts'
LIVE_WEBSITE = LIVE_RUNTIME_ROOT / 'website'
LIVE_WEBSITE_OPS = LIVE_WEBSITE / 'artifacts' / 'ops'
LIVE_WEBSITE_DATA = LIVE_WEBSITE / 'data'


def running_as_openclaw() -> bool:
    try:
        return pwd.getpwuid(os.geteuid()).pw_name == 'openclaw'
    except KeyError:
        return False


def openclaw_python_cmd(*parts: str) -> list[str]:
    cmd = [sys.executable, *parts]
    if running_as_openclaw():
        return cmd
    return ['sudo', '-n', '-H', '-u', 'openclaw', *cmd]


def run_live_python(*parts: str, capture_output: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        openclaw_python_cmd(*parts),
        cwd=str(ROOT),
        text=True,
        capture_output=capture_output,
        env=os.environ.copy(),
    )


def now_utc() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def ts_compact() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%SZ')


def is_x_url(url: str) -> bool:
    lowered = str(url or '').lower()
    return 'x.com/' in lowered or 'twitter.com/' in lowered


def _article_paths() -> list[Path]:
    return sorted(LIVE_RUNTIME_ARTICLES.glob('*.md'))


def _copy_if_exists(src: Path, dst: Path) -> bool:
    if not src.exists():
        return False
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    return True


def _latest_shift_path() -> str:
    matches = [Path(item) for item in glob.glob(str(LIVE_REPORTS_SHIFTS / '*.json'))]
    if not matches:
        return ''
    latest = sorted(matches, key=lambda item: item.stat().st_mtime, reverse=True)[0]
    try:
        return str(latest.relative_to(LIVE_RUNTIME_ROOT))
    except Exception:
        return str(latest)


def build_runtime_checkin_payload(stale_minutes: int = 120) -> dict[str, object]:
    counts: dict[str, int] = {}
    processable_non_x = 0
    pending_x = 0
    stalled: list[dict[str, str]] = []
    missing_source_custody: list[str] = []
    cutoff = dt.datetime.now(dt.timezone.utc) - dt.timedelta(minutes=stale_minutes)

    for path in _article_paths():
        frontmatter, _body = parse_markdown(path.read_text(encoding='utf-8'))
        article_id = str(frontmatter.get('article_id') or path.stem)
        state = str(frontmatter.get('filter_state') or 'pending')
        counts[state] = counts.get(state, 0) + 1
        source_url = str(frontmatter.get('canonical_url') or frontmatter.get('source_url') or '')
        discovered_raw = str(frontmatter.get('discovered_at_utc') or '')
        discovered_at = None
        try:
            discovered_at = dt.datetime.fromisoformat(discovered_raw.replace('Z', '+00:00')).astimezone(dt.timezone.utc)
        except Exception:
            discovered_at = None

        if state == 'pending' and is_x_url(source_url):
            pending_x += 1
        if state == 'pending' and not is_x_url(source_url):
            processable_non_x += 1
            if discovered_at and discovered_at < cutoff:
                stalled.append(
                    {
                        'articleId': article_id,
                        'sourceUrl': source_url,
                        'discoveredAtUtc': discovered_at.strftime('%Y-%m-%dT%H:%M:%SZ'),
                    }
                )
        if state in {'kept', 'discarded'} and str(frontmatter.get('source_custody_status') or '') == 'missing':
            missing_source_custody.append(article_id)

    if missing_source_custody:
        action = 'repair_source_custody'
    elif stalled:
        action = 'drain_stalled_pending_articles'
    elif processable_non_x > 0:
        action = 'drain_pending_articles'
    elif pending_x > 0:
        action = 'await_x_raw_content'
    else:
        action = 'ready_for_pm_daily_or_hardening'

    return {
        'checkedAtUtc': now_utc(),
        'articleRoot': 'research/articles',
        'statusCounts': counts,
        'processableNonXPending': processable_non_x,
        'pendingX': pending_x,
        'stalledPendingArticles': stalled,
        'missingSourceCustodyArticleIds': missing_source_custody[:50],
        'recommendedAction': action,
    }


def write_runtime_checkin(stale_minutes: int = 120) -> Path:
    payload = build_runtime_checkin_payload(stale_minutes=stale_minutes)
    LIVE_FACTORY_CHECKIN_DIR.mkdir(parents=True, exist_ok=True)
    stamped = LIVE_FACTORY_CHECKIN_DIR / f'article-checkin-{ts_compact()}.json'
    latest = LIVE_FACTORY_CHECKIN_DIR / 'article-checkin-latest.json'
    body = json.dumps(payload, indent=2, ensure_ascii=False) + '\n'
    stamped.write_text(body, encoding='utf-8')
    latest.write_text(body, encoding='utf-8')
    return stamped


def sync_live_ops_surfaces() -> None:
    LIVE_WEBSITE_OPS.mkdir(parents=True, exist_ok=True)
    LIVE_WEBSITE_DATA.mkdir(parents=True, exist_ok=True)

    _copy_if_exists(LIVE_FACTORY_CHECKIN_LATEST, LIVE_WEBSITE_OPS / 'factory-checkin-latest.json')
    _copy_if_exists(LIVE_ASSIGNMENT_STATUS, LIVE_WEBSITE_OPS / 'assignment-status.md')

    assignment_status_path = 'artifacts/ops/assignment-status.md' if (LIVE_WEBSITE_OPS / 'assignment-status.md').exists() else ''
    factory_checkin_path = 'artifacts/ops/factory-checkin-latest.json' if (LIVE_WEBSITE_OPS / 'factory-checkin-latest.json').exists() else ''
    latest_shift_path = _latest_shift_path()

    ops_payload = {
        'generatedAtUtc': now_utc(),
        'assignmentStatusPath': assignment_status_path,
        'factoryCheckinLatestPath': factory_checkin_path,
        'latestShiftPath': latest_shift_path,
    }
    (LIVE_WEBSITE_DATA / 'ops-latest.json').write_text(
        json.dumps(ops_payload, indent=2, ensure_ascii=False) + '\n',
        encoding='utf-8',
    )

    ops_files = sorted(path.name for path in LIVE_WEBSITE_OPS.iterdir() if path.is_file())
    ops_index = {
        'generatedAtUtc': now_utc(),
        'files': ops_files,
        'latest': {
            'assignmentStatus': Path(assignment_status_path).name if assignment_status_path else '',
            'factoryCheckin': Path(factory_checkin_path).name if factory_checkin_path else '',
            'latestShift': latest_shift_path,
        },
    }
    (LIVE_WEBSITE_OPS / 'index.json').write_text(
        json.dumps(ops_index, indent=2, ensure_ascii=False) + '\n',
        encoding='utf-8',
    )


def refresh_live_intake_ops_mirror() -> None:
    write_runtime_checkin()
    sync_live_ops_surfaces()


def publish_runtime_ops_surfaces(reason: str) -> None:
    proc = run_live_python(
        str(ROOT / 'scripts' / 'deploy_live_site.py'),
        '--skip-render',
        '--path',
        'artifacts/ops',
        '--path',
        'data/ops-latest.json',
    )
    if proc.returncode != 0:
        detail = (proc.stderr or proc.stdout or '').strip() or 'ops_deploy_failed'
        raise RuntimeError(f'ops_deploy_failed:{reason}:{detail}')


def read_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding='utf-8'))
