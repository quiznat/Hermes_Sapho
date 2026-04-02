# Queue Artifact — art-2026-03-04-025

Source URL: https://arxiv.org/abs/2507.13334  
Canonical URL: https://arxiv.org/abs/2507.13334  
Lane: agent-memory  
Decision: retain

## Thesis

Context engineering is a first-class systems discipline for LLM inference, not just prompt wording. Performance and reliability depend on end-to-end context retrieval, processing, management, and orchestration.

## Mechanism summary

This large survey (1400+ papers) formalizes context engineering into foundational components (retrieval/generation, processing, management) and system-level implementations (RAG, memory architectures, tool-integrated reasoning, multi-agent systems). It highlights a central asymmetry: current systems can increasingly understand complex context but still struggle to generate equivalently robust long-form outputs. That gap defines key future work.

## Confidence

High for taxonomy and landscape framing (broad survey scope, explicit decomposition), medium for causal claims due survey-style synthesis rather than controlled experiments.

## Why it matters for Sapho

Provides a canonical map for Sapho’s memory and orchestration lanes: prioritize explicit context pipelines, evaluation of context operations, and architecture-level controls over prompt-only tuning.
