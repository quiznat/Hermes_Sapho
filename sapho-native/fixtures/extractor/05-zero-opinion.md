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

- article_id: fixture-ex-05
- source_url: https://example.org/ex-05
- source_title: Extractor Fixture 05

Captured source markdown:

The source is broad opinion with no measurable result or direct evidence.
