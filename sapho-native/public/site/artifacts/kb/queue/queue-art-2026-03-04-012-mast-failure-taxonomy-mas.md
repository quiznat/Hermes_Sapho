# Queue Artifact — art-2026-03-04-012

Source URL: https://arxiv.org/abs/2503.13657  
Canonical URL: https://arxiv.org/abs/2503.13657  
Lane: agent-factory  
Decision: retain

## Thesis

Multi-agent LLM systems often fail due to system-level design and coordination pathologies, not just weak base models; improving architecture and verification can unlock larger gains than model substitution alone.

## Mechanism summary

The paper contributes a failure-analysis stack: MAST (a 14-mode failure taxonomy across system design, inter-agent misalignment, and task verification) and MAST-Data (1600+ annotated traces across 7 MAS frameworks). With high human annotation agreement and an LLM-as-judge pipeline, it quantifies recurring failure modes and shows practical intervention headroom via better orchestration and verification design.

## Confidence

High. This is a primary empirical study with explicit taxonomy construction, dataset release, and cross-framework trace analysis.

<!-- canonical-empirical-findings -->

## Empirical Findings (Data Snapshot)

| Novel finding | Quantitative result | Experimental setup/sample | Metric/outcome | Caveat/limit |
|---|---|---|---|---|
| System-level multi-agent failures are patterned and diagnosable via shared taxonomy rather than treated as random agent mistakes. | MAST defines **14 failure modes** and MAST-Data contains **1600+ annotated traces** across **7 MAS frameworks**. | Cross-framework empirical failure analysis with human annotation + LLM-as-judge support over real MAS execution traces. | Failure-mode prevalence and diagnostic coverage for system-design, inter-agent alignment, and verification breakdowns. | `qualitative_only` for per-mode prevalence in this pass; exact mode-level percentages require full table extraction beyond artifact summary. |

## Why it matters for Sapho

Directly relevant to factory governance: it offers a concrete failure ontology and instrumentation pattern for diagnosing loop breakdowns, prioritizing architecture fixes, and designing stage-gated verification policies.
