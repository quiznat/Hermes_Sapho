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
import run_micro_artifact_publish


def write_article(root: Path, article_id: str) -> Path:
    article_root = root / article_id
    article_root.mkdir(parents=True, exist_ok=True)
    body = """---
version: article.v1
article_id: art-test-601
ticket_id: ticket-art-test-601
source_url: https://example.com/source
canonical_url: https://example.com/source
source_title: Example Source
queued_at_utc: '2026-04-05T00:00:00Z'
captured_at_utc: '2026-04-05T00:01:00Z'
curator_decision: kept
artifact_minted_at_utc: '2026-04-05T00:02:00Z'
publication_status: ready-for-daily
---
# Example Source

## Core Thesis

Example thesis.
"""
    (article_root / "article.md").write_text(body, encoding="utf-8")
    return article_root


class RunMicroArtifactPublishTests(unittest.TestCase):
    def test_github_pages_mode_rebuilds_full_artifact_site(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            articles_dir = Path(tmpdir) / "articles"
            public_dir = Path(tmpdir) / "public"
            article_root = write_article(articles_dir, "art-test-601")
            with patch.object(common, "ARTICLES_DIR", articles_dir), \
                 patch.object(run_micro_artifact_publish, "article_file", lambda article_id: articles_dir / article_id / "article.md"), \
                 patch.object(run_micro_artifact_publish, "PUBLIC_DIR", public_dir), \
                 patch.object(run_micro_artifact_publish, "site_mode", return_value="github-pages"), \
                 patch.object(run_micro_artifact_publish, "assert_article_publication_authority", return_value={"verdict": "pass"}), \
                 patch.object(run_micro_artifact_publish, "render_artifact_site", return_value=[{"id": "pub-20260405001"}]):
                with patch.object(sys, "argv", ["run_micro_artifact_publish.py", "--article-id", "art-test-601"]):
                    rc = run_micro_artifact_publish.main()
            self.assertEqual(rc, 0)
            text = (article_root / "article.md").read_text(encoding="utf-8")
            self.assertIn("artifact_publication_status: published", text)
            self.assertIn("artifact_publication_alias:", text)


if __name__ == "__main__":
    unittest.main()
