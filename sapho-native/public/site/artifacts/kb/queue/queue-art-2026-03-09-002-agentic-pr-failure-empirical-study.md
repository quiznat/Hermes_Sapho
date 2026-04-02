# Queue Artifact — art-2026-03-09-002

Source URL: https://arxiv.org/html/2601.15195v1  
Canonical URL: https://arxiv.org/html/2601.15195v1  
Lane: agent-factory  
Decision: retain

## Thesis

Agent-authored pull request failure is not primarily a model-intelligence problem; it is a workflow-fit problem driven by CI breakage, oversized changes, and weak reviewer engagement.

## Mechanism summary

This paper studies more than 33,000 agent-authored GitHub pull requests across five coding agents and then qualitatively analyzes 600 not-merged PRs. The evidence points to a repeatable failure mechanism: agent PRs are accepted when they align with low-risk repository workflows (documentation/CI/build updates), and rejected when they require deeper contextual correctness (performance and bug-fix work), larger code diffs, stronger CI reliability, and sustained human review interaction. The qualitative taxonomy adds social/process failure modes that raw metrics miss, including reviewer abandonment, duplicate PRs, and unwanted feature implementations.

<!-- canonical-empirical-findings -->

## Empirical Findings (Data Snapshot)

| Novel finding | Quantitative result | Experimental setup/sample | Metric/outcome | Caveat/limit |
|---|---|---|---|---|
| , 2025 ) , which comprises over 33k PRs submitted by five major coding agents across GitHub projects with more than 100 stars. | 100, 2025 | , 2025 ) , which comprises over 33k PRs submitted by five major coding agents across GitHub projects with more than 100 stars. | , 2025 ) , which comprises over 33k PRs submitted by five major coding agents across GitHub projects with more than 100 stars. | — |
| Vasilescu (2017) The impact of continuous integration on other software development practices: a large-scale empirical study . | 2017 | Vasilescu (2017) The impact of continuous integration on other software development practices: a large-scale empirical study . | Vasilescu (2017) The impact of continuous integration on other software development practices: a large-scale empirical study . | — |
| Ray (2025) Understanding software engineering agents through the lens of traceability: an empirical study . | 2025 | Ray (2025) Understanding software engineering agents through the lens of traceability: an empirical study . | Ray (2025) Understanding software engineering agents through the lens of traceability: an empirical study . | — |
| Ye (2025) Understanding code agent behaviour: an empirical study of success and failure trajectories . | 2025 | Ye (2025) Understanding code agent behaviour: an empirical study of success and failure trajectories . | Ye (2025) Understanding code agent behaviour: an empirical study of success and failure trajectories . | — |
| Penta (2019) A study on the interplay between pull request review and continuous integration builds . | 2019 | Penta (2019) A study on the interplay between pull request review and continuous integration builds . | Penta (2019) A study on the interplay between pull request review and continuous integration builds . | — |

## Confidence

High for directional use in software-factory operations. The sample size is large and real-world, but the findings remain observational and repository-context dependent.

## Why it matters for Sapho

For Sapho Chapterhouse Institute, this supports lane policy that treats mergeability as a systems constraint: prioritize scoped, CI-safe contribution plans, enforce pre-merge validation discipline, and route high-ambiguity bug/performance work through stronger human-in-the-loop checkpoints instead of naive autonomous execution.
