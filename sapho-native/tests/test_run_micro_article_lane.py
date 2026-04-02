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
import run_micro_article_lane


class RunMicroArticleLaneTests(unittest.TestCase):
    def read_json(self, path: Path) -> dict:
        return json.loads(path.read_text(encoding="utf-8"))

    def read_jsonl(self, path: Path) -> list[dict]:
        text = path.read_text(encoding="utf-8")
        if not text.strip():
            return []
        return [json.loads(line) for line in text.splitlines() if line.strip()]

    def test_source_title_prefers_descriptive_source_title_over_arxiv_stub(self) -> None:
        title = run_micro_article_lane.source_title(
            {
                "source_title": "arXiv 2510.21413",
                "source_url": "https://arxiv.org/abs/2510.21413",
            },
            {
                "source_title": "Context Engineering for AI Agents in Open-Source Software",
                "source_url": "https://arxiv.org/html/2510.21413",
            },
        )
        self.assertEqual(title, "Context Engineering for AI Agents in Open-Source Software")

    def test_source_title_prefers_descriptive_title_from_source_body_when_meta_is_stub(self) -> None:
        source_body = """# Source Capture

## Title

arXiv 2510.21413

## Body

# arXiv 2510.21413

Source: https://arxiv.org/html/2510.21413v1

Context Engineering for AI Agents in Open-Source Software

## 1 Introduction
"""
        title = run_micro_article_lane.source_title(
            {
                "source_title": "arXiv 2510.21413",
                "source_url": "https://arxiv.org/abs/2510.21413",
            },
            {
                "source_title": "arXiv 2510.21413",
                "source_url": "https://arxiv.org/html/2510.21413",
            },
            source_body,
        )
        self.assertEqual(title, "Context Engineering for AI Agents in Open-Source Software")

    def test_source_title_prefers_bracketed_arxiv_title_over_stub(self) -> None:
        title = run_micro_article_lane.source_title(
            {
                "source_title": "arXiv 2602.11988",
                "source_url": "https://arxiv.org/abs/2602.11988",
            },
            {
                "source_title": "[2602.11988] Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?",
                "source_url": "https://arxiv.org/abs/2602.11988",
            },
        )
        self.assertEqual(title, "[2602.11988] Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?")

    def test_full_lane_materializes_charter_artifacts(self) -> None:
        article_id = "art-test-301"
        ticket_id = "ticket-test-301"

        def fake_curator(**_: object) -> dict:
            return {
                "raw": "",
                "meta": {
                    "role": "Curator",
                    "article_id": article_id,
                    "ticket_id": ticket_id,
                    "decision": "kept",
                    "reason": "Institute-worthy bounded workflow result.",
                },
                "body": "# Curator Receipt\n\n## Limits\n\nThe benchmark appendix is still partial.",
            }

        evidence_files = [
            {
                "filename": "evidence-01.md",
                "meta": {
                    "article_id": article_id,
                    "evidence_id": "evidence-001",
                    "kind": "method",
                    "citation": "Source method section",
                    "source_url": "https://example.com/post",
                    "confidence": "high",
                    "mechanism_relevance": "direct",
                    "contradiction_relevance": "none",
                },
                "body": "The workflow stages retrieval before generation.\n\n## Source Excerpt\n\nRetrieval is performed before generation.\n\n## Note\n\nDirect workflow description.",
                "statement": "The workflow stages retrieval before generation.",
                "source_excerpt": "Retrieval is performed before generation.",
                "note": "Direct workflow description.",
            },
            {
                "filename": "evidence-02.md",
                "meta": {
                    "article_id": article_id,
                    "evidence_id": "evidence-002",
                    "kind": "result",
                    "citation": "Source results section",
                    "source_url": "https://example.com/post",
                    "confidence": "medium",
                    "mechanism_relevance": "bounded",
                    "contradiction_relevance": "tension",
                },
                "body": "The reported reliability gain is bounded because the appendix is absent.\n\n## Source Excerpt\n\nThe source reports higher reliability but omits the appendix.\n\n## Note\n\nMechanism remains bounded by partial evidence.",
                "statement": "The reported reliability gain is bounded because the appendix is absent.",
                "source_excerpt": "The source reports higher reliability but omits the appendix.",
                "note": "Mechanism remains bounded by partial evidence.",
            },
        ]

        def fake_extractor(**_: object) -> dict:
            return {
                "raw": "",
                "meta": {
                    "role": "Extractor",
                    "article_id": article_id,
                    "evidence_count": 2,
                },
                "body": "# Extractor Receipt",
                "evidence_files": evidence_files,
            }

        def fake_claims(**_: object) -> dict:
            return {
                "summary": "One bounded mechanism claim is supported by two evidence records.",
                "claims": [
                    {
                        "claim_id": "claim-001",
                        "article_id": article_id,
                        "claim_text": "The workflow may improve reliability through staged retrieval and validation.",
                        "claim_kind": "mechanism_claim",
                        "supporting_fact_ids": [],
                        "supporting_evidence_ids": ["evidence-001", "evidence-002"],
                        "source_span_refs": [
                            f"articles/{article_id}/source.md#evidence-001",
                            f"articles/{article_id}/source.md#evidence-002",
                        ],
                        "caveats": ["The appendix is absent, so the gain remains bounded."],
                        "confidence": "medium",
                        "mechanism_or_bounds": "Reliability may improve because retrieval constrains generation first, but the appendix is missing.",
                        "contradiction_note": "Performance language must remain bounded by the missing appendix.",
                    }
                ],
            }

        def fake_article_write(**_: object) -> dict:
            body = """# Example Article

## Core Thesis

The workflow may improve reliability through staged retrieval and validation.

## Why It Matters

Sapho should keep mechanism and contradiction visibility explicit in the article package.

## Key Findings

- The workflow stages retrieval before generation.
- The reported reliability gain is bounded because the appendix is absent.

## Evidence Base

- Two evidence records support the claim, including a direct workflow description and a bounded result statement.

## Limits

The appendix is absent, so the reported gain remains bounded and should not be overstated.
"""
            return {"raw": "", "meta": {"article_id": article_id}, "body": body}

        def fake_contradiction_review(article_id: str, *_: object, **__: object) -> dict:
            article_root = common.article_dir(article_id)
            article_root.mkdir(parents=True, exist_ok=True)
            review = {
                "version": "contradiction-review.v1",
                "article_id": article_id,
                "reviewed_at_utc": "2026-03-31T00:20:00Z",
                "reviewer_role": "Extractor",
                "summary": "Strong performance language is visibly bounded by missing appendix evidence.",
                "review_confidence": "high",
                "contradiction_count": 1,
                "status": "disclosed",
            }
            rows = [
                {
                    "contradiction_id": "contradiction-001",
                    "article_id": article_id,
                    "contradiction_text": "Performance language is stronger than the available evidence basis.",
                    "related_claim_texts": ["The workflow may improve reliability through staged retrieval and validation."],
                    "related_fact_refs": ["fact-002"],
                    "disposition": "unresolved",
                    "disclosure": "Keep the missing appendix visible in the article limits.",
                    "confidence": "high",
                }
            ]
            (article_root / article_law_reviews.CONTRADICTION_REVIEW_FILE).write_text(json.dumps(review) + "\n", encoding="utf-8")
            (article_root / article_law_reviews.CONTRADICTIONS_FILE).write_text("\n".join(json.dumps(row) for row in rows) + "\n", encoding="utf-8")
            return {"review": review, "rows": rows}

        def fake_mechanism_review(article_id: str, *_: object, **__: object) -> dict:
            article_root = common.article_dir(article_id)
            article_root.mkdir(parents=True, exist_ok=True)
            review = {
                "version": "mechanism-review.v1",
                "article_id": article_id,
                "reviewed_at_utc": "2026-03-31T00:21:00Z",
                "reviewer_role": "Extractor",
                "summary": "The mechanism is present but explicitly bounded by missing appendix detail.",
                "review_confidence": "high",
                "mechanism_count": 1,
                "bounded_claim_count": 0,
                "status": "explained",
                "bounded_claims": [],
            }
            rows = [
                {
                    "mechanism_id": "mechanism-001",
                    "article_id": article_id,
                    "claim_text": "The workflow may improve reliability through staged retrieval and validation.",
                    "mechanism_text": "Retrieval constrains generation before validation, which may reduce context drift.",
                    "bounds": "The claimed gain remains bounded because the appendix is absent.",
                    "confidence": "high",
                }
            ]
            (article_root / article_law_reviews.MECHANISM_REVIEW_FILE).write_text(json.dumps(review) + "\n", encoding="utf-8")
            (article_root / article_law_reviews.MECHANISMS_FILE).write_text("\n".join(json.dumps(row) for row in rows) + "\n", encoding="utf-8")
            return {"review": review, "rows": rows}

        with tempfile.TemporaryDirectory() as tmpdir:
            articles_dir = Path(tmpdir) / "articles"
            queue_dir = Path(tmpdir) / "queue"
            with patch.object(common, "ARTICLES_DIR", articles_dir), patch.object(common, "QUEUE_DIR", queue_dir), patch.object(run_micro_article_lane, "run_curator_admission", side_effect=fake_curator), patch.object(run_micro_article_lane, "run_extractor_evidence", side_effect=fake_extractor), patch.object(run_micro_article_lane, "run_synthesist_claims", side_effect=fake_claims), patch.object(run_micro_article_lane, "run_synthesist_article_write", side_effect=fake_article_write), patch.object(run_micro_article_lane, "write_contradiction_review", side_effect=fake_contradiction_review), patch.object(run_micro_article_lane, "write_mechanism_review", side_effect=fake_mechanism_review):
                common.write_markdown(
                    common.article_file(article_id),
                    {
                        "version": "article.v1",
                        "article_id": article_id,
                        "ticket_id": ticket_id,
                        "source_url": "https://example.com/post",
                        "canonical_url": "https://example.com/post",
                        "queued_at_utc": "2026-03-31T00:00:00Z",
                        "publication_status": "queued",
                    },
                    "# Queued Article\n\nPending lane execution.\n",
                )
                common.write_markdown(
                    common.source_file(article_id),
                    {
                        "version": "source-capture.v1",
                        "article_id": article_id,
                        "ticket_id": ticket_id,
                        "source_url": "https://example.com/post",
                        "canonical_url": "https://example.com/post",
                        "source_title": "Example Source",
                        "capture_kind": "html",
                        "content_type": "text/html",
                        "captured_at_utc": "2026-03-31T00:05:00Z",
                    },
                    "# Source Capture\n\n## Title\n\nExample Source\n\n## Body\n\nThe workflow stages retrieval before generation. The source reports a bounded reliability gain but omits the appendix.\n",
                )
                common.write_markdown(
                    common.ticket_path(ticket_id),
                    {
                        "version": "ticket.v1",
                        "ticket_id": ticket_id,
                        "status": "queued",
                    },
                    "# Ticket\n\nQueue item for article lane testing.\n",
                )

                with patch.object(sys, "argv", ["run_micro_article_lane.py", "--article-id", article_id]):
                    result = run_micro_article_lane.main()
                self.assertEqual(result, 0)

                article_root = articles_dir / article_id
                article_meta, article_body = common.read_markdown(article_root / "article.md")
                self.assertEqual(article_meta["publication_status"], "ready-for-daily")
                self.assertEqual(article_meta["evidence_count"], 2)
                self.assertEqual(article_meta["claim_count"], 1)
                self.assertIn("## Core Thesis", article_body)

                self.assertTrue((article_root / "micro-worthiness.md").exists())
                self.assertTrue((article_root / "micro-facts.md").exists())
                self.assertTrue((article_root / "micro-findings.md").exists())
                self.assertTrue((article_root / "micro-summary.md").exists())
                self.assertTrue((article_root / "contradiction-review.json").exists())
                self.assertTrue((article_root / "mechanism-review.json").exists())

                evidence = self.read_jsonl(article_root / "evidence.jsonl")
                claims = self.read_jsonl(article_root / "claims.jsonl")
                validation = self.read_json(article_root / "validation.json")
                contradiction_review = self.read_json(article_root / "contradiction-review.json")
                mechanism_review = self.read_json(article_root / "mechanism-review.json")

                self.assertEqual(evidence[0]["mechanism_relevance"], "direct")
                self.assertEqual(evidence[1]["contradiction_relevance"], "tension")
                self.assertEqual(claims[0]["supporting_evidence_ids"], ["evidence-001", "evidence-002"])
                self.assertEqual(validation["overall_status"], "pass")
                self.assertEqual(validation["checks"]["contradiction_baseline"]["status"], "pass")
                self.assertEqual(validation["checks"]["mechanism_baseline"]["status"], "pass")
                self.assertEqual(contradiction_review["status"], "disclosed")
                self.assertEqual(mechanism_review["status"], "explained")


if __name__ == "__main__":
    unittest.main()
