# Queue Item Processing — art-2026-03-01-030

## Source metadata
- URL: https://github.com/snarktank/ralph
- Source type: GitHub repository (autonomous loop framework)
- Lane tags: `agent-factory`, `agent-memory`
- Processed at (UTC): 2026-03-01T23:27:00Z

## Enrichment artifacts consulted
- Repo page: https://github.com/snarktank/ralph
- Canonical README: https://raw.githubusercontent.com/snarktank/ralph/main/README.md

## Structured extraction

### What it is
Ralph is an autonomous coding loop runner that repeatedly executes fresh AI coding sessions against a PRD task list (`passes: false` -> `true`) until completion, with memory persisted outside the active context window.

### High-signal mechanisms
1. **Fresh-instance execution discipline**: each iteration starts with clean context, reducing drift from long conversational histories.
2. **Deterministic external memory** through artifact channels: `git history`, `progress.txt`, `prd.json`.
3. **Task-size doctrine**: stories must be small enough to complete within one context window, with explicit anti-patterns for oversized tasks.
4. **Feedback loop dependency**: typecheck/tests/CI are treated as essential control surfaces, not optional checks.
5. **AGENTS.md as durable learning sink**: post-iteration learnings are written back to machine-readable repo guidance for future runs.
6. **Tool/runtime flexibility**: supports Amp and Claude Code pathways, including marketplace skill packaging.

### Factory + memory-lane interpretation
This source is a direct implementation anchor for the core factory pattern we are using: short-context execution plus durable artifact memory. It strengthens the case that reliability is achieved by strict loop contracts and state externalization, not by attempting infinite-context reasoning.

## Decision
- Decision: **retain**
- Rationale: highest relevance to software-factory loop architecture and artifact-based memory strategy.
- Confidence: high.

## Processing notes
This item should be treated as canonical evidence for fresh-context loop governance in our evolving factory memo and for the final opinion paper on library/memory/context systems.
