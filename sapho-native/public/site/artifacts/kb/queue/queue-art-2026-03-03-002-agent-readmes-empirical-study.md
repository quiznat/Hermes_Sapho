# Queue Artifact — art-2026-03-03-002

Source URL: https://arxiv.org/html/2511.12884v1  
Canonical URL: https://arxiv.org/html/2511.12884v1  
Lane: agent-memory  
Decision: retain

## Thesis

Agent context files (AGENTS.md/CLAUDE.md/copilot-instructions style files) have become operational control artifacts, but in practice they are often complex, hard to read, and unevenly scoped: teams emphasize functional execution guidance while under-specifying non-functional guardrails.

## Mechanism summary

The paper reports a large empirical sample (2,303 context files across 1,925 repositories). It finds that maintenance behavior looks like configuration drift management (frequent small additions), and that instruction content is skewed toward build/run, implementation details, and architecture. Security and performance instructions appear far less frequently, creating a governance gap where agents are guided on *how to make things work* more than *how to keep outcomes safe and efficient*.

## Confidence

High for directional conclusions (primary-source abstract + body extraction with explicit counts and percentages), medium for fine-grained subgroup claims because this heartbeat pass does not reproduce all appendix tables.

<!-- canonical-empirical-findings -->

## Empirical Findings (Data Snapshot)

| Novel finding | Quantitative result | Experimental setup/sample | Metric/outcome | Caveat/limit |
|---|---|---|---|---|
| Agent context files are function-heavy governance artifacts with sparse non-functional guardrails. | Corpus size: **2,303 files** across **1,925 repositories**. Functional instruction prevalence: implementation details **69.9%**, architecture **67.7%**, build/run commands **62.3%**. Non-functional prevalence: security **14.5%**, performance **14.5%**. | Large-scale empirical content analysis of real OSS agent context files (AGENTS.md/CLAUDE.md/copilot-style manifests). | Instruction-type prevalence across 16 categories; governance coverage skew toward functional execution. | Percentages are prevalence rates, not causal outcome effects; full section-level variance requires deeper table-by-table extraction. |

## Why it matters for Sapho

This source strengthens the lane’s policy direction: context artifacts should be treated as enforceable governance contracts, not passive notes. The practical implication is to require explicit non-functional sections (security/performance/risk) in memory/context manifests, so agent behavior is constrained beyond execution convenience.
