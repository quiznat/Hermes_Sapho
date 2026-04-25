from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(ROOT))

import common
import run_website_publish_pipeline


ARTICLE_TEMPLATE = """---
version: article.v1
article_id: {article_id}
ticket_id: ticket-{article_id}
source_url: https://example.com/{article_id}
canonical_url: https://example.com/{article_id}
source_title: Example {article_id}
queued_at_utc: '2026-04-12T12:00:00Z'
captured_at_utc: '2026-04-12T12:01:00Z'
curator_decision: kept
artifact_minted_at_utc: '{minted_at}'
publication_status: ready-for-daily
---
# Example

## Core Thesis

Example thesis.
'"""


def write_article(root: Path, article_id: str, minted_at: str, *, current: bool = False) -> None:
    article_root = root / article_id
    article_root.mkdir(parents=True, exist_ok=True)
    body = ARTICLE_TEMPLATE.format(article_id=article_id, minted_at=minted_at)
    if current:
        body = body.replace(
            "publication_status: ready-for-daily\n---",
            "publication_status: ready-for-daily\nartifact_publication_status: published\nartifact_publication_alias: '20260412001'\nartifact_publication_minted_at_utc: '{minted_at}'\nartifact_publication_published_at_utc: '2026-04-12T12:05:00Z'\n---".format(minted_at=minted_at),
        )
    (article_root / "article.md").write_text(body, encoding="utf-8")


class RunWebsitePublishPipelineTests(unittest.TestCase):
    def test_stale_candidates_prefers_newest_and_skips_current(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            articles_dir = Path(tmpdir) / "articles"
            write_article(articles_dir, "art-test-001", "2026-04-12T12:00:00Z")
            write_article(articles_dir, "art-test-002", "2026-04-12T12:30:00Z")
            write_article(articles_dir, "art-test-003", "2026-04-12T12:45:00Z", current=True)
            with patch.object(common, "ARTICLES_DIR", articles_dir), patch.object(run_website_publish_pipeline, "ARTICLES_DIR", articles_dir):
                self.assertEqual(run_website_publish_pipeline.stale_candidates(limit=5), ["art-test-002", "art-test-001"])

    def test_validate_requested_articles_rejects_non_publishable(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            articles_dir = Path(tmpdir) / "articles"
            write_article(articles_dir, "art-test-001", "2026-04-12T12:00:00Z", current=True)
            with patch.object(common, "ARTICLES_DIR", articles_dir), patch.object(run_website_publish_pipeline, "ARTICLES_DIR", articles_dir):
                with self.assertRaisesRegex(RuntimeError, "article_not_publishable:art-test-001"):
                    run_website_publish_pipeline.validate_requested_articles(["art-test-001"])

    def test_main_runs_publish_script_with_github_pages_env(self) -> None:
        calls: list[dict[str, object]] = []

        def fake_publish(article_id: str, *, dry_run: bool = False) -> dict[str, object]:
            calls.append({
                "article_id": article_id,
                "dry_run": dry_run,
                "site_mode": run_website_publish_pipeline.website_env().get("SAPHO_SITE_MODE"),
                "site_base_url": run_website_publish_pipeline.website_env().get("SAPHO_SITE_BASE_URL"),
                "custom_domain": run_website_publish_pipeline.website_env().get("SAPHO_SITE_CUSTOM_DOMAIN"),
            })
            return {"article_id": article_id, "returncode": 0, "stdout": f"published_artifact {article_id}", "stderr": ""}

        with patch.object(run_website_publish_pipeline, "stale_candidates", return_value=["art-test-002", "art-test-001"]), \
             patch.object(run_website_publish_pipeline, "publish_article", side_effect=fake_publish), \
             patch.object(sys, "argv", ["run_website_publish_pipeline.py", "--limit", "2", "--dry-run"]):
            rc = run_website_publish_pipeline.main()
        self.assertEqual(rc, 0)
        self.assertEqual(calls, [
            {
                "article_id": "art-test-002",
                "dry_run": True,
                "site_mode": "github-pages",
                "site_base_url": "https://research.quiznat.com",
                "custom_domain": "research.quiznat.com",
            },
            {
                "article_id": "art-test-001",
                "dry_run": True,
                "site_mode": "github-pages",
                "site_base_url": "https://research.quiznat.com",
                "custom_domain": "research.quiznat.com",
            },
        ])


if __name__ == "__main__":
    unittest.main()
