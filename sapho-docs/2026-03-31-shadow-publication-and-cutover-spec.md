# Shadow Publication and Cutover Spec

Status: draft
Date: 2026-03-31
Author: Hermes
Purpose: define how the replacement Daily Rail should run in parallel on shadow surfaces, how it should be compared to live production, and what criteria govern cutover and rollback.

## 1. Objective

Before replacing the current live Daily Rail, the new rail must prove itself in real operation.

That proof must happen by publishing the replacement system to shadow surfaces for multiple days while the current live system remains authoritative.

The goal is to compare institutions in operation, not just scripts in isolation.

## 2. Scope

In scope:
- shadow site
- shadow kept-links
- shadow RSS/artifacts feed
- shadow Daily surfaces
- comparison receipts
- proof window
- cutover criteria
- rollback doctrine

Out of scope:
- Canon shadowing
- longform comparison

## 3. Core shadow principle

The shadow system should be as close as possible to real production behavior while remaining non-authoritative.

That means:
- same inputs whenever possible
- same production logic class
- same package/validator rules
- different publication target

The shadow system should not be a toy replay.
It should be a live parallel institution under test.

## 4. Shadow publication targets

The replacement rail should publish to a separate shadow root.

Minimum surfaces:
- shadow home/index
- shadow kept-links page and JSON
- shadow artifact pages
- shadow RSS/artifacts feed
- shadow Daily latest page
- shadow Daily archive surfaces
- shadow briefs latest/meta surfaces

Suggested naming:
- separate directory root or separate domain/subdomain
- separate `rss.xml` and `artifacts.xml`

Rule:
Shadow publication must not mutate the live authoritative site during proof.

## 5. Shadow operating modes

### Mode A: dry shadow
- render internally
- no external shadow surface
Useful for very early debugging only.

### Mode B: private shadow
- publish to an internal or non-publicly linked shadow target
- recommended first real proof mode

### Mode C: full shadow
- publicly reachable but clearly non-authoritative shadow environment
- appropriate for later proof if useful

Recommended sequence:
- start with private shadow
- move to full shadow only if needed

## 6. Shadow input policy

Preferred policy:
- shadow rail uses the same backlog/source inputs as live production on the same dates
- operator-supplied queue insertions should be mirrored or explicitly tagged for shadow comparison

This ensures meaningful comparison.

If exact same inputs cannot be used, the comparison becomes weaker and must be annotated accordingly.

## 7. Shadow comparison dimensions

The system should compare live vs shadow on at least these dimensions.

### 7.1 Reliability
- did AM run complete
- did artifact publication run complete
- did PM run complete
- did any blocking failures occur
- were repairs required

### 7.2 Throughput parity
- number of included articles per day
- number of artifacts published
- timing of artifact publication
- Daily package generation success

### 7.3 Content quality
- article bundle completeness
- public artifact coherence
- technical brief coherence
- executive brief coherence
- visible trustworthiness and specificity

### 7.4 Evidence quality
- structured bundle richness
- lineage coverage
- citation/linkage integrity
- contradiction/mechanism baseline coverage

### 7.5 Repairability
- time to diagnose issues
- time to patch issues
- verification quality
- rollback safety

### 7.6 Executive operability
- can Piter 2.0 understand the state quickly
- can Piter 2.0 repair bounded failures
- can Piter 2.0 compare shadow and live meaningfully

## 8. Required comparison receipts

Every proof-day should produce a comparison receipt containing at minimum:
- `date`
- `live_status`
- `shadow_status`
- `live_receipt_refs`
- `shadow_receipt_refs`
- `artifact_count_live`
- `artifact_count_shadow`
- `daily_status_live`
- `daily_status_shadow`
- `major_differences[]`
- `repairs_performed[]`
- `operator_attention_needed`
- `recommendation`: `continue_shadow | investigate | ready_for_cutover | do_not_cutover`

This receipt is the central decision object during the proof window.

## 9. Proof window

Recommended proof duration:
- several consecutive days to one week

The proof window should include:
- at least one normal healthy day
- at least one day with operator-supplied queue insertions if possible
- ideally at least one day where a non-trivial repair is needed and successfully handled in shadow

Why:
A replacement that only succeeds on perfect days is not ready.

## 10. Daily proof review questions

Each proof day should answer:
1. Did shadow complete all Daily Rail stages?
2. Did shadow preserve the live publication split correctly?
3. Did structured bundles materially improve auditability?
4. Did validators catch anything useful?
5. Did Piter 2.0 successfully monitor and intervene where needed?
6. Was shadow as good as or better than live on trustworthiness?
7. Is there any reason this shadow should not become live?

## 11. Cutover criteria

Cutover should require all of the following.

### 11.1 Functional parity
- AM ingest parity
- paper capture/remediation parity
- duplicate handling parity
- artifact publication parity
- PM synthesis/publication parity

### 11.2 Reliability parity or better
- no critical unhandled failures during proof window
- receipts and operational mirrors are complete
- shadow does not require constant manual babysitting

### 11.3 Bundle quality improvement
- internal structured bundles are materially better than live
- validators are producing useful operational signal

### 11.4 Piter 2.0 viability
- Piter can monitor the replacement rail
- Piter can repair bounded failures
- Piter can queue operator-supplied items cleanly
- Piter can form a meaningful view from the proof period

### 11.5 Rollback confidence
- there is a known rollback path
- rollback has been dry-run or otherwise validated

## 12. Cutover procedure

Recommended cutover sequence:
1. freeze cutover date and target window
2. confirm latest shadow comparison receipt recommends cutover
3. confirm no unresolved critical validator or repair issues
4. snapshot current live publication state and config
5. switch authoritative publication target from old live rail to replacement rail
6. keep old system available for rollback but non-authoritative
7. monitor first post-cutover cycles closely with Piter 2.0

## 13. Rollback doctrine

Rollback should be possible quickly if any of the following happen:
- critical publication corruption
- repeated unhandled failures
- validator layer producing false confidence
- artifact publication drift or broken feeds
- Piter unable to repair the replacement rail in bounded time

Rollback requirements:
- preserve old live system until proof is complete and cutover confidence is high
- keep environment-specific publication paths reversible
- keep a clear record of what changed at cutover

Rollback is not failure of the mission.
Rollback is proof that the institution is fail-closed.

## 14. Shadow-specific Piter 2.0 duties

During proof, Piter 2.0 should:
- monitor live and shadow
- compare outputs and receipts
- repair shadow first when possible
- keep a running issue ledger
- produce a recurring executive viewpoint on whether shadow is truly better

This is essential because shadow proof is not only testing the Daily Rail replacement.
It is also testing the executive control plane.

## 15. Success definition

The shadow phase succeeds when:
- the replacement rail consistently completes Daily operations
- public shadow outputs are coherent
- internal bundles are stronger than live
- Piter 2.0 can supervise and repair it effectively
- the comparison receipts make cutover the obvious decision rather than a gamble

## 16. Anti-goals

Do not:
- cut over because the replacement code feels cleaner
- treat one successful replay as proof
- mix Canon proof into Daily replacement proof
- let shadow mutate live authoritative surfaces accidentally

## 17. Bottom line

Shadow publication is the institutional proof mechanism for the Daily Rail replacement.

The replacement becomes real not when it exists, but when it can survive several days of parallel operation, produce better bundles and better repairability, and make cutover a conservative choice rather than a leap of faith.
