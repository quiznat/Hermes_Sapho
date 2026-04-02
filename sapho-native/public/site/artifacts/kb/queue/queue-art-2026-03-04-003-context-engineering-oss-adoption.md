# Queue Artifact — art-2026-03-04-003

Source URL: https://arxiv.org/html/2510.21413  
Canonical URL: https://arxiv.org/abs/2510.21413  
Lane: agent-memory  
Decision: retain

## Thesis

AI context files (AGENTS.md/CLAUDE.md/copilot-instructions variants) are now a measurable OSS phenomenon, but usage patterns are heterogeneous and still structurally immature.

## Mechanism summary

This preliminary empirical study analyzes adoption and content evolution of AI context files across a large OSS sample (10,000 sampled repos; detailed context-file analysis on 466 projects). The reported mechanism is governance variance: teams encode context using mixed presentation modes (descriptive, prescriptive, prohibitive, explanatory, conditional) without a stable canonical structure, which likely contributes to uneven downstream agent behavior quality.

## Confidence

Medium-high. Primary source with explicit research questions, sampling strategy, and commit-level evolution framing; still exploratory/preliminary in scope.

<!-- canonical-empirical-findings -->

## Empirical Findings (Data Snapshot)

| Novel finding | Quantitative result | Experimental setup/sample | Metric/outcome | Caveat/limit |
|---|---|---|---|---|
| OSS context-file adoption is measurable at scale, but structure/quality remains heterogeneous. | Adoption scan over **10,000 sampled repositories**; detailed context-file analysis on **466 projects**. | Preliminary empirical study of AGENTS.md/CLAUDE.md/copilot-instructions-style files, including evolution patterns across commits. | Presence/adoption and instruction-style distribution (descriptive/prescriptive/prohibitive/explanatory/conditional) across observed context artifacts. | Exploratory/preliminary design; prevalence and style heterogeneity are descriptive and do not directly quantify downstream task-success impact. |

## Why it matters for Sapho

This supports the need for explicit context contracts and standardized structure in Sapho memory systems, instead of ad-hoc prompt/file styles. It is direct evidence that “context engineering quality” is a first-order control surface, not an implementation detail.
