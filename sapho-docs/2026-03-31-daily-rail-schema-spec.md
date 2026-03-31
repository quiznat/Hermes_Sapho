# Daily Rail Schema Spec

Status: draft
Date: 2026-03-31
Author: Hermes
Purpose: define the canonical schemas for the Daily Rail replacement, including upgraded persona output contracts.

## 1. Scope

This spec covers only the Daily Rail phase.

In scope:
- source package schema
- queue/ticket schema
- article package schema
- artifact publication schema
- daily package schema
- receipt schema
- upgraded persona output schemas

Out of scope:
- Canon package schemas beyond optional placeholders
- longform-specific objects

## 2. Design principles

1. Preserve file-native truth.
2. Keep compatibility with the current working public surfaces.
3. Separate internal structured state from public prose.
4. Make every important decision validator-friendly.
5. Leave enough structure to support future dossiers later without implementing Canon now.

## 3. Format conventions

Human-facing canonical files:
- Markdown with YAML frontmatter where public readability matters

Machine-facing canonical files:
- JSON or JSONL for structured objects

Recommended conventions:
- one package directory per primary object
- one JSONL record type per file
- stable ids everywhere
- UTC timestamps in ISO8601 with `Z`

## 4. IDs

### 4.1 Source ID
Format:
- `src-YYYY-MM-DD-XXX` or a stable hash-based variant

### 4.2 Ticket ID
Format:
- `ticket-...`
- imported runtime tickets may preserve existing compatibility shape

### 4.3 Article ID
Format:
- preserve current style where possible, e.g. `art-2026-03-04-034`

### 4.4 Claim ID
Format:
- `clm-<article-id>-NNN`

### 4.5 Evidence ID
Format:
- `evd-<article-id>-NNN`

### 4.6 Fact ID
Format:
- `fact-<article-id>-NNN`

### 4.7 Daily package ID
Format:
- `daily-YYYY-MM-DD`

### 4.8 Receipt ID
Format:
- `<job-or-mode>-YYYYMMDDTHHMMSSZ-<suffix>`

## 5. Source package schema

Path:
- `research/sources/<source_id>/`

Files:
- `source.md`
- `capture.json`
- `raw.md` or `raw.txt`
- `provenance.json`

### 5.1 `capture.json`
Required fields:
- `version`
- `source_id`
- `source_url`
- `canonical_url`
- `source_type`
- `capture_status`
- `capture_kind`
- `content_type`
- `http_status`
- `captured_at_utc`
- `content_hash`
- `title`

Optional fields:
- `linked_paper_urls`
- `redirect_chain`
- `source_capture_gate_reason`
- `source_remediation_required`
- `source_remediation_status`
- `source_remediated_at_utc`
- `notes`

Enumerations:
- `capture_status`: `captured | capture_blocked | error`
- `source_type`: `paper | blog | benchmark | repo | docs | unknown`

### 5.2 `source.md`
Purpose:
- readable custody file for operators and debugging

Required frontmatter:
- `version`
- `source_id`
- `article_id` if already linked
- `source_url`
- `canonical_url`
- `source_title`
- `capture_kind`
- `http_status`
- `content_type`
- `captured_at_utc`

Body sections:
- `# Source Capture`
- `## Title`
- `## Body`
- optional `## Import Provenance`

## 6. Queue/ticket schema

Path:
- `queue/<ticket_id>.md`

Required frontmatter:
- `version`
- `ticket_id`
- `source_url`
- `canonical_url`
- `source_channel`
- `queued_at_utc`
- `status`
- `article_id`

Optional fields:
- `selection_source`
- `duplicate_of_article_id`
- `duplicate_match_signature`
- `source_capture_gate_reason`
- `operator_supplied`
- `operator_note`
- `priority`
- `labels`

Enumerations:
- `status`: `queued | captured | discarded | capture-blocked | duplicate-rejected | kept`

## 7. Article package schema

Path:
- `research/articles/<article_id>/`

Files:
- compatibility/public files:
  - `article.md`
  - `source.md`
  - `micro-worthiness.md`
  - `micro-findings.md`
  - `micro-facts.md`
  - `micro-summary.md`
- structured internal files:
  - `curator.json`
  - `findings.jsonl`
  - `facts.jsonl`
  - `claims.jsonl`
  - `evidence.jsonl`
  - `lineage.json`
  - `validation.json`
  - optional `contradictions.jsonl`
  - optional `mechanisms.jsonl`

### 7.1 `article.md`
Purpose:
- public-facing article artifact draft plus minimal routing metadata

Required frontmatter:
- `version`
- `article_id`
- `ticket_id`
- `source_id` if available
- `source_url`
- `canonical_url`
- `source_title`
- `queued_at_utc`
- `captured_at_utc`
- `curator_decision`
- `curated_at_utc`
- `artifact_minted_at_utc`
- `publication_status`
- `evidence_count`
- `claim_count`
- `extractor_mode`
- `findings_mode`
- `summary_mode`

Optional frontmatter:
- `contradiction_count`
- `mechanism_count`
- `duplicate_of_article_id`
- `duplicate_match_signature`
- `artifact_publication_alias`
- `artifact_publication_status`
- `artifact_publication_minted_at_utc`
- `artifact_publication_published_at_utc`
- `published_in_daily`
- `source_capture_gate_reason`
- `source_remediation_required`
- `source_remediation_status`
- `imported_from_runtime_article_id`
- `imported_from_runtime_last_stage`
- `imported_from_runtime_filter_state`

Enumerations:
- `curator_decision`: `pending | kept | discarded`
- `publication_status`: `pending | capture-blocked | discarded | duplicate-rejected | ready-for-daily | published`

Required body sections:
- `# <title>`
- `## Core Thesis`
- `## Why It Matters`
- `## Key Findings`
- `## Limits`

Optional section:
- `## Evidence Base`

### 7.2 `curator.json`
Purpose:
- structured Curator decision object

Required fields:
- `version`
- `article_id`
- `decision`
- `qualified_by`
- `evidence_basis`
- `novelty_strength`
- `excerpt_sufficiency`
- `reason`
- `limits`
- `confidence`
- `generated_at_utc`
- `mode`

Enumerations:
- `decision`: `kept | discarded`
- `qualified_by`: `novel_synthesis | novel_findings | experimental_blog | production_blog | comparative_survey | vendor_technical_results | none`
- `evidence_basis`: `benchmark | experiment | production | synthesis | mixed | none`
- `novelty_strength`: `low | medium | high`
- `excerpt_sufficiency`: `sufficient | partial | insufficient`
- `confidence`: `low | medium | high`

### 7.3 `findings.jsonl`
Purpose:
- top-line findings as typed records

Each record required fields:
- `finding_id`
- `article_id`
- `finding_text`
- `finding_type`
- `priority`
- `source_span_ref`
- `confidence`

Enumerations:
- `finding_type`: `result | implication | caveat | mechanism_hint`
- `priority`: `high | medium | low`
- `confidence`: `low | medium | high`

### 7.4 `facts.jsonl`
Purpose:
- atomic factual extractions

Each record required fields:
- `fact_id`
- `article_id`
- `fact_text`
- `fact_type`
- `metric_value` nullable
- `metric_unit` nullable
- `source_span_ref`
- `confidence`
- `caveat` nullable

Enumerations:
- `fact_type`: `benchmark_result | experiment_result | production_observation | methodological_detail | model_detail | dataset_detail | caveat | quote_fact | other`
- `confidence`: `low | medium | high`

### 7.5 `claims.jsonl`
Purpose:
- article-level claims derived from findings/facts

Each record required fields:
- `claim_id`
- `article_id`
- `claim_text`
- `claim_kind`
- `supporting_fact_ids`
- `supporting_evidence_ids`
- `source_span_refs`
- `caveats`
- `confidence`

Enumerations:
- `claim_kind`: `topline_judgment | empirical_claim | comparative_claim | mechanism_claim | implication_claim | limitation_claim`
- `confidence`: `low | medium | high`

### 7.6 `evidence.jsonl`
Purpose:
- evidence units tied closely to source spans

Each record required fields:
- `evidence_id`
- `article_id`
- `evidence_type`
- `evidence_text`
- `source_span_ref`
- `supports_claim_ids`
- `confidence`

Enumerations:
- `evidence_type`: `quote | metric | method | result | comparison | caveat`
- `confidence`: `low | medium | high`

### 7.7 `lineage.json`
Purpose:
- explicit summary of article-level lineage

Required fields:
- `version`
- `article_id`
- `summary_sections`
- `claim_ids`
- `fact_ids`
- `evidence_ids`
- `unresolved_gaps`

`summary_sections` should map section names like:
- `core_thesis`
- `why_it_matters`
- `key_findings`
- `limits`

to referenced claim ids.

### 7.8 `validation.json`
Purpose:
- validator results on the article package

Required fields:
- `version`
- `article_id`
- `validated_at_utc`
- `checks`
- `overall_status`

`checks` should contain named results for:
- completeness
- duplicate_conflict
- citation_linkage
- lineage_baseline
- contradiction_baseline
- mechanism_baseline

Enumerations:
- `overall_status`: `pass | warn | fail`

## 8. Artifact publication schema

Artifact publication is separate from Daily publication.

Path options:
- public site surfaces as today
- optional internal receipt directory such as `research/publication/artifacts/<alias-or-article-id>/`

### 8.1 Artifact publication receipt
Required fields:
- `version`
- `article_id`
- `artifact_publication_alias`
- `published_at_utc`
- `minted_at_utc`
- `artifact_rel`
- `source_rel`
- `rss_updated`
- `kept_links_updated`
- `status`

Enumerations:
- `status`: `published | skipped | failed`

## 9. Daily package schema

Path:
- `research/publication/daily/<date>/`

Files:
- `cluster-ledger.json`
- `technical-executive-report.md`
- `executive-brief.md`
- `daily.md`
- `conclave.md`
- `conclave.json`
- `publish.md`
- `lineage.json`
- `validation.json`

### 9.1 `cluster-ledger.json`
Required fields:
- `version`
- `date`
- `generated_at_utc`
- `cluster_count`
- `clusters`

Each cluster required fields:
- `cluster_id`
- `article_ids`
- `theme`
- `cluster_note_path`

### 9.2 `technical-executive-report.md`
Required frontmatter:
- `version`
- `date`
- `generated_at_utc`
- `mode`
- `status`
- `included_article_ids`

### 9.3 `executive-brief.md`
Required frontmatter:
- `version`
- `date`
- `generated_at_utc`
- `mode`
- `status`
- `included_article_ids`

### 9.4 `conclave.json`
Purpose:
- structured Conclave verdict

Required fields:
- `version`
- `date`
- `generated_at_utc`
- `verdict`
- `lineage_check`
- `contradiction_check`
- `mechanism_check`
- `citation_check`
- `completeness_check`
- `rationale`
- `remediation_items`

Enumerations for each check:
- `pass | warn | fail`

Verdict enumeration:
- `pass | block`

### 9.5 `lineage.json` for Daily
Purpose:
- tie top-line Daily judgments back to article/package claims

Required fields:
- `version`
- `date`
- `technical_claim_refs`
- `executive_claim_refs`
- `included_article_ids`

### 9.6 `validation.json` for Daily
Required fields:
- `version`
- `date`
- `validated_at_utc`
- `checks`
- `overall_status`

Checks should include:
- package_completeness
- included_article_state
- artifact_publication_current
- citation_linkage
- lineage_baseline
- contradiction_baseline
- mechanism_baseline

## 10. Receipt schema

Path:
- `research/receipts/` or existing runtime receipt paths

All receipts should include:
- `receipt_id`
- `job_or_mode`
- `generated_at_utc`
- `status`
- `command_or_action`
- `summary`
- `details`

Enumerations:
- `status`: `ok | warn | error | blocked | skipped`

## 11. Upgraded persona output contracts

These are output schemas, not final prompt prose.

### 11.1 Curator output contract
Current weakness addressed:
- prose-only keep/discard is too lossy

Structured contract:
- decision: `kept | discarded`
- qualified_by: `novel_synthesis | novel_findings | experimental_blog | production_blog | comparative_survey | vendor_technical_results | none`
- evidence_basis: `benchmark | experiment | production | synthesis | mixed | none`
- novelty_strength: `low | medium | high`
- excerpt_sufficiency: `sufficient | partial | insufficient`
- reason: string
- limits: string
- confidence: `low | medium | high`

Compatibility output:
- current plain-text KEEP/DISCARD file may remain
- but `curator.json` becomes canonical structured form

### 11.2 Extractor/Facts output contract
Current weakness addressed:
- bullets are too lossy and not audit-friendly

Structured contract per fact:
- fact_id
- fact_text
- fact_type
- metric_value nullable
- metric_unit nullable
- source_span_ref
- confidence
- caveat nullable

Compatibility output:
- current `micro-facts.md` can remain as a readable mirror
- `facts.jsonl` becomes canonical structured form

### 11.3 Findings output contract
Current weakness addressed:
- top 3 bullets are too compressed for later reasoning

Structured contract per finding:
- finding_id
- finding_text
- finding_type: `result | implication | caveat | mechanism_hint`
- priority: `high | medium | low`
- source_span_ref
- confidence

Compatibility output:
- current `micro-findings.md` can remain
- `findings.jsonl` becomes canonical structured form

### 11.4 Synthesist article output contract
Current weakness addressed:
- article prose is not explicitly tied back to structured internals

Structured contract:
- article title
- core_thesis_claim_ids[]
- why_it_matters_claim_ids[]
- key_finding_claim_ids[]
- limits_claim_ids[]
- optional evidence_base_evidence_ids[]

Public prose output remains markdown sections in `article.md`.
Canonical linkage lives in `lineage.json`.

### 11.5 Conclave output contract
Current weakness addressed:
- pass/block prose is too soft for institutional law

Structured contract:
- verdict: `pass | block`
- lineage_check: `pass | warn | fail`
- contradiction_check: `pass | warn | fail`
- mechanism_check: `pass | warn | fail`
- citation_check: `pass | warn | fail`
- completeness_check: `pass | warn | fail`
- rationale: string
- remediation_items[]: strings

Compatibility output:
- `conclave.md` may remain as readable prose artifact
- `conclave.json` becomes canonical structured verdict

## 12. Compatibility policy

The replacement system should support a staged transition:
- existing markdown compatibility artifacts may continue to exist
- new structured files become canonical for validation and future extension
- renderers can continue to consume current public-facing markdown at first
- later phases may progressively shift renderers to structured internals if useful

## 13. Minimal required bundle for phase-complete Daily Rail

To count as complete for this phase, a kept article package should include at minimum:
- `article.md`
- `source.md`
- `curator.json`
- `findings.jsonl`
- `facts.jsonl`
- `claims.jsonl`
- `evidence.jsonl`
- `lineage.json`
- `validation.json`

A Daily package should include at minimum:
- `technical-executive-report.md`
- `executive-brief.md`
- `conclave.md`
- `conclave.json`
- `publish.md`
- `cluster-ledger.json`
- `lineage.json`
- `validation.json`

## 14. Bottom line

This schema spec keeps the current Daily Rail recognizable while upgrading it from a prose-first rail into a structured, validator-friendly institution.

That is the correct foundation for:
- Daily Rail feature parity++
- Piter 2.0 supervision and repair
- shadow proof and cutover
- and only later, eventual Canon work.
