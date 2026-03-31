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

- article_id: fixture-ex-09
- source_url: https://example.org/ex-09
- source_title: Extractor Fixture 09

Captured source markdown:

The source states: Trial A cut cost 18%. Trial B cut escalation rate 9%.
