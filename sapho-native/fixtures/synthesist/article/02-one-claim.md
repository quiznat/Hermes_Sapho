---
version: eval-fixture.v1
persona: synthesist
job: article
role: synthesist
expect:
  claim_count: 1
expect_contains:
- '### file: article.md'
- '### file: claim-01.md'
expect_block_count: 2
---
# Fixture

- article_id: fixture-sa-02
- source_url: https://example.org/sa-02
- source_title: Article Synth Fixture 02
- queued_at_utc: 2026-03-23T00:00:00Z
- captured_at_utc: 2026-03-23T00:05:00Z
- evidence_count: 1

Evidence files:

## evidence-01.md

This evidence states that a measured result changed materially.
