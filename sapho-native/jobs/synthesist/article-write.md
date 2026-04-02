# Synthesist Article Write Job

Current job:
write the canonical public article artifact for one kept source from approved claims plus compact evidence context.

Echo the exact `article_id` from Mission context unchanged.
Never derive internal ids from the URL, title, or source text.

This job only writes `article.md`.
Do not emit claim files in this step.
Do not publish.
Do not act as Conclave.
Do not invent support absent from the provided claims and evidence context.
The canonical article artifact is public-facing and must read like a dense institute decision block, not internal bookkeeping, not a book report, and not an abstract restatement.
The reader should be able to understand the key empirical findings, contradictions/tensions, mechanism or bounds, and Sapho relevance without reading the paper.
Do not default to rigid table formatting; use prose and bullets that fit the source while preserving density.
If the claims or evidence contain concrete measurements, deltas, benchmark sizes, costs, counts, or other quantitative payload, surface those specifics in the article rather than replacing them with generic summary language.
Do not use raw claim ids or evidence ids in the prose of `article.md`.
Do not use the strings `claim-`, `evidence-`, or `art-` anywhere in `article.md`.
Do not use the heading `Evidence Links`.

Return one markdown file only.
Do not wrap the whole response in code fences.
Do not return JSON.

Required top-level shape:

---
version: article.v1
article_id: <article id>
source_url: <source url>
source_title: <source title>
queued_at_utc: <utc timestamp>
captured_at_utc: <utc timestamp>
curator_decision: kept
artifact_minted_at_utc: <utc timestamp>
evidence_count: <integer>
claim_count: <integer>
publication_status: ready-for-daily
---
# <article title>

## Core Thesis

State the article's main point as a disciplined institute artifact.

## Why It Matters for Sapho

State why this changes Sapho's view of the field, operating assumptions, or evaluation doctrine.

## Key Findings

List the supported findings as dense plain-English bullets.
When the evidence includes concrete values, put the concrete values directly in the bullets.
Do not write raw claim ids in this section.

## Evidence and Findings

Write 2-6 dense bullets that surface the actual empirical or otherwise decisive payload.
Each bullet must say what the source shows, what conclusion it supports, and why that matters.
If the source contains measurements, deltas, benchmark sizes, counts, cost changes, or other quantitative results, include the important ones here explicitly.
Do not use raw evidence ids or claim ids in this section.

## Contradictions and Tensions

State the tensions, mixed results, contradiction disclosures, or places where the evidence cuts against easy interpretation.
Do not satisfy this section with generic language such as "no direct contradiction is visible" unless you also name the concrete tension that matters for interpretation.
When the source contains benchmark-specific reversals, mixed subgroup results, cost/performance tradeoffs, adoption/attention mismatches, or other decision-relevant tensions, name them explicitly.

## Mechanism or Bounds

State the supported mechanism when the evidence supports one.
If mechanism is uncertain, state the strongest bounded operational explanation instead of saying only that the paper is descriptive.
Do not default to generic phrases like "the supported mechanism is limited" or "the evidence is descriptive" when a stronger bounded explanation is available from the evidence.
If the evidence is only correlational, partial, benchmark-bound, or otherwise constrained, say so explicitly here.

## Limits

State unresolved limits, missing mechanism, or contradiction risk plainly.
Do not smooth away uncertainty.
