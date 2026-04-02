# Queue Artifact — art-2026-03-04-074

Source URL: https://addyosmani.com/blog/factory-model/  
Canonical URL: https://addyosmani.com/blog/factory-model  
Lane: agent-factory  
Decision: retain

## Thesis

Agentic coding is shifting engineering leverage from manual implementation toward factory-style orchestration, where spec quality, architecture clarity, and verification discipline determine output quality.

## Mechanism summary

The article frames AI coding progression in three generations: autocomplete, synchronous copilots, then autonomous agents that execute multi-step work loops with limited supervision. The key operating model is a “software factory”: engineers define outcomes, split work across parallel agents, and review artifacts rather than author every line. In that model, tight specifications and reliable red/green test workflows become core control surfaces, while verification (not generation) is the bottleneck.

## Confidence

Medium. This is a strategic practitioner essay rather than controlled empirical research, but it provides a concrete systems-level framing that aligns with observed queue signals on orchestration, testing, and quality gates.

## Why it matters for Sapho

It reinforces Sapho’s contract-first doctrine: treat autonomous coding as a governed production system, prioritize spec precision over prompt improvisation, and invest in verification infrastructure to keep fail-closed quality standards intact under parallel agent execution.
