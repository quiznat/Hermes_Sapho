# Queue Artifact — art-2026-03-04-036

Source URL: https://arxiv.org/abs/2602.08316  
Canonical URL: https://arxiv.org/abs/2602.08316  
Lane: agent-memory  
Decision: retain

## Thesis

Programming-agent evaluation should explicitly measure cross-task experience reuse, not only per-task correctness, because real software work repeatedly benefits from prior resolved patterns.

## Mechanism summary

SWE-ContextBench extends SWE-Bench Lite with linked task sequences (300 base tasks plus 99 related tasks) to test whether agents can retrieve and apply prior experience. It evaluates accuracy, time efficiency, and cost efficiency together. Reported results show that correctly selected summarized experience can improve resolution while reducing runtime and token cost; unfiltered or poorly selected experience can produce weak or negative effects.

## Confidence

High for benchmark framing and directional findings from a primary-source benchmark paper.

<!-- canonical-empirical-findings -->

## Empirical Findings (Data Snapshot)

| Novel finding | Quantitative result | Experimental setup/sample | Metric/outcome | Caveat/limit |
|---|---|---|---|---|
| Cross-task memory reuse can improve issue resolution quality and efficiency, but retrieval quality is the key bottleneck. | Benchmark composition includes **300 base tasks** + **99 related tasks** in linked sequences. | SWE-ContextBench (derived from SWE-Bench Lite) evaluates agents on task chains where prior resolved context may be reused. | Accuracy, time efficiency, and cost efficiency under memory-reuse conditions. | `qualitative_only` for effect-size deltas in this heartbeat pass; abstract-level extraction did not include explicit percent improvements/declines by method. |

## Why it matters for Sapho

Directly relevant to Sapho memory governance: validates that memory representation and retrieval precision should be optimized and audited against both correctness and efficiency outcomes.
