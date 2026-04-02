# Queue Artifact — art-2026-03-04-037

Source URL: https://github.com/msitarzewski/agency-agents  
Canonical URL: https://github.com/msitarzewski/agency-agents  
Lane: agent-factory  
Decision: retain

## Thesis

`agency-agents` is a high-signal repository-level pattern library for role-specialized, persona-explicit AI collaborators, with concrete operating templates spanning engineering, design, product, marketing, QA, support, and orchestration.

## Mechanism summary

The repository provides a large roster of markdown-defined agents grouped by division, each with explicit mission, process framing, communication style, and deliverable expectations. The README includes a practical activation path for Claude Code (`~/.claude/agents/`) and frames the system as an interchangeable specialist team instead of a single generic assistant. For software-factory work, the actionable mechanism is a reusable control plane for role decomposition: specialized prompts + repeatable workflows + explicit success metrics. This supports faster task routing, clearer responsibility boundaries, and more auditable multi-agent coordination patterns.

## Confidence

Medium-high for structural and workflow claims (primary-source repository README and file layout).

## Why it matters for Sapho

Directly relevant to Lane 1 queue/factory synthesis: it provides practical evidence that agentic software execution quality is strongly shaped by role design and operating contracts, not just model choice, and offers a concrete template surface for future Sapho role-card standardization.
