# Extractor Evidence Job

Current job:
read one kept source and turn it into atomic evidence units.

Echo the exact `article_id` from Mission context unchanged.
Never derive internal ids from the URL, title, or source text.

Work only from the captured source markdown.
Do not rely on memory.
Do not invent evidence.
Do not summarize vaguely.
Make the units atomic but not fragmented.
If one sentence contains two distinct evidence-bearing facts, split them.
If one statement is only one fact, keep it as one evidence file.
Every embedded markdown file block must end with a closing ``` line.

Return one markdown receipt only.
Do not wrap it in code fences except for the required embedded markdown file blocks.
Do not return JSON.

Required top-level shape:

---
version: extractor-receipt.v1
role: Extractor
article_id: <article id>
evidence_count: <integer>
completed_at_utc: <utc timestamp>
---
# Extractor Receipt

## Summary

State what kind of evidence this source contains.

## Evidence Files

For each atomic evidence file, use this exact pattern:

### file: evidence-01.md
```markdown
---
version: evidence.v1
article_id: <article id>
evidence_id: evidence-01
kind: result|method|metric|incident|quote|claim-support
citation: <short citation string>
source_url: <source url>
confidence: low|medium|high
mechanism_relevance: direct|bounded|none
contradiction_relevance: supports|tension|none
---
One short evidence statement.

## Source Excerpt

Quote or paraphrase the exact supporting passage.

## Note

Any caveat that should remain attached to this evidence unit.
```

Only emit evidence files when the source actually supports them.
If the source contains no atomic evidence, set `evidence_count: 0` and explain why.
Set `mechanism_relevance: direct` only when the evidence itself states or directly supports how the result happens.
Set `mechanism_relevance: bounded` when the evidence matters to mechanism law mainly by showing the mechanism is unknown, partial, or limited.
Set `contradiction_relevance: tension` when the evidence introduces a visible tension, caveat, or unresolved conflict that must remain disclosed downstream.
