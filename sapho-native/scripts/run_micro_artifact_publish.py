from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import UTC, datetime
from email.utils import format_datetime
from pathlib import Path

from common import article_artifact_publication_current, article_file, read_markdown, slugify, utc_now, write_article_markdown
from publication_authority import assert_article_publication_authority
from render_site import (
    BASE_URL,
    PUBLIC_DIR,
    build_public_artifact_markdown,
    build_rss_items,
    first_heading,
    first_paragraph,
    html_redirect_page,
    normalize_url,
    overlay_kept_links,
    parse_existing_rss,
    parse_sections,
    payload_item_identity,
    public_article_url,
    read_text,
    rss_description,
    truncate_text,
    validate_kept_links_surface,
    visible_markdown_text,
    write_text,
)

ROOT = Path(__file__).resolve().parents[1]
LIVE_SITE = Path('/home/openclaw/.openclaw/workspace/website')
ALIAS_PATTERN = re.compile(rf"{re.escape(BASE_URL)}/a/(\d{{11}})\.html")
ARTIFACT_DEPLOY_PATHS = [
    'a',
    's',
    'artifacts/kb/queue',
    'kept-links.html',
    'data/kept-links.json',
    'rss.xml',
    'artifacts.xml',
    'data/artifacts-feed.json',
]


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def stage_path(rel: str) -> None:
    source = LIVE_SITE / rel
    target = PUBLIC_DIR / rel
    if source.is_dir():
        shutil.rmtree(target, ignore_errors=True)
        if source.exists():
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(source, target)
        else:
            target.mkdir(parents=True, exist_ok=True)
        return
    ensure_parent(target)
    if source.exists():
        shutil.copy2(source, target)
        return
    if target.exists():
        target.unlink()
    if target.suffix == '.json':
        write_text(target, '{}\n')
    else:
        write_text(target, '')


def stage_live_artifact_surfaces() -> None:
    for rel in ARTIFACT_DEPLOY_PATHS:
        stage_path(rel)


def used_live_aliases() -> set[str]:
    aliases: set[str] = set()
    kept_payload_path = PUBLIC_DIR / 'data' / 'kept-links.json'
    if kept_payload_path.exists():
        payload = json.loads(read_text(kept_payload_path))
        for item in payload.get('items') or []:
            item_id = str(item.get('id') or '').strip()
            match = re.fullmatch(r'pub-(\d{11})', item_id)
            if match:
                aliases.add(match.group(1))
            artifact_path = str(item.get('artifactWebPath') or '').strip()
            match = re.search(r'queue-(\d{11})-', artifact_path)
            if match:
                aliases.add(match.group(1))
    rss_path = PUBLIC_DIR / 'rss.xml'
    if rss_path.exists():
        for item in parse_existing_rss(read_text(rss_path)):
            match = ALIAS_PATTERN.fullmatch(str(item.get('link') or '').strip())
            if match:
                aliases.add(match.group(1))
    return aliases


def next_alias_for_date(aliases: set[str], daily_date: str) -> str:
    prefix = daily_date.replace('-', '')
    ordinals = [int(alias[-3:]) for alias in aliases if re.fullmatch(rf'{prefix}\d{{3}}', alias)]
    next_ordinal = (max(ordinals) if ordinals else 0) + 1
    return f'{prefix}{next_ordinal:03d}'


def existing_alias_for_source(source_url: str) -> str:
    identity = payload_item_identity({'url': normalize_url(source_url)})
    kept_payload_path = PUBLIC_DIR / 'data' / 'kept-links.json'
    if kept_payload_path.exists():
        payload = json.loads(read_text(kept_payload_path))
        for item in payload.get('items') or []:
            if payload_item_identity(item) != identity:
                continue
            item_id = str(item.get('id') or '').strip()
            match = re.fullmatch(r'pub-(\d{11})', item_id)
            if match:
                return match.group(1)
            artifact_path = str(item.get('artifactWebPath') or '').strip()
            match = re.search(r'queue-(\d{11})-', artifact_path)
            if match:
                return match.group(1)
    rss_path = PUBLIC_DIR / 'rss.xml'
    if rss_path.exists():
        for item in parse_existing_rss(read_text(rss_path)):
            if payload_item_identity({'url': str(item.get('source_url') or '')}) != identity:
                continue
            match = ALIAS_PATTERN.fullmatch(str(item.get('link') or '').strip())
            if match:
                return match.group(1)
    return ''


def current_item_for_article(meta: dict, body: str, alias: str, published_at: str) -> dict:
    title = first_heading(body, str(meta.get('source_title') or f'pub-{alias}'))
    title = re.sub(r'^\[[^\]]+\]\s*', '', title).strip() or f'pub-{alias}'
    slug = slugify(title, fallback=f'article-{alias[-3:]}')
    artifact_name = f'queue-{alias}-{slug}.md'
    artifact_rel = f'artifacts/kb/queue/{artifact_name}'
    summary = first_paragraph(parse_sections(body).get('Core Thesis', '')) or first_paragraph(body)
    summary = truncate_text(visible_markdown_text(summary), 280)
    source_url = normalize_url(str(meta.get('canonical_url') or meta.get('source_url') or ''))
    return {
        'id': f'pub-{alias}',
        'alias': alias,
        'daily_date': str(meta.get('published_in_daily') or str(meta.get('artifact_minted_at_utc') or '')[:10] or published_at[:10]),
        'title': title,
        'summary': summary,
        'url': source_url,
        'canonical_url': source_url,
        'published_at': published_at,
        'artifact_rel': artifact_rel,
        'link': public_article_url(alias),
        'guid': public_article_url(alias),
    }


def write_artifact_surfaces(meta: dict, body: str, item: dict) -> None:
    title = str(item['title'])
    alias = str(item['alias'])
    artifact_rel = str(item['artifact_rel'])
    source_url = str(item['canonical_url'] or item['url'])
    write_text(PUBLIC_DIR / artifact_rel, build_public_artifact_markdown(str(item['id']), title, meta, body))
    write_text(
        PUBLIC_DIR / 'a' / f'{alias}.html',
        html_redirect_page(
            title,
            f'{BASE_URL}/viewer.html?file={artifact_rel}',
            'Redirecting to the canonical Sapho artifact.',
            'Open Artifact',
        ),
    )
    write_text(
        PUBLIC_DIR / 's' / f'{alias}.html',
        html_redirect_page(
            f'{title} Source',
            source_url,
            'Redirecting to the canonical source URL.',
            'Open Source',
        ),
    )


def render_single_rss_item(item: dict) -> dict:
    source_url = normalize_url(str(item.get('canonical_url') or item.get('url') or ''))
    return {
        'source_url': source_url,
        'title': str(item['title']),
        'link': str(item['link']),
        'guid': str(item['guid']),
        'alias': str(item['alias']),
        'pubDate': format_datetime(datetime.fromisoformat(str(item['published_at']).replace('Z', '+00:00')).astimezone(UTC)),
        'description': rss_description(str(item['summary']), str(item['link']), source_url),
    }


def update_rss_feed(item: dict, generated_at: str) -> int:
    rss_path = PUBLIC_DIR / 'rss.xml'
    existing_items = parse_existing_rss(read_text(rss_path) if rss_path.exists() else None)
    candidate = render_single_rss_item(item)
    identity = payload_item_identity({'url': candidate['source_url']})
    updated: list[dict] = []
    replaced = False
    for existing in existing_items:
        existing_link = str(existing.get('link') or '').strip()
        existing_identity = payload_item_identity({'url': str(existing.get('source_url') or '')})
        if existing_identity == identity:
            if existing_link and existing_link != candidate['link']:
                raise RuntimeError(f"rss_source_conflict:{candidate['source_url']}")
            updated.append(candidate)
            replaced = True
            continue
        if existing_link == candidate['link'] and str(existing.get('source_url') or '').strip() != candidate['source_url']:
            raise RuntimeError(f"rss_link_conflict:{candidate['link']}")
        updated.append(existing)
    if not replaced:
        updated.append(candidate)
    updated.sort(
        key=lambda row: (datetime.strptime(str(row.get('pubDate') or ''), '%a, %d %b %Y %H:%M:%S %z'), str(row.get('link') or '')),
        reverse=True,
    )
    feed = build_rss_items({'items': updated})
    write_text(PUBLIC_DIR / 'rss.xml', feed)
    write_text(PUBLIC_DIR / 'artifacts.xml', feed)
    write_text(
        PUBLIC_DIR / 'data' / 'artifacts-feed.json',
        json.dumps(
            {
                'generatedAtUtc': generated_at,
                'channelTitle': 'Sapho Chapterhouse Institute Research Artifacts',
                'feedPath': '/artifacts.xml',
                'mirrorPath': '/rss.xml',
                'itemCount': len(updated),
                'sourceDataset': 'website/rss.xml',
                'filter': 'published_artifacts_only',
            },
            indent=2,
        )
        + '\n',
    )
    return len(updated)


def deploy_artifact_surfaces() -> None:
    cmd = [sys.executable, str(ROOT / 'scripts' / 'deploy_live_site.py'), '--skip-render']
    for rel in ARTIFACT_DEPLOY_PATHS:
        cmd.extend(['--path', rel])
    proc = subprocess.run(cmd, cwd=str(ROOT), text=True, env=os.environ.copy())
    if proc.returncode != 0:
        raise SystemExit(proc.returncode)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--article-id', required=True)
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--skip-deploy', action='store_true')
    parser.add_argument('--force', action='store_true')
    args = parser.parse_args()

    path = article_file(args.article_id)
    meta, body = read_markdown(path)
    status = str(meta.get('publication_status') or '')
    minted_at = str(meta.get('artifact_minted_at_utc') or '').strip()
    if status not in {'ready-for-daily', 'published'}:
        print(f'not_publishable {args.article_id} status={status or "missing"}')
        return 0
    if not minted_at:
        raise ValueError('missing_artifact_minted_at_utc')
    if not args.force and article_artifact_publication_current(meta):
        print(f'already_published {args.article_id}')
        return 0

    assert_article_publication_authority(args.article_id)

    stage_live_artifact_surfaces()
    alias = str(meta.get('artifact_publication_alias') or '').strip()
    if not alias:
        alias = existing_alias_for_source(str(meta.get('canonical_url') or meta.get('source_url') or ''))
    if not alias:
        date = str(meta.get('published_in_daily') or minted_at[:10] or utc_now()[:10])
        alias = next_alias_for_date(used_live_aliases(), date)
    if str(meta.get('artifact_publication_alias') or '').strip() != alias:
        meta['artifact_publication_alias'] = alias
        write_article_markdown(path, meta, body)

    published_at = utc_now()
    item = current_item_for_article(meta, body, alias, published_at)

    if args.dry_run:
        print(f'publish_candidate {args.article_id} alias={alias} minted={minted_at}')
        return 0

    write_artifact_surfaces(meta, body, item)
    kept_items = overlay_kept_links([item])
    validate_kept_links_surface(read_text(PUBLIC_DIR / 'kept-links.html'))
    rss_count = update_rss_feed(item, published_at)
    if not args.skip_deploy:
        deploy_artifact_surfaces()

    updated_meta, article_body = read_markdown(path)
    updated_meta['artifact_publication_alias'] = alias
    updated_meta['artifact_publication_status'] = 'published'
    updated_meta['artifact_publication_minted_at_utc'] = minted_at
    updated_meta['artifact_publication_published_at_utc'] = published_at
    write_article_markdown(path, updated_meta, article_body)
    print(f'published_artifact {args.article_id} alias={alias} kept={len(kept_items)} rss={rss_count}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
