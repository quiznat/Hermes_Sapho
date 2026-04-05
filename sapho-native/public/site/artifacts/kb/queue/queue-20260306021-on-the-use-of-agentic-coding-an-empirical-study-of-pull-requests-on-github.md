<details class="traceability-panel">
<summary>Traceability</summary>
<div class="traceability-body">
<ul>
  <li><strong>Source:</strong> <a href="https://arxiv.org/html/2509.14745v1" target="_blank" rel="noopener">https://arxiv.org/html/2509.14745v1</a></li>
  <li><strong>Intake queued:</strong> 2026-03-06T09:32:11Z</li>
  <li><strong>Source captured:</strong> 2026-04-05T04:12:16Z</li>
  <li><strong>Curated:</strong> 2026-04-05T04:12:32Z</li>
  <li><strong>Artifact finalized:</strong> 2026-04-05T04:14:55Z</li>
  <li><strong>Artifact published:</strong> 2026-04-05T13:13:58Z</li>
</ul>
</div>
</details>

# On the Use of Agentic Coding: An Empirical Study of Pull Requests on GitHub

## Core Thesis

In this matched study of GitHub pull requests explicitly labeled as generated with Claude Code, agentic coding produced a high merge rate but still underperformed matched human pull requests on acceptance: 475 of 567 agentic pull requests were merged, an 83.77425% acceptance rate, versus 91.00529% for the matched human set. The important result is not that agentic coding failed in open source, but that it cleared review often while still showing a statistically significant acceptance gap that the paper does not causally explain.

## Why It Matters for Sapho

This matters because it pushes Sapho toward a more disciplined view of coding agents: strong operational usefulness does not automatically imply parity with humans at the point of project acceptance. The evidence supports a doctrine of split evaluation. One layer is raw usefulness, where agentic systems clearly can land substantial work. The second is review conversion, where apparently capable output can still lose ground before merge for reasons that are only partly visible in review traces. Sapho should therefore treat agentic coding claims as acceptance-pipeline claims, not just code-generation claims, and should resist smooth narratives of either human replacement or obvious failure.

## Key Findings

- The analyzed matched dataset contains 567 Claude Code-generated pull requests across 157 open-source projects, of which 475 were merged, yielding an 83.77425% acceptance rate.
- Matched human pull requests were accepted at 91.00529%, so the agentic set trailed by roughly 7.23 percentage points, and the paper reports the difference as statistically significant.
- Among pull requests that did get merged, post-submission handling looked broadly similar: 54.94737% of merged agentic pull requests and 58.52713% of merged human pull requests were merged without revision, with no statistically significant difference.
- When revisions were needed before merge, both groups typically required a median of 2 revised commits, which weakens any simple claim that accepted agentic pull requests imposed dramatically heavier rework.
- The study identifies the dataset by searching GitHub pull request descriptions for the explicit string “Generated with Claude Code,” so the findings are about labeled usage rather than the full universe of agent-assisted coding.
- The retrieval pipeline began with 797 pull requests from repositories with at least 10 stars between February 24, 2025 and April 30, 2025, then excluded open items and later excluded 176 agentic pull requests that could not be matched to same-author human pull requests in a similar time frame.

## Evidence and Findings

- The paper shows that agentic coding was not a fringe phenomenon in this sample: 567 labeled pull requests across 157 projects survived into the matched analysis, and 475 of them were merged. That supports the conclusion that explicitly declared Claude Code usage can produce reviewable contributions that often land in real open-source repositories.
- The decisive comparative result is the acceptance gap: 83.77425% for the agentic set versus 91.00529% for matched human pull requests, with statistical significance reported by the authors. That supports a bounded conclusion of lower review conversion for the labeled agentic pull requests in this matched design, not a claim of general agentic inadequacy.
- The downstream review pattern among merged pull requests cuts against a simple “accepted but burdensome” story. Median time to merge was 1.23 hours for the agentic set versus 1.04 hours for humans, with no significant difference, and merge-without-revision rates were also not significantly different at 54.94737% versus 58.52713%. This matters because the observed disadvantage appears more concentrated at acceptance than in the visible revision burden for pull requests that do pass.
- Revision intensity among successful pull requests was also close in the reported summary: when revisions were required, both groups typically had a median of 2 revised commits before merge. That supports the narrower conclusion that accepted agentic pull requests were not obviously trapped in materially longer revision loops than accepted human pull requests.
- The dataset construction itself carries decision weight. Pull requests were found through the literal phrase “Generated with Claude Code,” limited to repositories with at least 10 stars and a narrow collection window, then further narrowed by matching constraints that removed 176 agentic pull requests lacking comparable same-author human baselines. This supports using the paper as evidence about explicit, labeled, matchable Claude Code usage rather than about all coding-agent activity on GitHub.
- The rejection record is only partially interpretable. Among rejected agentic pull requests, 12.1% lost because another solution landed first and 5.5% existed only to trigger automated verification rather than to merge, while 63.7% were closed without explanatory comments or discussion. That matters because some non-merge outcomes are clearly not clean code-quality failures, and most of the rejection pool lacks enough review trace to support a confident causal story.

## Contradictions and Tensions

- The central tension is that agentic pull requests were accepted less often, yet the ones that were merged did not show meaningfully slower merge times or heavier visible revision patterns than matched human pull requests. That blocks the easy interpretation that lower acceptance was simply the product of obviously worse accepted code.
- The rejection evidence is mixed in a way that weakens clean narratives. Some non-merges were procedural or contingent rather than direct failures of implementation quality, including cases where another solution arrived first and cases opened only to trigger verification workflows.
- At the same time, 63.7% of rejected agentic pull requests were closed without explanatory discussion, which means the paper exposes an outcome gap more clearly than it explains the reason for that gap.
- The manually classified sample suggests agentic pull requests skewed more toward refactoring and test-related changes, with refactoring at 24.9% versus 14.9% and test-related changes at 18.8% versus 4.5% for humans. That may signal a different task mix, which complicates direct quality interpretation of the acceptance gap.

## Mechanism or Bounds

The strongest supported explanation is bounded rather than causal. The paper shows a review-conversion gap for explicitly labeled Claude Code pull requests, but it does not establish whether the gap comes from code quality, task selection, reviewer trust, project norms, disclosure effects, or other submission-context factors. What the evidence does support is a two-stage operational picture: agentic systems can generate pull requests that are frequently good enough to merge, but the subset of labeled submissions still converts to acceptance less often than matched human submissions. Because the sample is built from pull requests explicitly marked “Generated with Claude Code,” drawn from repositories with at least 10 stars over a short 2025 window and then narrowed by same-author matching, the findings should be treated as descriptive for that labeled and filtered population only.

## Limits

The paper does not identify the causal driver of the acceptance gap.
Most rejected agentic pull requests lack explanatory review comments, leaving the major failure modes largely unobserved.
The evidence is bounded to explicitly labeled Claude Code usage and likely misses unlabeled or differently disclosed agent-assisted work.
The matched design improves comparability but excludes a substantial portion of the retrieved agentic set, including 176 pull requests that could not be paired to same-author human examples in a similar time frame.
The post-merge similarity results apply only to pull requests that were accepted, so they cannot erase the earlier acceptance disparity.
The classification results on refactoring and test-related work come from a manually classified sample rather than the full matched dataset, so they should inform interpretation but not carry more weight than the direct acceptance findings.
