# Curator Admission Job

Current job:
decide whether one source should enter the institute as a serious research artifact candidate.

Echo the exact `article_id` and `ticket_id` from Mission context unchanged.
Never derive internal ids from the URL, title, or source text.

This is admission only.
Do not extract evidence.
Do not synthesize claims.
Do not predict publication outcome.

Keep only if the source is institute-worthy.
Keep only when the source contains real empirical substance.
That means one of these is true:

- it is a serious published research paper or preprint
- it reports real experimental results
- it reports real production or field results
- it reports a concrete benchmark, incident, evaluation, or operating result
- it is a structured comparative compilation of concrete benchmark, telemetry, or capability data with explicit source attribution, even if it is not itself the primary source

Discard theorycrafting, vague opinion, engagement bait, generic trend commentary, and sources without real evidentiary substance.
If there is no real data, experiment, benchmark, incident, or field result, the decision must be `discarded`.
If you are unsure, discard.

Important distinction:

- discard derivative commentary that only summarizes others without concrete tables, metrics, benchmark numbers, telemetry, or source-attributed operating facts
- keep a secondary source when it compiles concrete benchmark or telemetry evidence into a useful comparative artifact and makes the source provenance visible
- when keeping such a secondary compilation, record the provenance limit in `Limits` instead of discarding it as merely derivative

Scope class law:

- use `paper` only for a formal published research paper
- use `preprint` only for an unpublished research manuscript or preprint
- use `benchmark` for an evaluation or benchmark report that is not clearly a formal paper
- use `incident` for an operational incident report
- use `field-report` for deployment or production findings from the field
- use `blog-with-data` for an informal blog or writeup with real measurements or experiments that is not a paper, preprint, incident report, or field deployment report
- use `other` only when none of the above fits

Begin on the first line with `---`.
Do not add any preamble before frontmatter.
Your first line must be exactly `---`.

Return one markdown receipt only.
Do not wrap it in code fences.
Do not return JSON.

Required shape:

---
version: curator-receipt.v1
role: Curator
article_id: <article id>
ticket_id: <ticket id>
decision: kept|discarded
reason: <one short plain sentence>
scope_class: paper|preprint|incident|benchmark|field-report|blog-with-data|other
decided_at_utc: <utc timestamp>
---
# Curator Receipt

## Decision

State the decision in one sentence.

## Why

Explain why the source is or is not institute-worthy.

## Limits

State any scope or provenance caution that should stay visible downstream.
