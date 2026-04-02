from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(ROOT))

import article_law_reviews
import common
import remediate_historical_imports


def article_markdown(*, article_id: str, ticket_id: str, publication_status: str = "published", imported: bool = True) -> str:
    imported_block = f"imported_from_runtime_article_id: runtime-{article_id}\n" if imported else ""
    return f"""---
version: article.v1
article_id: {article_id}
ticket_id: {ticket_id}
source_url: https://example.com/{article_id}
canonical_url: https://example.com/{article_id}
source_title: Example {article_id}
queued_at_utc: '2026-03-31T00:00:00Z'
captured_at_utc: '2026-03-31T00:05:00Z'
curator_decision: kept
curated_at_utc: '2026-03-31T00:10:00Z'
artifact_minted_at_utc: '2026-03-31T00:15:00Z'
publication_status: {publication_status}
{imported_block}---
# Example Article

## Core Thesis

A thesis.

## Why It Matters

It matters.

## Key Findings

- One finding.

## Limits

One limit.
"""


def source_markdown(*, article_id: str) -> str:
    return f"""---
version: source-capture.v1
article_id: {article_id}
source_url: https://example.com/{article_id}
canonical_url: https://example.com/{article_id}
source_title: Example {article_id}
captured_at_utc: '2026-03-31T00:05:00Z'
content_type: text/html
capture_kind: html
linked_paper_urls: []
---
# Source Capture

## Title

Example {article_id}

## Body

This is complete source body text with enough detail for rerun.
"""


def ticket_markdown(*, article_id: str, ticket_id: str) -> str:
    return f"""---
version: ticket.v1
ticket_id: {ticket_id}
article_id: {article_id}
status: pending
source_url: https://example.com/{article_id}
canonical_url: https://example.com/{article_id}
source_title: Example {article_id}
queued_at_utc: '2026-03-31T00:00:00Z'
---
# Ticket
"""


class RemediateHistoricalImportsTests(unittest.TestCase):
    def test_select_candidates_returns_only_imported_quarantined_or_compliant_targets(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            articles_dir = Path(tmpdir) / "articles"
            queue_dir = Path(tmpdir) / "queue"
            articles_dir.mkdir(parents=True, exist_ok=True)
            queue_dir.mkdir(parents=True, exist_ok=True)

            for article_id, ticket_id, imported, policy_status in [
                ("art-a", "ticket-a", True, "legacy_quarantined"),
                ("art-b", "ticket-b", True, "current_law_compliant"),
                ("art-c", "ticket-c", True, "blocked_not_publishable"),
                ("art-d", "ticket-d", False, "not_applicable"),
            ]:
                root = articles_dir / article_id
                root.mkdir(parents=True, exist_ok=True)
                (root / "article.md").write_text(article_markdown(article_id=article_id, ticket_id=ticket_id, imported=imported), encoding="utf-8")
                (root / "historical-policy.json").write_text(json.dumps({
                    "article_id": article_id,
                    "policy_status": policy_status,
                    "applies": imported,
                }) + "\n", encoding="utf-8")
                (queue_dir / f"{ticket_id}.md").write_text(ticket_markdown(article_id=article_id, ticket_id=ticket_id), encoding="utf-8")

            with patch.object(common, "ARTICLES_DIR", articles_dir), patch.object(common, "QUEUE_DIR", queue_dir), patch.object(remediate_historical_imports, "ARTICLES_DIR", articles_dir), patch.object(remediate_historical_imports, "QUEUE_DIR", queue_dir):
                candidates = remediate_historical_imports.select_candidate_article_ids()

            self.assertEqual(candidates, ["art-a", "art-b"])

    def test_remediation_run_executes_lane_and_writes_report_without_publishing(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            articles_dir = Path(tmpdir) / "articles"
            queue_dir = Path(tmpdir) / "queue"
            reports_dir = Path(tmpdir) / "state" / "reports"
            articles_dir.mkdir(parents=True, exist_ok=True)
            queue_dir.mkdir(parents=True, exist_ok=True)

            article_id = "art-remediate-001"
            ticket_id = "ticket-remediate-001"
            article_root = articles_dir / article_id
            article_root.mkdir(parents=True, exist_ok=True)
            (article_root / "article.md").write_text(article_markdown(article_id=article_id, ticket_id=ticket_id), encoding="utf-8")
            (article_root / "source.md").write_text(source_markdown(article_id=article_id), encoding="utf-8")
            (article_root / "historical-policy.json").write_text(json.dumps({
                "article_id": article_id,
                "policy_status": "legacy_quarantined",
                "applies": True,
            }) + "\n", encoding="utf-8")
            (queue_dir / f"{ticket_id}.md").write_text(ticket_markdown(article_id=article_id, ticket_id=ticket_id), encoding="utf-8")

            def fake_run(cmd: list[str], check: bool, cwd: str, text: bool, capture_output: bool) -> subprocess.CompletedProcess[str]:
                self.assertIn("run_micro_article_lane.py", cmd[1])
                self.assertNotIn("run_micro_artifact_publish.py", " ".join(cmd))
                updated = article_markdown(article_id=article_id, ticket_id=ticket_id, publication_status="ready-for-daily")
                (article_root / "article.md").write_text(updated, encoding="utf-8")
                (article_root / "historical-policy.json").write_text(json.dumps({
                    "article_id": article_id,
                    "policy_status": "current_law_compliant",
                    "applies": True,
                }) + "\n", encoding="utf-8")
                return subprocess.CompletedProcess(args=cmd, returncode=0, stdout="ok", stderr="")

            with patch.object(common, "ARTICLES_DIR", articles_dir), patch.object(common, "QUEUE_DIR", queue_dir), patch.object(remediate_historical_imports, "ARTICLES_DIR", articles_dir), patch.object(remediate_historical_imports, "QUEUE_DIR", queue_dir), patch.object(remediate_historical_imports, "REPORTS_DIR", reports_dir), patch("remediate_historical_imports.subprocess.run", side_effect=fake_run):
                summary = remediate_historical_imports.remediate_articles([article_id], replay_date="2026-04-01")

            self.assertEqual(summary["article_count"], 1)
            self.assertEqual(summary["status_counts"]["ok"], 1)
            row = summary["articles"][0]
            self.assertEqual(row["article_id"], article_id)
            self.assertEqual(row["before_policy_status"], "legacy_quarantined")
            self.assertEqual(row["after_policy_status"], "current_law_compliant")
            self.assertEqual(row["after_publication_status"], "ready-for-daily")
            self.assertFalse(row["published_artifact"])
            report_path = Path(summary["report_path"])
            self.assertTrue(report_path.exists())


if __name__ == "__main__":
    unittest.main()
