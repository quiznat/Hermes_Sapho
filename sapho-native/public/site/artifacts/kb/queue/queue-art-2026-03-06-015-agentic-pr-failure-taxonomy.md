# Queue Artifact — art-2026-03-06-015

Source URL: https://arxiv.org/html/2601.15195v1  
Canonical URL: https://arxiv.org/abs/2601.15195  
Lane: agent-memory  
Decision: retain

## Thesis

Agent-authored pull-request failure is primarily a socio-technical workflow problem, not just a model-capability problem: merge success depends on task type, change scope, CI discipline, and reviewer engagement dynamics.

## Mechanism summary

The paper studies ~33k agent-authored PRs across GitHub and contrasts merged vs not-merged outcomes over task categories, code-change magnitude, CI behavior, and review dynamics, then adds a qualitative taxonomy from 600 PRs. The key mechanism is that broad, riskier, or poorly aligned changes amplify process friction (CI failures, review churn, abandonment), while narrower operational task classes (docs/CI/build updates) align better with current agent strengths and team acceptance norms.

<!-- canonical-empirical-findings -->

## Empirical Findings (Data Snapshot)

| Novel finding | Quantitative result | Experimental setup/sample | Metric/outcome | Caveat/limit |
|---|---|---|---|---|
| Dataset scale | ~33k PRs from five coding agents across real repositories. | — | — | — |
| Highest merge-success task classes | documentation, CI, and build updates. | — | — | — |
| Lowest merge-success task classes | performance and bug-fix tasks. | — | — | — |
| Not-merged PRs correlate with larger changes (more files/edits), lower CI pass behavior, and weaker reviewer convergence. | — | — | — | — |
| Qualitative rejection patterns include reviewer abandonment, duplicates, undesired feature direction, and agent-requirement misalignment. | — | — | — | — |

## Confidence

High. Primary empirical study with large-sample quantitative analysis plus qualitative failure taxonomy.

## Why it matters for Sapho

Directly supports Sapho’s fail-closed publication and harness-governance doctrine: prioritize scoped tasks, enforce CI/pass-gates, reduce blast radius per change, and treat review-process health as a first-class reliability signal for agentic software delivery.
