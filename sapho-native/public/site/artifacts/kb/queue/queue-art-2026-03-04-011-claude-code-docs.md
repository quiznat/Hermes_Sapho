# Queue Artifact — art-2026-03-04-011

Source URL: https://docs.anthropic.com/en/docs/claude-code  
Canonical URL: https://docs.anthropic.com/en/docs/claude-code  
Lane: agent-research  
Decision: retain

## Thesis

Claude Code should be modeled as a full-stack agentic coding runtime, not just a chat interface: the docs specify a cross-surface execution system (terminal/IDE/web/desktop/chat/CI) that preserves shared control artifacts (`CLAUDE.md`, skills, hooks, MCP servers) while exposing automation primitives (file edits, command execution, git workflows, sub-agents).

## Mechanism summary

The official docs define both operational surfaces and governance levers. Operationally, Claude Code can execute multi-file code changes, run shell commands, stage commits/PRs, and coordinate sub-agents. Governance-wise, behavior is steered through project-level instruction memory (`CLAUDE.md`), reusable commands/skills, hooks, and MCP-based tool/data connectors. This architecture matters because it makes orchestration policy portable across environments while keeping execution auditable via explicit repo artifacts and CI/chat integrations.

## Confidence

Medium-high. This is first-party Anthropic documentation and therefore authoritative for product capabilities and interface contracts; however, it is product documentation rather than an independent empirical benchmark.

## Why it matters for Sapho

Direct relevance to both queue lanes: Lane 1 gains an evidence-grade reference for codifying agent control surfaces and reusable instruction contracts, and Lane 2 gains implementation guidance for environment-portable, artifact-first agent execution with explicit governance hooks.
