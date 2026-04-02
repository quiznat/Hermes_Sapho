# Queue Artifact — art-2026-03-03-013

Source URL: https://arxiv.org/html/2602.20478v1  
Canonical URL: https://arxiv.org/abs/2602.20478  
Lane: agent-memory  
Decision: retain

## Thesis

Single-file agent manifests do not scale reliably for complex codebases; a tiered “codified context infrastructure” (hot-memory constitution + specialist agents + cold-memory knowledge base) can preserve cross-session coherence and reduce repeated failure patterns.

## Mechanism summary

The paper reports a large-project case (108k-line distributed system) and proposes a three-tier memory architecture: always-loaded core conventions, task-invoked domain specialists, and on-demand deep specs. The claimed mechanism is scoped context loading: keep universal guardrails persistent while routing detailed domain knowledge only when needed, avoiding both context amnesia and context overload.

## Confidence

Medium. This is primary-source evidence with concrete architecture and quantitative session metrics, but it is largely an observational/system-report style contribution rather than a randomized comparative benchmark.

<!-- canonical-empirical-findings -->

## Empirical Findings (Data Snapshot)

| Novel finding | Quantitative result | Experimental setup/sample | Metric/outcome | Caveat/limit |
|---|---|---|---|---|
| Layered context infrastructure can preserve cross-session coherence in long-horizon, multi-agent software work. | Case system size **108,000 lines**; infrastructure includes **19 specialized agents** + **34 knowledge documents**; telemetry covers **283 development sessions**. | Observational study during construction of a large C# distributed system using hot-memory constitution, specialist agents, and cold-memory specs. | Interaction-pattern and infrastructure-growth metrics tied to reported consistency/failure-prevention case observations. | No randomized controlled baseline; evidence is high-value but observational and project-specific. |

## Why it matters for Sapho

This is strong design input for Sapho’s memory lane: formalize layered memory contracts and retrieval hooks so orchestration remains stable as project complexity grows, instead of relying on one oversized manifest.
