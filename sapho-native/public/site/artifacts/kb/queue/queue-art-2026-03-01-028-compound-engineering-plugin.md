# Queue Item Processing — art-2026-03-01-028

## Source metadata
- URL: https://github.com/EveryInc/compound-engineering-plugin
- Source type: GitHub repository (plugin marketplace + adapter CLI)
- Lane tags: `agent-factory`, `agent-research`
- Processed at (UTC): 2026-03-01T22:27:00Z

## Enrichment artifacts consulted
- Repo page: https://github.com/EveryInc/compound-engineering-plugin
- Canonical README: https://raw.githubusercontent.com/EveryInc/compound-engineering-plugin/main/README.md
- Component reference: https://raw.githubusercontent.com/EveryInc/compound-engineering-plugin/main/plugins/compound-engineering/README.md

## Structured extraction

### What it is
A compound-engineering plugin system plus conversion CLI that ports Claude Code plugin assets (commands/skills/agents/MCP settings) into multiple agent-tool ecosystems (OpenCode, Codex, Droid, Pi, Gemini CLI, Copilot, Kiro).

### High-signal mechanisms
1. **Cross-tool portability layer** for command/skill ecosystems, reducing lock-in to a single agent runtime.
2. **Workflow codification** (`plan -> work -> review -> compound`) as explicit reusable command primitives.
3. **Large modular capability pack** (agents/skills/commands) indicating a role-based multi-agent operating style.
4. **Personal-config sync** (skills + MCP) to propagate institutional setup patterns across tools.
5. **Experimental-target warning** acknowledges fast-moving format risk and adapter drift.

### Factory-lane interpretation
This is strong evidence for a “meta-harness” pattern: production value comes from portable process artifacts (skills/commands/rules), not just any single CLI. Teams can preserve methodology while swapping execution front-ends.

## Decision
- Decision: **retain**
- Rationale: high relevance to software-factory portability, workflow standardization, and capability compounding.
- Confidence: medium-high (documentation is detailed and implementation-facing).

## Processing notes
This source should inform roadmap work around adapter contracts and schema-normalized skill portability between toolchains.
