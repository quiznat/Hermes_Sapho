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

- article_id: fixture-ex-10
- source_url: https://example.org/ex-10
- source_title: Extractor Fixture 10

Captured source markdown:

The source is a generic roundup that mentions trends but contains no usable evidence unit.
