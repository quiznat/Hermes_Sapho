from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(ROOT))

import task_runner
import common
from micro_common import run_loose_agent


class TaskRunnerTests(unittest.TestCase):
    def test_normalize_output_strips_hermes_cli_chrome(self) -> None:
        raw = """
╭─ ⚕ Hermes ───────────────────────────────────────────────────────────────────╮
```text
KEEP

Because this source contains benchmark evidence.
```

session_id: 20260331_032122_c6700d
"""
        self.assertEqual(
            task_runner.normalize_output(raw),
            "KEEP\n\nBecause this source contains benchmark evidence.",
        )

    def test_normalize_output_collapses_duplicated_payload(self) -> None:
        payload = "article_id: art-1\nsummary: repeated once\nclaims:\n  - claim_id: claim-001\n    claim_text: A concrete result.\n"
        raw = f"\n╭─ ⚕ Hermes ──╮\n{payload}{payload}\nsession_id: abc\n"
        self.assertEqual(task_runner.normalize_output(raw), payload.strip())

    def test_load_frontmatter_repairs_bracket_prefixed_scalar(self) -> None:
        text = "version: article.v1\nsource_title: [2512.08296] Towards a Science of Scaling Agent Systems\n"
        meta = common.load_frontmatter(text)
        self.assertEqual(meta["source_title"], "[2512.08296] Towards a Science of Scaling Agent Systems")

    def test_build_hermes_command_uses_role_model(self) -> None:
        config = task_runner.load_task_runner_config()
        role_cfg = task_runner.role_config("curator", config)
        command = task_runner.build_hermes_command("Decide keep or discard.", role_cfg, config)
        self.assertIn("hermes", command[0])
        self.assertIn("-m", command)
        self.assertIn("gpt-5.4", command)
        self.assertIn("--source", command)
        self.assertIn("tool", command)

    def test_backend_failure_output_is_classified_as_error(self) -> None:
        raw = "⚠️ API call failed (attempt 1/3): BadRequestError [HTTP 400]"
        clean = task_runner.normalize_output(raw)
        self.assertEqual(task_runner.classify_status(raw, clean, None), "error")

    def test_run_task_writes_receipt_and_returns_ok(self) -> None:
        completed = subprocess.CompletedProcess(
            args=["hermes"],
            returncode=0,
            stdout="\n╭─ ⚕ Hermes ──╮\nOK\n\nsession_id: abc\n",
            stderr="",
        )
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = Path(tmpdir) / "task_runner.json"
            receipts_dir = Path(tmpdir) / "receipts"
            config = {
                "backend": "hermes_cli",
                "hermes_command": "hermes",
                "receipts_dir": str(receipts_dir),
                "roles": {
                    "curator": {
                        "persona_file": "curator.md",
                        "identity_name": "Curator",
                        "provider": "auto",
                        "model": "demo-model"
                    }
                }
            }
            config_path.write_text(json.dumps(config), encoding="utf-8")
            with patch.dict(os.environ, {"SAPHO_TASK_RUNNER_CONFIG": str(config_path)}, clear=False):
                with patch("task_runner.subprocess.run", return_value=completed):
                    result = task_runner.run_task("curator", "Reply with OK.", timeout=30, thinking="off")
            receipt = json.loads(Path(result.receipt_path).read_text(encoding="utf-8"))
            self.assertEqual(result.status, "ok")
            self.assertEqual(result.clean_output, "OK")
            self.assertTrue(result.receipt_path)
            self.assertEqual(receipt["status"], "ok")
            self.assertEqual(receipt["role"], "curator")
            self.assertEqual(receipt["model"], "demo-model")

    def test_run_task_uses_file_prompt_transport_for_large_assignment(self) -> None:
        completed = subprocess.CompletedProcess(
            args=[sys.executable],
            returncode=0,
            stdout="\n╭─ ⚕ Hermes ──╮\nOK\n\nsession_id: abc\n",
            stderr="",
        )
        captured: list[list[str]] = []

        def fake_run(command, **kwargs):
            captured.append(command)
            self.assertEqual(command[0], sys.executable)
            self.assertEqual(command[1], "-c")
            prompt_path = Path(command[3])
            self.assertTrue(prompt_path.exists())
            self.assertGreater(prompt_path.stat().st_size, 24000)
            self.assertNotIn("x" * 1000, " ".join(command))
            return completed

        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = Path(tmpdir) / "task_runner.json"
            receipts_dir = Path(tmpdir) / "receipts"
            config = {
                "backend": "hermes_cli",
                "hermes_command": "hermes",
                "receipts_dir": str(receipts_dir),
                "roles": {
                    "curator": {
                        "persona_file": "curator.md",
                        "identity_name": "Curator",
                        "provider": "auto",
                        "model": "demo-model"
                    }
                }
            }
            config_path.write_text(json.dumps(config), encoding="utf-8")
            prompt = "x" * 26000
            with patch.dict(os.environ, {"SAPHO_TASK_RUNNER_CONFIG": str(config_path)}, clear=False):
                with patch("task_runner.subprocess.run", side_effect=fake_run):
                    result = task_runner.run_task("curator", prompt, timeout=30, thinking="off")
        self.assertEqual(result.status, "ok")
        self.assertEqual(result.clean_output, "OK")
        self.assertEqual(len(captured), 1)

    def test_run_loose_agent_uses_new_runner_by_default(self) -> None:
        fake_result = task_runner.TaskResult(
            status="ok",
            role="curator",
            raw_output="raw",
            clean_output="clean",
            started_at_utc="2026-03-31T00:00:00Z",
            finished_at_utc="2026-03-31T00:00:01Z",
            duration_seconds=1.0,
            backend="hermes_cli",
            model="demo-model",
            error=None,
            receipt_path=None,
        )
        with patch.dict(os.environ, {}, clear=True):
            with patch("micro_common.run_task", return_value=fake_result) as mocked_runner:
                with patch("micro_common.run_pocket_agent") as mocked_legacy:
                    result = run_loose_agent("curator", "prompt")
        self.assertEqual(result, "clean")
        mocked_runner.assert_called_once()
        mocked_legacy.assert_not_called()

    def test_run_loose_agent_can_roll_back_to_legacy_backend(self) -> None:
        with patch.dict(os.environ, {"SAPHO_USE_LEGACY_OPENCLAW": "1"}, clear=True):
            with patch("micro_common.run_pocket_agent", return_value="```text\nlegacy\n```") as mocked_legacy:
                with patch("micro_common.run_task") as mocked_runner:
                    result = run_loose_agent("curator", "prompt")
        self.assertEqual(result, "legacy")
        mocked_legacy.assert_called_once()
        mocked_runner.assert_not_called()


if __name__ == "__main__":
    unittest.main()
