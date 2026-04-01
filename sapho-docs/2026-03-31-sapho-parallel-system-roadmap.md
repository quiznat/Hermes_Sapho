# Sapho Parallel System Roadmap

Status: revised
Date: 2026-03-31
Author: Hermes

## 1. Executive summary

Sapho already has a real Daily Rail.
The goal now is not to invent an institution from scratch. The goal is to replace and strengthen the existing Daily Rail without losing what already works.

The recommended path is:
- preserve the current live rail shape
- replace the OpenClaw execution seam
- strengthen internal artifact bundles
- add explicit validators
- introduce Piter 2.0 as executive control plane
- run the replacement in parallel on a shadow site and shadow RSS
- cut over only after proof that it is better

Important constraint:
Canon is off-limits for this phase.
We may prepare for future Canon by structuring bundles properly, but no Canon implementation or longform autonomous rail should be built until Daily Rail feature parity++ is achieved and proven.

## 1.1 Current build snapshot (updated 2026-04-01)

The build is ahead of the earlier written audit.

Current status by phase:
- Phase 0: done
- Phase 1: done
- Phase 2: largely done
- Phase 3: partially done
- Phase 4: not started in a meaningful production form
- Phase 5: not started
- Phase 6: not started

Concrete current state in `/home/hermes/sapho-native`:
- the provider-neutral task runner is active under the article lane
- bounded persona job contracts are wired for Curator admission, Extractor evidence, Synthesist claims, and Synthesist article writing
- bounded contradiction and mechanism review jobs are wired and materialized into article packages
- structured bundle outputs and `validation.json` are being generated
- tests are green
- validator enforcement is fail-closed for missing contradiction/mechanism surfaces

Important remaining truth:
- the forward lane is much more charter-shaped than before
- the historical package corpus is not yet fully brought up to the new standard
- shadow publication, proof-window comparison, and Piter 2.0 control-plane work remain ahead

## 2. What is working now

The live system already has:
- AM ingest and per-article processing
- abstract-only paper capture blocking and remediation
- duplicate rejection
- incremental kept artifact publication
- PM daily synthesis and Daily publication
- receipt surfaces and ops mirrors

That is enough to treat the Daily Rail as real production infrastructure.

## 3. What is strategically insufficient

### 3.1 The execution substrate is too coupled
The main remaining OpenClaw-specific seam is the disposable worker execution path through `openclaw_pocket_agent.py`.

### 3.2 The internal bundles are too compressed
Current bundles preserve enough for the Daily Rail, but not enough for strong lineage, future dossiering, or robust validation.

### 3.3 Repair and supervision are underpowered
The old setup lacked a true executive repair/control plane. Monitoring existed; repair authority and bounded intervention were too weak.

### 3.4 The replacement needs proof, not faith
The new system should not cut over because it feels cleaner. It should cut over only after surviving a real parallel proof period against the current live rail.

## 4. Guiding doctrine for this phase

1. One working path.
2. Preserve the split between artifact publication and Daily publication.
3. Preserve file-native canonical truth.
4. Make repair first-class.
5. Make receipts first-class.
6. Build shadow proof before cutover.
7. Keep Canon out of scope for now.

## 5. Target components for this phase

### Component A: Production Daily Rail
Responsibilities:
- source capture/import
- article conversion
- incremental artifact publication
- PM daily synthesis/publication

### Component B: Validation layer
Responsibilities:
- completeness
- duplicate/conflict checks
- citation/linkage checks
- lineage checks
- contradiction/mechanism baseline checks

### Component C: Piter 2.0 control plane
Responsibilities:
- monitor
- repair
- intake
- form view

### Component D: Shadow publication layer
Responsibilities:
- shadow site
- shadow RSS/artifacts feed
- live vs shadow comparison receipts

## 6. Where parallelism belongs in this phase

Safe parallelism:
- source capture across candidates
- per-article conversion across independent items
- artifact publication queueing one item at a time
- cluster note generation across PM clusters
- validator runs over frozen packages
- shadow and live running side by side

Unsafe parallelism:
- multiple writers on one mutable article package
- multiple writers on one Daily package
- free-form repair swarms
- Canon implementation in parallel with unfinished Daily Rail replacement

## 7. Roadmap phases

### Phase 0: Planning completion
Goal:
- finish all pre-coding specs

Deliverables:
- current-system map
- full implementation plan
- Piter 2.0 control-plane spec
- remaining technical specs

### Phase 1: Execution seam replacement
Status:
- completed

Goal:
- replace OpenClaw disposable worker dependency

Deliverable:
- provider-neutral task runner under the current micro rail

Current assessment:
- this is now implemented in `scripts/task_runner.py`
- the article lane defaults to the new runner
- rollback remains available through `SAPHO_USE_LEGACY_OPENCLAW=1`
- task receipts are being written under `state/receipts/task-runs/`

### Phase 2: Structured bundle hardening
Status:
- largely completed

Goal:
- preserve current public behavior while strengthening internals

Deliverable:
- claims/evidence/lineage/validation structure in article packages

Current assessment:
- the article lane now runs bounded Extractor evidence, bounded Synthesist claims, and bounded Synthesist article-write jobs
- contradiction and mechanism review artifacts are also being generated from bounded job surfaces
- structured package files are being materialized alongside compatibility markdown outputs
- the remaining gap is not basic wiring but migration/completeness across the historical corpus and any remaining compatibility-derived internals

### Phase 3: Validation-first Daily Rail
Status:
- partially completed

Goal:
- introduce explicit validators beneath current keep/pass gates

Deliverable:
- machine-checkable package trust layer

Current assessment:
- explicit validation is implemented and machine-checkable
- contradiction/mechanism absence now fails packages instead of being silently tolerated
- this phase is not finished because the validator has not yet been fully converted into the complete publication-authority layer and older packages still fail under the stronger law

### Phase 4: Shadow publication infrastructure
Status:
- not yet started in a meaningful production form

Goal:
- run the replacement rail in parallel to shadow surfaces

Deliverable:
- shadow site and shadow RSS/artifacts feed

Current assessment:
- this remains a real future milestone; no credible production shadow site/shadow RSS layer should be claimed yet

### Phase 5: Proof window
Status:
- not started

Goal:
- show the replacement is better in real operation

Deliverable:
- several days to one week of successful shadow runs

Current assessment:
- this cannot begin until shadow publication infrastructure exists and the comparison surface is trustworthy

### Phase 6: Cutover
Status:
- not started

Goal:
- make the replacement Daily Rail authoritative

Deliverable:
- controlled production cutover with rollback path

Current assessment:
- cutover remains premature until shadow proof, stronger operational comparison, and bounded repair confidence exist

## 8. What to keep, discard, and improve

### Keep
- current live Daily Rail topology
- incremental artifact publication
- PM-only Daily briefing publication
- paper full-text capture rule
- duplicate rejection
- file-native canonical truth
- fail-closed publication instinct

### Discard
- OpenClaw disposable worker dependence
- overreliance on prompt-only authority
- underdocumented repair behavior
- implicit executive oversight with no formal role contract

### Improve
- internal bundle structure
- validators
- repair receipts
- operator-facing executive control plane
- shadow-run comparability

## 9. Piter 2.0 in the roadmap

Piter 2.0 is part of this phase, not a later add-on.

Current status:
- not meaningfully implemented yet in `/home/hermes/sapho-native`

Why:
- the old system failed at turning oversight into reliable repair
- the new rail must be operable, not just executable
- shadow runs need executive comparison and intervention

Piter 2.0 should therefore be built alongside the replacement Daily Rail as:
- monitor
- repair operator
- queue inserter for operator-supplied material
- institute viewpoint layer

Near-term implication:
- the next Piter slice should be small and operationally real: monitor rail health, surface failures, propose bounded repairs, and emit receipts

## 10. Cutover doctrine

Do not cut over because the replacement is elegant.
Cut over because the replacement proves itself.

Minimum proof:
- feature parity with the live rail
- stronger receipts and repairability
- successful shadow site/shadow RSS operation for multiple days
- no hidden dependence on the old OpenClaw worker substrate
- operator confidence that Piter 2.0 can repair bounded failures

## 11. Bottom line

The mission for this phase is not to build the whole future institute.
It is to replace and strengthen the Daily Rail so thoroughly that it can safely become the institute’s new production core.

If we do this well, Canon becomes possible later.
If we skip this step, Canon will be built on weak operational footing.
