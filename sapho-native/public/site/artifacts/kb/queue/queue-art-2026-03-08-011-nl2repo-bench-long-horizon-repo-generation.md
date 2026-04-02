# Queue Artifact — art-2026-03-08-011

Source URL: https://arxiv.org/html/2512.12730v1  
Canonical URL: https://arxiv.org/abs/2512.12730  
Lane: agent-factory  
Decision: retain

## Thesis

Long-horizon repository generation remains unsolved for current coding agents: even top models fail to reliably transform a single requirements document into a complete installable library with passing upstream tests.

## Mechanism summary

NL2Repo-Bench evaluates agents from an empty workspace with only a natural-language specification and no scaffolding, signatures, or test disclosure. Agents must autonomously perform architecture design, dependency management, multi-file implementation, packaging, and verification. Execution is judged only by original upstream pytest suites, making correctness strictly behavioral.

<!-- canonical-empirical-findings -->

## Empirical Findings (Data Snapshot)

| Novel finding | Quantitative result | Experimental setup/sample | Metric/outcome | Caveat/limit |
|---|---|---|---|---|
| Strong agents underperform on long-horizon repo generation | **<40% average test pass rate** for best-performing systems | NL2Repo-Bench across SOTA open/closed models in multiple agent frameworks | Mean upstream-test pass rate | Aggregate figure from paper summary; per-model breakdown requires full tables |

## Confidence

High. Primary arXiv source with explicit benchmark design and quantitative summary statistics.

## Why it matters for Sapho

Reinforces Sapho’s doctrine that long-horizon autonomy must be measured under fail-closed, execution-verified conditions; local code quality proxies are insufficient for production confidence.
