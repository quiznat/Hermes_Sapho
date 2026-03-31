from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(ROOT))

from common import assert_unique_canonical_records, build_article_record, find_duplicate_canonical_pairs, find_kept_canonical_conflict


class CanonicalDuplicateTests(unittest.TestCase):
    def record(
        self,
        article_id: str,
        canonical_url: str,
        *,
        publication_status: str = "published",
        curator_decision: str = "kept",
        source_title: str = "",
        source_body: str = "",
        linked_paper_urls: list[str] | None = None,
    ) -> dict:
        return build_article_record(
            {
                "article_id": article_id,
                "source_url": canonical_url,
                "canonical_url": canonical_url,
                "publication_status": publication_status,
                "curator_decision": curator_decision,
                "source_title": source_title,
            },
            article_id=article_id,
            source_meta={
                "source_title": source_title,
                "linked_paper_urls": linked_paper_urls or [],
            },
            source_body=source_body,
        )

    def test_duplicate_pairs_match_arxiv_variants(self) -> None:
        records = [
            self.record("art-a", "https://arxiv.org/html/2505.02133v1"),
            self.record("art-b", "https://arxiv.org/pdf/2505.02133"),
        ]
        pairs = find_duplicate_canonical_pairs(records)
        self.assertEqual(len(pairs), 1)
        self.assertEqual(pairs[0]["signature"], "arxiv:2505.02133")

    def test_duplicate_pairs_match_shared_title_work_identity(self) -> None:
        records = [
            self.record(
                "art-blog",
                "https://example.ai/blog/measuring-coordination-in-agent-systems",
                source_title="Measuring Coordination in Agent Systems",
            ),
            self.record(
                "art-paper",
                "https://arxiv.org/abs/2603.12345",
                source_title="[2603.12345] Measuring Coordination in Agent Systems",
            ),
        ]
        pairs = find_duplicate_canonical_pairs(records)
        self.assertEqual(len(pairs), 1)
        self.assertEqual(pairs[0]["signature"], "work:title:measuring-coordination-in-agent-systems")

    def test_kept_conflict_ignores_discarded_articles(self) -> None:
        records = [
            self.record("art-discarded", "https://github.com/acme/demo", publication_status="discarded", curator_decision="discarded"),
            self.record("art-kept", "https://github.com/acme/demo", publication_status="published", curator_decision="kept"),
        ]
        conflict = find_kept_canonical_conflict(
            "https://github.com/acme/demo/blob/main/README.md",
            exclude_article_id="art-candidate",
            records=records,
        )
        self.assertIsNotNone(conflict)
        self.assertEqual(conflict["existing_article"]["article_id"], "art-kept")
        self.assertEqual(conflict["matched_signature"], "github:acme/demo")

    def test_kept_conflict_matches_explicit_linked_paper(self) -> None:
        records = [
            self.record(
                "art-paper",
                "https://openreview.net/forum?id=41xrZ3uGuI",
                publication_status="published",
                curator_decision="kept",
            ),
        ]
        conflict = find_kept_canonical_conflict(
            "https://example.ai/blog/coordination-results",
            exclude_article_id="art-blog",
            records=records,
            title="Coordination results",
            text="Read the paper at https://openreview.net/forum?id=41xrZ3uGuI for full details.",
        )
        self.assertIsNotNone(conflict)
        self.assertEqual(conflict["existing_article"]["article_id"], "art-paper")
        self.assertEqual(conflict["matched_signature"], "work:paper:openreview:41xrZ3uGuI")

    def test_assert_unique_records_raises_for_github_repo_variants(self) -> None:
        with self.assertRaisesRegex(ValueError, "duplicate_canonical_url:publication-proof:art-a:art-b:github:acme/demo"):
            assert_unique_canonical_records(
                [
                    self.record("art-a", "https://github.com/acme/demo"),
                    self.record("art-b", "https://github.com/acme/demo/tree/main"),
                ],
                context="publication-proof",
            )


if __name__ == "__main__":
    unittest.main()
