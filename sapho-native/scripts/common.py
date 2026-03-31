from __future__ import annotations

import json
import os
import hashlib
import html
import re
from datetime import date
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
QUEUE_DIR = ROOT / "queue"
ARTICLES_DIR = ROOT / "articles"
DAILY_DIR = ROOT / "daily"
PUBLIC_DIR = ROOT / "public" / "site"
PERSONAS_DIR = ROOT / "personas"
from url_utils_local import canonicalize_url as runtime_canonicalize_url
from url_utils_local import extract_linked_paper_urls as runtime_extract_linked_paper_urls
from url_utils_local import source_identity_signatures as runtime_source_identity_signatures

DUPLICATE_REJECTED_STATUS = "duplicate-rejected"
TERMINAL_PUBLICATION_STATUSES = {
    "discarded",
    "capture-blocked",
    DUPLICATE_REJECTED_STATUS,
    "ready-for-daily",
    "published",
}
TERMINAL_SELECTOR_STATUSES = set(TERMINAL_PUBLICATION_STATUSES)
INACTIVE_PUBLICATION_STATUSES = {
    "discarded",
    "capture-blocked",
    DUPLICATE_REJECTED_STATUS,
}
KEPT_PUBLICATION_STATUSES = {
    "kept-awaiting-extraction",
    "kept-awaiting-article-synthesis",
    "kept-awaiting-article-claims",
    "kept-awaiting-article-write",
    "ready-for-daily",
    "published",
}
ARTIFACT_PUBLICATION_FIELDS = (
    "artifact_publication_status",
    "artifact_publication_alias",
    "artifact_publication_minted_at_utc",
    "artifact_publication_published_at_utc",
)
DAILY_PUBLICATION_FIELDS = ("published_in_daily",)
DUPLICATE_ONLY_FIELDS = (
    "duplicate_of_article_id",
    "duplicate_match_signature",
    "duplicate_rejected_at_utc",
    "alternate_surface_for_article_id",
)


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def utc_date() -> str:
    return utc_now()[:10]


def timestamp_for_date(replay_date: str | None = None) -> str:
    if not replay_date:
        return utc_now()
    return f"{replay_date}{utc_now()[10:]}"


def ensure_dir(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    return path


def env_flag(name: str) -> bool:
    value = str(os.environ.get(name, "")).strip().lower()
    return value in {"1", "true", "yes", "on"}


def normalize_name(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", (value or "").strip().lower()).strip("-")


def slugify(value: str, fallback: str = "item") -> str:
    cleaned = re.sub(r"[^a-zA-Z0-9]+", "-", (value or "").strip().lower()).strip("-")
    return cleaned or fallback


def display_title(value: str) -> str:
    text = (value or "").strip()
    text = re.sub(r"^\[[^\]]+\]\s*", "", text)
    if text.startswith("GitHub - "):
        text = re.sub(r"\s*[·-]\s*GitHub$", "", text).strip()
        text = re.sub(r"^GitHub - [^:]+:\s*", "", text).strip()
    text = re.sub(r"^WIP:\s*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"^#+\s*", "", text)
    text = re.sub(r"\s+\|\s+(?:Benched\.ai|Render Blog|Augment Code)$", "", text).strip()
    text = re.sub(r"\s+-\s+nilenso blog$", "", text, flags=re.IGNORECASE).strip()
    return text or "Untitled"


def _dedupe_paths(paths: list[Path]) -> list[Path]:
    seen: set[str] = set()
    result: list[Path] = []
    for path in paths:
        key = str(path)
        if key in seen:
            continue
        seen.add(key)
        result.append(path)
    return result


def resolve_persona_charter_path(
    persona: str,
    legacy_names: list[str] | tuple[str, ...] | None = (),
) -> Path | None:
    slug = normalize_name(persona)
    legacy_names = tuple(legacy_names or ())
    candidates = _dedupe_paths(
        [
            PERSONAS_DIR / slug / "agent.md",
            PERSONAS_DIR / slug / "persona.md",
            PERSONAS_DIR / f"{slug}.md",
            *[PERSONAS_DIR / f"{normalize_name(name)}.md" for name in legacy_names],
        ]
    )
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return None


def resolve_job_template_path(
    persona: str,
    job: str,
    legacy_names: list[str] | tuple[str, ...] | None = (),
) -> Path | None:
    persona_slug = normalize_name(persona)
    job_slug = normalize_name(job)
    legacy_names = tuple(legacy_names or ())
    job_variants = [job_slug]
    if persona_slug == "conclave" and job_slug == "gate":
        job_variants.extend(["daily-gate", "conclave-gate"])
    candidates = _dedupe_paths(
        [
            *[ROOT / "jobs" / persona_slug / f"{variant}.md" for variant in job_variants],
            *[ROOT / "jobs" / f"{persona_slug}-{variant}.md" for variant in job_variants],
            *[ROOT / "job-templates" / persona_slug / f"{variant}.md" for variant in job_variants],
            *[ROOT / "job_templates" / persona_slug / f"{variant}.md" for variant in job_variants],
            *[ROOT / "prompts" / persona_slug / f"{variant}.md" for variant in job_variants],
            *[PERSONAS_DIR / persona_slug / "jobs" / f"{variant}.md" for variant in job_variants],
            *[PERSONAS_DIR / f"{normalize_name(name)}.md" for name in legacy_names],
        ]
    )
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return None


def load_persona_charter(persona: str, legacy_names: list[str] | tuple[str, ...] = (), required: bool = True) -> str:
    path = resolve_persona_charter_path(persona, legacy_names=legacy_names)
    if path is None:
        if required:
            raise ValueError(f"missing_persona_charter:{persona}")
        return ""
    return path.read_text(encoding="utf-8").strip()


def load_job_template(
    persona: str,
    job: str,
    legacy_names: list[str] | tuple[str, ...] = (),
    required: bool = True,
) -> str:
    path = resolve_job_template_path(persona, job, legacy_names=legacy_names)
    if path is None:
        if required:
            raise ValueError(f"missing_job_template:{persona}:{job}")
        return ""
    return path.read_text(encoding="utf-8").strip()


def compose_persona_job_prompt(
    persona: str,
    job: str,
    *,
    legacy_persona_names: list[str] | tuple[str, ...] | None = (),
    legacy_job_names: list[str] | tuple[str, ...] | None = (),
    require_persona: bool = True,
    require_job: bool = False,
) -> str:
    persona_path = resolve_persona_charter_path(persona, legacy_names=legacy_persona_names)
    job_path = resolve_job_template_path(persona, job, legacy_names=legacy_job_names)
    if persona_path is None and require_persona:
        raise ValueError(f"missing_persona_charter:{persona}")
    if job_path is None and require_job:
        raise ValueError(f"missing_job_template:{persona}:{job}")
    if persona_path is None and job_path is None:
        raise ValueError(f"missing_prompt_binding:{persona}:{job}")
    if persona_path is not None and job_path is not None and persona_path == job_path:
        return persona_path.read_text(encoding="utf-8").strip()

    parts: list[str] = []
    if persona_path is not None:
        parts.append(persona_path.read_text(encoding="utf-8").strip())
    if job_path is not None:
        job_text = job_path.read_text(encoding="utf-8").strip()
        if parts:
            parts.append("Current Job Contract:\n\n" + job_text)
        else:
            parts.append(job_text)
    return "\n\n".join(part for part in parts if part.strip()).strip()


def default_agent_id(persona: str, job: str | None = None) -> str:
    slug = normalize_name(persona)
    if slug in {"curator", "extractor", "synthesist", "conclave"}:
        return slug
    if slug == "piter":
        return "main"
    if job is not None:
        return normalize_name(job)
    return slug or "curator"


def short_hash(value: str) -> str:
    return hashlib.sha1(value.encode("utf-8")).hexdigest()[:8]


def parse_markdown(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---\n"):
        raise ValueError("missing_frontmatter")
    parts = text.split("\n---\n", 1)
    if len(parts) != 2:
        raise ValueError("unterminated_frontmatter")
    meta = load_frontmatter(parts[0][4:])
    if not isinstance(meta, dict):
        raise ValueError("frontmatter_not_mapping")
    return normalize_yaml(meta), parts[1].lstrip("\n")


def load_frontmatter(text: str) -> dict[str, Any]:
    try:
        return yaml.safe_load(text) or {}
    except yaml.YAMLError:
        repaired = repair_frontmatter_text(text)
        return yaml.safe_load(repaired) or {}


def repair_frontmatter_text(text: str) -> str:
    repaired_lines: list[str] = []
    for line in text.splitlines():
        stripped = line.lstrip()
        indent = line[: len(line) - len(stripped)]
        if not stripped or stripped.startswith("- "):
            repaired_lines.append(line)
            continue
        if ":" not in stripped:
            repaired_lines.append(line)
            continue
        key, value = stripped.split(":", 1)
        if not value.startswith(" "):
            repaired_lines.append(line)
            continue
        scalar = value[1:]
        if not scalar:
            repaired_lines.append(line)
            continue
        if scalar.startswith(("'", '"', "|", ">")):
            repaired_lines.append(line)
            continue
        if scalar in {"true", "false", "null"}:
            repaired_lines.append(line)
            continue
        if re.fullmatch(r"[-+]?[0-9]+(?:\.[0-9]+)?", scalar):
            repaired_lines.append(line)
            continue
        if ":" in scalar:
            quoted = yaml.safe_dump(scalar, default_style='"').strip()
            repaired_lines.append(f"{indent}{key}: {quoted}")
            continue
        repaired_lines.append(line)
    return "\n".join(repaired_lines)


def normalize_yaml(value: Any) -> Any:
    if isinstance(value, dict):
        return {str(key): normalize_yaml(inner) for key, inner in value.items()}
    if isinstance(value, list):
        return [normalize_yaml(item) for item in value]
    if isinstance(value, datetime):
        return value.astimezone(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    if isinstance(value, date):
        return value.isoformat()
    return value


def dump_markdown(meta: dict[str, Any], body: str) -> str:
    frontmatter = yaml.safe_dump(meta, sort_keys=False, allow_unicode=False).strip()
    return f"---\n{frontmatter}\n---\n{body.rstrip()}\n"


def read_markdown(path: Path) -> tuple[dict[str, Any], str]:
    return parse_markdown(path.read_text(encoding="utf-8"))


def write_markdown(path: Path, meta: dict[str, Any], body: str) -> None:
    ensure_dir(path.parent)
    path.write_text(dump_markdown(meta, body), encoding="utf-8")


def read_body(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def markdown_section(text: str, heading: str) -> str:
    pattern = re.compile(rf"^{re.escape(heading)}\s*(?P<section>.*?)(?:\n## |\Z)", re.MULTILINE | re.DOTALL)
    match = pattern.search(text)
    if match is None:
        return ""
    return match.group("section").strip()


def ticket_path(ticket_id: str) -> Path:
    return QUEUE_DIR / f"{ticket_id}.md"


def article_dir(article_id: str) -> Path:
    return ARTICLES_DIR / article_id


def article_file(article_id: str) -> Path:
    return article_dir(article_id) / "article.md"


def source_file(article_id: str) -> Path:
    return article_dir(article_id) / "source.md"


def daily_dir(date: str) -> Path:
    return DAILY_DIR / date


def daily_file(date: str) -> Path:
    return daily_dir(date) / "daily.md"


def conclave_file(date: str) -> Path:
    return daily_dir(date) / "conclave.md"


def publish_file(date: str) -> Path:
    return daily_dir(date) / "publish.md"


def make_ticket_id(url: str, timestamp: str) -> str:
    return f"ticket-{timestamp.replace('-', '').replace(':', '').lower()}-{short_hash(url)}"


def make_article_id(url: str, timestamp: str) -> str:
    return f"art-{timestamp[:10].replace('-', '')}-{short_hash(url)}"


def canonicalize_article_url(url: str) -> str:
    return runtime_canonicalize_url(str(url or "").strip())


def canonical_signatures(
    url: str,
    *,
    title: str = "",
    text: str = "",
    related_urls: list[str] | tuple[str, ...] | set[str] | None = None,
) -> set[str]:
    return runtime_source_identity_signatures(
        str(url or "").strip(),
        title=title,
        text=text,
        related_urls=related_urls,
    )


def extract_linked_paper_urls(text: str) -> list[str]:
    return runtime_extract_linked_paper_urls(str(text or ""))


def article_canonical_url(meta: dict[str, Any]) -> str:
    return canonicalize_article_url(str(meta.get("canonical_url") or meta.get("source_url") or "").strip())


def article_signature_set(
    meta: dict[str, Any],
    *,
    source_meta: dict[str, Any] | None = None,
    source_body: str = "",
) -> set[str]:
    source_meta = dict(source_meta or {})
    related_urls = source_meta.get("linked_paper_urls") or source_meta.get("linkedPaperUrls") or []
    if not isinstance(related_urls, list):
        related_urls = []
    return canonical_signatures(
        str(meta.get("canonical_url") or meta.get("source_url") or "").strip(),
        title=str(source_meta.get("source_title") or meta.get("source_title") or "").strip(),
        text=str(source_body or "").strip(),
        related_urls=related_urls,
    )


def article_is_kept_or_published(meta: dict[str, Any]) -> bool:
    status = str(meta.get("publication_status") or "").strip()
    decision = str(meta.get("curator_decision") or "").strip()
    return decision == "kept" or status in KEPT_PUBLICATION_STATUSES


def publication_status(meta: dict[str, Any]) -> str:
    return str(meta.get("publication_status") or "").strip()


def article_artifact_publication_current(meta: dict[str, Any]) -> bool:
    minted_at = str(meta.get("artifact_minted_at_utc") or "").strip()
    if not minted_at:
        return False
    return (
        str(meta.get("artifact_publication_status") or "").strip() == "published"
        and str(meta.get("artifact_publication_minted_at_utc") or "").strip() == minted_at
    )


def article_is_terminal_for_selector(meta: dict[str, Any]) -> bool:
    return publication_status(meta) in TERMINAL_SELECTOR_STATUSES


def article_ready_for_daily_on_date(meta: dict[str, Any], replay_date: str, *, require_artifact_publication: bool = False) -> bool:
    if publication_status(meta) != "ready-for-daily":
        return False
    minted_at = str(meta.get("artifact_minted_at_utc") or "").strip()
    if not minted_at.startswith(replay_date):
        return False
    if require_artifact_publication and not article_artifact_publication_current(meta):
        return False
    return True


def article_published_for_daily_on_date(meta: dict[str, Any], replay_date: str) -> bool:
    return publication_status(meta) == "published" and str(meta.get("published_in_daily") or "").strip() == replay_date


def article_included_for_date_meta(meta: dict[str, Any], replay_date: str) -> bool:
    return article_ready_for_daily_on_date(meta, replay_date) or article_published_for_daily_on_date(meta, replay_date)


def article_ready_for_pm_on_date(meta: dict[str, Any], replay_date: str) -> bool:
    return article_ready_for_daily_on_date(meta, replay_date, require_artifact_publication=True)


def normalize_article_meta(meta: dict[str, Any]) -> dict[str, Any]:
    normalized = dict(meta)
    status = publication_status(normalized)

    if status != "published":
        for key in DAILY_PUBLICATION_FIELDS:
            normalized.pop(key, None)

    if status in {"discarded", "capture-blocked", DUPLICATE_REJECTED_STATUS}:
        for key in ARTIFACT_PUBLICATION_FIELDS:
            normalized.pop(key, None)

    if status != DUPLICATE_REJECTED_STATUS:
        for key in DUPLICATE_ONLY_FIELDS:
            normalized.pop(key, None)

    if status == "published" and article_artifact_publication_current(normalized):
        normalized["artifact_publication_status"] = "published"
        normalized["artifact_publication_minted_at_utc"] = str(normalized.get("artifact_minted_at_utc") or "").strip()

    return normalized


def write_article_markdown(path: Path, meta: dict[str, Any], body: str) -> None:
    write_markdown(path, normalize_article_meta(meta), body)


def choose_preferred_signature(signatures: set[str]) -> str:
    if not signatures:
        return ""
    return sorted(signatures, key=lambda value: (value.startswith("url:"), value))[0]


def signature_kind(signature: str) -> str:
    if signature.startswith("work:"):
        return "work"
    if signature.startswith("url:"):
        return "canonical_url"
    prefix, _sep, _rest = signature.partition(":")
    return prefix or "signature"


def build_article_record(
    meta: dict[str, Any],
    *,
    article_id: str | None = None,
    article_path: Path | None = None,
    source_meta: dict[str, Any] | None = None,
    source_body: str = "",
) -> dict[str, Any]:
    source_meta = dict(source_meta or {})
    resolved_article_id = str(article_id or meta.get("article_id") or (article_path.parent.name if article_path else "")).strip()
    canonical_url = article_canonical_url(meta)
    related_urls = source_meta.get("linked_paper_urls") or source_meta.get("linkedPaperUrls") or []
    if not isinstance(related_urls, list):
        related_urls = []
    return {
        "article_id": resolved_article_id,
        "article_path": str(article_path) if article_path is not None else "",
        "canonical_url": canonical_url,
        "signatures": article_signature_set(meta, source_meta=source_meta, source_body=source_body),
        "publication_status": str(meta.get("publication_status") or "").strip(),
        "curator_decision": str(meta.get("curator_decision") or "").strip(),
        "queued_at_utc": str(meta.get("queued_at_utc") or "").strip(),
        "artifact_minted_at_utc": str(meta.get("artifact_minted_at_utc") or "").strip(),
        "published_in_daily": str(meta.get("published_in_daily") or "").strip(),
        "source_url": str(meta.get("source_url") or "").strip(),
        "source_title": str(source_meta.get("source_title") or meta.get("source_title") or "").strip(),
        "related_urls": related_urls,
        "source_body": str(source_body or "").strip(),
    }


def load_article_records(article_paths: list[Path] | None = None) -> list[dict[str, Any]]:
    paths = sorted(article_paths or ARTICLES_DIR.glob("*/article.md"))
    records: list[dict[str, Any]] = []
    for article_path in paths:
        if not article_path.exists():
            continue
        meta, _body = read_markdown(article_path)
        source_path = article_path.parent / "source.md"
        source_meta, source_body = ({}, "")
        if source_path.exists():
            source_meta, source_body = read_markdown(source_path)
        records.append(build_article_record(meta, article_path=article_path, source_meta=source_meta, source_body=source_body))
    return records


def find_duplicate_canonical_pairs(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    ordered = sorted(
        records,
        key=lambda item: (
            str(item.get("artifact_minted_at_utc") or ""),
            str(item.get("queued_at_utc") or ""),
            str(item.get("article_id") or ""),
        ),
    )
    duplicates: list[dict[str, Any]] = []
    for index, left in enumerate(ordered):
        left_id = str(left.get("article_id") or "").strip()
        left_signatures = set(left.get("signatures") or set())
        if not left_id or not left_signatures:
            continue
        for right in ordered[index + 1 :]:
            right_id = str(right.get("article_id") or "").strip()
            if not right_id or left_id == right_id:
                continue
            overlap = left_signatures & set(right.get("signatures") or set())
            if not overlap:
                continue
            duplicates.append(
                {
                    "signature": choose_preferred_signature(overlap),
                    "articles": [left, right],
                }
            )
    return duplicates


def find_kept_canonical_conflict(
    canonical_url: str,
    *,
    exclude_article_id: str | None = None,
    records: list[dict[str, Any]] | None = None,
    title: str = "",
    text: str = "",
    related_urls: list[str] | tuple[str, ...] | set[str] | None = None,
) -> dict[str, Any] | None:
    candidate_canonical_url = canonicalize_article_url(canonical_url)
    candidate_signatures = canonical_signatures(
        candidate_canonical_url,
        title=title,
        text=text,
        related_urls=related_urls,
    )
    if not candidate_canonical_url or not candidate_signatures:
        return None
    for record in records or load_article_records():
        article_id = str(record.get("article_id") or "").strip()
        if exclude_article_id and article_id == exclude_article_id:
            continue
        if not article_is_kept_or_published(record):
            continue
        overlap = candidate_signatures & set(record.get("signatures") or set())
        if not overlap:
            continue
        return {
            "candidate_canonical_url": candidate_canonical_url,
            "candidate_signatures": sorted(candidate_signatures),
            "matched_signature": choose_preferred_signature(overlap),
            "existing_article": record,
        }
    return None


def assert_unique_canonical_records(records: list[dict[str, Any]], context: str) -> None:
    duplicates = find_duplicate_canonical_pairs(records)
    if not duplicates:
        return
    first = duplicates[0]
    left, right = first["articles"]
    raise ValueError(
        "duplicate_canonical_url:"
        f"{context}:"
        f"{left['article_id']}:{right['article_id']}:"
        f"{first['signature']}:"
        f"{left['canonical_url']}:{right['canonical_url']}"
    )


def require_keys(meta: dict[str, Any], keys: list[str]) -> None:
    missing = [key for key in keys if key not in meta or meta[key] in ("", None, [])]
    if missing:
        raise ValueError(f"missing_keys:{','.join(missing)}")


def strip_outer_code_fence(text: str) -> str:
    stripped = text.strip()
    fence_match = re.match(r"^```[A-Za-z0-9_-]*\n(?P<body>.*)\n```$", stripped, flags=re.DOTALL)
    if fence_match:
        return fence_match.group("body").strip()
    return stripped


def extract_named_markdown_blocks(text: str) -> list[tuple[str, str]]:
    header_pattern = re.compile(
        r"^### file:\s*(?P<name>[^\n]+)\n(?:```(?:markdown|md)\n)?",
        re.MULTILINE,
    )
    matches = list(header_pattern.finditer(text))
    blocks: list[tuple[str, str]] = []
    for idx, match in enumerate(matches):
        body_start = match.end()
        body_end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        body = text[body_start:body_end].strip()
        if body.endswith("```"):
            body = body[:-3].rstrip()
        blocks.append((match.group("name").strip(), body + "\n"))
    return blocks


CHROME_LINE_PATTERNS = [
    re.compile(pattern, re.IGNORECASE)
    for pattern in [
        r"^skip to content\b",
        r"^navigation menu\b",
        r"^toggle navigation\b",
        r"^sign in\b",
        r"^appearance settings\b",
        r"^search or jump to",
        r"^footer\b",
        r"^terms\b",
        r"^privacy\b",
        r"^security\b",
        r"^status\b",
        r"^community\b",
        r"^docs\b",
        r"^contact\b",
        r"^manage cookies\b",
        r"^do not share my personal information\b",
        r"^uh oh! there was an error while loading",
        r"^you can.?t perform that action at this time",
        r"^report repository\b",
        r"^releases\b",
        r"^packages\b",
        r"^contributors\b",
        r"^languages\b",
        r"^stars\b",
        r"^watchers\b",
        r"^forks\b",
        r"^github(?:\s|$)",
        r"^platform ai\b",
        r"^developer workflows\b",
        r"^application security\b",
        r"^explore\b",
        r"^resources\b",
        r"^open source\b",
        r"^enterprise solutions\b",
        r"^pricing\b",
        r"^© \d{4}\b",
    ]
]

CHROME_SEGMENT_PATTERNS = [
    re.compile(pattern, re.IGNORECASE | re.DOTALL)
    for pattern in [
        r"Skip to content.*?Search or jump to\.\.\.",
        r"Footer © \d{4}.*$",
        r"Uh oh! There was an error while loading\. Please reload this page \.\s*",
        r"You can.?t perform that action at this time\.\s*",
    ]
]

CONTENT_STOP_PATTERNS = [
    re.compile(pattern, re.IGNORECASE)
    for pattern in [
        r"^Example:?$",
        r"^Creating actions and running$",
        r"^Thoughts while building$",
        r"^TODO$",
        r"^Contributing$",
        r"^License$",
        r"^Try Render Free$",
        r"^Explore Docs$",
        r"^Resources$",
        r"^Company$",
        r"^Articles$",
    ]
]


def source_body_text(source_body: str) -> str:
    marker = "\n## Body\n"
    if marker in source_body:
        return source_body.split(marker, 1)[1].strip()
    if source_body.startswith("## Body\n"):
        return source_body.split("## Body\n", 1)[1].strip()
    return markdown_section(source_body, "## Body") or source_body.strip()


def compact_source_markdown(source_body: str, max_chars: int = 4500) -> str:
    body_section = source_body_text(source_body)
    compact = body_section
    for pattern in CHROME_SEGMENT_PATTERNS:
        compact = pattern.sub("", compact)
    compact = re.sub(r"\n{3,}", "\n\n", compact)
    compact = re.sub(r"[ \t]{2,}", " ", compact)

    filtered_lines: list[str] = []
    seen: set[str] = set()
    for raw_line in compact.splitlines():
        line = re.sub(r"\s+", " ", raw_line).strip()
        if not line:
            continue
        if any(pattern.search(line) for pattern in CHROME_LINE_PATTERNS):
            continue
        if line in seen:
            continue
        seen.add(line)
        filtered_lines.append(line)

    anchor_patterns = [
        re.compile(r"^(?:#+\s*)?README$", re.IGNORECASE),
        re.compile(r"^(?:#+\s*)?Abstract$", re.IGNORECASE),
        re.compile(r"^(?:#+\s*)?Summary$", re.IGNORECASE),
        re.compile(r"^(?:#+\s*)?Overview$", re.IGNORECASE),
        re.compile(r"^(?:#+\s*)?Introduction$", re.IGNORECASE),
        re.compile(r"^(?:#+\s*)?TL;DR[:\s]", re.IGNORECASE),
    ]
    start_index = 0
    for idx, line in enumerate(filtered_lines):
        if any(pattern.match(line) for pattern in anchor_patterns):
            start_index = idx
            break
        if "repository files navigation" in line.lower():
            for jdx in range(idx + 1, len(filtered_lines)):
                if any(pattern.match(filtered_lines[jdx]) for pattern in anchor_patterns):
                    start_index = jdx
                    break
            if start_index:
                break

    if start_index == 0:
        for idx, line in enumerate(filtered_lines):
            word_count = len(line.split())
            has_sentence_punctuation = any(mark in line for mark in [".", ":", ";", "!", "?"])
            if word_count >= 12 and (len(line) >= 80 or has_sentence_punctuation):
                start_index = idx
                break

    trimmed_lines: list[str] = []
    for line in filtered_lines[start_index:]:
        if trimmed_lines and any(pattern.match(line) for pattern in CONTENT_STOP_PATTERNS):
            break
        trimmed_lines.append(line)
        if len(trimmed_lines) >= 24:
            break

    normalized = "\n".join(trimmed_lines).strip()
    if not normalized:
        normalized = body_section.strip()
    if len(normalized) > max_chars:
        normalized = normalized[:max_chars].rstrip() + "\n\n[truncated]"
    return normalized


class TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self._chunks: list[str] = []
        self._skip_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"script", "style", "noscript"}:
            self._skip_depth += 1
            return
        if self._skip_depth:
            return
        if tag in {"p", "div", "section", "article", "header", "footer", "li", "br"}:
            self._chunks.append("\n")
        if tag in {"h1", "h2", "h3"}:
            self._chunks.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "noscript"} and self._skip_depth:
            self._skip_depth -= 1
            return
        if self._skip_depth:
            return
        if tag in {"p", "div", "section", "article", "header", "footer", "li", "h1", "h2", "h3"}:
            self._chunks.append("\n")

    def handle_data(self, data: str) -> None:
        if self._skip_depth:
            return
        text = re.sub(r"\s+", " ", data)
        if text.strip():
            self._chunks.append(text.strip() + " ")

    def as_text(self) -> str:
        text = html.unescape("".join(self._chunks))
        text = re.sub(r"[ \t]+\n", "\n", text)
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text.strip()


def html_to_text(source: str) -> str:
    parser = TextExtractor()
    parser.feed(source)
    return parser.as_text()


def extract_github_blog_main_html(source: str) -> str | None:
    match = re.search(r"<main id=\"start-of-content\".*?</main>", source, flags=re.IGNORECASE | re.DOTALL)
    if not match:
        return None
    main_html = match.group(0)
    if "<aside id=\"sidebar\"" in main_html:
        main_html = main_html.split("<aside id=\"sidebar\"", 1)[0]
    return main_html


def extract_github_repo_richtext_html(source: str) -> str | None:
    scripts = re.findall(
        r"<script type=\"application/json\" data-target=\"react-app\.embeddedData\">(.*?)</script>",
        source,
        flags=re.IGNORECASE | re.DOTALL,
    )
    for script_body in scripts:
        try:
            payload = json.loads(html.unescape(script_body))
        except Exception:
            continue
        route = (((payload or {}).get("payload") or {}).get("codeViewRepoRoute") or {})
        overview = route.get("overview") or {}
        overview_files = overview.get("overviewFiles") or []
        for item in overview_files:
            rich_text = str((item or {}).get("richText") or "").strip()
            if rich_text:
                return rich_text
    return None


def extract_jetbrains_blog_article_html(source: str) -> str | None:
    match = re.search(
        r"<section[^>]+class=\"[^\"]*article-section[^\"]*\"[^>]*>.*?</section>",
        source,
        flags=re.IGNORECASE | re.DOTALL,
    )
    if not match:
        return None
    return match.group(0)


def best_effort_html_to_text(source_url: str, source: str) -> str:
    lowered_url = (source_url or "").lower()
    preferred_html: str | None = None
    if "github.blog/" in lowered_url:
        preferred_html = extract_github_blog_main_html(source)
    elif "blog.jetbrains.com/" in lowered_url:
        preferred_html = extract_jetbrains_blog_article_html(source)
    elif "github.com/" in lowered_url and "/discussions/" not in lowered_url:
        preferred_html = extract_github_repo_richtext_html(source)
    if preferred_html:
        text = html_to_text(preferred_html)
        if text.strip():
            return text
    return html_to_text(source)


def render_markdown(text: str) -> str:
    lines = text.splitlines()
    html_lines: list[str] = []
    in_list = False
    in_code = False
    code_lines: list[str] = []

    def close_list() -> None:
        nonlocal in_list
        if in_list:
            html_lines.append("</ul>")
            in_list = False

    def close_code() -> None:
        nonlocal in_code, code_lines
        if in_code:
            html_lines.append("<pre><code>")
            html_lines.append(html.escape("\n".join(code_lines)))
            html_lines.append("</code></pre>")
            in_code = False
            code_lines = []

    for raw_line in lines:
        line = raw_line.rstrip()
        if line.startswith("```"):
            close_list()
            if in_code:
                close_code()
            else:
                in_code = True
            continue
        if in_code:
            code_lines.append(line)
            continue
        if not line.strip():
            close_list()
            continue
        if line.startswith("### "):
            close_list()
            html_lines.append(f"<h3>{html.escape(line[4:])}</h3>")
            continue
        if line.startswith("## "):
            close_list()
            html_lines.append(f"<h2>{html.escape(line[3:])}</h2>")
            continue
        if line.startswith("# "):
            close_list()
            html_lines.append(f"<h1>{html.escape(line[2:])}</h1>")
            continue
        if line.startswith("- "):
            if not in_list:
                html_lines.append("<ul>")
                in_list = True
            html_lines.append(f"<li>{html.escape(line[2:])}</li>")
            continue
        close_list()
        html_lines.append(f"<p>{html.escape(line)}</p>")

    close_code()
    close_list()
    return "\n".join(html_lines)


def article_sort_key(path: Path) -> tuple[str, str]:
    meta, _ = read_markdown(path)
    return str(meta.get("artifact_minted_at_utc") or ""), str(meta.get("article_id") or path.parent.name)
