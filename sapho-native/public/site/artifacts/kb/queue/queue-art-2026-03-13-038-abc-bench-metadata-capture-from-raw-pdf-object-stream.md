> Superseded artifact note: this path is retained as a compatibility alias. The metadata-only PDF object-stream stub has been replaced by the repaired source-grounded artifact at `artifacts/kb/queue/queue-art-2026-03-13-038-abc-bench-measures-backend-agents-on-deployment-verified-full-lifecycle-tasks.md`.
>
> The body below mirrors the repaired artifact so legacy viewer links resolve to the corrected content.

# Queue Item Processing — art-2026-03-13-038

## Source metadata
- URL: https://arxiv.org/pdf/2601.11077
- Source type: firehose-brave
- Lane tags: `agent-factory, agent-factory`
- Curated at (UTC): 2026-03-14T02:18:30Z
- Finalized at (UTC): 2026-03-14T02:20:09Z

## Source custody
- Source snapshot: `research/evidence/source-material/2026-03-13/art-2026-03-13-038.json`
- Clean text path: `research/evidence/source-material/2026-03-13/art-2026-03-13-038.md`

## Core thesis
ABC-Bench evaluates backend coding agents on tasks that require repository exploration, code modification, environment configuration, service deployment, and API-level verification, and the reported results show materially lower reliability once the workflow extends beyond code-only editing into runtime setup and deployment.

## Mechanism summary
The benchmark is built with ABC-Pipeline, which filters open-source backend repositories, generates verification suites, synthesizes runtime containers, and instantiates masked benchmark tasks. Evaluation runs agents in an isolated outer container, then builds and launches the resulting service in a separate inner container and scores success only through external API-level functional checks against the deployed system.

## Why it matters for Sapho
This benchmark matters because it pushes coding-agent evaluation closer to the real operational boundary for backend software: not just producing plausible code, but getting a service to build, start, and behave correctly through its exposed API. The reported gap between overall pass rates and environment-build success, along with especially weak Rust performance and much lower outcomes for smaller models, suggests that deployment setup and stack-specific runtime demands remain major bottlenecks even for strong agents. That makes ABC-Bench useful as a corrective to benchmark regimes that may overstate practical readiness by focusing on narrower code-editing tasks without deployment-verified execution.

<!-- canonical-empirical-findings -->

## Empirical Findings (Data Snapshot)

| Novel finding | Quantitative result | Experimental setup/sample | Metric/outcome | Caveat/limit |
|---|---|---|---|---|
| ABC-Bench was constructed as a full-lifecycle backend benchmark from a large repository pool and then filtered into a smaller balanced task set. | The pipeline starts from 2,000 open-source repositories, initially generates 600 candidate tasks, and filters them to 224 final tasks spanning 8 programming languages and 19 frameworks; 132 tasks focus mainly on logic implementation and 92 additionally require autonomous environment configuration and containerized service startup. | ABC-Pipeline explores repositories, generates dedicated API verification suites, synthesizes container configuration, and then creates masked task packages. Task verification requires tests to pass on the original unmasked repository and fail after masking. | The final benchmark composition reported in the visible text is 224 verified tasks with both logic-focused and environment-configuration variants. | Detailed category and distribution statistics are referenced in figures and tables that are not fully visible in the provided source snapshot. |
| The main benchmark results reported in the visible text show a wide performance spread across models on full-lifecycle backend tasks. | Claude Sonnet 4.5 achieves 63.2% pass@1 overall; DeepSeek-V3.2 is described as around 50%; Qwen3-8B does not reach 10%. | All model-agent pairings are evaluated with OpenHands as the default framework, using three independent runs per task. The reported temperatures are 0.7 for standard models and 1.0 for reasoning-enhanced variants. | The source reports strong stratification between top proprietary models, mid-tier models, and smaller models on ABC-Bench. | The full per-model table is not visible in the provided text, so only the explicitly stated headline values can be extracted with confidence. |
| The language-stack breakdown in the visible text reports especially weak performance on Rust relative to more common languages. | Most models, including DeepSeek-V3.2, score 0.0% on Rust tasks, while Claude Sonnet 4.5 and GPT-5 are reported as above 30%. | The benchmark spans 8 programming languages, and the results section compares performance across language stacks including Python, Go, JavaScript, and Rust. | The source reports higher success for widely used stacks such as Python, Go, and JavaScript, with Rust presented as an extreme low-performing case. | The excerpt does not provide the full per-language score table, so only the explicitly named Rust values and qualitative comparisons are recoverable here. |
| The environment-configuration subset analysis decomposes failure into build-stage and post-build functional-stage outcomes and reports setup as the weaker stage for several models. | Across 92 environment-related tasks, Claude Sonnet 4.5 reaches S1=78% and S2=80%; GPT-5 and DeepSeek-V3.2 are described as having S2 above 80% but S1 below 50%; Qwen3-8B has S1 below 20%. | The analysis defines S1 as Environment Build, checking whether the service can be constructed and started, and S2 as Functional Execution, measuring functional test pass rate only for tasks that passed S1. | The visible result separates environment setup success from downstream functional correctness and reports lower setup success than functional success for several models. | Exact S1 and S2 values are not given for every model in the visible excerpt, only thresholds and named values for some cases. |
| Agentic supervised fine-tuning on public trajectory data improves Qwen3 performance in the reported OpenHands evaluation. | Qwen3-8B rises from 8.3% to 13.9% pass@1, and Qwen3-32B rises from 8.9% to 33.8% pass@1. | The paper fine-tunes Qwen3-8B and Qwen3-32B on the agentic coding subset of the publicly available Nex-N1 dataset and evaluates both models with OpenHands. | The source reports higher pass@1 after agentic supervised fine-tuning for both model sizes. | The excerpt does not provide the underlying sample counts for this ablation beyond the general benchmark context, and the full figure is not shown. |

## Confidence
high

Justification: The rating is high because the source is a primary-paper markdown reconstruction from the arXiv e-print bundle and the visible text includes concrete benchmark-construction details plus multiple quantitative findings on task composition, model performance, language breakdowns, environment-stage failures, and fine-tuning effects. The main caveat is that the snapshot is truncated and some referenced figures and tables are only partially visible, so confidence applies to the explicitly recoverable claims rather than to any missing breakdowns.
