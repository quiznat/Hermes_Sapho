# arXiv 2601.20404

## Core Thesis

In a paired study covering 10 repositories and 124 pull requests, the presence of repository-level AGENTS.md guidance was associated with faster agent completion and lower output-token use, but the paper supports an efficiency reading more strongly than a correctness reading because validation of output quality was limited.

## Why It Matters for Sapho

This matters because it strengthens the case that explicit local instructions can materially change agent operating efficiency inside real repositories, not just prompt aesthetics. For Sapho, that raises two practical implications: instruction surfaces deserve treatment as measurable infrastructure, and efficiency gains should not be accepted as operational wins unless they remain tied to visible bounds on task scope and output quality.

## Key Findings

- Across 124 paired pull-request tasks from 10 repositories, runs with AGENTS.md showed a statistically significant reduction in median wall-clock runtime under the paper's evaluation setup.
- Median wall-clock time fell from 98.57 seconds without AGENTS.md to 70.34 seconds with it, a reported reduction of 28.64%.
- Median output-token consumption fell from 2,925.00 tokens to 2,440.00 tokens, a reported reduction of 16.58%, and the paper marks that difference as statistically significant.
- The study design was heavily filtered before analysis: repositories were narrowed from 132 to 89 under a root-only instruction-file rule, then to 26 after content filtering and manual verification, with the final reported experiment using 10 repositories.
- The evaluated pull requests were restricted to merged code-changing tasks of at most 100 changed lines and no more than 5 modified files, which keeps the result tied to relatively small repository edits rather than broad software work.
- The paper did not run a full correctness or functional-equivalence evaluation; instead, it reports a manual sanity check on 50 randomly sampled tasks for non-empty, non-trivial outputs.

## Evidence and Findings

- The central empirical result is a paired comparison over 10 repositories and 124 pull requests showing lower median runtime when AGENTS.md is present: 98.57 seconds falls to 70.34 seconds, a 28.64% reduction, with a Wilcoxon signed-rank result reported at p < 0.05. That supports the claim that repository-specific agent instructions can change execution efficiency in measurable ways rather than only shaping style.
- The token result moves in the same direction: median output tokens drop from 2,925.00 to 2,440.00, or 16.58%, again reported as statistically significant at p < 0.05. That matters because the gain is not only faster completion but also lower generated-output volume, which suggests a more constrained or more directed interaction pattern.
- The dataset construction is itself part of the finding boundary. A root-only AGENTS.md constraint reduced the candidate repository set from 132 to 89, and further content-based filtering plus manual verification retained 26 qualifying repositories before the final experimental subset. This supports a careful reading: the result is about repositories with a particular instruction-file structure, not about all repositories that contain agent guidance anywhere.
- Task selection was narrow by design: only merged code-changing pull requests with at most 100 added-plus-deleted lines, no more than 5 modified files, and dates after AGENTS.md introduction were included. That matters because the measured gains are strongest as evidence for small, bounded maintenance-style tasks rather than complex multi-file engineering work.
- Some task statements were synthesized when pull requests lacked usable descriptions, using a local gpt-oss-120b model over the diff and pre-merge repository structure. This improves comparability across tasks, but it also means parts of the evaluation input were reconstructed rather than taken directly from human-authored task briefs.
- Quality validation was materially weaker than the efficiency measurement: the paper did not perform full correctness or functional-equivalence testing, relying instead on a manual sanity check over 50 randomly sampled tasks for non-empty, non-trivial outputs. That supports a bounded conclusion that AGENTS.md is associated with lower runtime and token use, while leaving open whether those savings always preserve solution quality.

## Contradictions and Tensions

The paper does not report a direct contradiction in the headline efficiency metrics; runtime and output-token results point in the same direction and are both marked statistically significant. The real tension is methodological rather than numeric: stronger evidence is provided for speed and output compression than for correctness. A second tension is that the study presents repository-guidance effects as operationally meaningful while evaluating only a filtered slice of small merged pull requests, making it unclear how far the benefit extends to harder or less standardized work.

## Mechanism or Bounds

The paper shows association, not a demonstrated causal mechanism. The best bounded explanation is that repository-level instructions may reduce search, hesitation, or unnecessary generation by giving the agent clearer local operating constraints, but the study does not isolate which properties of AGENTS.md produce the observed reductions. The result is further bounded by repository filtering, root-only instruction-file selection, small-task pull-request criteria, and partial reconstruction of task statements for PRs with weak descriptions.

## Limits

The study does not establish that faster and shorter outputs are functionally equivalent to slower or longer ones.
It is restricted to a filtered sample of repositories and small merged code-change tasks.
The repository-selection pipeline was substantial, so external generalization is limited.
Some task prompts were generated from pull-request materials rather than taken from original human instructions.
Mechanism remains uncertain: the paper measures outcome differences but does not identify which instruction features caused them.
Without full correctness evaluation, the evidence supports efficiency claims more strongly than reliability or quality claims.
