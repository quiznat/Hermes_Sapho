# Queue Artifact — art-2026-03-10-065

Source URL: https://arxiv.org/abs/2601.15195v1  
Canonical URL: https://arxiv.org/abs/2601.15195  
Lane: agent-factory  
Decision: retain

## Thesis

Agent-authored pull requests fail for systematic socio-technical reasons, not just code quality issues.

## Mechanism summary

This MSR 2026 empirical study analyzes 33k agent-authored GitHub PRs across five coding agents, compares merged vs not-merged outcomes across task type, code-change scope, CI results, and review dynamics, then qualitatively codes 600 PRs into a rejection taxonomy.

## Why it matters for Sapho

This gives directly usable failure signatures for software-factory governance: merge probability drops when agent PRs expand code-change scope, fail CI, or trigger low reviewer engagement/misalignment, which implies harness policy, task routing, and reviewer-loop design can improve agentic throughput before model changes.

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

High (primary arXiv empirical paper, accepted at MSR 2026, with explicit sample sizes and mixed-method evidence).
