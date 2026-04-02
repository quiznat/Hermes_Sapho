# Queue Item Analysis — art-2026-03-02-011

## Source
- URL: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns
- Type: Microsoft architecture guidance (implementation-oriented design patterns)
- Lane hint: agent-factory

## Core thesis
Agentic systems should be engineered with explicit pattern selection and orchestration controls rather than generic “agent” abstractions. Pattern choice should match task topology, coordination cost, and reliability requirements.

## High-signal mechanisms
- Separates practical agent patterns (single-agent with tools, planner/executor, multi-agent topologies, evaluator loops), which gives direct operating choices instead of broad taxonomy alone.
- Emphasizes orchestration and guardrails (tool boundaries, human-in-the-loop checkpoints, fallback/retry patterns) as first-class reliability controls.
- Highlights memory/context handling and decomposition boundaries as decisive architecture variables, not secondary implementation detail.
- Provides architecture-level pattern guidance that can be translated into queue policy and dispatch heuristics.

## Limits / caveats
- Vendor architecture guidance, not controlled benchmark science; point claims still need empirical corroboration for strict policy commitments.
- Some recommendations are Azure-stack oriented and require portability mapping for non-Azure tooling.

## Categorization decision
- Decision: retain
- Confidence: medium-high
- Lane tags: agent-factory, agent-memory, UI-design
- Rationale: while not experimental, this source is implementation-oriented and contributes concrete pattern-level guidance useful for orchestrator policy and architecture decision templates.

## Immediate workspace implication
Codify pattern-selection prompts/checklists in factory operations so dispatch decisions explicitly choose architecture style (single/planner-executor/multi-agent) with stated guardrails and expected coordination tradeoffs.
