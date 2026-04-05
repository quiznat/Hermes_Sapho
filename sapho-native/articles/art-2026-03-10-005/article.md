---
version: article.v1
article_id: art-2026-03-10-005
ticket_id: ticket-import-art-2026-03-10-005
source_url: https://arxiv.org/pdf/2510.08790
source_title: '[2510.08790] COMPASS: Enhancing Agent Long-Horizon Reasoning with Evolving
  Context'
queued_at_utc: '2026-03-10T04:03:59Z'
captured_at_utc: '2026-03-10T06:02:42Z'
canonical_url: https://arxiv.org/abs/2510.08790
curator_decision: kept
artifact_minted_at_utc: '2026-04-05T15:02:39Z'
evidence_count: 11
claim_count: 4
publication_status: ready-for-daily
imported_from_runtime_article_id: art-2026-03-10-005
imported_from_runtime_last_stage: intake
imported_from_runtime_filter_state: pending
curator_reason: This arXiv preprint reports concrete benchmark results for a new long-horizon
  agent framework.
curated_at_utc: '2026-04-05T15:00:26Z'
curator_mode: agent
extracted_at_utc: '2026-04-05T15:02:39Z'
extractor_mode: agent
findings_mode: agent
summary_mode: agent
artifact_publication_alias: '20260310005'
artifact_publication_status: published
artifact_publication_minted_at_utc: '2026-04-05T15:02:39Z'
artifact_publication_published_at_utc: '2026-04-05T15:14:35Z'
---
# COMPASS: Enhancing Agent Long-Horizon Reasoning with Evolving Context

## Core Thesis

COMPASS argues that long-horizon agent performance is bottlenecked less by raw model capability than by context handling over extended tasks. Its answer is a hierarchical design that splits execution, planning, and context evolution across a MainAgent, a Meta-Thinker, and a ContextManager, and the reported results indicate that this structure can materially improve benchmark performance in browsing-heavy and multi-step reasoning settings.

## Why It Matters for Sapho

This matters because it sharpens a live doctrine question: when agents fail on long tasks, the limiting factor may be memory and state management rather than another increment in base-model strength. For Sapho, that pushes evaluation away from generic “agentic” claims and toward a harder question: what specific context-management structure is carrying performance, on which task families, and at what token cost. The paper is useful not because it proves a universal architecture, but because it makes the context bottleneck legible and shows that explicit role separation can buy measurable gains under bounded conditions.

## Key Findings

- COMPASS centers long-horizon reasoning on a three-part hierarchy: a MainAgent for task execution, a Meta-Thinker for higher-level planning, and a ContextManager for maintaining an evolving usable state.
- The paper frames context management as the central failure point in long-horizon agents, and the system design is built directly around that diagnosis rather than around simple agent multiplication.
- Across GAIA, BrowseComp, and Humanity’s Last Exam, the paper reports accuracy improvements of up to 20% over single-agent and multi-agent baselines.
- With Gemini 2.5 Pro, base COMPASS reaches 35.4 Pass@1 on BrowseComp, 67.8 on GAIA, and 31.7 on Humanity’s Last Exam.
- On BrowseComp with Gemini 2.5 Pro, removing the Meta-Thinker drops Pass@1 from 35.4 to 15.2, while removing the ContextManager drops it to 26.4, indicating the larger measured contribution in that setting comes from the Meta-Thinker.
- Test-time scaling pushes results higher—to 43.7 on BrowseComp, 72.1 on GAIA, and 35.2 on Humanity’s Last Exam with Gemini 2.5 Pro—but these gains come with higher token use and diminishing returns that flatten around four samples.
- The paper also reports that a specialized context component, Context-12B, achieves BrowseComp performance comparable to Gemini 2.5 Flash while using about 70% of the tokens.

## Evidence and Findings

- The source presents long-horizon failure as a context-management problem and builds COMPASS as a three-role hierarchy around that premise; this supports the conclusion that performance gains are being pursued through structured memory and planning separation rather than through a monolithic agent, which matters because it identifies a concrete intervention target for agent design.
- The reported benchmark results show COMPASS reaching 35.4 Pass@1 on BrowseComp, 67.8 on GAIA, and 31.7 on Humanity’s Last Exam with Gemini 2.5 Pro, alongside a headline claim of up to 20% accuracy improvement over single-agent and multi-agent baselines; this supports the conclusion that the architecture is not merely conceptually tidy but competitively effective in the paper’s tested settings.
- The BrowseComp ablations are decisive for component contribution: removing the Meta-Thinker cuts Pass@1 from 35.4 to 15.2, while removing the ContextManager cuts it to 26.4; this supports the conclusion that both components matter, with the Meta-Thinker appearing to carry more of the measured lift on that benchmark, which matters because it constrains where the architecture’s value may actually reside.
- The test-time scaling results raise scores to 43.7 on BrowseComp, 72.1 on GAIA, and 35.2 on Humanity’s Last Exam, but the paper also states that token cost rises and gains level off around n = 4; this supports the conclusion that broader inference-time search can extend the system further, but only with a visible efficiency tradeoff rather than a free improvement.
- The reported Context-12B result—BrowseComp performance comparable to Gemini 2.5 Flash at about 70% of the tokens—supports a narrower conclusion that context-specialized components may offer meaningful efficiency leverage, which matters because it suggests architectural decomposition may improve not just accuracy but cost structure in some settings.
- The evaluation is bounded to controlled tasks centered on search, text browsing, and code execution, and it relies mainly on proprietary frontier models; this supports the conclusion that the gains are credible within that envelope but should not be generalized to all long-horizon reasoning or all deployment environments.

## Contradictions and Tensions

- The strongest visible tension is accuracy versus efficiency: test-time scaling improves results, but token cost rises with it, and the gains flatten around four samples rather than compounding cleanly.
- The architecture is presented as a context-management solution, yet the clearest ablation signal on BrowseComp shows a larger drop from removing the Meta-Thinker than from removing the ContextManager. That does not refute the context thesis, but it does complicate any simple claim that context handling alone is the dominant performance driver.
- The paper’s headline strength is broad benchmark improvement, but its external validity is narrower than that headline suggests because the evaluations concentrate on search, browsing, and code-execution tasks using proprietary frontier systems.
- The efficiency story is suggestive rather than settled: the Context-12B comparison hints that a specialized context module can reduce token use, but that does not automatically mean the full hierarchical system is globally efficient once planning overhead and scaling costs are included.

## Mechanism or Bounds

The supported mechanism is bounded role specialization around an evolving-context workflow. The MainAgent handles execution, the Meta-Thinker appears to improve higher-level planning and trajectory control, and the ContextManager is meant to keep working state usable over long horizons. The ablations support that both added roles contribute and that, on BrowseComp with Gemini 2.5 Pro, the Meta-Thinker contributes more to Pass@1 than the ContextManager. That is enough to support a practical mechanism claim: structured decomposition can improve long-horizon performance by reducing the burden on a single agent to both act and maintain coherent task state.

But the mechanism is not fully isolated. The evidence does not prove that context management, in a strict causal sense, is the sole or dominant reason for the gains across all benchmarks. The support is strongest as a benchmark-bounded operational explanation in controlled tasks involving search, text browsing, and code execution.

## Limits

- The evidence is evaluation-bounded and does not establish transfer to broader real-world long-horizon settings.
- The mechanism claim is supported by architectural design and ablation, not by direct causal isolation across all tasks and model families.
- The benchmark-specific contribution ordering between planning and context management is only clearly shown for BrowseComp with Gemini 2.5 Pro and may not generalize.
- The strongest additional gains come from parallel test-time scaling, which increases token cost and weakens any simple performance claim that ignores efficiency.
- The paper relies mainly on proprietary frontier models, so it leaves open how much of the reported lift depends on that model regime rather than on the architecture alone.
