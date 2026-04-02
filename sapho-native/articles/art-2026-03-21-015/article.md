---
version: article.v1
article_id: art-2026-03-21-015
ticket_id: ticket-import-art-2026-03-21-015
source_url: https://www.augmentcode.com/blog/1-open-source-agent-on-swe-bench-verified-by-combining-claude-3-7-and-o1
source_title: '#1 open-source agent on SWE-Bench Verified by combining Claude 3.7
  and O1 | Augment Code'
queued_at_utc: '2026-03-21T06:28:15Z'
captured_at_utc: '2026-03-21T22:52:56Z'
canonical_url: https://www.augmentcode.com/blog/1-open-source-agent-on-swe-bench-verified-by-combining-claude-3-7-and-o1
curator_decision: kept
artifact_minted_at_utc: '2026-03-24T01:48:11Z'
evidence_count: 8
claim_count: 3
publication_status: published
imported_from_runtime_article_id: art-2026-03-21-015
imported_from_runtime_last_stage: facts
imported_from_runtime_filter_state: pending
curator_reason: 'The source details a concrete achievement: reaching the #1 spot on
  the SWE-bench benchmark with a 65.4% success rate. It mentions specific models used
  (Claude Sonnet 3.7 and OpenAI''s o1) and provides a link to an open-sourced repository
  detailing their approach. This indicates substantive research and verifiable results
  in the agentic code benchmark space.

  The source is a blog post that focuses on a specific technical achievement and provides
  details on the methodology and open-sourced approach. It lacks extensive commentary
  or generic product marketing, making it valuable for understanding agent performance
  on code benchmarks.'
curated_at_utc: '2026-03-24T01:47:16Z'
curator_mode: agent
extracted_at_utc: '2026-03-24T01:48:11Z'
extractor_mode: agent
findings_mode: agent
summary_mode: agent
published_in_daily: '2026-03-24'
---
# Augment Code Hits #1 on SWE-Bench by Combining Claude 3.7 and O1

## Core Thesis

Augment Code has claimed the top spot on the SWE-bench Verified leaderboard with a 65.4% success rate, demonstrating that strategic model ensembling can outperform single-model approaches on complex software engineering benchmarks.

## Why It Matters

The SWE-bench benchmark tests an agent's ability to solve real GitHub issues autonomously. Achieving leading performance here signals genuine capability in production-grade code assistance, not just synthetic coding tasks. By open-sourcing their complete pipeline, Augment has made their methodology reproducible and auditable, raising the bar for transparency in competitive AI benchmarking.

## Key Findings

- **Ensemble beats monolith**: The approach combines Claude Sonnet 3.7 and OpenAI's o1, suggesting complementary strengths between different model architectures when attacking complex code problems.
- **End-to-end pipeline released**: The open-sourced implementation includes Dockerized agent runs, solution ensembling, and automated evaluation, providing a complete reference implementation for the research community.
- **Professional-grade focus**: Augment explicitly targets professional software engineering workflows, testing and tuning models across the full coding experience rather than optimizing for narrow benchmark subsets.

## Limits

The benchmark measures autonomous issue resolution on curated open-source repositories, which differs from the collaborative, context-rich environment of professional software teams. Real-world deployment involves constraints and workflows not captured in SWE-bench's controlled setting.
