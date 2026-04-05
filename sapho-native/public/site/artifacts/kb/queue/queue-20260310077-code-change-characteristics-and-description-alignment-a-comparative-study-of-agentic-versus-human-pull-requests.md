<details class="traceability-panel">
<summary>Traceability</summary>
<div class="traceability-body">
<ul>
  <li><strong>Source:</strong> <a href="https://arxiv.org/html/2601.17627v1" target="_blank" rel="noopener">https://arxiv.org/html/2601.17627v1</a></li>
  <li><strong>Intake queued:</strong> 2026-03-10T22:35:54Z</li>
  <li><strong>Source captured:</strong> 2026-04-05T16:11:16Z</li>
  <li><strong>Curated:</strong> 2026-04-05T16:11:32Z</li>
  <li><strong>Artifact finalized:</strong> 2026-04-05T16:13:46Z</li>
  <li><strong>Artifact published:</strong> 2026-04-05T16:19:25Z</li>
</ul>
</div>
</details>

# Code Change Characteristics and Description Alignment: A Comparative Study of Agentic versus Human Pull Requests

## Core Thesis

Across 33,596 agentic pull requests and 6,618 human pull requests, agentic software change work in this study looks structurally narrower and locally better described at the commit level, but it merges less often and the code it introduces is revised or removed sooner. The result is not that agentic pull requests are simply worse or better than human ones; it is that they appear easier to segment and narrate locally while remaining less robust at the decision and downstream maintenance layers that matter most.

## Why It Matters for Sapho

This matters because it cuts against a common shortcut in evaluating coding agents: tidy descriptions and smaller patches are not enough. Sapho should treat local legibility, merge success, and downstream code survival as separate evaluation surfaces. If agent systems produce changes that look well-packaged yet still merge less often and churn faster after introduction, then apparent composure at the artifact level can mask weaker end-to-end acceptance or durability.

## Key Findings

- Agentic pull requests merged at 76.80%, below the 82.82% merge rate for human pull requests.
- Agentic pull requests had smaller median footprints in commits, files changed, and directories changed, but not in lines changed, so the size difference is structural rather than universal.
- Each additional commit was associated with roughly a 5% reduction in merge odds, which makes the smaller multi-commit shape of agentic work relevant to interpretation even though it does not explain the merge gap by itself.
- On description quality, agentic pull requests beat human pull requests on commit-level alignment by both patch-message semantic similarity and an LLM-based consistency score.
- That advantage did not carry through to the pull-request level: PR-to-commit similarity was slightly worse for agentic pull requests, with median scores of 0.86 versus 0.88 for human pull requests.
- Files and symbols introduced by agentic pull requests were modified, revised, or removed at higher rates and sooner than those introduced by human pull requests.
- In the description-quality analysis, the evaluated sample was much smaller than the full dataset: 647 agentic pull requests and 571 human pull requests after English filtering.
- Within agentic pull requests, stronger descriptions were associated with longer textual scaffolding: commit messages of at least 13 words, PR titles of at least 7 words, and PR bodies of at least 80 words, with commit message length emerging as the strongest predictor and reaching a maximum SHAP value of 0.57.

## Evidence and Findings

- The study’s main comparison is large enough to matter operationally: 33,596 agentic pull requests from five coding agents are compared against 6,618 human pull requests. Within that corpus, the 76.80% versus 82.82% merge-rate split supports a real acceptance gap, which matters because adoption claims for coding agents often lean on output volume while underweighting whether maintainers actually take the work.
- Agentic pull requests are not merely “smaller” in a generic sense. Their median footprints are lower on commits, files changed, and directories changed, while lines changed do not show the same pattern. That supports a bounded conclusion that agent systems package work into narrower structural units, not that they universally reduce change magnitude.
- The merge analysis adds an important decision signal: each additional commit is associated with about a 5% drop in merge odds. That does not explain why agentic pull requests still merge less often despite their smaller commit footprints, but it shows that PR shape matters and that simple “smaller is better” stories are incomplete.
- Description quality splits across levels. Agentic pull requests perform better on commit-level alignment by both semantic-similarity and LLM-consistency measures, supporting the view that agents can generate locally matched commit narratives. But at the PR level the median similarity drops to 0.86 versus 0.88 for humans, which matters because maintainers review the whole PR, not only the local commit messages.
- The description-quality mechanism is partly visible but bounded. In the agentic subset, longer commit messages, titles, and bodies correlate with better measured description quality, and commit message length is the strongest predictor with a maximum SHAP value of 0.57. That supports an operational explanation that richer local textual scaffolding improves measured alignment, while leaving true factual adequacy unresolved.
- Downstream durability is weaker for agent-introduced code. Files added by agentic pull requests are modified later at higher rates and much sooner, and newly introduced symbols also churn more and are removed sooner. That matters because acceptance at merge time is not the end state; faster post-merge revision suggests that the introduced work is less stable, less well-targeted, or both.

## Contradictions and Tensions

- The central tension is that agentic pull requests look easier to package but still fare worse where it counts: they are structurally narrower, yet they merge less often.
- Description quality is not directionally consistent. Agents lead on commit-level alignment but trail slightly on PR-level alignment, so “agents write better change descriptions” is too broad a reading.
- The PR-level alignment gap is small, 0.86 versus 0.88, while the commit-level advantage is clearer. That makes the interpretation more subtle: agents may be good at describing isolated patches without being equally good at summarizing the full intent and coherence of a pull request.
- The downstream churn result complicates any optimistic reading of smaller PR shape. Smaller, more segmented changes do not translate here into more durable introduced files or symbols.
- Task mix may be part of the story without settling it. Agentic pull requests rank documentation and test work third and fourth, while human pull requests rank chore and build work there. That difference may affect footprint and churn patterns, but the study does not prove it as the causal driver.

## Mechanism or Bounds

The strongest bounded explanation is that agentic systems in this dataset are better at generating locally aligned patch descriptions than at producing globally coherent pull-request summaries, and that they tend to package work into narrower structural units. Longer commit messages, longer titles, and longer PR bodies are associated with better measured description quality, which supports a practical mechanism of improved alignment through richer textual context. But the merge-rate gap and the faster revision or removal of introduced files and symbols remain mechanistically unresolved. They could reflect lower initial quality, faster correction cycles, different task mixes, or differences in repository and reviewer interaction. The evidence is comparative and partially correlational, with proxy quality measures rather than direct truth checks.

## Limits

- The study does not identify a causal reason why agentic pull requests merge less often than human pull requests.
- The description-quality analysis is based on a filtered English subset of 647 agentic and 571 human pull requests, not the full comparison corpus.
- Reported description-quality measures are proxies and may miss factual correctness; the classifier recalled only 31.9% of good descriptions, which materially limits confidence in any strong claim about true writing quality.
- The smaller-footprint pattern does not hold across all size metrics, because it does not extend to lines changed.
- Higher downstream churn for agent-introduced files and symbols is clear in direction but ambiguous in meaning: it may indicate poorer initial quality, faster iteration, or task-distribution effects rather than a single defect mode.
- The agentic and human datasets come from different date windows, which does not invalidate the comparison but does limit how cleanly the differences can be attributed to authorship alone.
