# Sapho Full Implementation Plan

Status: revised
Date: 2026-03-31
Author: Hermes
Basis: direct inspection of the live OpenClaw workspace plus the live public institute site

## 1. Objective

Build a Sapho-native replacement for the current Daily Rail that:
- achieves feature parity with the current live system
- exceeds it on reliability, evidence structure, and repairability
- runs in parallel against a shadow site and shadow RSS for a proof period
- cuts over only after that proof shows the new rail is better

Important scope rule:
Canon/longform work is off-limits for now.
The plan may prepare for future Canon by making artifact bundles more structured, but no Canon implementation work should begin until Daily Rail feature parity++ is achieved and proven.

## 2. What counts as feature parity++

Feature parity means the replacement system can do everything the current live system does on the Daily side:
- AM ingest
- source import/capture
- abstract-only paper blocking and remediation
- curator keep/discard
- duplicate rejection
- findings/facts/summary generation
- incremental artifact publication to site and RSS
- PM daily synthesis
- Conclave pass/block gate
- daily publication surfaces
- receipts and operational mirrors

Feature parity++ means all of the above plus:
- cleaner execution substrate with no OpenClaw disposable worker dependency
- more structured internal artifact bundles
- clearer validators and stronger receipts
- explicit repair/control-plane support through Piter 2.0
- shadow-run comparability and easier rollback

## 3. Non-negotiable design principles

1. Keep one working path.
2. Preserve the current rail split:
   - artifact publication is incremental and separate from PM Daily publication
3. Preserve file-native canonical state.
4. Do not touch Canon implementation until Daily Rail replacement is proven.
5. Replace seams before redesigning the whole machine.
6. Make repair and rollback first-class.
7. Every change that matters must leave durable receipts.

## 4. Current live baseline to preserve

The live chain is:
- AM: `run_runtime_am_job.py` -> `run_micro_am_shift.py`
- Artifact poller: `run_runtime_artifact_job.py` -> `run_micro_artifact_watch.py` -> `run_micro_artifact_publish.py`
- PM: `run_runtime_pm_job.py` -> `run_micro_pm_publish.py` -> `run_pm_cycle.py` -> `run_micro_daily.py`

The main remaining OpenClaw-specific seam in that chain is:
- `parallel-sapho/scripts/openclaw_pocket_agent.py`

That is the primary technical seam to replace first.

## 5. The target architecture for this phase

The Daily-era target system should have four major layers.

### Layer A: Production rail
The normal throughput path.
Responsibilities:
- source capture/import
- article conversion
- artifact publication
- daily synthesis
- daily publication

### Layer B: Validation layer
The law/check layer.
Responsibilities:
- package completeness
- duplicate/conflict checking
- citation integrity
- lineage integrity
- contradiction disclosure baseline
- mechanism field presence baseline

Note: contradiction/mechanism can start minimal in this phase; the point is to structure for them now, not to build full Canon reasoning.

### Layer C: Piter 2.0 control plane
The executive/repair layer.
Responsibilities:
- monitor the Daily Rail
- repair bounded failures
- queue operator-supplied links/material
- produce executive viewpoint outputs

### Layer D: Shadow publication layer
The proof layer.
Responsibilities:
- publish the replacement rail to a shadow site and shadow RSS
- keep it separate from the live public site
- compare outputs, receipts, and reliability against current production

## 6. Workstreams

## Workstream 1: Freeze and codify the current baseline
Goal:
- preserve the exact current Daily system as the comparison target

Deliverables:
- current-system map
- active job chain map
- state transition map
- receipt map
- public surface map
- gold-path article example
- gold-path daily example

Status:
- substantially complete in the existing docs

## Workstream 2: Define the replacement execution substrate
Goal:
- remove dependency on `openclaw_pocket_agent.py`
- keep higher-level production logic unchanged initially

Current call path:
- `micro_common.py` -> `run_loose_agent()` -> `run_pocket_agent()` -> OpenClaw worker

Target interface:
- `run_task(role, prompt, timeout, thinking) -> plain_text`

Requirements:
- preserve role identities used by the rail:
  - curator
  - extractor
  - synthesist
  - conclave/orchestrator
- preserve timeout controls
- preserve output cleaning/sanitization
- preserve strict plain-text contract expectations
- make backend replaceable

Success criterion:
- the new execution adapter can run the existing micro jobs without changing business logic

## Workstream 3: Strengthen artifact bundles without changing public behavior
Goal:
- preserve current public outputs while making internal bundles more structured

Current live article package:
- `article.md`
- `source.md`
- `micro-worthiness.md`
- `micro-findings.md`
- `micro-facts.md`
- `micro-summary.md`

Target upgraded internal package:
- keep the current files for compatibility
- add adjacent structured internals such as:
  - `claims.jsonl`
  - `evidence.jsonl`
  - `lineage.json`
  - `validation.json`
  - optional `contradictions.jsonl`
  - optional `mechanisms.jsonl`

Important constraint:
The public article artifact should not need to change much during this phase. Internals get stronger first.

Success criterion:
- every kept article package has enough structure to support validation and future dossiering
- the current artifact pages and daily pages still render as before

## Workstream 4: Add validators under the current rail
Goal:
- make pass/block and keep/discard less dependent on prompt-only judgment

Validators to define and stage:
1. completeness validator
2. duplicate/conflict validator
3. citation/linkage validator
4. lineage validator
5. contradiction presence/disclosure baseline validator
6. mechanism baseline validator

For this phase, validators do not need to be philosophically complete.
They need to be operationally useful and block obvious bad packages.

Success criterion:
- weak or malformed packages can be blocked by explicit checks even if prose generation looks plausible

## Workstream 5: Formalize Piter 2.0
Goal:
- create the executive control plane that the old system lacked

Piter 2.0 owns four modes:
- Watch
- Repair
- Intake
- View

Piter 2.0 does not own routine throughput.
It sits above the rail.

Responsibilities:
- monitor receipts, state, logs, and public/shadow surfaces
- repair bounded failures with receipts and verification
- queue operator-supplied items into the canonical rail
- produce executive viewpoint outputs from observed patterns

Success criterion:
- when the rail stalls or drifts, Piter can fix it without becoming the rail itself

## Workstream 6: Build the shadow-run infrastructure
Goal:
- run the replacement Daily Rail in parallel without touching the live public site

Needed outputs:
- shadow site root
- shadow kept-links
- shadow artifact pages
- shadow RSS/artifacts feed
- shadow Daily briefing surfaces
- comparison receipts between live and shadow runs

Shadow-run policy:
- no live cutover during proof period
- the live system remains authoritative until shadow wins on evidence

Success criterion:
- the new rail can run for multiple days in parallel without operator babysitting

## Workstream 7: Define cutover criteria
Goal:
- remove ambiguity about when to switch

Suggested cutover criteria:
1. no critical rail failures during proof window
2. artifact publication works incrementally in shadow
3. PM daily surfaces publish cleanly in shadow
4. paper remediation parity is maintained
5. queue insertion works cleanly
6. receipts and ops mirrors are at least as good as live
7. structured bundles and validators provide materially better auditability
8. rollback path is tested

Success criterion:
- cutover becomes a formal decision, not a gut feeling

## 7. Parallel shadow strategy

The end state of this planning phase should support:
- current live system continuing to publish normally
- replacement system running in parallel to a shadow site and shadow RSS
- comparison for several days to a week
- formal cutover only after the replacement proves better

Recommended proof dimensions:
- reliability
- article quality
- artifact publication consistency
- PM package quality
- repairability when something goes wrong
- clarity of receipts and operator visibility

This is the right proving mechanism because it compares institutions, not just scripts.

## 8. Piter 2.0 within the plan

Piter 2.0 should be implemented as the executive overlay for both live and shadow operation.

During the proof window, Piter should be able to:
- monitor both live and shadow rails
- compare their outputs and health
- queue operator-provided sources into the appropriate system under test
- repair shadow failures first without risking the live public rail
- generate viewpoint on whether the replacement is truly better

This is important: the shadow period is not just for the rail. It is also the proof period for Piter 2.0 as an operational role.

## 9. Structured bundle spec for this phase

To prepare for future Canon without implementing it now, structured bundles should at least include:

### Source package additions
- stable `source_id`
- provenance metadata
- content hash
- capture method

### Article package additions
- stable `article_id`
- `claims.jsonl`
- `evidence.jsonl`
- `lineage.json`
- `validation.json`
- optional placeholders for contradiction/mechanism records

### Daily package additions
- cluster ledger
- package lineage summary
- validation reports
- clearer Conclave/validator receipts

The rule for this phase:
Structure for future Canon, but do not build Canon.

## 10. The phases

### Phase 0: Planning freeze
Deliverables:
- current-system docs
- Piter 2.0 spec
- full implementation plan
- schema/validator/execution/shadow specs

### Phase 1: Execution seam replacement
Deliverables:
- provider-neutral runner interface
- existing rail runs unchanged against new backend

### Phase 2: Structured artifact bundle upgrade
Deliverables:
- enriched internal bundles
- compatibility with existing public outputs

### Phase 3: Validator layer
Deliverables:
- explicit package checks
- stronger pass/block foundations

### Phase 4: Shadow publication stack
Deliverables:
- shadow site
- shadow RSS/artifacts feed
- side-by-side receipts and comparisons

### Phase 5: Proof window
Deliverables:
- several days to one week of successful parallel shadow runs
- issue list and fixes
- formal cutover recommendation

### Phase 6: Cutover
Deliverables:
- replacement Daily Rail becomes authoritative
- rollback path retained

## 11. Out-of-scope list for now

Out of scope until cutover success:
- Canon implementation
- longform autonomous paper generation
- large-scale topic dossiering beyond what is needed to structure bundles
- broad institute-wide topology changes beyond the Daily Rail replacement

We can prepare for those later by choosing good schemas now.
We should not build them yet.

## 12. The real definition of success

This phase succeeds when:
- the replacement Daily Rail can do everything the current system does
- it is easier to repair and supervise
- artifact bundles are more structured and auditable
- Piter 2.0 can monitor, repair, queue, and form view without becoming a hero bottleneck
- the replacement can prove itself on a shadow site/shadow RSS before cutover

## 13. Recommended next planning documents

Before coding, the remaining planning docs that should exist are:
1. Daily Rail schema spec
2. validator spec
3. execution substrate replacement spec
4. shadow publication and cutover spec

Those four specs complete the pre-coding plan for this phase.
