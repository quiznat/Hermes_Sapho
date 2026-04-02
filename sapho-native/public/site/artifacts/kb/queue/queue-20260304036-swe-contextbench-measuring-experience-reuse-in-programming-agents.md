# SWE-ContextBench: Measuring Experience Reuse in Programming Agents

## Source metadata
- Title: SWE-ContextBench: Measuring Experience Reuse in Programming Agents
- URL: https://arxiv.org/abs/2602.08316
- Source type: Sapho Daily artifact
- Curated at (UTC): 2026-03-30T18:19:39Z
- Finalized at (UTC): 2026-03-30T18:22:08Z

## Core thesis
Programming agents can improve their performance by reusing prior solution experiences, but the effectiveness of this reuse depends heavily on context selection and summarization. SWE-ContextBench provides a structured evaluation framework that isolates and measures these effects across accuracy, time, and cost dimensions.

## Why it matters for Sapho
Experience reuse promises to make coding agents more efficient, yet unfiltered or poorly selected prior context can degrade rather than enhance performance. A rigorous benchmark that quantifies these trade-offs enables researchers to develop retrieval strategies that actually deliver on efficiency claims without compromising output quality.

## Key findings
- SWE-ContextBench augments SWE-Bench Lite with 99 related tasks drawn from dependency and reference relationships, creating task sequences that share contextual grounding for testing experience transfer.
- Correctly selected and summarized experience measurably improves resolution accuracy while reducing both runtime and token costs, demonstrating that compact context can outperform full trajectory reuse.
- Unfiltered or incorrectly selected experience yields limited gains or active harm, indicating that context quality and relevance matter more than volume.

## Limits
This analysis reflects a partial snapshot of the work; full experimental protocols, broader agent comparisons, and detailed failure-mode analyses reside in the complete paper and are not captured here.
