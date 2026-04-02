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
import article_job_runtime
from article_job_runtime import JobContractError, apply_claim_links, evidence_files_to_fact_lines, evidence_files_to_records, parse_evidence_receipt_files
from structured_artifact_bundle import materialize_article_structured_bundle


EXTRACTOR_RECEIPT = """---
version: extractor-receipt.v1
role: Extractor
article_id: art-test-101
evidence_count: 2
completed_at_utc: '2026-03-31T00:00:00Z'
---
# Extractor Receipt

## Summary

The source contains one method statement and one bounded result statement.

## Evidence Files

### file: evidence-01.md
```markdown
---
version: evidence.v1
article_id: art-test-101
evidence_id: evidence-001
kind: method
citation: Source method section
source_url: https://example.com/source
confidence: high
mechanism_relevance: direct
contradiction_relevance: none
---
The workflow stages retrieval before generation.

## Source Excerpt

The paper says retrieval is performed before generation.

## Note

This is a direct workflow description.
```

### file: evidence-02.md
```markdown
---
version: evidence.v1
article_id: art-test-101
evidence_id: evidence-002
kind: result
citation: Source results section
source_url: https://example.com/source
confidence: medium
mechanism_relevance: bounded
contradiction_relevance: tension
---
The reported reliability gain is bounded because the excerpt omits the full benchmark appendix.

## Source Excerpt

The source reports higher reliability but the appendix is not present in the excerpt.

## Note

Mechanism remains uncertain and the benchmark details are partial.
```
"""

EXTRACTOR_RECEIPT_MISSING_RELEVANCE = """---
version: extractor-receipt.v1
role: Extractor
article_id: art-test-102
evidence_count: 1
completed_at_utc: '2026-03-31T00:00:00Z'
---
# Extractor Receipt

## Summary

The source contains one evidence statement.

## Evidence Files

### file: evidence-01.md
```markdown
---
version: evidence.v1
article_id: art-test-102
evidence_id: evidence-001
kind: method
citation: Source method section
source_url: https://example.com/source
confidence: high
---
The workflow stages retrieval before generation.

## Source Excerpt

The paper says retrieval is performed before generation.

## Note

Direct workflow description.
```
"""

EXTRACTOR_RECEIPT_BOUNDED_WITHOUT_NOTE = """---
version: extractor-receipt.v1
role: Extractor
article_id: art-test-103
evidence_count: 1
completed_at_utc: '2026-03-31T00:00:00Z'
---
# Extractor Receipt

## Summary

The source contains one bounded evidence statement.

## Evidence Files

### file: evidence-01.md
```markdown
---
version: evidence.v1
article_id: art-test-103
evidence_id: evidence-001
kind: result
citation: Source results section
source_url: https://example.com/source
confidence: medium
mechanism_relevance: bounded
contradiction_relevance: tension
---
The reported reliability gain is bounded because the appendix is absent.

## Source Excerpt

The source reports higher reliability but omits the appendix.
```
"""

MALFORMED_CLAIMS_YAML = """article_id: art-test-106
summary: Context files changed behavior more than outcomes.
claims:
  - claim_id: claim-001
    claim_text: Developer-written context files improved performance by about 4% on average.
    claim_kind: empirical_claim
    evidence_ids:
      - evidence-001
    mechanism_or_bounds: A bounded mechanism is supported: context files increased exploration but did not guarantee better outcomes.
    contradiction_note: No direct contradiction is visible: the main tension is weak payoff despite higher overhead.
    confidence: high
"""


class ArticleJobRuntimeTests(unittest.TestCase):
    def read_json(self, path: Path) -> dict:
        return json.loads(path.read_text(encoding="utf-8"))

    def read_jsonl(self, path: Path) -> list[dict]:
        text = path.read_text(encoding="utf-8")
        if not text.strip():
            return []
        return [json.loads(line) for line in text.splitlines() if line.strip()]

    def test_parse_extractor_receipt_and_materialize_with_explicit_claims(self) -> None:
        evidence_files = parse_evidence_receipt_files("art-test-101", EXTRACTOR_RECEIPT)
        self.assertEqual(len(evidence_files), 2)
        self.assertEqual(evidence_files_to_fact_lines(evidence_files)[0], "The workflow stages retrieval before generation.")

        evidence_records = evidence_files_to_records("art-test-101", evidence_files)
        claims, linked_evidence = apply_claim_links(
            [
                {
                    "claim_id": "claim-001",
                    "article_id": "art-test-101",
                    "claim_text": "The workflow improves reliability through staged retrieval and validation.",
                    "claim_kind": "mechanism_claim",
                    "supporting_fact_ids": [],
                    "supporting_evidence_ids": ["evidence-001", "evidence-002"],
                    "source_span_refs": [
                        "articles/art-test-101/source.md#evidence-001",
                        "articles/art-test-101/source.md#evidence-002",
                    ],
                    "caveats": ["Benchmark appendix is not present in the excerpt."],
                    "confidence": "medium",
                    "mechanism_or_bounds": "The staged workflow may improve reliability by constraining generation with retrieval first, but the benchmark appendix is missing.",
                    "contradiction_note": "No direct contradiction is visible, but the evidence remains bounded by the partial excerpt.",
                }
            ],
            evidence_records,
        )

        article_body = """# Example Article

## Core Thesis

The workflow may improve reliability through staged retrieval and validation.

## Why It Matters

This keeps mechanism and bounds visible rather than smoothing them away.

## Key Findings

- The workflow stages retrieval before generation.

## Evidence Base

- The source describes a staged workflow and a bounded reliability result.

## Limits

The benchmark appendix is missing, so the mechanism and effect size remain bounded.
"""

        with tempfile.TemporaryDirectory() as tmpdir:
            with patch.object(common, "ARTICLES_DIR", Path(tmpdir)):
                result = materialize_article_structured_bundle(
                    article_id="art-test-101",
                    article_meta={
                        "article_id": "art-test-101",
                        "publication_status": "ready-for-daily",
                        "curator_mode": "agent",
                    },
                    article_body=article_body,
                    worthiness_text="KEEP\n\nInstitute-worthy bounded result.\n\nLimits: appendix is missing.",
                    findings_text="- The workflow may improve reliability through staged retrieval and validation.\n",
                    facts_text="- The workflow stages retrieval before generation.\n- The reported reliability gain is bounded because the excerpt omits the full benchmark appendix.\n",
                    claims_records=claims,
                    evidence_records=linked_evidence,
                )

                self.assertEqual(result["claim_count"], 1)
                self.assertEqual(result["evidence_count"], 2)

                article_root = Path(tmpdir) / "art-test-101"
                saved_claims = self.read_jsonl(article_root / "claims.jsonl")
                saved_evidence = self.read_jsonl(article_root / "evidence.jsonl")
                validation = self.read_json(article_root / "validation.json")

                self.assertEqual(saved_claims[0]["supporting_evidence_ids"], ["evidence-001", "evidence-002"])
                self.assertEqual(saved_evidence[0]["supports_claim_ids"], ["claim-001"])
                self.assertEqual(validation["checks"]["citation_linkage"]["status"], "pass")
                self.assertEqual(validation["checks"]["contradiction_baseline"]["status"], "fail")

    def test_parse_extractor_receipt_requires_relevance_fields(self) -> None:
        with self.assertRaises(JobContractError) as ctx:
            parse_evidence_receipt_files("art-test-102", EXTRACTOR_RECEIPT_MISSING_RELEVANCE)
        self.assertEqual(str(ctx.exception), "missing_evidence_relevance_fields")

    def test_article_write_requires_dense_decision_sections(self) -> None:
        thin_article = """# Thin Article

## Core Thesis

A study evaluates context files.

## Why It Matters

This matters for coding agents.

## Key Findings

- The study looks at success rate and cost.

## Evidence Base

- The source contains experiments.

## Limits

The paper may contain more detail.
"""
        claims = [
            {
                "claim_id": "claim-001",
                "article_id": "art-test-104",
                "claim_text": "Developer-written context files improve performance by about 4% on average while LLM-generated context files reduce it by about 3% on average.",
                "claim_kind": "empirical_claim",
                "supporting_fact_ids": [],
                "supporting_evidence_ids": ["evidence-001", "evidence-002"],
                "source_span_refs": ["articles/art-test-104/source.md#evidence-001"],
                "caveats": [],
                "confidence": "high",
                "mechanism_or_bounds": "Broader exploration and unnecessary requirements may make tasks harder and more expensive.",
                "contradiction_note": "No direct contradiction is visible, but benefits differ between developer-written and LLM-generated context files.",
            }
        ]
        evidence_records = [
            {
                "evidence_id": "evidence-001",
                "article_id": "art-test-104",
                "evidence_type": "result",
                "evidence_text": "Developer-provided context files improve performance by about 4% on average.",
                "source_span_ref": "articles/art-test-104/source.md#evidence-001",
                "supports_claim_ids": ["claim-001"],
                "confidence": "high",
                "mechanism_relevance": "bounded",
                "contradiction_relevance": "tension",
                "note": "Benefits are marginal rather than transformative.",
            },
            {
                "evidence_id": "evidence-002",
                "article_id": "art-test-104",
                "evidence_type": "result",
                "evidence_text": "LLM-generated context files reduce performance by about 3% on average and increase inference cost by over 20%.",
                "source_span_ref": "articles/art-test-104/source.md#evidence-002",
                "supports_claim_ids": ["claim-001"],
                "confidence": "high",
                "mechanism_relevance": "bounded",
                "contradiction_relevance": "tension",
                "note": "Costs rise while performance falls.",
            },
        ]
        with self.assertRaises(JobContractError) as ctx:
            article_job_runtime.validate_article_write_body(thin_article, claims=claims, evidence_records=evidence_records)
        self.assertEqual(str(ctx.exception), "article_write_missing_dense_sections")

    def test_article_write_rejects_empirically_thin_article_when_evidence_has_numbers(self) -> None:
        thin_but_sectioned_article = """# Context Files and Coding Agents

## Core Thesis

Context files may affect coding-agent performance.

## Why It Matters for Sapho

Sapho needs to know whether context engineering actually helps in production workflows.

## Key Findings

- Context files change coding-agent behavior.

## Evidence and Findings

- The source reports experimental comparisons across agents and models.

## Contradictions and Tensions

- Benefits are mixed and may depend on how the context file is produced.

## Mechanism or Bounds

- Extra requirements may change exploration behavior.

## Limits

- The benchmark setting may not transfer to every repository.
"""
        claims = [
            {
                "claim_id": "claim-001",
                "article_id": "art-test-105",
                "claim_text": "Developer-written context files improve performance by about 4% on average while LLM-generated context files reduce it by about 3% on average.",
                "claim_kind": "empirical_claim",
                "supporting_fact_ids": [],
                "supporting_evidence_ids": ["evidence-001", "evidence-002"],
                "source_span_refs": ["articles/art-test-105/source.md#evidence-001"],
                "caveats": [],
                "confidence": "high",
                "mechanism_or_bounds": "Broader exploration and unnecessary requirements may make tasks harder and more expensive.",
                "contradiction_note": "No direct contradiction is visible, but benefits differ between developer-written and LLM-generated context files.",
            }
        ]
        evidence_records = [
            {
                "evidence_id": "evidence-001",
                "article_id": "art-test-105",
                "evidence_type": "result",
                "evidence_text": "Developer-provided context files improve performance by about 4% on average.",
                "source_span_ref": "articles/art-test-105/source.md#evidence-001",
                "supports_claim_ids": ["claim-001"],
                "confidence": "high",
                "mechanism_relevance": "bounded",
                "contradiction_relevance": "tension",
                "note": "Benefits are marginal rather than transformative.",
            },
            {
                "evidence_id": "evidence-002",
                "article_id": "art-test-105",
                "evidence_type": "result",
                "evidence_text": "LLM-generated context files reduce performance by about 3% on average and increase inference cost by over 20%.",
                "source_span_ref": "articles/art-test-105/source.md#evidence-002",
                "supports_claim_ids": ["claim-001"],
                "confidence": "high",
                "mechanism_relevance": "bounded",
                "contradiction_relevance": "tension",
                "note": "Costs rise while performance falls.",
            },
        ]
        with self.assertRaises(JobContractError) as ctx:
            article_job_runtime.validate_article_write_body(thin_but_sectioned_article, claims=claims, evidence_records=evidence_records)
        self.assertEqual(str(ctx.exception), "article_write_missing_empirical_specificity")

    def test_parse_extractor_receipt_deduplicates_repeated_receipt_output(self) -> None:
        duplicated = EXTRACTOR_RECEIPT + "\n\n" + EXTRACTOR_RECEIPT
        evidence_files = parse_evidence_receipt_files("art-test-101", duplicated)
        self.assertEqual(len(evidence_files), 2)
        self.assertEqual([row["meta"]["evidence_id"] for row in evidence_files], ["evidence-001", "evidence-002"])

    def test_extract_last_article_document_prefers_final_complete_article(self) -> None:
        first = """---
version: article.v1
article_id: art-test-107
source_url: https://example.com/a
source_title: First Draft
queued_at_utc: 2026-04-02T00:00:00Z
captured_at_utc: 2026-04-02T00:00:00Z
curator_decision: kept
artifact_minted_at_utc: 2026-04-02T00:00:00Z
evidence_count: 1
claim_count: 1
publication_status: ready-for-daily
---
# First Draft

## Core Thesis

Thin.
"""
        second = """---
version: article.v1
article_id: art-test-107
source_url: https://example.com/a
source_title: Final Draft
queued_at_utc: 2026-04-02T00:00:00Z
captured_at_utc: 2026-04-02T00:00:00Z
curator_decision: kept
artifact_minted_at_utc: 2026-04-02T00:00:00Z
evidence_count: 2
claim_count: 2
publication_status: ready-for-daily
---
# Final Draft

## Core Thesis

Dense final output.
"""
        extracted = article_job_runtime.extract_last_article_document(first + "\n\n" + second)
        self.assertIn("# Final Draft", extracted)
        self.assertNotIn("# First Draft", extracted)

    def test_yaml_mapping_tolerates_unquoted_colons_in_scalar_values(self) -> None:
        payload = article_job_runtime._yaml_mapping(MALFORMED_CLAIMS_YAML)
        self.assertEqual(payload["article_id"], "art-test-106")
        self.assertEqual(payload["claims"][0]["claim_id"], "claim-001")
        self.assertIn("bounded mechanism is supported", payload["claims"][0]["mechanism_or_bounds"])

    def test_parse_extractor_receipt_requires_note_for_bounded_or_tension_evidence(self) -> None:
        with self.assertRaises(JobContractError) as ctx:
            parse_evidence_receipt_files("art-test-103", EXTRACTOR_RECEIPT_BOUNDED_WITHOUT_NOTE)
        self.assertEqual(str(ctx.exception), "bounded_or_tension_evidence_missing_note")


if __name__ == "__main__":
    unittest.main()
