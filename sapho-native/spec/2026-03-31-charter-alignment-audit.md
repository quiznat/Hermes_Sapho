# Charter Alignment Audit

Date: 2026-03-31
Workspace: `/home/hermes/sapho-native`

## Charter-first rules used for this audit

Source of truth:
- `/home/hermes/sapho-native/spec/00-charter-law.md`

Key constraints:
- personas are institute-wide reasoning functions
- jobs are bounded assignments performed by personas
- gates are legal publication checks, not personas
- admitted source is transformed into structured evidence by Extractor
- Synthesist performs article synthesis
- Conclave is the sole publication authority
- contradiction and mechanism are constitutional laws, not optional polish

## Aligned so far

- fail-closed article validation now blocks eligible packages missing contradiction/mechanism review
- duplicate-rejected packages are treated as correctly blocked rather than validator failures
- article package surfaces preserve explicit lineage, evidence, and validation files
- no placeholder contradiction/mechanism artifacts are used for greenwashing eligibility

## Not yet fully charter-aligned

### 1. Structured claims/evidence are still compatibility-derived

Current `structured_artifact_bundle.py` derives:
- `findings.jsonl`
- `facts.jsonl`
- `claims.jsonl`
- `evidence.jsonl`

from legacy-compatible markdown outputs and local heuristics.

This is useful for transition and auditability, but it is not the final charter-native form because:
- Extractor evidence is not yet produced from the bounded `jobs/extractor/evidence.md` contract
- Synthesist claims are not yet produced from the bounded `jobs/synthesist/article-claims.md` contract
- article synthesis is still driven by micro compatibility prompts instead of the bounded charter job set

### 2. Contradiction/mechanism review jobs are not yet implemented

The validator is now correct to fail these packages.
The production jobs that satisfy those laws still need to be added.

### 3. Current lane still uses micro prompt surfaces

`run_micro_article_lane.py` still runs:
- `micro/jobs/curator-worthiness.md`
- `micro/jobs/facts.md`
- `micro/jobs/article-summary.md`

This is operationally useful but remains looser than the charter-first job contracts already present under `jobs/`.

## Required next slice

To move toward charter-native execution:

1. use bounded Extractor evidence job
2. use bounded Synthesist claim job
3. use bounded Synthesist article-write job
4. add bounded Synthesist contradiction review job
5. add bounded Synthesist mechanism review job
6. keep Conclave/validators fail-closed until those outputs exist and pass

## Policy

Until those bounded jobs exist, the system should prefer visible failure over false eligibility.
