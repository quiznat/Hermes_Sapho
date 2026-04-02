# Technical Viewpoint Report — Agentic Research Program

Date: 2026-03-02 (UTC)

## Thesis

The evidence supports a strong position: this program should operate as a governed software factory, not a content summarization pipeline. The winning architecture is harness-first, artifact-memory-centric, eval-governed, and multi-lane by design.

## Evidence base and graph coverage

The current graph ingests all known queue sources and explicitly tracks status across processed, deferred, and discarded items. Coverage now includes 35 total source items, with 15 processed, 19 deferred (X/raw-content gated), and 1 discarded as derivative low-signal.

Primary artifacts:
- `research/kg/nodes.jsonl`
- `research/kg/edges.jsonl`
- `research/kg/stats.json`
- `research/kg/source-manifest.jsonl`

## Position 1 — Harness beats prompt cleverness

The strongest retained signals converge on one point: output quality scales with constraint systems, observability, and structural checks rather than increasingly elaborate one-shot prompts. This includes explicit architecture invariants, feedback gates, and legible repository control planes.

Implication: future build effort should prioritize harness evolution and validation contracts before adding model complexity.

## Position 2 — Externalized memory is non-negotiable

Fresh-instance loop evidence repeatedly confirms that durable artifacts (`prd.json`, progress ledgers, queue records, git history, machine-readable guidance) are the reliable memory substrate. Long context windows are useful but insufficient as operational memory.

Implication: treat artifact quality and update discipline as first-class engineering work.

## Position 3 — Autonomy must be eval-governed

As autonomy increases, risk scales unless evaluation and regression checks tighten in parallel. The retained corpus supports an explicit governance stance: each gain in speed should be paid for with stronger canarying, review synthesis, and deterministic state transitions.

Implication: no new autonomous lane should be promoted without corresponding eval instrumentation and rollback-safe controls.

## Position 4 — Multi-lane synthesis outperforms single-lane generation

The graph-weighted theme distribution and source-level patterns support specialist lane separation plus synthesis, especially for architecture and security-sensitive work. The analysis/write control split is especially important for auditability and idempotent state mutation.

Implication: maintain lane specialization and synthesis contracts; do not collapse into single-model execution for complex technical decisions.

## Data quality policy shift already applied

Derivative aggregator pages are now explicitly gated and can be discarded when they add no net-new technical evidence. This improves novelty density and prevents viewpoint drift from recycled summaries.

Operationalized via:
- `research/firehose/config.seed.yaml` domain gating
- queue decision records (`retain`/`defer`/`discard`) with rationale

## Current blind spot and unblock requirement

The biggest coverage gap is deferred X sources. The graph marks them explicitly as deferred but they cannot contribute substantive claims until raw content payloads are provided.

Unblock path: user-provided raw text + outbound links for deferred X IDs in `research/queue/X-RAW-CONTENT-TODO.md`.

## Next execution move

Implement deferred-X policy hardening in orchestration scripts (`deferReason=awaiting_user_raw_content`, `needsRawContent=true`, TODO sync automation), then rebuild the graph so blocked-source semantics are explicit and queryable in edges.
