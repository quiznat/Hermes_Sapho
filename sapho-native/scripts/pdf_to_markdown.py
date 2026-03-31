#!/usr/bin/env python3
"""Canonical PDF -> Markdown entrypoint for the parallel-sapho rail."""

from __future__ import annotations

import argparse
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request, urlopen

from pdf_markdown_local import (
    convert_local_pdf_to_markdown,
    convert_pdf_bytes_to_markdown,
    fetch_arxiv_best_markdown,
    parse_arxiv_id,
)

UA = 'Mozilla/5.0 (ParallelSapho pdf-to-markdown)'


def resolve_output_path(input_value: str, provided: str) -> Path:
    if provided:
        return Path(provided)
    candidate = Path(input_value)
    if candidate.exists():
        return candidate.with_suffix('.md')
    arxiv_id = parse_arxiv_id(input_value)
    if arxiv_id:
        return Path.cwd() / f'{arxiv_id}.md'
    parsed = urlparse(input_value)
    if parsed.scheme in {'http', 'https'}:
        stem = Path(parsed.path or 'document.pdf').stem or 'document'
        return Path.cwd() / f'{stem}.md'
    raise SystemExit('output path required for this input')


def fetch_pdf_url(url: str) -> bytes:
    req = Request(url, headers={'User-Agent': UA})
    with urlopen(req, timeout=45) as response:
        content_type = (response.headers.get('content-type') or '').split(';')[0].strip().lower()
        if 'pdf' not in content_type and not url.lower().endswith('.pdf'):
            raise SystemExit(f'not_a_pdf_url:{url}')
        return response.read()


def main() -> int:
    parser = argparse.ArgumentParser(description='Convert a PDF or arXiv paper into markdown.')
    parser.add_argument('input', help='Local PDF path, PDF URL, arXiv URL, or arXiv id')
    parser.add_argument('--output', help='Destination markdown path')
    args = parser.parse_args()

    output_path = resolve_output_path(args.input, args.output or '')
    input_path = Path(args.input)
    if input_path.exists():
        result = convert_local_pdf_to_markdown(input_path)
    else:
        arxiv_id = parse_arxiv_id(args.input)
        if arxiv_id:
            result = fetch_arxiv_best_markdown(arxiv_id)
        else:
            pdf_bytes = fetch_pdf_url(args.input)
            fallback_title = Path(urlparse(args.input).path or 'document.pdf').stem or 'document'
            result = convert_pdf_bytes_to_markdown(pdf_bytes, source_url=args.input, fallback_title=fallback_title)

    if not result.get('ok'):
        raise SystemExit(f'conversion_failed:{result}')

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(str(result.get('markdown') or ''), encoding='utf-8')
    print(output_path)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
