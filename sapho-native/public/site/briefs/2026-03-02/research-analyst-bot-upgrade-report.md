# Research Analyst Bot Upgrade Report

Date: 2026-03-02 (UTC)

The failure mode in analyst bots is usually not “bad model quality,” it is architectural mismatch. When teams push more agents into a workflow without matching coordination to task structure, quality drops while cost rises. The evidence from this run points to a different playbook: keep orchestration minimal by default, spend complexity only where decomposition is truly parallel, and build evaluation + citation reliability into the core loop instead of as a post-hoc patch.

## What the pipeline run produced

Two focused firehose discovery runs were executed for this question.

- Run `20260302T021844Z`: 50 candidates, 8 kept, 8 inserted into queue (`art-2026-03-02-005` … `012`).
- Run `20260302T022020Z`: 48 candidates, 6 kept, 6 inserted into queue (`art-2026-03-02-013` … `018`).

Together, the pipeline added 14 new non-X items to the queue around agent architecture, evaluation, grounding, and benchmark design.

## Strategic findings that matter for a better analyst bot

The strongest cross-source conclusion is that you should not optimize for “maximum agent count”; you should optimize for coordination-task fit. Google’s scaling study on 180 configurations shows large gains for centralized multi-agent setups on parallelizable work, but heavy degradations on sequential tasks, plus strong error amplification in poorly coordinated topologies. That means your analyst bot should make orchestration a policy decision per task, not a global default.

Anthropic’s multi-agent research-system write-up converges with that result in production conditions: multi-agent designs do outperform single-agent setups on breadth-first research, but token burn is dramatically higher, so economic viability depends on high-value tasks and strict effort scaling. Their engineering details imply a practical rule: use subagents for independent search fronts, and externalize plan/memory aggressively to avoid context-collapse behavior.

Anthropic’s eval methodology suggests the next hard requirement: treat the analyst bot as a harnessed system, not a prompt. The core unit is not just answer quality; it is task outcome under multi-turn tool use, evaluated through trials, transcripts, outcomes, and mixed graders (code-based, model-based, human calibration). Capability suites should push frontier behavior, while regression suites should protect stable behavior after each change.

Benchmark literature reinforces this direction. DeepResearch Bench explicitly evaluates both report quality and citation effectiveness/accuracy, which is closer to analyst-grade performance than generic QA benchmarks. The FACTS benchmark line adds a broader factuality suite (parametric, search, grounding, multimodal) that can serve as a reliability envelope for release gates.

Finally, memory and grounding are not optional add-ons. A-Mem-style dynamic memory organization highlights a path to long-horizon improvement, while grounding surveys emphasize that imperfect retrieval remains the practical bottleneck. In other words: stronger models without retrieval quality control and citation verification still produce confident, expensive mistakes.

## Recommended architecture (opinionated)

Build the analyst as a **policy-driven orchestrator with selective parallelism**. Start with a single-agent path for low-entropy tasks. Escalate to centralized orchestrator-worker mode only when the query is decomposable into independent research branches. Keep decentralized or free-for-all agent topologies out of production paths unless a specific benchmark proves superiority in your domain.

Persist three artifacts on every run: (1) search/retrieval trace, (2) evidence ledger with claim-to-source spans, and (3) synthesis transcript with decision rationale. Make citation verification a first-class stage before finalization, not a stylistic formatter after writing.

Use an eval harness that computes both outcome metrics (did we answer correctly and completely) and process metrics (tool-use efficiency, citation precision, unsupported-claim rate, retry loops, token-to-confidence ratio). Release criteria should require passing both capability and regression suites.

## 14-day implementation plan

Days 1-3 should establish the reliability floor: deterministic harness runs, transcript capture, and claim-source citation checks. Days 4-7 should introduce orchestration policy routing (single-agent default, centralized multi-agent escalation), plus effort budgets tied to query complexity. Days 8-10 should wire benchmark-style tests (DeepResearch-like report quality and citation metrics, FACTS-style factuality slices). Days 11-14 should focus on memory and grounding hardening: dynamic memory updates, retrieval quality monitors, and failure-mode dashboards that block weak outputs from publication.

## High-signal sources used in synthesis

- https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work/
- https://arxiv.org/abs/2512.08296
- https://www.anthropic.com/engineering/multi-agent-research-system
- https://www.anthropic.com/engineering/building-effective-agents
- https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- https://arxiv.org/abs/2506.11763
- https://deepresearch-bench.github.io/
- https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns
- https://arxiv.org/abs/2502.12110
- https://arxiv.org/abs/2407.12858
- https://arxiv.org/abs/2512.10791
