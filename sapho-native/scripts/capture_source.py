from __future__ import annotations

import argparse
import re
from http.client import IncompleteRead
from urllib.request import Request, urlopen

from common import (
    article_dir,
    article_file,
    best_effort_html_to_text,
    canonicalize_article_url,
    extract_linked_paper_urls,
    make_article_id,
    read_markdown,
    source_file,
    ticket_path,
    utc_now,
    write_article_markdown,
    write_markdown,
)
from pdf_markdown_local import convert_pdf_bytes_to_markdown, fetch_arxiv_best_markdown, parse_arxiv_id

USER_AGENT = "SaphoParallel/0.1 (+https://sapho.chapterhouse)"


def read_response_bytes(response) -> bytes:
    chunks: list[bytes] = []
    while True:
        try:
            chunk = response.read(1024 * 1024)
        except IncompleteRead as exc:
            if exc.partial:
                chunks.append(exc.partial)
            break
        if not chunk:
            break
        chunks.append(chunk)
    return b"".join(chunks)


def fetch_response(url: str) -> tuple[bytes, str, str, int]:
    req = Request(url, headers={"User-Agent": USER_AGENT})
    with urlopen(req, timeout=45) as response:
        raw_bytes = read_response_bytes(response)
        content_type = (response.headers.get("content-type") or "").split(";")[0].strip().lower()
        status_code = int(getattr(response, "status", 0) or response.getcode() or 0)
    title = ""
    text = ""
    if "pdf" not in content_type and not url.lower().endswith(".pdf"):
        text = raw_bytes.decode("utf-8", errors="replace")
    if "<title" in text.lower():
        match = re.search(r"<title[^>]*>(.*?)</title>", text, re.IGNORECASE | re.DOTALL)
        if match:
            title = re.sub(r"\s+", " ", match.group(1)).strip()
    return raw_bytes, title, content_type, status_code


def fetch_url(url: str) -> tuple[str, str, str, int]:
    raw_bytes, title, content_type, status_code = fetch_response(url)
    return raw_bytes.decode("utf-8", errors="replace"), title, content_type, status_code


def strip_pdf_markdown_wrapper(markdown: str) -> str:
    blocks = [block.strip() for block in str(markdown or "").split("\n\n") if block.strip()]
    while blocks and (
        blocks[0].startswith("# ")
        or blocks[0].startswith("Source:")
        or blocks[0].startswith("Generated:")
        or blocks[0].startswith("> Note:")
    ):
        blocks.pop(0)
    return "\n\n".join(blocks).strip()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ticket-id", required=True)
    args = parser.parse_args()

    ticket_meta, ticket_body = read_markdown(ticket_path(args.ticket_id))
    article_id = ticket_meta.get("article_id") or make_article_id(ticket_meta["source_url"], ticket_meta["queued_at_utc"])
    captured_at = utc_now()
    source_url = ticket_meta["source_url"]
    canonical_url = canonicalize_article_url(str(ticket_meta.get("canonical_url") or source_url))
    title = ""
    content_type = ""
    status_code = 0
    arxiv_id = parse_arxiv_id(source_url)
    if arxiv_id:
        try:
            converted = fetch_arxiv_best_markdown(arxiv_id, allow_abs_fallback=False)
            title = str(converted.get("title") or source_url)
            body_text = strip_pdf_markdown_wrapper(str(converted.get("markdown") or "")) or "Paper capture returned no readable markdown."
            content_type = "application/pdf" if str(converted.get("method") or "").startswith("pdf") else "text/html"
            status_code = 200
            capture_kind = str(converted.get("method") or "arxiv")
            linked_paper_urls = []
            write_markdown(
                source_file(article_id),
                {
                    "version": "source-capture.v1",
                    "article_id": article_id,
                    "ticket_id": args.ticket_id,
                    "source_url": source_url,
                    "canonical_url": canonical_url,
                    "source_title": title or source_url,
                    "capture_kind": capture_kind,
                    "http_status": status_code,
                    "content_type": content_type,
                    "captured_at_utc": captured_at,
                    "linked_paper_urls": linked_paper_urls,
                },
                f"# Source Capture\n\n## Title\n\n{title or source_url}\n\n## Body\n\n{body_text.strip()}\n",
            )

            write_article_markdown(
                article_file(article_id),
                {
                    "version": "article.v1",
                    "article_id": article_id,
                    "ticket_id": args.ticket_id,
                    "source_url": source_url,
                    "canonical_url": canonical_url,
                    "source_title": title or source_url,
                    "queued_at_utc": ticket_meta["queued_at_utc"],
                    "captured_at_utc": captured_at,
                    "curator_decision": "pending",
                    "artifact_minted_at_utc": "",
                    "evidence_count": 0,
                    "claim_count": 0,
                    "publication_status": "pending",
                },
                "# Pending Article\n\nThis article has been captured and is waiting for Curator.\n",
            )

            ticket_meta["article_id"] = article_id
            ticket_meta["status"] = "captured"
            ticket_meta["canonical_url"] = canonical_url
            write_markdown(ticket_path(args.ticket_id), ticket_meta, ticket_body)
            print(article_dir(article_id))
            return 0
        except Exception as exc:
            write_markdown(
                source_file(article_id),
                {
                    "version": "source-capture.v1",
                    "article_id": article_id,
                    "ticket_id": args.ticket_id,
                    "source_url": source_url,
                    "canonical_url": canonical_url,
                    "source_title": source_url,
                    "capture_kind": "capture-blocked",
                    "http_status": status_code,
                    "content_type": content_type,
                    "captured_at_utc": captured_at,
                    "source_capture_gate_reason": "abstract-only-paper-source",
                },
                f"# Source Remediation Needed\n\nFull paper capture failed for this paper source. Abstract-only capture is not allowed.\n\n{exc}\n",
            )
            write_article_markdown(
                article_file(article_id),
                {
                    "version": "article.v1",
                    "article_id": article_id,
                    "ticket_id": args.ticket_id,
                    "source_url": source_url,
                    "canonical_url": canonical_url,
                    "source_title": source_url,
                    "queued_at_utc": ticket_meta["queued_at_utc"],
                    "captured_at_utc": captured_at,
                    "curator_decision": "pending",
                    "artifact_minted_at_utc": "",
                    "evidence_count": 0,
                    "claim_count": 0,
                    "publication_status": "capture-blocked",
                    "source_capture_gate_reason": "abstract-only-paper-source",
                    "source_remediation_required": True,
                },
                "# Source Remediation Needed\n\nThis paper source could not be captured at full-text level. Abstract-only capture is blocked.\n",
            )
            ticket_meta["article_id"] = article_id
            ticket_meta["status"] = "capture-blocked"
            ticket_meta["canonical_url"] = canonical_url
            ticket_meta["source_capture_gate_reason"] = "abstract-only-paper-source"
            write_markdown(ticket_path(args.ticket_id), ticket_meta, ticket_body)
            print(article_dir(article_id))
            return 0
    try:
        raw_bytes, title, content_type, status_code = fetch_response(source_url)
    except Exception as exc:
        write_markdown(
            source_file(article_id),
            {
                "version": "source-capture.v1",
                "article_id": article_id,
                "ticket_id": args.ticket_id,
                "source_url": source_url,
                "canonical_url": canonical_url,
                "source_title": source_url,
                "capture_kind": "error",
                "http_status": status_code,
                "content_type": content_type,
                "captured_at_utc": captured_at,
            },
            f"# Source Capture Error\n\n{exc}\n",
        )
        write_article_markdown(
            article_file(article_id),
            {
                "version": "article.v1",
                "article_id": article_id,
                "ticket_id": args.ticket_id,
                "source_url": source_url,
                "canonical_url": canonical_url,
                "source_title": source_url,
                "queued_at_utc": ticket_meta["queued_at_utc"],
                "captured_at_utc": captured_at,
                "curator_decision": "pending",
                "artifact_minted_at_utc": "",
                "evidence_count": 0,
                "claim_count": 0,
                "publication_status": "capture-blocked",
            },
            "# Capture Blocked\n\nThe source could not be fetched.\n",
        )
        ticket_meta["article_id"] = article_id
        ticket_meta["status"] = "capture-blocked"
        write_markdown(ticket_path(args.ticket_id), ticket_meta, ticket_body)
        print(article_dir(article_id))
        return 0

    if "html" in content_type:
        capture_kind = "html"
        raw_text = raw_bytes.decode("utf-8", errors="replace")
        body_text = best_effort_html_to_text(source_url, raw_text)
        linked_paper_urls = extract_linked_paper_urls(raw_text)
    elif "text/" in content_type or content_type in {"application/xml", "application/xhtml+xml"}:
        capture_kind = "text"
        raw_text = raw_bytes.decode("utf-8", errors="replace")
        body_text = raw_text
        linked_paper_urls = extract_linked_paper_urls(raw_text)
    elif "pdf" in content_type or source_url.lower().endswith(".pdf"):
        converted = convert_pdf_bytes_to_markdown(
            raw_bytes,
            source_url=canonical_url or source_url,
            fallback_title=title or source_url,
        )
        capture_kind = str(converted.get("method") or "pdf")
        title = str(converted.get("title") or title or source_url)
        body_text = strip_pdf_markdown_wrapper(str(converted.get("markdown") or "")) or "PDF capture returned no readable markdown."
        linked_paper_urls = []
    else:
        capture_kind = "binary"
        body_text = f"Unsupported capture kind: {content_type or 'unknown'}"
        linked_paper_urls = []

    write_markdown(
        source_file(article_id),
            {
                "version": "source-capture.v1",
                "article_id": article_id,
                "ticket_id": args.ticket_id,
                "source_url": source_url,
                "canonical_url": canonical_url,
                "source_title": title or source_url,
                "capture_kind": capture_kind,
                "http_status": status_code,
                "content_type": content_type,
                "captured_at_utc": captured_at,
                "linked_paper_urls": linked_paper_urls,
        },
        f"# Source Capture\n\n## Title\n\n{title or source_url}\n\n## Body\n\n{body_text.strip()}\n",
    )

    write_article_markdown(
        article_file(article_id),
            {
                "version": "article.v1",
                "article_id": article_id,
                "ticket_id": args.ticket_id,
                "source_url": source_url,
                "canonical_url": canonical_url,
                "source_title": title or source_url,
                "queued_at_utc": ticket_meta["queued_at_utc"],
                "captured_at_utc": captured_at,
            "curator_decision": "pending",
            "artifact_minted_at_utc": "",
            "evidence_count": 0,
            "claim_count": 0,
            "publication_status": "pending",
        },
        "# Pending Article\n\nThis article has been captured and is waiting for Curator.\n",
    )

    ticket_meta["article_id"] = article_id
    ticket_meta["status"] = "captured"
    ticket_meta["canonical_url"] = canonical_url
    write_markdown(ticket_path(args.ticket_id), ticket_meta, ticket_body)
    print(article_dir(article_id))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
