---
version: article.v1
article_id: art-2026-03-04-026
ticket_id: ticket-import-art-2026-03-04-026
source_url: https://arxiv.org/abs/2307.07924
source_title: 'ChatDev: Communicative Agents for Software Development'
queued_at_utc: '2026-03-04T03:59:01Z'
captured_at_utc: '2026-03-30T18:06:21Z'
canonical_url: https://arxiv.org/abs/2307.07924
curator_decision: kept
artifact_minted_at_utc: '2026-03-30T18:09:01Z'
evidence_count: 10
claim_count: 3
publication_status: published
imported_from_runtime_article_id: art-2026-03-04-026
imported_from_runtime_last_stage: facts
imported_from_runtime_filter_state: pending
curator_reason: 'This source introduces ChatDev, a novel framework for software development
  using communicative LLM agents. It details their approach to agent communication,
  phases of development, and mechanisms to mitigate coding hallucinations, presenting
  it as a paradigm shift in multi-agent collaboration. The abstract and introduction
  suggest experimental analysis and results, fulfilling the criteria for novel findings
  and potentially real experimental data.

  Limits: The provided excerpt is the abstract and introduction of a paper. While
  it strongly suggests experimental data and findings, the concrete results, benchmarks,
  or production data are not explicitly detailed within this specific excerpt. The
  full paper would need to be consulted to confirm the depth of experimental evidence.'
curated_at_utc: '2026-03-30T18:06:55Z'
curator_mode: agent
extracted_at_utc: '2026-03-30T18:09:01Z'
extractor_mode: agent
findings_mode: agent
summary_mode: agent
artifact_publication_status: published
artifact_publication_minted_at_utc: '2026-03-30T18:09:01Z'
artifact_publication_published_at_utc: '2026-03-30T18:09:02Z'
artifact_publication_alias: '20260304026'
source_remediation_status: completed
source_remediated_at_utc: '2026-03-30T18:06:21Z'
published_in_daily: '2026-03-30'
---
# ChatDev: Communicative Agents for Software Development

## Core Thesis

ChatDev demonstrates that software development can be automated through collaborative LLM agents assigned distinct social roles, structured communication protocols, and phased workflows—mitigating the hallucination risks that plague solo LLM coding tools.

## Why It Matters

This framework points toward a shift in how software gets built: from individual programmers or human teams to autonomous agent collectives that segment complex projects into manageable, verifiable steps.

## Key Findings

- Specialized LLM agents with assigned social roles collaborate autonomously across design, coding, and testing phases, with each phase broken into granular subtasks via a "chat chain" structure.
- "Communicative dehallucination" provides a mechanism to catch and reduce coding errors before they propagate.
- Natural language proves most effective for system design discussions, while programming language communication aids debugging and code-level verification.

## Limits

The cited material comes from an abstract and introduction only; specific benchmarks, quantitative results, and production deployment data are not detailed in the excerpt and would require examination of the full paper.
