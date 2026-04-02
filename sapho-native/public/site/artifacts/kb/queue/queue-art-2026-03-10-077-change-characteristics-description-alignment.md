# Queue Artifact — art-2026-03-10-077

Source URL: https://arxiv.org/html/2601.17627v1  
Canonical URL: https://arxiv.org/abs/2601.17627  
Lane: agent-factory  
Decision: retain

## Thesis

Agentic pull requests demonstrate strong local-level commit communication but weaker PR-level alignment and higher short-horizon code churn compared with human pull requests.

## Mechanism summary

The study compares 33,596 agent-generated PRs and 6,618 human PRs, finding faster removal of APR-introduced symbols (median 3 vs 34 days), higher symbol churn (7.33% vs 4.10%), stronger commit-message semantic similarity (0.72 vs 0.68), and weaker PR-level summarization alignment (0.86 vs 0.88).

## Why it matters for Sapho

This provides actionable software-factory signal: governance should target macro-level PR reasoning and end-to-end change coherence, not just per-commit quality, and should treat churn/rapid rollback as a first-class reliability metric for agentic delivery.

<!-- canonical-empirical-findings -->

## Empirical Findings (Data Snapshot)

| Novel finding | Quantitative result | Experimental setup/sample | Metric/outcome | Caveat/limit |
|---|---|---|---|---|
| [2601.17627] Code Change Characteristics and Description Alignment: A Comparative Study of Agentic versus Human Pull Requests | 2601.17627 | [2601.17627] Code Change Characteristics and Description Alignment: A Comparative Study of Agentic versus Human Pull Requests | [2601.17627] Code Change Characteristics and Description Alignment: A Comparative Study of Agentic versus Human Pull Requests | — |

## Confidence

High (primary arXiv empirical source with explicit sample sizes and quantitative comparisons).
