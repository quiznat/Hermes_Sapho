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
The canonical article artifact is public-facing and must read like a short institute note, not internal bookkeeping.
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

## Why It Matters

State why this belongs in Sapho.

## Key Findings

List the supported findings as plain-English bullets.
Do not write raw claim ids in this section.

## Evidence Base

Write 2-5 plain-English bullets describing the evidence.
Each bullet must say what the source shows, which conclusion it supports in words, and why it matters.
Do not use raw evidence ids or claim ids in this section.

## Limits

State unresolved limits, missing mechanism, or contradiction risk plainly.
If no direct contradiction is visible, say that plainly without pretending the evidence is cleaner than it is.
If mechanism remains uncertain, say so explicitly rather than smoothing it away.
