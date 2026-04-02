# Queue Artifact — art-2026-03-12-004

Source URL: https://arxiv.org/html/2601.06112v1  
Canonical URL: https://arxiv.org/abs/2601.06112  
Lane: agent-factory  
Decision: retain

## Thesis

Single-run success rates materially overstate production readiness for tool-using LLM agents; reliability under repeated runs, semantic perturbation, and tool/API faults needs direct stress testing before deployment decisions.

## Mechanism summary

The paper introduces ReliabilityBench with a unified reliability surface \(R(k,\epsilon,\lambda)\) spanning repeated execution consistency (`pass^k`), perturbation robustness, and fault tolerance under injected tool/API failures. It evaluates ReAct and Reflexion with Gemini 2.0 Flash and GPT-4o across four operational domains and 1,280 episodes.

## Why retain

This is a primary empirical benchmark paper directly aligned with Lane 1 reliability priorities (tool-calling agents, production-like stress, quantified outcomes, explicit evaluation protocol), so it clears fail-closed evidence thresholds for retained queue artifacts.

## Confidence

High.
