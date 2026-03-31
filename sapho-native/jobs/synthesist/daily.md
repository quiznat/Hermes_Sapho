# Synthesist Daily Job

Current job:
write the Daily package for the current UTC day from the provided finalized article artifacts.

Use the provided article ids exactly as given.
Never invent or rewrite article ids.
The Daily package is public-facing and must read like an institute note, not internal wiring.
Do not use raw article ids, claim ids, or evidence ids anywhere in the body.
Do not use the headings `Claim Graph`, `Evidence Index`, or `Article Index`.
The body must read like a finished institute note, not a trace log.

Daily is a time gate.
Do not invent article membership.
Use all provided articles and only the provided articles.

Return one markdown file only.
Do not wrap it in code fences.
Do not return JSON.
Begin on the first line with `---`.
Do not add any preamble before frontmatter.
Use the provided date exactly.
List the provided article ids exactly once each.
Set artifact_count to the number of provided article ids.

Required shape:

---
version: daily-package.v1
date: <yyyy-mm-dd>
article_ids:
  - <article id>
artifact_count: <integer>
status: draft
generated_at_utc: <utc timestamp>
---
# Daily Dose — <yyyy-mm-dd>

## Top-Line Judgments

State the main judgments the institute is asking readers to accept today.

## Article Readouts

For each article, add one `### <Article Title>` subsection.
Inside each subsection include:
- one short paragraph stating the article's core thesis
- a `Key findings:` bullet list with plain-English supported conclusions
- an `Evidence base:` bullet list with plain-English evidence statements
Do not use raw internal ids anywhere.

## Mechanism Notes

Explain why the important effects should hold, or where mechanism remains bounded.

## Contradiction Register

State any conflicts, tension, uncertainty, or unresolved disagreement across today's set.

## Scope and Limits

State what today's Daily does not claim.
