---
version: eval-fixture.v1
persona: extractor
job: evidence
role: extractor
expect:
  evidence_count: 1
expect_contains:
- '# Extractor Receipt'
- '### file: evidence-01.md'
expect_block_count: 1
---
# Fixture

- article_id: fixture-ex-01
- source_url: https://example.org/ex-01
- source_title: Extractor Fixture 01

Captured source markdown:

The source states: The model improved benchmark accuracy from 61% to 74% on 120 tasks.
