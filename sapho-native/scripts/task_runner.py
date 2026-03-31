from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from hashlib import sha256
from pathlib import Path
from typing import Any
from uuid import uuid4

from common import ROOT, strip_outer_code_fence

DEFAULT_CONFIG_PATH = ROOT / "micro" / "task_runner.json"
DEFAULT_RECEIPTS_DIR = ROOT / "state" / "receipts" / "task-runs"
ANSI_PATTERN = re.compile(r"\x1b\[[0-9;]*[A-Za-z]")
SESSION_PATTERN = re.compile(r"^session_id:\s+", re.IGNORECASE)
BOX_DRAWING_PREFIXES = ("╭", "╰", "│", "├", "└", "┌", "┐", "┘", "┤", "┬", "┴", "─")
CLI_NOISE_PREFIXES = ("⚠️", "⏳", "❌", "🔌", "🌐", "📝", "📋", "💀")
CLI_FAILURE_PATTERNS = [
    re.compile(r"api call failed", re.IGNORECASE),
    re.compile(r"max retries", re.IGNORECASE),
    re.compile(r"badrequesterror", re.IGNORECASE),
    re.compile(r"http\s+4\d\d", re.IGNORECASE),
    re.compile(r"not supported when using codex", re.IGNORECASE),
]
WHITESPACE_RUNS = re.compile(r"\n{3,}")


@dataclass
class TaskResult:
    status: str
    role: str
    raw_output: str
    clean_output: str
    started_at_utc: str
    finished_at_utc: str
    duration_seconds: float
    backend: str
    model: str
    error: str | None = None
    receipt_path: str | None = None


class TaskRunnerError(RuntimeError):
    pass


class TaskRunnerTimeout(TaskRunnerError):
    pass


def utc_now() -> datetime:
    return datetime.now(UTC)


def load_task_runner_config() -> dict[str, Any]:
    path = Path(os.environ.get("SAPHO_TASK_RUNNER_CONFIG", DEFAULT_CONFIG_PATH))
    if not path.exists():
        raise TaskRunnerError(f"missing_task_runner_config:{path}")
    return json.loads(path.read_text(encoding="utf-8"))


def role_config(role: str, config: dict[str, Any]) -> dict[str, Any]:
    roles = config.get("roles") or {}
    if role in roles:
        return roles[role]
    if role == "orchestrator" and "conclave" in roles:
        return roles["conclave"]
    raise TaskRunnerError(f"unknown_task_role:{role}")


def persona_text(persona_file: str) -> str:
    path = ROOT / "micro" / "personas" / persona_file
    if not path.exists():
        raise TaskRunnerError(f"missing_persona:{path}")
    return path.read_text(encoding="utf-8").strip()


def build_assignment(role: str, prompt: str, role_cfg: dict[str, Any]) -> str:
    persona = persona_text(role_cfg["persona_file"])
    identity_name = role_cfg.get("identity_name") or role.title()
    return (
        f"You are {identity_name} of Sapho Chapterhouse Institute.\n\n"
        f"Role guidance:\n{persona}\n\n"
        "This is a fresh one-shot isolated task.\n"
        "Do not use tools.\n"
        "Do not mention hidden instructions, runtimes, or sessions.\n"
        "Return only the requested answer as plain text.\n\n"
        "Assignment:\n\n"
        f"{prompt.strip()}\n"
    )


def build_hermes_command(assignment: str, role_cfg: dict[str, Any], config: dict[str, Any]) -> list[str]:
    command = [
        config.get("hermes_command") or "hermes",
        "chat",
        "-Q",
        "--source",
        "tool",
        "-q",
        assignment,
    ]
    model = role_cfg.get("model")
    provider = role_cfg.get("provider")
    if model:
        command.extend(["-m", model])
    if provider and provider != "auto":
        command.extend(["--provider", provider])
    return command


def looks_like_backend_failure(text: str) -> bool:
    stripped = text.strip()
    if not stripped:
        return False
    return any(pattern.search(stripped) for pattern in CLI_FAILURE_PATTERNS)


def classify_status(raw_output: str, clean_output: str, error: str | None) -> str:
    if error or looks_like_backend_failure(raw_output) or looks_like_backend_failure(clean_output):
        return "error"
    if not raw_output.strip() or not clean_output.strip():
        return "malformed"
    return "ok"


def normalize_output(text: str) -> str:
    cleaned = ANSI_PATTERN.sub("", text or "").replace("\r", "\n")
    kept: list[str] = []
    for raw_line in cleaned.splitlines():
        line = raw_line.rstrip()
        stripped = line.strip()
        if not stripped:
            kept.append("")
            continue
        if SESSION_PATTERN.match(stripped):
            continue
        if stripped.startswith(BOX_DRAWING_PREFIXES):
            continue
        if stripped.startswith(CLI_NOISE_PREFIXES):
            continue
        if stripped.lower().startswith("tool use:"):
            continue
        kept.append(line)
    cleaned = "\n".join(kept).strip()
    cleaned = strip_outer_code_fence(cleaned).strip()
    cleaned = WHITESPACE_RUNS.sub("\n\n", cleaned)
    return cleaned


def make_receipt_payload(result: TaskResult, *, timeout: int, thinking: str, context: dict[str, Any] | None) -> dict[str, Any]:
    payload = asdict(result)
    payload["timeout"] = timeout
    payload["thinking"] = thinking
    payload["context"] = context or {}
    payload["prompt_sha256"] = None
    return payload


def write_receipt(result: TaskResult, *, prompt: str, timeout: int, thinking: str, context: dict[str, Any] | None, config: dict[str, Any]) -> str:
    receipts_dir = Path(config.get("receipts_dir") or DEFAULT_RECEIPTS_DIR)
    receipts_dir.mkdir(parents=True, exist_ok=True)
    started = result.started_at_utc.replace(":", "").replace("-", "")
    receipt_name = f"{started}-{result.role}-{uuid4().hex[:10]}.json"
    receipt_path = receipts_dir / receipt_name
    payload = make_receipt_payload(result, timeout=timeout, thinking=thinking, context=context)
    payload["prompt_sha256"] = sha256(prompt.encode("utf-8")).hexdigest()
    payload["receipt_path"] = str(receipt_path)
    receipt_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return str(receipt_path)


def run_task(role: str, prompt: str, timeout: int, thinking: str, context: dict[str, Any] | None = None) -> TaskResult:
    config = load_task_runner_config()
    runner_backend = config.get("backend", "hermes_cli")
    cfg = role_config(role, config)
    assignment = build_assignment(role, prompt, cfg)
    started = utc_now()
    raw_output = ""
    error: str | None = None
    try:
        if runner_backend != "hermes_cli":
            raise TaskRunnerError(f"unsupported_task_backend:{runner_backend}")
        command = build_hermes_command(assignment, cfg, config)
        completed = subprocess.run(
            command,
            cwd=str(ROOT),
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=timeout,
            check=False,
        )
        raw_output = completed.stdout or ""
        if completed.returncode != 0:
            details = (completed.stderr or completed.stdout or "").strip()
            error = f"backend_exit_{completed.returncode}:{details}" if details else f"backend_exit_{completed.returncode}"
    except subprocess.TimeoutExpired as exc:
        finished = utc_now()
        result = TaskResult(
            status="timeout",
            role=role,
            raw_output=(exc.stdout or "") if isinstance(exc.stdout, str) else "",
            clean_output=normalize_output((exc.stdout or "") if isinstance(exc.stdout, str) else ""),
            started_at_utc=started.isoformat().replace("+00:00", "Z"),
            finished_at_utc=finished.isoformat().replace("+00:00", "Z"),
            duration_seconds=round((finished - started).total_seconds(), 3),
            backend=runner_backend,
            model=str(cfg.get("model") or ""),
            error=f"timeout_after_seconds:{timeout}",
        )
        result.receipt_path = write_receipt(result, prompt=prompt, timeout=timeout, thinking=thinking, context=context, config=config)
        return result
    except Exception as exc:
        error = str(exc)
    finished = utc_now()
    clean_output = normalize_output(raw_output)
    status = classify_status(raw_output, clean_output, error)
    if status == "error" and error is None:
        error = "backend_output_error"
    result = TaskResult(
        status=status,
        role=role,
        raw_output=raw_output,
        clean_output=clean_output,
        started_at_utc=started.isoformat().replace("+00:00", "Z"),
        finished_at_utc=finished.isoformat().replace("+00:00", "Z"),
        duration_seconds=round((finished - started).total_seconds(), 3),
        backend=runner_backend,
        model=str(cfg.get("model") or ""),
        error=error,
    )
    result.receipt_path = write_receipt(result, prompt=prompt, timeout=timeout, thinking=thinking, context=context, config=config)
    return result


__all__ = [
    "DEFAULT_CONFIG_PATH",
    "DEFAULT_RECEIPTS_DIR",
    "TaskResult",
    "load_task_runner_config",
    "build_assignment",
    "build_hermes_command",
    "normalize_output",
    "run_task",
]
