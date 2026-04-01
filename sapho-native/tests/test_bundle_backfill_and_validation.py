from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(ROOT))

import backfill_structured_bundles
import common
import validate_article_bundles

ARTICLE_BODY = """---
version: article.v1
article_id: art-test-003
ticket_id: ticket-test-003
source_url: https://example.com/post
canonical_url: https://example.com/post
source_title: Example Source
queued_at_utc: '2026-03-31T00:00:00Z'
captured_at_utc: '2026-03-31T00:05:00Z'
curator_decision: kept
curated_at_utc: '2026-03-31T00:10:00Z'
artifact_minted_at_utc: '2026-03-31T00:15:00Z'
publication_status: ready-for-daily
evidence_count: 2
claim_count: 2
extractor_mode: agent
findings_mode: agent
summary_mode: agent
---
# Example Article

## Core Thesis

A structured workflow improves auditability.

## Why It Matters

It gives Sapho stronger lineage and clearer checks.

## Key Findings

- The workflow emits claims and evidence records.
- Validation surfaces gaps as explicit warnings.

## Limits

Contradiction and mechanism records are not explicit yet.
"""


class BundleBackfillAndValidationTests(unittest.TestCase):
    def test_backfill_and_validation_refresh(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            article_root = Path(tmpdir) / "art-test-003"
            article_root.mkdir(parents=True, exist_ok=True)
            (article_root / "article.md").write_text(ARTICLE_BODY, encoding="utf-8")
            (article_root / "micro-worthiness.md").write_text(
                "KEEP\n\nNovel synthesis with enough evidence.\n\nLimits: contradiction and mechanism records are not explicit yet.\n",
                encoding="utf-8",
            )
            (article_root / "micro-findings.md").write_text(
                "- The workflow emits claims and evidence records.\n- Validation surfaces gaps as explicit warnings.\n",
                encoding="utf-8",
            )
            (article_root / "micro-facts.md").write_text(
                "- The workflow emits claims and evidence records for each article package.\n- Validation surfaces contradiction and mechanism gaps as warnings.\n",
                encoding="utf-8",
            )

            with patch.object(common, "ARTICLES_DIR", Path(tmpdir)), patch.object(backfill_structured_bundles, "ARTICLES_DIR", Path(tmpdir)), patch.object(validate_article_bundles, "ARTICLES_DIR", Path(tmpdir)):
                result = backfill_structured_bundles.backfill_article("art-test-003")
                self.assertEqual(result["article_id"], "art-test-003")
                self.assertTrue((article_root / "validation.json").exists())

                validation_row = validate_article_bundles.validate_article("art-test-003", refresh=True)
                self.assertEqual(validation_row["article_id"], "art-test-003")
                self.assertEqual(validation_row["overall_status"], "fail")
                self.assertIn("contradiction_baseline", validation_row["fail_checks"])

                validation = json.loads((article_root / "validation.json").read_text(encoding="utf-8"))
                self.assertEqual(validation["checks"]["citation_linkage"]["status"], "pass")

                historical_policy = json.loads((article_root / "historical-policy.json").read_text(encoding="utf-8"))
                self.assertEqual(historical_policy["policy_status"], "not_applicable")
                self.assertFalse(historical_policy["applies"])


if __name__ == "__main__":
    unittest.main()
