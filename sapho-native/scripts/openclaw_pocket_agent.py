from __future__ import annotations

import argparse
import fcntl
import os
import pwd
import re
import shutil
import signal
import subprocess
import tempfile
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MICRO_PERSONAS_DIR = ROOT / "micro" / "personas"
OPENCLAW_CWD = Path("/tmp")
POCKET_AGENT_LOCK = Path("/tmp/openclaw-pocket-agent.lock")

ANSI_PATTERN = re.compile(r"\x1b\[[0-9;]*[A-Za-z]")
NOISE_PATTERNS = [
    re.compile(r"^\s*⚠️\s*✉️ Message failed\b"),
    re.compile(r"^\s*Config overwrite:"),
    re.compile(r"^\s*Updated ~/.openclaw/openclaw\.json"),
    re.compile(r"^\s*Workspace OK:"),
    re.compile(r"^\s*Sessions OK:"),
    re.compile(r"^\s*Agent:"),
    re.compile(r"^\s*Workspace:"),
    re.compile(r"^\s*Agent dir:"),
    re.compile(r"^\s*Model:"),
    re.compile(r"^\s*Deleted agent:"),
    re.compile(r"^\s*Failed to move to Trash"),
    re.compile(r"^\s*Routing rules map channel/account/peer"),
    re.compile(r"^\s*Channel status reflects local config/creds"),
    re.compile(r"^\s*Docs:\s+https://docs\.openclaw\.ai/cli/agent"),
    re.compile(r"^\s*-\s+channels\.telegram\.groupPolicy"),
    re.compile(r"^\s*Add sender IDs to channels\.telegram\.groupAllowFrom"),
]

WORKER_SPECS = {
    "curator": {
        "persona_file": "curator.md",
        "seed_agent": "curator",
        "model": "openrouter/google/gemini-2.5-flash-lite",
        "identity_name": "Curator",
    },
    "extractor": {
        "persona_file": "extractor.md",
        "seed_agent": "extractor",
        "model": "openrouter/google/gemini-2.5-flash-lite",
        "identity_name": "Extractor",
    },
    "synthesist": {
        "persona_file": "synthesist.md",
        "seed_agent": "synthesist",
        "model": "openrouter/moonshotai/kimi-k2.5",
        "identity_name": "Synthesist",
    },
    "orchestrator": {
        "persona_file": "conclave.md",
        "seed_agent": "orchestrator",
        "model": "openrouter/google/gemini-2.5-flash",
        "identity_name": "Conclave",
    },
}


def openclaw_cmd(*parts: str) -> list[str]:
    if pwd.getpwuid(os.geteuid()).pw_name == "openclaw":
        return list(parts)
    return ["sudo", "-n", "-u", "openclaw", *parts]


def worker_spec(agent_id: str) -> dict[str, str]:
    spec = WORKER_SPECS.get(agent_id)
    if spec is not None:
        return spec
    return {
        "persona_file": "synthesist.md",
        "seed_agent": "synthesist",
        "model": "openrouter/moonshotai/kimi-k2.5",
        "identity_name": agent_id.strip() or "Worker",
    }


def run_cmd(cmd: list[str], *, timeout: int | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        cmd,
        check=True,
        cwd=str(OPENCLAW_CWD),
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=timeout,
    )


def load_persona_bootstrap(agent_id: str) -> str:
    spec = worker_spec(agent_id)
    path = MICRO_PERSONAS_DIR / spec["persona_file"]
    return path.read_text(encoding="utf-8").strip()


def safe_write(path: Path, text: str) -> None:
    if path.exists():
        path.unlink()
    path.write_text(text.rstrip() + "\n", encoding="utf-8")
    path.chmod(0o666)


def stage_workspace(agent_id: str, workspace: Path, assignment: str) -> None:
    spec = worker_spec(agent_id)
    persona_text = load_persona_bootstrap(agent_id)
    files = {
        "AGENTS.md": (
            "This is a disposable one-shot work session.\n"
            "Read BOOTSTRAP.md, IDENTITY.md, SOUL.md, TOOLS.md, and USER.md.\n"
            "Do not use tools.\n"
            "Do not read or write any other files.\n"
            "Return only the requested answer.\n"
        ),
        "BOOTSTRAP.md": (
            "You are sitting down at a clean temporary desk for one assignment only.\n"
            "Read IDENTITY.md, SOUL.md, TOOLS.md, and USER.md.\n"
            "Complete the single assignment.\n"
            "Do not ask clarifying questions.\n"
            "Do not mention this workspace.\n"
            "Do not create or edit files.\n"
            "When the answer is complete, stop.\n"
        ),
        "IDENTITY.md": (
            f"# {spec['identity_name']}\n\n"
            f"You are {spec['identity_name']} of Sapho Chapterhouse Institute.\n"
        ),
        "SOUL.md": (
            f"{persona_text}\n\n"
            "This is a fresh isolated session.\n"
            "There is no prior context and nothing persists after this run.\n"
            "Use only the materials already provided in this workspace.\n"
        ),
        "TOOLS.md": (
            "Tools are off for this assignment.\n"
            "No git.\n"
            "No shell.\n"
            "No file edits.\n"
            "No browsing.\n"
            "Answer in plain text only.\n"
        ),
        "USER.md": (
            "# Single Assignment\n\n"
            "This is the only assignment in this session.\n\n"
            f"{assignment.strip()}\n\n"
            "Return only the requested answer.\n"
        ),
        "HEARTBEAT.md": "",
    }
    for name, text in files.items():
        safe_write(workspace / name, text)


def seed_agent_dir(agent_id: str, agent_dir: Path) -> None:
    spec = worker_spec(agent_id)
    seed_root = Path(f"/home/openclaw/.openclaw/agents/{spec['seed_agent']}/agent")
    for filename in ["auth-profiles.json", "models.json"]:
        run_cmd(
            openclaw_cmd("cp", str(seed_root / filename), str(agent_dir / filename)),
            timeout=30,
        )


def sanitize_output(text: str) -> str:
    cleaned = ANSI_PATTERN.sub("", text or "").replace("\r", "\n")
    lines = cleaned.splitlines()
    kept: list[str] = []
    for raw in lines:
        line = raw.rstrip()
        stripped = line.strip()
        if not stripped:
            kept.append("")
            continue
        if stripped.startswith(("│", "◇", "├", "╭", "╰")):
            continue
        if any(pattern.search(stripped) for pattern in NOISE_PATTERNS):
            continue
        kept.append(line)
    cleaned = "\n".join(kept).strip()
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    return cleaned


def compose_message(assignment: str) -> str:
    return (
        "This is a disposable one-shot work session.\n"
        "Read AGENTS.md, BOOTSTRAP.md, IDENTITY.md, SOUL.md, TOOLS.md, and USER.md for role context.\n"
        "Do not use tools.\n"
        "Do not read or write any other files.\n"
        "Complete the assignment below and return only the requested answer.\n\n"
        "Assignment:\n\n"
        f"{assignment.strip()}\n"
    )


def delete_worker(worker_id: str) -> None:
    subprocess.run(
        openclaw_cmd("openclaw", "agents", "delete", worker_id, "--force"),
        cwd=str(OPENCLAW_CWD),
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=30,
        check=False,
    )


class PocketAgentLock:
    def __init__(self, path: Path) -> None:
        self.path = path
        self.handle: object | None = None

    def __enter__(self) -> "PocketAgentLock":
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.handle = open(self.path, "a+", encoding="utf-8")
        fcntl.flock(self.handle.fileno(), fcntl.LOCK_EX)
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        if self.handle is None:
            return
        try:
            fcntl.flock(self.handle.fileno(), fcntl.LOCK_UN)
        finally:
            self.handle.close()
            self.handle = None


def run_pocket_agent(agent_id: str, assignment: str, *, timeout: int = 600, thinking: str = "off") -> str:
    spec = worker_spec(agent_id)
    root = Path(tempfile.mkdtemp(prefix=f"openclaw-pocket-{agent_id}-", dir="/tmp"))
    agent_dir = root / "agent"
    workspace = root / "workspace"
    worker_id = f"pocket{re.sub(r'[^a-z0-9]+', '', agent_id.lower())[:12]}{uuid.uuid4().hex[:10]}"
    session_id = f"{worker_id}-{uuid.uuid4().hex[:10]}"
    proc: subprocess.Popen[str] | None = None
    try:
        with PocketAgentLock(POCKET_AGENT_LOCK):
            agent_dir.mkdir(mode=0o777)
            workspace.mkdir(mode=0o777)
            root.chmod(0o777)
            agent_dir.chmod(0o777)
            workspace.chmod(0o777)

            seed_agent_dir(agent_id, agent_dir)
            run_cmd(
                openclaw_cmd(
                    "openclaw",
                    "agents",
                    "add",
                    worker_id,
                    "--non-interactive",
                    "--agent-dir",
                    str(agent_dir),
                    "--workspace",
                    str(workspace),
                    "--model",
                    spec["model"],
                ),
                timeout=60,
            )
            stage_workspace(agent_id, workspace, assignment)

            cmd = openclaw_cmd(
                "openclaw",
                "agent",
                "--local",
                "--agent",
                worker_id,
                "--session-id",
                session_id,
                "--message",
                compose_message(assignment),
                "--thinking",
                thinking,
                "--timeout",
                str(timeout),
            )
            proc = subprocess.Popen(
                cmd,
                cwd=str(OPENCLAW_CWD),
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                start_new_session=True,
            )
            try:
                stdout, stderr = proc.communicate(timeout=timeout + 45)
            except subprocess.TimeoutExpired as exc:
                try:
                    os.killpg(proc.pid, signal.SIGTERM)
                except ProcessLookupError:
                    pass
                try:
                    stdout, stderr = proc.communicate(timeout=5)
                except subprocess.TimeoutExpired:
                    try:
                        os.killpg(proc.pid, signal.SIGKILL)
                    except ProcessLookupError:
                        pass
                    stdout, stderr = proc.communicate()
                raise RuntimeError(f"pocket_agent_timeout:{agent_id}:{timeout}") from exc
            if proc.returncode != 0:
                raise RuntimeError(f"pocket_agent_failed:{agent_id}:{(stderr or '').strip()}")
            output = sanitize_output(stdout)
            if not output:
                raise RuntimeError(f"empty_pocket_agent_output:{agent_id}")
            return output
    finally:
        if proc is not None and proc.poll() is None:
            try:
                os.killpg(proc.pid, signal.SIGTERM)
            except ProcessLookupError:
                pass
        delete_worker(worker_id)
        shutil.rmtree(root, ignore_errors=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--agent", required=True)
    parser.add_argument("--prompt-file", required=True)
    parser.add_argument("--timeout", type=int, default=600)
    parser.add_argument("--thinking", default="off")
    args = parser.parse_args()
    prompt = Path(args.prompt_file).read_text(encoding="utf-8")
    print(run_pocket_agent(args.agent, prompt, timeout=args.timeout, thinking=args.thinking))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
