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

- article_id: fixture-ex-02
- source_url: https://example.org/ex-02
- source_title: Extractor Fixture 02

Captured source markdown:

The source states: The outage lasted 43 minutes and was caused by stale cache invalidation.
