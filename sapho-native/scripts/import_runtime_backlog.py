from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
from pathlib import Path
from typing import Any

from capture_source import fetch_url
from common import (
    article_file,
    best_effort_html_to_text,
    canonicalize_article_url,
    parse_markdown,
    source_file,
    ticket_path,
    utc_now,
    write_article_markdown,
    write_markdown,
)
from runtime_paths import RUNTIME_ARTICLES_ROOT, RUNTIME_FACTORY_CHECKIN_LATEST, RUNTIME_REPORTS_SHIFTS, RUNTIME_ROOT, RUNTIME_SOURCE_ROOT

ROOT = Path(__file__).resolve().parents[1]
RUNTIME_RESEARCH = RUNTIME_ROOT / "research"
RUNTIME_ARTICLES = RUNTIME_ARTICLES_ROOT
RUNTIME_SOURCE = RUNTIME_SOURCE_ROOT
RUNTIME_SHIFTS = RUNTIME_REPORTS_SHIFTS
RUNTIME_CHECKIN = RUNTIME_FACTORY_CHECKIN_LATEST


def run_cmd(parts: list[str]) -> str:
    proc = subprocess.run(parts, text=True, capture_output=True)
    if proc.returncode != 0:
        stderr = (proc.stderr or "").strip()
        raise RuntimeError(stderr or "command_failed")
    return proc.stdout


def _can_read_runtime_directly() -> bool:
    return os.geteuid() in {0, 1000, 1002}


def sudo_read_text(path: Path) -> str:
    if _can_read_runtime_directly():
        return path.read_text(encoding="utf-8")
    return run_cmd(["sudo", "-n", "cat", str(path)])


def sudo_load_json(path: Path) -> dict[str, Any]:
    return json.loads(sudo_read_text(path))


def sudo_find(paths: list[Path], pattern: str) -> list[Path]:
    found: list[Path] = []
    for base in paths:
        if _can_read_runtime_directly():
            matches = sorted(base.glob(pattern))
            found.extend(path for path in matches if path.is_file())
            continue
        output = run_cmd(["sudo", "-n", "find", str(base), "-maxdepth", "1", "-type", "f", "-name", pattern])
        for line in output.splitlines():
            line = line.strip()
            if line:
                found.append(Path(line))
    return sorted(found)


def dedupe_ordered(values: list[str]) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for value in values:
        if value in seen:
            continue
        seen.add(value)
        ordered.append(value)
    return ordered


def article_stub_path(article_id: str) -> Path:
    return RUNTIME_ARTICLES / f"{article_id}.md"


def source_json_path(article_id: str) -> Path:
    return RUNTIME_SOURCE / f"{article_id}.json"


def source_txt_path(article_id: str) -> Path:
    return RUNTIME_SOURCE / f"{article_id}.txt"


def load_runtime_markdown(path: Path) -> tuple[dict[str, Any], str]:
    return parse_markdown(sudo_read_text(path))


def discover_front_half_order() -> tuple[list[str], dict[str, Any]]:
    candidates = sudo_find([RUNTIME_SHIFTS], "front-half*.json")
    ranked: list[tuple[str, Path, dict[str, Any]]] = []
    for path in candidates:
        payload = sudo_load_json(path)
        ids = payload.get("remainingProcessablePendingArticleIds")
        if isinstance(ids, list) and ids:
            ranked.append((str(payload.get("generatedAtUtc") or ""), path, payload))
    if not ranked:
        raise RuntimeError("missing_front_half_pending_order")
    _generated_at, selected_path, selected_payload = sorted(ranked, key=lambda item: (item[0], str(item[1])))[-1]
    return dedupe_ordered([str(item) for item in selected_payload["remainingProcessablePendingArticleIds"]]), {
        "kind": "front-half-report",
        "path": str(selected_path),
        "runId": selected_payload.get("runId") or "",
        "generatedAtUtc": selected_payload.get("generatedAtUtc") or "",
        "remainingProcessablePendingCount": int(selected_payload.get("remainingProcessablePendingCount") or 0),
    }


def discover_checkin_order() -> tuple[list[str], dict[str, Any]]:
    payload = sudo_load_json(RUNTIME_CHECKIN)
    direct_ids = payload.get("processablePendingArticleIds") or []
    ordered = [str(item).strip() for item in direct_ids if str(item).strip()]
    if not ordered:
        items = payload.get("stalledPendingArticles") or []
        for item in items:
            article_id = str((item or {}).get("articleId") or "").strip()
            if article_id:
                ordered.append(article_id)
    return dedupe_ordered(ordered), {
        "kind": "article-checkin",
        "path": str(RUNTIME_CHECKIN),
        "checkedAtUtc": payload.get("checkedAtUtc") or "",
        "processableNonXPending": int(payload.get("processableNonXPending") or 0),
    }


def load_default_order() -> tuple[list[str], dict[str, Any]]:
    try:
        return discover_front_half_order()
    except Exception:
        return discover_checkin_order()


def load_id_file(path: Path) -> list[str]:
    ids: list[str] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        value = raw.strip()
        if not value or value.startswith("#"):
            continue
        ids.append(value)
    return ids


def import_ticket_id(article_id: str) -> str:
    return f"ticket-import-{article_id}"


def local_paths(article_id: str) -> dict[str, Path]:
    ticket_id = import_ticket_id(article_id)
    return {
        "ticket": ticket_path(ticket_id),
        "article": article_file(article_id),
        "source": source_file(article_id),
    }


def build_source_body(
    title: str,
    source_text: str,
    article_meta: dict[str, Any],
    source_meta: dict[str, Any],
    *,
    refreshed_live_source: bool = False,
) -> str:
    return (
        "# Source Capture\n\n"
        "## Title\n\n"
        f"{title}\n\n"
        "## Body\n\n"
        f"{source_text.strip()}\n\n"
        "## Import Provenance\n\n"
        "- imported_from: canonical-openclaw-runtime\n"
        f"- runtime_article_bundle_path: research/articles/{article_meta['article_id']}.md\n"
        f"- runtime_source_snapshot_json: research/source-material/{article_meta['article_id']}.json\n"
        f"- runtime_source_snapshot_text: research/source-material/{article_meta['article_id']}.txt\n"
        f"- runtime_filter_state: {article_meta.get('filter_state') or ''}\n"
        f"- runtime_last_stage: {article_meta.get('last_stage') or ''}\n"
        f"- refreshed_live_source: {'true' if refreshed_live_source else 'false'}\n"
    )


def build_ticket_body(source_url: str, selection_source: str) -> str:
    return (
        "# Intake Ticket\n\n"
        "This ticket was imported from the Hermes-native Sapho discovery runtime for compact Daily proving.\n\n"
        f"- URL: {source_url}\n"
        "- Channel: native-runtime-replay\n"
        f"- Selection: {selection_source}\n"
    )


def build_article_body() -> str:
    return (
        "# Pending Article\n\n"
        "This article was imported from the Hermes-native Sapho discovery runtime and is waiting for Curator.\n"
    )


LOW_QUALITY_SOURCE_PATTERNS = [
    re.compile(pattern, re.IGNORECASE)
    for pattern in [
        r"skip to content",
        r"navigation menu",
        r"toggle navigation",
        r"appearance settings",
        r"try github copilot",
        r"customer stories",
        r"subscribe",
        r"newsletter",
        r"community article published",
    ]
]

ALWAYS_REFRESH_SOURCE_DOMAINS = [
    "blog.jetbrains.com/",
]


def source_looks_low_quality(source_text: str) -> bool:
    head = re.sub(r"\s+", " ", (source_text or "")[:2500]).strip().lower()
    if not head:
        return True
    matches = sum(1 for pattern in LOW_QUALITY_SOURCE_PATTERNS if pattern.search(head))
    return matches >= 2


def maybe_refresh_live_source(source_url: str, source_text: str) -> tuple[str, str, str, int, str, bool]:
    should_force_refresh = any(domain in (source_url or "").lower() for domain in ALWAYS_REFRESH_SOURCE_DOMAINS)
    if not source_url or (not should_force_refresh and not source_looks_low_quality(source_text)):
        return "", source_text, "runtime-import", 0, "", False
    try:
        raw_text, title, content_type, status_code = fetch_url(source_url)
    except Exception:
        return "", source_text, "runtime-import", 0, "", False
    if "html" in content_type:
        refreshed_text = best_effort_html_to_text(source_url, raw_text)
        capture_kind = "html-refresh"
    elif "text/" in content_type or content_type in {"application/xml", "application/xhtml+xml"}:
        refreshed_text = raw_text
        capture_kind = "text-refresh"
    else:
        return "", source_text, "runtime-import", 0, "", False
    if len((refreshed_text or "").strip()) < 400:
        return "", source_text, "runtime-import", 0, "", False
    return title, refreshed_text, capture_kind, status_code, content_type, True


def build_import_item(article_id: str, selection_rank: int, selection_source: str, *, refresh_live: bool = False) -> dict[str, Any]:
    runtime_article = article_stub_path(article_id)
    runtime_source_json = source_json_path(article_id)
    runtime_source_txt = source_txt_path(article_id)
    item: dict[str, Any] = {
        "articleId": article_id,
        "selectionRank": selection_rank,
        "runtimeArticlePath": str(runtime_article),
        "runtimeSourceJsonPath": str(runtime_source_json),
        "runtimeSourceTxtPath": str(runtime_source_txt),
    }
    try:
        article_meta, _article_body = load_runtime_markdown(runtime_article)
    except Exception as exc:
        item["action"] = "missing-runtime-article"
        item["error"] = str(exc)
        return item
    source_meta: dict[str, Any] = {}
    source_text = ""
    has_runtime_source = True
    try:
        source_meta = sudo_load_json(runtime_source_json)
    except Exception:
        has_runtime_source = False
    try:
        source_text = sudo_read_text(runtime_source_txt)
    except Exception:
        has_runtime_source = False

    source_url = str(article_meta.get("source_url") or source_meta.get("sourceUrl") or "").strip()
    canonical_url = canonicalize_article_url(
        str(article_meta.get("canonical_url") or source_meta.get("canonicalUrl") or source_url)
    )
    title = str(source_meta.get("title") or article_meta.get("artifact_title") or source_url or article_id).strip()
    queued_at = str(article_meta.get("discovered_at_utc") or source_meta.get("generatedAtUtc") or utc_now())
    captured_at = str(source_meta.get("generatedAtUtc") or article_meta.get("updated_at_utc") or queued_at)
    capture_kind = "runtime-import"
    http_status = int(source_meta.get("httpStatus") or 0)
    content_type = str(source_meta.get("contentType") or "")
    refreshed = False
    if refresh_live:
        refreshed_title, source_text, capture_kind, http_status, content_type, refreshed = maybe_refresh_live_source(
            source_url,
            source_text,
        )
        if refreshed_title:
            title = refreshed_title.strip()
    ticket_id = import_ticket_id(article_id)
    paths = local_paths(article_id)
    existing = {name: str(path) for name, path in paths.items() if path.exists()}
    item.update(
        {
            "sourceUrl": source_url,
            "canonicalUrl": canonical_url,
            "sourceTitle": title,
            "queuedAtUtc": queued_at,
            "capturedAtUtc": captured_at,
            "ticketId": ticket_id,
            "selectionSource": selection_source,
            "runtimeFilterState": article_meta.get("filter_state") or "",
            "runtimeLastStage": article_meta.get("last_stage") or "",
            "refreshedLiveSource": refreshed,
            "paths": {name: str(path) for name, path in paths.items()},
            "existingPaths": existing,
        }
    )
    if len(existing) == len(paths):
        item["action"] = "skip-existing"
        return item

    item["action"] = "would-import" if has_runtime_source else "would-import-ticket-only"
    ticket_status = "captured" if has_runtime_source else "queued"
    article_status = "pending"
    article_body = build_article_body()
    duplicate_fields = {}
    item["_write"] = {
        "ticket": (
            {
                "version": "intake-ticket.v1",
                "ticket_id": ticket_id,
                "source_url": source_url,
                "canonical_url": canonical_url,
                "source_channel": "native-runtime-replay",
                "queued_at_utc": queued_at,
                "status": ticket_status,
                "article_id": article_id,
                "operator_note": f"Imported from Hermes-native runtime via {selection_source}",
                **duplicate_fields,
            },
            build_ticket_body(source_url, selection_source),
        ),
    }
    if has_runtime_source:
        item["_write"].update({
            "article": (
                {
                    "version": "article.v1",
                    "article_id": article_id,
                    "ticket_id": ticket_id,
                    "source_url": source_url,
                    "source_title": title,
                    "queued_at_utc": queued_at,
                    "captured_at_utc": captured_at,
                    "canonical_url": canonical_url,
                    "curator_decision": "pending",
                    "artifact_minted_at_utc": "",
                    "evidence_count": 0,
                    "claim_count": 0,
                    "publication_status": article_status,
                    "imported_from_runtime_article_id": article_id,
                    "imported_from_runtime_last_stage": str(article_meta.get("last_stage") or ""),
                    "imported_from_runtime_filter_state": str(article_meta.get("filter_state") or ""),
                    **duplicate_fields,
                },
                article_body,
            ),
            "source": (
                {
                    "version": "source-capture.v1",
                    "article_id": article_id,
                    "ticket_id": ticket_id,
                    "source_url": source_url,
                    "canonical_url": canonical_url,
                    "source_title": title,
                    "capture_kind": capture_kind,
                    "http_status": http_status,
                    "content_type": content_type,
                    "captured_at_utc": captured_at,
                },
                build_source_body(title, source_text, article_meta, source_meta, refreshed_live_source=refreshed),
            ),
        })
    return item


def write_import_item(item: dict[str, Any]) -> None:
    paths = local_paths(item["articleId"])
    payload = item.pop("_write")
    ticket_meta, ticket_body = payload["ticket"]
    write_markdown(paths["ticket"], ticket_meta, ticket_body)
    if "article" in payload:
        article_meta, article_body = payload["article"]
        write_article_markdown(paths["article"], article_meta, article_body)
    if "source" in payload:
        source_meta, source_body = payload["source"]
        write_markdown(paths["source"], source_meta, source_body)
    item["action"] = "imported" if "article" in payload else "imported-ticket-only"


def summarize_actions(items: list[dict[str, Any]]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for item in items:
        action = str(item.get("action") or "unknown")
        counts[action] = counts.get(action, 0) + 1
    return counts


def public_item(item: dict[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in item.items() if not key.startswith("_")}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--article-id", action="append", dest="article_ids", default=[])
    parser.add_argument("--article-ids-file")
    parser.add_argument("--batch-size", type=int)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--refresh-live", action="store_true")
    args = parser.parse_args()

    requested_ids = list(args.article_ids or [])
    if args.article_ids_file:
        requested_ids.extend(load_id_file(Path(args.article_ids_file)))

    if requested_ids:
        order = dedupe_ordered(requested_ids)
        selection_meta = {
            "kind": "explicit-list",
            "providedCount": len(order),
        }
    else:
        order, selection_meta = load_default_order()

    if args.batch_size is not None:
        order = order[: max(args.batch_size, 0)]
        selection_meta["batchSize"] = max(args.batch_size, 0)

    selection_source = str(selection_meta.get("kind") or "unknown")
    items = [
        build_import_item(article_id, index, selection_source, refresh_live=args.refresh_live)
        for index, article_id in enumerate(order, start=1)
    ]

    if not args.dry_run:
        for item in items:
            if item.get("action") == "would-import":
                write_import_item(item)

    result = {
        "mode": "dry-run" if args.dry_run else "write",
        "generatedAtUtc": utc_now(),
        "selection": selection_meta,
        "selectedCount": len(order),
        "actionCounts": summarize_actions(items),
        "items": [public_item(item) for item in items],
    }
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
