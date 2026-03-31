---
version: eval-fixture.v1
persona: synthesist
job: article
role: synthesist-article
expect:
  claim_count: 2
expect_contains:
- '### file: article.md'
- '### file: claim-01.md'
expect_block_count: 3
---
# Fixture

- article_id: fixture-sa-05
- source_url: https://example.org/sa-05
- source_title: Article Synth Fixture 05
- queued_at_utc: 2026-03-23T00:00:00Z
- captured_at_utc: 2026-03-23T00:05:00Z
- evidence_count: 2

Evidence files:

## evidence-01.md

This evidence states that a measured result changed materially.
## evidence-02.md

This evidence states a secondary measured result and caveat.
