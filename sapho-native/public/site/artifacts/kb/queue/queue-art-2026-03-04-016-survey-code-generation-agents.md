# Queue Artifact — art-2026-03-04-016

Source URL: https://arxiv.org/abs/2508.00083  
Canonical URL: https://arxiv.org/abs/2508.00083  
Lane: agent-factory  
Decision: retain

## Thesis

LLM-based code-generation agents are a distinct systems layer beyond classic code-generation models: autonomy, full-SDLC scope, and engineering-first design become the central bottlenecks and opportunity surfaces.

## Mechanism summary

This survey synthesizes architectures (single-agent and multi-agent), SDLC applications, benchmarks/metrics, and tools while emphasizing a field shift from algorithmic generation quality to system reliability, workflow control, tool integration, and verification loops. The practical mechanism is orchestration depth: gains come less from one-shot model outputs and more from iterative planning/action/feedback pipelines.

## Confidence

Medium-high. It is a broad survey (v2 work-in-progress) rather than a controlled benchmark, but it provides a comprehensive map of design space and recurring constraints.

## Why it matters for Sapho

Useful as a canonical frame for factory roadmap prioritization: invest in orchestration, process controls, and evaluation contracts, not only larger base models.
