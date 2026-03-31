#!/usr/bin/env python3
"""Parallel Sapho PDF -> Markdown helpers with stdlib-only fallbacks.

Design goals:
- Prefer high-quality arXiv HTML when a PDF maps to an arXiv paper.
- Otherwise, extract readable text from text-based PDFs without external binaries.
- Produce LLM-friendly markdown so downstream pipelines stop ingesting binary PDF garbage.
"""

from __future__ import annotations

import gzip
import html
import io
import json
import re
import tarfile
import zlib
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path, PurePosixPath
from typing import Any
from urllib.request import Request, urlopen

try:
    from pypdf import PdfReader
except Exception:  # pragma: no cover - optional dependency
    PdfReader = None

UA = 'Mozilla/5.0 (ParallelSapho pdf-markdown pipeline)'
PDF_TOKEN_RE = re.compile(rb'\((?:\\.|[^\\)])*\)|<([0-9A-Fa-f\s]+)>', re.DOTALL)
STREAM_RE = re.compile(rb'(<<.*?>>)?\s*stream\r?\n(.*?)\r?\nendstream', re.DOTALL)
TEXT_OBJECT_RE = re.compile(rb'BT(.*?)ET', re.DOTALL)
ARXIV_ID_RE = re.compile(r'(\d{4}\.\d{4,5})(?:v\d+)?')


class TextExtractor(HTMLParser):
    BLOCK_TAGS = {'p', 'div', 'section', 'article', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li', 'tr', 'pre', 'blockquote'}
    SKIP_TAGS = {'script', 'style', 'noscript'}

    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []
        self.skip = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in self.SKIP_TAGS:
            self.skip += 1
            return
        if self.skip:
            return
        if tag in self.BLOCK_TAGS:
            self.parts.append('\n\n')
        if tag == 'li':
            self.parts.append('- ')

    def handle_endtag(self, tag: str) -> None:
        if tag in self.SKIP_TAGS and self.skip:
            self.skip -= 1
            return
        if self.skip:
            return
        if tag in self.BLOCK_TAGS:
            self.parts.append('\n')

    def handle_data(self, data: str) -> None:
        if self.skip:
            return
        txt = data.strip()
        if txt:
            self.parts.append(txt + ' ')

    def text(self) -> str:
        body = ''.join(self.parts)
        body = re.sub(r'\n{3,}', '\n\n', body)
        body = re.sub(r'[ \t]{2,}', ' ', body)
        return body.strip() + '\n'


def parse_arxiv_id(value: str) -> str:
    match = ARXIV_ID_RE.search(str(value or '').strip())
    return match.group(1) if match else ''


def fetch_url(url: str, *, timeout: int = 30) -> str:
    req = Request(url, headers={'User-Agent': UA})
    with urlopen(req, timeout=timeout) as response:
        return response.read().decode('utf-8', errors='replace')


def fetch_best_arxiv_html(arxiv_id: str, *, allow_abs_fallback: bool = True) -> tuple[str, str]:
    candidates = [
        f'https://arxiv.org/html/{arxiv_id}v1',
        f'https://arxiv.org/html/{arxiv_id}',
    ]
    if allow_abs_fallback:
        candidates.append(f'https://arxiv.org/abs/{arxiv_id}')
    last_error: Exception | None = None
    for url in candidates:
        try:
            return url, fetch_url(url)
        except Exception as exc:  # pragma: no cover - network failure path
            last_error = exc
    raise RuntimeError(f'failed_arxiv_fetch:{arxiv_id}:{last_error}')


def _now_label() -> str:
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')


def _bad_arxiv_html_capture(title: str, markdown: str) -> bool:
    low_title = str(title or '').strip().lower()
    low_body = str(markdown or '').lower()
    if low_title in {'', 'untitled document'}:
        return True
    if 'check_x_y' in low_body:
        return True
    if len(low_body) < 5000 and 'introduction' not in low_body:
        return True
    return False


def _normalize_text(text: str) -> str:
    body = html.unescape(str(text or ''))
    body = body.replace('\xa0', ' ')
    body = body.replace('\r', '\n')
    body = re.sub(r'\n{3,}', '\n\n', body)
    body = '\n'.join(re.sub(r'[ \t]+', ' ', line).strip() for line in body.splitlines())
    body = '\n'.join(line for line in body.splitlines() if line)
    return body.strip()


def convert_html_to_markdownish(html_body: str, *, source_url: str, title_hint: str = '', note: str = '') -> str:
    scoped_html = str(html_body or '')
    for pattern in (r'(?is)<article\b[^>]*>(.*?)</article>', r'(?is)<main\b[^>]*>(.*?)</main>'):
        match = re.search(pattern, scoped_html)
        if match:
            scoped_html = match.group(1)
            break
    parser = TextExtractor()
    parser.feed(scoped_html)
    body = parser.text().strip()
    title_line = _normalize_text(title_hint)
    if not title_line:
        first_line = next((line.strip() for line in body.splitlines() if line.strip()), '')
        title_line = first_line[:200] if first_line else 'PDF markdown conversion'
    preface = [
        f'# {title_line}',
        '',
        f'Source: {source_url}',
        '',
        f'Generated: {_now_label()}',
        '',
    ]
    if note:
        preface.extend([f'> Note: {note}', '', ''])
    return '\n'.join(preface) + body + '\n'


def fetch_arxiv_markdown(arxiv_id: str, *, allow_abs_fallback: bool = True) -> dict[str, Any]:
    source_url, html_body = fetch_best_arxiv_html(arxiv_id, allow_abs_fallback=allow_abs_fallback)
    title_match = re.search(r'(?is)<title[^>]*>(.*?)</title>', html_body)
    title = _normalize_text(title_match.group(1) if title_match else f'arXiv {arxiv_id}')
    method = 'arxiv_abs' if '/abs/' in source_url else 'arxiv_html'
    note = (
        'Generated from arXiv abstract HTML because full-text HTML was unavailable on this VM.'
        if method == 'arxiv_abs'
        else 'Generated from arXiv HTML full text as a higher-fidelity fallback where native PDF extraction tools are unavailable on this VM.'
    )
    markdown = convert_html_to_markdownish(
        html_body,
        source_url=source_url,
        title_hint=title,
        note=note,
    )
    if method == 'arxiv_html' and _bad_arxiv_html_capture(title, markdown):
        raise RuntimeError(f'bad_arxiv_html_capture:{arxiv_id}')
    return {
        'ok': True,
        'method': method,
        'sourceUrl': source_url,
        'title': title,
        'markdown': markdown,
    }


def _fetch_arxiv_source_bundle(arxiv_id: str) -> bytes:
    url = f'https://arxiv.org/e-print/{arxiv_id}'
    req = Request(url, headers={'User-Agent': UA})
    with urlopen(req, timeout=30) as response:
        return response.read()


def _read_text_from_tar_member(tf: tarfile.TarFile, member_name: str) -> str:
    fh = tf.extractfile(member_name)
    if fh is None:
        return ''
    raw = fh.read()
    for encoding in ('utf-8', 'latin-1'):
        try:
            return raw.decode(encoding)
        except Exception:
            continue
    return raw.decode('utf-8', errors='replace')


def _tex_strip_comments(text: str) -> str:
    return re.sub(r'(?<!\\)%.*', '', text)


def _resolve_tex_include(base_name: str, include_name: str, files: dict[str, str]) -> str:
    base_dir = PurePosixPath(base_name).parent
    candidate = PurePosixPath(str(include_name or '').strip())
    if not candidate.suffix:
        candidate = candidate.with_suffix('.tex')
    resolved = str((base_dir / candidate).as_posix())
    return resolved if resolved in files else ''


def _expand_tex_includes(name: str, files: dict[str, str], seen: set[str] | None = None) -> str:
    seen = seen or set()
    if name in seen:
        return ''
    seen.add(name)
    text = files.get(name, '')
    if not text:
        return ''

    pattern = re.compile(r'\\(?:input|include)\{([^{}]+)\}')

    def replace(match: re.Match[str]) -> str:
        target = _resolve_tex_include(name, match.group(1), files)
        if not target:
            return ''
        return '\n' + _expand_tex_includes(target, files, seen) + '\n'

    return pattern.sub(replace, text)


def _tex_to_markdown(text: str) -> str:
    body = str(text or '')
    doc_match = re.search(r'(?is)\\begin\{document\}(.*)\\end\{document\}', body)
    if doc_match:
        body = doc_match.group(1)
    body = _tex_strip_comments(body)
    body = re.sub(r'(?is)\\begin\{(?:figure\*?|table\*?|equation\*?|align\*?|tikzpicture|lstlisting)\}.*?\\end\{(?:figure\*?|table\*?|equation\*?|align\*?|tikzpicture|lstlisting)\}', '\n', body)
    body = re.sub(r'\\(?:begin|end)\{(?:itemize|enumerate|description)\}', '\n', body)
    body = re.sub(r'\\maketitle', '', body)
    body = re.sub(r'\\title\{([^{}]+)\}', r'# \1\n', body)
    body = re.sub(r'\\section\*?\{([^{}]+)\}', r'\n## \1\n', body)
    body = re.sub(r'\\subsection\*?\{([^{}]+)\}', r'\n### \1\n', body)
    body = re.sub(r'\\subsubsection\*?\{([^{}]+)\}', r'\n#### \1\n', body)
    body = re.sub(r'\\paragraph\*?\{([^{}]+)\}', r'\n**\1** ', body)
    body = re.sub(r'\\begin\{abstract\}', '\n## Abstract\n', body)
    body = re.sub(r'\\end\{abstract\}', '\n', body)
    body = re.sub(r'\\begin\{document\}|\\end\{document\}', '\n', body)
    body = re.sub(r'\\(?:textbf|textit|emph|underline|textrm|texttt)\{([^{}]*)\}', r'\1', body)
    body = re.sub(r'\\href\{[^{}]*\}\{([^{}]*)\}', r'\1', body)
    body = re.sub(r'\\url\{([^{}]*)\}', r'\1', body)
    body = re.sub(r'\\(?:cite|citet|citep|ref|eqref|label|footnote)\{[^{}]*\}', '', body)
    body = re.sub(r'\\(?:item|newline|linebreak)\b', '\n- ', body)
    body = re.sub(r'\\[a-zA-Z]+\*?(?:\[[^\]]*\])?', '', body)
    body = body.replace('{', '').replace('}', '')
    body = body.replace('~', ' ')
    body = body.replace('\\', '\n')
    body = _normalize_text(body)
    body = '\n'.join(
        line for line in body.splitlines()
        if line.strip() and not re.fullmatch(r'footnote\d*', line.strip(), flags=re.IGNORECASE)
    )
    return _normalize_text(body)


def _looks_like_submission_template(text: str) -> bool:
    lowered = str(text or '').lower()
    template_markers = (
        'submission guidelines',
        'camera-ready',
        'double-blind review',
        'icml 2024',
        'do not distribute',
        'paper template',
        'format of the paper',
        'dimensions',
        'anonymous submission',
    )
    hit_count = sum(1 for marker in template_markers if marker in lowered)
    return hit_count >= 2


def _score_tex_candidate(markdown_body: str) -> int:
    body = str(markdown_body or '')
    lowered = body.lower()
    lines = [line.strip() for line in body.splitlines() if line.strip()]
    score = 0

    # Prefer substantial documents with section structure.
    score += min(len(body) // 2000, 30)
    score += min(sum(1 for line in lines if line.startswith('## ')), 20)

    # Penalize known conference-template / submission boilerplate.
    if _looks_like_submission_template(lowered):
        score -= 80

    # Reward paper-like content signals.
    positive_markers = ('abstract', 'introduction', 'method', 'results', 'discussion', 'conclusion')
    score += sum(3 for marker in positive_markers if marker in lowered)
    return score


def fetch_arxiv_source_markdown(arxiv_id: str) -> dict[str, Any]:
    bundle = _fetch_arxiv_source_bundle(arxiv_id)
    raw = gzip.decompress(bundle)
    tf = tarfile.open(fileobj=io.BytesIO(raw), mode='r:')
    names = [member.name for member in tf.getmembers() if member.isfile()]
    files = {name: _read_text_from_tar_member(tf, name) for name in names if name.endswith('.tex') or name.endswith('.sty')}

    readme = {}
    if '00README.json' in names:
        try:
            readme = json.loads(_read_text_from_tar_member(tf, '00README.json'))
        except Exception:
            readme = {}

    top_levels = [
        str(item.get('filename') or '').strip()
        for item in list(readme.get('sources') or [])
        if str(item.get('usage') or '').strip() == 'toplevel'
    ]
    if not top_levels:
        top_levels = [name for name in files if name.endswith('.tex')]
    if not top_levels:
        raise RuntimeError(f'no_tex_sources:{arxiv_id}')

    candidates: list[tuple[int, str, str, str]] = []
    for name in top_levels:
        if name not in files:
            continue
        expanded = _expand_tex_includes(name, files, set())
        if not expanded:
            continue
        body = _tex_to_markdown(expanded)
        if not body:
            continue

        raw_title = ''
        raw_title_match = re.search(r'(?im)^\s*\\title(?:\[[^\]]*\])?\{(.+?)\}\s*$', expanded)
        if raw_title_match:
            raw_title = _normalize_text(re.sub(r'\\[a-zA-Z]+', ' ', raw_title_match.group(1)).replace('\\', ' '))

        title = raw_title
        if not title:
            title_match = re.search(r'(?m)^#\s+(.+)$', body)
            if title_match:
                title = _normalize_text(title_match.group(1))
        if not title:
            title = f'arXiv {arxiv_id}'

        candidates.append((_score_tex_candidate(body), name, title, body))

    if not candidates:
        raise RuntimeError(f'empty_tex_markdown:{arxiv_id}')

    # Keep the highest-quality manuscript candidate (avoid template.tex / style boilerplate).
    candidates.sort(key=lambda row: row[0], reverse=True)
    best_score, best_name, title, body = candidates[0]
    if best_score < -20:
        raise RuntimeError(f'low_quality_tex_candidate:{arxiv_id}:{best_name}')

    markdown = build_pdf_markdown(
        source_label=f'https://arxiv.org/e-print/{arxiv_id}',
        title=title,
        body=body,
        note='Generated from the arXiv e-print source bundle as a higher-fidelity fallback when HTML full text is unavailable.',
    )
    return {
        'ok': True,
        'method': 'arxiv_source_tex',
        'sourceUrl': f'https://arxiv.org/e-print/{arxiv_id}',
        'title': title,
        'markdown': markdown,
        'sourceCandidate': best_name,
    }


def fetch_arxiv_pdf_markdown(arxiv_id: str) -> dict[str, Any]:
    url = f'https://arxiv.org/pdf/{arxiv_id}.pdf'
    req = Request(url, headers={'User-Agent': UA})
    with urlopen(req, timeout=45) as response:
        pdf_bytes = response.read()
    converted = convert_pdf_bytes_to_markdown(pdf_bytes, source_url=url)
    markdown = str(converted.get('markdown') or '').strip()
    if not markdown:
        raise RuntimeError(f'empty_pdf_markdown:{arxiv_id}')
    return {
        'ok': True,
        'method': str(converted.get('method') or 'arxiv_pdf_stream_extract'),
        'sourceUrl': str(converted.get('sourceUrl') or url),
        'title': str(converted.get('title') or f'arXiv {arxiv_id}').strip(),
        'markdown': markdown + ('\n' if not markdown.endswith('\n') else ''),
    }


def fetch_arxiv_best_markdown(arxiv_id: str, *, allow_abs_fallback: bool = True) -> dict[str, Any]:
    for fn in (
        lambda: fetch_arxiv_markdown(arxiv_id, allow_abs_fallback=False),
        lambda: fetch_arxiv_pdf_markdown(arxiv_id),
    ):
        try:
            return fn()
        except Exception:
            continue
    if allow_abs_fallback:
        return fetch_arxiv_markdown(arxiv_id, allow_abs_fallback=True)
    raise RuntimeError(f'failed_arxiv_best_markdown:{arxiv_id}')


def _decode_pdf_literal_string(token: bytes) -> str:
    if len(token) < 2:
        return ''
    data = token[1:-1]
    out = bytearray()
    i = 0
    while i < len(data):
        byte = data[i]
        if byte != 0x5C:  # backslash
            out.append(byte)
            i += 1
            continue
        i += 1
        if i >= len(data):
            break
        esc = data[i]
        if esc in b'nrtbf':
            mapping = {
                ord('n'): b'\n',
                ord('r'): b'\r',
                ord('t'): b'\t',
                ord('b'): b'\b',
                ord('f'): b'\f',
            }
            out.extend(mapping.get(esc, bytes([esc])))
            i += 1
            continue
        if esc in b'()\\':
            out.append(esc)
            i += 1
            continue
        if 48 <= esc <= 55:  # octal
            digits = [esc]
            i += 1
            for _ in range(2):
                if i < len(data) and 48 <= data[i] <= 55:
                    digits.append(data[i])
                    i += 1
                else:
                    break
            out.append(int(bytes(digits), 8))
            continue
        out.append(esc)
        i += 1
    try:
        return out.decode('utf-8')
    except Exception:
        return out.decode('latin-1', errors='replace')


def _decode_pdf_hex_string(token: bytes) -> str:
    cleaned = re.sub(rb'\s+', b'', token[1:-1])
    if not cleaned:
        return ''
    if len(cleaned) % 2 == 1:
        cleaned += b'0'
    try:
        raw = bytes.fromhex(cleaned.decode('ascii', errors='ignore'))
    except Exception:
        return ''
    for encoding in ('utf-16-be', 'utf-8', 'latin-1'):
        try:
            if encoding == 'utf-16-be' and b'\x00' not in raw and not raw.startswith((b'\xfe\xff', b'\xff\xfe')):
                continue
            return raw.decode(encoding, errors='replace')
        except Exception:
            continue
    return raw.decode('latin-1', errors='replace')


def _decode_pdf_string_token(token: bytes) -> str:
    if token.startswith(b'('):
        return _decode_pdf_literal_string(token)
    if token.startswith(b'<') and token.endswith(b'>'):
        return _decode_pdf_hex_string(token)
    return ''


def _decode_stream_bytes(header: bytes, stream: bytes) -> bytes:
    filters = header or b''
    data = stream
    if b'/FlateDecode' in filters:
        try:
            data = zlib.decompress(stream)
        except Exception:
            return b''
    return data


def _extract_text_blocks_from_stream(decoded: bytes) -> list[str]:
    blocks = TEXT_OBJECT_RE.findall(decoded)
    if not blocks:
        return []
    out: list[str] = []
    for block in blocks:
        fragments = [_decode_pdf_string_token(match.group(0)) for match in PDF_TOKEN_RE.finditer(block)]
        text = _normalize_text(''.join(fragment for fragment in fragments if fragment))
        if text:
            out.append(text)
    return out


def extract_text_from_pdf_bytes(raw_bytes: bytes) -> str:
    if PdfReader is not None:
        try:
            reader = PdfReader(io.BytesIO(raw_bytes))
            pages: list[str] = []
            for page in reader.pages:
                page_text = _normalize_text(page.extract_text() or '')
                if page_text:
                    pages.append(page_text)
            body = '\n\n'.join(pages).strip()
            if body:
                return body
        except Exception:
            pass

    blocks: list[str] = []
    for match in STREAM_RE.finditer(raw_bytes):
        header = match.group(1) or b''
        stream = match.group(2) or b''
        decoded = _decode_stream_bytes(header, stream)
        if not decoded:
            continue
        blocks.extend(_extract_text_blocks_from_stream(decoded))
    deduped: list[str] = []
    seen: set[str] = set()
    for block in blocks:
        key = block[:500]
        if key in seen:
            continue
        seen.add(key)
        deduped.append(block)
    return '\n\n'.join(deduped).strip()


def extract_pdf_metadata(raw_bytes: bytes) -> dict[str, str]:
    metadata: dict[str, str] = {}
    for field in ('Title', 'Author', 'Subject'):
        match = re.search(rb'/' + field.encode('ascii') + rb'\s*\((.*?)\)', raw_bytes, re.DOTALL)
        if not match:
            continue
        metadata[field] = _normalize_text(_decode_pdf_literal_string(b'(' + match.group(1) + b')'))
    return metadata


def build_pdf_markdown(*, source_label: str, title: str, body: str, note: str) -> str:
    header = [
        f'# {title or "PDF markdown conversion"}',
        '',
        f'Source: {source_label}',
        '',
        f'Generated: {_now_label()}',
        '',
        f'> Note: {note}',
        '',
    ]
    normalized_body = _normalize_text(body)
    if normalized_body:
        header.extend([normalized_body, ''])
    return '\n'.join(header)


def convert_pdf_bytes_to_markdown(pdf_bytes: bytes, *, source_url: str = '', fallback_title: str = '') -> dict[str, Any]:
    metadata = extract_pdf_metadata(pdf_bytes)
    body = extract_text_from_pdf_bytes(pdf_bytes)
    title = metadata.get('Title') or _normalize_text(fallback_title)
    if not title:
        first_line = next((line.strip() for line in body.splitlines() if line.strip()), '')
        title = first_line[:200] if first_line else 'PDF markdown conversion'
    markdown = build_pdf_markdown(
        source_label=source_url or 'local PDF bytes',
        title=title,
        body=body,
        note='Generated from PDF stream extraction fallback because native PDF-to-text binaries are unavailable on this VM. Layout may be imperfect.',
    )
    return {
        'ok': bool(body or title),
        'method': 'pdf_stream_extract',
        'sourceUrl': source_url or 'local-pdf-bytes',
        'title': title,
        'markdown': markdown,
        'metadata': metadata,
    }


def convert_local_pdf_to_markdown(pdf_path: Path | str, *, source_url: str = '') -> dict[str, Any]:
    path = Path(pdf_path)
    pdf_bytes = path.read_bytes()
    fallback_title = path.stem
    source_label = source_url or str(path)
    result = convert_pdf_bytes_to_markdown(pdf_bytes, source_url=source_label, fallback_title=fallback_title)
    result['localPath'] = str(path)
    return result
