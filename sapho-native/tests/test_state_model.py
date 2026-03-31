from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(ROOT))

from common import (
    DUPLICATE_REJECTED_STATUS,
    article_artifact_publication_current,
    article_included_for_date_meta,
    article_is_terminal_for_selector,
    article_ready_for_pm_on_date,
    normalize_article_meta,
)


class StateModelTests(unittest.TestCase):
    def test_duplicate_terminal_state_strips_publication_fields(self) -> None:
        meta = normalize_article_meta(
            {
                "publication_status": DUPLICATE_REJECTED_STATUS,
                "artifact_minted_at_utc": "2026-03-28T10:00:00Z",
                "artifact_publication_status": "published",
                "artifact_publication_minted_at_utc": "2026-03-28T10:00:00Z",
                "artifact_publication_published_at_utc": "2026-03-28T10:05:00Z",
                "published_in_daily": "2026-03-28",
                "duplicate_of_article_id": "art-kept",
            }
        )
        self.assertNotIn("artifact_publication_status", meta)
        self.assertNotIn("artifact_publication_minted_at_utc", meta)
        self.assertNotIn("artifact_publication_published_at_utc", meta)
        self.assertNotIn("published_in_daily", meta)
        self.assertEqual(meta["duplicate_of_article_id"], "art-kept")

    def test_discarded_terminal_state_strips_duplicate_and_publication_fields(self) -> None:
        meta = normalize_article_meta(
            {
                "publication_status": "discarded",
                "published_in_daily": "2026-03-28",
                "duplicate_of_article_id": "art-other",
                "duplicate_match_signature": "work:demo",
            }
        )
        self.assertNotIn("published_in_daily", meta)
        self.assertNotIn("duplicate_of_article_id", meta)
        self.assertNotIn("duplicate_match_signature", meta)

    def test_ready_for_pm_requires_current_artifact_publication(self) -> None:
        not_published = {
            "publication_status": "ready-for-daily",
            "artifact_minted_at_utc": "2026-03-28T09:00:00Z",
        }
        published = {
            "publication_status": "ready-for-daily",
            "artifact_minted_at_utc": "2026-03-28T09:00:00Z",
            "artifact_publication_status": "published",
            "artifact_publication_minted_at_utc": "2026-03-28T09:00:00Z",
        }
        self.assertFalse(article_ready_for_pm_on_date(not_published, "2026-03-28"))
        self.assertTrue(article_artifact_publication_current(published))
        self.assertTrue(article_ready_for_pm_on_date(published, "2026-03-28"))

    def test_article_included_for_date_counts_ready_and_published(self) -> None:
        ready = {
            "publication_status": "ready-for-daily",
            "artifact_minted_at_utc": "2026-03-28T09:00:00Z",
        }
        published = {
            "publication_status": "published",
            "published_in_daily": "2026-03-28",
        }
        discarded = {
            "publication_status": "discarded",
            "artifact_minted_at_utc": "2026-03-28T09:00:00Z",
        }
        self.assertTrue(article_included_for_date_meta(ready, "2026-03-28"))
        self.assertTrue(article_included_for_date_meta(published, "2026-03-28"))
        self.assertFalse(article_included_for_date_meta(discarded, "2026-03-28"))

    def test_selector_terminal_statuses_are_closed(self) -> None:
        self.assertTrue(article_is_terminal_for_selector({"publication_status": "ready-for-daily"}))
        self.assertTrue(article_is_terminal_for_selector({"publication_status": "published"}))
        self.assertTrue(article_is_terminal_for_selector({"publication_status": "discarded"}))
        self.assertTrue(article_is_terminal_for_selector({"publication_status": DUPLICATE_REJECTED_STATUS}))
        self.assertFalse(article_is_terminal_for_selector({"publication_status": "pending"}))


if __name__ == "__main__":
    unittest.main()
