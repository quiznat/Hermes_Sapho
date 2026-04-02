# Queue Artifact — art-2026-03-11-017

Source URL: https://arxiv.org/html/2505.02133v1  
Canonical URL: https://arxiv.org/abs/2505.02133  
Lane: agent-factory  
Decision: retain

## Thesis

Combining multi-agent collaboration with runtime-execution debugging measurably changes code-generation performance, and model response to this composition is heterogeneous enough to matter for system design decisions.

## Mechanism summary

The paper evaluates a chained code-generation workflow that first uses role-specialized multi-agent collaboration (analyst/coder/tester style decomposition) and then applies runtime-feedback-driven debugging, comparing standalone and combined strategies across a broad model set.

<!-- canonical-empirical-findings -->

## Empirical Findings (Data Snapshot)

| Novel finding | Quantitative result | Experimental setup/sample | Metric/outcome | Caveat/limit |
|---|---|---|---|---|
| Our study use 19 LLMs to examines the performance of individual and the proposed strategies, offering comprehensive insights into how different programming activities compositions and training paradigms influence code generation effectiveness. | 19 | Our study use 19 LLMs to examines the performance of individual and the proposed strategies, offering comprehensive insights into how different programming activities compositions and training paradigms influence code generation effectiveness. | Our study use 19 LLMs to examines the performance of individual and the proposed strategies, offering comprehensive insights into how different programming activities compositions and training paradigms influence code generation effectiveness. | — |
| View a PDF of the paper titled Enhancing LLM Code Generation: A Systematic Evaluation of Multi-Agent Collaboration and Runtime Debugging for Improved Accuracy, Reliability, and Latency, by Nazmus Ashrafi and 2 other authors | 2 | View a PDF of the paper titled Enhancing LLM Code Generation: A Systematic Evaluation of Multi-Agent Collaboration and Runtime Debugging for Improved Accuracy, Reliability, and Latency, by Nazmus Ashrafi and 2 other authors | View a PDF of the paper titled Enhancing LLM Code Generation: A Systematic Evaluation of Multi-Agent Collaboration and Runtime Debugging for Improved Accuracy, Reliability, and Latency, by Nazmus Ashrafi and 2 other authors | — |
| [2505.02133] Enhancing LLM Code Generation: A Systematic Evaluation of Multi-Agent Collaboration and Runtime Debugging for Improved Accuracy, Reliability, and Latency | 2505.02133 | [2505.02133] Enhancing LLM Code Generation: A Systematic Evaluation of Multi-Agent Collaboration and Runtime Debugging for Improved Accuracy, Reliability, and Latency | [2505.02133] Enhancing LLM Code Generation: A Systematic Evaluation of Multi-Agent Collaboration and Runtime Debugging for Improved Accuracy, Reliability, and Latency | — |

## Why retain

This is primary empirical benchmark-style evidence directly aligned with Lane 1 goals (multi-agent coding architecture + reliability trade-offs), and it contributes model-selection signal beyond anecdotal engineering blog content.

## Confidence

Medium-high (core design and scope clear; deeper metric extraction should be done if promoted into synthesis memo).
