<details class="traceability-panel">
<summary>Traceability</summary>
<div class="traceability-body">
<ul>
  <li><strong>Source:</strong> <a href="https://snap-research.github.io/locomo/" target="_blank" rel="noopener">https://snap-research.github.io/locomo/</a></li>
  <li><strong>Intake queued:</strong> 2026-03-10T22:35:55Z</li>
  <li><strong>Source captured:</strong> 2026-04-05T16:14:24Z</li>
  <li><strong>Curated:</strong> 2026-04-05T16:14:39Z</li>
  <li><strong>Artifact finalized:</strong> 2026-04-05T16:17:25Z</li>
  <li><strong>Artifact published:</strong> 2026-04-05T16:19:25Z</li>
</ul>
</div>
</details>

# Evaluating Very Long-Term Conversational Memory of LLM Agents

## Core Thesis

LoCoMo is a deliberately constructed benchmark for testing long-horizon conversational memory across months of interaction, and the reported results show that current language models remain far from human performance on this problem. The benchmark is useful because it forces retrieval, temporal tracking, and reasoning across long dialogue histories, but its claims must be read with the bound that the conversations are synthetic and materially corrected by human annotators rather than captured as raw natural conversation.

## Why It Matters for Sapho

This matters because it sharpens a core Sapho judgment: long context alone should not be treated as evidence of durable memory competence. LoCoMo shows that memory performance depends on what is retrieved, how relevance is preserved, and whether models can reason over temporally distributed facts without drowning in noise. It also shows why evaluation doctrine must distinguish between a controlled stress test and a realism claim. The benchmark is valuable as a hard testbed for long-range conversational coherence and recall, but it does not justify broad claims that agents already handle real-world longitudinal dialogue.

## Key Findings

- LoCoMo is built from 50 long conversations averaging 304.9 turns, 19.3 sessions, and 9,209.2 tokens per dialogue, with interactions spanning months and including multimodal content.
- The corpus is not purely naturalistic: conversations are first generated through an LLM-agent pipeline and then revised by human annotators, who edited nearly 15% of turns and removed or replaced about 19% of images.
- The benchmark QA set contains 7,512 questions, including 2,705 single-hop, 1,104 multi-hop, 1,547 temporal, 285 open-domain, and 1,871 adversarial items, making it a broad test of recall and reasoning rather than a narrow retrieval exercise.
- Humans score 87.9 overall F1 on the QA task, while the best reported long-context model in the main table reaches 37.8, leaving a large unresolved gap in long-term conversational memory performance.
- Performance is especially brittle under adversarial conditions: one reported long-context setting for gpt-3.5-turbo-16K falls to 2.1 F1 on adversarial QA, while GPT-4-turbo in a 4K base setting reaches 70.2.
- Retrieval helps when it is selective and observation-centered: top-5 observation retrieval reaches 41.4 overall F1, outperforming top-5 dialog retrieval at 31.7 and top-5 summary retrieval at 32.5, but expanding observation retrieval to top-50 drops performance back to 37.8.

## Evidence and Findings

- The benchmark is genuinely long-horizon by dialogue standards: 50 conversations average 304.9 turns, 19.3 sessions, and 9,209.2 tokens, with temporal structure extending across months. That supports using LoCoMo as a memory stress test rather than a short-context chat benchmark, which matters because many agent claims are still evaluated on much thinner interaction histories.
- The dataset is engineered, not passively observed. Conversations are generated through LLM-based agents with expanded personas and dated event graphs spanning 6 to 12 months, then repaired by humans for consistency. That supports the conclusion that LoCoMo is a controlled benchmark for long-range coherence, and it matters because its strengths come partly from design discipline rather than raw ecological realism.
- Human correction is substantial, not incidental: annotators edited nearly 15% of dialogue turns and removed or substituted about 19% of images. This supports the conclusion that the raw generation pipeline was not sufficient to maintain coherence on its own, which matters because any realism claim must be bounded by the scale of post-generation repair.
- The main empirical result is a large capability gap. On QA, humans reach 87.9 overall F1, while the best reported long-context model reaches 37.8. This supports the conclusion that very long-term conversational memory remains unsolved on this benchmark, and it matters because model competence in ordinary chat or short retrieval settings does not transfer cleanly to months-long conversational recall.
- The failure is not just average underperformance but instability under challenge. The benchmark includes 1,871 adversarial questions, and one reported long-context setting drops to 2.1 F1 on that slice. This supports the conclusion that expanded context exposure does not reliably produce robust memory reasoning, which matters because production systems can fail hardest when distractors and confusable details accumulate.
- Retrieval is helpful only when relevance is tightly controlled. Top-5 observation retrieval reaches 41.4 overall F1, better than top-5 dialog retrieval at 31.7 and top-5 summary retrieval at 32.5, yet top-50 observation retrieval declines to 37.8. This supports the conclusion that selective memory cues outperform broader recall dumps, which matters because more memory surface can degrade performance when it introduces noise instead of usable signal.

## Contradictions and Tensions

- The benchmark’s core value and its core limitation are the same design choice: LoCoMo is useful precisely because it engineers long-range persona and event consistency, but that also means it is not straightforward evidence about how models perform on raw real-world conversation.
- Human repair rates are high enough to create a real tension between controlled benchmark quality and naturalism. If nearly 15% of turns and about 19% of images required editing or replacement, then the benchmark demonstrates a curated long-memory environment more than an untouched behavioral trace.
- Longer context does not cleanly translate into better results. The best reported long-context QA score still remains far below human performance, adversarial QA can collapse sharply in one long-context setting, and event summarization shows a smaller-context configuration outperforming a larger-context one, with FactScore F1 of 45.9 for gpt-3.5-turbo at 4,096 context versus 39.9 for gpt-3.5-turbo-16K.
- Retrieval shows the same non-monotonic pattern. Observation-based top-5 retrieval helps, but performance falls at top-50, indicating that access to more memory can act as contamination rather than support.
- Multimodal assistance is also mixed rather than uniformly additive. MiniGPT-5 with top-5 retrieved observations reaches the best reported MM-Relevance score of 57.8, only modestly above the base model’s 56.1, and the paper reports that multimodal relevance drops as dialogue history grows.

## Mechanism or Bounds

The strongest supported operational mechanism is selective memory cueing rather than brute-force long-context exposure. LoCoMo’s own generation pipeline separates short-term session summaries from turn-level long-term observations, and the evaluation results align with that structure: targeted observation retrieval is more useful than broader dialog or summary retrieval, suggesting that fine-grained, relevance-preserving memory cues better support question answering than larger undifferentiated context windows.

But this mechanism is bounded. The results do not isolate a single cause of failure, and the deficits likely reflect a combination of retrieval noise, temporal reasoning difficulty, hallucination under distractors, attribution mistakes, and weak saliency control. The benchmark also cannot support a claim that these same mechanisms govern fully natural human conversation, because the dialogues are synthetic, scaffolded by event graphs and personas, and materially corrected after generation.

## Limits

LoCoMo is a strong benchmark for long-horizon conversational memory, but it is still a benchmark built from synthetic conversations rather than a direct sample of natural longitudinal dialogue.
The evidence shows a large human-model gap, but it does not cleanly decompose which portion comes from retrieval failure, temporal reasoning failure, hallucination, or benchmark-specific design effects.
The benchmark’s realism is bounded by the construction pipeline, including persona expansion, event-graph planning, memory scaffolding, and substantial human revision.
Some reported gains are narrow and unstable: retrieval helps in selective settings, but more retrieved material or longer history can reduce performance instead of improving it.
The paper supplies a demanding testbed and a clear negative result on current model competence, but it does not justify general claims about universal long-term conversational memory failure outside this benchmark family.
