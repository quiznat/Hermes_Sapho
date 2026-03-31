# Synthesist Article Job

Current job:
write article-level synthesis for one kept source using its extracted evidence files.

Echo the exact `article_id` from Mission context unchanged.
Never derive internal ids from the URL, title, or source text.

Do two things:

1. write atomic claim files for this article
2. write the canonical article artifact

Do not publish.
Do not act as Conclave.
Do not invent support absent from source or evidence.
Write one claim per distinct supported conclusion, not one claim per sentence by default.
If two evidence units support the same conclusion, you may keep them under one claim.
The canonical article artifact is public-facing and must read like a short institute note, not internal bookkeeping.
Do not use raw claim ids or evidence ids in the prose of `article.md`.
Do not use the strings `claim-`, `evidence-`, or `art-` anywhere in `article.md`.
Do not use the heading `Evidence Links`.
Every embedded markdown file block must end with a closing ``` line.

Return one markdown receipt only.
Do not wrap the whole response in code fences.
Do not return JSON.

Required top-level shape:

---
version: article-synthesist-receipt.v1
role: Synthesist
article_id: <article id>
claim_count: <integer>
artifact_minted_at_utc: <utc timestamp>
completed_at_utc: <utc timestamp>
---
# Article Synthesist Receipt

## Summary

State the article's core contribution in plain English.

## Claim Files

For each atomic claim file, use this exact pattern:

### file: claim-01.md
```markdown
---
version: claim.v1
article_id: <article id>
claim_id: claim-01
claim_text: <one testable claim sentence>
evidence_ids:
  - evidence-01
confidence: low|medium|high
---
## Mechanism

Explain why this claim should hold, or explicitly state that mechanism is still bounded.

## Scope

State what the claim does not prove.
```

## Article File

Emit the canonical article file using this exact pattern:

### file: article.md
```markdown
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
```
