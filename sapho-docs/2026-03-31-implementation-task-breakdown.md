# Implementation Task Breakdown

Status: draft
Date: 2026-03-31
Author: Hermes
Purpose: final pre-coding breakdown for replacing and strengthening the Daily Rail without breaking live production.

## 1. Build rule

Do not rewrite the whole system at once.
Implement in thin vertical slices.
At every stage:
- preserve current live behavior
- keep rollback easy
- prove each slice before moving on

## 2. Sequence overview

Implementation order:
1. create replacement seam scaffolding
2. swap execution backend behind compatibility adapter
3. add structured article internals while preserving current outputs
4. add validators in non-blocking mode
5. add Piter 2.0 control-plane surfaces and receipts
6. create shadow publication targets
7. run shadow proof
8. tighten validators and cut over

## 3. Phase 1: Execution seam replacement

Goal:
- replace OpenClaw disposable worker dependency with minimal business-logic change

Tasks:
1. Add new task-runner module with canonical `run_task()` interface.
2. Add TaskResult shape and receipt writing.
3. Implement compatibility adapter for `run_loose_agent()`.
4. Preserve current role names and timeout behavior.
5. Add backend config surface for role -> model/runtime mapping.
6. Switch `micro_common.py` to new adapter.
7. Keep old OpenClaw path available behind a feature flag for rollback.

Verification:
- Curator output still parses correctly.
- Findings/facts/summary jobs still run.
- Daily cluster/technical/executive/conclave still run.
- A gold-path article can be processed end to end.

Rollback:
- flip adapter back to old backend flag.

## 4. Phase 2: Structured artifact bundle upgrade

Goal:
- strengthen internals while keeping current public/article behavior stable

Tasks:
1. Add canonical structured files to article package:
   - `curator.json`
   - `findings.jsonl`
   - `facts.jsonl`
   - `claims.jsonl`
   - `evidence.jsonl`
   - `lineage.json`
   - `validation.json`
2. Keep existing compatibility files:
   - `micro-worthiness.md`
   - `micro-findings.md`
   - `micro-facts.md`
   - `micro-summary.md`
3. Extend article lane to write both compatibility outputs and structured outputs.
4. Keep `article.md` public-facing section format stable.
5. Add optional placeholders for contradiction/mechanism files without making them hard requirements yet.

Verification:
- existing public artifact rendering still works
- article counts/metadata remain correct
- structured files are coherent with article.md

Rollback:
- keep renderer and downstream rail reading current markdown outputs until structured internals are proven

## 5. Phase 3: Validator layer in warn mode

Goal:
- introduce validators without immediately increasing fragility

Tasks:
1. Implement article validators:
   - completeness
   - duplicate/conflict
   - source-capture integrity
   - citation/linkage baseline
   - lineage baseline
2. Implement artifact publication validators:
   - alias integrity
   - kept-links integrity
   - RSS/feed integrity
3. Implement Daily validators:
   - included-article eligibility
   - artifact-publication-current
   - daily completeness
   - daily lineage baseline
   - public surface readiness
4. Write `validation.json` outputs.
5. Run validators in warn mode first.

Verification:
- validators produce usable signals on current known-good packages
- validators identify intentionally malformed test packages
- no blocking behavior yet on live rail

Rollback:
- disable validator enforcement, keep receipts for debugging only

## 6. Phase 4: Piter 2.0 control-plane implementation

Goal:
- create executive layer for watch, repair, intake, and view

Tasks:
1. Define Piter’s runtime entrypoints or commands for:
   - watch
   - repair
   - queue
   - view
2. Add repair receipt format and storage.
3. Add issue ledger / status note surface.
4. Add queue insertion workflow for operator-supplied links.
5. Add bounded repair workflow with verification and rollback notes.
6. Add recurring viewpoint output surface.

Verification:
- Piter can inspect current receipts and state
- Piter can queue supplied links correctly
- Piter can perform one bounded repair and emit receipt
- Piter can summarize current institute view from the rail

Rollback:
- Piter features are additive; disable repair actions if needed while preserving watch mode

## 7. Phase 5: Shadow publication targets

Goal:
- publish replacement rail outputs without touching live authoritative site

Tasks:
1. Define shadow publication root and config.
2. Add shadow kept-links and feeds.
3. Add shadow Daily latest/archive surfaces.
4. Ensure artifact and Daily rendering can target shadow root cleanly.
5. Add shadow-specific deployment path or static output target.
6. Add comparison receipts between live and shadow.

Verification:
- replacement rail can publish to shadow without mutating live
- shadow feeds parse correctly
- shadow pages render coherently

Rollback:
- shadow is non-authoritative, so simply stop publishing to it

## 8. Phase 6: Shadow proof window

Goal:
- prove the new Daily Rail is better in operation

Tasks:
1. Run shadow rail daily for several days.
2. Compare live vs shadow receipts, outputs, and reliability.
3. Record every failure and repair.
4. Tighten validators from warn -> block where justified.
5. Confirm Piter 2.0 can supervise the replacement effectively.

Verification:
- multiple successful shadow days
- no critical unresolved drift
- better auditability and repairability than live

Rollback:
- no cutover yet, so live remains authoritative

## 9. Phase 7: Cutover

Goal:
- replace live Daily Rail safely

Tasks:
1. Freeze cutover decision from comparison receipts.
2. Snapshot live config/state.
3. Switch authoritative publication target to replacement rail.
4. Keep old rail available as rollback path.
5. Monitor first post-cutover cycles closely.

Verification:
- first AM/artifact/PM cycles succeed after cutover
- feeds and site are correct
- receipts and Piter oversight remain healthy

Rollback:
- revert to old authoritative publication target and documented prior config

## 10. Exact implementation priorities

Priority 1:
- execution seam replacement

Priority 2:
- structured article internals

Priority 3:
- validators in warn mode

Priority 4:
- Piter 2.0 control plane

Priority 5:
- shadow publication

Priority 6:
- proof window and tightening

Priority 7:
- cutover

## 11. Suggested testing strategy

### Gold-path tests
- one imported blog article
- one imported paper article with remediation
- one duplicate candidate
- one discarded candidate
- one fully published artifact
- one full PM daily package

### Failure-path tests
- malformed Curator output
- malformed Conclave output
- broken source span refs
- missing structured file
- alias collision
- article not artifact-published before Daily

### Operational tests
- task runner timeout
- task runner backend failure
- Piter repair receipt creation
- shadow publication isolation from live

## 12. Definition of done before coding starts

Planning is complete enough to start building if these docs exist:
- current system map
- operations blueprint
- roadmap
- full implementation plan
- Piter 2.0 control-plane spec
- Daily Rail schema spec
- validator spec
- execution substrate spec
- shadow/cutover spec
- implementation task breakdown

That condition is now satisfied.

## 13. Bottom line

The safest build path is:
- swap the seam
- strengthen the bundle
- add validators
- add Piter
- prove in shadow
- cut over

That sequence preserves the working institute while making the replacement measurable, repairable, and governable.
