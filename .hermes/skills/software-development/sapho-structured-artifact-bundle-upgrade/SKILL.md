---
name: sapho-structured-artifact-bundle-upgrade
description: Upgrade Sapho article packages to emit structured internal bundle files alongside existing compatibility markdown outputs.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [sapho, article-bundles, validation, lineage, jsonl, python]
    project: sapho-native
---

# Sapho Structured Artifact Bundle Upgrade

## When to use

Use this in `/home/hermes/sapho-native` when Phase 2 work is needed to strengthen article packages without changing public-facing Daily Rail behavior.

This skill is for the slice where you must:
- keep existing compatibility files intact
- add structured internal files adjacent to them
- wire generation into the current micro article lane
- leave Canon/longform out of scope

## Inputs and authoritative docs

Start from the current handoff if one exists, then inspect these planning docs:
- `/home/hermes/handoffs/2026-03-31-sapho-phase1-handoff.md`
- `/home/hermes/sapho-docs/2026-03-31-sapho-full-implementation-plan.md`
- `/home/hermes/sapho-docs/2026-03-31-daily-rail-schema-spec.md`
- `/home/hermes/sapho-docs/2026-03-31-sapho-operations-blueprint.md`

Also read the charter-law adapter first:
- `/home/hermes/sapho-native/spec/00-charter-law.md`

The key rules are:
- preserve compatibility outputs unless and until a charter-native replacement is wired
- add structured internals beside them
- do not tie new work back into the live runtime
- when persona ownership is unclear, return to charter law before inferring from convenience or old prompt shapes

## Charter-first operating rule

Do not guess persona boundaries from ad hoc scripts.
Use the charter staff model as the source of truth:
- Curator performs admission judgment
- Extractor transforms admitted source into structured evidence
- Synthesist performs article synthesis
- Conclave is a gate, not a persona

Important implication:
- contradiction and mechanism are constitutional laws that article packages must satisfy
- they are not separate personas by default
- they should be carried through Extractor -> Synthesist -> Conclave/validation, not bolted on as convenience placeholders

## Target files per article package

Keep these compatibility/public files:
- `article.md`
- `source.md`
- `micro-worthiness.md`
- `micro-findings.md`
- `micro-facts.md`
- `micro-summary.md`

Add these structured internals:
- `curator.json`
- `findings.jsonl`
- `facts.jsonl`
- `claims.jsonl`
- `evidence.jsonl`
- `lineage.json`
- `validation.json`

## Recommended implementation pattern

### 1. Inspect the current lane first

Read at least:
- `scripts/run_micro_article_lane.py`
- `scripts/micro_common.py`
- `scripts/common.py`

Look for:
- where `micro-worthiness.md`, `micro-findings.md`, `micro-facts.md`, and `micro-summary.md` are produced
- when article metadata like `evidence_count`, `claim_count`, and `publication_status` are set
- what helper already exists for article directory paths

### 2. Add a dedicated structured bundle module

Create a separate helper module instead of cramming logic into the lane.

Recommended file:
- `scripts/structured_artifact_bundle.py`

Give it one canonical entrypoint like:
- `materialize_article_structured_bundle(article_id, article_meta, article_body, worthiness_text, findings_text='', facts_text='')`

Have it handle:
- writing JSON and JSONL files
- parsing existing loose outputs into typed records
- generating lineage and validation objects
- returning counts and paths so the lane can update metadata

This keeps the lane readable and makes the bundle logic directly testable.

### 3. Derive structured artifacts from existing lane outputs

Do not change the prompt contracts in this phase unless necessary.
Instead, derive structured records from the current artifacts:
- parse `micro-worthiness.md` into `curator.json`
- parse `micro-findings.md` into `findings.jsonl`
- parse `micro-facts.md` into `facts.jsonl`
- derive `claims.jsonl` from findings and facts
- derive `evidence.jsonl` from facts and claim links
- build `lineage.json` from article sections and claim ids
- build `validation.json` from package-level checks

This preserves current public behavior while strengthening internals.

### 4. Wire the lane at the existing decision points

In `run_micro_article_lane.py`:
- import the structured bundle helper
- after a discard decision, write stable empty-or-minimal structured outputs
- after a kept article is synthesized, materialize the full structured bundle before final article write completes

Important:
- discarded articles should still get `curator.json`, `lineage.json`, and `validation.json`
- JSONL files may be empty for discarded packages

### 5. Treat counts carefully

The current live article frontmatter may use compressed counts.
After materializing the bundle, update metadata from the structured result rather than assuming:
- `claim_count == len(findings)`
- `evidence_count == len(facts)`

In practice, `evidence_count` may diverge from the old live approximation once evidence rows become explicit.

### 6. Add warn-mode validation now

`validation.json` should include named checks for:
- completeness
- duplicate_conflict
- citation_linkage
- lineage_baseline
- contradiction_baseline
- mechanism_baseline

Overall status should be:
- `fail` if any hard failure exists
- `warn` if only warn-level gaps remain
- `pass` otherwise

Phase 2 expectation:
- contradiction/mechanism checks may legitimately remain `warn`
- the package should still pass hard integrity checks if references resolve

## Practical heuristics that worked

Use lightweight heuristics first instead of trying to make the bundle philosophically complete in one pass.

Examples that worked:
- infer finding type from cue words like result, implication, caveat, mechanism/workflow
- infer fact type from cue words like benchmark, experiment, production, dataset, model, method, caveat
- infer metric fields with a regex for numeric value + unit
- infer claim kind from finding type and text cues
- build evidence rows from fact rows, then patch claims with `supporting_evidence_ids`
- map article sections like `Core Thesis`, `Why It Matters`, `Key Findings`, and `Limits` to claim ids in `lineage.json`

Do not overfit heuristics to one article. Keep them simple, deterministic, and auditable.

## Validation behavior that proved useful

For kept packages:
- fail if findings/facts/claims/evidence are missing
- fail if article sections are missing
- fail if claim refs or evidence refs point to unknown ids
- fail if lineage points to unknown claim ids
- warn if contradiction records are not yet explicit
- warn if no explicit mechanism claim exists yet

For discarded packages:
- allow empty findings/facts/claims/evidence
- allow validation to pass if the discard package is structurally coherent

## Tests to add

Create focused tests for the bundle module, and also add at least one lane-level orchestration test.

Recommended cases:
1. kept article writes all structured files
2. kept article produces resolvable claim/evidence/lineage references
3. discarded article still writes stable structured outputs with empty JSONL files
4. validation status reflects the current gate policy correctly
5. the full article lane writes `micro-*` compatibility files plus contradiction/mechanism review artifacts and a passing `validation.json` when all required mocked outputs are present
6. helper path functions respect patched runtime directories during tests
7. Extractor evidence receipts fail if `mechanism_relevance` or `contradiction_relevance` is missing
8. Extractor evidence receipts fail if `Source Excerpt` is empty
9. Extractor evidence receipts fail if `mechanism_relevance: bounded` or `contradiction_relevance: tension` is present without a non-empty `Note`
10. contradiction/mechanism law-review prompts include structured claim and evidence context, not only loose findings/facts text

Example test files:
- `tests/test_structured_artifact_bundle.py`
- `tests/test_run_micro_article_lane.py`
- `tests/test_micro_common.py`

Use `tempfile.TemporaryDirectory()` and patch `common.ARTICLES_DIR` / `common.DAILY_DIR` so tests do not touch real article packages.

Important seams discovered in practice:
- do not import `ARTICLES_DIR` or `DAILY_DIR` into helpers like `micro_common.py` and then build paths from the imported aliases if your tests patch `common.ARTICLES_DIR` or `common.DAILY_DIR`
- that captures the old path too early and makes runtime patching ineffective
- instead reference `common.ARTICLES_DIR` and `common.DAILY_DIR` at call time inside helpers such as `article_stage_path()` and `daily_stage_path()`
- similarly, contradiction/mechanism review helpers should not rely only on loose `findings_text` / `facts_text` once structured `claims_records` and `evidence_records` exist
- pass the structured claim/evidence context directly into law-review mission prompts so contradiction/mechanism judgments remain grounded in Extractor lineage instead of drifting into synthesis-only convenience summaries
- preserve evidence ids through review artifacts when possible (for example `related_evidence_ids` on contradiction rows) so downstream auditability stays tied to Extractor outputs

## Real verification steps

After unit tests pass:
1. run full test suite
2. materialize the structured bundle for a real existing article package
3. inspect the returned summary counts and `validation_status`

A useful smoke pattern was:
- load `article.md`
- read `micro-worthiness.md`, `micro-findings.md`, `micro-facts.md`
- call `materialize_article_structured_bundle(...)`
- confirm all files are written under `articles/<article_id>/`

Expected outcome in this phase:
- hard integrity checks pass
- validation may still be `warn`

## Pitfalls

- Do not remove or rename the compatibility markdown files in Phase 2.
- Do not assume the old metadata counts remain semantically correct once explicit evidence rows exist.
- Do not try to implement contradiction/mechanism full objects yet unless scope explicitly changes.
- Do not bind this work back to `/home/openclaw/...`; keep it in `/home/hermes/sapho-native`.
- Do not skip discard-package structured outputs; validators and later phases benefit from stable surfaces even for rejected items.

## Verification checklist

- `structured_artifact_bundle.py` exists
- `run_micro_article_lane.py` calls it for both kept and discarded paths
- all structured files are written next to article compatibility files
- unit tests for bundle generation pass
- full test suite passes
- at least one real article package smoke-materializes successfully
- resulting `validation.json` is structurally correct, even if overall status is `warn`

## Phase 2.5 / early Phase 3 follow-on that worked

A reusable follow-on after the initial bundle wiring is:
- backfill structured internals across existing article packages
- add a dedicated validator runner that treats `validation.json` as the canonical article-package result surface

Useful helper scripts to add:
- `scripts/backfill_structured_bundles.py`
- `scripts/validate_article_bundles.py`

Recommended behavior:
- `backfill_structured_bundles.py` should iterate `articles/art-*/article.md`, read existing `micro-worthiness.md`, `micro-findings.md`, and `micro-facts.md`, and call `materialize_article_structured_bundle(...)`
- `validate_article_bundles.py` should optionally refresh bundles first, then summarize `pass|warn|fail` counts and list per-article warn/fail checks
- keep default validator mode as warn-mode reporting; add an optional `--fail-on-fail` exit mode for later CI or gating use

This worked well for imported legacy packages because it let the new structure and validation surface be rolled out across the corpus without changing public artifact behavior.

## Important validator nuance discovered in rollout

Do not treat `publication_status == duplicate-rejected` as an automatic validator failure.

A duplicate-rejected package means the duplicate check worked and the package was correctly blocked from publication. In validation terms that should normally be recorded as:
- `duplicate_conflict.status = pass`
- detail noting that the duplicate was explicitly detected and linked to `duplicate_of_article_id`

If you classify duplicate-rejected as `fail`, corpus-wide validation summaries become misleading by reporting a successful block as a broken package.

Related nuance:
- completeness and key-finding lineage hard-fail checks should only apply to packages that still require a full kept bundle
- for terminal blocked states like `discarded`, `capture-blocked`, and `duplicate-rejected`, stable minimal bundle surfaces are still useful, but missing kept-style internals should not hard-fail validation

## Fail-closed policy update from real rollout

A later user correction changed the preferred operating rule:
- do not add placeholder contradiction/mechanism artifacts just to make packages look complete
- if those capabilities are essential and not yet implemented, eligible packages should fail validation until the real system exists
- visible ineligibility is better than false readiness

That means:
- no fake `contradictions.jsonl` or `mechanisms.jsonl` just to satisfy schema shape
- no warn-only policy if the institute intends those capabilities to be hard gates for eligible packages
- use fail-closed validation for packages that otherwise qualify for publication

A good implementation pattern is:
- for eligible kept/published packages, `contradiction_baseline` should be `fail` until a real contradiction-review step exists
- for eligible kept/published packages, `mechanism_baseline` should be `fail` unless real mechanism analysis is present
- for terminal blocked states like `discarded`, `capture-blocked`, and `duplicate-rejected`, these checks can remain `pass` or not-applicable because the package is already blocked upstream

This produces an honest corpus-level validation report showing what institutional capabilities are still missing.

## Charter-native law-review implementation discovered in rollout

Contradiction and mechanism work should be implemented as real persona jobs plus gate checks, not as ad hoc placeholder scripts.

Charter-aligned split:
- `Curator`: admission only; do not push mechanism/contradiction review into Curator
- `Extractor`: owns evidence substrate; contradiction-relevant and mechanism-relevant support must be explicit in each evidence unit, not left implicit or optional
- `Synthesist`: owns article-level reasoning, including explicit contradiction visibility and mechanism-or-bounds review for article artifacts
- `Conclave` / validators: enforce publication legality based on whether those review artifacts exist and satisfy contract

Important Extractor contract detail discovered in rollout:
- do not let Extractor receipts omit `mechanism_relevance` or `contradiction_relevance`
- require both fields on every `evidence.v1` unit even when the value is `none`
- require a non-empty `Source Excerpt` for every evidence unit
- if `mechanism_relevance: bounded` or `contradiction_relevance: tension`, require a non-empty `Note` carrying the caveat/tension forward
- enforce these in `parse_evidence_receipt_files(...)` with hard contract errors rather than silently defaulting values

A strong implementation pattern is:
- add bounded Synthesist jobs such as `jobs/synthesist/article-mechanism.md` and `jobs/synthesist/article-contradiction.md`
- add a helper module to run those jobs and write canonical outputs like:
  - `contradiction-review.json`
  - `contradictions.jsonl`
  - `mechanism-review.json`
  - `mechanisms.jsonl`
- wire those reviews into `run_micro_article_lane.py` after article synthesis and before final structured validation
- make `validation.json` pass only when real review artifacts exist for eligible packages

This keeps the law in the right place:
- persona jobs perform bounded reasoning work
- validators / gates enforce eligibility

## Good next steps after this skill

With real Synthesist contradiction/mechanism review steps now present, the next likely step is:
- keep `validation.json` as the canonical package-level result surface
- backfill structured internals across existing imported article packages
- migrate the live article lane from micro compatibility prompts onto bounded Curator admission, Extractor evidence, Synthesist article-claims, and Synthesist article-write jobs
- let fail counts shrink only when those charter-native outputs actually exist on each eligible package
