# Queue Artifact — art-2026-03-04-034

Source URL: https://arxiv.org/abs/2405.15793  
Canonical URL: https://arxiv.org/abs/2405.15793  
Lane: agent-factory  
Decision: retain

## Thesis

SWE-agent shows that software-engineering performance depends strongly on the quality of the agent-computer interface (ACI), not just model capability.

## Mechanism summary

The paper frames LLM agents as a new class of software user and introduces a purpose-built ACI that gives the agent structured primitives for repository navigation, file editing, and test execution. By constraining and shaping interaction with the development environment, SWE-agent improves action reliability over non-interactive prompting and reaches stronger pass@1 performance on SWE-bench and HumanEvalFix than prior baselines.

## Confidence

High. Primary-source paper with concrete benchmark reporting, system design details, and open implementation artifacts.

<!-- canonical-empirical-findings -->

## Empirical Findings (Data Snapshot)

| Novel finding | Quantitative result | Experimental setup/sample | Metric/outcome | Caveat/limit |
|---|---|---|---|---|
| A purpose-built agent-computer interface (ACI) substantially improves autonomous software-task execution quality over non-interactive prompting baselines. | Reported pass@1: **12.5% on SWE-bench** and **87.7% on HumanEvalFix**. | SWE-agent evaluated on two coding benchmarks with custom ACI enabling repository navigation, editing, and test execution. | pass@1 benchmark performance under autonomous agent execution. | Benchmarks and era-specific baselines may not reflect current frontier models; gains are measured within the paper’s evaluation setup. |

## Why it matters for Sapho

This is direct evidence for Sapho’s contract-first orchestration doctrine: better interface and control-surface design materially improves coding-agent outcomes even before changing the underlying model.
