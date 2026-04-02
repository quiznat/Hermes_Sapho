# Queue Artifact — art-2026-03-04-026

Source URL: https://arxiv.org/abs/2307.07924  
Canonical URL: https://arxiv.org/abs/2307.07924  
Lane: agent-factory  
Decision: retain

## Thesis

Software delivery can be organized as a language-mediated multi-agent workflow where specialized roles coordinate via structured dialogue rather than isolated single-model prompts.

## Mechanism summary

ChatDev frames software development as coordinated communication across role-specialized LLM agents covering design, coding, and testing. The paper’s core mechanisms are a guided chat chain (which constrains what gets communicated across roles) and communicative dehallucination controls (which constrain how agents communicate to reduce drift). A notable operational finding is modality split by task: natural language supports cross-role planning and system design, while code-level exchanges improve debugging precision.

## Confidence

Medium-high for architecture direction (accepted ACL 2024 system paper with released codebase), medium for production-generalization claims because results are framework-centric rather than broad industry benchmarks.

<!-- canonical-empirical-findings -->

## Empirical Findings (Data Snapshot)

| Novel finding | Quantitative result | Experimental setup/sample | Metric/outcome | Caveat/limit |
|---|---|---|---|---|
| Role-specialized, communication-constrained agent teams can complete end-to-end software workflow phases in a unified language-mediated loop. | `qualitative_only` in this heartbeat pass (abstract-level extraction did not expose explicit benchmark deltas). | ChatDev evaluates a multi-agent design/coding/testing framework with chat-chain communication constraints and communicative dehallucination controls. | Demonstrated end-to-end software-task completion behavior and qualitative debugging/design benefits from modality-aware communication. | Full effect sizes and benchmark-by-benchmark numeric gains require deeper table-level extraction from the paper body beyond this pass. |

## Why it matters for Sapho

This is a direct precedent for Sapho’s live multi-agent synthesis doctrine: reliability depends on explicit role protocol + communication contracts, not just stronger base models. It strengthens Lane 2 emphasis on agent-role orchestration and auditable inter-agent handoffs.
