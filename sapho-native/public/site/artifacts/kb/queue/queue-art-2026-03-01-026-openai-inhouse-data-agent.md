# Queue Item Processing — art-2026-03-01-026

## Source metadata
- URL: https://openai.com/index/inside-our-in-house-data-agent/
- Source type: long-form engineering post
- Lane tags: `agent-factory`, `agent-memory`, `agent-research`
- Processed at (UTC): 2026-03-01T21:57:00Z

## Enrichment artifacts consulted
- Primary source: OpenAI, "Inside OpenAI’s in-house data agent"

## Structured extraction

### Core thesis
Reliable data agents require layered grounding and continuous evaluation, not just strong base models. Accuracy at organizational scale depends on context quality, memory reuse, and strict access/evaluation controls.

### High-signal mechanisms
1. **Multi-layer context grounding**: metadata, query inference, curated human descriptions, code-level table derivations, company docs, learned memory, and live warehouse checks.
2. **Daily offline context pipeline**: normalize/aggregate context, embed, and retrieve at runtime for predictable low-latency RAG over large table estates.
3. **Conversational closed-loop execution**: self-correction across multi-step analysis with interruption/clarification handling.
4. **Workflow packaging**: recurring analyses promoted into reusable instruction sets for consistency and speed.
5. **Evaluation discipline**: curated Q/A + golden SQL, executed result comparison, graded by eval framework to catch regressions continuously.
6. **Security model**: strict pass-through permissions and transparent reasoning/result linkage for verifiability.

### Factory + memory-lane interpretation
This is high-confidence evidence for factory systems that elevate context engineering, evals, and memory governance into core infrastructure. The practical lesson is to design agent systems as supervised analytical control loops with explicit provenance, not single-prompt SQL generators.

## Decision
- Decision: **retain**
- Rationale: strong primary-source operational detail directly tied to memory/context and software-factory architecture.
- Confidence: high.

## Processing notes
This item should anchor recommendations in both `software-factory-variant-memo.md` and the upcoming opinion paper on library/memory/context evolution, especially around layered context governance + eval-first regression protection.
