# Queue Artifact — art-2026-03-04-027

Source URL: https://arxiv.org/abs/2601.18341  
Canonical URL: https://arxiv.org/abs/2601.18341  
Lane: agent-factory  
Decision: retain

## Thesis

Coding-agent adoption on GitHub accelerated extremely quickly in 2025 and is already broad across project maturity, organizations, languages, and domains.

## Mechanism summary

This large-scale repository study analyzes explicit coding-agent traces across 129k+ projects and estimates adoption in the ~16% to ~23% range, with growth over time. Agent-assisted commits are observed to be larger and disproportionately feature/fix oriented. The mechanism is workflow autonomy plus artifact traceability: agent tools can act at PR/commit granularity while leaving analyzable signatures in repository history.

## Confidence

High for adoption-direction and scale observations (primary empirical source with large sample and explicit measurement strategy).

<!-- canonical-empirical-findings -->

## Empirical Findings (Data Snapshot)

| Novel finding | Quantitative result | Experimental setup/sample | Metric/outcome | Caveat/limit |
|---|---|---|---|---|
| Coding-agent adoption on GitHub reached high double-digit penetration within months of emergence. | Large-scale study over **129,134 projects** estimates adoption at **15.85%–22.60%**, with upward trend. | Trace-based observational analysis of explicit coding-agent signatures in GitHub artifacts (commits/PR co-authorship and related markers). | Repository-level adoption rate, adopter distribution, and commit-level characteristic shifts. | Observational trace-based method may miss silent/undocumented agent use and does not establish causal productivity impact. |

## Why it matters for Sapho

This validates that agentic development is already mainstream enough to require production-grade governance: merge gates, verification workflows, and telemetry-backed oversight should be treated as defaults, not optional controls.
