<details class="traceability-panel">
<summary>Traceability</summary>
<div class="traceability-body">
<ul>
  <li><strong>Source:</strong> <a href="https://arxiv.org/abs/2512.24630" target="_blank" rel="noopener">https://arxiv.org/abs/2512.24630</a></li>
  <li><strong>Intake queued:</strong> 2026-03-21T06:28:15Z</li>
  <li><strong>Source captured:</strong> 2026-03-23T01:11:29Z</li>
  <li><strong>Curated:</strong> 2026-04-11T13:33:25Z</li>
  <li><strong>Artifact finalized:</strong> 2026-04-11T13:36:01Z</li>
  <li><strong>Artifact published:</strong> 2026-04-11T13:37:47Z</li>
</ul>
</div>
</details>

# How Do Agentic AI Systems Address Performance Optimizations? A BERTopic-Based Analysis of Pull Requests

## Core Thesis

Performance work in agentic software development is real, broad, and operationally costly, but it is not easy to identify with naive filters and it does not behave like a narrow low-level tuning niche. In this corpus, reliable detection required LLM-based classification plus manual recovery; the resulting performance pull requests were spread across 447 repositories, five agents, and 10 higher-level topic categories, and they were rejected materially more often than non-performance pull requests.

## Why It Matters for Sapho

This source shifts Sapho away from the assumption that agentic performance optimization is mostly a small bucket of obvious speed work. The paper instead shows a wider field: UI, AI, analytics, hardware, low-level, and other layers all appear in the optimization record, and review outcomes are harsher for performance-related changes than for ordinary pull requests. That matters for evaluation doctrine. Any system judging agentic engineering quality needs better detection than keyword search, needs to treat performance work as cross-stack rather than niche, and should expect review friction and slower merges in some categories even when raw change size is not doing much explanatory work.

## Key Findings

- Naive keyword filtering badly overstated the amount of performance work: 10,894 pull requests matched the keyword screen, but a manual check of 100 sampled cases found a 92% false-positive rate.
- The study replaced keyword filtering with zero-shot binary classification using gpt-oss-20B and then manually recovered misses, ending with a final dataset of 1,221 performance-related pull requests.
- That final performance set was broad rather than concentrated: the LLM step identified 1,160 performance pull requests across 447 repositories and five agents, and topic modeling organized the material into 52 topics grouped into 10 higher-level categories.
- Performance-related pull requests were rejected more often than non-performance pull requests: 36.5% versus 22.7%.
- Among 625 accepted performance pull requests, UI, AI, and Analytics had the longest median merge times, while Low-level work merged fastest.
- Change size did not explain much of the timing pattern: the reported association between change size and merge time was weak, with the highest Kendall's tau only 0.38 in Hardware.

## Evidence and Findings

- The paper starts from 33,596 agentic pull requests in the AIDev-POP subset and shows that simple keyword retrieval is not a usable identification method for performance work. Pulling 10,894 candidates sounds comprehensive, but the 92% false-positive rate in a manual sample means the filter mostly captured performance language without actual performance concern. That supports a hard procedural lesson: performance detection in agentic repositories needs semantic judgment, not token matching.
- The authors then reframed the task as binary classification and used zero-shot gpt-oss-20B to mark pull requests as performance-related only when performance was explicitly a concern. In a manual inspection of 200 sampled cases, the reported false-positive rate fell to 7.5%, with 97.5% observed agreement, Cohen's kappa of 0.79, and Gwet's AC1 of 0.97. They also added 61 missed cases from perf-labeled AIDev records, producing a final set of 1,221 pull requests. The supported conclusion is not that the classifier is perfect, but that it is substantially more faithful than keyword screening and good enough to support downstream analysis.
- The resulting performance corpus is structurally broad. The LLM-identified set spans 447 repositories and five agents, and the selected BERTopic configuration yields 52 topics plus 101 outliers, later grouped into 10 higher-level categories across multiple software-stack layers. That matters because it argues against treating agentic optimization as a single narrow practice; the work appears distributed across many kinds of systems and intervention points.
- Topic construction was not arbitrary freehand summarization. The chosen BERTopic setup was selected with a coherence score of 0.47 and a silhouette score of 0.57, and independent topic labeling by the first two authors reached Cohen's kappa of 0.92 before four disagreements were resolved through discussion. This does not make the taxonomy ground truth, but it does support using it as a disciplined map of where performance work appears.
- Outcome comparisons are sharper than the taxonomy story. Performance-related pull requests had a 36.5% rejection rate, versus 22.7% for non-performance pull requests. That is a large practical gap. The paper does not prove why reviewers reject them more often, but it does support the decision-relevant conclusion that performance work carries higher review risk in agentic development settings.
- Timing data points the same way. Among 625 accepted pull requests, UI, AI, and Analytics categories had the longest median merge times, while Low-level work merged fastest. Because change size had only weak association with merge time, peaking at Kendall's tau 0.38 in Hardware, the paper supports a bounded conclusion that category-specific review dynamics matter more than a simple “bigger changes take longer” story.

## Contradictions and Tensions

- The paper's strongest tension is methodological. Keyword filtering produced a huge candidate pool but failed catastrophically, while the LLM-based review sample reported only a 7.5% false-positive rate. That is not a contradiction in the final conclusion, but it shows how badly naive retrieval can distort the apparent scale of performance work.
- Breadth of distribution is visible, but the source cannot tell whether that breadth reflects real underlying demand for optimization, the behavior of the agents, or the composition of the benchmarked repositories. The taxonomy is informative, not a direct census of all possible performance work.
- Review friction is clear, but cause is not. A 36.5% rejection rate versus 22.7% for non-performance work could reflect technical difficulty, stricter review norms, higher deployment risk, or repository-specific governance. The evidence supports the gap, not a single explanation for the gap.
- Merge-time variation cuts against an easy size-based interpretation. UI, AI, and Analytics merged slowest, yet change size had only weak association with merge time. That leaves open the possibility that reviewers are reacting to domain-specific complexity or risk rather than raw patch magnitude.
- The paper also notes that, except for Hardware, most observed optimizations were associated with feature implementation rather than testing or maintenance. That broadens the picture of where performance work happens, but it also creates interpretive tension: optimization appears embedded in development flow, not cleanly separated as a later hardening phase.

## Mechanism or Bounds

The strongest supported mechanism here is procedural and organizational, not causal in the strong sense. Performance-related work is hard to detect because surface performance vocabulary often does not mark true performance concern, which is why semantic classification materially outperforms keyword matching. Once identified, performance work appears across many stack layers and categories, and its review path varies by category more than by raw change size. A bounded operational reading is that performance pull requests trigger heterogeneous review burdens tied to the kind of system being changed, not just to how large the patch is. But the source is still observational: it does not isolate why certain categories merge slower or why performance work is rejected more often.

## Limits

The study is descriptive and corpus-bound.
It relies on a specific agentic pull-request dataset rather than direct observation of the full field.
The classification pipeline is clearly better than keyword filtering, but it is not equivalent to perfect ground truth.
The topic map depends on BERTopic configuration and higher-level grouping choices.
The rejection and merge-time findings establish outcome differences, not their causes.
The paper does not resolve whether observed breadth comes from true optimization demand, agent habits, repository selection, or some interaction among them.
