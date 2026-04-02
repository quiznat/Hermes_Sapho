# Queue Artifact — art-2026-03-10-015

Source URL: https://arxiv.org/html/2509.16941  
Canonical URL: https://arxiv.org/abs/2509.16941  
Lane: agent-factory  
Decision: retain

## Thesis

Agentic coding performance on real enterprise software work remains far from autonomous reliability once evaluated on long-horizon, contamination-resistant tasks rather than easier public bug-fix subsets.

## Mechanism summary

SWE-Bench Pro expands benchmark realism with 1,865 human-verified tasks across 41 repositories and split design (public, held-out, commercial) that tests multi-file, long-duration software changes under practical enterprise-like constraints.

## Why it matters for Sapho

This provides high-signal benchmark infrastructure for software-factory oversight: it supports stricter claims about long-horizon capability limits and offers a stronger basis for reliability gating than legacy single-scope SWE-Bench-style evaluations.

<!-- canonical-empirical-findings -->

## Empirical Findings (Data Snapshot)

| Novel finding | Quantitative result | Experimental setup/sample | Metric/outcome | Caveat/limit |
|---|---|---|---|---|
| The benchmark is partitioned into a public set with open access to problems sourced from 11 repositories, a held-out set of 12 repositories and a commercial set of 18 proprietary repositories where we have formal partnership agreements with early-stage startups. | 11, 12, 18 | The benchmark is partitioned into a public set with open access to problems sourced from 11 repositories, a held-out set of 12 repositories and a commercial set of 18 proprietary repositories where we have formal partnership agreements with early-stage startups. | The benchmark is partitioned into a public set with open access to problems sourced from 11 repositories, a held-out set of 12 repositories and a commercial set of 18 proprietary repositories where we have formal partnership agreements with early-stage startups. | Problems in the held-out and the commercial set are not publicly accessible, but we release results on the commercial set. |
| SWE-BENCH PRO contains 1,865 problems sourced from a diverse set of 41 actively maintained repositories spanning business applications, B2B services, and developer tools. | 1,865, 25, 41 | SWE-BENCH PRO contains 1,865 problems sourced from a diverse set of 41 actively maintained repositories spanning business applications, B2B services, and developer tools. | SWE-BENCH PRO contains 1,865 problems sourced from a diverse set of 41 actively maintained repositories spanning business applications, B2B services, and developer tools. | Abstract: We introduce SWE-Bench Pro, a substantially more challenging benchmark that builds upon the best practices of SWE-BENCH [25], but is explicitly designed to capture realistic, complex, enterprise-level problems beyond the scope of SWE-BENCH. |
| Abstract: We introduce SWE-Bench Pro, a substantially more challenging benchmark that builds upon the best practices of SWE-BENCH [25], but is explicitly designed to capture realistic, complex, enterprise-level problems beyond the scope of SWE-BENCH. | 25 | Abstract: We introduce SWE-Bench Pro, a substantially more challenging benchmark that builds upon the best practices of SWE-BENCH [25], but is explicitly designed to capture realistic, complex, enterprise-level problems beyond the scope of SWE-BENCH. | Abstract: We introduce SWE-Bench Pro, a substantially more challenging benchmark that builds upon the best practices of SWE-BENCH [25], but is explicitly designed to capture realistic, complex, enterprise-level problems beyond the scope of SWE-BENCH. | — |

## Confidence

High (primary arXiv benchmark source with explicit scale, partitioning, and task-design details).
