# Queue Artifact — art-2026-03-02-024

Source URL: https://zenodo.org/records/17760288  
Lane: agent-memory-systems  
Decision: retain

This Zenodo preprint presents a long-horizon human–AI collaboration case study focused on controlling drift in practical execution. The stated contribution is procedural: reliability comes from governance structure rather than raw model capability. The record describes controls such as canonical separation of numerics and narrative, a single strategy master, canonical numbers discipline, and explicit stabilization/challenge protocols.

For Sapho memory-systems work, the paper is directly relevant because it targets the same failure class seen in long-running assistant workflows: context churn, numeric inconsistency, and decision-surface drift. Even with the expected N=1 external-validity limit, it offers a concrete governance pattern that can be translated into enforceable contracts and gate checks.

Next synthesis implication: extract protocol primitives from the full PDF and map each primitive to current foundation contracts (ingest/library/memory/categorization), then test where existing gates already cover drift and where additional constraints are required.

<!-- canonical-empirical-findings -->

## Empirical Findings (Data Snapshot)

| Novel finding | Quantitative result | Experimental setup/sample | Metric/outcome | Caveat/limit |
|---|---|---|---|---|
| Governance-first collaboration controls (canonical numerics/narrative separation, strategy master, stabilization/challenge protocol) reduced drift risk in the reported long-horizon workflow. | `qualitative_only`; single-case report with explicit **N=1** external-validity limitation. | Long-horizon human–AI collaboration case study documented in Zenodo preprint workflow record. | Drift-control pattern effectiveness described directionally in case execution narrative (procedural reliability vs raw-model capability). | Single-case evidence; no controlled comparative benchmark or multi-team replication reported in this extraction pass. |
