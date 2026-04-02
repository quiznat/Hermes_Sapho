# Queue Artifact — art-2026-03-04-015

Source URL: https://arxiv.org/abs/2503.02400  
Canonical URL: https://arxiv.org/abs/2503.02400  
Lane: agent-research  
Decision: retain

## Thesis

Prompt-enabled systems now require a formal software engineering discipline ("promptware engineering") because prompt artifacts behave like software but run in probabilistic, non-deterministic runtime environments.

## Mechanism summary

The paper frames a lifecycle model for promptware that maps established SE stages (requirements, design, implementation, testing, debugging, evolution, deployment, monitoring) onto prompt-centric systems. The mechanism claim is that ad-hoc trial-and-error prompt iteration does not scale for reliability or governance, so teams need structured process controls, explicit artifact management, and lifecycle-level quality practices.

## Confidence

Medium-high for roadmap-level guidance: this is a primary conceptual framework paper (ACM TOSEM accepted) with clear problem framing, though the core contribution is methodological synthesis rather than a large new benchmark.

## Why it matters for Sapho

This supports Sapho Chapterhouse Institute treating prompts and context files as governed engineering artifacts instead of informal notes, reinforcing contract-driven lifecycle controls in Lane 1 intake and Lane 2 production pipelines.
