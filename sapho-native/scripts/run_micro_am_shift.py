from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

from article_bundle_store_local import load_article_bundle_by_id, save_article_bundle
from common import ARTICLES_DIR, DUPLICATE_REJECTED_STATUS, article_file, article_included_for_date_meta, article_is_terminal_for_selector, publication_status, read_markdown, utc_date, utc_now
from import_runtime_backlog import build_import_item, discover_checkin_order, load_default_order, write_import_item
from runtime_ops import publish_runtime_ops_surfaces, refresh_live_intake_ops_mirror

ROOT = Path(__file__).resolve().parents[1]


def run_local_step(*parts: str) -> tuple[int, str, str]:
    proc = subprocess.run(
        [sys.executable, *parts],
        cwd=str(ROOT),
        text=True,
        capture_output=True,
    )
    return proc.returncode, proc.stdout, proc.stderr


def parse_json_stdout(raw: str) -> dict:
    text = str(raw or "").strip()
    if not text:
        return {}
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return {}


def refresh_live_discovery() -> dict[str, object]:
    feeder_rc, feeder_stdout, feeder_stderr = run_local_step(str(ROOT / "scripts" / "run_brave_feeder_local.py"))
    feeder_summary = parse_json_stdout(feeder_stdout)
    if feeder_rc != 0:
        return {
            "status": "error",
            "step": "feeder",
            "code": feeder_rc,
            "stderr": feeder_stderr.strip(),
        }

    try:
        refresh_live_intake_ops_mirror()
    except Exception as exc:
        return {
            "status": "error",
            "step": "article_checkin",
            "code": 1,
            "stderr": str(exc).strip(),
            "feeder": feeder_summary,
        }

    return {
        "status": "ok",
        "feeder": feeder_summary,
    }


def live_order() -> tuple[list[str], dict]:
    try:
        return discover_checkin_order()
    except Exception:
        return load_default_order()


def included_article_ids(replay_date: str) -> list[str]:
    rows: list[str] = []
    for path in sorted(ARTICLES_DIR.glob("*/article.md")):
        meta, _ = read_markdown(path)
        if article_included_for_date_meta(meta, replay_date):
            rows.append(path.parent.name)
    return rows


def inclusion_count(replay_date: str) -> int:
    return len(included_article_ids(replay_date))


def sync_runtime_bundle(article_id: str) -> None:
    if not article_file(article_id).exists():
        return
    local_meta, _ = read_markdown(article_file(article_id))
    runtime_bundle = load_article_bundle_by_id(article_id)
    runtime_meta = dict(runtime_bundle.get('frontmatter') or {})
    status = publication_status(local_meta)
    decision = str(local_meta.get('curator_decision') or '').strip()
    if status in {'ready-for-daily', 'published'} or decision == 'kept':
        runtime_meta['filter_state'] = 'kept'
        runtime_meta['last_stage'] = 'facts'
        runtime_meta['artifact_minted_at_utc'] = str(local_meta.get('artifact_minted_at_utc') or runtime_meta.get('artifact_minted_at_utc') or '')
        runtime_meta['artifact_title'] = str(local_meta.get('source_title') or runtime_meta.get('artifact_title') or '')
    elif status in {'discarded', 'capture-blocked', DUPLICATE_REJECTED_STATUS}:
        runtime_meta['filter_state'] = 'discarded'
        runtime_meta['last_stage'] = 'filter'
    else:
        runtime_meta['filter_state'] = 'pending'
    runtime_meta['filter_decided_at_utc'] = str(local_meta.get('curated_at_utc') or local_meta.get('captured_at_utc') or utc_now())
    runtime_meta['filter_rationale'] = str(local_meta.get('curator_reason') or local_meta.get('source_capture_gate_reason') or '')
    runtime_meta['source_custody_status'] = 'present' if (article_file(article_id).parent / 'source.md').exists() else runtime_meta.get('source_custody_status') or 'missing'
    save_article_bundle(runtime_meta, str(runtime_bundle.get('body') or ''))


def article_needs_local_work(article_id: str, replay_date: str) -> bool:
    path = article_file(article_id)
    if not path.exists():
        return True
    meta, _ = read_markdown(path)
    if article_is_terminal_for_selector(meta):
        return False
    return not article_included_for_date_meta(meta, replay_date)


def ensure_local_article(
    article_id: str,
    selection_rank: int,
    selection_source: str,
    *,
    dry_run: bool,
) -> dict:
    item = build_import_item(article_id, selection_rank, selection_source)
    if not dry_run and item.get("action") in {"would-import", "would-import-ticket-only"}:
        write_import_item(item)
    return item


def run_capture(ticket_id: str) -> subprocess.CompletedProcess[str]:
    cmd = [
        sys.executable,
        str(ROOT / "scripts" / "capture_source.py"),
        "--ticket-id",
        ticket_id,
    ]
    return subprocess.run(cmd, check=False, cwd=str(ROOT), text=True, capture_output=True)


def run_article_lane(article_id: str, replay_date: str) -> subprocess.CompletedProcess[str]:
    cmd = [
        sys.executable,
        str(ROOT / "scripts" / "run_micro_article_lane.py"),
        "--article-id",
        article_id,
    ]
    if replay_date:
        cmd.extend(["--replay-date", replay_date])
    return subprocess.run(cmd, check=False, cwd=str(ROOT), text=True, capture_output=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-items", type=int, default=None)
    parser.add_argument("--max-inclusions", type=int, default=8)
    parser.add_argument("--replay-date", default=utc_date())
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    max_items = None if args.max_items is None else max(args.max_items, 0)
    max_inclusions = max(args.max_inclusions, 0)
    replay_date = args.replay_date

    discovery = refresh_live_discovery()
    if discovery.get("status") != "ok":
        step = str(discovery.get("step") or "native_discovery")
        code = discovery.get("code")
        detail = str(discovery.get("stderr") or "").strip() or "command_failed"
        print(f"native_discovery_warning step={step} code={code} detail={detail}", file=sys.stderr)
    else:
        feeder = discovery.get("feeder") or {}
        if isinstance(feeder, dict):
            paused = "true" if feeder.get("paused") else "false"
            pending = int(feeder.get("pendingArticles") or 0)
            inserted = int(feeder.get("inserted") or 0)
            print(f"native_discovery paused={paused} pending={pending} inserted={inserted}")

    order, selection_meta = live_order()
    selection_source = str(selection_meta.get("kind") or "native-runtime")
    included = inclusion_count(replay_date)
    processed = 0
    failed = 0
    attempted = 0
    stop_reason = "queue-exhausted"

    for selection_rank, article_id in enumerate(order, start=1):
        if included >= max_inclusions:
            stop_reason = "inclusion-cap"
            break
        if max_items is not None and attempted >= max_items:
            stop_reason = "item-cap"
            break
        if not article_needs_local_work(article_id, replay_date):
            if not args.dry_run and article_file(article_id).exists():
                sync_runtime_bundle(article_id)
            continue

        item = ensure_local_article(
            article_id,
            selection_rank,
            selection_source,
            dry_run=args.dry_run,
        )
        action = str(item.get("action") or "")
        if action == "missing-runtime-article":
            if args.dry_run:
                print(f"missing {article_id} {action}")
            continue

        if args.dry_run:
            print(f"candidate {article_id} {action}")
            processed += 1
            attempted += 1
            continue

        attempted += 1
        if not article_file(article_id).exists():
            ticket_id = str(item.get("ticketId") or "")
            capture_proc = run_capture(ticket_id)
            if capture_proc.returncode != 0:
                failed += 1
                detail = str(capture_proc.stderr or capture_proc.stdout or "").strip()
                detail_line = detail.splitlines()[-1] if detail else "capture_source_failed"
                print(
                    f"capture_source_warning article_id={article_id} ticket_id={ticket_id} code={capture_proc.returncode} detail={detail_line}",
                    file=sys.stderr,
                )
                continue

        if not article_file(article_id).exists():
            failed += 1
            print(f"article_lane_warning article_id={article_id} detail=article_missing_after_import", file=sys.stderr)
            continue

        proc = run_article_lane(article_id, replay_date)
        if proc.returncode != 0:
            failed += 1
            detail = str(proc.stderr or proc.stdout or "").strip()
            detail_line = detail.splitlines()[-1] if detail else "article_lane_failed"
            print(
                f"article_lane_warning article_id={article_id} code={proc.returncode} detail={detail_line}",
                file=sys.stderr,
            )
            continue
        sync_runtime_bundle(article_id)
        processed += 1
        included = inclusion_count(replay_date)
    else:
        if included >= max_inclusions:
            stop_reason = "inclusion-cap"

    remaining = sum(1 for article_id in order if article_needs_local_work(article_id, replay_date))
    if not args.dry_run:
        refresh_live_intake_ops_mirror()
        publish_runtime_ops_surfaces(f'am-ops-{replay_date}')
    included_ids = included_article_ids(replay_date)
    print(
        f"processed={processed} failed={failed} attempted={attempted} included={included} remaining={remaining} "
        f"target={max_inclusions} stop={stop_reason} date={replay_date}"
    )
    print("included_article_ids=" + ",".join(included_ids))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
