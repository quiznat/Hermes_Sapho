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

- article_id: fixture-ex-04
- source_url: https://example.org/ex-04
- source_title: Extractor Fixture 04

Captured source markdown:

The source states: Result one shows latency dropped 30%. Result two shows error rate dropped from 8% to 3%.
