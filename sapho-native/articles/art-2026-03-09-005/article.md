---
version: article.v1
article_id: art-2026-03-09-005
ticket_id: ticket-import-art-2026-03-09-005
source_url: https://arxiv.org/html/2601.17581
source_title: 'How AI Coding Agents Modify Code: A Large-Scale Study of GitHub Pull
  Requests'
queued_at_utc: '2026-03-09T10:00:08Z'
captured_at_utc: '2026-04-05T14:13:06Z'
canonical_url: https://arxiv.org/abs/2601.17581
curator_decision: kept
artifact_minted_at_utc: '2026-04-09T11:49:53Z'
evidence_count: 12
claim_count: 4
publication_status: ready-for-daily
imported_from_runtime_article_id: art-2026-03-09-005
imported_from_runtime_last_stage: facts
imported_from_runtime_filter_state: pending
source_remediation_status: completed
source_remediated_at_utc: '2026-04-05T14:13:06Z'
curator_reason: This is an empirical large-scale study of agentic versus human pull
  requests with concrete dataset sizes and measured results.
curated_at_utc: '2026-04-09T11:47:34Z'
curator_mode: agent
extracted_at_utc: '2026-04-09T11:49:53Z'
extractor_mode: agent
findings_mode: agent
summary_mode: agent
artifact_publication_alias: '20260309005'
artifact_publication_status: published
artifact_publication_minted_at_utc: '2026-04-09T11:49:53Z'
artifact_publication_published_at_utc: '2026-04-09T12:05:34Z'
---
# How AI Coding Agents Modify Code: A Large-Scale Study of GitHub Pull Requests

## Core Thesis

AI-agent pull requests are structurally different from human pull requests in ways that are large enough to matter operationally, and the clearest separator is commit count rather than raw changed-line volume. The study also finds a modest edge for agent pull requests on description-to-diff alignment, but that alignment result is narrower and more measurement-bounded than the structural differences.

## Why It Matters for Sapho

This shifts evaluation away from vague claims that coding agents merely "work differently" and toward a tighter doctrine: review systems should watch workflow shape, commit segmentation, and description-to-change coherence, not just total diff size. It also warns against treating apparent alignment gains as fully settled quality evidence, because some of the reported alignment signal is only relative and noisy. For Sapho, the useful update is that agentic code work appears distinguishable at scale, but the strongest evidence is about PR structure, not causal mechanism or end-to-end software quality.

## Key Findings

- Across the study's examined structural metrics, agent and human pull requests differed with p ≤ 0.001, indicating a consistent distributional separation rather than a one-off metric artifact.
- Commit count was the strongest reported separator, with Cliff's delta = 0.5429, a large effect and the biggest practical difference reported in the comparison.
- Files touched also differed materially, with Cliff's delta = 0.4487, while deleted lines showed a similarly substantial gap at 0.4462; by contrast, added lines (0.2836) and total line changes (0.3158) were only small-effect separators.
- The analysis was built on a large filtered sample: 24,014 agent pull requests with 440,295 commits with valid patches versus 5,081 human pull requests with 23,242 commits with valid patches.
- Agent pull requests showed slightly better description-to-diff alignment across all four reported alignment metrics, including higher median semantic similarity on CodeBERT (0.9375 vs 0.9347) and GraphCodeBERT (0.8302 vs 0.8067).
- The human comparison set was methodologically weaker at the commit level because commit metadata and file-level patches had to be reconstructed from the GitHub REST API rather than taken from an originally complete commit-level record.

## Evidence and Findings

- The paper's largest practical separation between agent and human pull requests is commit count, with Cliff's delta = 0.5429 and significance reported at p ≤ 0.001. That supports the conclusion that agentic work is not just a cosmetic variant of ordinary PR behavior; its workflow shape is materially different in a way reviewers and benchmarks should treat as first-order.
- Structural differences extend beyond commits. Files touched reached a medium effect size of 0.4487, and deleted lines reached 0.4462, while additions and total changed lines were weaker at 0.2836 and 0.3158. This supports a more specific conclusion: the strongest distinctions appear in edit organization and scope patterning, not simply in how many lines changed overall.
- The alignment results are directionally favorable to agents but modest. Agent pull requests had slightly higher central tendency on all four description-to-diff alignment measures, with semantic medians of 0.9375 versus 0.9347 on CodeBERT and 0.8302 versus 0.8067 on GraphCodeBERT. That supports the claim that agent-generated PR descriptions may track code changes somewhat better, but only by a limited margin.
- The scale of the filtered sample strengthens the comparison's relevance: 24,014 agent pull requests and 5,081 human pull requests survived filtering, with 440,295 and 23,242 valid-patch commits respectively. That gives the reported differences weight as large-sample observations rather than anecdotal cases, though it does not remove comparability limits.
- One important methodological bound sits inside the human baseline itself: because the human dataset lacked commit-level information, commit metadata and file-level patches were reconstructed through the GitHub REST API. This supports cautious interpretation of the comparison, because part of the baseline depends on reconstruction rather than directly preserved source records.

## Contradictions and Tensions

- The paper shows a strong structural separation, but that separation is uneven. Commit count is a large-effect discriminator, while additions and total line changes are only small-effect. That cuts against any simple reading that agents merely make "bigger" or "smaller" pull requests overall.
- Files touched and deleted lines show medium effects, yet the study interprets files touched as reflecting broader modification scope in human pull requests. The tension is that the comparison reveals difference clearly, but the operational meaning of that difference is not one-dimensional across all edit metrics.
- Description-to-diff alignment favors agents on every reported metric, but the gains are explicitly slight rather than decisive. That matters because a clean "agents document changes better" headline would overstate a result that is real but narrow.
- The BM25-based alignment family is especially unstable: scores are unbounded, highly variable, and treated by the authors only as a relative lexical signal. So the alignment story points in one direction, but one of its metric families is not a calibrated warrant for strong claims.

## Mechanism or Bounds

The strongest supported explanation is operational rather than causal: agent and human pull requests appear to be produced through different editing and packaging workflows, and those workflow differences show up most clearly in commit segmentation and PR structure. The evidence does not establish whether higher agent commit counts come from agent design, review habits, task selection, or dataset construction. Likewise, the modest alignment edge supports only a bounded claim that agent PR descriptions track their diffs somewhat better on the study's measures; it does not show that agents understand changes better or produce superior code quality. The results are comparative, large-sample, and statistically strong, but they remain observational and metric-bound.

## Limits

The study does not identify the causal source of the observed structural differences.
The human baseline required reconstruction of commit metadata and file-level patches, which is a real comparability constraint.
The sample includes only merged pull requests that survived filtering, so the results do not automatically generalize to all attempted agent or human code changes.
The alignment result is modest, and part of its measurement stack carries explicit uncertainty because BM25 is treated only as a relative lexical signal with extremely high variance.
Structural distinctness should not be read as proof of higher software quality, better review outcomes, or better engineering judgment.
