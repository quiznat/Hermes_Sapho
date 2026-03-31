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
from article_job_runtime import apply_claim_links, evidence_files_to_fact_lines, evidence_files_to_records, parse_evidence_receipt_files
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


if __name__ == "__main__":
    unittest.main()
