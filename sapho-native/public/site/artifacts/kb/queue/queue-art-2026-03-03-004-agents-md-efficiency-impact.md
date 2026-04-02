# Queue Artifact — art-2026-03-03-004

Source URL: https://arxiv.org/pdf/2601.20404  
Canonical URL: https://arxiv.org/abs/2601.20404  
Lane: agent-memory  
Decision: retain

## Thesis

This paper reports that AGENTS.md can improve **operational efficiency** for coding-agent runs, with lower median runtime and lower output-token usage in a paired with/without-file setup across sampled pull requests.

## Mechanism summary

The mechanism claim is configuration compression and guidance efficiency: a repository-level instruction file can reduce exploratory overhead by providing persistent project constraints and workflows up front. In the reported data (10 repositories, 124 PRs), this is associated with faster completion and lower token spend while maintaining comparable completion behavior.

## Confidence

Medium. This is a primary source with explicit quantitative deltas and study design framing, but sample size is modest and findings are in tension with other AGENTS.md studies in this queue, so generalization should be treated cautiously.

<!-- canonical-empirical-findings -->

## Empirical Findings (Data Snapshot)

| Novel finding | Quantitative result | Experimental setup/sample | Metric/outcome | Caveat/limit |
|---|---|---|---|---|
| AGENTS.md can improve execution efficiency without obvious completion collapse in this evaluated cohort. | Median runtime improvement **Δ28.64%** and output-token reduction **Δ16.58%** with AGENTS.md enabled. | 10 repositories, 124 GitHub pull requests; paired with-vs-without AGENTS.md runs for AI coding agents. | Wall-clock execution time and output token usage; completion behavior reported as comparable. | Small sample and context-specific repository mix; result conflicts with other AGENTS.md studies, so external validity is uncertain. |

## Why it matters for Sapho

This is valuable contrarian evidence against a blanket “AGENTS.md hurts outcomes” rule. For Sapho memory governance, the stronger policy is conditional: context manifests should be **minimal and operationally targeted**, then validated by task- and metric-specific experiments (success, latency, tokens), not adopted or rejected on ideology.
