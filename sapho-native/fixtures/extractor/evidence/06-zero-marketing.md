---
version: eval-fixture.v1
persona: extractor
job: evidence
role: extractor
expect:
  evidence_count: 0
expect_contains:
- '# Extractor Receipt'
expect_block_count: 0
---
# Fixture

- article_id: fixture-ex-06
- source_url: https://example.org/ex-06
- source_title: Extractor Fixture 06

Captured source markdown:

The source is marketing copy with slogans and no experiment or operational detail.
