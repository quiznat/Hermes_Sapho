<details class="traceability-panel">
<summary>Traceability</summary>
<div class="traceability-body">
<ul>
  <li><strong>Source:</strong> <a href="https://arxiv.org/abs/2603.15994" target="_blank" rel="noopener">https://arxiv.org/abs/2603.15994</a></li>
  <li><strong>Intake queued:</strong> 2026-04-12T22:41:10Z</li>
  <li><strong>Source captured:</strong> 2026-04-13T13:01:27Z</li>
  <li><strong>Curated:</strong> 2026-04-13T13:01:53Z</li>
  <li><strong>Artifact finalized:</strong> 2026-04-13T13:05:18Z</li>
  <li><strong>Artifact published:</strong> 2026-04-14T23:38:14Z</li>
</ul>
</div>
</details>

# Selective Memory for Artificial Intelligence: Write-Time Gating with Hierarchical Archiving

## Core Thesis

The paper argues that memory quality can be improved upstream, at write time, rather than mainly at retrieval time. By scoring incoming knowledge for salience and admitting only a small subset into the active store while archiving lower-salience and superseded material with lineage, the system cuts distractor load sharply without losing the ability to answer temporal questions about prior states.

## Why It Matters for Sapho

This matters because it pushes against the common assumption that memory failures are mainly read-side ranking problems. The reported results suggest that store construction policy is itself a major control surface: if irrelevant or outdated material is prevented from dominating the searchable set, retrieval accuracy can rise substantially with less query-time machinery. For Sapho, that supports a stricter doctrine around admission, lineage, and bounded active memory rather than treating all captured material as equally queryable forever.

## Key Findings

- On the main synthetic benchmark with 50 knowledge objects, consisting of 10 correct facts and 40 distractors, write gating admitted only 12-14 objects yet achieved 100.0% ± 0.0% accuracy, while ungated retrieval reached just 13.3% ± 4.7%.
- In the temporal-query test, retaining low-salience and superseded knowledge in cold storage with supersession links preserved prior-state access: the archive-with-lineage design scored 100% on prior-state queries, while an overwrite design scored 0%.
- In distractor-heavy comparisons, write gating usually beat both ungated retrieval and the paper's Self-RAG baseline: at 8:1 synthetic distractors it scored 100% versus 0% for both ungated retrieval and Self-RAG; on procedural pharmacology at 8:1 it scored 96.6% ± 1.6% versus 32.0% ± 4.0% ungated and 80.2% ± 2.1% for Self-RAG; on 2026 arXiv papers at 8:1 it scored 93.6% ± 3.2% versus 45.2% ± 2.0% ungated and 83.2% ± 1.6% for Self-RAG.
- On Wikipedia facts at a 4:1 distractor ratio, write gating reached 98.1% ± 1.1% versus 85.2% ± 2.0% for ungated retrieval.
- The source-label feature helped, but only modestly in the reported Wikipedia setting: removing it reduced write-gated accuracy from 97.8% ± 1.1% to 96.4% ± 1.4%, which suggests source metadata is not the sole driver of performance.

## Evidence and Findings

- The system scores incoming knowledge objects using source reputation, novelty, and source reliability, then applies a salience threshold before retrieval ever occurs. The supported conclusion is that the main performance gain comes from controlling what enters the active store, which matters because it reframes memory quality as an admission problem, not only a search problem.
- On the 50-object synthetic benchmark, the active store was cut down to 12-14 admitted objects and still reached 100.0% ± 0.0% accuracy, while the ungated condition fell to 13.3% ± 4.7%. This supports the conclusion that much of the error came from distractor overload rather than lack of available facts, which matters because it shows selective storage can outperform simply searching a larger pool.
- The temporal experiment preserved older and low-salience objects in cold storage and connected updates through supersession links instead of overwriting. That design reached 100% on prior-state queries, while overwrite reached 0%, supporting the conclusion that lineage-preserving archival can retain historical answerability without keeping every item in the hot store.
- The cross-dataset results show the same pattern under heavier distractor pressure: 100% for write gating at 8:1 synthetic distractors versus 0% for ungated retrieval and 0% for Self-RAG; 96.6% ± 1.6% on procedural pharmacology versus 32.0% ± 4.0% ungated and 80.2% ± 2.1% for Self-RAG; 93.6% ± 3.2% on 2026 arXiv data versus 45.2% ± 2.0% ungated and 83.2% ± 1.6% for Self-RAG. The conclusion is that write-time filtering remains strong outside a single toy setting, which matters because it gives the proposal broader but still bounded operational credibility.
- On Wikipedia at 4:1 distractors, write gating achieved 98.1% ± 1.1% against 85.2% ± 2.0% ungated, and removing the source-label signal only reduced performance from 97.8% ± 1.1% to 96.4% ± 1.4%. This supports the conclusion that source labels contribute but do not explain most of the gain, which matters because it limits any easy story that the method works mainly by relying on external reputation metadata.
- The paper reports that with k=8 retrieved passages, Self-RAG requires 9 LLM calls per query versus 1 for write gating. That supports a practical conclusion beyond accuracy alone: the proposed approach may reduce query-time cost and complexity, which matters because a memory system that wins only by adding heavy read-time machinery may be less attractive in deployment.

## Contradictions and Tensions

- The strongest tension is that write gating alone beat the combined write-gating-plus-Self-RAG condition on the synthetic read-time comparison: 100.0% ± 0.0% for write gating alone versus 93.8% ± 6.3% for both the combined setup and Self-RAG alone. The paper's explanation is that once the store is already clean, the critic can introduce false negatives. That matters because it cuts against the easy assumption that stacking more filtering always helps.
- The paper presents broad superiority claims over Self-RAG, but the comparison is bounded by the fact that it used a Self-RAG-style prompted critic rather than the trained Self-RAG model. That weakens any attempt to interpret the results as a definitive victory over the full original method.
- The source-label signal matters less than one might expect: removing it on Wikipedia only reduced accuracy by 1.4 percentage points, from 97.8% to 96.4%. This creates tension with any interpretation that source reputation is the dominant mechanism; the gains appear to depend more on selective admission overall than on that feature in isolation.
- The temporal-memory result is extremely strong, but it is shown in a specific prior-state query experiment rather than a broad real-world temporal benchmark suite. The operational lesson is important, but its external scope remains narrower than the headline 100% versus 0% contrast may suggest.

## Mechanism or Bounds

The supported mechanism is selective write-time admission. Incoming knowledge objects are scored for salience using signals that include source reputation, novelty, and source reliability, and only a subset enters the active searchable memory. This reduces distractor density before retrieval begins, which is the bounded explanation for the large gains on distractor-heavy tasks. A second mechanism governs temporal robustness: low-salience and superseded objects are archived rather than deleted, and updates are connected through supersession links, allowing prior states to remain recoverable without keeping all historical material in the hot path.

These mechanisms are supported by the reported experiments, but the bounds are clear. The strongest evidence comes from one 50-object synthetic benchmark, a temporal-query experiment, and a small set of chosen datasets including Wikipedia facts, procedural pharmacology, and 2026 arXiv papers under specified distractor ratios. The Self-RAG comparison is also bounded by the use of a prompted critic variant rather than the trained original system.

## Limits

The paper shows strong empirical gains, but it does not establish that the same admission policy will transfer cleanly to open-ended real-world knowledge streams with noisier update patterns and harder novelty judgments.
The comparison against Self-RAG is informative but not final because the evaluated baseline is not the trained original model.
Some of the most dramatic numbers come from synthetic or tightly structured settings, so the magnitude of improvement may shrink in less controlled environments.
The source-label ablation shows that one named scoring signal has only a modest marginal effect in at least one setting, which means the paper does not fully isolate which parts of the scoring function are doing the most work.
The temporal result demonstrates preservation of prior-state access under an archive-and-lineage design, but it does not by itself prove broad historical reasoning performance across varied domains or long update chains.
