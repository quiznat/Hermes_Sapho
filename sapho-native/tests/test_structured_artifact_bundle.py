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
from structured_artifact_bundle import materialize_article_structured_bundle


class StructuredArtifactBundleTests(unittest.TestCase):
    def read_json(self, path: Path) -> dict:
        return json.loads(path.read_text(encoding="utf-8"))

    def read_jsonl(self, path: Path) -> list[dict]:
        text = path.read_text(encoding="utf-8")
        if not text.strip():
            return []
        return [json.loads(line) for line in text.splitlines() if line.strip()]

    def test_kept_bundle_writes_structured_internal_files(self) -> None:
        article_body = """# Example Article

## Core Thesis

A coordinated workflow improves code-assistant reliability.

## Why It Matters

Better context handling can make AI code assistants more trustworthy on large repositories.

## Key Findings

- The workflow combines retrieval, synthesis, and multi-agent execution.
- The system improves accuracy and reliability on real-world repositories.
- Benchmark comparisons show stronger project-context adherence than baseline approaches.

## Limits

The available excerpt does not include the paper's full experimental appendix.
"""
        worthiness_text = """KEEP

Novel synthesis with empirical grounding.

Limits: The excerpt is partial and should be checked against the full paper.
"""
        findings_text = """- The workflow combines retrieval, synthesis, and multi-agent execution.
- The system improves accuracy and reliability on real-world repositories.
- Benchmark comparisons show stronger project-context adherence than baseline approaches.
"""
        facts_text = """- The paper combines retrieval, NotebookLM synthesis, and multi-agent execution in one workflow.
- The system improves single-shot success rates by 12% on real-world repositories.
- Benchmark comparisons against baseline approaches show better adherence to project context.
"""

        with tempfile.TemporaryDirectory() as tmpdir:
            with patch.object(common, "ARTICLES_DIR", Path(tmpdir)):
                result = materialize_article_structured_bundle(
                    article_id="art-test-001",
                    article_meta={
                        "article_id": "art-test-001",
                        "publication_status": "ready-for-daily",
                        "curator_mode": "agent",
                    },
                    article_body=article_body,
                    worthiness_text=worthiness_text,
                    findings_text=findings_text,
                    facts_text=facts_text,
                )

                article_root = Path(tmpdir) / "art-test-001"
                self.assertTrue((article_root / "curator.json").exists())
                self.assertTrue((article_root / "findings.jsonl").exists())
                self.assertTrue((article_root / "facts.jsonl").exists())
                self.assertTrue((article_root / "claims.jsonl").exists())
                self.assertTrue((article_root / "evidence.jsonl").exists())
                self.assertTrue((article_root / "lineage.json").exists())
                self.assertTrue((article_root / "validation.json").exists())

                curator = self.read_json(article_root / "curator.json")
                findings = self.read_jsonl(article_root / "findings.jsonl")
                facts = self.read_jsonl(article_root / "facts.jsonl")
                claims = self.read_jsonl(article_root / "claims.jsonl")
                evidence = self.read_jsonl(article_root / "evidence.jsonl")
                lineage = self.read_json(article_root / "lineage.json")
                validation = self.read_json(article_root / "validation.json")

                self.assertEqual(curator["decision"], "kept")
                self.assertEqual(len(findings), 3)
                self.assertEqual(len(facts), 3)
                self.assertEqual(len(claims), 3)
                self.assertEqual(len(evidence), 3)
                self.assertEqual(result["claim_count"], 3)
                self.assertEqual(result["evidence_count"], 3)
                self.assertEqual(lineage["summary_sections"]["key_findings"], ["claim-001", "claim-002", "claim-003"])
                self.assertEqual(validation["checks"]["citation_linkage"]["status"], "pass")
                self.assertEqual(validation["checks"]["lineage_baseline"]["status"], "pass")
                self.assertEqual(validation["checks"]["contradiction_baseline"]["status"], "fail")
                self.assertEqual(validation["overall_status"], "fail")

    def test_discarded_bundle_still_writes_stable_empty_structures(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch.object(common, "ARTICLES_DIR", Path(tmpdir)):
                result = materialize_article_structured_bundle(
                    article_id="art-test-002",
                    article_meta={
                        "article_id": "art-test-002",
                        "publication_status": "discarded",
                        "curator_mode": "agent-fallback-discard",
                    },
                    article_body="# Discarded Article\n\nThis source was discarded by Curator.\n",
                    worthiness_text="DISCARD\n\nThe source is not sufficiently novel for the Daily rail.",
                )

                article_root = Path(tmpdir) / "art-test-002"
                curator = self.read_json(article_root / "curator.json")
                findings = self.read_jsonl(article_root / "findings.jsonl")
                facts = self.read_jsonl(article_root / "facts.jsonl")
                claims = self.read_jsonl(article_root / "claims.jsonl")
                evidence = self.read_jsonl(article_root / "evidence.jsonl")
                lineage = self.read_json(article_root / "lineage.json")
                validation = self.read_json(article_root / "validation.json")

                self.assertEqual(curator["decision"], "discarded")
                self.assertEqual(findings, [])
                self.assertEqual(facts, [])
                self.assertEqual(claims, [])
                self.assertEqual(evidence, [])
                self.assertEqual(lineage["claim_ids"], [])
                self.assertEqual(result["claim_count"], 0)
                self.assertEqual(result["evidence_count"], 0)
                self.assertEqual(validation["checks"]["completeness"]["status"], "pass")
                self.assertEqual(validation["overall_status"], "pass")

    def test_duplicate_rejected_bundle_records_duplicate_as_resolved_not_failed(self) -> None:
        article_body = """# Duplicate Rejected

This source passed worthiness but was blocked at the keep gate because the same work already exists in the institute.
"""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch.object(common, "ARTICLES_DIR", Path(tmpdir)), patch.object(article_law_reviews, "article_dir", lambda article_id: Path(tmpdir) / article_id):
                result = materialize_article_structured_bundle(
                    article_id="art-test-004",
                    article_meta={
                        "article_id": "art-test-004",
                        "publication_status": "duplicate-rejected",
                        "duplicate_of_article_id": "art-test-000",
                        "curator_mode": "agent",
                    },
                    article_body=article_body,
                    worthiness_text="KEEP\n\nNovel enough on its own, but duplicate of an existing kept package.",
                )

                article_root = Path(tmpdir) / "art-test-004"
                validation = self.read_json(article_root / "validation.json")

                self.assertEqual(result["validation_status"], "pass")
                self.assertEqual(validation["checks"]["duplicate_conflict"]["status"], "pass")
                self.assertEqual(validation["checks"]["duplicate_conflict"]["duplicate_of_article_id"], "art-test-000")

    def test_review_artifacts_make_eligible_package_pass_law_checks(self) -> None:
        article_body = """# Example Article

## Core Thesis

The system improves reliability through bounded retrieval and validation steps.

## Why It Matters

The article becomes eligible only when mechanism and contradiction law are explicit.

## Key Findings

- The workflow stages retrieval before generation.
- The system validates edits against project context.

## Limits

Contradictions were reviewed and no material unresolved conflict was found.
"""
        with tempfile.TemporaryDirectory() as tmpdir:
            def fake_article_dir(article_id: str) -> Path:
                return Path(tmpdir) / article_id

            with patch.object(common, "ARTICLES_DIR", Path(tmpdir)), patch.object(article_law_reviews, "article_dir", fake_article_dir):
                article_root = Path(tmpdir) / "art-test-005"
                article_root.mkdir(parents=True, exist_ok=True)
                (article_root / "contradiction-review.json").write_text(json.dumps({
                    "version": "contradiction-review.v1",
                    "article_id": "art-test-005",
                    "status": "clean",
                    "contradiction_count": 0
                }) + "\n", encoding="utf-8")
                (article_root / "mechanism-review.json").write_text(json.dumps({
                    "version": "mechanism-review.v1",
                    "article_id": "art-test-005",
                    "status": "explained",
                    "mechanism_count": 1,
                    "bounded_claim_count": 0
                }) + "\n", encoding="utf-8")

                result = materialize_article_structured_bundle(
                    article_id="art-test-005",
                    article_meta={
                        "article_id": "art-test-005",
                        "publication_status": "ready-for-daily",
                        "curator_mode": "agent",
                    },
                    article_body=article_body,
                    worthiness_text="KEEP\n\nNovel synthesis with explicit bounds.\n\nLimits: mechanism is bounded to the evidence provided.",
                    findings_text="- The workflow stages retrieval before generation.\n- The system validates edits against project context.\n",
                    facts_text="- The workflow stages retrieval before generation.\n- The system validates edits against project context.\n",
                )

                validation = self.read_json(article_root / "validation.json")
                self.assertEqual(result["validation_status"], "pass")
                self.assertEqual(validation["checks"]["contradiction_baseline"]["status"], "pass")
                self.assertEqual(validation["checks"]["mechanism_baseline"]["status"], "pass")


if __name__ == "__main__":
    unittest.main()
