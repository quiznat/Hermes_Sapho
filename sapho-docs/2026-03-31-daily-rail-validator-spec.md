# Daily Rail Validator Spec

Status: draft
Date: 2026-03-31
Author: Hermes
Purpose: define the validator layer for the Daily Rail replacement.

## 1. Scope

This validator spec is for the Daily Rail phase only.

In scope:
- article package validators
- artifact publication validators
- Daily package validators
- repair-oriented validation behavior

Out of scope:
- deep Canon/longform scholarly validation

## 2. Validator philosophy

Validators exist to make institutional law operational.
They are not cosmetic lint.
They should:
- catch malformed or untrustworthy packages early
- produce explicit pass/warn/fail results
- support repair and rollback
- block weak publication when necessary

Rule:
Conclave may add judgment and rationale, but validators establish the minimum legal substrate.

## 3. Result model

Each validator returns:
- `name`
- `scope`
- `status`: `pass | warn | fail`
- `summary`
- `details`
- `blocking`: `true | false`
- `repair_hint` optional

Interpretation:
- `pass`: requirement satisfied
- `warn`: package usable but degraded; not necessarily blocking
- `fail`: requirement not satisfied
- `blocking=true`: package may not advance automatically

## 4. Validator groups

### Group A: Article package validators
1. completeness
2. duplicate/conflict
3. source-capture integrity
4. citation/linkage baseline
5. lineage baseline
6. contradiction baseline
7. mechanism baseline

### Group B: Artifact publication validators
1. artifact alias integrity
2. kept-links surface integrity
3. RSS/artifacts feed integrity
4. publication state synchronization

### Group C: Daily package validators
1. included-article eligibility
2. artifact-publication-current
3. daily package completeness
4. daily lineage baseline
5. daily citation/linkage baseline
6. daily contradiction baseline
7. daily mechanism baseline
8. public surface readiness

## 5. Article validators

## 5.1 Completeness validator
Scope:
- one article package

Checks:
- required files exist:
  - `article.md`
  - `source.md`
  - `curator.json`
  - `findings.jsonl`
  - `facts.jsonl`
  - `claims.jsonl`
  - `evidence.jsonl`
  - `lineage.json`
  - `validation.json` may be absent while generating but must exist before package completion
- required frontmatter keys exist in `article.md`
- counts in metadata are coherent with structured file counts

Fail examples:
- missing `claims.jsonl`
- `claim_count=4` but only 2 claim records exist

Blocking:
- yes

## 5.2 Duplicate/conflict validator
Scope:
- one article package against existing kept/published packages

Checks:
- canonical URL conflict against existing kept/published records
- source identity signature conflict where relevant
- duplicate-rejected packages are not advancing further

Fail examples:
- two kept articles share same canonical work without explicit aliasing policy

Blocking:
- yes

## 5.3 Source-capture integrity validator
Scope:
- one article package and linked source package

Checks:
- source capture exists and is readable
- paper-like sources are not abstract-only when marked captured
- `capture-blocked` items are not treated as publishable
- remediation state is coherent

Fail examples:
- paper source with only abstract text and no introduction/body capture
- article marked `ready-for-daily` but source package still signals full-text remediation needed

Blocking:
- yes

## 5.4 Citation/linkage baseline validator
Scope:
- one article package

Checks:
- `source_url` exists
- `canonical_url` exists
- every `source_span_ref` in claims/facts/evidence resolves to a valid span definition or valid source reference convention
- article/source ids are coherent across files

Warn examples:
- non-critical missing secondary linked-paper urls

Fail examples:
- claims refer to nonexistent span refs
- source/canonical URLs missing

Blocking:
- yes

## 5.5 Lineage baseline validator
Scope:
- one article package

Checks:
- every top-line article section maps to claim ids in `lineage.json`
- every cited claim id exists in `claims.jsonl`
- every claim has at least one supporting fact or evidence id
- every supporting fact/evidence id exists

Warn examples:
- one low-priority section has thin support but not zero support

Fail examples:
- `Core Thesis` has no mapped claim ids
- claim exists with no support

Blocking:
- yes

## 5.6 Contradiction baseline validator
Scope:
- one article package

Checks:
- if contradictions are known, they are at least surfaced in placeholder form
- if no contradiction file exists, `validation.json` or package metadata explicitly notes absence

This is intentionally modest in this phase.
It is a baseline, not a full contradiction engine.

Warn examples:
- contradiction placeholder absent but article is otherwise usable

Fail examples:
- package makes strong comparative claims while contradiction notes are explicitly missing and validator policy requires them

Blocking:
- warn by default in this phase, fail only on clear policy-sensitive cases

## 5.7 Mechanism baseline validator
Scope:
- one article package

Checks:
- major explanatory claims are either:
  - tagged as mechanism claims and supported, or
  - bounded as uncertain/non-mechanistic
- if `mechanisms.jsonl` absent, package exposes that no explicit mechanism object was produced

Warn examples:
- article contains implications but no explicit mechanism object

Fail examples:
- article presents unsupported causal explanation as settled mechanism

Blocking:
- warn by default in this phase, fail for egregious unsupported causal framing

## 6. Artifact publication validators

## 6.1 Artifact alias integrity validator
Scope:
- one artifact publication event

Checks:
- alias exists and is unique
- alias format valid
- alias-source mapping stable
- no collision with different source identity

Blocking:
- yes

## 6.2 Kept-links surface validator
Scope:
- artifact publication surfaces

Checks:
- new item appears in kept-links payload and page
- item title/link/source link coherent
- no malformed HTML/JSON output

Blocking:
- yes

## 6.3 RSS/artifacts feed validator
Scope:
- rss.xml / artifacts.xml / artifacts-feed.json

Checks:
- feed parses
- new item identity coherent
- no duplicate source under conflicting links
- pubDate valid
- source URL extracted correctly

Blocking:
- yes

## 6.4 Publication state synchronization validator
Scope:
- article package + artifact publication receipt + public surfaces

Checks:
- article metadata reflects artifact publication fields after publication
- public surfaces reflect same alias/article

Blocking:
- yes

## 7. Daily package validators

## 7.1 Included-article eligibility validator
Scope:
- Daily package article set

Checks:
- every included article is in correct state for the date
- no discarded/capture-blocked/duplicate-rejected article is included
- date eligibility matches policy

Blocking:
- yes

## 7.2 Artifact-publication-current validator
Scope:
- Daily package article set

Checks:
- every included article already has current artifact publication

This preserves an important live policy already encoded today.

Blocking:
- yes

## 7.3 Daily package completeness validator
Scope:
- daily package directory

Checks:
- required files exist:
  - `cluster-ledger.json`
  - `technical-executive-report.md`
  - `executive-brief.md`
  - `conclave.md`
  - `conclave.json`
  - `publish.md`
  - `lineage.json`
  - `validation.json`
- required metadata fields present
- included article ids listed consistently

Blocking:
- yes

## 7.4 Daily lineage baseline validator
Scope:
- Daily package

Checks:
- top-line technical and executive judgments map back to article/package claims
- `lineage.json` references valid claim ids and included article ids

Blocking:
- yes

## 7.5 Daily citation/linkage baseline validator
Scope:
- Daily package

Checks:
- included article references resolve
- article canonical/source links coherent
- no broken package references in generated surfaces

Blocking:
- yes

## 7.6 Daily contradiction baseline validator
Scope:
- Daily package

Checks:
- if included articles carry known contradiction notes relevant to synthesis, package either:
  - surfaces them, or
  - explicitly omits them with note

Blocking:
- warn by default in this phase

## 7.7 Daily mechanism baseline validator
Scope:
- Daily package

Checks:
- major causal/explanatory claims in daily outputs are either supported by included article mechanism support or explicitly bounded

Blocking:
- warn by default in this phase, fail for obviously overclaimed causal language

## 7.8 Public surface readiness validator
Scope:
- daily publication surfaces

Checks:
- rendered daily pages exist
- latest pointers exist and resolve
- archive surfaces update coherently

Blocking:
- yes for publish completion

## 8. Overall blocking policy

### Article progression block policy
Block article progression when any of these fail:
- completeness
n- duplicate/conflict
- source-capture integrity
- citation/linkage baseline
- lineage baseline

Warn-only by default in this phase:
- contradiction baseline
- mechanism baseline

### Daily publication block policy
Block Daily publication when any of these fail:
- included-article eligibility
- artifact-publication-current
- daily package completeness
- daily lineage baseline
- daily citation/linkage baseline
- public surface readiness

Warn-only by default in this phase:
- daily contradiction baseline
- daily mechanism baseline

## 9. Repair integration

Validators are not only gates; they are repair hooks.

Every validator failure should expose:
- failing object
- exact failing check
- human-readable summary
- machine-readable details
- suggested repair hint where possible

Example repair hints:
- `missing_file:claims.jsonl`
- `artifact_alias_conflict`
- `article_not_artifact_published`
- `source_span_ref_missing`
- `paper_capture_abstract_only`

This is especially important for Piter 2.0 repair mode.

## 10. Validation timing

### During article conversion
Run:
- source-capture integrity
- duplicate/conflict
- article completeness (partial)
- citation/linkage baseline
- lineage baseline once claims/evidence exist

### Before artifact publication
Run:
- article completeness
- duplicate/conflict
- citation/linkage baseline
- artifact alias integrity if alias prepared

### Before Daily Conclave
Run:
- included-article eligibility
- artifact-publication-current
- daily package completeness
- daily lineage baseline
- daily citation/linkage baseline
- contradiction/mechanism baseline

### After publication
Run:
- public surface readiness
- synchronization checks

## 11. Validator outputs in files

Recommended storage:
- article validators write/refresh `validation.json` in article package
- Daily validators write/refresh `validation.json` in daily package
- major publication events also produce receipts in receipts directory

Suggested `validation.json` structure:
- `version`
- `scope`
- `validated_at_utc`
- `overall_status`
- `checks[]`

Where each `checks[]` element contains:
- `name`
- `status`
- `blocking`
- `summary`
- `details`
- `repair_hint`

## 12. Relationship to Conclave

Conclave should consume validator output.
It should not replace validator output.

In this phase:
- validators establish minimum legal and structural trust
- Conclave adds judgment, coherence review, and publication rationale

Therefore a package can fail before Conclave if validators fail.
And a package can still be blocked by Conclave even if validators pass, if the package is incoherent or visibly untrustworthy.

## 13. Minimum validator set for shadow proof

Before shadow proof begins, the replacement rail should at minimum implement:
- article completeness
- duplicate/conflict
- source-capture integrity
- citation/linkage baseline
- lineage baseline
- artifact alias integrity
- RSS/feed integrity
- included-article eligibility
- artifact-publication-current
- daily package completeness
- public surface readiness

This minimum set is enough to make shadow comparison meaningful.

## 14. Bottom line

The validator layer is what turns the Daily Rail from a prompt-guided workflow into a governed institution.

For this phase, validators do not need to be philosophically complete.
They need to be operationally decisive, repair-friendly, and strong enough to support shadow proof and cutover with confidence.
