from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(ROOT))

import article_law_reviews
import common


class ArticleLawReviewsTests(unittest.TestCase):
    def test_contradiction_review_prompt_carries_structured_claim_and_evidence_context(self) -> None:
        captured: dict[str, str] = {}

        def fake_run_loose_agent(agent_id: str, prompt: str, **_: object) -> str:
            captured["agent_id"] = agent_id
            captured["prompt"] = prompt
            return """summary: Bounded performance tension is visible.
review_confidence: high
contradictions:
  - contradiction_text: Performance language outruns the visible appendix support.
    related_claim_texts:
      - The workflow may improve reliability through staged retrieval and validation.
    related_fact_refs:
      - fact-002
    related_evidence_ids:
      - evidence-002
    disposition: unresolved
    disclosure: Keep the missing appendix visible.
    confidence: high
"""

        with tempfile.TemporaryDirectory() as tmpdir:
            with patch.object(common, "ARTICLES_DIR", Path(tmpdir)), patch.object(article_law_reviews, "article_dir", lambda article_id: Path(tmpdir) / article_id), patch.object(article_law_reviews, "run_loose_agent", side_effect=fake_run_loose_agent):
                result = article_law_reviews.write_contradiction_review(
                    "art-test-401",
                    {
                        "article_id": "art-test-401",
                        "source_title": "Example Source",
                        "source_url": "https://example.com/post",
                    },
                    "# Example Article\n\n## Core Thesis\n\nThe workflow may improve reliability through staged retrieval and validation.\n",
                    "- The workflow may improve reliability through staged retrieval and validation.\n",
                    "- The workflow stages retrieval before generation.\n- The reported reliability gain is bounded because the appendix is absent.\n",
                    claims_records=[
                        {
                            "claim_id": "claim-001",
                            "claim_text": "The workflow may improve reliability through staged retrieval and validation.",
                            "supporting_evidence_ids": ["evidence-001", "evidence-002"],
                            "mechanism_or_bounds": "Retrieval constrains generation first, but the appendix is absent.",
                            "contradiction_note": "Performance remains bounded by the missing appendix.",
                        }
                    ],
                    evidence_records=[
                        {
                            "evidence_id": "evidence-001",
                            "evidence_text": "The workflow stages retrieval before generation.",
                            "evidence_type": "method",
                            "mechanism_relevance": "direct",
                            "contradiction_relevance": "none",
                            "note": "Direct workflow description.",
                        },
                        {
                            "evidence_id": "evidence-002",
                            "evidence_text": "The reported reliability gain is bounded because the appendix is absent.",
                            "evidence_type": "result",
                            "mechanism_relevance": "bounded",
                            "contradiction_relevance": "tension",
                            "note": "The appendix is absent.",
                        },
                    ],
                )

                self.assertEqual(captured["agent_id"], "synthesist")
                self.assertIn("Claims:", captured["prompt"])
                self.assertIn("claim-001", captured["prompt"])
                self.assertIn("evidence-002", captured["prompt"])
                self.assertIn("contradiction_relevance=tension", captured["prompt"])
                self.assertIn("mechanism_relevance=bounded", captured["prompt"])
                self.assertEqual(result["rows"][0]["related_evidence_ids"], ["evidence-002"])

                saved = json.loads((Path(tmpdir) / "art-test-401" / "contradiction-review.json").read_text(encoding="utf-8"))
                self.assertEqual(saved["contradiction_count"], 1)


if __name__ == "__main__":
    unittest.main()
