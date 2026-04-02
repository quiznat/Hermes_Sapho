# Queue Artifact — art-2026-03-10-005

Source URL: https://arxiv.org/pdf/2510.08790  
Canonical URL: https://arxiv.org/abs/2510.08790  
Lane: agent-memory  
Decision: retain

## Thesis

Long-horizon agent reliability is heavily constrained by context-management failure, and explicitly separating execution, strategy oversight, and context curation can materially improve benchmark performance.

## Mechanism summary

The paper proposes COMPASS, a three-component framework with a Main Agent (task execution), a Meta-Thinker (strategic interventions), and a Context Manager (stage-specific progress briefs) to reduce context drift and error compounding in long-horizon tool-use tasks.

## Why it matters for Sapho

This is direct empirical evidence for the Agent Memory Systems lane: it links context-organization architecture to measurable long-horizon gains and provides a concrete design pattern for memory-aware orchestration.

## Confidence

Medium-high (paper abstract reports up to 20% accuracy improvement across GAIA, BrowseComp, and Humanity's Last Exam; full-method and appendix verification still needed for production-grade mechanism calibration).
