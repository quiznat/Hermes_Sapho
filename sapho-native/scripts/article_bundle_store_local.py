#!/usr/bin/env python3
"""Canonical article, fact, source, and Daily publication storage."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

import yaml

from url_utils_local import canonicalize_url

ROOT = Path('/home/openclaw/.openclaw/workspace')
ARTICLES_ROOT = ROOT / 'research/articles'
FACTS_ROOT = ROOT / 'research/facts'
SOURCE_ROOT = ROOT / 'research/source-material'
OLD_SOURCE_ROOT = ROOT / 'research/evidence/source-material'
DAILY_ROOT = ROOT / 'research/publication/daily'

ARTICLE_VERSION = 'article-bundle.v1'
FACT_VERSION = 'research-fact.v1'
DAILY_VERSION = 'daily-publication.v1'


def now_utc() -> str:
    from datetime import datetime, timezone

    return datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def _article_date(article_id: str) -> str:
    match = re.match(r'^art-(\d{4}-\d{2}-\d{2})-', str(article_id or '').strip())
    return match.group(1) if match else now_utc()[:10]


def article_path(article_id: str) -> Path:
    return ARTICLES_ROOT / f'{article_id}.md'


def fact_dir(article_id: str) -> Path:
    return FACTS_ROOT / article_id


def fact_path(article_id: str, fact_id: str) -> Path:
    return fact_dir(article_id) / f'{fact_id}.md'


def source_json_path(article_id: str) -> Path:
    return SOURCE_ROOT / f'{article_id}.json'


def source_text_path(article_id: str) -> Path:
    return SOURCE_ROOT / f'{article_id}.txt'


def daily_bundle_dir(date_value: str) -> Path:
    return DAILY_ROOT / date_value


def _relative_runtime_path(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except Exception:
        return str(path)


def _split_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith('---\n'):
        return {}, text
    marker = '\n---\n'
    end = text.find(marker, 4)
    if end == -1:
        return {}, text
    raw = text[4:end]
    body = text[end + len(marker):]
    payload = yaml.safe_load(raw) or {}
    if not isinstance(payload, dict):
        payload = {}
    return payload, body


def _render_frontmatter(payload: dict[str, Any], body: str) -> str:
    rendered = yaml.safe_dump(payload, sort_keys=False, allow_unicode=True).strip()
    cleaned_body = str(body or '').lstrip('\n')
    return f'---\n{rendered}\n---\n\n{cleaned_body}' if cleaned_body else f'---\n{rendered}\n---\n'


def _clean(text: Any) -> str:
    return re.sub(r'\s+', ' ', str(text or '')).strip()


def _normalize_confidence(value: Any) -> str:
    cleaned = _clean(value).lower()
    return cleaned if cleaned in {'low', 'medium', 'high'} else ''


def _normalize_canonical_url(url: Any) -> str:
    return canonicalize_url(_clean(url))


def _empty_article_frontmatter(article_id: str, *, source_url: str = '', canonical_url: str = '', discovered_at_utc: str = '') -> dict[str, Any]:
    cleaned_source_url = _clean(source_url)
    normalized_canonical_url = _normalize_canonical_url(canonical_url) or _normalize_canonical_url(cleaned_source_url)
    return {
        'version': ARTICLE_VERSION,
        'article_id': article_id,
        'source_url': cleaned_source_url,
        'canonical_url': normalized_canonical_url,
        'discovered_at_utc': _clean(discovered_at_utc) or now_utc(),
        'source_snapshot_json_path': _relative_runtime_path(source_json_path(article_id)),
        'source_snapshot_text_path': _relative_runtime_path(source_text_path(article_id)),
        'source_custody_status': 'missing',
        'filter_state': 'pending',
        'filter_decided_at_utc': '',
        'filter_rationale': '',
        'artifact_minted_at_utc': '',
        'artifact_title': '',
        'artifact_core_thesis': '',
        'artifact_mechanism_summary': '',
        'artifact_why_it_matters': '',
        'artifact_confidence': '',
        'artifact_confidence_justification': '',
        'fact_count': 0,
        'last_stage': 'intake',
        'last_stage_run_id': '',
        'updated_at_utc': now_utc(),
    }


def normalize_article_frontmatter(payload: dict[str, Any], *, article_id: str | None = None) -> dict[str, Any]:
    article_id = _clean(article_id or payload.get('article_id') or payload.get('id'))
    source_url = _clean(payload.get('source_url') or payload.get('url'))
    canonical_url = _normalize_canonical_url(payload.get('canonical_url') or payload.get('canonicalUrl') or source_url)
    discovered_at = _clean(payload.get('discovered_at_utc') or payload.get('addedAtUtc'))

    normalized = _empty_article_frontmatter(
        article_id,
        source_url=source_url,
        canonical_url=canonical_url,
        discovered_at_utc=discovered_at,
    )
    normalized['source_snapshot_json_path'] = _relative_runtime_path(source_json_path(article_id))
    normalized['source_snapshot_text_path'] = _relative_runtime_path(source_text_path(article_id))
    normalized['source_custody_status'] = _clean(payload.get('source_custody_status') or payload.get('custody_status') or payload.get('evidence_harvest_status')) or normalized['source_custody_status']
    normalized['filter_state'] = _clean(payload.get('filter_state') or payload.get('decision') or payload.get('status')).lower() or normalized['filter_state']
    if normalized['filter_state'] not in {'pending', 'kept', 'discarded'}:
        normalized['filter_state'] = 'pending'
    normalized['filter_decided_at_utc'] = _clean(payload.get('filter_decided_at_utc') or payload.get('curatedAtUtc') or payload.get('processedAtUtc'))
    normalized['filter_rationale'] = _clean(payload.get('filter_rationale') or payload.get('notes') or payload.get('rationale'))
    normalized['artifact_minted_at_utc'] = _clean(payload.get('artifact_minted_at_utc') or payload.get('synthesistFinalizedAtUtc'))
    normalized['artifact_title'] = _clean(payload.get('artifact_title') or payload.get('title') or ((payload.get('synthesistFinalFields') or {}).get('title')))
    normalized['artifact_core_thesis'] = _clean(payload.get('artifact_core_thesis') or ((payload.get('synthesistFinalFields') or {}).get('coreThesis')))
    normalized['artifact_mechanism_summary'] = _clean(payload.get('artifact_mechanism_summary') or ((payload.get('synthesistFinalFields') or {}).get('mechanismSummary')))
    normalized['artifact_why_it_matters'] = _clean(payload.get('artifact_why_it_matters') or ((payload.get('synthesistFinalFields') or {}).get('whyItMatters')))
    normalized['artifact_confidence'] = _normalize_confidence(payload.get('artifact_confidence') or ((payload.get('synthesistFinalFields') or {}).get('confidence')) or payload.get('confidence'))
    normalized['artifact_confidence_justification'] = _clean(payload.get('artifact_confidence_justification') or ((payload.get('synthesistFinalFields') or {}).get('confidenceJustification')))
    normalized['last_stage'] = _clean(payload.get('last_stage') or payload.get('lastStage')).lower() or normalized['last_stage']
    if normalized['last_stage'] not in {'intake', 'filter', 'artifact', 'facts', 'published'}:
        normalized['last_stage'] = 'facts' if normalized['fact_count'] else 'artifact' if normalized['artifact_minted_at_utc'] else 'filter' if normalized['filter_state'] != 'pending' else 'intake'
    normalized['last_stage_run_id'] = _clean(payload.get('last_stage_run_id') or payload.get('last_pipeline_run_id') or payload.get('synthesistRunId') or payload.get('extractorRunId') or payload.get('curatorRunId'))
    normalized['updated_at_utc'] = _clean(payload.get('updated_at_utc')) or now_utc()
    normalized['fact_count'] = int(payload.get('fact_count') or 0)
    return normalized


def load_article_bundle(path: Path) -> dict[str, Any]:
    frontmatter, body = _split_frontmatter(path.read_text(encoding='utf-8', errors='replace'))
    normalized = normalize_article_frontmatter(frontmatter, article_id=path.stem)
    normalized['fact_count'] = len(load_fact_payloads(path.stem))
    return {
        'path': _relative_runtime_path(path),
        'frontmatter': normalized,
        'body': body,
    }


def load_article_bundle_by_id(article_id: str) -> dict[str, Any]:
    path = article_path(article_id)
    if path.exists():
        return load_article_bundle(path)
    payload = _empty_article_frontmatter(article_id)
    return {'path': _relative_runtime_path(path), 'frontmatter': payload, 'body': ''}


def save_article_bundle(frontmatter: dict[str, Any], body: str) -> str:
    article_id = _clean(frontmatter.get('article_id'))
    if not article_id:
        raise ValueError('article_id required')
    normalized = normalize_article_frontmatter(frontmatter, article_id=article_id)
    normalized['fact_count'] = len(load_fact_payloads(article_id))
    normalized['updated_at_utc'] = now_utc()
    path = article_path(article_id)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(_render_frontmatter(normalized, body), encoding='utf-8')
    return _relative_runtime_path(path)


def next_article_id(date_value: str) -> str:
    existing = []
    prefix = f'art-{date_value}-'
    for path in ARTICLES_ROOT.glob(f'{prefix}*.md'):
        match = re.match(rf'^{re.escape(prefix)}(\d+)$', path.stem)
        if match:
            existing.append(int(match.group(1)))
    return f'{prefix}{max(existing, default=0) + 1:03d}'


def ensure_article_bundle_for_discovery(*, source_url: str, canonical_url: str, discovered_at_utc: str, article_id: str | None = None, title_hint: str = '') -> dict[str, Any]:
    article_id = _clean(article_id) or next_article_id((discovered_at_utc or now_utc())[:10])
    existing = load_article_bundle_by_id(article_id)
    fm = dict(existing['frontmatter'])
    if not _clean(fm.get('source_url')):
        fm['source_url'] = _clean(source_url)
    if not _clean(fm.get('canonical_url')):
        fm['canonical_url'] = _normalize_canonical_url(canonical_url) or _normalize_canonical_url(source_url)
    if not _clean(fm.get('discovered_at_utc')):
        fm['discovered_at_utc'] = _clean(discovered_at_utc) or now_utc()
    if title_hint and not _clean(fm.get('artifact_title')):
        fm['artifact_title'] = _clean(title_hint)
    save_article_bundle(fm, existing['body'])
    return load_article_bundle_by_id(article_id)


def write_source_material(article_id: str, source_payload: dict[str, Any]) -> dict[str, str]:
    SOURCE_ROOT.mkdir(parents=True, exist_ok=True)
    json_path = source_json_path(article_id)
    text_path = source_text_path(article_id)
    clean_text = str(source_payload.get('cleanText') or '').strip()
    stored = dict(source_payload)
    stored['articleId'] = article_id
    stored['capturedAtUtc'] = stored.get('capturedAtUtc') or now_utc()
    json_path.write_text(json.dumps(stored, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    text_path.write_text((clean_text + '\n') if clean_text else '', encoding='utf-8')
    return {
        'json_path': _relative_runtime_path(json_path),
        'text_path': _relative_runtime_path(text_path),
    }


def load_source_material(article_id: str) -> dict[str, Any]:
    path = source_json_path(article_id)
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding='utf-8'))
    except Exception:
        return {}


def write_fact_files(article_id: str, facts: list[dict[str, Any]]) -> list[str]:
    directory = fact_dir(article_id)
    directory.mkdir(parents=True, exist_ok=True)
    for existing in directory.glob('*.md'):
        existing.unlink()
    written: list[str] = []
    for index, fact in enumerate(facts, start=1):
        fact_id = _clean(fact.get('fact_id') or fact.get('factId')) or f'{article_id}-fact-{index:02d}'
        payload = {
            'version': FACT_VERSION,
            'fact_id': fact_id,
            'article_id': article_id,
            'canonical_url': _clean(fact.get('canonical_url') or fact.get('canonicalUrl')),
            'source_material_ref': _clean(fact.get('source_material_ref') or fact.get('sourceMaterialRef')) or _relative_runtime_path(source_json_path(article_id)),
            'harvested_at_utc': _clean(fact.get('harvested_at_utc') or fact.get('harvestedAtUtc')) or now_utc(),
            'extraction_method': _clean(fact.get('extraction_method') or fact.get('extractionMethod')) or 'llm_extractor',
            'extraction_confidence': _normalize_confidence(fact.get('extraction_confidence') or fact.get('extractionConfidence')) or 'medium',
            'custody_status': _clean(fact.get('custody_status') or fact.get('custodyStatus')) or 'verified_from_source_material',
            'novel_finding': _clean(fact.get('novel_finding') or fact.get('novelFinding')),
            'quantitative_result': _clean(fact.get('quantitative_result') or fact.get('quantitativeResult')),
            'experimental_setup_sample': _clean(fact.get('experimental_setup_sample') or fact.get('experimentalSetupSample')),
            'metric_outcome': _clean(fact.get('metric_outcome') or fact.get('metricOutcome')),
            'caveat_limit': _clean(fact.get('caveat_limit') or fact.get('caveatLimit')),
        }
        body = _clean(fact.get('source_excerpt') or fact.get('sourceExcerpt'))
        path = fact_path(article_id, fact_id)
        path.write_text(_render_frontmatter(payload, body + '\n' if body else ''), encoding='utf-8')
        written.append(_relative_runtime_path(path))
    return written


def load_fact_payloads(article_id: str) -> list[dict[str, Any]]:
    directory = fact_dir(article_id)
    if not directory.exists():
        return []
    rows: list[dict[str, Any]] = []
    for path in sorted(directory.glob('*.md')):
        frontmatter, body = _split_frontmatter(path.read_text(encoding='utf-8', errors='replace'))
        if not isinstance(frontmatter, dict):
            continue
        row = dict(frontmatter)
        row['source_excerpt'] = body.strip()
        rows.append(row)
    return rows


def render_article_body(frontmatter: dict[str, Any], facts: list[dict[str, Any]]) -> str:
    title = _clean(frontmatter.get('artifact_title')) or _clean(frontmatter.get('canonical_url')) or frontmatter['article_id']
    lines = [f'# {title}', '']
    if _clean(frontmatter.get('canonical_url')):
        lines.extend(['## Source', _clean(frontmatter.get('canonical_url')), ''])
    if _clean(frontmatter.get('artifact_core_thesis')):
        lines.extend(['## Core Thesis', _clean(frontmatter.get('artifact_core_thesis')), ''])
    if _clean(frontmatter.get('artifact_mechanism_summary')):
        lines.extend(['## Mechanism', _clean(frontmatter.get('artifact_mechanism_summary')), ''])
    if _clean(frontmatter.get('artifact_why_it_matters')):
        lines.extend(['## Why It Matters', _clean(frontmatter.get('artifact_why_it_matters')), ''])
    if facts:
        lines.extend(['## Atomic Facts', ''])
        for fact in facts:
            lines.append(f"### { _clean(fact.get('fact_id')) or 'fact' }")
            lines.append(f"- Novel finding: {_clean(fact.get('novel_finding') or fact.get('novelFinding'))}")
            lines.append(f"- Quantitative result: {_clean(fact.get('quantitative_result') or fact.get('quantitativeResult'))}")
            lines.append(f"- Experimental setup/sample: {_clean(fact.get('experimental_setup_sample') or fact.get('experimentalSetupSample'))}")
            lines.append(f"- Metric/outcome: {_clean(fact.get('metric_outcome') or fact.get('metricOutcome'))}")
            lines.append(f"- Caveat/limit: {_clean(fact.get('caveat_limit') or fact.get('caveatLimit'))}")
            excerpt = _clean(fact.get('source_excerpt') or fact.get('sourceExcerpt'))
            if excerpt:
                lines.append(f"> {excerpt}")
            lines.append('')
    if _clean(frontmatter.get('artifact_confidence')):
        lines.extend(['## Confidence', _clean(frontmatter.get('artifact_confidence')), ''])
    if _clean(frontmatter.get('artifact_confidence_justification')):
        lines.extend(['## Confidence Justification', _clean(frontmatter.get('artifact_confidence_justification')), ''])
    return '\n'.join(lines).strip() + '\n'


def list_article_bundle_paths() -> list[Path]:
    if not ARTICLES_ROOT.exists():
        return []
    return sorted(ARTICLES_ROOT.glob('*.md'))


def load_pending_article_bundles(limit: int | None = None) -> list[dict[str, Any]]:
    rows = []
    for path in list_article_bundle_paths():
        bundle = load_article_bundle(path)
        if bundle['frontmatter']['filter_state'] == 'pending':
            rows.append(bundle)
    rows.sort(key=lambda item: (item['frontmatter']['discovered_at_utc'], item['frontmatter']['article_id']))
    return rows[:limit] if limit else rows


def load_kept_article_bundle_records_for_date(date_value: str) -> list[dict[str, Any]]:
    rows = []
    for path in list_article_bundle_paths():
        bundle = load_article_bundle(path)
        fm = bundle['frontmatter']
        if fm['filter_state'] != 'kept':
            continue
        if _clean(fm.get('artifact_minted_at_utc'))[:10] != date_value:
            continue
        facts = load_fact_payloads(fm['article_id'])
        rows.append({
            'articleId': fm['article_id'],
            'title': fm['artifact_title'],
            'sourceUrl': fm['canonical_url'],
            'artifactPath': bundle['path'],
            'thesis': fm['artifact_core_thesis'],
            'mechanism': fm['artifact_mechanism_summary'],
            'whyItMatters': fm['artifact_why_it_matters'],
            'confidence': fm['artifact_confidence'],
            'facts': facts,
        })
    rows.sort(key=lambda item: (item['articleId'], item['title']))
    return rows


def render_daily_markdown(date_value: str, bundles: list[dict[str, Any]]) -> str:
    lines = [f'# Sapho Collegium Daily - {date_value}', '']
    lines.append(f'Sapho minted {len(bundles)} kept artifact(s) on {date_value}.')
    lines.append('')
    for bundle in bundles:
        fm = bundle['frontmatter']
        lines.append(f"## { _clean(fm.get('artifact_title')) or fm['article_id'] }")
        lines.append(f"- Article ID: `{fm['article_id']}`")
        lines.append(f"- Source: {_clean(fm.get('canonical_url'))}")
        lines.append(f"- Minted at UTC: {_clean(fm.get('artifact_minted_at_utc'))}")
        lines.append(f"- Core thesis: {_clean(fm.get('artifact_core_thesis'))}")
        lines.append(f"- Mechanism: {_clean(fm.get('artifact_mechanism_summary'))}")
        lines.append(f"- Why it matters: {_clean(fm.get('artifact_why_it_matters'))}")
        lines.append('')
    return '\n'.join(lines).strip() + '\n'


def normalize_existing_source_material() -> int:
    count = 0
    if not OLD_SOURCE_ROOT.exists():
        return count
    SOURCE_ROOT.mkdir(parents=True, exist_ok=True)
    for day_dir in sorted(OLD_SOURCE_ROOT.glob('*')):
        if not day_dir.is_dir():
            continue
        for path in day_dir.iterdir():
            if not path.is_file():
                continue
            target = SOURCE_ROOT / path.name
            if target.exists():
                continue
            target.write_bytes(path.read_bytes())
            count += 1
    return count


def normalize_existing_fact_files() -> int:
    count = 0
    if not FACTS_ROOT.exists():
        return count
    for article_dir in sorted(FACTS_ROOT.glob('*')):
        if not article_dir.is_dir():
            continue
        article_id = article_dir.name
        facts = load_fact_payloads(article_id)
        if not facts:
            continue
        write_fact_files(article_id, facts)
        count += len(facts)
    return count


def normalize_existing_article_bundles() -> int:
    count = 0
    ARTICLES_ROOT.mkdir(parents=True, exist_ok=True)
    for path in list_article_bundle_paths():
        bundle = load_article_bundle(path)
        fm = dict(bundle['frontmatter'])
        facts = load_fact_payloads(fm['article_id'])
        fm['fact_count'] = len(facts)
        if facts and fm['last_stage'] in {'intake', 'filter', 'artifact'}:
            fm['last_stage'] = 'facts'
        if fm['filter_state'] == 'kept' and not _clean(fm.get('artifact_minted_at_utc')):
            fm['artifact_minted_at_utc'] = fm['updated_at_utc']
        save_article_bundle(fm, render_article_body(fm, facts))
        count += 1
    return count
