# Queue Artifact — art-2026-03-03-001

Source URL: https://arxiv.org/abs/2602.11988  
Canonical URL: https://arxiv.org/abs/2602.11988  
Lane: agent-memory  
Decision: retain

## Thesis

Repository-level context files (for example AGENTS.md) are not automatically performance-improving for coding agents. In the paper’s evaluations, context files often reduced task success while increasing inference cost.

## Mechanism summary

The reported mechanism is behavioral over-constraint: context files induce broader exploration and instruction-following (more file traversal/testing and stricter requirement adherence), but this added process overhead can make task completion harder when requirements are unnecessary or overly broad. The authors observe that LLM-generated context files trend negative on success, while developer-authored files provide only marginal benefit.

## Confidence

Medium-high. This is a primary paper source with explicit benchmark framing and quantitative directional claims, but this heartbeat pass uses abstract + HTML extraction only (not full table-by-table reproduction).

## Empirical Findings (Data Snapshot)

| Novel finding | Quantitative result | Experimental setup/sample | Metric/outcome | Caveat/limit |
|---|---|---|---|---|
| Repository-level context files can make coding-agent tasks harder despite improving instruction-following behavior. | Inference cost increases by **over 20%** with context files; task success is directionally lower vs. no repository context (exact per-agent deltas not provided in abstract text). | Two evaluation settings: (1) SWE-bench tasks with LLM-generated context files, and (2) a novel issue collection from repositories with developer-committed context files; multiple coding agents + LLMs. | Task completion success rate (decrease) and inference cost (increase). | Abstract-level extraction only; exact effect sizes require full paper tables/appendix review. |

## Why it matters for Sapho

This is high-signal evidence for memory/context governance: more context is not inherently better. The immediate implication is to bias toward minimal, task-relevant context contracts and measure net task outcomes rather than assuming context-file presence is beneficial.
