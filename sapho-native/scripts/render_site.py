from __future__ import annotations

import html
import json
import os
import re
import shutil
import subprocess
from datetime import UTC, datetime
from email.utils import format_datetime
from pathlib import Path
from xml.etree.ElementTree import Element, SubElement, register_namespace, tostring

from common import (
    ARTICLES_DIR,
    DAILY_DIR,
    PUBLIC_DIR,
    assert_unique_canonical_records,
    build_article_record,
    canonical_signatures,
    choose_preferred_signature,
    ensure_dir,
    html_to_text,
    parse_markdown,
    read_markdown,
    render_markdown,
    slugify,
)

BASE_URL = "https://research.quiznat.com"
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PUBLIC_SEED_DIR = Path("/home/openclaw/.openclaw/workspace/website")
PUBLIC_SEED_ENV_VAR = "SAPHO_PUBLIC_SEED_DIR"

COMPAT_ALIAS_REDIRECTS = {
    "20260327001": {
        "artifact_alias": "20260303004",
        "source_url": "https://arxiv.org/abs/2601.20404",
        "title": "AGENTS.md Boosts AI Coding Agent Efficiency",
    },
}
RUNTIME_CHARTER = Path("/home/openclaw/.openclaw/workspace/research/contracts/sapho-chapterhouse-institute-charter.md")
LIVE_FACTORY_CHECKIN_LATEST = Path('/home/openclaw/.openclaw/workspace/research/factory/checkins/article-checkin-latest.json')
STATE_DIR = ROOT / "state"
RSS_REGISTRY_PATH = STATE_DIR / "rss-registry.json"
RSS_VALIDATION_PATH = STATE_DIR / "rss-validation-latest.json"
RSS_SOURCE_PATTERN = re.compile(r"\n\nArtifact: (?P<artifact>\S+) · Source: (?P<source>\S+)\s*$")
INTERNAL_ID_PATTERN = re.compile(r"\b(?:art-\d{4}-\d{2}-\d{2}-\d{3}|claim-\d+|evidence-\d+)\b")


def now_utc() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def ensure_parent(path: Path) -> None:
    ensure_dir(path.parent)


def write_text(path: Path, text: str) -> None:
    ensure_parent(path)
    path.write_text(text, encoding="utf-8")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def public_seed_dir() -> Path:
    configured = os.environ.get(PUBLIC_SEED_ENV_VAR, "").strip()
    if not configured:
        return DEFAULT_PUBLIC_SEED_DIR
    candidate = Path(configured).expanduser()
    if not candidate.is_absolute():
        candidate = (ROOT / candidate).resolve()
    return candidate


def prune_overlay_dir(path: Path, allowed_names: set[str]) -> None:
    if not path.exists():
        return
    for child in path.iterdir():
        if child.name not in allowed_names and child.is_file():
            child.unlink()


def reset_public_dir() -> None:
    seed_dir = public_seed_dir()
    if not seed_dir.is_dir():
        raise RuntimeError(f"public_seed_dir_missing:{seed_dir}")
    ensure_dir(PUBLIC_DIR)
    proc = subprocess.run([
        'rsync',
        '-a',
        '--delete',
        f'{seed_dir}/',
        f'{PUBLIC_DIR}/',
    ], text=True, capture_output=True)
    if proc.returncode != 0:
        detail = (proc.stderr or proc.stdout or '').strip() or 'seed_sync_failed'
        raise RuntimeError(f'public_seed_sync_failed:{detail}')


def strip_frontmatter(text: str) -> str:
    if not text.startswith("---\n"):
        return text
    try:
        _meta, body = parse_markdown(text)
    except Exception:
        return text
    return body


def first_paragraph(text: str) -> str:
    cleaned = [block.strip() for block in text.strip().split("\n\n") if block.strip()]
    if not cleaned:
        return ""
    if cleaned[0].startswith("# ") and len(cleaned) > 1:
        return " ".join(cleaned[1].split())
    return " ".join(cleaned[0].split())


def first_heading(text: str, fallback: str = "") -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip() or fallback
    return fallback


def parse_sections(body: str) -> dict[str, str]:
    sections: dict[str, str] = {}
    current_name: str | None = None
    current_lines: list[str] = []
    for line in body.splitlines():
        if line.startswith("## "):
            if current_name is not None:
                sections[current_name] = "\n".join(current_lines).strip()
            current_name = line[3:].strip()
            current_lines = []
            continue
        if current_name is not None:
            current_lines.append(line)
    if current_name is not None:
        sections[current_name] = "\n".join(current_lines).strip()
    return sections


def truncate_text(text: str, limit: int = 190) -> str:
    cleaned = " ".join(text.split())
    if len(cleaned) <= limit:
        return cleaned
    return cleaned[: limit - 1].rstrip() + "…"


def load_json(path: Path, default: dict | list | None = None):
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def strip_inline_markdown(text: str) -> str:
    cleaned = text or ""
    cleaned = re.sub(r"\*\*(.+?)\*\*", r"\1", cleaned)
    cleaned = re.sub(r"\*(.+?)\*", r"\1", cleaned)
    cleaned = re.sub(r"__(.+?)__", r"\1", cleaned)
    cleaned = re.sub(r"_(.+?)_", r"\1", cleaned)
    cleaned = re.sub(r"`(.+?)`", r"\1", cleaned)
    return cleaned


def visible_markdown_text(text: str) -> str:
    raw = strip_inline_markdown((text or "").strip())
    if not raw:
        return ""
    rendered = render_markdown(raw)
    visible = html_to_text(rendered)
    visible = strip_inline_markdown(visible)
    return " ".join(visible.split())


def public_article_url(alias: str) -> str:
    return f"{BASE_URL}/a/{alias}.html"


def public_source_url(alias: str) -> str:
    return f"{BASE_URL}/s/{alias}.html"


def normalize_url(value: str) -> str:
    cleaned = str(value or "").strip()
    if not cleaned:
        return ""
    if re.fullmatch(r"https?://[^/]+", cleaned):
        return cleaned
    return cleaned.rstrip("/")


def previous_public_rss() -> str | None:
    path = PUBLIC_DIR / "rss.xml"
    if path.exists():
        return read_text(path)
    return None


def parse_rfc2822(value: str) -> datetime:
    return datetime.strptime(value, "%a, %d %b %Y %H:%M:%S %z").astimezone(UTC)


def normalized_pubdate(value: str, link: str) -> str:
    raw = str(value or "").strip()
    if raw:
        try:
            return format_datetime(parse_rfc2822(raw))
        except Exception:
            pass
    match = re.fullmatch(rf"{re.escape(BASE_URL)}/a/(\d{{4}})(\d{{2}})(\d{{2}})\d{{3}}\.html", link)
    if match:
        derived = datetime(
            int(match.group(1)),
            int(match.group(2)),
            int(match.group(3)),
            0,
            0,
            0,
            tzinfo=UTC,
        )
        return format_datetime(derived)
    return format_datetime(datetime(1970, 1, 1, tzinfo=UTC))


def extract_source_url(description: str) -> str:
    match = RSS_SOURCE_PATTERN.search(description or "")
    if not match:
        return ""
    return normalize_url(match.group("source"))


def rss_description(summary: str, artifact_url: str, source_url: str) -> str:
    clean_summary = visible_markdown_text(summary)
    clean_summary = INTERNAL_ID_PATTERN.sub("an earlier published artifact", clean_summary)
    clean_summary = re.sub(r"\s+", " ", clean_summary).strip()
    return f"{clean_summary}\n\nArtifact: {artifact_url} · Source: {source_url}"


def parse_existing_rss(feed_text: str | None) -> list[dict]:
    if not feed_text:
        return []
    root = Element("rss")
    try:
        import xml.etree.ElementTree as ET

        root = ET.fromstring(feed_text)
    except Exception:
        return []
    items: list[dict] = []
    for node in root.findall("./channel/item"):
        link = str(node.findtext("link") or "").strip()
        guid = str(node.findtext("guid") or "").strip()
        title = str(node.findtext("title") or "").strip()
        description = str(node.findtext("description") or "").strip()
        pub_date = str(node.findtext("pubDate") or "").strip()
        items.append(
            {
                "title": title,
                "link": link,
                "guid": guid,
                "pubDate": normalized_pubdate(pub_date, link),
                "description": description,
                "source_url": extract_source_url(description),
            }
        )
    return items


def default_registry() -> dict:
    return {
        "version": "rss-registry.v1",
        "updatedAtUtc": now_utc(),
        "items": [],
    }


def seed_registry_from_feed(feed_text: str | None) -> dict:
    registry = default_registry()
    items = parse_existing_rss(feed_text)
    registry_items = []
    for item in items:
        link = str(item.get("link") or "").strip()
        title = str(item.get("title") or "").strip()
        description = str(item.get("description") or "").strip()
        source_url = str(item.get("source_url") or "").strip()
        pub_date = str(item.get("pubDate") or "").strip()
        summary = description.split("\n\nArtifact:", 1)[0].strip()
        alias = ""
        match = re.fullmatch(rf"{re.escape(BASE_URL)}/a/(\d{{11}})\.html", link)
        if match:
            alias = match.group(1)
        registry_items.append(
            {
                "source_url": normalize_url(source_url),
                "title": title,
                "link": link,
                "guid": link,
                "alias": alias,
                "pubDate": normalized_pubdate(pub_date, link),
                "description": rss_description(summary, link, normalize_url(source_url)),
            }
        )
    registry["items"] = registry_items
    return registry


def load_rss_registry(previous_feed_text: str | None) -> dict:
    registry = load_json(RSS_REGISTRY_PATH, None)
    if isinstance(registry, dict) and isinstance(registry.get("items"), list):
        return registry
    return seed_registry_from_feed(previous_feed_text)


def save_rss_registry(registry: dict) -> None:
    ensure_dir(STATE_DIR)
    registry["updatedAtUtc"] = now_utc()
    write_text(RSS_REGISTRY_PATH, json.dumps(registry, indent=2) + "\n")


def used_aliases(registry: dict) -> set[str]:
    aliases: set[str] = set()
    for item in registry.get("items") or []:
        alias = str(item.get("alias") or "").strip()
        if alias:
            aliases.add(alias)
    return aliases


def next_alias_for_date(registry: dict, daily_date: str) -> str:
    ymd = daily_date.replace("-", "")
    matches = []
    for alias in used_aliases(registry):
        if re.fullmatch(rf"{ymd}\d{{3}}", alias):
            matches.append(int(alias[-3:]))
    next_ordinal = (max(matches) if matches else 0) + 1
    return f"{ymd}{next_ordinal:03d}"


def html_redirect_page(title: str, target: str, message: str, button_label: str) -> str:
    safe_title = html.escape(title)
    safe_target = html.escape(target, quote=True)
    safe_message = html.escape(message)
    safe_button = html.escape(button_label)
    return (
        "<!doctype html>\n"
        "<html>\n"
        "<head>\n"
        '  <meta charset="utf-8" />\n'
        '  <meta name="viewport" content="width=device-width, initial-scale=1" />\n'
        f"  <title>{safe_title}</title>\n"
        f'  <meta http-equiv="refresh" content="0; url={safe_target}" />\n'
        '  <link rel="stylesheet" href="/assets/style.css?v=scholarly-20260314d" />\n'
        '  <link rel="icon" type="image/png" href="/assets/sapho-seal.png?v=seal-20260315" />\n'
        '  <link rel="apple-touch-icon" href="/assets/sapho-seal.png?v=seal-20260315" />\n'
        "</head>\n"
        "<body>\n"
        '  <main class="portal">\n'
        '    <section class="mentat-card scanlines">\n'
        f"      <h1>{safe_title}</h1>\n"
        f"      <p>{safe_message}</p>\n"
        f'      <p><a class="mentat-button" href="{safe_target}">{safe_button}</a></p>\n'
        "    </section>\n"
        "  </main>\n"
        f"  <script>location.replace({target!r});</script>\n"
        "</body>\n"
        "</html>\n"
    )


def build_daily_page_html(date: str, summary: str) -> str:
    safe_date = html.escape(date)
    safe_summary = html.escape(visible_markdown_text(summary) or "Daily package published.")
    technical_target = f"/viewer.html?file=briefs/{date}/technical-executive-report.md"
    executive_target = f"/viewer.html?file=briefs/{date}/executive-brief.md"
    archive_target = "/daily-briefing-archive.html"
    return (
        "<!doctype html>\n"
        "<html>\n"
        "<head>\n"
        '  <meta charset="utf-8" />\n'
        '  <meta name="viewport" content="width=device-width, initial-scale=1" />\n'
        f"  <title>Daily Briefing {safe_date}</title>\n"
        '  <link rel="stylesheet" href="/assets/style.css?v=scholarly-20260314d" />\n'
        '  <link rel="icon" type="image/png" href="/assets/sapho-seal.png?v=seal-20260315" />\n'
        '  <link rel="apple-touch-icon" href="/assets/sapho-seal.png?v=seal-20260315" />\n'
        "</head>\n"
        "<body>\n"
        '  <main class="portal">\n'
        '    <section class="mentat-card scanlines">\n'
        f"      <p class=\"meta\">Sapho Daily · {safe_date}</p>\n"
        f"      <h1>Daily Briefing — {safe_date}</h1>\n"
        f"      <p>{safe_summary}</p>\n"
        "      <p>Canonical publication surfaces for this Daily:</p>\n"
        "      <ul>\n"
        f"        <li><a href=\"{html.escape(technical_target, quote=True)}\">Technical Executive Report</a></li>\n"
        f"        <li><a href=\"{html.escape(executive_target, quote=True)}\">Executive Brief</a></li>\n"
        f"        <li><a href=\"{html.escape(archive_target, quote=True)}\">Daily Briefing Archive</a></li>\n"
        "      </ul>\n"
        "    </section>\n"
        "  </main>\n"
        "</body>\n"
        "</html>\n"
    )


def replace_first(text: str, old: str, new: str) -> str:
    return text.replace(old, new, 1)


def overwrite_charter() -> None:
    if RUNTIME_CHARTER.exists():
        write_text(PUBLIC_DIR / "charter.md", read_text(RUNTIME_CHARTER))


def latest_daily_date() -> str:
    dates = []
    for day_dir in DAILY_DIR.iterdir():
        if not day_dir.is_dir():
            continue
        if (day_dir / "technical-executive-report.md").exists() and (day_dir / "executive-brief.md").exists():
            dates.append(day_dir.name)
    if not dates:
        raise RuntimeError("no_current_brief_date")
    return sorted(dates)[-1]


def overlay_current_briefs(date: str) -> dict[str, str]:
    technical_source = DAILY_DIR / date / "technical-executive-report.md"
    executive_source = DAILY_DIR / date / "executive-brief.md"

    technical_raw = read_text(technical_source)
    executive_raw = read_text(executive_source)
    technical_meta, _technical_body = read_markdown(technical_source)
    executive_meta, _executive_body = read_markdown(executive_source)

    technical_public = strip_frontmatter(technical_raw).rstrip() + "\n"
    executive_public = strip_frontmatter(executive_raw).rstrip() + "\n"

    dated_dir = PUBLIC_DIR / "briefs" / date
    latest_dir = PUBLIC_DIR / "briefs" / "latest"
    ensure_dir(dated_dir)
    ensure_dir(latest_dir)

    write_text(dated_dir / "technical-executive-report.md", technical_public)
    write_text(dated_dir / "executive-brief.md", executive_public)
    write_text(latest_dir / "technical-executive-report.md", technical_public)
    write_text(latest_dir / "executive-brief.md", executive_public)

    write_text(
        dated_dir / "technical-executive-report.html",
        html_redirect_page(
            "Technical Executive Report",
            f"/viewer.html?file=briefs/{date}/technical-executive-report.md",
            "Redirecting to the canonical markdown view.",
            "Open Document",
        ),
    )
    write_text(
        dated_dir / "executive-brief.html",
        html_redirect_page(
            "Executive Brief",
            f"/viewer.html?file=briefs/{date}/executive-brief.md",
            "Redirecting to the canonical markdown view.",
            "Open Document",
        ),
    )

    write_text(
        latest_dir / "meta.json",
        json.dumps(
            {
                "latestDate": date,
                "generatedAtUtc": str(technical_meta.get("generated_at_utc") or executive_meta.get("generated_at_utc") or now_utc()),
                "version": "chapterhouse-portal-v1.3.0",
            },
            indent=2,
        )
        + "\n",
    )
    prune_overlay_dir(dated_dir, {"technical-executive-report.md", "technical-executive-report.html", "executive-brief.md", "executive-brief.html"})
    prune_overlay_dir(latest_dir, {"technical-executive-report.md", "technical-executive-report.html", "executive-brief.md", "executive-brief.html", "meta.json"})

    daily_dir = PUBLIC_DIR / "daily"
    ensure_dir(daily_dir)

    top_line_section = parse_sections(technical_public).get("Top-Line Judgments", "")
    bullet_summaries = [line[2:].strip() for line in top_line_section.splitlines() if line.strip().startswith("- ")]
    technical_summary = " ".join(bullet_summaries[:2]) if bullet_summaries else (first_paragraph(top_line_section) or first_paragraph(technical_public))
    technical_summary = visible_markdown_text(technical_summary)
    published_at = str(technical_meta.get("generated_at_utc") or executive_meta.get("generated_at_utc") or now_utc())
    write_text(daily_dir / f"{date}.html", build_daily_page_html(date, technical_summary))
    write_text(
        daily_dir / "latest.html",
        html_redirect_page(
            "Latest Daily Briefing",
            f"/daily/{date}.html",
            "Redirecting to the latest published Daily briefing page.",
            "Open Latest Daily",
        ),
    )
    return {
        "date": date,
        "summary": technical_summary,
        "published_at": published_at,
        "site_path": f"daily/{date}.html",
    }


def extract_bullet_lines(section_text: str) -> list[str]:
    lines = []
    for line in section_text.splitlines():
        stripped = line.strip()
        if stripped.startswith("- "):
            lines.append(stripped)
    return lines


def build_public_artifact_markdown(public_id: str, title: str, meta: dict, body: str) -> str:
    sections = parse_sections(body)
    core_thesis = sections.get("Core Thesis", "").strip()
    why_it_matters = sections.get("Why It Matters", "").strip()
    limits = sections.get("Limits", "").strip()
    findings = extract_bullet_lines(sections.get("Key Findings", ""))
    evidence = extract_bullet_lines(sections.get("Evidence Base", ""))

    alternate_sources = [str(value).strip() for value in (meta.get('alternate_source_urls') or []) if str(value).strip()]
    source_metadata_lines = [
        f"- Title: {title}\n",
        f"- URL: {meta.get('source_url', '')}\n",
        "- Source type: Sapho Daily artifact\n",
        f"- Curated at (UTC): {meta.get('captured_at_utc') or meta.get('queued_at_utc') or ''}\n",
        f"- Finalized at (UTC): {meta.get('artifact_minted_at_utc') or ''}\n",
    ]
    for alt_url in alternate_sources:
        source_metadata_lines.append(f"- Alternate surface: {alt_url}\n")

    parts = [
        f"# {title}\n\n",
        "## Source metadata\n",
        *source_metadata_lines,
        "\n",
        "## Core thesis\n",
        f"{core_thesis}\n\n" if core_thesis else "\n",
        "## Why it matters for Sapho\n",
        f"{why_it_matters}\n\n" if why_it_matters else "\n",
    ]

    if findings:
        parts.append("## Key findings\n")
        for item in findings:
            parts.append(f"{item}\n")
        parts.append("\n")

    if evidence:
        parts.append("## Evidence base\n")
        for item in evidence:
            parts.append(f"{item}\n")
        parts.append("\n")

    if limits:
        parts.append("## Limits\n")
        parts.append(f"{limits}\n")

    return "".join(parts).rstrip() + "\n"


def artifact_publication_is_current(meta: dict) -> bool:
    minted_at = str(meta.get("artifact_minted_at_utc") or "").strip()
    if not minted_at:
        return False
    return (
        str(meta.get("artifact_publication_status") or "") == "published"
        and str(meta.get("artifact_publication_minted_at_utc") or "").strip() == minted_at
    )


def collect_current_articles(registry: dict, include_ready_ids: set[str] | None = None) -> list[dict]:
    include_ready_ids = {str(article_id).strip() for article_id in (include_ready_ids or set()) if str(article_id).strip()}
    published: list[tuple[str, dict, str, dict]] = []
    for article_path in sorted(ARTICLES_DIR.glob("*/article.md")):
        meta, body = read_markdown(article_path)
        article_id = article_path.parent.name
        status = str(meta.get("publication_status") or "")
        record = build_article_record(meta, article_path=article_path)
        if status == "published":
            published.append((article_id, meta, body, record))
            continue
        if status != "ready-for-daily":
            continue
        if article_id not in include_ready_ids and not artifact_publication_is_current(meta):
            continue
        published.append((article_id, meta, body, record))

    published.sort(key=lambda item: (str(item[1].get("artifact_minted_at_utc") or ""), item[0]))
    assert_unique_canonical_records([record for _article_id, _meta, _body, record in published], context="render-site")
    items: list[dict] = []
    registry_items = list(registry.get("items") or [])
    registry_by_identity: dict[str, dict] = {}
    for item in registry_items:
        identity = registry_item_identity(item)
        if not identity:
            continue
        existing = registry_by_identity.get(identity)
        if existing is None or prefer_registry_item(item, existing) is item:
            registry_by_identity[identity] = item
    assigned_aliases = used_aliases(registry)

    for _article_key, meta, body, record in published:
        date = str(meta.get("published_in_daily") or str(meta.get("artifact_minted_at_utc") or "")[:10] or now_utc()[:10])
        source_url = normalize_url(str(record.get("canonical_url") or meta.get("source_url") or ""))
        existing = registry_by_identity.get(payload_item_identity({"url": source_url}))
        if existing:
            alias = str(existing.get("alias") or "")
        else:
            alias = next_alias_for_date({"items": [{"alias": value} for value in sorted(assigned_aliases)]}, date)
            assigned_aliases.add(alias)
        public_id = f"pub-{alias}"
        title = first_heading(body, str(meta.get("source_title") or public_id))
        title = re.sub(r"^\[[^\]]+\]\s*", "", title).strip() or public_id
        slug = slugify(title, fallback=f"article-{alias[-3:]}")
        artifact_name = f"queue-{alias}-{slug}.md"
        artifact_rel = f"artifacts/kb/queue/{artifact_name}"
        summary = first_paragraph(parse_sections(body).get("Core Thesis", "")) or first_paragraph(body)
        summary = visible_markdown_text(summary)
        link = public_article_url(alias)
        guid = link

        write_text(PUBLIC_DIR / artifact_rel, build_public_artifact_markdown(public_id, title, meta, body))
        write_text(
            PUBLIC_DIR / "a" / f"{alias}.html",
            html_redirect_page(
                title,
                f"{BASE_URL}/viewer.html?file={artifact_rel}",
                "Redirecting to the canonical Sapho artifact.",
                "Open Artifact",
            ),
        )
        write_text(
            PUBLIC_DIR / "s" / f"{alias}.html",
            html_redirect_page(
                f"{title} Source",
                source_url,
                "Redirecting to the canonical source URL.",
                "Open Source",
            ),
        )

        items.append(
            {
                "id": public_id,
                "alias": alias,
                "daily_date": date,
                "title": title,
                "summary": truncate_text(summary, 280),
                "url": source_url,
                "canonical_url": source_url,
                "published_at": str(meta.get("artifact_minted_at_utc") or now_utc()),
                "category": "agent-factory",
                "artifact_rel": artifact_rel,
                "link": link,
                "guid": guid,
            }
        )
    return items


def reconcile_rss_registry(registry: dict, current_items: list[dict]) -> dict:
    merged: dict[str, dict] = {}
    for item in registry.get("items") or []:
        candidate = dict(item)
        identity = registry_item_identity(candidate)
        if not identity:
            link = str(candidate.get("link") or "").strip()
            if not link:
                continue
            identity = f"link:{link}"
        existing = merged.get(identity)
        if existing is None or prefer_registry_item(candidate, existing) is candidate:
            merged[identity] = candidate

    for item in current_items:
        source_url = normalize_url(str(item.get("canonical_url") or item.get("url") or ""))
        identity = payload_item_identity({"url": source_url})
        existing = merged.get(identity)
        description = rss_description(str(item.get("summary") or ""), str(item["link"]), source_url)
        registry_item = {
            "source_url": source_url,
            "title": str(item.get("title") or ""),
            "link": str(item["link"]),
            "guid": str(item["guid"]),
            "alias": str(item["alias"]),
            "pubDate": format_datetime(datetime.fromisoformat(str(item["published_at"]).replace("Z", "+00:00"))),
            "description": description,
        }
        if existing is not None:
            existing.update(registry_item)
        else:
            merged[identity] = registry_item

    items = sorted(
        merged.values(),
        key=lambda item: (
            parse_rfc2822(str(item.get("pubDate") or "Thu, 01 Jan 1970 00:00:00 +0000")),
            str(item.get("link") or ""),
        ),
        reverse=True,
    )
    return {
        "version": "rss-registry.v1",
        "updatedAtUtc": now_utc(),
        "items": items,
    }


def current_item_to_payload_item(item: dict) -> dict:
    return {
        "id": item["id"],
        "title": item["title"],
        "displayTitle": item["title"],
        "summary": item["summary"],
        "url": item["url"],
        "dailyDate": item.get("daily_date"),
        "rssRevision": 0,
        "rssRepublishedAtUtc": None,
        "status": "processed",
        "decision": "retain",
        "laneTags": ["agent-factory"],
        "laneTagsOriginal": ["agent-factory"],
        "processedAtUtc": item["published_at"],
        "artifactSourcePath": f"research/{item['artifact_rel']}",
        "artifactWebPath": item["artifact_rel"],
        "historicalRegimeArtifact": False,
        "historicalRegimeNote": "",
    }


def payload_item_identity(item: dict) -> str:
    source_url = normalize_url(str(item.get("canonical_url") or item.get("url") or ""))
    if source_url:
        signatures = canonical_signatures(source_url)
        work_signatures = sorted(signature for signature in signatures if signature.startswith("work:"))
        if work_signatures:
            return f"sig:{work_signatures[0]}"
        preferred = choose_preferred_signature(signatures)
        if preferred:
            return f"sig:{preferred}"
        return f"url:{source_url}"
    artifact_path = str(item.get("artifactWebPath") or item.get("artifact_rel") or "").strip()
    if artifact_path:
        return f"artifact:{artifact_path}"
    return f"id:{str(item.get('id') or '').strip()}"


def registry_item_identity(item: dict) -> str:
    source_url = normalize_url(str(item.get("source_url") or item.get("canonical_url") or item.get("url") or ""))
    payload = {
        "url": source_url,
        "canonical_url": source_url,
        "artifactWebPath": str(item.get("artifactWebPath") or item.get("artifact_rel") or "").strip(),
        "id": str(item.get("id") or item.get("alias") or item.get("link") or "").strip(),
    }
    return payload_item_identity(payload)


def prefer_registry_item(candidate: dict, existing: dict) -> dict:
    candidate_alias = str(candidate.get("alias") or "")
    existing_alias = str(existing.get("alias") or "")
    if candidate_alias and existing_alias and candidate_alias != existing_alias:
        return candidate if candidate_alias < existing_alias else existing
    candidate_pub = str(candidate.get("pubDate") or "")
    existing_pub = str(existing.get("pubDate") or "")
    if candidate_pub and existing_pub and candidate_pub != existing_pub:
        return candidate if parse_rfc2822(candidate_pub) <= parse_rfc2822(existing_pub) else existing
    candidate_link = str(candidate.get("link") or "")
    existing_link = str(existing.get("link") or "")
    return candidate if candidate_link < existing_link else existing


def write_compat_alias_redirects() -> None:
    for alias, target in COMPAT_ALIAS_REDIRECTS.items():
        artifact_alias = str(target.get("artifact_alias") or "").strip()
        title = str(target.get("title") or artifact_alias or alias)
        source_url = normalize_url(str(target.get("source_url") or ""))
        if artifact_alias:
            artifact_link = f"{BASE_URL}/a/{artifact_alias}.html"
            write_text(
                PUBLIC_DIR / "a" / f"{alias}.html",
                html_redirect_page(
                    title,
                    artifact_link,
                    "Redirecting to the canonical Sapho artifact alias.",
                    "Open Artifact",
                ),
            )
        if source_url:
            write_text(
                PUBLIC_DIR / "s" / f"{alias}.html",
                html_redirect_page(
                    f"{title} Source",
                    source_url,
                    "Redirecting to the canonical source URL.",
                    "Open Source",
                ),
            )


def prune_public_artifact_overlay(kept_items: list[dict], registry: dict) -> None:
    allowed_aliases = {str(item.get("alias") or "").strip() for item in (registry.get("items") or []) if str(item.get("alias") or "").strip()}
    allowed_aliases.update(COMPAT_ALIAS_REDIRECTS.keys())
    for dirname in ("a", "s"):
        target_dir = PUBLIC_DIR / dirname
        if not target_dir.exists():
            continue
        for path in target_dir.glob("*.html"):
            if path.stem not in allowed_aliases:
                path.unlink()

    allowed_artifacts = {kept_item_artifact_rel(item) for item in kept_items if kept_item_artifact_rel(item)}
    queue_dir = PUBLIC_DIR / "artifacts" / "kb" / "queue"
    if queue_dir.exists():
        for path in queue_dir.glob("*.md"):
            rel = str(path.relative_to(PUBLIC_DIR)).replace("\\", "/")
            if rel not in allowed_artifacts:
                path.unlink()


def payload_item_sort_key(item: dict) -> tuple[str, str, str]:
    return (
        str(item.get("dailyDate") or str(item.get("processedAtUtc") or "")[:10]),
        str(item.get("processedAtUtc") or ""),
        str(item.get("id") or ""),
    )


def kept_item_meta_text(item: dict) -> str:
    daily_date = str(item.get("dailyDate") or "").strip()
    if daily_date:
        return f"Published {daily_date} · Sapho Daily"
    item_id = str(item.get("id") or "").strip()
    match = re.fullmatch(r"art-(\d{4}-\d{2}-\d{2})-\d{3}", item_id)
    if match:
        return f"Published {match.group(1)} · Sapho Archive"
    processed = str(item.get("processedAtUtc") or "").strip()[:10]
    if processed:
        return f"Published {processed} · Sapho Archive"
    return "Published earlier · Sapho Archive"


def kept_item_artifact_rel(item: dict) -> str:
    return str(item.get("artifactWebPath") or item.get("artifact_rel") or "").strip()


def build_kept_links_cards(items: list[dict]) -> str:
    cards: list[str] = []
    for item in items:
        title = str(item.get("displayTitle") or item.get("title") or "")
        summary = str(item.get("summary") or "")
        source_url = str(item.get("url") or "")
        artifact_rel = kept_item_artifact_rel(item)
        cards.append(
            "        <article class=\"report-card kept-card\">\n"
            f"      <p class=\"meta\">{html.escape(kept_item_meta_text(item))}</p>\n"
            f"      <h3>{html.escape(title)}</h3>\n"
            f"      <p class=\"kept-desc\">{html.escape(summary)}</p>\n"
            f"      <p class=\"kept-links\"><a href=\"{html.escape(source_url)}\" target=\"_blank\" rel=\"noopener\">source</a> · <a href=\"viewer.html?file={html.escape(artifact_rel)}\">artifact</a></p>\n"
            "    </article>"
        )
    return "".join(cards)


def overlay_kept_links(current_items: list[dict]) -> list[dict]:
    page_path = PUBLIC_DIR / "kept-links.html"
    page = read_text(page_path)
    data_path = PUBLIC_DIR / "data" / "kept-links.json"
    payload = json.loads(read_text(data_path))
    items = [dict(item) for item in (payload.get("items") or [])]

    baseline_kept = int(payload.get("keptCount") or len(items))
    baseline_processed = int(payload.get("processedCount") or payload.get("decisionedCount") or len(items))
    baseline_decisioned = int(payload.get("decisionedCount") or baseline_processed)

    inserted_count = 0
    for item in current_items:
        payload_item = current_item_to_payload_item(item)
        identity = payload_item_identity(payload_item)
        replacement_index = next((idx for idx, existing in enumerate(items) if payload_item_identity(existing) == identity), None)
        if replacement_index is None:
            items.append(payload_item)
            inserted_count += 1
        else:
            items[replacement_index] = payload_item

    ordered_items = sorted(items, key=payload_item_sort_key, reverse=True)
    page = re.sub(
        r"<div class=\"portal-grid\">.*?</div>",
        "<div class=\"portal-grid\">\n" + build_kept_links_cards(ordered_items) + "\n      </div>",
        page,
        count=1,
        flags=re.DOTALL,
    )
    page = re.sub(
        r"<p class=\"meta\">\d+ kept · \d+ decisioned · updated [^<]+</p>",
        (
            f'<p class="meta">{max(baseline_kept + inserted_count, len(ordered_items))} kept · '
            f'{max(baseline_decisioned + inserted_count, len(ordered_items))} decisioned · '
            f'updated {html.escape(now_utc())}</p>'
        ),
        page,
        count=1,
    )
    write_text(page_path, page)
    payload["last_updated"] = now_utc()
    payload["generatedAtUtc"] = payload["last_updated"]
    payload["processedCount"] = max(baseline_processed + inserted_count, len(ordered_items))
    payload["decisionedCount"] = max(baseline_decisioned + inserted_count, len(ordered_items))
    payload["keptCount"] = max(baseline_kept + inserted_count, len(ordered_items))
    decision_counts = payload.get("decisionCounts") or {}
    decision_counts["retain"] = max(int(decision_counts.get("retain") or baseline_kept) + inserted_count, len(ordered_items))
    payload["decisionCounts"] = decision_counts
    lane_counts = payload.get("laneCounts") or {}
    lane_counts["agent-factory"] = int(lane_counts.get("agent-factory") or 0) + inserted_count
    payload["laneCounts"] = lane_counts
    payload["items"] = ordered_items
    write_text(data_path, json.dumps(payload, indent=2) + "\n")
    return payload["items"]


def overlay_daily_archive(current_brief: dict[str, str]) -> None:
    page_path = PUBLIC_DIR / "daily-briefing-archive.html"
    page = read_text(page_path)
    new_row = (
        f"<tr><td>{html.escape(current_brief['date'])}</td>"
        f"<td>{html.escape(truncate_text(visible_markdown_text(current_brief['summary']), 180))}</td>"
        f"<td><a href='viewer.html?file=briefs/{html.escape(current_brief['date'])}/executive-brief.md'>Executive</a> · "
        f"<a href='viewer.html?file=briefs/{html.escape(current_brief['date'])}/technical-executive-report.md'>Technical</a> · "
        "<span class='muted'>Morning Synthesis (n/a)</span></td></tr>"
    )
    page = re.sub(
        r"(<tbody>\s*)",
        r"\1" + new_row,
        page,
        count=1,
    )
    page = re.sub(
        r"(<p class='meta'>version=chapterhouse-portal-v1\.3\.0 · last_updated=)([^<]+)(</p>)",
        lambda match: match.group(1) + now_utc() + match.group(3),
        page,
        count=1,
    )
    write_text(page_path, page)


def collect_public_brief_rows(current_brief: dict[str, str]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    briefs_root = PUBLIC_DIR / "briefs"
    latest_published_at = str(current_brief.get("published_at") or now_utc())
    for day_dir in sorted(briefs_root.iterdir(), reverse=True):
        if not day_dir.is_dir():
            continue
        if day_dir.name == "latest" or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", day_dir.name):
            continue
        technical_path = day_dir / "technical-executive-report.md"
        executive_path = day_dir / "executive-brief.md"
        if not technical_path.exists() or not executive_path.exists():
            continue
        technical_text = read_text(technical_path)
        summary = first_paragraph(parse_sections(technical_text).get("Top-Line Judgments", "")) or first_paragraph(technical_text)
        summary = visible_markdown_text(summary)
        published_at = latest_published_at if day_dir.name == current_brief["date"] else f"{day_dir.name}T00:00:00Z"
        rows.append(
            {
                "date": day_dir.name,
                "summary": summary,
                "published_at": published_at,
                "technical_rel": f"briefs/{day_dir.name}/technical-executive-report.md",
                "executive_rel": f"briefs/{day_dir.name}/executive-brief.md",
            }
        )
    rows.sort(key=lambda row: row["date"], reverse=True)
    return rows


def build_rss_items(registry: dict) -> str:
    register_namespace("dc", "http://purl.org/dc/elements/1.1/")
    rss = Element("rss", version="2.0")
    channel = SubElement(rss, "channel")
    SubElement(channel, "title").text = "Sapho Chapterhouse Institute Research Artifacts"
    SubElement(channel, "link").text = BASE_URL
    SubElement(channel, "description").text = "Retained research artifacts published by Sapho Chapterhouse Institute."
    SubElement(channel, "language").text = "en-us"
    SubElement(channel, "lastBuildDate").text = format_datetime(datetime.now(UTC))
    SubElement(channel, "generator").text = "parallel-sapho micro canonical rss"
    SubElement(channel, "ttl").text = "60"

    ordered_items = list(registry.get("items") or [])

    for item in ordered_items:
        node = SubElement(channel, "item")
        title = str(item.get("title") or "")
        link = str(item.get("link") or "")
        SubElement(node, "link").text = link
        SubElement(node, "title").text = title
        guid = SubElement(node, "guid")
        guid.set("isPermaLink", "true")
        guid.text = str(item.get("guid") or link)
        SubElement(node, "{http://purl.org/dc/elements/1.1/}creator").text = "Sapho Institute"
        pub_date = str(item.get("pubDate") or "")
        if pub_date:
            SubElement(node, "pubDate").text = pub_date
        description = str(item.get("description") or "")
        SubElement(node, "description").text = description
        for category in ["agent-factory"]:
            SubElement(node, "category").text = str(category)

    return tostring(rss, encoding="unicode")


def validate_rss_candidate(candidate_text: str, previous_feed_text: str | None) -> dict:
    ensure_dir(STATE_DIR)
    result = {
        "generatedAtUtc": now_utc(),
        "ok": False,
        "checks": {},
        "errors": [],
    }
    try:
        import xml.etree.ElementTree as ET

        root = ET.fromstring(candidate_text)
    except Exception as exc:
        result["errors"].append(f"xml_parse_failed:{exc}")
        write_text(RSS_VALIDATION_PATH, json.dumps(result, indent=2) + "\n")
        return result

    items = root.findall("./channel/item")
    result["checks"]["xml_parses"] = True

    ordered_pubdates: list[datetime] = []
    candidate_by_source: dict[str, dict] = {}
    candidate_items: list[dict] = []
    seen_source_urls: set[str] = set()
    for node in items:
        title = str(node.findtext("title") or "").strip()
        link = str(node.findtext("link") or "").strip()
        guid = str(node.findtext("guid") or "").strip()
        description = str(node.findtext("description") or "").strip()
        pub_date = str(node.findtext("pubDate") or "").strip()
        source_url = normalize_url(extract_source_url(description))
        if source_url:
            if source_url in seen_source_urls:
                result["errors"].append(f"duplicate_source_identity:{source_url}")
            seen_source_urls.add(source_url)
        candidate_by_source[source_url] = {
            "title": title,
            "link": link,
            "guid": guid,
            "pubDate": pub_date,
            "description": description,
        }
        candidate_items.append(
            {
                "title": title,
                "link": link,
                "guid": guid,
                "pubDate": pub_date,
                "description": description,
            }
        )

        if not re.fullmatch(rf"{re.escape(BASE_URL)}/a/\d{{11}}\.html", link):
            result["errors"].append(f"invalid_public_link:{link}")
        if guid != link:
            result["errors"].append(f"guid_not_public_link:{guid}")
        if INTERNAL_ID_PATTERN.search(" ".join([title, description])):
            result["errors"].append(f"internal_id_leak:{title}")
        if any(token in description for token in ["**", "__", "`", "<", ">"]):
            result["errors"].append(f"description_not_plain_text:{title}")
        if not RSS_SOURCE_PATTERN.search(description):
            result["errors"].append(f"description_shape_invalid:{title}")
        try:
            ordered_pubdates.append(parse_rfc2822(pub_date))
        except Exception:
            result["errors"].append(f"invalid_pubdate:{title}")

    result["checks"]["visible_fields_no_internal_ids"] = not any(err.startswith("internal_id_leak:") for err in result["errors"])
    result["checks"]["plain_text_descriptions"] = not any(err.startswith("description_") for err in result["errors"])
    result["checks"]["stable_public_identities"] = not any(err.startswith("invalid_public_link:") or err.startswith("guid_not_public_link:") for err in result["errors"])
    result["checks"]["newest_first_ordering"] = ordered_pubdates == sorted(ordered_pubdates, reverse=True)
    if not result["checks"]["newest_first_ordering"]:
        result["errors"].append("ordering_not_newest_first")

    previous_items = parse_existing_rss(previous_feed_text)
    previous_by_source = {
        normalize_url(str(item.get("source_url") or "")): item
        for item in previous_items
        if normalize_url(str(item.get("source_url") or ""))
    }
    identity_drift_errors = []
    for source_url, previous_item in previous_by_source.items():
        candidate_item = candidate_by_source.get(source_url)
        if not candidate_item:
            continue
        previous_pub = normalized_pubdate(str(previous_item.get("pubDate") or ""), str(previous_item.get("link") or ""))
        candidate_pub = normalized_pubdate(str(candidate_item.get("pubDate") or ""), str(candidate_item.get("link") or ""))
        if str(candidate_item.get("link") or "").strip() != str(previous_item.get("link") or "").strip():
            identity_drift_errors.append(f"identity_drift:{source_url}:link")
        if str(candidate_item.get("guid") or "").strip() != str(previous_item.get("guid") or "").strip():
            identity_drift_errors.append(f"identity_drift:{source_url}:guid")
        if candidate_pub != previous_pub:
            identity_drift_errors.append(f"identity_drift:{source_url}:pubDate")
    if identity_drift_errors:
        result["errors"].extend(identity_drift_errors)
    previous_links = {str(item.get("link") or "").strip() for item in previous_items if str(item.get("link") or "").strip()}
    candidate_links = {str(item.get("link") or "").strip() for item in candidate_items if str(item.get("link") or "").strip()}
    renumber_errors = []
    missing_links = sorted(previous_links - candidate_links)
    for link in missing_links:
        renumber_errors.append(f"missing_prior_link:{link}")
    for new in candidate_items:
        if str(new.get("guid") or "").strip() != str(new.get("link") or "").strip():
            renumber_errors.append(f"guid_not_link:{str(new.get('link') or '')}")
    if renumber_errors:
        result["errors"].extend(renumber_errors)
    result["checks"]["no_silent_renumbering"] = not renumber_errors
    result["checks"]["stable_source_identity"] = not any(err.startswith("identity_drift:") or err.startswith("duplicate_source_identity:") for err in result["errors"])

    result["itemCount"] = len(items)
    result["ok"] = not result["errors"]
    write_text(RSS_VALIDATION_PATH, json.dumps(result, indent=2) + "\n")
    return result


def build_daily_feed(brief_rows: list[dict[str, str]]) -> str:
    rss = Element("rss", version="2.0")
    channel = SubElement(rss, "channel")
    SubElement(channel, "title").text = "Sapho Chapterhouse Institute Daily Briefings"
    SubElement(channel, "link").text = f"{BASE_URL}/daily-briefing-archive.html"
    SubElement(channel, "description").text = "Daily executive and technical briefings published by Sapho Chapterhouse Institute."
    SubElement(channel, "language").text = "en-us"
    SubElement(channel, "lastBuildDate").text = format_datetime(datetime.now(UTC))
    SubElement(channel, "generator").text = "parallel-sapho legacy overlay"
    SubElement(channel, "ttl").text = "60"

    for row in brief_rows:
        node = SubElement(channel, "item")
        SubElement(node, "title").text = f"Technical Executive Report — {row['date']}"
        link = f"{BASE_URL}/viewer.html?file={row['technical_rel']}"
        SubElement(node, "link").text = link
        guid = SubElement(node, "guid")
        guid.set("isPermaLink", "false")
        guid.text = f"daily-{row['date']}"
        pub_date = str(row.get("published_at") or "")
        if pub_date:
            dt = datetime.fromisoformat(pub_date.replace("Z", "+00:00"))
            SubElement(node, "pubDate").text = format_datetime(dt)
        description = (
            f"{row.get('summary') or ''}\n\n"
            f"Technical: {BASE_URL}/viewer.html?file={row['technical_rel']} · "
            f"Executive: {BASE_URL}/viewer.html?file={row['executive_rel']}"
        )
        SubElement(node, "description").text = description

    return tostring(rss, encoding="unicode")


def render_site_inventory() -> None:
    files = sorted(path for path in PUBLIC_DIR.rglob("*") if path.is_file())
    lines = [str(path.relative_to(PUBLIC_DIR)).replace("\\", "/") for path in files]
    write_text(PUBLIC_DIR / "site-files.txt", "\n".join(lines) + "\n")
    json_items = []
    for path in files:
        rel = str(path.relative_to(PUBLIC_DIR)).replace("\\", "/")
        stat = path.stat()
        timestamp = datetime.fromtimestamp(stat.st_mtime, UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")
        json_items.append(
            {
                "path": rel,
                "absoluteUrl": f"{BASE_URL}/{rel}",
                "timestamp": timestamp,
                "suffix": path.suffix,
            }
        )
    write_text(PUBLIC_DIR / "site-files.json", json.dumps(json_items, indent=2) + "\n")
    write_text(
        PUBLIC_DIR / "index.json",
        json.dumps(
            {
                "version": "machine-index-v1.1.0",
                "last_updated": now_utc(),
                "update_cadence": "publish-run",
                "site": "research.quiznat.com",
                "start_here": "/agents-start-here.html",
                "regime": {"activeFounding": "Sapho Chapterhouse Institute Charter"},
                "inventory": {"text": "/site-files.txt", "json": "/site-files.json", "count": len(json_items)},
                "items": [
                    {
                        "title": "Sapho Chapterhouse Institute Charter",
                        "url": "/charter.md",
                        "absoluteUrl": f"{BASE_URL}/charter.md",
                        "timestamp": now_utc(),
                        "tags": ["canonical", "policy", "charter", "institute"],
                        "version": "schr-001-v2.1.0",
                        "priority": 1,
                    },
                    {
                        "title": "Latest Executive Brief (raw markdown)",
                        "url": "/briefs/latest/executive-brief.md",
                        "absoluteUrl": f"{BASE_URL}/briefs/latest/executive-brief.md",
                        "timestamp": now_utc(),
                        "tags": ["canonical", "briefing", "executive"],
                        "version": "daily-brief-latest",
                        "priority": 2,
                    },
                    {
                        "title": "Latest Strategic Insight Report (raw markdown)",
                        "url": "/briefs/latest/technical-executive-report.md",
                        "absoluteUrl": f"{BASE_URL}/briefs/latest/technical-executive-report.md",
                        "timestamp": now_utc(),
                        "tags": ["canonical", "briefing", "technical"],
                        "version": "technical-report-latest",
                        "priority": 3,
                    },
                ],
                "allFiles": json_items,
            },
            indent=2,
        )
        + "\n",
    )


def refresh_agents_page() -> None:
    page_path = PUBLIC_DIR / "agents-start-here.html"
    page = read_text(page_path)
    page = re.sub(
        r"(version=agents-start-here-v1\.1\.0 · last_updated=)([^<]+)",
        lambda match: match.group(1) + now_utc(),
        page,
        count=1,
    )
    write_text(page_path, page)




def validate_public_ops_surfaces() -> None:
    runtime_checkin = LIVE_FACTORY_CHECKIN_LATEST
    public_checkin = PUBLIC_DIR / 'artifacts' / 'ops' / 'factory-checkin-latest.json'
    if not runtime_checkin.exists():
        raise RuntimeError('runtime_checkin_missing')
    if not public_checkin.exists():
        raise RuntimeError('public_ops_checkin_missing')
    if read_text(public_checkin) != read_text(runtime_checkin):
        raise RuntimeError('public_ops_checkin_stale')

    ops_latest_path = PUBLIC_DIR / 'data' / 'ops-latest.json'
    if not ops_latest_path.exists():
        raise RuntimeError('ops_latest_missing')
    ops_latest = json.loads(read_text(ops_latest_path))
    if str(ops_latest.get('factoryCheckinLatestPath') or '') != 'artifacts/ops/factory-checkin-latest.json':
        raise RuntimeError('ops_latest_checkin_pointer_invalid')


def validate_public_alias_surfaces(current_items: list[dict]) -> None:
    for item in current_items:
        alias = str(item.get("alias") or "").strip()
        source_url = normalize_url(str(item.get("canonical_url") or item.get("url") or ""))
        if not alias:
            continue
        alias_path = PUBLIC_DIR / "a" / f"{alias}.html"
        source_path = PUBLIC_DIR / "s" / f"{alias}.html"
        if not alias_path.exists():
            raise RuntimeError(f"artifact_alias_missing:{alias}")
        if not source_path.exists():
            raise RuntimeError(f"source_alias_missing:{alias}")
        alias_text = read_text(alias_path)
        source_text = read_text(source_path)
        if "viewer.html?file=" not in alias_text:
            raise RuntimeError(f"artifact_alias_target_invalid:{alias}")
        if source_url and source_url not in source_text:
            raise RuntimeError(f"source_alias_target_invalid:{alias}")

    for alias, target in COMPAT_ALIAS_REDIRECTS.items():
        compat_path = PUBLIC_DIR / "a" / f"{alias}.html"
        if not compat_path.exists():
            raise RuntimeError(f"compat_alias_missing:{alias}")
        target_alias = str(target.get("artifact_alias") or "").strip()
        if target_alias and not (PUBLIC_DIR / "a" / f"{target_alias}.html").exists():
            raise RuntimeError(f"compat_alias_target_missing:{alias}->{target_alias}")


def validate_render(current_items: list[dict], current_brief: dict[str, str]) -> None:
    seed_dir = public_seed_dir()
    required = [
        PUBLIC_DIR / "viewer.html",
        PUBLIC_DIR / "charter.md",
        PUBLIC_DIR / "kept-links.html",
        PUBLIC_DIR / "daily-briefing-archive.html",
        PUBLIC_DIR / "daily" / f"{current_brief['date']}.html",
        PUBLIC_DIR / "briefs" / "latest" / "technical-executive-report.md",
        PUBLIC_DIR / "briefs" / "latest" / "executive-brief.md",
    ]
    for path in required:
        if not path.exists():
            raise RuntimeError(f"missing_required_surface:{path.relative_to(PUBLIC_DIR)}")

    if read_text(PUBLIC_DIR / "index.html") != read_text(seed_dir / "index.html"):
        raise RuntimeError("homepage_not_exact_seed")
    if read_text(PUBLIC_DIR / "viewer.html") != read_text(seed_dir / "viewer.html"):
        raise RuntimeError("viewer_not_exact_seed")
    if read_text(PUBLIC_DIR / "charter.html") != read_text(seed_dir / "charter.html"):
        raise RuntimeError("charter_wrapper_not_exact_seed")

    validate_public_ops_surfaces()

    kept_links = read_text(PUBLIC_DIR / "kept-links.html")
    validate_kept_links_surface(kept_links)
    legacy_payload = json.loads(read_text(seed_dir / "data" / "kept-links.json"))
    seed_kept = int(legacy_payload.get("keptCount") or 0)
    for item in current_items:
        if f"viewer.html?file={item['artifact_rel']}" not in kept_links:
            raise RuntimeError("new_artifact_missing_from_kept_links")
    kept_count_match = re.search(r"(\d+) kept", kept_links)
    if not kept_count_match:
        raise RuntimeError("kept_count_missing")
    current_kept = int(kept_count_match.group(1))
    if current_kept < seed_kept:
        raise RuntimeError("kept_count_regressed")

    archive = read_text(PUBLIC_DIR / "daily-briefing-archive.html")
    if f"<td>{current_brief['date']}</td>" not in archive:
        raise RuntimeError("current_day_missing_from_archive")
    if f"viewer.html?file=briefs/{current_brief['date']}/technical-executive-report.md" not in archive:
        raise RuntimeError("current_technical_missing_from_archive")
    dated_daily = read_text(PUBLIC_DIR / "daily" / f"{current_brief['date']}.html")
    if f"viewer.html?file=briefs/{current_brief['date']}/technical-executive-report.md" not in dated_daily:
        raise RuntimeError("dated_daily_missing_technical_link")
    if not (PUBLIC_DIR / "daily.xml").exists():
        raise RuntimeError("daily_feed_missing")


def validate_artifact_render(current_items: list[dict]) -> None:
    seed_dir = public_seed_dir()
    required = [
        PUBLIC_DIR / "viewer.html",
        PUBLIC_DIR / "kept-links.html",
        PUBLIC_DIR / "rss.xml",
        PUBLIC_DIR / "artifacts.xml",
    ]
    for path in required:
        if not path.exists():
            raise RuntimeError(f"missing_required_surface:{path.relative_to(PUBLIC_DIR)}")

    if read_text(PUBLIC_DIR / "index.html") != read_text(seed_dir / "index.html"):
        raise RuntimeError("homepage_not_exact_seed")
    if read_text(PUBLIC_DIR / "viewer.html") != read_text(seed_dir / "viewer.html"):
        raise RuntimeError("viewer_not_exact_seed")

    validate_public_ops_surfaces()

    kept_links = read_text(PUBLIC_DIR / "kept-links.html")
    validate_kept_links_surface(kept_links)
    if current_items and f"viewer.html?file={current_items[0]['artifact_rel']}" not in kept_links:
        raise RuntimeError("new_artifact_missing_from_kept_links")
    rss_text = read_text(PUBLIC_DIR / "rss.xml")
    if current_items and str(current_items[0]["link"]) not in rss_text:
        raise RuntimeError("new_artifact_missing_from_rss")


def validate_daily_briefing_render(current_brief: dict[str, str], seed_dir: Path) -> None:
    required = [
        PUBLIC_DIR / "viewer.html",
        PUBLIC_DIR / "kept-links.html",
        PUBLIC_DIR / "daily-briefing-archive.html",
        PUBLIC_DIR / "daily" / f"{current_brief['date']}.html",
        PUBLIC_DIR / "briefs" / "latest" / "technical-executive-report.md",
        PUBLIC_DIR / "briefs" / "latest" / "executive-brief.md",
        PUBLIC_DIR / "daily.xml",
    ]
    for path in required:
        if not path.exists():
            raise RuntimeError(f"missing_required_surface:{path.relative_to(PUBLIC_DIR)}")

    validate_public_ops_surfaces()

    for rel in [
        "kept-links.html",
        "data/kept-links.json",
        "rss.xml",
        "artifacts.xml",
        "data/artifacts-feed.json",
    ]:
        public_path = PUBLIC_DIR / rel
        seed_path = seed_dir / rel
        if seed_path.exists():
            if not public_path.exists():
                raise RuntimeError(f"pm_mutated_or_removed:{rel}")
            if read_text(public_path) != read_text(seed_path):
                raise RuntimeError(f"pm_mutated_artifact_surface:{rel}")

    archive = read_text(PUBLIC_DIR / "daily-briefing-archive.html")
    if f"<td>{current_brief['date']}</td>" not in archive:
        raise RuntimeError("current_day_missing_from_archive")
    dated_daily = read_text(PUBLIC_DIR / "daily" / f"{current_brief['date']}.html")
    if f"viewer.html?file=briefs/{current_brief['date']}/technical-executive-report.md" not in dated_daily:
        raise RuntimeError("dated_daily_missing_technical_link")


def validate_kept_links_surface(kept_links_html: str) -> None:
    payload = json.loads(read_text(PUBLIC_DIR / "data" / "kept-links.json"))
    missing: list[str] = []
    for item in payload.get("items") or []:
        artifact_rel = kept_item_artifact_rel(item)
        if artifact_rel and f"viewer.html?file={artifact_rel}" not in kept_links_html:
            missing.append(str(item.get("id") or artifact_rel))
    if missing:
        preview = ",".join(missing[:5])
        raise RuntimeError(f"kept_links_missing_payload_items:{preview}")


def render_artifact_site(include_ready_ids: set[str] | None = None) -> list[dict]:
    previous_feed_text = previous_public_rss()
    registry = load_rss_registry(previous_feed_text)
    reset_public_dir()
    current_items = collect_current_articles(registry, include_ready_ids=include_ready_ids)
    if not current_items:
        raise RuntimeError("no_artifact_items_to_publish")
    kept_items = overlay_kept_links(current_items)
    reconciled_registry = reconcile_rss_registry(registry, current_items)
    feed = build_rss_items(reconciled_registry)
    rss_validation = validate_rss_candidate(feed, previous_feed_text)
    if rss_validation.get("ok"):
        save_rss_registry(reconciled_registry)
        write_text(PUBLIC_DIR / "rss.xml", feed)
        write_text(PUBLIC_DIR / "artifacts.xml", feed)
    elif previous_feed_text:
        write_text(PUBLIC_DIR / "rss.xml", previous_feed_text)
        write_text(PUBLIC_DIR / "artifacts.xml", previous_feed_text)
    else:
        raise RuntimeError("rss_candidate_invalid_without_previous_feed")
    artifacts_feed_meta = {
        "generatedAtUtc": now_utc(),
        "channelTitle": "Sapho Chapterhouse Institute Research Artifacts",
        "feedPath": "/artifacts.xml",
        "mirrorPath": "/rss.xml",
        "itemCount": len((reconciled_registry.get("items") or []) if rss_validation.get("ok") else parse_existing_rss(previous_feed_text)),
        "sourceDataset": "state/rss-registry.json",
        "filter": "published_artifacts_only",
        "validationPath": str(RSS_VALIDATION_PATH.relative_to(ROOT)),
    }
    write_text(PUBLIC_DIR / "data" / "artifacts-feed.json", json.dumps(artifacts_feed_meta, indent=2) + "\n")
    write_compat_alias_redirects()
    validate_public_alias_surfaces(current_items)
    render_site_inventory()
    refresh_agents_page()
    validate_artifact_render(current_items)
    return current_items


def render_daily_briefing_site() -> dict[str, str]:
    seed_dir = public_seed_dir()
    reset_public_dir()
    current_brief = overlay_current_briefs(latest_daily_date())
    overlay_daily_archive(current_brief)
    brief_rows = collect_public_brief_rows(current_brief)
    write_text(PUBLIC_DIR / "daily.xml", build_daily_feed(brief_rows))
    render_site_inventory()
    refresh_agents_page()
    validate_daily_briefing_render(current_brief, seed_dir)
    return current_brief


def render_site() -> None:
    previous_feed_text = previous_public_rss()
    registry = load_rss_registry(previous_feed_text)
    reset_public_dir()
    current_brief = overlay_current_briefs(latest_daily_date())
    current_items = collect_current_articles(registry)
    kept_items = overlay_kept_links(current_items)
    overlay_daily_archive(current_brief)
    brief_rows = collect_public_brief_rows(current_brief)
    reconciled_registry = reconcile_rss_registry(registry, current_items)
    feed = build_rss_items(reconciled_registry)
    rss_validation = validate_rss_candidate(feed, previous_feed_text)
    if rss_validation.get("ok"):
        save_rss_registry(reconciled_registry)
        write_text(PUBLIC_DIR / "rss.xml", feed)
        write_text(PUBLIC_DIR / "artifacts.xml", feed)
    elif previous_feed_text:
        write_text(PUBLIC_DIR / "rss.xml", previous_feed_text)
        write_text(PUBLIC_DIR / "artifacts.xml", previous_feed_text)
    else:
        raise RuntimeError("rss_candidate_invalid_without_previous_feed")
    write_text(PUBLIC_DIR / "daily.xml", build_daily_feed(brief_rows))
    artifacts_feed_meta = {
        "generatedAtUtc": now_utc(),
        "channelTitle": "Sapho Chapterhouse Institute Research Artifacts",
        "feedPath": "/artifacts.xml",
        "mirrorPath": "/rss.xml",
        "itemCount": len((reconciled_registry.get("items") or []) if rss_validation.get("ok") else parse_existing_rss(previous_feed_text)),
        "sourceDataset": "state/rss-registry.json",
        "filter": "published_artifacts_only",
        "validationPath": str(RSS_VALIDATION_PATH.relative_to(ROOT)),
    }
    write_text(PUBLIC_DIR / "data" / "artifacts-feed.json", json.dumps(artifacts_feed_meta, indent=2) + "\n")
    write_compat_alias_redirects()
    validate_public_alias_surfaces(current_items)
    render_site_inventory()
    refresh_agents_page()
    validate_render(current_items, current_brief)


def main() -> int:
    render_site()
    print(PUBLIC_DIR)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
