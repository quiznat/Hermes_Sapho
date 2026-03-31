---
version: eval-fixture.v1
persona: extractor
job: evidence
role: extractor
expect:
  evidence_count: 2
expect_contains:
- '# Extractor Receipt'
- '### file: evidence-01.md'
expect_block_count: 2
---
# Fixture

- article_id: fixture-ex-03
- source_url: https://example.org/ex-03
- source_title: Extractor Fixture 03

Captured source markdown:

The source states: The system used retrieval reranking with an ablation showing a 12 point gain.
