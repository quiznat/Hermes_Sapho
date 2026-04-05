---
version: article.v1
article_id: art-2026-03-10-069
ticket_id: ticket-import-art-2026-03-10-069
source_url: https://arxiv.org/abs/2601.00477
source_title: 'Security in the Age of AI Teammates: An Empirical Study of Agentic
  Pull Requests on GitHub'
queued_at_utc: '2026-03-10T20:39:42Z'
captured_at_utc: '2026-04-05T16:08:04Z'
canonical_url: https://arxiv.org/abs/2601.00477
curator_decision: kept
artifact_minted_at_utc: '2026-04-05T16:10:33Z'
evidence_count: 15
claim_count: 4
publication_status: ready-for-daily
imported_from_runtime_article_id: art-2026-03-10-069
imported_from_runtime_last_stage: facts
imported_from_runtime_filter_state: pending
source_remediation_status: completed
source_remediated_at_utc: '2026-04-05T16:08:04Z'
curator_reason: This is a serious empirical preprint reporting large-scale measured
  results on agent-authored security pull requests.
curated_at_utc: '2026-04-05T16:08:29Z'
curator_mode: agent
extracted_at_utc: '2026-04-05T16:10:33Z'
extractor_mode: agent
findings_mode: agent
summary_mode: agent
artifact_publication_alias: '20260310069'
artifact_publication_status: published
artifact_publication_minted_at_utc: '2026-04-05T16:10:33Z'
artifact_publication_published_at_utc: '2026-04-05T16:19:24Z'
---
# Security in the Age of AI Teammates: An Empirical Study of Agentic Pull Requests on GitHub

## Core Thesis

Security-relevant work is already a visible slice of agent-authored software change on GitHub, but the dominant pattern is not just direct bug repair. In this dataset, agents are frequently contributing broader security hardening work such as refactoring, testing, documentation, configuration, and error-handling improvements, while security-tagged changes also face materially slower and less merge-friendly review paths than non-security changes.

## Why It Matters for Sapho

This matters because it shifts the practical question from “can coding agents fix vulnerabilities” to “how are agents actually entering the security workflow, and where does trust break down.” The paper suggests that agentic security contribution is real but heterogeneous: some of the value comes through supportive hardening rather than headline vulnerability patches, and some of the friction appears tied less to explicit security labels than to reviewer reactions to complexity and verbose change descriptions. For Sapho, that is a doctrine-level reminder that evaluation should track review behavior, workload shape, and operational acceptance, not just nominal security intent.

## Key Findings

- In a curated dataset of 33,596 agent-authored pull requests, 1,293 were classified as security-related, yielding a prevalence rate of 3.85%.
- That 1,293 total came from 2,598 keyword-matched candidates that were then manually vetted, showing that roughly half of surface security matches did not survive closer classification.
- The coded action profile leans toward supportive hardening work: code refactoring appeared 957 times, testing 755 times, and documentation 692 times.
- The coded intent profile was mixed rather than narrowly exploit-fix oriented: functionality improvement appeared 890 times, while vulnerability mitigation appeared 741 times.
- Security-related pull requests merged less often than non-security pull requests, at 61.50% versus 77.33%.
- Security-related pull requests also moved much more slowly through review, with median review latency of 3.92 hours versus 0.11 hours for non-security pull requests.
- Early rejection was more strongly associated with textual signals of complexity and verbosity than with explicit security keywords, and text-based prediction outperformed structured-feature models.

## Evidence and Findings

- The paper studies 33,596 agent-authored pull requests from popular GitHub repositories and identifies 1,293 security-related cases, which supports the claim that security work is a real but minority share of current agent contribution rather than a dominant mode.
- The identification pipeline matters: 2,598 pull requests were first surfaced by keyword filtering, then reduced to 1,293 after manual vetting. That supports the prevalence estimate while also showing that keyword-level security signaling substantially overstates true security relevance.
- The article’s coding results show that agentic security work often takes a hardening form rather than only a patching form: refactoring was coded 957 times, testing 755 times, and documentation 692 times. That supports a broader view of how agents contribute to security posture in practice.
- Intent coding strengthens that interpretation but keeps it bounded. Functionality improvement appeared 890 times and vulnerability mitigation 741 times, which supports the claim that supportive work is common without justifying any claim that direct security remediation is rare or unimportant.
- Review outcomes diverged sharply from non-security work. Security-related pull requests merged at 61.50% versus 77.33% for non-security pull requests and had a median review latency of 3.92 hours versus 0.11 hours, supporting the conclusion that these changes receive more hesitant or burdensome review treatment.
- The rejection analysis suggests that review friction is not driven mainly by overt security wording. Early rejection tracked complexity and verbosity signals more strongly than explicit security keywords, and text-based models beat structured features, which matters because reviewer resistance may be responding to how difficult a change appears to parse rather than to security labeling alone.

## Contradictions and Tensions

- The paper’s own discovery pipeline contains an important tension: 2,598 pull requests looked security-related at the keyword stage, but only 1,293 remained after manual review. That gap means surface language around security is a noisy proxy for actual security substance.
- The “supportive hardening” pattern is real but not exclusive. Vulnerability mitigation still appeared 741 times, so the evidence does not support a simplistic claim that agentic security work is mostly documentation or cleanup.
- The cautious-review pattern is not uniform across contexts. Reported merge rates vary meaningfully by tool and language, with security pull requests from OpenAI Codex at 86.59% and Copilot at 49.60%, while TypeScript security pull requests showed a 56.51% merge rate and Rust the lowest merge rate in the top-language table at 51.16%.
- One agent-level sentence in the source appears numerically inconsistent with the curated subset totals, which weakens confidence in overinterpreting per-agent distribution details even though the higher-level dataset findings remain usable.

## Mechanism or Bounds

The strongest supported operational explanation is that agentic security work is entering repositories through a broad maintenance-and-hardening channel, not solely through explicit vulnerability repair, and that reviewers treat these changes as higher-friction when their text signals complexity, verbosity, or interpretive burden. The prevalence finding is bounded by a two-stage identification pipeline that began with keyword filtering on titles and descriptions, and pull requests without keyword matches were not manually reviewed, so some security-relevant work may have been missed. The review result is also bounded: latency is used as a proxy for scrutiny, not a direct measure of reviewer intent, so the paper supports a cautious-review interpretation without proving why reviewers behaved that way.

## Limits

The study is descriptive rather than causal. It shows prevalence, coding patterns, review outcomes, and rejection associations, but it does not establish why agents produced these categories of work, why reviewers slowed or rejected them, or whether the observed patterns generalize beyond the curated repositories and agent set studied here. The security-identification method may undercount security-relevant pull requests that lacked obvious keywords, and some agent-level reporting should be read cautiously because at least one sentence appears inconsistent with the dataset totals.
