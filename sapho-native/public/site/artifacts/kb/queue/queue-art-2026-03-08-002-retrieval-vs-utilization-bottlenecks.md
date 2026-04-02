# Queue Artifact — art-2026-03-08-002

Source URL: https://arxiv.org/abs/2603.02473  
Canonical URL: https://arxiv.org/abs/2603.02473  
Lane: agent-memory  
Decision: retain

## Thesis

In memory-augmented LLM agents, retrieval quality is a larger performance bottleneck than write-time memory sophistication under current pipeline designs.

## Mechanism summary

The paper runs a 3×3 diagnostic study crossing three write strategies (raw chunks, Mem0-style fact extraction, MemGPT-style summarization) with three retrieval methods (cosine, BM25, hybrid reranking). It separates where failures occur—write, retrieval, or utilization—and shows most performance variance is explained by retrieval choice, not write strategy complexity.

<!-- canonical-empirical-findings -->

## Empirical Findings (Data Snapshot)

| Novel finding | Quantitative result | Experimental setup/sample | Metric/outcome | Caveat/limit |
|---|---|---|---|---|
| Retrieval method dominates performance variance | Accuracy spans **57.1% → 77.2%** across retrieval methods (≈**20-point** spread) | 3×3 crossing of write strategies × retrieval methods on LoCoMo | End-task accuracy | Results are benchmark-specific to LoCoMo and evaluated methods |
| Simpler raw storage can match/beat expensive lossy writes | Raw chunk storage (zero LLM write-time calls) matches or outperforms lossy alternatives in reported setting | Comparative run across write pipelines under shared retrieval diagnostics | Cost-efficiency and quality tradeoff signal | Depends on retrieval stack quality; may shift with stronger downstream retrieval/utilization |

## Confidence

High. Primary arXiv empirical source with explicit experimental matrix and quantitative deltas in abstract.

## Why it matters for Sapho

Supports Sapho’s foundation-first architecture doctrine: prioritize retrieval pipeline quality and memory-access reliability before increasing write-time complexity.
