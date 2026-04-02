# Queue Artifact — art-2026-03-04-024

Source URL: https://arxiv.org/abs/2510.10460  
Canonical URL: https://arxiv.org/abs/2510.10460  
Lane: agent-research  
Decision: retain

## Thesis

Multi-agent code-generation systems can look strong on benchmark averages while still being brittle to semantically equivalent input perturbations, and a major causal failure point is a planner-coder information-loss gap.

## Mechanism summary

The paper applies mutation-based robustness testing with semantic-preserving operators and a task fitness function across multiple MAS configurations, datasets, and model backbones. Even when problem semantics are preserved, solve rates collapse on many cases (reported failure on 7.9%–83.3% of previously solved tasks). Failure attribution points to a planner-coder gap as the dominant mechanism: planning agents emit underspecified decompositions and coding agents then misinterpret latent logic during implementation. The proposed repair adds multi-prompt plan generation plus a monitor agent to reduce information loss between planning and coding stages, recovering a substantial fraction of failures.

## Confidence

High for the directional finding that robustness brittleness is real and often rooted in inter-agent handoff quality; medium for exact effect-size transferability outside the evaluated stacks and benchmarks.

## Empirical Findings (Data Snapshot)

| Novel finding | Quantitative result | Experimental setup/sample | Metric/outcome | Caveat/limit |
|---|---|---|---|---|
| Semantics-preserving mutations can drastically reduce multi-agent solve reliability, revealing hidden brittleness. | Previously solved tasks fail under mutation in **7.9%–83.3%** of cases across evaluated setups. | Mutation-based robustness evaluation with semantic-preserving operators and fitness checks across multiple MAS configurations, datasets, and model backbones. | Robustness failure rate under semantic-invariance stress tests; planner-coder handoff identified as dominant failure source. | Exact uplift from the proposed monitor-based repair is directional in this pass (full table-level deltas not extracted here). |

## Why it matters for Sapho

This is direct evidence that multi-agent software-factory performance depends on handoff-contract quality, not just model capability. It supports stronger planning artifacts, explicit monitor roles, and robustness gates that test semantic invariance before trusting production autonomy.
