# Eval Law

Prompt quality is the real trust boundary in this runtime.

## Rules

- Each active persona has a charter file.
- Each active job has a template file.
- Each active persona-and-job pair has a fixture pack.
- A fixture pack contains ten fixed fixtures.
- A persona-and-job pair is not promoted into active use until it passes ten of ten.
- Any persona or job-template edit reruns the affected pack.
- Eval output is stored as markdown receipts, not JSON.

## Active minds and gates for v1 Daily

- Curator
- Extractor
- Synthesist

Active jobs and gates:

- Curator admission
- Extractor evidence
- Synthesist article claims
- Synthesist article write
- Synthesist daily synthesis
- Conclave Daily gate

## Script role in evals

Scripts may:

- load fixtures
- load persona charters
- load job templates
- call agents
- lint frontmatter and required sections
- compare expected values
- call a reviewer harness for job-quality judgment
- write markdown eval reports

Structural checks alone are not enough for Daily promotion.
Promotion requires declared expected outcomes plus an explicit quality-review receipt for the relevant persona-and-job pair.
