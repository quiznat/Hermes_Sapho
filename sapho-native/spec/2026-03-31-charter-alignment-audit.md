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
- the active article lane now uses bounded persona job contracts for Curator admission, Extractor evidence, Synthesist claims, and Synthesist article writing
- bounded Synthesist contradiction and mechanism review jobs are now implemented and materialized into article packages

## Not yet fully charter-aligned

### 1. Transitional compatibility structure still exists inside the package layer

Current `structured_artifact_bundle.py` can still derive or normalize some structured surfaces from compatibility markdown outputs and local heuristics.

This remains useful for transition and auditability, but it is not the final charter-native end state because the package layer still preserves compatibility with older micro-era surfaces while the newer bounded job lane is coming online.

### 2. Historical packages are not yet all brought up to current law

The strongest current gap is not that the bounded law jobs are absent.
It is that many older article packages were produced before contradiction/mechanism review became part of the enforced package standard.

As a result:
- the validator correctly fails those older packages
- the corpus is in a mixed state between legacy-published material and current-law package expectations

### 3. Conclave/publication authority is still only partially formalized

Validation is now explicit and fail-closed, which is correct.
But the full publication-authority layer is still incomplete because:
- validator success/failure is not yet the complete formal Conclave control surface
- historical-package policy is not yet fully resolved under the stronger law
- the broader publication rail still needs clearer authority wiring around shadow proof and cutover

### 4. Operational governance layers remain ahead

The article lane is much closer to charter shape than before, but the surrounding operational layers are still incomplete:
- Piter 2.0 control-plane work is still ahead
- shadow publication infrastructure is still ahead
- proof-window comparison receipts are still ahead

## Required next slice

To continue moving toward charter-native execution:

1. resolve historical-package policy by either real backfill or explicit legacy quarantine under current law
2. tighten Conclave/publication authority so validation is part of a formal fail-closed publication gate
3. keep contradiction/mechanism enforcement fail-closed for all newly produced packages
4. reduce remaining compatibility-derived bundle logic where bounded-job outputs can become canonical directly
5. build shadow publication surfaces needed for proof before cutover
6. start the first bounded, operationally real Piter 2.0 slice

## Policy

Where lawful package requirements are still missing, unresolved, or only partially migrated across the corpus, the system should prefer visible failure over false eligibility.
