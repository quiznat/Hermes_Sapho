# Sapho Live Transition Execution Roadmap

Status: active execution plan
Date: 2026-04-02
Author: Hermes

## 1. Purpose

This document is the formal execution roadmap for getting Sapho onto the new primary system.

OpenClaw is no longer functioning as an operational rail.
That means the new Sapho-native system is no longer a side build or optional replacement path.
It is now the production succession path and must be treated as such.

The goal is not to rush.
The goal is to execute a disciplined sequence of fail-closed slices until the new system is fully operable as the institute’s primary publication rail.

From this point onward, work should proceed by roadmap slice rather than by repeatedly deciding what to do next.

## 2. Governing rules

1. Charter is the law.
2. Fail closed rather than publish weak or unlawful artifacts.
3. Every slice must leave a clean committed fallback point.
4. Artifact quality is judged by dense, decision-grade substance, not by abstract restatement.
5. The article artifact itself must carry the empirical findings, contradictions/tensions, mechanism or bounds, and Sapho relevance.
6. Canon and longform remain out of scope until Daily Rail replacement is proven.
7. If a slice reveals a blocker, fix the blocker and return to the roadmap; do not abandon the roadmap.

## 3. Quality bar for article artifacts

The following regenerated packages are now accepted reference examples for artifact quality:
- `sapho-native/articles/art-2026-03-03-001/`
- `sapho-native/articles/art-2026-03-02-025/`

These define the current article quality bar:
- dense empirical payload
- explicit contradictions/tensions
- explicit mechanism or bounds
- explicit Sapho relevance
- not table-first by default
- not a book report
- not an abstract restatement

Any future artifact article that materially underperforms these examples should be treated as below standard.

## 4. Current state snapshot

What is already true:
- execution seam replacement is complete
- article lane uses bounded Curator / Extractor / Synthesist jobs
- contradiction and mechanism reviews are implemented
- explicit validation exists and is fail-closed
- historical remediation runner exists
- multiple historical artifacts have already been successfully regenerated at the new quality bar
- Sapho content is now tracked broadly in git for disaster recovery and review

What is not yet complete:
- historical corpus remediation is incomplete
- Conclave/publication authority is not yet the full formal live gate
- operator-facing live operations control surface is incomplete
- shadow publication/proof doctrine must be reinterpreted because OpenClaw is no longer a functioning comparison rail
- Piter 2.0 control-plane work remains ahead

## 5. Execution phases

### Phase A — Artifact-quality and replay hardening

Objective:
Make the article lane reliably generate dense, lawful artifacts and survive historical replay.

Status:
- in progress

Already completed inside this phase:
- historical-policy quarantine/current-law classification
- historical remediation runner
- article quality contract hardening
- replay fixes for duplicated outputs, malformed YAML scalars, repeated article documents, and frontmatter quoting
- successful regeneration of `art-2026-03-03-001`
- successful regeneration of `art-2026-03-02-025`

Exit criteria:
- replay path is stable enough to process small batches without frequent parser/runtime failures
- regenerated artifacts consistently meet the new quality bar

### Phase B — Historical corpus remediation

Objective:
Convert meaningful historical imported packages into explicit current-law outcomes.

Allowed outcomes per article:
- `ready-for-daily`
- `discarded`
- `duplicate-rejected`
- `capture-blocked`
- explicit hard failure with receipt if the lane cannot yet process the item

Rules:
- process in small batches
- commit after each successful batch
- keep receipts and before/after state tracked
- do not auto-publish merely because an item becomes `ready-for-daily`

Exit criteria:
- historically important packages are either remediated or explicitly resolved
- failure classes are understood rather than accumulating silently

### Phase C — Formal publication authority gate

Objective:
Turn validation + package legality into the actual live publication gate.

Required outcomes:
- only lawful/current packages are promotion candidates
- explicit package state transitions are enforced
- no publication surface bypasses validation or historical-policy status
- ready-for-daily means genuinely publication-ready under current law

Exit criteria:
- publication authority is explicit and fail-closed
- blocked/quarantined/discarded states are operationally enforced

### Phase D — Live operations control surface

Objective:
Give operators enough visibility and control to run the new primary rail.

Minimum useful capabilities:
- list packages by state
- inspect recent failures by stage
- inspect latest receipts
- rerun one package
- rerun a batch
- identify stuck/problem packages
- list promotion candidates

Exit criteria:
- daily operation does not require ad hoc shell archaeology
- operator can see what is healthy, blocked, or broken

### Phase E — New-primary publication flow

Objective:
Run the new system as the actual institute rail.

Required outcomes:
- source capture/import operational
- article lane operational
- lawful reviews operational
- validation operational
- artifact output operational
- promotion/publication gate operational
- PM/Daily flow operational on the new system

Exit criteria:
- the new system can carry real publication work as the institute’s active rail

### Phase F — Post-stabilization work

Objective:
Strengthen operations after the new rail is genuinely live.

Includes later work such as:
- Piter 2.0 bounded operational slice
- richer monitoring/repair interfaces
- stronger comparison/proof reporting against internal quality standards
- broader historical remediation completion

Not in scope here:
- Canon / longform autonomous rail

## 6. Slice execution protocol

For every slice:
1. inspect context
2. implement narrowly
3. test or otherwise verify
4. update docs if the system state changed
5. commit
6. push
7. report what changed, what passed, and the next roadmap slice

Do not stop after a slice to ask what to do next unless a real branching decision or blocker exists.
The default behavior is to continue to the next roadmap slice.

## 7. Ordered active backlog

This is the execution order from here unless a blocker forces temporary reordering.

### Slice 1
Continue historical remediation in small batches using the stabilized replay path.
Goal:
- expand the set of current-law-compliant regenerated artifacts
- classify remaining failures into real blocker classes

### Slice 2
Build the formal publication authority gate.
Goal:
- ensure `ready-for-daily` and downstream promotion are truly lawful states

### Slice 3
Build the live operations control surface/report.
Goal:
- make the new primary rail operable without constant manual forensics

### Slice 4
Run additional historical remediation batches under the live gate/control surface.
Goal:
- steadily convert the meaningful historical corpus

### Slice 5
Wire the complete new-primary publication flow.
Goal:
- new system can run capture -> article -> law -> validation -> publication as the institute’s live rail

### Slice 6
Begin bounded post-stabilization work.
Goal:
- add operator/repair strength without destabilizing the live rail

## 8. Immediate next slice

Immediate next slice after this roadmap commit:

`Historical remediation batch continuation`

Concrete objective:
- run the next small batch of historical imported candidates through the strengthened lane
- keep the article-quality bar enforced
- commit and push the resulting package updates and receipts

## 9. Completion condition

This roadmap is complete when:
- the new system is the functioning primary publication rail
- article artifacts consistently meet the accepted quality bar
- publication is fail-closed and explicit under current law
- operator can inspect and run the rail without depending on the dead OpenClaw system
- historical-important packages are either remediated or explicitly resolved
