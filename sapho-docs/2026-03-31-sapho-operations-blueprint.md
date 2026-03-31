# Sapho Operations Blueprint

Status: revised
Date: 2026-03-31
Author: Hermes
Purpose: translate the current working Daily Rail and charter into a concrete operating scaffold for the replacement system in this phase.

## 1. Scope for this phase

This blueprint is for the Daily Rail replacement only.

In scope:
- source capture/import
- article conversion
- incremental artifact publication
- PM daily synthesis/publication
- validators
- Piter 2.0 control plane
- shadow site/shadow RSS proof

Out of scope:
- Canon implementation
- autonomous longform paper production

Future Canon is prepared for only by choosing good internal bundle structure now.

## 2. Core principle

Sapho in this phase is a governed Daily institution with:
- a file-native production rail
- a validation layer
- an executive control plane
- a shadow proof layer

The public system must remain fail-closed.
The replacement system must prove itself before cutover.

## 3. Canonical package layout for this phase

Recommended top-level shape:
- `research/sources/<source_id>/`
- `research/articles/<article_id>/`
- `research/publication/artifacts/<alias-or-article-id>/`
- `research/publication/daily/<date>/`
- `research/receipts/<run-id>/`
- `research/contracts/`
- `research/status/`
- `research/shadow/` or equivalent shadow publication root

## 4. Source package contract

Files:
- `source.md`
- `capture.json`
- `raw.md` or `raw.txt`
- `provenance.json`

Required fields:
- `source_id`
- `source_url`
- `canonical_url`
- `source_type`
- `captured_at_utc`
- `capture_status`
- `capture_kind`
- `content_hash`

## 5. Article package contract

Files:
- compatibility files:
  - `article.md`
  - `source.md`
  - `micro-worthiness.md`
  - `micro-findings.md`
  - `micro-facts.md`
  - `micro-summary.md`
- strengthened internals:
  - `claims.jsonl`
  - `evidence.jsonl`
  - `lineage.json`
  - `validation.json`
  - optional `contradictions.jsonl`
  - optional `mechanisms.jsonl`

Required fields in frontmatter:
- `article_id`
- `source_url`
- `canonical_url`
- `source_title`
- `curator_decision`
- `artifact_minted_at_utc`
- `publication_status`
- `evidence_count`
- `claim_count`

## 6. Artifact publication contract

Artifact publication remains separate from Daily publication.

Artifact publication fields:
- `artifact_publication_status`
- `artifact_publication_alias`
- `artifact_publication_minted_at_utc`
- `artifact_publication_published_at_utc`

Artifact surfaces:
- kept-links
- artifact markdown pages
- alias redirects
- rss.xml
- artifacts.xml

## 7. Daily package contract

Files:
- `cluster-ledger.json`
- `technical-executive-report.md`
- `executive-brief.md`
- `conclave.md`
- `conclave.json`
- `publish.md`
- `lineage.json`
- `validation.json`

Required fields:
- `date`
- `included_article_ids`
- `generated_at_utc`
- `verdict`
- `status`

## 8. State machine

### Source states
- discovered
- captured
- capture_blocked
- retained
- discarded

### Article states
- pending
- capture_blocked
- discarded
- duplicate_rejected
- ready_for_daily
- published

### Artifact-publication states
- unpublished
- published

### Daily package states
- draft
- blocked
- published

Rule:
one owner stage mutates a package at a time, and every meaningful mutation should leave a receipt.

## 9. Role-to-stage mapping for this phase

### Curator
- keep/discard decision
- novelty and evidence worthiness gate

### Extractor
- findings
- facts
- evidence objects
- claim objects if split from findings

### Synthesist
- article summary
- cluster notes
- technical daily
- executive daily

### Conclave
- final Daily pass/block judgment on a frozen package
- should increasingly rely on validator outputs

### Piter 2.0
- watch
- repair
- intake
- view

Piter 2.0 is not part of normal throughput.

## 10. Daily Rail runbook

### Stage D1: backlog selection/import
Select candidate sources or import runtime backlog truth.
Emit:
- selection receipt
- source/article/ticket creation where needed

### Stage D2: article conversion
Per article:
- source capture/remediation
- curator gate
- duplicate gate
- findings
- facts
- summary
- internal structured bundle files

Parallelism:
- yes, one article at a time per worker

### Stage D3: artifact publication
For each article ready for artifact publication:
- assign/reuse alias
- generate artifact surfaces
- update kept-links and feeds
- emit receipt

Parallelism:
- serial or tightly controlled one-at-a-time, as today

### Stage D4: PM synthesis
For the day:
- collect eligible articles
- build cluster ledger
- build technical and executive outputs
- run validators
- run Conclave

### Stage D5: Daily publication
If pass:
- mark articles published in Daily
- render and deploy daily surfaces
- emit receipt
If block:
- preserve blocked package and reason

## 11. Piter 2.0 runbook

### Watch
- inspect receipts, logs, state, public/shadow surfaces
- classify green/watch/blocked

### Repair
- patch bounded failures
- rerun bounded steps
- verify and emit repair receipt

### Intake
- insert operator-supplied links/material into the queue cleanly

### View
- produce viewpoint and direction from observed patterns

## 12. Validation contracts for this phase

### Contract A: completeness
Checks:
- required package files exist
- required frontmatter keys exist
- included article references resolve

### Contract B: duplicate/conflict
Checks:
- canonical conflict or duplicate signatures are not silently entering kept/publication paths

### Contract C: citation/linkage
Checks:
- source URL and canonical URL exist and are coherent
- artifact aliases and public links resolve cleanly

### Contract D: lineage baseline
Checks:
- summary claims have corresponding findings/facts/evidence records

### Contract E: contradiction/mechanism baseline
Checks:
- packages expose placeholders or notes where contradiction/mechanism handling is expected

These validators do not need full future sophistication yet; they need to be operationally useful now.

## 13. Shadow proof design

The replacement rail should publish to:
- a shadow site root
- a shadow RSS/artifacts feed

The shadow stack should support comparison of:
- article bundle counts
- artifact publication timing
- PM publication timing
- public output coherence
- validator results
- repair frequency and repair success

Cutover should not happen before a multi-day shadow proof window.

## 14. Success criteria for this phase

The phase is successful when:
- the replacement Daily Rail matches current production capability
- artifact bundles are more structured
- Piter 2.0 can monitor and repair the rail effectively
- shadow outputs prove the replacement is better
- cutover can happen with rollback confidence

## 15. Bottom line

For this phase, Sapho should be built as a stronger Daily institution first.
That means:
- better bundles
- better validators
- better executive repair/control
- better proof discipline

Canon can wait.
The right foundation cannot.
