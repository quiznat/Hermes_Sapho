# Queue Artifact — art-2026-03-04-033

Source URL: https://arxiv.org/abs/2308.08155  
Canonical URL: https://arxiv.org/abs/2308.08155  
Lane: agent-factory  
Decision: retain

## Thesis

AutoGen established a practical pattern for building LLM applications as structured multi-agent conversations, where agent roles and interaction protocols are first-class design objects.

## Mechanism summary

The framework centers on conversable, customizable agents that can combine LLM reasoning, tool use, and human input. Developers can define interaction patterns in natural language and code, enabling reusable orchestration templates across tasks (coding, QA, operations, decision workflows). The key mechanism is protocolized collaboration: explicit conversation topology and role boundaries improve composability and adaptability versus monolithic single-agent loops.

## Confidence

Medium-high. This is a foundational framework paper with broad examples and open-source implementation; performance claims are mostly application-level demonstrations rather than a single standardized benchmark.

## Why it matters for Sapho

Important lineage source for Sapho factory architecture: validates explicit role decomposition and interaction contracts as core levers for scaling agentic workflows.
