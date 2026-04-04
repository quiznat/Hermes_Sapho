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
import publication_authority
from common import dump_markdown


def write_article(root: Path, article_id: str, *, publication_status: str = "ready-for-daily", artifact_published: bool = True) -> Path:
    article_root = root / article_id
    article_root.mkdir(parents=True, exist_ok=True)
    minted_at = "2026-04-04T00:15:00Z"
    meta = {
        "version": "article.v1",
        "article_id": article_id,
        "ticket_id": f"ticket-{article_id}",
        "source_url": f"https://example.com/{article_id}",
        "canonical_url": f"https://example.com/{article_id}",
        "source_title": f"Source {article_id}",
        "queued_at_utc": "2026-04-04T00:00:00Z",
        "captured_at_utc": "2026-04-04T00:05:00Z",
        "curator_decision": "kept",
        "artifact_minted_at_utc": minted_at,
        "publication_status": publication_status,
        "evidence_count": 1,
        "claim_count": 1,
    }
    if artifact_published:
        meta.update(
            {
                "artifact_publication_status": "published",
                "artifact_publication_minted_at_utc": minted_at,
                "artifact_publication_published_at_utc": "2026-04-04T00:20:00Z",
            }
        )
    body = "# Example\n\n## Core Thesis\n\nExample thesis.\n"
    (article_root / "article.md").write_text(dump_markdown(meta, body), encoding="utf-8")
    return article_root


def write_validation(article_root: Path, *, overall_status: str = "pass") -> None:
    (article_root / "validation.json").write_text(
        json.dumps({"article_id": article_root.name, "overall_status": overall_status, "checks": {}}, indent=2) + "\n",
        encoding="utf-8",
    )


def write_policy(article_root: Path, *, current_law_eligible: bool = True, policy_status: str = "current_law_compliant", applies: bool = True) -> None:
    (article_root / "historical-policy.json").write_text(
        json.dumps(
            {
                "article_id": article_root.name,
                "applies": applies,
                "policy_status": policy_status,
                "current_law_eligible": current_law_eligible,
                "publication_status": "ready-for-daily",
                "validation_status": "pass",
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )


class PublicationAuthorityTests(unittest.TestCase):
    def test_article_authority_blocks_failed_validation(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            articles_dir = Path(tmpdir) / "articles"
            article_root = write_article(articles_dir, "art-test-401")
            write_validation(article_root, overall_status="fail")
            write_policy(article_root)
            with patch.object(common, "ARTICLES_DIR", articles_dir), patch.object(publication_authority, "ARTICLES_DIR", articles_dir):
                decision = publication_authority.evaluate_article_publication_authority("art-test-401")
            self.assertEqual(decision["verdict"], "block")
            self.assertIn("validation_fail", decision["reasons"])

    def test_article_authority_blocks_ineligible_historical_package(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            articles_dir = Path(tmpdir) / "articles"
            article_root = write_article(articles_dir, "art-test-402")
            write_validation(article_root, overall_status="pass")
            write_policy(article_root, current_law_eligible=False, policy_status="legacy_quarantined")
            with patch.object(common, "ARTICLES_DIR", articles_dir), patch.object(publication_authority, "ARTICLES_DIR", articles_dir):
                decision = publication_authority.evaluate_article_publication_authority("art-test-402")
            self.assertEqual(decision["verdict"], "block")
            self.assertIn("historical_policy_ineligible", decision["reasons"])

    def test_daily_authority_blocks_when_artifact_not_current(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            articles_dir = Path(tmpdir) / "articles"
            daily_dir = Path(tmpdir) / "daily"
            article_root = write_article(articles_dir, "art-test-403", artifact_published=False)
            write_validation(article_root, overall_status="pass")
            write_policy(article_root)
            with patch.object(common, "ARTICLES_DIR", articles_dir), patch.object(common, "DAILY_DIR", daily_dir), patch.object(publication_authority, "ARTICLES_DIR", articles_dir), patch.object(publication_authority, "DAILY_DIR", daily_dir):
                decision = publication_authority.evaluate_daily_publication_authority(
                    replay_date="2026-04-04",
                    article_ids=["art-test-403"],
                    conclave_verdict="pass",
                )
            self.assertEqual(decision["verdict"], "block")
            self.assertIn("artifact_publication_not_current:art-test-403", decision["reasons"])

    def test_daily_authority_passes_when_articles_and_conclave_pass(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            articles_dir = Path(tmpdir) / "articles"
            daily_dir = Path(tmpdir) / "daily"
            article_root = write_article(articles_dir, "art-test-404")
            write_validation(article_root, overall_status="pass")
            write_policy(article_root)
            with patch.object(common, "ARTICLES_DIR", articles_dir), patch.object(common, "DAILY_DIR", daily_dir), patch.object(publication_authority, "ARTICLES_DIR", articles_dir), patch.object(publication_authority, "DAILY_DIR", daily_dir):
                decision = publication_authority.evaluate_daily_publication_authority(
                    replay_date="2026-04-04",
                    article_ids=["art-test-404"],
                    conclave_verdict="pass",
                )
            self.assertEqual(decision["verdict"], "pass")
            self.assertEqual(decision["reasons"], [])


if __name__ == "__main__":
    unittest.main()
