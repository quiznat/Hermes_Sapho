# Executive Brief

Date: `2026-03-12`
Run ID: `pm-live-20260312T233011Z`

## Executive Summary
The evidence supports a stress-first readiness model: single-pass correctness is insufficient for deployment decisions because reliability degrades under repetition, semantic perturbation, and tool/API faults. Production fitness is conditional on task-routed framework selection, model-aware collaboration-plus-debugging composition, long-horizon memory mitigation, and PR governance controls, with security-sensitive lanes requiring stricter throughput planning.

## Top Findings
- **art-2026-03-12-004** (agent-factory · confidence=high): Single-run success rates materially overstate production readiness for tool-using LLM agents; reliability under repeated runs, semantic perturbation, and tool/API faults needs direct stress testing before deployment decisions.
  - Mechanism: ReliabilityBench defines a joint reliability surface over repeat consistency, perturbation robustness, and injected tool/API fault tolerance, and evaluates ReAct/Reflexion across operational domains to expose failures that single-pass metrics miss.
  - Source: https://arxiv.org/html/2601.06112v1
- **art-2026-03-11-020** (UI-design · confidence=high): Agent-framework performance on code-centric software engineering is currently moderate and highly trade-off-driven; framework selection materially affects effectiveness, efficiency, and cost outcomes by task type.
  - Mechanism: Comparative evaluation of seven agent frameworks across software development, vulnerability detection, and program repair shows task-dependent shifts in correctness, runtime efficiency, and token/cost overhead.
  - Source: https://arxiv.org/html/2511.00872v1
- **art-2026-03-11-017** (agent-factory · confidence=high): Combining multi-agent collaboration with runtime-execution debugging measurably changes code-generation performance, and model response to this composition is heterogeneous enough to matter for system design decisions.
  - Mechanism: A chained analyst/coder/tester-style decomposition followed by runtime-feedback debugging is benchmarked against standalone strategies, showing model-dependent net effects rather than uniform uplift.
  - Source: https://arxiv.org/html/2505.02133v1
- **art-2026-03-10-080** (agent-memory · confidence=high): LoCoMo is a primary benchmark for very long-horizon conversational memory, exposing persistent recall and temporal-causal reasoning gaps in current LLM agents.
  - Mechanism: Grounded long-conversation generation with persona and temporal event-graph structure is evaluated via QA, event-graph summarization, and multimodal dialogue generation, revealing durable long-horizon memory weaknesses.
  - Source: https://snap-research.github.io/locomo/
- **art-2026-03-10-077** (agent-factory · confidence=high): Agentic pull requests demonstrate strong local-level commit communication but weaker PR-level alignment and higher short-horizon code churn compared with human pull requests.
  - Mechanism: At large scale, agent PRs show higher commit-level semantic similarity but weaker PR-summary alignment, faster symbol removal, and higher short-horizon churn, indicating local coherence does not guarantee stable integration intent.
  - Source: https://arxiv.org/html/2601.17627v1
- **art-2026-03-10-069** (agent-factory · confidence=high): Agent-authored pull requests make meaningful security contributions in real repositories, but those contributions face stricter human scrutiny, lower merge rates, and longer review latency than non-security agentic PRs.
  - Mechanism: Large-scale AIDev analysis with manual validation of security-related PRs shows governance and review burden are stronger constraints in security lanes than in non-security agent PR lanes.
  - Source: https://arxiv.org/abs/2601.00477

## Actions
- Adopt stress-gated evaluation requiring thresholds for repeated-run consistency, perturbation robustness, and injected tool/API fault tolerance.
- Replace global framework defaults with task-routed policies jointly optimized for correctness, runtime, and token/cost.
- Build model-family interaction maps for collaboration-plus-debugging chains and enforce explicit composition allow/deny rules.
- Instrument long-horizon memory failure indicators and map LoCoMo-style breakdowns to coding-session continuity risks.
- Add PR gates for PR-level alignment and churn-risk alongside commit-level quality checks.
- Create dedicated security-PR lanes with stronger pre-merge validation, reviewer-capacity planning, and explicit latency budgets.

## Risks
- Readiness decisions based on single-pass metrics can miss instability under repetition, perturbation, and tool/API faults.
- One-size-fits-all framework defaults can degrade net utility under changing task mixes.
- Unmanaged collaboration-plus-debugging chains can add orchestration overhead and propagate errors.
- Long-horizon memory weakness can degrade planning continuity and PR-level intent coherence.
- High local commit coherence can mask PR-level misalignment and churn-driven rework.
- Security lanes can accumulate latency and rejection bottlenecks without dedicated governance and capacity controls.
