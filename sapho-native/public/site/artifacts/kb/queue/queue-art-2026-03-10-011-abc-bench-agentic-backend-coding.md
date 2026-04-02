# Queue Artifact — art-2026-03-10-011

Source URL: https://arxiv.org/pdf/2601.11077  
Canonical URL: https://arxiv.org/abs/2601.11077  
Lane: agent-factory  
Decision: retain

## Thesis

Agentic coding systems remain substantially underpowered for realistic backend development when evaluated across full lifecycle execution rather than static code-generation tasks.

## Mechanism summary

ABC-Bench evaluates agents through repository exploration, environment configuration, containerized service setup, and external end-to-end API tests, forcing execution-grounded backend delivery rather than patch-only reasoning.

## Why it matters for Sapho

This provides direct benchmark evidence for software-factory realism: backend reliability must be measured in executable environments with deployment and API validation, not only in isolated PR/bug-fix settings.

<!-- canonical-empirical-findings -->

## Empirical Findings (Data Snapshot)

| Novel finding | Quantitative result | Experimental setup/sample | Metric/outcome | Caveat/limit |
|---|---|---|---|---|
| Using a scalable automated pipeline, we curated 224 practical tasks spanning 8 languages and 19 frameworks from open-source repositories. | 19, 224, 8 | Using a scalable automated pipeline, we curated 224 practical tasks spanning 8 languages and 19 frameworks from open-source repositories. | Using a scalable automated pipeline, we curated 224 practical tasks spanning 8 languages and 19 frameworks from open-source repositories. | However, current benchmarks predominantly evaluate code logic in static contexts, neglecting the dynamic, full-process requirements of real-world engineering, particularly in backend development which demands rigorous environment configuration and service deployment. |

## Confidence

High (primary arXiv benchmark source with explicit task construction and scope counts).
