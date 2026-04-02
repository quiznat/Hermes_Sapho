# Queue Artifact — art-2026-03-04-035

Source URL: https://arxiv.org/abs/2510.04618  
Canonical URL: https://arxiv.org/abs/2510.04618  
Lane: agent-memory  
Decision: retain

## Thesis

Context adaptation should be engineered as an evolving system process (generation, reflection, curation), not a one-shot prompt rewrite, to avoid context collapse and maintain domain-specific fidelity over time.

## Mechanism summary

The ACE framework treats prompts/memory as evolving playbooks and applies structured incremental updates rather than monolithic rewrites. The paper identifies two recurrent failure modes in prior context optimization—brevity bias and context collapse—and reports improvements across agent and domain benchmarks with lower adaptation overhead. The key mechanism is controlled context evolution: preserve and refine detailed strategies while continuously integrating execution feedback.

## Confidence

Medium-high. This is a primary framework paper with benchmark claims and explicit mechanism analysis; broader external replication is still valuable.

## Empirical Findings (Data Snapshot)

| Novel finding | Quantitative result | Experimental setup/sample | Metric/outcome | Caveat/limit |
|---|---|---|---|---|
| Evolving playbook-style context adaptation improves both task quality and adaptation efficiency compared with static/rewrite baselines. | Reported gains: **+10.6% on agent benchmarks** and **+8.6% on finance benchmarks**. | ACE evaluated for offline prompt optimization and online agent-memory adaptation with iterative generation-reflection-curation updates. | Performance uplift with reduced adaptation latency and rollout cost. | Abstract-level extraction in this pass does not expose full benchmark-by-benchmark confidence intervals or all ablation detail. |

## Why it matters for Sapho

Directly aligned with Sapho memory doctrine: context artifacts should be durable, iterative, and governance-controlled, with update discipline that preserves useful detail instead of repeatedly compressing it away.
