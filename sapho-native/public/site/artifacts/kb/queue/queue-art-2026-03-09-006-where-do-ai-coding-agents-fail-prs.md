# Queue Artifact — art-2026-03-09-006

Source URL: https://arxiv.org/abs/2601.15195v1  
Canonical URL: https://arxiv.org/abs/2601.15195  
Lane: agent-factory  
Decision: retain

## Thesis

Failed agentic pull requests are driven less by a single model-quality issue and more by a socio-technical failure stack: task selection mismatch, CI/test breakage, oversized change scope, and reviewer abandonment.

## Mechanism summary

The paper analyzes 33,596 agent-authored GitHub pull requests from five coding agents, compares merged vs not-merged outcomes across task type, code-change size, CI status, and review dynamics, then manually codes 600 rejected PRs (562 accessible) into a hierarchical taxonomy of failure patterns.

<!-- canonical-empirical-findings -->

## Empirical Findings (Data Snapshot)

| Novel finding | Quantitative result | Experimental setup/sample | Metric/outcome | Caveat/limit |
|---|---|---|---|---|
| , 2025 ) , which comprises over 33k PRs submitted by five major coding agents across GitHub projects with more than 100 stars. | 100, 2025 | , 2025 ) , which comprises over 33k PRs submitted by five major coding agents across GitHub projects with more than 100 stars. | , 2025 ) , which comprises over 33k PRs submitted by five major coding agents across GitHub projects with more than 100 stars. | — |
| Vasilescu (2017) The impact of continuous integration on other software development practices: a large-scale empirical study . | 2017 | Vasilescu (2017) The impact of continuous integration on other software development practices: a large-scale empirical study . | Vasilescu (2017) The impact of continuous integration on other software development practices: a large-scale empirical study . | — |
| Ray (2025) Understanding software engineering agents through the lens of traceability: an empirical study . | 2025 | Ray (2025) Understanding software engineering agents through the lens of traceability: an empirical study . | Ray (2025) Understanding software engineering agents through the lens of traceability: an empirical study . | — |
| Ye (2025) Understanding code agent behaviour: an empirical study of success and failure trajectories . | 2025 | Ye (2025) Understanding code agent behaviour: an empirical study of success and failure trajectories . | Ye (2025) Understanding code agent behaviour: an empirical study of success and failure trajectories . | — |
| Penta (2019) A study on the interplay between pull request review and continuous integration builds . | 2019 | Penta (2019) A study on the interplay between pull request review and continuous integration builds . | Penta (2019) A study on the interplay between pull request review and continuous integration builds . | — |

## Why it matters for Sapho

This is high-grade empirical evidence for the software-factory lane: the practical bottlenecks are not only model capability but also workflow fit. It supports stricter pre-PR CI validation, duplicate-detection checks, and narrower task-scoping before autonomous agents propose changes.

## Confidence

High.
