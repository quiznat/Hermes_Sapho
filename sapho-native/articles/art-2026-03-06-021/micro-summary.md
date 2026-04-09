# On the Use of Agentic Coding: An Empirical Study of Pull Requests on GitHub

## Core Thesis

Explicitly labeled Claude Code pull requests were merged often in this sample of open-source repositories, but still less often than human pull requests. Once an agentic pull request cleared the acceptance threshold, its downstream revision pattern looked broadly similar to human submissions on the metrics the study measured. The evidence therefore supports a bounded view: agentic coding can produce mergeable work at meaningful scale, but acceptance remains selective and appears entangled with task mix, repository context, and review dynamics rather than showing simple parity with human contribution.

## Why It Matters for Sapho

This matters because it cuts against both easy optimism and easy dismissal. Sapho should not treat agentic coding as unfit for real repository workflows when 475 of 567 sampled pull requests were merged across 157 projects. But Sapho also should not collapse “often merged” into “human-equivalent,” because the acceptance gap remains material: 83.77425% for the sampled Claude Code pull requests versus 91.00529% for human pull requests. The practical doctrine update is to separate three questions that are often blurred together: whether agentic work gets accepted at all, whether accepted work requires unusually heavy repair, and what kinds of tasks agents are actually being used for. This paper says those are not the same question.

## Key Findings

- In the sampled repositories, 475 of 567 explicitly labeled Claude Code pull requests were merged, yielding an 83.77425% merge rate across 157 open-source projects.
- Human pull requests in the study were accepted more often than the Claude Code pull requests, 91.00529% versus 83.77425%, and the paper reports that this difference was statistically significant.
- Among merged submissions, acceptance without revision was similar: 54.94737% of merged Claude Code pull requests versus 58.52713% of human pull requests, with no statistically significant difference on that measure.
- When revisions were needed, the study found no statistically significant difference in revision frequency or measured revision cost between Claude Code and human pull requests.
- The task mix differed sharply: Claude Code pull requests were more concentrated in refactoring (24.9% versus 14.9%), documentation (22.1% versus 14.0%), and testing work (18.8% versus 4.5%).
- Claude Code submissions were much more often multi-purpose than human pull requests, 40.0% versus 12.2%, and also arrived with larger initial additions and far longer descriptions, with medians of 48 versus 24 added lines and 355 versus 56 words in pull request descriptions.

## Evidence and Findings

- The strongest adoption signal is simple scale with nontrivial success: 567 explicitly labeled Claude Code pull requests were identified across 157 repositories, and 475 were merged. That supports the conclusion that agentic coding was not confined to toy use in this sample; maintainers were regularly willing to merge the output into live open-source projects.
- The main cautionary comparison is the acceptance gap against human submissions: 83.77425% for the sampled Claude Code pull requests versus 91.00529% for human pull requests. The supported conclusion is not that agentic coding fails, but that it still encountered a meaningful acceptance penalty in this observed workflow.
- Post-submission handling among merged work looks more similar than the headline acceptance gap would suggest. Of merged Claude Code pull requests, 54.94737% went in without revision, close to the 58.52713% rate for human pull requests, and the study found no statistically significant difference in revision frequency or measured revision cost when revisions occurred. That matters because it narrows the likely problem surface: the biggest separation may be at the acceptance gate rather than in costly downstream repair of already-accepted work.
- The work profile was not neutral. Claude Code pull requests over-indexed toward refactoring, documentation, and tests, and were far more often multi-purpose, at 40.0% versus 12.2%. This supports the conclusion that the observed agentic contribution pattern was shaped by a distinct task mix, which complicates any naive one-number comparison with human pull requests.
- Initial agentic submissions were also packaged differently: median added lines were 48 versus 24 for human pull requests, and median description length was 355 words versus 56. That matters because review outcomes may reflect not only code content but submission form, scope, and the amount of reviewer interpretation the pull request demands.
- The rejection record is only partially legible. Among rejected Claude Code pull requests, explicit categories included alternative solutions already provided by others or the team (12.1%), verification-only submissions (5.5%), oversized pull requests (3.3%), and obsolete pull requests (3.3%), but 63.7% of rejected cases were closed without explanatory comments or discussion. The supported conclusion is that rejection is real and common enough to matter, while the causal story behind rejection remains substantially underobserved.

## Contradictions and Tensions

- The central tension is that agentic pull requests were accepted less often overall, yet among the ones that were merged, revision behavior looked similar to human pull requests. That cuts against the easy story that lower acceptance must simply reflect obviously inferior code requiring heavier clean-up.
- The task mix creates an interpretive tension. Claude Code pull requests were more concentrated in refactoring, documentation, testing, and multi-purpose changes, so the acceptance gap cannot be cleanly read as a like-for-like quality comparison across identical work types.
- Submission form may itself be part of the tension: agentic pull requests tended to add more lines and use much longer descriptions, while some explicit rejections cited oversized pull requests. That leaves open whether lower acceptance reflects code quality, scope packaging, reviewer burden, or all three together.
- The rejection-cause evidence is thin exactly where one would want explanatory clarity. With 63.7% of rejected agentic pull requests closed without explanation, the paper shows a robust outcome difference without providing equally robust visibility into why that difference occurred.
- The study captures explicitly labeled Claude Code pull requests shortly after the tool’s release, which creates a tension between real-world relevance and generality: the sample is concrete and valuable, but it may reflect early-adoption behavior rather than stable long-run norms for agentic coding.

## Mechanism or Bounds

The strongest supported operational explanation is not a causal mechanism but a bounded workflow account. In this sample, explicitly labeled Claude Code pull requests were entering normal open-source review pipelines and often clearing them, but they arrived with a different task profile and packaging profile than human pull requests. They were more likely to bundle multiple purposes, more concentrated in refactoring, documentation, and tests, and often presented with longer descriptions and somewhat larger initial additions. That combination plausibly changes how maintainers evaluate them at the acceptance boundary, even though accepted submissions did not show heavier measured revision burdens afterward. This remains a bounded interpretation rather than a proven mechanism, because the study is observational, the identification method depends on the “Generated with Claude Code” label in pull request descriptions, the repository pool was restricted to projects with at least 10 stars, and the sampled window ran only from February 24, 2025 to April 30, 2025.

## Limits

The study does not establish why the acceptance gap exists.
It covers only explicitly labeled Claude Code pull requests, not agentic coding in general or unlabeled AI-assisted work.
The observation window is short and begins at tool release, so maturation effects and changing maintainer norms are unresolved.
Most rejected agentic pull requests lacked explanatory feedback, which sharply limits causal inference about rejection drivers.
The measured revision-cost metrics are useful but narrow; similarity on commits, files changed, line edits, and code-modification percentage does not prove equivalence in code quality, maintainability, or long-run downstream impact.
Because task mix differs substantially between agentic and human pull requests, the comparison should not be treated as a clean apples-to-apples productivity or quality ranking.
