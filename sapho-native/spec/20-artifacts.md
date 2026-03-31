# Artifact Spec

## Intake ticket

One markdown file per queued item.

Required frontmatter:

- `version`
- `ticket_id`
- `source_url`
- `source_channel`
- `queued_at_utc`
- `status`

## Source capture

One markdown file per article folder.

Required frontmatter:

- `version`
- `article_id`
- `ticket_id`
- `source_url`
- `canonical_url`
- `source_title`
- `capture_kind`
- `captured_at_utc`

## Curator receipt

Required frontmatter:

- `version`
- `role`
- `article_id`
- `ticket_id`
- `decision`
- `reason`
- `scope_class`
- `decided_at_utc`

## Evidence file

One markdown file per evidence unit.

Required frontmatter:

- `version`
- `article_id`
- `evidence_id`
- `kind`
- `citation`
- `source_url`
- `confidence`

## Claim file

One markdown file per claim.

Required frontmatter:

- `version`
- `article_id`
- `claim_id`
- `claim_text`
- `evidence_ids`
- `confidence`

Claim files are emitted by the Synthesist article-claims job.

## Article claims receipt

Required frontmatter:

- `version`
- `role`
- `article_id`
- `claim_count`
- `completed_at_utc`

## Article artifact

The canonical article file for one kept article.

Required frontmatter:

- `version`
- `article_id`
- `source_url`
- `source_title`
- `queued_at_utc`
- `captured_at_utc`
- `curator_decision`
- `artifact_minted_at_utc`
- `evidence_count`
- `claim_count`
- `publication_status`

The article artifact is emitted by the Synthesist article-write job.

## Daily package

One markdown file per UTC day.

Required frontmatter:

- `version`
- `date`
- `article_ids`
- `artifact_count`
- `status`
- `generated_at_utc`

Required sections:

- `Top-Line Judgments`
- `Article Readouts`
- `Mechanism Notes`
- `Contradiction Register`
- `Scope and Limits`

The Daily package is emitted by the Synthesist daily-synthesis job.

## Conclave dossier

One markdown file per Daily package.

Required frontmatter:

- `version`
- `date`
- `verdict`
- `reviewed_at_utc`

Required sections:

- `Lineage Law`
- `Mechanism Law`
- `Contradiction Law`
- `Citation Integrity`
- `Rationale`

The Conclave dossier is a gate artifact, not a persona artifact.

## Publish receipt

One deterministic markdown file per published day.

Required frontmatter:

- `version`
- `date`
- `verdict`
- `published_at_utc`
- `site_path`
- `daily_feed_path`
- `artifact_feed_path`
