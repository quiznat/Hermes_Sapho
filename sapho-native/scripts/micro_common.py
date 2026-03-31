from __future__ import annotations

import os
import re
from pathlib import Path

import common
from common import (
    CHROME_LINE_PATTERNS,
    CHROME_SEGMENT_PATTERNS,
    CONTENT_STOP_PATTERNS,
    ROOT,
    compact_source_markdown,
    dump_markdown,
    markdown_section,
    source_body_text,
    strip_outer_code_fence,
)
from openclaw_pocket_agent import run_pocket_agent
from task_runner import run_task

MICRO_ROOT = ROOT / "micro"
MICRO_JOBS = MICRO_ROOT / "jobs"
VISIBLE_ID_PATTERN = re.compile(r"\b(?:art-[0-9a-z-]+|claim-\d+|evidence-\d+|ticket-[0-9a-z-]+)\b")


def read_job(name: str) -> str:
    return (MICRO_JOBS / name).read_text(encoding="utf-8").strip()


def article_stage_path(article_id: str, stage: str, suffix: str = ".md") -> Path:
    return common.ARTICLES_DIR / article_id / f"micro-{stage}{suffix}"


def daily_stage_path(date: str, stage: str, suffix: str = ".md") -> Path:
    return common.DAILY_DIR / date / f"micro-{stage}{suffix}"


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def run_loose_agent(agent_id: str, prompt: str, *, timeout: int = 60, thinking: str = "off") -> str:
    if os.environ.get("SAPHO_USE_LEGACY_OPENCLAW", "").strip().lower() in {"1", "true", "yes", "on"}:
        raw = run_pocket_agent(agent_id, prompt, timeout=timeout, thinking=thinking)
        return strip_outer_code_fence(raw).strip()
    result = run_task(
        agent_id,
        prompt,
        timeout=timeout,
        thinking=thinking,
        context={"adapter": "run_loose_agent"},
    )
    if result.status != "ok":
        raise RuntimeError(result.error or f"task_runner_status:{result.status}")
    return result.clean_output


def clean_loose_text(text: str) -> str:
    cleaned = strip_outer_code_fence(text).strip()
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    return cleaned


def compact_handoff(text: str, max_chars: int = 2200) -> str:
    collapsed = re.sub(r"[ \t]+", " ", text).strip()
    if len(collapsed) <= max_chars:
        return collapsed
    return collapsed[:max_chars].rstrip() + "…"


def parse_keep_discard(text: str) -> tuple[str, str]:
    lines = [line.strip() for line in clean_loose_text(text).splitlines() if line.strip()]
    if not lines:
        raise ValueError("empty_curator_output")
    positive = ("keep", "kept", "retain", "retained", "accept", "accepted", "admit", "admitted")
    negative = ("discard", "discarded", "drop", "dropped", "reject", "rejected", "block", "blocked")
    prefixes = ("decision", "verdict", "judgment", "answer")

    for idx, raw_line in enumerate(lines):
        line = re.sub(r"^[\-\*\d\.\)\s]+", "", raw_line).strip()
        lowered = line.lower()
        for prefix in prefixes:
            if lowered.startswith(f"{prefix}:"):
                line = line.split(":", 1)[1].strip()
                lowered = line.lower()
                break
        if lowered.startswith(positive):
            return "kept", "\n".join(lines[idx + 1 :]).strip()
        if lowered.startswith(negative):
            return "discarded", "\n".join(lines[idx + 1 :]).strip()
    raise ValueError("missing_keep_or_discard")


def parse_pass_block(text: str) -> tuple[str, str]:
    lines = [line.strip() for line in clean_loose_text(text).splitlines() if line.strip()]
    if not lines:
        raise ValueError("empty_gate_output")
    for idx, line in enumerate(lines):
        head = line.upper()
        if head.startswith("PASS"):
            return "pass", "\n".join(lines[idx + 1 :]).strip()
        if head.startswith("BLOCK"):
            return "block", "\n".join(lines[idx + 1 :]).strip()
    raise ValueError("missing_pass_or_block")


def bullet_lines(text: str) -> list[str]:
    lines: list[str] = []
    for raw in clean_loose_text(text).splitlines():
        line = raw.strip()
        if not line:
            continue
        line = re.sub(r"^[-*]\s*", "", line)
        line = re.sub(r"^\d+\.\s*", "", line)
        if line:
            lines.append(line)
    return lines


def assert_no_visible_internal_ids(text: str, *, label: str) -> None:
    if VISIBLE_ID_PATTERN.search(text):
        raise ValueError(f"visible_internal_id_leak:{label}")


def package_markdown(meta: dict, body: str, path: Path) -> None:
    assert_no_visible_internal_ids(body, label=str(path))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(dump_markdown(meta, body), encoding="utf-8")


def summary_title(body: str, fallback: str) -> str:
    first = body.splitlines()[0].strip() if body.strip() else ""
    if first.startswith("# "):
        return first[2:].strip() or fallback
    return fallback


def summary_section(body: str, name: str) -> str:
    return markdown_section(body, f"## {name}")


def source_excerpt(source_body: str, *, max_chars: int = 3600) -> str:
    return compact_source_markdown(source_body, max_chars=max_chars)


def filtered_source_text(source_body: str) -> str:
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
        if len(trimmed_lines) >= 80:
            break
    return "\n".join(trimmed_lines).strip()


def head_tail_source_excerpt(source_body: str, *, max_chars: int = 4200, tail_chars: int = 1200) -> str:
    normalized = filtered_source_text(source_body)
    if not normalized:
        return source_excerpt(source_body, max_chars=max_chars)
    if len(normalized) <= max_chars or tail_chars <= 0:
        return normalized[:max_chars].rstrip()

    marker = "\n\n[...]\n\n"
    head_budget = max_chars - tail_chars - len(marker)
    if head_budget < max_chars // 2:
        head_budget = max_chars // 2
        tail_chars = max_chars - head_budget - len(marker)

    head = normalized[:head_budget]
    if "\n" in head:
        head = head.rsplit("\n", 1)[0]
    tail = normalized[-tail_chars:]
    if "\n" in tail:
        tail = tail.split("\n", 1)[-1]
    return f"{head.rstrip()}{marker}{tail.lstrip()}".strip()
