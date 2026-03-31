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

- article_id: fixture-ex-08
- source_url: https://example.org/ex-08
- source_title: Extractor Fixture 08

Captured source markdown:

The source states: We observed recurring timeout failures once queue depth exceeded 200 items.
