---
version: article.v1
article_id: art-2026-03-04-036
ticket_id: ticket-import-art-2026-03-04-036
source_url: https://arxiv.org/abs/2602.08316
source_title: 'SWE Context Bench: A Benchmark for Context Learning in Coding'
queued_at_utc: '2026-03-04T04:07:37Z'
captured_at_utc: '2026-03-30T18:19:39Z'
canonical_url: https://arxiv.org/abs/2602.08316
curator_decision: kept
artifact_minted_at_utc: '2026-03-30T18:22:08Z'
evidence_count: 17
claim_count: 3
publication_status: published
imported_from_runtime_article_id: art-2026-03-04-036
imported_from_runtime_last_stage: facts
imported_from_runtime_filter_state: pending
curator_reason: 'This source presents a new benchmark (SWE-ContextBench) for evaluating
  experience reuse in programming agents. It details the benchmark''s design, methodology,
  and presents experimental results comparing different experience reuse strategies,
  including accuracy, time, and cost efficiency. This constitutes novel findings and
  a disciplined survey of a specific area within agent development.

  Limits: The provided excerpt is a partial snapshot of a larger work, and may not
  include all the nuances, limitations, or broader implications discussed in the full
  document. The abstract and introduction provide a good overview, but the full paper
  would offer more comprehensive details on the experimental setup and analysis.'
curated_at_utc: '2026-03-30T18:20:12Z'
curator_mode: agent
extracted_at_utc: '2026-03-30T18:22:08Z'
extractor_mode: agent
findings_mode: agent
summary_mode: agent
artifact_publication_alias: '20260304036'
artifact_publication_status: published
artifact_publication_minted_at_utc: '2026-03-30T18:22:08Z'
artifact_publication_published_at_utc: '2026-03-30T18:30:02Z'
source_remediation_status: completed
source_remediated_at_utc: '2026-03-30T18:19:39Z'
published_in_daily: '2026-03-30'
---
# SWE-ContextBench: Measuring Experience Reuse in Programming Agents

## Core Thesis

Programming agents can improve their performance by reusing prior solution experiences, but the effectiveness of this reuse depends heavily on context selection and summarization. SWE-ContextBench provides a structured evaluation framework that isolates and measures these effects across accuracy, time, and cost dimensions.

## Why It Matters

Experience reuse promises to make coding agents more efficient, yet unfiltered or poorly selected prior context can degrade rather than enhance performance. A rigorous benchmark that quantifies these trade-offs enables researchers to develop retrieval strategies that actually deliver on efficiency claims without compromising output quality.

## Key Findings

- SWE-ContextBench augments SWE-Bench Lite with 99 related tasks drawn from dependency and reference relationships, creating task sequences that share contextual grounding for testing experience transfer.
- Correctly selected and summarized experience measurably improves resolution accuracy while reducing both runtime and token costs, demonstrating that compact context can outperform full trajectory reuse.
- Unfiltered or incorrectly selected experience yields limited gains or active harm, indicating that context quality and relevance matter more than volume.

## Limits

This analysis reflects a partial snapshot of the work; full experimental protocols, broader agent comparisons, and detailed failure-mode analyses reside in the complete paper and are not captured here.
