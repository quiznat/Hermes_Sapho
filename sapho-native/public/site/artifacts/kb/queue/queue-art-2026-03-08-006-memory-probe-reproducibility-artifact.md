# Queue Artifact — art-2026-03-08-006

Source URL: https://github.com/boqiny/memory-probe  
Canonical URL: https://github.com/boqiny/memory-probe  
Lane: agent-memory  
Decision: retain

## Thesis

This repository is a primary reproducibility artifact for the retained arXiv memory-bottleneck paper and provides concrete implementation pathways for verifying retrieval-vs-utilization claims.

## Mechanism summary

The repo operationalizes the study design across three memory strategies (raw chunks, extracted facts, summarized episodes), includes runnable experiment scripts, top-k ablations, and analysis tooling, and links directly to the paper (`arXiv:2603.02473`). It enables independent reruns rather than relying on abstract-only claims.

<!-- canonical-empirical-findings -->

## Empirical Findings (Data Snapshot)

| Novel finding | Quantitative result | Experimental setup/sample | Metric/outcome | Caveat/limit |
|---|---|---|---|---|
| Reproducibility path includes strategy-level comparisons | 3 memory strategies exposed in runnable pipeline | `run_experiment.py` supports `basic_rag`, `extracted_facts`, `summarized_episodes`-style workflows | Enables direct replication of cross-strategy comparisons | Final metrics depend on dataset/API configuration at run time |
| Retrieval-sensitivity experiments are operationalized | top-k ablation command supports **k=3,5,10** | `python run_experiment.py --top-k 3 5 10` | Supports analysis of retrieval-depth effects | Requires external model API + dataset availability |
| Minimal pilot-to-full scaling path provided | pilot and full experiment modes included | `--pilot` and full-run commands documented | Low-friction validation before full-cost runs | Cost/latency not fixed; environment-dependent |

## Confidence

High. First-party code repository tied to the paper and containing explicit experiment/analysis entry points.

## Why it matters for Sapho

Provides an auditable bridge from paper claims to executable evaluation, aligning with Sapho’s fail-closed evidence doctrine and reproducibility-first memory lane.
