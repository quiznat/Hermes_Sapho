# Executive Brief

Date: `2026-03-06`
Run ID: `pm-live-20260306T003008Z`

## Executive Summary
The evidence supports a conditional factory-model thesis with medium confidence: agentic software leverage increases when orchestration is paired with strong verification, constrained intent-to-action translation, disciplined operations, and high-quality memory/retrieval controls. The evidence does not support autonomy-alone claims. With discarded items far exceeding processed items, conclusions should be treated as boundary-aware and stress-tested rather than universal.

## Top Findings
- **art-2026-03-04-074** (agent-factory · confidence=medium): Agentic coding is shifting leverage toward factory-style orchestration, where specification quality, architecture clarity, and verification discipline determine output quality.
  - Mechanism: The model progresses from autocomplete to copilots to autonomous multi-step agents; as generation scales, verification becomes the bottleneck, making tight specs and reliable red/green workflows core control surfaces.
  - Source: https://addyosmani.com/blog/factory-model/
- **art-2026-03-04-060** (agent-memory · confidence=medium): Natural-language workflow control becomes materially more usable when tied to reproducible operations and policy boundaries.
  - Mechanism: Intent is translated into constrained workflow actions so human-readable control is preserved while execution remains deterministic and guardrailed.
  - Source: https://aws.amazon.com/blogs/opensource/introducing-strands-agent-sops-natural-language-workflows-for-ai-agents/
- **art-2026-03-04-050** (agent-factory · confidence=medium): Self-hosted personal agents can move to cloud infrastructure when isolation, automation, persistence, and model mediation are composed as a coherent stack.
  - Mechanism: A decomposed architecture separates control plane, isolated runtime, browser automation, persistent storage, and model gateway routing, improving governability while adding service-interface dependencies.
  - Source: https://blog.cloudflare.com/moltworker-self-hosted-ai-agent/
- **art-2026-03-04-038** (agent-research · confidence=medium): OpenClaw outcomes are driven more by ongoing operating discipline than by one-time setup.
  - Mechanism: A loop of delegation, recurring automation, staged permissioning, safety boundaries, and iterative feedback compounds reliability and governance quality.
  - Source: https://every.to/guides/claw-school?source=post_button
- **art-2026-03-04-037** (agent-factory · confidence=medium): Role-specialized agent catalogs are a practical control-plane pattern for multi-agent decomposition.
  - Mechanism: Persona-explicit templates with defined missions, process framing, and deliverables improve routing and auditability, but depend on consistent handoff and escalation schemas.
  - Source: https://github.com/msitarzewski/agency-agents
- **art-2026-03-04-036** (agent-memory · confidence=medium): Programming-agent evaluation should measure cross-task experience reuse, not only per-task correctness.
  - Mechanism: Linked-task benchmarking shows that relevant summarized prior experience can improve resolution and lower runtime/token cost, while weakly selected memory can degrade performance via negative transfer.
  - Source: https://arxiv.org/abs/2602.08316

## Actions
- Publish conclusions with explicit boundary conditions, medium-confidence labeling, and documented failure modes.
- Run adversarial intent-to-action compilation tests to detect ambiguity collapse and policy-bypass paths before execution.
- Measure verification bottlenecks directly (defect escape, review load, rework rate, test stability) before claiming factory productivity gains.
- Benchmark decomposed versus monolithic stacks on matched workloads with injected boundary faults.
- Standardize specialist-agent handoffs with required input/output schema, ownership assignment, and escalation triggers.
- Apply retrieval-quality gates: relevance thresholds, provenance requirements, freshness checks, and suppression of low-confidence memory reuse.

## Risks
- High discard ratio (105 discarded vs 61 processed) may introduce selection effects in narrative weighting.
- Evidence remains medium-confidence and partly practitioner-derived, limiting strong causal generalization.
- Natural-language orchestration can create false confidence if compiler constraints fail under adversarial or ambiguous prompts.
- Decomposed architectures can shift failures to service boundaries and increase coordination overhead.
- Specialist-agent proliferation can fragment accountability without mandatory handoff/arbitration contracts.
- Memory reuse pipelines can propagate stale or low-fidelity summaries across repeated tasks.
