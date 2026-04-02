# Queue Item Processing — art-2026-03-01-023

## Source metadata
- URL: https://openai.com/index/harness-engineering/
- Source type: long-form engineering post
- Lane tags: `agent-factory`, `agent-research`
- Processed at (UTC): 2026-03-01T21:28:00Z

## Enrichment artifacts consulted
- Primary source: OpenAI, "Harness engineering: leveraging Codex in an agent-first world"

## Structured extraction

### Core thesis
In high-throughput agentic development, the primary engineering bottleneck shifts from writing code to designing the harness: constraints, observability, review loops, and repository-legible context that let agents execute reliably.

### High-signal mechanisms
1. A strict no-manual-code operating constraint forced all capability improvements to be encoded in reusable scaffolding rather than ad hoc heroics.
2. Agent throughput was sustained through iterative PR loops, local/cloud agent reviews, and Ralph-style self-review cycles.
3. UI and observability were made directly legible to agents through CDP access, per-worktree app instances, and queryable logs/metrics traces.
4. A short AGENTS.md acted as a map, while deeper docs/plans were structured in-repo and mechanically checked by linters/CI.
5. Architectural invariants were enforced with custom structural checks, allowing local implementation freedom inside hard boundaries.

### Factory-lane interpretation
This is strong evidence that software factories compound when they move judgment into codified invariants and testable harnesses. The practical recommendation is to invest in system-level feedback loops and repository-legible control planes before optimizing model cleverness.

## Decision
- Decision: **retain**
- Rationale: directly aligned with software-factory operating model design and provides concrete, transferable controls.
- Confidence: high (detailed primary-source operational account).

## Processing notes
This item should be treated as reference evidence for supervisor-mode orchestration, doc-as-map architectures, and invariant-first governance in the canonical roadmap and living factory memo.
