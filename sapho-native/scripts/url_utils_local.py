#!/usr/bin/env python3
"""URL utilities for firehose feeder."""

from __future__ import annotations
import hashlib
import re
from urllib.parse import urlsplit, urlunsplit, parse_qsl, urlencode

TRACKING_KEYS = {
    "ref",
    "source",
    "s",
    "fbclid",
    "gclid",
    "mc_cid",
    "mc_eid",
}
TRACKING_PREFIXES = ("utm_",)
ARXIV_ID_RE = re.compile(r'(?<!\d)(\d{4}\.\d{4,5})(?:v\d+)?')
OPENREVIEW_ID_RE = re.compile(r'^[A-Za-z0-9_-]{6,}$')
ARXIV_URL_RE = re.compile(r'https?://(?:www\.)?arxiv\.org/(?:abs|pdf|html)/(?P<id>\d{4}\.\d{4,5})(?:v\d+)?', re.IGNORECASE)
ARXIV_TEXT_RE = re.compile(r'\barxiv\s*:?\s*(?P<id>\d{4}\.\d{4,5})(?:v\d+)?', re.IGNORECASE)
OPENREVIEW_URL_RE = re.compile(r'https?://(?:www\.)?openreview\.net/(?:forum|pdf)\?id=(?P<id>[A-Za-z0-9_-]{6,})', re.IGNORECASE)
DOI_URL_RE = re.compile(r'https?://(?:(?:dx|www)\.)?doi\.org/(?P<doi>10\.\d{4,9}/[-._;()/:A-Za-z0-9]+)', re.IGNORECASE)
DOI_TEXT_RE = re.compile(r'\b(?:doi\s*:?\s*)(?P<doi>10\.\d{4,9}/[-._;()/:A-Za-z0-9]+)', re.IGNORECASE)
TITLE_ARXIV_PREFIX_RE = re.compile(r'^\[\d{4}\.\d{4,5}(?:v\d+)?\]\s*')
CURATED_WORK_IDENTITY_OVERRIDES = {
    'scaling-agent-systems-2512.08296': {
        'canonical_urls': {
            'https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work',
        },
        'source_signatures': {
            'arxiv:2512.08296',
        },
    },
}
BLOG_PATH_MARKERS = {
    'blog',
    'blogs',
    'news',
    'updates',
    'post',
    'posts',
    'article',
    'articles',
}
GITHUB_RESERVED_TOP_LEVEL = {
    'about',
    'account',
    'apps',
    'collections',
    'contact',
    'customer-stories',
    'enterprise',
    'explore',
    'features',
    'github',
    'issues',
    'login',
    'marketplace',
    'models',
    'notifications',
    'orgs',
    'pricing',
    'pulls',
    'search',
    'security',
    'settings',
    'site',
    'sponsors',
    'team',
    'teams',
    'topics',
}


def sha256_text(value: str) -> str:
    return hashlib.sha256((value or "").encode("utf-8")).hexdigest()


def domain_from_url(url: str) -> str:
    try:
        return (urlsplit(url).hostname or "").lower()
    except Exception:
        return ""


def is_blocked_domain(url: str, blocklist: list[str]) -> bool:
    host = domain_from_url(url)
    if not host:
        return False
    for blocked in blocklist:
        b = (blocked or "").lower().strip()
        if not b:
            continue
        if host == b or host.endswith('.' + b):
            return True
    return False


def canonicalize_url(url: str) -> str:
    """Canonicalize URL by stripping common tracking params and normalizing host/scheme/path."""
    if not url:
        return ""

    parts = urlsplit(url)
    scheme = (parts.scheme or 'https').lower()
    netloc = (parts.netloc or '').lower()

    path = parts.path or '/'
    if path != '/':
        path = path.rstrip('/') or '/'

    kept = []
    for k, v in parse_qsl(parts.query, keep_blank_values=True):
        key = (k or '').lower()
        if key in TRACKING_KEYS:
            continue
        if any(key.startswith(prefix) for prefix in TRACKING_PREFIXES):
            continue
        kept.append((k, v))

    kept.sort(key=lambda t: (t[0], t[1]))
    query = urlencode(kept, doseq=True)

    return urlunsplit((scheme, netloc, path, query, ''))


def _path_segments(url: str) -> list[str]:
    try:
        return [segment for segment in urlsplit(url).path.split('/') if segment]
    except Exception:
        return []


def _parse_arxiv_id(url: str) -> str:
    match = ARXIV_ID_RE.search(str(url or '').strip())
    return match.group(1) if match else ''


def _normalize_doi(value: str) -> str:
    cleaned = str(value or '').strip().rstrip(').,;')
    return cleaned.lower()


def _normalize_title_for_work_identity(title: str) -> str:
    text = str(title or '').strip()
    text = TITLE_ARXIV_PREFIX_RE.sub('', text)
    text = re.sub(r'^\s*title:\s*', '', text, flags=re.IGNORECASE)
    text = re.sub(r'[\u2018\u2019\u201c\u201d]', "'", text)
    text = re.sub(r'[^A-Za-z0-9]+', ' ', text).strip().lower()
    text = re.sub(r'\s+', ' ', text)
    if len(text) < 24:
        return ''
    if len(text.split()) < 4:
        return ''
    return text


def _title_work_signature(title: str) -> str:
    normalized = _normalize_title_for_work_identity(title)
    if not normalized:
        return ''
    return 'work:title:' + re.sub(r'[^a-z0-9]+', '-', normalized).strip('-')[:120]


def _looks_like_blog_surface(url: str) -> bool:
    canonical = canonicalize_url(url)
    if not canonical:
        return False
    segments = {segment.lower() for segment in _path_segments(canonical)}
    return bool(segments & BLOG_PATH_MARKERS)


def _paper_work_signatures_from_signature_set(signatures: set[str]) -> set[str]:
    work_ids: set[str] = set()
    for signature in set(signatures or set()):
        if signature.startswith(('arxiv:', 'openreview:', 'doi:')):
            work_ids.add(f'work:paper:{signature}')
    return work_ids


def _extract_related_url_signatures(*texts: str, related_urls: list[str] | tuple[str, ...] | set[str] | None = None) -> set[str]:
    related_signatures: set[str] = set()
    for raw in related_urls or ():
        related_signatures.update(_source_signatures_without_work_identity(str(raw or '').strip()))

    haystack = "\n".join(str(text or '') for text in texts if str(text or '').strip())
    if haystack:
        for match in ARXIV_URL_RE.finditer(haystack):
            related_signatures.add(f'arxiv:{match.group("id")}')
        for match in ARXIV_TEXT_RE.finditer(haystack):
            related_signatures.add(f'arxiv:{match.group("id")}')
        for match in OPENREVIEW_URL_RE.finditer(haystack):
            related_signatures.add(f'openreview:{match.group("id")}')
        for match in DOI_URL_RE.finditer(haystack):
            related_signatures.add(f'doi:{_normalize_doi(match.group("doi"))}')
        for match in DOI_TEXT_RE.finditer(haystack):
            related_signatures.add(f'doi:{_normalize_doi(match.group("doi"))}')
    return related_signatures

def _source_signatures_without_work_identity(url: str) -> set[str]:
    canonical = canonicalize_url(url)
    if not canonical:
        return set()

    signatures = {f'url:{canonical}'}
    host = domain_from_url(canonical)
    segments = _path_segments(canonical)

    arxiv_id = _parse_arxiv_id(canonical)
    if host.endswith('arxiv.org') and arxiv_id:
        signatures.add(f'arxiv:{arxiv_id}')

    if host == 'openreview.net':
        try:
            query_params = dict(parse_qsl(urlsplit(canonical).query, keep_blank_values=True))
        except Exception:
            query_params = {}
        openreview_id = str(query_params.get('id') or '').strip()
        if OPENREVIEW_ID_RE.fullmatch(openreview_id):
            signatures.add(f'openreview:{openreview_id}')

    if host in {'doi.org', 'dx.doi.org', 'www.doi.org'}:
        doi = _normalize_doi('/'.join(segments)) if segments else ''
        if doi.startswith('10.'):
            signatures.add(f'doi:{doi}')

    if host == 'github.com' and len(segments) >= 2:
        owner = segments[0].lower()
        repo = segments[1].lower()
        repo_mode = len(segments) == 2 or segments[2].lower() in {'blob', 'tree', 'raw', 'releases', 'wiki', 'commits', 'commit'}
        if owner not in GITHUB_RESERVED_TOP_LEVEL and repo_mode:
            signatures.add(f'github:{owner}/{repo}')

    if host.endswith('researchgate.net'):
        if len(segments) >= 2 and segments[0].lower() == 'publication':
            publication_id = re.match(r'^(\d+)', segments[1])
            if publication_id:
                signatures.add(f'researchgate-publication:{publication_id.group(1)}')

    if host.endswith('alphaxiv.org'):
        if len(segments) >= 2 and segments[0].lower() == 'resources' and ARXIV_ID_RE.search(segments[1]):
            signatures.add(f'alphaxiv:{_parse_arxiv_id(segments[1])}')

    return signatures


def work_signatures(
    url: str,
    *,
    title: str = '',
    text: str = '',
    related_urls: list[str] | tuple[str, ...] | set[str] | None = None,
) -> set[str]:
    canonical = canonicalize_url(url)
    if not canonical:
        return set()

    base_signatures = _source_signatures_without_work_identity(canonical)
    work_ids: set[str] = set()
    work_ids.update(_paper_work_signatures_from_signature_set(base_signatures))

    related_signatures = _extract_related_url_signatures(title, text, related_urls=related_urls)
    if _looks_like_blog_surface(canonical):
        work_ids.update(_paper_work_signatures_from_signature_set(related_signatures))

    title_signature = _title_work_signature(title)
    if title_signature:
        has_paper_surface = any(signature.startswith(('arxiv:', 'openreview:', 'doi:')) for signature in base_signatures)
        if has_paper_surface or _looks_like_blog_surface(canonical):
            work_ids.add(title_signature)

    for work_id, override in CURATED_WORK_IDENTITY_OVERRIDES.items():
        override_urls = {
            canonicalize_url(value)
            for value in set(override.get('canonical_urls') or set())
            if canonicalize_url(value)
        }
        override_signatures = {
            str(value or '').strip()
            for value in set(override.get('source_signatures') or set())
            if str(value or '').strip()
        }
        if canonical in override_urls or base_signatures & override_signatures or related_signatures & override_signatures:
            work_ids.add(f'work:{work_id}')
    return work_ids


def source_identity_signatures(
    url: str,
    *,
    title: str = '',
    text: str = '',
    related_urls: list[str] | tuple[str, ...] | set[str] | None = None,
) -> set[str]:
    signatures = _source_signatures_without_work_identity(url)
    signatures.update(work_signatures(url, title=title, text=text, related_urls=related_urls))
    return signatures


def extract_linked_paper_urls(text: str) -> list[str]:
    linked: set[str] = set()
    haystack = str(text or '')
    for match in ARXIV_URL_RE.finditer(haystack):
        linked.add(canonicalize_url(f"https://arxiv.org/abs/{match.group('id')}"))
    for match in ARXIV_TEXT_RE.finditer(haystack):
        linked.add(canonicalize_url(f"https://arxiv.org/abs/{match.group('id')}"))
    for match in OPENREVIEW_URL_RE.finditer(haystack):
        linked.add(canonicalize_url(f"https://openreview.net/forum?id={match.group('id')}"))
    for match in DOI_URL_RE.finditer(haystack):
        linked.add(canonicalize_url(f"https://doi.org/{_normalize_doi(match.group('doi'))}"))
    for match in DOI_TEXT_RE.finditer(haystack):
        linked.add(canonicalize_url(f"https://doi.org/{_normalize_doi(match.group('doi'))}"))
    return sorted(value for value in linked if value)


def source_signatures(url: str) -> set[str]:
    return _source_signatures_without_work_identity(url)
