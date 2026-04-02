# Queue Artifact — art-2026-03-10-009

Source URL: https://arxiv.org/abs/2602.10975  
Canonical URL: https://arxiv.org/abs/2602.10975  
Lane: agent-factory  
Decision: retain

## Thesis

Current agentic coding systems that perform well on bug-fix benchmarks fail sharply on end-to-end feature development tasks, indicating a major capability gap in long-horizon software delivery.

## Mechanism summary

FeatureBench introduces execution-based, test-driven feature-task extraction from repository dependency graphs, generating multi-commit and multi-PR feature tasks with verifiable environments and post-change regression checks.

## Why it matters for Sapho

This is high-value empirical evidence for software-factory evaluation design: it quantifies the gap between SWE-bench-style performance and real feature delivery, and supplies a scalable benchmark construction pattern for ongoing agent reliability tracking.

<!-- canonical-empirical-findings -->

## Empirical Findings (Data Snapshot)

| Novel finding | Quantitative result | Experimental setup/sample | Metric/outcome | Caveat/limit |
|---|---|---|---|---|
| Empirical evaluation reveals that the state-of-the-art agentic model, such as Claude 4.5 Opus, which achieves a 74.4% resolved rate on SWE-bench, succeeds on only 11.0% of tasks, opening new opportunities for advancing agentic coding. | 11.0%, 4.5, 74.4% | Empirical evaluation reveals that the state-of-the-art agentic model, such as Claude 4.5 Opus, which achieves a 74.4% resolved rate on SWE-bench, succeeds on only 11.0% of tasks, opening new opportunities for advancing agentic coding. | Empirical evaluation reveals that the state-of-the-art agentic model, such as Claude 4.5 Opus, which achieves a 74.4% resolved rate on SWE-bench, succeeds on only 11.0% of tasks, opening new opportunities for advancing agentic coding. | — |
| Using this framework, we curated 200 challenging evaluation tasks and 3825 executable environments from 24 open-source repositories in the first version of our benchmark. | 11.0%, 200, 24, 3825, 4.5, 74.4% | Using this framework, we curated 200 challenging evaluation tasks and 3825 executable environments from 24 open-source repositories in the first version of our benchmark. | Using this framework, we curated 200 challenging evaluation tasks and 3825 executable environments from 24 open-source repositories in the first version of our benchmark. | Empirical evaluation reveals that the state-of-the-art agentic model, such as Claude 4.5 Opus, which achieves a 74.4% resolved rate on SWE-bench, succeeds on only 11.0% of tasks, opening new opportunities for advancing agentic coding. |

## Confidence

High (arXiv primary source with explicit benchmark construction and quantitative outcomes).
