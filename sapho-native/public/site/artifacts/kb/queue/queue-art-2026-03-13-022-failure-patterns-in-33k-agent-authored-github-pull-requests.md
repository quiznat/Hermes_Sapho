# Queue Item Processing — art-2026-03-13-022

## Source metadata
- URL: https://arxiv.org/abs/2601.15195v1
- Source type: firehose-brave
- Lane tags: `agent-factory, agent-factory`
- Curated at (UTC): 2026-03-13T06:02:22Z
- Finalized at (UTC): 2026-03-13T20:02:41Z

## Source custody
- Source snapshot: `research/evidence/source-material/2026-03-13/art-2026-03-13-022.json`
- Clean text path: `research/evidence/source-material/2026-03-13/art-2026-03-13-022.txt`

## Core thesis
Agentic pull request failure is driven by both technical quality signals, especially CI/test failures and larger code-change scope, and socio-technical workflow factors, notably reviewer abandonment and duplicate or misaligned PR submissions.

## Mechanism summary
The paper analyzes 33,596 agent-authored GitHub pull requests from five coding agents and compares merged versus not-merged PRs across task types, change size, CI outcomes, and review dynamics using effect sizes and logistic regression, then derives a hierarchical rejection taxonomy from a manually annotated rejected PR subset to capture failure reasons not visible in aggregate metrics. Reported results show 71.48% overall merge success with large variation by agent, higher merge rates for documentation, CI, and build tasks than for performance and fix tasks, lower merge odds as CI failures accumulate, larger scope for not-merged PRs, reviewer abandonment as the largest rejection category, and duplicates plus CI/test failures as the most concentrated concrete rejection modes.

## Why it matters for Sapho
This matters because it evaluates coding-agent reliability where it matters operationally: integration into real repository workflows rather than isolated code-generation benchmarks. Its significance is that successful deployment depends not only on whether an agent can produce plausible code, but also on task selection, scope control, CI stability, and compatibility with human review processes, which makes workflow design and validation policy central to real-world agent performance.

<!-- canonical-empirical-findings -->

## Empirical Findings (Data Snapshot)

| Novel finding | Quantitative result | Experimental setup/sample | Metric/outcome | Caveat/limit |
|---|---|---|---|---|
| Overall merge success is substantial but highly uneven across coding agents in real repositories. | From 33,596 PRs, 24,014 were merged (71.48%). Merge rates by agent: OpenAI Codex 82.59% (18,004/21,799), Cursor 65.22% (1,005/1,541), Claude Code 59.04% (271/459), Devin 53.76% (2,595/4,827), Copilot 43.04% (2,139/4,970). | Large-scale analysis of AIDev-pop PRs submitted by five coding agents across GitHub projects with more than 100 stars. | Acceptance outcomes differ strongly by agent even within the same dataset and workflow context. | Findings are observational and scoped to PRs contained in AIDev-pop and these five agents. |
| Task type strongly correlates with merge outcomes, with maintenance-oriented categories performing best. | Across agents, documentation 84%, CI 79%, and build 74% have the highest merge rates; performance 55% and fix 64% are the lowest overall. | RQ1 task-type analysis over 11 Conventional Commits categories (feature, fix, performance, refactoring, style, documentation, test, chore, build, CI, other). | Agentic PRs in documentation/CI/build are more likely to merge than performance/fix tasks. | Task labels come from dataset taxonomy and may not capture within-category complexity differences. |
| Not-merged PRs are associated with larger scope and worse CI outcomes than merged PRs. | Cliff’s delta indicates larger changes for not-merged PRs: LOC delta 17% (δ=-0.17), file-change delta 10% (δ=-0.10), CI-failure delta 24% (δ=-0.24). Logistic regression reports each additional failed CI check lowers merge odds by about 15% (odds ratio 85%). | Merged vs not-merged comparison across 33k+ PRs using effect sizes, kernel density distributions, and logistic regression. | CI failure burden and larger modification scope are practical negative signals for merge likelihood. | Review-comment and review-revision predictors showed small effects and non-significant p-values in the reported model. |
| Reviewer abandonment is the dominant rejection pattern in manually examined rejected agentic PRs. | In a 600-PR rejected sample, 38 became inaccessible, leaving 562 categorized; reviewer-level abandonment accounts for 228 PRs (38%), pull-request-level reasons 188 (31%), code-level reasons 133 (22%), and agentic-level issues 13 (2%). | Random stratified sample of 600 rejected PRs across five agents; manual qualitative coding with hierarchical taxonomy. | A large share of failures occurs before meaningful human review, indicating socio-technical workflow bottlenecks beyond code correctness. | Category frequencies are based on the accessible subset (562) after deletions/archival. |
| Among reviewed rejections, duplicates and CI/test failures are the largest concrete failure modes. | Duplicate PRs: 142 (23%); CI/test failure: 99 (17%); unwanted features: 24 (4%); incorrect implementation: 19 (3%); incomplete implementation: 15 (2%); non-functional PR: 13 (2%); misalignment: 9 (1%); license issues: 4 (<1%). | Hierarchical rejection taxonomy applied to the manually annotated rejected PR subset. | Rejection concentration in duplicates and CI/test failures suggests coordination and validation gaps in agentic contribution workflows. | These percentages are from qualitative coding categories and may depend on annotation definitions. |

## Confidence
high

Justification: The source is a primary arXiv study with a very large observational dataset, explicit quantitative comparisons, regression analysis, and qualitative rejection coding, so the evidence base is strong for workflow-level reliability conclusions. The main caveat is that the findings are observational and scoped to the sampled repositories and agents, which limits causal interpretation and generalization beyond this dataset.
