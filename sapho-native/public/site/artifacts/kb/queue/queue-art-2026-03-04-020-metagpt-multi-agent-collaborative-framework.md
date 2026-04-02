# Queue Artifact — art-2026-03-04-020

Source URL: https://arxiv.org/abs/2308.00352  
Canonical URL: https://arxiv.org/abs/2308.00352  
Lane: agent-factory  
Decision: retain

## Thesis

MetaGPT argues that multi-agent LLM systems become more reliable when collaboration is structured as explicit SOP-driven role handoffs rather than free-form chat among agents.

## Mechanism summary

The framework encodes software-team style Standardized Operating Procedures into prompt chains and assigns specialized agent roles in an assembly-line workflow. This introduces intermediate verification points, role-specific artifacts, and decomposition/recomposition loops that reduce cascading hallucinations in complex tasks.

## Confidence

Medium-high. The work is foundational and benchmark-oriented rather than production-audit evidence, but it is one of the earliest concrete formulations of SOP-first multi-agent orchestration with software engineering framing.

## Why it matters for Sapho

High relevance to Sapho Chapterhouse Institute architecture: it supports contract/SOP-first orchestration, explicit role boundaries, and staged quality checks as practical mechanisms for scaling agent collaboration without collapsing coherence.
