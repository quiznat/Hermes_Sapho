# Queue Artifact — art-2026-03-04-005

Source URL: https://github.com/Cluster444/agentic  
Canonical URL: https://github.com/Cluster444/agentic  
Lane: agent-memory  
Decision: retain

## Thesis

`agentic` is a practical context-engineering workflow layer for OpenCode that operationalizes phased software delivery (ticket → research → plan → execute → commit → review) and persists project knowledge in a structured “thoughts” memory surface.

## Mechanism summary

The repository packages reusable agents and slash-commands via a distributable CLI (`agentic pull`) that installs standardized command/agent scaffolding into global or project-local `.opencode` directories. This creates a portable control plane for multi-step coding work, with explicit phase boundaries and intermediate artifacts intended to reduce context drift and improve reproducibility across runs.

## Confidence

Medium. The source is a primary repository/readme with concrete workflow and install semantics, but without benchmark-grade quantitative evidence in the fetched surface.

## Why it matters for Sapho

This is directly relevant to Sapho’s lane focus on context contracts and memory discipline: it is an implementation-grade example of converting prompt behavior into durable workflow structure and explicit handoff artifacts.
