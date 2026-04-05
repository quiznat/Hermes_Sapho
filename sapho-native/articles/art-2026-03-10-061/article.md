---
version: article.v1
article_id: art-2026-03-10-061
ticket_id: ticket-import-art-2026-03-10-061
source_url: https://www.arxiv.org/pdf/2601.18749
source_title: "Let\u2019s Make Every Pull Request Meaningful: An Empirical Analysis\
  \ of Developer and Agentic Pull Requests"
queued_at_utc: '2026-03-10T18:36:28Z'
captured_at_utc: '2026-04-05T16:04:21Z'
canonical_url: https://arxiv.org/abs/2601.18749
curator_decision: kept
artifact_minted_at_utc: '2026-04-05T16:07:11Z'
evidence_count: 15
claim_count: 4
publication_status: ready-for-daily
imported_from_runtime_article_id: art-2026-03-10-061
imported_from_runtime_last_stage: facts
imported_from_runtime_filter_state: pending
source_remediation_status: completed
source_remediated_at_utc: '2026-04-05T16:04:21Z'
curator_reason: Formal empirical software engineering paper with large-scale PR outcome
  analysis and concrete benchmark metrics.
curated_at_utc: '2026-04-05T16:04:36Z'
curator_mode: agent
extracted_at_utc: '2026-04-05T16:07:11Z'
extractor_mode: agent
findings_mode: agent
summary_mode: agent
artifact_publication_alias: '20260310061'
artifact_publication_status: published
artifact_publication_minted_at_utc: '2026-04-05T16:07:11Z'
artifact_publication_published_at_utc: '2026-04-05T16:19:24Z'
---
# Let’s Make Every Pull Request Meaningful: An Empirical Analysis of Developer and Agentic Pull Requests

## Core Thesis

Within this dataset, agentic pull requests were more predictable at merge time than human pull requests, and the strongest merge signal in both cases was not code shape but submitter position in the workflow. The paper’s central value is not a claim that agents are intrinsically easier to evaluate, but a narrower result: merge outcomes for agentic PRs appear strongly structured by governance and review context, and those patterns are not uniform across agent ecosystems.

## Why It Matters for Sapho

This matters because it pushes Sapho away from simple narratives about AI coding quality and toward a harder operational question: what institutions are actually approving when they merge agent-generated work. If merge probability is dominated by submitter-integrator alignment and if review signals flip direction between human and agentic PRs, then repository process may be carrying more explanatory weight than the underlying code artifact alone. For Sapho’s evaluation doctrine, that means agent performance claims should be treated as workflow-conditioned unless the evidence cleanly separates technical merit from governance structure, review burden, and tool-specific usage patterns.

## Key Findings

- The study analyzes 40,214 pull requests from the AIDev dataset, including 6,618 human-authored PRs and 33,596 agentic PRs, using logistic regression over 64 extracted features expanded to 106 model terms and reduced to 96 after multicollinearity filtering.
- The all-agentic merge model outperformed the human-PR model on this dataset, reaching AUC 0.960 versus 0.878, F1 0.923 versus 0.884, and Brier score 0.073 versus 0.119, indicating stronger predictive discrimination and calibration for agentic PR outcomes in the sampled repositories.
- Submitter attributes were the dominant feature family in both models, accounting for 69.00% of total LR chi-square in human PRs and 76.15% in agentic PRs.
- Contributor-integrator identity alignment was associated with extremely large increases in merge odds: about 219x for human PRs and 5,419x for agentic PRs when the contributor was also the integrator.
- The merged subsets also showed strong same-user concentration: 57.63% of merged human PRs and 77.51% of merged agentic PRs had contributor-integrator alignment, a difference that was statistically significant (z = -29.38, p < 0.001).
- Review-discussion signals split by authorship type: each additional reviewer comment was associated with a 2.7% increase in merge odds for human PRs but a 2.8% decrease for agentic PRs.
- Agent-specific patterns were heterogeneous rather than uniform: each additional commit was associated with 2.11x higher merge likelihood for Copilot PRs and 1.57x higher for Codex PRs, but about a 7% decrease in merge odds for Devin PRs.
- The cross-agent comparison was bounded by sample-size constraints that excluded Cursor and Claude Code from the RQ3 modeling stage, despite sample sizes of 1,541 and 459 PRs respectively.

## Evidence and Findings

- The paper shows that a logistic-regression approach can predict merge outcomes much more cleanly for agentic PRs than for human PRs in the sampled data, with agentic AUC at 0.960 versus 0.878 and Brier score at 0.073 versus 0.119. That supports a real discrimination gap in observed merge patterns, and it matters because it suggests agentic PR acceptance is governed by more regular and legible signals than the human baseline in this dataset.
- The strongest explanatory family in both model classes was submitter attributes, not code-change features, contributing 69.00% of LR chi-square in the human model and 76.15% in the agentic model. That supports the conclusion that who submits and how they sit inside repository workflow is central to merge outcomes, which matters because it weakens naive readings of merge rate as a direct quality proxy.
- The contributor-equals-integrator relationship was associated with very large merge-odds increases, roughly 219x for human PRs and 5,419x for agentic PRs, and merged agentic PRs showed same-user alignment in 77.51% of cases versus 57.63% for merged human PRs. This supports a governance-centered reading of the results, and it matters because agentic PR success may often reflect approval structure, ownership, or repository control rather than purely independent downstream validation.
- Review activity did not behave the same way across authorship types: each extra reviewer comment aligned with a 2.7% increase in merge odds for human PRs but a 2.8% decrease for agentic PRs, and agentic PRs with more than three reviewers were more common among unmerged cases than merged ones (5.8% versus 3.7%). That supports the conclusion that discussion load may signal friction more than reassurance in agentic workflows, which matters because “more review” cannot be treated as a uniformly positive quality signal.
- The agent-specific models show that the same feature can reverse meaning across ecosystems: more commits were positively associated with merge likelihood for Copilot and Codex PRs but negatively associated with merge odds for Devin PRs, while feature-family importance also shifted by agent. That supports a heterogeneous ecosystem view rather than a single “AI PR” pattern, and it matters because evaluation and governance claims about coding agents should be tool-specific when possible.
- The paper also states decisive bounds on interpretation: the models are correlational rather than causal, NULL merged_at collapses open and closed-unmerged states, and the AIDev dataset excludes repositories that ban AI-generated PRs. These constraints support only a bounded operational reading, and they matter because the reported merge dynamics are shaped by dataset selection and workflow structure rather than cleanly isolating technical merit.

## Contradictions and Tensions

- The cleanest tension is that review-discussion intensity appears mildly beneficial for human PRs but mildly adverse for agentic PRs. The same signal points in opposite directions, which cuts against any simple claim that more reviewer engagement universally improves merge prospects.
- The paper’s strongest associations point to repository role structure rather than to code-content quality. That creates an interpretive tension: the study is about “meaningful” pull requests, but the dominant merge predictors suggest institutional position and integration control may be carrying more weight than artifact-level evaluation.
- Agent-specific results resist flattening. Commit count tracks with higher merge likelihood for Copilot and Codex but lower merge odds for Devin, so aggregate claims about agentic PR behavior risk erasing tool-specific workflow differences.
- The agentic model is more predictive than the human model, but that does not cleanly imply that agentic PRs are better, easier, or more trustworthy. It may instead indicate that their acceptance pathways are more standardized, more role-concentrated, or more constrained by repository governance.
- The cross-agent comparison is explicitly incomplete because Cursor and Claude Code were excluded from the RQ3 modeling budget. That leaves a live tension between the paper’s heterogeneous-agent framing and the fact that two named agent ecosystems could not be modeled in that stage.

## Mechanism or Bounds

The strongest bounded explanation is workflow structuring, not demonstrated causal mechanism. Merge outcomes appear to be heavily organized by submitter role, contributor-integrator alignment, and review dynamics, with these institutional signals especially dominant in the agentic sample. A plausible operational reading is that PRs merge more often when the submitter also controls or closely aligns with integration authority, and that heavier discussion around agentic PRs more often marks friction, unresolved concerns, or exception handling rather than healthy validation. But the study does not establish that these factors cause merges. The regressions are correlational, the data are restricted to repositories already participating in AIDev, and the observed patterns are benchmark- and ecosystem-bound rather than universal.

## Limits

- The paper identifies correlations, not causal effects, so the results cannot tell us why submitter alignment or review activity changes merge odds.
- PRs with NULL merged_at combine open and closed-unmerged states, which can blur outcome interpretation.
- The AIDev dataset excludes repositories that prohibit AI-generated PRs, so the findings are drawn from an already AI-permitting slice of development practice.
- Agent-specific comparison is incomplete because Cursor and Claude Code were excluded from the RQ3 models for degrees-of-freedom reasons.
- Merge status is not a direct measure of code quality, safety, or downstream correctness, especially when governance structure is such a dominant predictor.
- The evidence supports heterogeneity across agent ecosystems, which means summary statements about “agentic PRs” remain vulnerable to overgeneralization if applied outside the sampled repositories and modeled agents.
