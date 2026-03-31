#!/usr/bin/env python3
"""
Executable multi-source discovery feeder for the atomic article-bundle pipeline.

The live behavior aggregates Brave, RSS, sitemap, and arXiv sources before applying
dedupe and canonical article-bundle creation limits.
"""

from __future__ import annotations

import argparse
import collections
import datetime as dt
import json
import os
import random
import re
import time
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Any
from urllib.parse import urlencode, urlsplit
from urllib.request import Request, urlopen

from schema_guard_local import validate_payload

from url_utils_local import canonicalize_url, domain_from_url, is_blocked_domain, sha256_text, source_signatures
from article_bundle_store_local import ensure_article_bundle_for_discovery, list_article_bundle_paths, load_article_bundle

ROOT = Path(__file__).resolve().parents[1]
DISCOVERY_DIR = ROOT / "discovery"
DISCOVERY_LOGS_DIR = ROOT / "state" / "discovery" / "logs"
DISCOVERY_SCOREBOARD = ROOT / "state" / "discovery" / "query-yield-scoreboard.jsonl"
DISCOVERY_SCHEMA = DISCOVERY_DIR / "schemas" / "discovery-event.schema.json"
DISCOVERY_CONFIG = DISCOVERY_DIR / "config.seed.yaml"


CHANNEL_PRIORITY = {
    'arxiv': 90,
    'rss': 75,
    'sitemap': 45,
    'brave': 60,
}
HIGH_SIGNAL_HOSTS = {
    'arxiv.org',
    'aclanthology.org',
    'anthropic.com',
    'openai.com',
    'developers.googleblog.com',
    'developer.microsoft.com',
    'learn.microsoft.com',
    'github.com',
}
LOW_SIGNAL_HOSTS = {
    'reddit.com',
    'medium.com',
}
POSITIVE_TERMS = {
    'agent',
    'benchmark',
    'bench',
    'eval',
    'evaluation',
    'incident',
    'memory',
    'postmortem',
    'reasoning',
    'reliability',
    'sandbox',
    'security',
    'swe-bench',
    'telemetry',
    'tool',
}
NEGATIVE_TERMS = {
    'best',
    'comparison',
    'comprehensive overview',
    'frameworks',
    'listicle',
    'reddit',
    'roundup',
    'top 5',
    'top five',
    'which framework',
}
DEFAULT_RECENCY_DAYS = 14


def append_jsonl(path: Path, row: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('a', encoding='utf-8') as handle:
        handle.write(json.dumps(row, ensure_ascii=False) + '\n')


def _active_bundle_sets() -> tuple[set[str], set[str], int]:
    canonicals: set[str] = set()
    signatures: set[str] = set()
    pending_count = 0
    for bundle_path in list_article_bundle_paths():
        bundle = load_article_bundle(bundle_path)
        fm = bundle.get('frontmatter') or {}
        canonical = canonicalize_url(str(fm.get('canonical_url') or fm.get('source_url') or '').strip())
        if canonical:
            canonicals.add(canonical)
            signatures.update(source_signatures(canonical))
        if str(fm.get('filter_state') or '').strip() == 'pending':
            pending_count += 1
    return canonicals, signatures, pending_count


def now_utc() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _indent(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def _extract_list_after_key(lines: list[str], key: str) -> list[str]:
    for i, line in enumerate(lines):
        if line.strip().startswith(f"{key}:"):
            base = _indent(line)
            vals: list[str] = []
            j = i + 1
            while j < len(lines):
                ln = lines[j]
                s = ln.strip()
                if not s:
                    j += 1
                    continue
                ind = _indent(ln)
                if ind <= base:
                    break
                if s.startswith("- "):
                    v = s[2:].strip().strip('"').strip("'")
                    vals.append(v)
                j += 1
            return vals
    return []


def _extract_scalar(lines: list[str], key: str, cast=str, default=None):
    pat = re.compile(rf"^\s*{re.escape(key)}\s*:\s*(.+?)\s*$")
    for ln in lines:
        m = pat.match(ln)
        if not m:
            continue
        raw = m.group(1).strip().strip('"').strip("'")
        try:
            return cast(raw)
        except Exception:
            return default
    return default


def load_seed_config(path: Path) -> dict[str, Any]:
    defaults = {
        "queries": [
            "SWE-bench verified agentic coding results",
            "AI coding agent incident postmortem",
            "agent observability tracing telemetry architecture",
            "LLM agent memory benchmark software tasks",
        ],
        "query_pool": [],
        "queries_per_run": 8,
        "per_query_limit": 15,
        "recency_filter": "week",
        "recency_days": DEFAULT_RECENCY_DAYS,
        "maxPendingNonXBeforePause": 12,
        "blocklist_domains": ["x.com", "twitter.com"],
        "allowlist_patterns": ["/research/", "/blog/", "/papers/", "/publications/", "/posts/"],
        "rss_feeds": [],
        "sitemap_roots": [],
        "arxiv_categories": [],
        "arxiv_keywords": [],
        "arxiv_max_results": 25,
        "max_per_source_key": 8,
    }

    if not path.exists():
        return defaults

    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    queries = _extract_list_after_key(lines, "queries") or defaults["queries"]
    query_pool = _extract_list_after_key(lines, "query_pool") or defaults["query_pool"]
    blocklist = _extract_list_after_key(lines, "blocklist_domains") or defaults["blocklist_domains"]
    allowlist = _extract_list_after_key(lines, "allowlist_patterns") or defaults["allowlist_patterns"]
    rss_feeds = _extract_list_after_key(lines, "feeds") or defaults["rss_feeds"]
    sitemap_roots = _extract_list_after_key(lines, "roots") or defaults["sitemap_roots"]
    arxiv_categories = _extract_list_after_key(lines, "categories") or defaults["arxiv_categories"]
    arxiv_keywords = _extract_list_after_key(lines, "keywords") or defaults["arxiv_keywords"]
    queries_per_run = _extract_scalar(lines, "queries_per_run", int, defaults["queries_per_run"])
    per_query_limit = _extract_scalar(lines, "per_query_limit", int, defaults["per_query_limit"])
    recency_filter = _extract_scalar(lines, "recency_filter", str, defaults["recency_filter"])
    recency_days = _extract_scalar(lines, "recency_days", int, defaults["recency_days"])
    max_backlog = _extract_scalar(lines, "maxPendingNonXBeforePause", int, defaults["maxPendingNonXBeforePause"])
    arxiv_max_results = _extract_scalar(lines, "max_results", int, defaults["arxiv_max_results"])
    max_per_source_key = _extract_scalar(lines, "max_per_source_key", int, defaults["max_per_source_key"])

    return {
        "queries": queries,
        "query_pool": query_pool,
        "queries_per_run": queries_per_run,
        "per_query_limit": per_query_limit,
        "recency_filter": recency_filter,
        "recency_days": recency_days,
        "maxPendingNonXBeforePause": max_backlog,
        "blocklist_domains": blocklist,
        "allowlist_patterns": allowlist,
        "rss_feeds": rss_feeds,
        "sitemap_roots": sitemap_roots,
        "arxiv_categories": arxiv_categories,
        "arxiv_keywords": arxiv_keywords,
        "arxiv_max_results": arxiv_max_results,
        "max_per_source_key": max(1, int(max_per_source_key or defaults["max_per_source_key"])),
    }


def select_run_queries(cfg: dict[str, Any], run_id: str) -> list[str]:
    base = [str(q).strip() for q in (cfg.get("queries") or []) if str(q).strip()]
    pool = [str(q).strip() for q in (cfg.get("query_pool") or []) if str(q).strip()]

    requested = int(cfg.get("queries_per_run") or 0)
    if not pool or requested <= 0:
        selected = base + pool
    else:
        k = min(requested, len(pool))
        rng = random.Random(sha256_text(run_id)[:16])
        sampled = rng.sample(pool, k)
        selected = base + sampled

    deduped: list[str] = []
    seen: set[str] = set()
    for q in selected:
        key = q.lower()
        if key in seen:
            continue
        seen.add(key)
        deduped.append(q)

    order_rng = random.Random(sha256_text(f"{run_id}:query-order")[:16])
    order_rng.shuffle(deduped)
    return deduped


def fetch_brave_results(
    *,
    query: str,
    count: int,
    freshness: str | None,
    api_key: str,
    max_retries: int = 2,
    base_backoff_seconds: float = 0.8,
) -> list[dict[str, Any]]:
    params = {"q": query, "count": count}
    if freshness:
        params["freshness"] = freshness
    url = "https://api.search.brave.com/res/v1/web/search?" + urlencode(params)

    last_err: Exception | None = None
    for attempt in range(max_retries + 1):
        try:
            req = Request(
                url,
                headers={
                    "Accept": "application/json",
                    "X-Subscription-Token": api_key,
                    "User-Agent": "OpenClaw-Firehose/1.0",
                },
            )
            with urlopen(req, timeout=30) as response:
                payload = json.loads(response.read().decode("utf-8", errors="replace"))
            return payload.get("web", {}).get("results", [])
        except Exception as exc:
            last_err = exc
            if attempt >= max_retries:
                break
            sleep_seconds = base_backoff_seconds * (2 ** attempt) + random.uniform(0.0, 0.35)
            time.sleep(sleep_seconds)

    raise RuntimeError(f"brave_fetch_failed:{type(last_err).__name__}")


def _request_text(url: str, *, headers: dict[str, str] | None = None, timeout: int = 30) -> str:
    req = Request(url, headers=headers or {"User-Agent": "OpenClaw-Firehose/1.0"})
    with urlopen(req, timeout=timeout) as response:
        return response.read().decode("utf-8", errors="replace")


def _parse_datetime(raw: str) -> dt.datetime | None:
    value = str(raw or '').strip()
    if not value:
        return None
    try:
        parsed = parsedate_to_datetime(value)
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=dt.timezone.utc)
        return parsed.astimezone(dt.timezone.utc)
    except Exception:
        pass
    try:
        parsed = dt.datetime.fromisoformat(value.replace('Z', '+00:00'))
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=dt.timezone.utc)
        return parsed.astimezone(dt.timezone.utc)
    except Exception:
        return None


def _is_recent(raw: str, recency_days: int) -> bool:
    parsed = _parse_datetime(raw)
    if parsed is None:
        return True
    cutoff = dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=max(1, recency_days))
    return parsed >= cutoff


def _tag_name(value: str) -> str:
    return value.rsplit('}', 1)[-1].lower()


def _child_text(node: ET.Element, *names: str) -> str:
    for child in list(node):
        if _tag_name(child.tag) in names:
            return (child.text or '').strip()
    return ''


def _child_attr(node: ET.Element, name: str, attr: str) -> str:
    for child in list(node):
        if _tag_name(child.tag) == name:
            return str(child.attrib.get(attr) or '').strip()
    return ''


def _title_from_url(url: str) -> str:
    path = urlsplit(url).path.strip('/')
    if not path:
        return urlsplit(url).netloc or url
    return path.split('/')[-1].replace('-', ' ').replace('_', ' ').strip() or url


def fetch_rss_results(
    *,
    feeds: list[str],
    recency_days: int,
    max_items_per_feed: int = 12,
) -> tuple[list[dict[str, Any]], list[dict[str, str]]]:
    results: list[dict[str, Any]] = []
    errors: list[dict[str, str]] = []
    for feed in feeds:
        try:
            body = _request_text(feed, timeout=20)
            root = ET.fromstring(body)
        except Exception as exc:
            errors.append({'channel': 'rss', 'queryOrFeed': feed, 'error': str(exc)})
            continue
        collected = 0
        for item in root.iter():
            tag = _tag_name(item.tag)
            if tag not in {'item', 'entry'}:
                continue
            title = _child_text(item, 'title')
            url = _child_text(item, 'link') or _child_attr(item, 'link', 'href')
            snippet = _child_text(item, 'description', 'summary', 'content')
            published = _child_text(item, 'pubdate', 'updated', 'published', 'lastbuilddate')
            if not _is_recent(published, recency_days):
                continue
            results.append(
                {
                    'channel': 'rss',
                    'queryOrFeed': feed,
                    'url': url,
                    'title': title,
                    'snippet': snippet[:800],
                    'publishedAtUtc': published,
                    'rank': collected + 1,
                }
            )
            collected += 1
            if collected >= max_items_per_feed:
                break
    return results, errors


def fetch_sitemap_results(
    *,
    roots: list[str],
    recency_days: int,
    allowlist_patterns: list[str],
    max_items_per_root: int = 12,
    max_nested_sitemaps: int = 6,
) -> tuple[list[dict[str, Any]], list[dict[str, str]]]:
    results: list[dict[str, Any]] = []
    errors: list[dict[str, str]] = []
    for root in roots:
        try:
            body = _request_text(root, timeout=20)
            xml_root = ET.fromstring(body)
        except Exception as exc:
            errors.append({'channel': 'sitemap', 'queryOrFeed': root, 'error': str(exc)})
            continue

        documents: list[tuple[str, ET.Element]] = [(root, xml_root)]
        nested_locs = [
            _child_text(node, 'loc')
            for node in xml_root.iter()
            if _tag_name(node.tag) == 'sitemap' and _child_text(node, 'loc')
        ]
        for nested in nested_locs[: max(0, int(max_nested_sitemaps))]:
            try:
                nested_body = _request_text(nested, timeout=20)
                documents.append((nested, ET.fromstring(nested_body)))
            except Exception as exc:
                errors.append({'channel': 'sitemap', 'queryOrFeed': nested, 'error': str(exc)})

        collected = 0
        for _, document_root in documents:
            for node in document_root.iter():
                if _tag_name(node.tag) != 'url':
                    continue
                loc = _child_text(node, 'loc')
                lastmod = _child_text(node, 'lastmod')
                if not loc:
                    continue
                if allowlist_patterns and not any(pattern in loc for pattern in allowlist_patterns):
                    continue
                if not _is_recent(lastmod, recency_days):
                    continue
                results.append(
                    {
                        'channel': 'sitemap',
                        'queryOrFeed': root,
                        'url': loc,
                        'title': _title_from_url(loc),
                        'snippet': f'sitemap lastmod={lastmod}' if lastmod else '',
                        'publishedAtUtc': lastmod,
                        'rank': collected + 1,
                    }
                )
                collected += 1
                if collected >= max_items_per_root:
                    break
            if collected >= max_items_per_root:
                break
    return results, errors


def fetch_arxiv_results(
    *,
    categories: list[str],
    keywords: list[str],
    max_results: int,
    recency_days: int,
) -> list[dict[str, Any]]:
    if not categories:
        return []
    category_query = '+OR+'.join(f'cat:{category}' for category in categories)
    url = (
        'https://export.arxiv.org/api/query?'
        + urlencode(
            {
                'search_query': category_query,
                'start': 0,
                'max_results': max_results,
                'sortBy': 'submittedDate',
                'sortOrder': 'descending',
            }
        )
    )
    body = _request_text(url, timeout=30)
    root = ET.fromstring(body)
    results: list[dict[str, Any]] = []
    lowered_keywords = [str(keyword).strip().lower() for keyword in keywords if str(keyword).strip()]
    for index, entry in enumerate(root.iter(), start=0):
        if _tag_name(entry.tag) != 'entry':
            continue
        title = _child_text(entry, 'title')
        summary = _child_text(entry, 'summary')
        published = _child_text(entry, 'published', 'updated')
        if not _is_recent(published, recency_days):
            continue
        haystack = f'{title} {summary}'.lower()
        if lowered_keywords and not any(keyword in haystack for keyword in lowered_keywords):
            continue
        url = ''
        for child in list(entry):
            if _tag_name(child.tag) != 'link':
                continue
            rel = str(child.attrib.get('rel') or '').strip().lower()
            href = str(child.attrib.get('href') or '').strip()
            if rel in {'alternate', ''} and href:
                url = href
                break
        url = url or _child_text(entry, 'id')
        results.append(
            {
                'channel': 'arxiv',
                'queryOrFeed': 'arxiv:' + ','.join(categories),
                'url': url,
                'title': title,
                'snippet': summary[:800],
                'publishedAtUtc': published,
                'rank': index + 1,
            }
        )
    return results


def load_brave_api_key() -> str:
    key = os.getenv("BRAVE_API_KEY", "").strip()
    if key:
        return key

    cfg_path = Path.home() / ".openclaw" / "openclaw.json"
    try:
        data = json.loads(cfg_path.read_text(encoding="utf-8"))
        key2 = data.get("tools", {}).get("web", {}).get("search", {}).get("apiKey", "")
        if isinstance(key2, str):
            return key2.strip()
    except Exception:
        pass
    return ""


def _record_priority(record: dict[str, Any]) -> int:
    score = CHANNEL_PRIORITY.get(str(record.get('channel') or ''), 0)
    host = domain_from_url(str(record.get('url') or ''))
    text = ' '.join(
        [
            str(record.get('queryOrFeed') or ''),
            str(record.get('title') or ''),
            str(record.get('snippet') or ''),
            str(record.get('url') or ''),
        ]
    ).lower()

    if host in HIGH_SIGNAL_HOSTS:
        score += 18
    if host in LOW_SIGNAL_HOSTS:
        score -= 25
    for term in POSITIVE_TERMS:
        if term in text:
            score += 3
    for term in NEGATIVE_TERMS:
        if term in text:
            score -= 6
    rank = int(record.get('rank') or 99)
    score -= max(0, rank - 1)
    return score


def _make_event(*, run_id: str, record: dict[str, Any], decision: str, reason: str) -> dict[str, Any]:
    url = str(record.get('url') or '').strip()
    canonical = canonicalize_url(url)
    return {
        "runId": run_id,
        "channel": str(record.get('channel') or '').strip(),
        "queryOrFeed": str(record.get('queryOrFeed') or '').strip(),
        "url": url,
        "title": str(record.get('title') or ''),
        "snippet": str(record.get('snippet') or ''),
        "rank": int(record.get('rank') or 0),
        "decision": decision,
        "decisionReason": reason,
        "retrievedAtUtc": now_utc(),
        "canonicalUrl": canonical,
        "urlHash": sha256_text(canonicalize_url(url)),
        "canonicalUrlHash": sha256_text(canonical),
    }


def _channel_stats() -> dict[str, Any]:
    return {"candidates": 0, "kept": 0, "dropped": 0, "queryErrors": 0, "reasonCounts": collections.Counter()}


def _query_stats() -> dict[str, Any]:
    return {"candidates": 0, "kept": 0, "dropped": 0, "queryErrors": 0, "reasonCounts": collections.Counter()}


def _bump_reason(stats: dict[str, Any], reason: str) -> None:
    counters = stats.setdefault('reasonCounts', collections.Counter())
    counters[str(reason or 'unknown')] += 1


def _serialize_stats_map(stats_map: dict[str, dict[str, Any]]) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    for key, stats in stats_map.items():
        out[str(key)] = {
            'candidates': int(stats.get('candidates', 0)),
            'kept': int(stats.get('kept', 0)),
            'dropped': int(stats.get('dropped', 0)),
            'queryErrors': int(stats.get('queryErrors', 0)),
            'reasonCounts': dict(stats.get('reasonCounts') or {}),
        }
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default=str(DISCOVERY_CONFIG))
    ap.add_argument("--logs-dir", default=str(DISCOVERY_LOGS_DIR))
    ap.add_argument("--scoreboard", default=str(DISCOVERY_SCOREBOARD))
    ap.add_argument("--discovery-schema", default=str(DISCOVERY_SCHEMA))
    ap.add_argument("--run-id", default="")
    ap.add_argument("--max-new", type=int, default=60)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    ts = now_utc()
    run_id = args.run_id or dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    cfg = load_seed_config(Path(args.config))
    active_queries = select_run_queries(cfg, run_id)
    existing, existing_signatures, pending_count = _active_bundle_sets()
    paused = pending_count > int(cfg["maxPendingNonXBeforePause"])

    logs_dir = Path(args.logs_dir)
    logs_dir.mkdir(parents=True, exist_ok=True)
    events_path = logs_dir / f"discovery-events-{run_id}.jsonl"
    run_path = logs_dir / f"run-{run_id}.json"

    if paused:
        summary = {
            "runId": run_id,
            "generatedAtUtc": ts,
            "paused": True,
            "pauseReason": "pending_articles_above_threshold",
            "pendingArticles": pending_count,
            "maxPendingBeforePause": cfg["maxPendingNonXBeforePause"],
            "inserted": 0,
            "eventsPath": str(events_path),
        }
        run_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(json.dumps(summary, indent=2, ensure_ascii=False))
        return 0

    inserted_ids: list[str] = []
    inserted_urls: list[str] = []
    reason_counts = collections.Counter()
    duplicate_domains = collections.Counter()
    channel_breakdown: dict[str, dict[str, Any]] = collections.defaultdict(_channel_stats)
    query_errors: list[dict[str, str]] = []
    brave_per_query: dict[str, dict[str, Any]] = {query: _query_stats() for query in active_queries}

    raw_records: list[dict[str, Any]] = []
    brave_api_key = load_brave_api_key()
    if brave_api_key:
        for query in active_queries:
            try:
                results = fetch_brave_results(
                    query=query,
                    count=int(cfg["per_query_limit"]),
                    freshness=cfg.get("recency_filter"),
                    api_key=brave_api_key,
                )
            except Exception as exc:
                channel_breakdown['brave']['queryErrors'] += 1
                brave_per_query[query]['queryErrors'] += 1
                query_errors.append({'channel': 'brave', 'queryOrFeed': query, 'error': str(exc)})
                continue
            for rank, result in enumerate(results, start=1):
                raw_records.append(
                    {
                        'channel': 'brave',
                        'queryOrFeed': query,
                        'url': str(result.get('url') or '').strip(),
                        'title': str(result.get('title') or ''),
                        'snippet': str(result.get('description') or ''),
                        'rank': rank,
                    }
                )
    else:
        query_errors.append({'channel': 'brave', 'queryOrFeed': 'config', 'error': 'missing_brave_api_key'})

    try:
        rss_payload = fetch_rss_results(
            feeds=list(cfg.get('rss_feeds') or []),
            recency_days=int(cfg.get('recency_days') or DEFAULT_RECENCY_DAYS),
        )
        rss_records, rss_errors = rss_payload if isinstance(rss_payload, tuple) else (rss_payload, [])
        raw_records.extend(rss_records)
        query_errors.extend(rss_errors)
        channel_breakdown['rss']['queryErrors'] += len(rss_errors)
    except Exception as exc:
        channel_breakdown['rss']['queryErrors'] += 1
        query_errors.append({'channel': 'rss', 'queryOrFeed': 'feeds', 'error': str(exc)})

    try:
        sitemap_payload = fetch_sitemap_results(
            roots=list(cfg.get('sitemap_roots') or []),
            recency_days=int(cfg.get('recency_days') or DEFAULT_RECENCY_DAYS),
            allowlist_patterns=list(cfg.get('allowlist_patterns') or []),
        )
        sitemap_records, sitemap_errors = sitemap_payload if isinstance(sitemap_payload, tuple) else (sitemap_payload, [])
        raw_records.extend(sitemap_records)
        query_errors.extend(sitemap_errors)
        channel_breakdown['sitemap']['queryErrors'] += len(sitemap_errors)
    except Exception as exc:
        channel_breakdown['sitemap']['queryErrors'] += 1
        query_errors.append({'channel': 'sitemap', 'queryOrFeed': 'roots', 'error': str(exc)})

    try:
        arxiv_payload = fetch_arxiv_results(
            categories=list(cfg.get('arxiv_categories') or []),
            keywords=list(cfg.get('arxiv_keywords') or []),
            max_results=int(cfg.get('arxiv_max_results') or 25),
            recency_days=int(cfg.get('recency_days') or DEFAULT_RECENCY_DAYS),
        )
        arxiv_records, arxiv_errors = arxiv_payload if isinstance(arxiv_payload, tuple) else (arxiv_payload, [])
        raw_records.extend(arxiv_records)
        query_errors.extend(arxiv_errors)
        channel_breakdown['arxiv']['queryErrors'] += len(arxiv_errors)
    except Exception as exc:
        channel_breakdown['arxiv']['queryErrors'] += 1
        query_errors.append({'channel': 'arxiv', 'queryOrFeed': 'categories', 'error': str(exc)})

    scored_records: list[dict[str, Any]] = []
    for record in raw_records:
        channel = str(record.get('channel') or '').strip()
        source_key = str(record.get('queryOrFeed') or '').strip() or channel
        channel_breakdown[channel]['candidates'] += 1
        if channel == 'brave' and source_key in brave_per_query:
            brave_per_query[source_key]['candidates'] += 1
        record['score'] = _record_priority(record)
        scored_records.append(record)

    scored_records.sort(key=lambda item: (int(item.get('score') or 0), -int(item.get('rank') or 0)), reverse=True)

    seen_canonical: set[str] = set()
    seen_signatures: set[str] = set()
    eligible_records: list[dict[str, Any]] = []
    events: list[dict[str, Any]] = []
    for record in scored_records:
        channel = str(record.get('channel') or '').strip()
        source_key = str(record.get('queryOrFeed') or '').strip() or channel
        url = str(record.get('url') or '').strip()
        canonical = canonicalize_url(url)
        signatures = source_signatures(url)
        record['sourceSignatures'] = sorted(signatures)

        decision = 'kept'
        reason = 'passes_filters'
        if not url:
            decision, reason = 'dropped', 'missing_url'
        elif is_blocked_domain(url, list(cfg.get('blocklist_domains') or [])):
            decision, reason = 'dropped', 'blocked_domain'
        elif canonical in existing or canonical in seen_canonical:
            decision, reason = 'dropped', 'duplicate_canonical'
            duplicate_domains[domain_from_url(canonical)] += 1
        elif signatures & existing_signatures:
            decision, reason = 'dropped', 'historical_source_duplicate'
            duplicate_domains[domain_from_url(canonical)] += 1
        elif signatures & seen_signatures:
            decision, reason = 'dropped', 'source_signature_duplicate'
            duplicate_domains[domain_from_url(canonical)] += 1

        event = _make_event(run_id=run_id, record=record, decision=decision, reason=reason)
        try:
            validate_payload(event, args.discovery_schema)
        except Exception:
            channel_breakdown[channel]['dropped'] += 1
            reason_counts['schema_validation_error'] += 1
            _bump_reason(channel_breakdown[channel], 'schema_validation_error')
            if channel == 'brave' and source_key in brave_per_query:
                brave_per_query[source_key]['dropped'] += 1
                _bump_reason(brave_per_query[source_key], 'schema_validation_error')
            continue

        if decision == 'dropped':
            events.append(event)
            channel_breakdown[channel]['dropped'] += 1
            reason_counts[reason] += 1
            _bump_reason(channel_breakdown[channel], reason)
            if channel == 'brave' and source_key in brave_per_query:
                brave_per_query[source_key]['dropped'] += 1
                _bump_reason(brave_per_query[source_key], reason)
            continue

        seen_canonical.add(canonical)
        seen_signatures.update(signatures)
        eligible_records.append(record)

    novel_eligible_total = len(eligible_records)
    selected_counts_by_source_key = collections.Counter()
    max_per_source_key = int(cfg.get('max_per_source_key') or 8)
    kept_canonicals: set[str] = set()
    for record in eligible_records:
        channel = str(record.get('channel') or '').strip()
        source_key = str(record.get('queryOrFeed') or '').strip() or channel
        canonical = canonicalize_url(str(record.get('url') or '').strip())
        if len(inserted_ids) >= int(args.max_new):
            decision, reason = 'dropped', 'run_cap_reached'
        elif selected_counts_by_source_key[source_key] >= max_per_source_key:
            decision, reason = 'dropped', 'source_key_cap_reached'
        elif canonical in kept_canonicals:
            decision, reason = 'dropped', 'duplicate_canonical'
        else:
            decision, reason = 'kept', 'passes_filters'

        event = _make_event(run_id=run_id, record=record, decision=decision, reason=reason)
        events.append(event)
        if decision == 'kept':
            bundle = ensure_article_bundle_for_discovery(
                source_url=str(record.get('url') or '').strip(),
                canonical_url=canonical,
                discovered_at_utc=ts,
                title_hint=str(record.get('title') or '').strip(),
            )
            article_id = str((bundle.get('frontmatter') or {}).get('article_id') or '').strip()
            if article_id:
                inserted_ids.append(article_id)
                inserted_urls.append(canonical)
                existing.add(canonical)
                kept_canonicals.add(canonical)
                existing_signatures.update(source_signatures(canonical))
                selected_counts_by_source_key[source_key] += 1
            channel_breakdown[channel]['kept'] += 1
            _bump_reason(channel_breakdown[channel], reason)
            if channel == 'brave' and source_key in brave_per_query:
                brave_per_query[source_key]['kept'] += 1
                _bump_reason(brave_per_query[source_key], reason)
        else:
            channel_breakdown[channel]['dropped'] += 1
            _bump_reason(channel_breakdown[channel], reason)
            if channel == 'brave' and source_key in brave_per_query:
                brave_per_query[source_key]['dropped'] += 1
                _bump_reason(brave_per_query[source_key], reason)
        reason_counts[reason] += 1

    if events:
        with events_path.open('a', encoding='utf-8') as handle:
            for event in events:
                handle.write(json.dumps(event, ensure_ascii=False) + '\n')

    scoreboard_rows_written = 0
    if not args.dry_run:
        scoreboard_path = Path(args.scoreboard)
        week = iso_week_label()
        for query, stats in brave_per_query.items():
            row = {
                'week': week,
                'runId': run_id,
                'query': query,
                'channel': 'brave',
                'candidates': int(stats.get('candidates', 0)),
                'kept': int(stats.get('kept', 0)),
                'dropped': int(stats.get('dropped', 0)),
                'duplicateCanonical': int((stats.get('reasonCounts') or {}).get('duplicate_canonical', 0)),
                'sourceKeyCapReached': int((stats.get('reasonCounts') or {}).get('source_key_cap_reached', 0)),
                'queryErrors': int(stats.get('queryErrors', 0)),
                'deepDives': 0,
                'avgTechnicalDensity': 0.0,
                'avgNovelty': 0.0,
                'action': 'observed',
            }
            append_jsonl(scoreboard_path, row)
            scoreboard_rows_written += 1

    summary = {
        'runId': run_id,
        'generatedAtUtc': ts,
        'paused': False,
        'dryRun': bool(args.dry_run),
        'queries': len(active_queries),
        'selectedQueries': active_queries,
        'baseQueries': len(cfg.get('queries') or []),
        'queryPool': len(cfg.get('query_pool') or []),
        'queriesPerRun': int(cfg.get('queries_per_run') or 0),
        'perQueryLimit': int(cfg.get('per_query_limit') or 0),
        'maxPerSourceKey': max_per_source_key,
        'pendingArticlesBeforeRun': pending_count,
        'candidatesTotal': len(raw_records),
        'novelEligibleTotal': novel_eligible_total,
        'kept': len(inserted_ids),
        'dropped': max(0, len(events) - len(inserted_ids)),
        'inserted': 0 if args.dry_run else len(inserted_ids),
        'insertedIds': [] if args.dry_run else inserted_ids,
        'insertedCanonicalUrls': [] if args.dry_run else inserted_urls,
        'queryErrors': len(query_errors),
        'queryErrorDetails': query_errors,
        'reasonCounts': dict(reason_counts),
        'channelBreakdown': _serialize_stats_map(channel_breakdown),
        'bravePerQuery': _serialize_stats_map(brave_per_query),
        'topDuplicateDomains': [
            {'domain': domain, 'count': count}
            for domain, count in duplicate_domains.most_common(10)
            if domain
        ],
        'eventsPath': str(events_path),
        'articlesRoot': '/home/openclaw/.openclaw/workspace/research/articles',
        'scoreboardPath': str(Path(args.scoreboard)),
        'scoreboardRowsWritten': scoreboard_rows_written,
    }

    run_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    return 0

def iso_week_label(ts: dt.datetime | None = None) -> str:
    value = ts or dt.datetime.now(dt.timezone.utc)
    year, week, _ = value.isocalendar()
    return f"{year}-W{week:02d}"


if __name__ == "__main__":
    raise SystemExit(main())
