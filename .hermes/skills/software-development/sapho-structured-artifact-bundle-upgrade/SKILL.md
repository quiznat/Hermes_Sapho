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
- pass structured `claims_records` and `evidence_records` into the law-review helper, not just loose findings/facts text
- make `validation.json` pass only when real review artifacts exist for eligible packages

Important lineage hardening discovered in rollout:
- contradiction review outputs should carry `related_evidence_ids` when the tension is grounded in explicit Extractor evidence units
- mechanism review outputs should carry `evidence_ids` for both positive mechanism explanations and bounded claims when evidence anchors are available
- review runtime should fail closed if a law-review output cites evidence ids that are not present in the provided evidence list
- this keeps the constitutional chain explicit: Extractor evidence -> evidence ids -> Synthesist law review -> validator/gate

This keeps the law in the right place:
- persona jobs perform bounded reasoning work
- validators / gates enforce eligibility

## Historical imported-package policy discovered in rollout

Once structured backfill and fail-closed validation are active across a mixed corpus, a new ambiguity appears:
- older imported runtime packages may still be present in the corpus
- some are already blocked/discarded and should not be treated as publication candidates
- some are historically published but missing contradiction/mechanism law reviews
- a small number may already satisfy the stronger law

A reusable pattern that worked well is to materialize an explicit per-package policy artifact:
- `historical-policy.json`

Recommended classification:
- `not_applicable` — native package outside the historical-import policy scope
- `blocked_not_publishable` — imported package is already `discarded`, `capture-blocked`, or `duplicate-rejected`; it is not a current publication candidate
- `legacy_quarantined` — imported package is `published` or `ready-for-daily` but still fails contradiction/mechanism law checks, so it must remain explicitly ineligible under current law
- `current_law_compliant` — imported package is backed by real lawful artifacts and now passes current law
- `needs_remediation` — imported package is neither blocked nor lawful and still needs repair work beyond the standard quarantine case

Important rule discovered in practice:
- do not label imported blocked packages as `current_law_compliant` just because their validator status is `pass`
- blocked packages are non-candidates, not compliant publication packages
- classify them separately as `blocked_not_publishable`

A strong `historical-policy.json` shape includes:
- `version`
- `article_id`
- `applies`
- `source_regime` (`runtime-import` vs `native`)
- `publication_status`
- `validation_status`
- `policy_status`
- `current_law_eligible`
- `missing_law_checks`
- `disposition`
- `reviewed_at_utc`

Recommended implementation point:
- generate this artifact inside `structured_artifact_bundle.py` right after `validation.json` is built, so every backfill and every future lane materialization emits a stable policy surface

Recommended tests to add:
1. native package writes `historical-policy.json` with `not_applicable`
2. imported published package missing contradiction/mechanism review becomes `legacy_quarantined`
3. imported package with real contradiction/mechanism artifacts becomes `current_law_compliant`
4. imported discarded package becomes `blocked_not_publishable`

Recommended operational step after implementation:
- run `python scripts/backfill_structured_bundles.py` across the real corpus so every historical package gets an explicit policy artifact
- summarize resulting counts in a short persisted report under `spec/` so the new historical status is documented, not only visible in terminal output

## Historical remediation replay runner discovered in rollout

Once `historical-policy.json` exists, a second reusable need appears:
- systematically rerun imported historical packages through the new bounded article lane
- let the current system decide whether each package should now be `ready-for-daily`, `discarded`, `duplicate-rejected`, or `capture-blocked`
- do this without auto-publishing artifacts during replay

A strong pattern is to add a dedicated wrapper script rather than overloading backfill:
- `scripts/remediate_historical_imports.py`

Recommended behavior:
- select only imported runtime packages where `historical-policy.json` currently reports:
  - `legacy_quarantined`
  - `current_law_compliant`
- exclude `blocked_not_publishable` packages from replay by default
- rerun each candidate through:
  - `python scripts/run_micro_article_lane.py --article-id <id> [--replay-date YYYY-MM-DD]`
- never call `run_micro_artifact_publish.py` from the remediation runner
- record before/after values for:
  - `publication_status`
  - `policy_status`
  - return code
  - stdout/stderr
- write a JSON report under `state/reports/`

Important implementation finding:
- keep remediation and publication separate
- even if replay yields `ready-for-daily`, do not auto-publish during remediation
- this preserves fail-closed operator review and keeps replay from silently mutating live public surfaces

Recommended tests:
1. candidate selection returns only imported packages with replay-eligible policy states
2. remediation runner shells out to `run_micro_article_lane.py`, not the artifact publisher
3. remediation summary includes before/after publication and policy states
4. remediation runner writes a persisted report file

A useful real-world operating pattern is:
- first run `python scripts/remediate_historical_imports.py --dry-run`
- then remediate a small batch with `--limit 5`
- inspect the report before widening the replay set

## Artifact article quality bar discovered in rollout

A major user correction changed what “good enough” means for public Sapho artifact articles.

The article artifact itself must be a dense, actionable decision block.
It is not enough for `article.md` to:
- restate the abstract
- summarize the topic in generic prose
- merely point at `source.md` for the real substance

The reader should be able to read the artifact article and extract the key paper result without opening the source.

Required outcome:
- the artifact itself should carry the meaningful empirical findings when they exist
- it should surface contradiction/tension explicitly
- it should surface mechanism when supported, or explicit bounds when mechanism is not established
- it should explain why the result matters for Sapho’s goals, not only for the paper’s own framing

Important anti-pattern discovered in practice:
- do not make the artifact table-first by default
- tables can be useful occasionally, but they are not the right canonical shape because they force content into inappropriate cells and can limit dense synthesis
- the real target is a compressed high-signal information block, not a rigid template or book report

A better artifact article typically needs expressive sections such as:
- thesis
- dense findings block with concrete measured results when available
- contradiction / tension
- mechanism or bounds
- limits
- why it matters for Sapho
- confidence / evidence posture

Practical writing rule:
- if the source/evidence bundle contains concrete numbers, benchmark counts, measurable deltas, or hard operational distinctions, the article should surface them directly
- if the article only says “the paper studies X” while omitting those decisive specifics, treat that as inadequate synthesis even if structure/law checks pass

Important historical-package diagnostic discovered in rollout:
- some imported packages have strong `source.md` captures but weak legacy `article.md` artifacts
- when replay fails before article rewrite completes, do not mistake the weak carried-forward `article.md` for the intended end-state quality bar
- first fix the replay blocker, then judge the rewritten article against the denser Sapho artifact standard

## Git tracking policy discovered in rollout

A user correction changed repo policy for Sapho content:
- track Sapho content broadly in git
- do not exclude generated content by default
- exclude mainly secrets, credentials, caches, and true temporary files

Practical implication for the top-level disaster-recovery repo:
- `sapho-native/articles/` should be tracked
- `sapho-native/daily/` should be tracked
- `sapho-native/discovery/` should be tracked
- `sapho-native/public/` should be tracked
- `sapho-native/queue/` should be tracked
- `sapho-native/state/` should be tracked when it contains durable content worth review/history

Still ignore:
- secrets and auth material
- `.env` files and credential files
- caches
- temporary files
- upstream nested repos with their own git history

This matters because human review of article artifacts and replay outcomes is much easier when those artifacts are directly visible on GitHub rather than only on local disk.

## Historical replay operating rule discovered in rollout

When first enabling `scripts/remediate_historical_imports.py`, do not widen immediately to the full corpus.
Use a sanity-check batch first.

Recommended operating pattern:
1. `--dry-run`
2. replay `--limit 5`
3. inspect before/after report and resulting article artifacts
4. only widen after understanding error classes

Important finding from the first real batch:
- some historically published packages may now be discarded by the stronger bounded Curator lane, which is a legitimate outcome
- some packages may fail replay due to contract errors like `extractor_evidence_count_mismatch`
- this means historical remediation is both a quality upgrade and a debugging surface; treat it as such, not as a guaranteed auto-upgrade path

## Replay/debugging findings from a successful regenerated sample

A real replay of `art-2026-03-03-001` exposed three reusable failure classes that are worth checking immediately whenever a historical replay stalls:

### 1. Repeated task-runner payloads can break downstream parsers

Observed failure mode:
- the Hermes CLI output for Extractor and Synthesist sometimes repeated the same payload twice in one response
- downstream code then counted duplicate evidence blocks or saw duplicate YAML/article documents

Practical fixes that worked:
- in `task_runner.normalize_output()`, collapse exact duplicated payloads after stripping CLI chrome and session ids
- in `parse_evidence_receipt_files(...)`, deduplicate evidence units by `evidence_id` so repeated receipt blocks do not inflate counts
- in article-write handling, extract the final complete article document rather than assuming the whole raw response is one article

Verification to add:
- a task-runner test where the same YAML/article payload is repeated twice and normalization returns one copy
- an article-runtime test where an Extractor receipt body is duplicated and `parse_evidence_receipt_files(...)` still returns the unique evidence units once
- an article-runtime test where two article documents are concatenated and the helper chooses the final complete one

### 2. Synthesist YAML may be structurally right but syntactically fragile

Observed failure mode:
- Synthesist claim output used colon-containing scalar text without quoting, causing `yaml.safe_load(...)` to raise `ScannerError`

Practical fix that worked:
- keep normal YAML parsing first
- on YAML parse failure, run a conservative scalar-quoting fallback for plain `key: value` lines before retrying `yaml.safe_load(...)`
- do not try to rewrite list markers or structured YAML blocks indiscriminately; only quote obvious plain scalar values

Verification to add:
- a regression test using malformed claim YAML where `mechanism_or_bounds` or `contradiction_note` contains an unquoted colon
- assert that `_yaml_mapping(...)` still recovers the expected mapping

### 3. Article-write output can pass content review but still leak internal structure if duplicated

Observed failure mode:
- article-write produced a strong dense artifact, but duplicated the full article document
- the second frontmatter block leaked into the first body, triggering `visible_internal_id_leak:article-write`

Practical fix that worked:
- add a helper like `extract_last_article_document(...)`
- parse only the final full `article.v1` document from the raw article-write output before validating sections and internal-id leakage

Verification to add:
- a regression test with two concatenated `article.v1` documents where the helper returns the final one only

### 4. Article frontmatter can fail on bracket-prefixed titles even when content is otherwise valid

Observed failure mode:
- article-write output for arXiv-derived titles sometimes emits frontmatter like:
  - `source_title: [2512.08296] Towards a Science of Scaling Agent Systems`
- YAML interprets the leading `[` as a flow-sequence start, so `parse_markdown()` / `load_frontmatter()` can fail before the article body is even reviewed

Practical fix that worked:
- broaden `repair_frontmatter_text(...)` in `common.py`
- do not only quote scalar values containing `:`
- also quote scalar values starting with YAML-special prefixes such as:
  - `[`
  - `{`
  - `&`
  - `*`
  - `!`
  - `%`
  - `@`
  - `` ` ``
- keep numbers, booleans, nulls, and already-quoted scalars untouched

Verification to add:
- a regression test where `load_frontmatter(...)` receives a bracket-prefixed article title and still returns the expected string value

### 5. Law-review YAML can fail on unquoted colon-bearing list-item mappings

Observed failure mode:
- contradiction/mechanism review outputs sometimes emit list-item mappings like:
  - `- contradiction_text: The aggregate result is negative: some narrower cases are positive.`
- the initial tolerant YAML fallback handled plain `key: value` lines but not `- key: value` list-item mapping lines
- this caused `article_law_reviews._load_yaml_payload(...)` to fail even after claims parsing had already been hardened

Practical fix that worked:
- add the same tolerant scalar-quoting fallback to `article_law_reviews.py`
- handle both forms:
  - `key: value`
  - `- key: value`
- on YAML parse failure, quote only obvious scalar tails and retry `yaml.safe_load(...)`

Verification to add:
- a regression test where contradiction review YAML contains unquoted colon-bearing scalar values on list items and still loads into a mapping correctly

### 6. A successful regenerated sample is a better stopping point than a fixed runner alone

Operational lesson:
- do not stop after fixing the replay infrastructure in the abstract
- keep working until at least one historically quarantined kept article is actually rerun into:
  - a dense public artifact
  - passing `validation.json`
  - lawful contradiction/mechanism review artifacts
  - `historical-policy.json` changing to `current_law_compliant`

A good review checkpoint is a concrete GitHub-visible artifact package, not only passing tests.

### 7. Two regenerated kept samples provide a much stronger replay confidence bar than one

A valuable experiential finding from this rollout:
- one successful regenerated article proves the path can work
- a second successful regenerated article after additional parser/frontmatter fixes proves the fixes generalize better than a one-off patch

Concrete examples that were fully rerun into dense, lawful, reviewable artifacts:
- `art-2026-03-03-001`
- `art-2026-03-02-025`

Both ended with:
- `publication_status: ready-for-daily`
- passing `validation.json`
- contradiction/mechanism review artifacts present
- `historical-policy.json` set to `current_law_compliant`

Use this as the practical confidence bar before widening remediation batches further.

### 8. When the legacy/OpenClaw rail is dead, change posture from replacement project to live-transition execution

A major strategic change discovered in rollout:
- if the old OpenClaw rail is no longer functioning, the new Sapho-native rail is no longer just a replacement build
- it becomes the production succession path and should be treated as the path to go live
- do not rush quality gates, but do stop acting as though the old rail remains a usable fallback

Recommended execution posture:
- maintain fail-closed publication law
- keep frequent commits and pushes as operational fallback points
- stop re-deciding priorities ad hoc
- execute against a formal roadmap with ordered slices

A useful roadmap order that worked well was:
1. continue historical remediation in small batches using the stabilized replay path
2. build the formal publication-authority gate so `ready-for-daily` really means lawful promotion candidate
3. build an operator-facing live-operations control surface/report
4. continue broader remediation under that stronger operating model
5. wire the complete new-primary publication flow
6. only then expand post-stabilization work like richer control-plane features

### 9. Batch-remediation operating rule after replay hardening

Once replay is stable enough to produce good reference artifacts, continue in small explicit batches rather than widening to the full corpus.

Recommended pattern:
- choose 3–5 explicit article ids, not an open-ended limit, once the queue contains mixed already-remediated and still-quarantined items
- rerun them with `scripts/remediate_historical_imports.py --article-id ... --replay-date YYYY-MM-DD`
- inspect the generated report under `state/reports/`
- spot-check at least one regenerated `article.md` plus `validation.json` and `historical-policy.json`
- commit and push each successful batch before moving on
- when reporting the batch to the operator, include direct GitHub links for:
  - the commit
  - the remediation report under `state/reports/`
  - each article package directory
  - each article's `article.md`
  - each article's `validation.json`
  - each article's `historical-policy.json`
  - for blocked/discarded outcomes, include `micro-worthiness.md` too

A useful backlog-selection pattern discovered in later imported-batch processing:
- when the queue contains a mix of already-remediated articles and untouched imported leftovers, identify the next explicit batch by finding imported articles whose latest `git log --follow -- articles/<id>/article.md` entry is still only the import commit (for example `424902b sapho: import 44 leftover stalled runtime items`)
- this gives a reliable list of untouched backlog items even when many other imported articles already have later replay commits or website-publication commits
- then take the next 6 such untouched ids in sorted order as the next backlog batch

This worked well for the later 6-item batches because it avoided accidentally reprocessing already-remediated articles that still looked imported at a metadata level.

This proved important in practice because the operator wanted to click straight into GitHub to review each regenerated artifact without asking for paths to be converted into links afterward.

Good outcomes to expect in healthy batches:
- historical `published` / `legacy_quarantined` packages become `ready-for-daily` / `current_law_compliant`
- regenerated article artifacts meet the dense empirical quality bar
- contradiction/mechanism reviews and validation pass cleanly

This turns historical remediation into a reliable execution slice rather than a one-off cleanup task.

### 10. Guard against descriptive backslide in regenerated artifacts

A later remediation batch exposed an important failure mode:
- some regenerated artifacts technically passed structure/law checks but slid back toward descriptive survey voice
- the weak pattern looked like:
  - generic contradiction language such as `No direct empirical contradiction is reported ...`
  - generic mechanism language such as `The supported mechanism is limited` or `the evidence most strongly supports a descriptive account`
  - evidence sections that were numerically grounded but still too close to literature-summary tone instead of decision-grade synthesis

Operational lesson:
- do not assume passing structure + numeric payload checks are sufficient
- use accepted regenerated artifacts as positive controls and weaker regenerated artifacts as negative controls

Useful positive controls:
- `art-2026-03-03-001`
- `art-2026-03-02-025`

Useful negative-control pattern:
- regenerated articles like the earlier versions of `art-2026-03-04-003` and `art-2026-03-04-012` that felt too descriptive and under-emphasized concrete tension/mechanism framing

Validation hardening that worked:
- reject contradiction sections that rely on phrases like:
  - `no direct empirical contradiction is reported`
  - `no direct contradiction is visible`
  unless the section also names a concrete operational or empirical tension
- reject mechanism sections that rely on generic phrases like:
  - `the supported mechanism is limited`
  - `descriptive account`
  when a stronger bounded explanation is available from the evidence
- keep these checks inside article-write validation so weak style cannot slip through just because headings exist

Prompt/contract hardening that worked:
- explicitly tell the writer not to satisfy contradiction/tension with generic disclaimer language
- explicitly tell the writer not to satisfy mechanism/bounds with generic “descriptive account” fallback when bounded operational explanation is possible
- require concrete benchmark reversals, subgroup differences, cost/performance tradeoffs, adoption/attention mismatches, or similar decision-relevant tensions to be named when they exist

Recommended test pattern:
- keep one negative-control article fixture in tests that contains adequate sections and some numeric payload but still uses the weak generic contradiction/mechanism voice
- assert `validate_article_write_body(...)` fails with a dedicated error such as `article_write_weak_tension_or_mechanism`

### 10.5. Empirical-specificity validation must recognize percentage metrics

A later replay/debugging pass exposed a validator false-negative that can stall otherwise good historical remediation.

Observed failure mode:
- `validate_article_write_body(...)` is meant to fail thin descriptive artifacts when claims/evidence contain numeric payload but the visible article surface does not
- a regenerated article for `art-2026-03-21-013` correctly surfaced concrete benchmark numbers like `72.5%`, `49%`, and `43.2%`
- but the replay still failed closed with `article_write_missing_empirical_specificity`

Root cause:
- `_contains_numeric_payload(...)` used a regex that required a trailing word boundary after `%`
- percentages such as `72.5%` do not satisfy `\b` after `%` because `%` and the following space/punctuation are both non-word characters
- result: real percent-bearing evidence and article sections were misclassified as non-numeric

Fix that worked:
- broaden the detector so percent metrics are treated as numeric payload explicitly
- a robust pattern is to match either:
  - `\d+(?:\.\d+)?\s*%(?!\w)`
  - or the existing unit-style numeric forms like `x`, `ms`, `seconds`, `minutes`, `hours`, `repos`, etc.
- keep the soft-language numeric fallback such as `about 4`, `over 20`, `less than 3`

Why this matters operationally:
- otherwise replay can wrongly quarantine or fail an article that actually does surface concrete benchmark results
- this is especially important for agent-eval and benchmark-comparison sources where `%` is the dominant empirical surface

Verification to add:
1. a regression test where claims/evidence/article sections contain percentage metrics like `72.5%`, `49%`, and `43.2%`
2. assert `validate_article_write_body(...)` accepts the article when the dense sections clearly surface those numbers
3. keep the existing negative-control test where thin sectioned prose still fails for missing empirical specificity

Operational rule:
- when `article_write_missing_empirical_specificity` appears on an article that visibly contains percentages, inspect the numeric detector before blaming the writer output
- treat this as a validator bug class, not a content-quality failure, until the detector is confirmed correct

### 11. Verify identity before overreacting to regenerated wording changes

Another important operational lesson from remediation:
- regenerated artifacts can look very different from the old historical summaries even when they are the correct underlying item
- this often happens because the old article was weak and the replay is performing a real re-extraction and rewrite from the same source package

Before assuming the wrong paper was used, verify identity directly from package metadata:
- `article_id`
- `ticket_id`
- `source_url`
- `canonical_url`
- `imported_from_runtime_article_id`
- `source.md` title/body

A good verification pattern is:
- compare `article.md` frontmatter with `source.md`
- confirm the source capture still matches the intended paper/work
- then judge whether the regenerated article is a justified rewrite or a true mismatch

Practical nuance discovered in rollout:
- identity can be correct even when the old artifact and new artifact feel radically different
- that usually means the legacy summary underfit the source, not that replay selected the wrong work
- however, title normalization can still be imperfect (for example, `arXiv 2510.21413` as an article title when the source body clearly carries a fuller title), so treat title-surface cleanup as a separate packaging bug class rather than an identity failure

### 12. Title normalization for replayed papers needs a source-body fallback

A later remediation slice showed that replayed papers can still surface weak titles even after identity is correct.

Observed failure mode:
- `article.md` frontmatter and the rendered article title may keep a generic stub like `arXiv 2510.21413`
- meanwhile `source.md` clearly contains the descriptive paper title in the body text
- this makes the package look wrong even when the source identity is actually correct

Fix that worked:
- keep a helper like `_is_generic_arxiv_stub(title)` to detect titles such as:
  - `arXiv 2510.21413`
  - `arXiv 2602.11988`
  - versioned forms like `arXiv 2510.21413v1`
- in `source_title(...)`, do not automatically trust `article_meta["source_title"]` if it is only an arXiv stub
- prefer, in order:
  1. a non-stub `article_meta["source_title"]`
  2. a non-stub `source_meta["source_title"]`
  3. a descriptive title extracted from `source.md` body text
  4. only then fall back to the stub or URL
- when extracting from `source.md` body, skip lines like:
  - markdown headings
  - `Source:`
  - `Generated:`
  - `> Note:`
  - generic arXiv stub lines
  - bare `Introduction` headings
- choose the first plausible descriptive title line with enough words to be a real paper title

Practical verification that should be added:
- a test where `article_meta["source_title"]` is `arXiv 2510.21413` but `source_meta["source_title"]` is descriptive; the descriptive title must win
- a test where both metadata titles are arXiv stubs but `source.md` body contains the real title; the body-derived title must win
- rerun at least one affected real package after the fix and confirm both:
  - frontmatter `source_title` is corrected
  - the rendered article heading uses the descriptive paper title

Operational rule:
- if a replayed article feels like the wrong paper but ids/source URLs match, check title normalization before suspecting an identity mismatch
- weak title surfacing is often a packaging bug, not a replay-selection bug

### 13. Large historical replays can fail at the Hermes CLI boundary with `Argument list too long`

A later remediation batch exposed a new infrastructure-class replay failure on large imported packages.

Observed failure mode:
- `scripts/remediate_historical_imports.py` invokes `scripts/run_micro_article_lane.py`
- the lane eventually calls `run_loose_agent(...)` through `article_job_runtime.py`
- for some articles with very large source bodies or mission payloads, the underlying Hermes CLI invocation fails before the agent runs with:
  - `RuntimeError: [Errno 7] Argument list too long: 'hermes'`

Why this matters:
- this is not a content-quality rejection
- the package can remain stuck in `published` + `legacy_quarantined` simply because the replay transport is using an oversized command-line argument payload
- once one article hits this, nearby large-source historical packages may hit it too

Operational rule:
- when a remediation report shows `Argument list too long`, treat it as a replay/runtime transport bug first, not as evidence that the article should be discarded or remain quarantined
- do not move on casually; patch the transport so large missions are passed safely, then rerun the affected article id

Recommended implementation direction:
- inspect `scripts/micro_common.py` and the task-runner / Hermes CLI seam used by `run_loose_agent(...)`
- stop passing the full prompt/mission as a giant command-line argument when payloads can exceed OS argv limits
- keep the small-assignment fast path if desired, but add a large-payload fallback in `scripts/task_runner.py`
- the fix that worked in practice was:
  1. detect oversized assignments with a conservative byte threshold helper such as `should_use_file_prompt_transport(...)`
  2. write the full built assignment to a temp file
  3. invoke `sys.executable -c ...` with a tiny bootstrap that imports `cli.main`, reads the query from that temp file, sets `HERMES_SESSION_SOURCE='tool'`, and calls `cli_main(query=..., quiet=True, model=..., provider=...)`
  4. keep an additional retry fallback on `OSError errno == 7` so an unexpectedly large assignment still retries through the file-backed path
  5. delete the temp file in a `finally` block
- preserve the same bounded-task semantics and receipt behavior after changing transport

Why this implementation is good:
- it avoids changing Hermes CLI contracts
- it keeps receipts and output normalization in the current runner
- it removes argv size as the bottleneck while preserving one-shot isolation

Verification to add:
1. a regression test for the task-runner seam where a very large prompt body is submitted without using oversized argv payloads
2. an integration-style remediation test or seam test showing a large historical source can still reach Extractor without `Argument list too long`
3. rerun the previously failing article and confirm it transitions out of `legacy_quarantined` only based on actual lane outcome, not transport failure

Practical batch-handling guidance:
- if one article in a 3-item remediation batch fails this way while others succeed, keep the successful outputs
- record the failed article id explicitly as a replay transport blocker
- fix the transport bug before widening to the next set of similarly large historical packages

### 13. Task-runner retry noise can falsely fail otherwise valid persona outputs

A later backlog-processing slice exposed a task-runner classification bug in the Hermes seam.

### 13.5. Hermes activity-feed shell echo can leak into cleaned receipts and break frontmatter parsing

A later remediation batch exposed a new Hermes CLI chrome leak in the task-runner seam.

Observed failure mode:
- `normalize_output(...)` already stripped banner box-drawing lines and common emoji noise lines
- but Hermes activity-feed shell echo lines like:
  - `┊ 💻 $ date -u ...`
- were still surviving in `clean_output`
- Curator receipts then began with that shell-echo line instead of `---`
- downstream parsers failed closed with errors like:
  - `ValueError: missing_frontmatter`

Why this matters:
- the underlying Curator output can be perfectly valid
- but one leaked activity-feed line at the top makes the whole receipt unusable
- this failure can suddenly appear after CLI display changes even when Sapho prompts/jobs are unchanged

Fix that worked:
- broaden task-runner chrome stripping so the activity-feed prefix is treated as display noise too
- in practice, extending the box-drawing/noise prefix filtering to drop lines beginning with `┊` fixed the replay path
- keep a regression test with a raw payload that starts with:
  - `┊ 💻 $ ...`
  - followed by valid frontmatter
- assert normalized output starts directly at the receipt frontmatter

Operational rule:
- if Curator/Extractor/Synthesist suddenly fail with `missing_frontmatter`, inspect the latest task-runner receipt JSON before changing prompts
- treat leading shell/activity-feed text as a transport/display bug class first

### 13.6. Duplicate extractor receipts can survive deduping when the second copy ends with a stray closing fence

Another remediation slice exposed a subtler Extractor replay failure.

Observed failure mode:
- Extractor sometimes returned the same receipt twice in one response
- the second copy could end with an extra trailing closing fence like:
  - ````` ``` `````
- or the final evidence block could arrive without its closing fence at end-of-response
- `normalize_output(...)` and the evidence parser could then fail to collapse or fully parse the duplicate payload
- downstream result looked like:
  - `extractor_evidence_count_mismatch`
  - or, in some cases, a false `bounded_or_tension_evidence_missing_note`
  because the parser accidentally consumed the start of the duplicate receipt inside the final evidence block

Fixes that worked:
- harden `_collapse_exact_duplicate_payload(...)` so it recognizes duplicated receipts by receipt-signature, not only by first-line heuristics
- allow the duplicate-tail case where the second copy is identical except for a trailing stray closing fence
- harden `article_job_runtime._CODE_BLOCK_RE` so the final evidence block can still be parsed when the closing fence is missing at end-of-response, or when the next receipt starts immediately after it
- add regression tests for both:
  1. duplicate extractor receipt + stray trailing fence
  2. final evidence block with no closing fence

Prompt hardening that also helped:
- strengthen `jobs/extractor/evidence.md` to explicitly say the final evidence file must end with a closing fence before stopping

Operational rule:
- if replay fails with `extractor_evidence_count_mismatch` on an otherwise plausible receipt, inspect the stored extractor task-run receipt before editing article logic
- first check for duplicated receipts, trailing stray fences, or an unclosed final evidence block

### 13.7. Duplicate-rejected replay paths must refresh structured policy and publication-authority surfaces

A later batch exposed a policy-surface drift bug in the duplicate path.

Observed failure mode:
- an article could be replayed into `publication_status: duplicate-rejected`
- but if the duplicate branch returned early after writing only `article.md`, the older structured outputs could remain in place
- this left stale artifacts such as:
  - `historical-policy.json` still saying `current_law_compliant`
  - `publication-authority.json` still saying `verdict: pass`
- the visible article body looked correctly blocked, but the canonical machine-readable legality surfaces were stale and wrong

Fix that worked:
- in the duplicate-rejected branch of `run_micro_article_lane.py`, materialize the structured bundle before returning, just like the discarded path
- set terminal-state metadata first (`publication_status`, duplicate fields, zero counts as appropriate), then call `materialize_article_structured_bundle(...)`
- add a lane-level regression test asserting that a duplicate-rejected replay refreshes:
  - `historical-policy.json -> blocked_not_publishable`
  - `validation.json` remains structurally pass for the resolved duplicate surface
  - `publication-authority.json` blocks publication

Operational rule:
- any terminal blocked path (`discarded`, `capture-blocked`, `duplicate-rejected`) must rewrite the canonical structured/policy/authority surfaces before returning
- otherwise the visible article and the legal machine surfaces can drift apart

Observed failure mode:
- the provider could emit transient retry noise like:
  - `API call failed (attempt 1/3): RemoteProtocolError`
  - `Retrying in 2s...`
- then still return a valid final Curator/Extractor/Synthesist payload in the same raw output
- `normalize_output(...)` would correctly recover the valid payload
- but `classify_status(...)` still marked the run as `error` because it inspected the raw output for failure text
- the lane then failed closed with `backend_output_error` even though the final cleaned payload was usable

Fix that worked:
- treat the cleaned payload as authoritative for success/failure classification
- keep `looks_like_backend_failure(clean_output)` as a hard failure
- but do not mark the run `error` just because `raw_output` contains retry noise if `clean_output` is non-empty and valid
- preserve the hard failure case when raw output contains backend failure text and the cleaned output is empty

Practical implementation shape:
- in `task_runner.classify_status(...)`:
  - fail on explicit `error`
  - fail if `clean_output` itself still looks like backend failure text
  - fail if raw output looks like backend failure text and `clean_output` is empty
  - otherwise allow success classification to proceed

Verification to add:
1. a regression test where raw output contains retry/failure lines plus a valid final receipt payload and status becomes `ok`
2. keep the existing regression where pure backend failure text with no valid payload still becomes `error`

Why this matters operationally:
- once the rail is stable enough to run larger 6-item batches, transient upstream retry noise is more likely to appear
- if the runner treats every noisy-but-recovered output as fatal, batch throughput drops for the wrong reason
- the fix preserves fail-closed behavior for real failures while allowing successful recovered runs to count

### 14. Historical replay can hit OS argv limits on large one-shot assignments

A later remediation batch exposed another replay-path failure class:
- historical packages with large captured sources can build very large one-shot assignments for Curator / Extractor / Synthesist
- when the task runner shells out as `hermes chat -q <very large assignment>`, the process can fail before model execution with:
  - `[Errno 7] Argument list too long: 'hermes'`

This is not a content judgment failure.
It is an invocation-transport failure caused by putting too much prompt text into argv.

Fix that worked:
- keep the normal direct `hermes chat -q ...` path for small assignments
- add a size threshold or OSError fallback in `scripts/task_runner.py`
- when the assignment is too large, write the full prompt to a temporary file
- invoke Python directly and call Hermes CLI entrypoints from code, reading the prompt from that file instead of passing it on the command line
- clean up the temp file after the subprocess completes

A robust implementation pattern is:
- keep `build_hermes_command(...)` for the normal path
- add helpers like:
  - `should_use_file_prompt_transport(...)`
  - `build_python_file_prompt_command(...)`
- in `run_task(...)`, either:
  - proactively switch to file transport above a soft byte limit, or
  - catch `OSError(errno=7)` and retry once through file transport

Important nuance discovered in rollout:
- piping to `stdin` is not necessarily safe if the Hermes CLI command path assumes TTY-ish behavior or only officially supports `-q`
- calling the CLI entrypoint from Python with `cli.main(query=...)` while loading the large prompt from a temp file avoids argv overflow without depending on unsupported shell piping semantics

Recommended verification to add:
1. a regression test where a very large assignment routes through file transport instead of argv
2. assert the subprocess command is Python-based, points at a temp prompt path, and does not contain the giant prompt text inline
3. rerun the previously failing historical article after the fix and confirm replay succeeds end-to-end

Operational lesson:
- if a replay fails with `Argument list too long`, do not treat it as article-specific quality failure
- fix the prompt transport once, rerun the blocked article, then continue the remediation batch

### 14. Percent-style empirical metrics can be falsely rejected if validators only detect `\b...%\b`

A later historical remediation slice exposed a subtle validator bug in the article-write quality gate.

Observed failure mode:
- a regenerated article could surface concrete metrics like:
  - `72.5%`
  - `49%`
  - `43.2%`
- the article still failed with:
  - `article_write_missing_empirical_specificity`
- root cause was the numeric-payload detector using a regex shape like `\b\d+(?:\.\d+)?\s*%\b`
- `%` is not a word character, so the trailing `\b` after `%` can prevent otherwise valid percent metrics from matching

Why this matters:
- this is a false fail-closed rejection, not a real article-quality miss
- coding/evaluation benchmark articles often carry their decisive evidence as percentages
- if the detector misses percent forms, lawful dense articles can remain quarantined for the wrong reason

Fix that worked:
- replace the percent/unit matcher with a pattern that does not rely on a trailing word boundary after `%`
- a robust pattern is to separate `%` from word-unit cases, for example:
  - `\b\d+(?:\.\d+)?(?:\s*%(?!\w)|\s*(?:x|k|m|ms|s|sec|seconds?|minutes?|hours?|turns?|instances?|repos?(?:itories)?)\b)`
- keep the qualitative numeric fallback too, such as:
  - `about 4`
  - `over 20`
  - `more than 10`

Verification to add:
1. a regression test where claims/evidence contain percent metrics and the article surfaces the same percentages in `Key Findings` / `Evidence and Findings`
2. assert `validate_article_write_body(...)` passes instead of raising `article_write_missing_empirical_specificity`
3. rerun the previously blocked historical article and confirm it transitions based on true article quality, not regex failure

Practical example from rollout:
- `art-2026-03-21-013` initially failed replay despite surfacing benchmark-specific percentages
- after patching the detector and adding a regression test, replay succeeded and the package moved to `current_law_compliant`

### 15. Formal publication authority should be a canonical gate layer, not scattered status checks

A later roadmap slice clarified an important architectural gap:
- `validation.json` existing is not the same thing as having a formal publication-authority layer
- artifact publication and Daily publication can still rely on scattered checks such as `publication_status`, artifact-current checks, or Conclave output parsing in individual scripts
- this leaves Hermes/Piter and downstream site/render flows operating over an implicit state machine instead of one explicit authority surface

What the formal gate should do:
- evaluate article-level publication authority from canonical package surfaces
- evaluate Daily-level publication authority from article authority + Conclave verdict + artifact-current checks
- write durable decision objects such as `publication-authority.json`
- fail closed before publication-state mutation when authority does not pass

A good implementation pattern that worked:
- add a dedicated module such as `scripts/publication_authority.py`
- for article scope, require at minimum:
  - `publication_status` is in a publishable state like `ready-for-daily` or `published`
  - `validation.json.overall_status == pass`
  - if `historical-policy.json` applies, `current_law_eligible` must be true
- for Daily scope, require at minimum:
  - every included article passes article authority
  - every included article has current artifact publication state
  - Conclave verdict is `pass`
- write the authority decision to:
  - `articles/<article_id>/publication-authority.json`
  - `daily/<date>/publication-authority.json`

Important wiring rule:
- `run_micro_artifact_publish.py` should assert article publication authority before publishing artifact surfaces
- `run_micro_daily.py` should assert daily publication authority after Conclave verdict is produced and before mutating articles to `published`
- this turns authority into a true gate instead of a descriptive afterthought

Important parser hardening discovered in the same slice:
- if the Conclave prompt requires dossier frontmatter like:
  - `verdict: pass|block|withdraw`
- then the runtime parser must accept frontmatter-style verdict lines, not only plain leading `PASS` / `BLOCK` text
- otherwise the prompt contract and runtime parser drift apart in a brittle way

Recommended tests to add:
1. article authority blocks on failed `validation.json`
2. article authority blocks on `historical-policy.json.current_law_eligible == false`
3. Daily authority blocks when an included article's artifact publication is not current
4. Daily authority passes only when article authority passes and Conclave verdict is `pass`
5. gate parser accepts dossier frontmatter lines like `verdict: pass`

Why this matters:
- it gives Hermes/Piter a canonical legal/control surface to watch and explain
- it makes Website 2.0 and later publication surfaces render from explicit authority rather than inferred status
- it closes the gap between "validators exist" and "Conclave/publication authority is truly formalized"

### 16. Batch remediation reporting should include direct GitHub review links

A user workflow correction changed the preferred reporting format for historical remediation batches:
- do not only report statuses and local paths
- include direct clickable GitHub links so the user can immediately inspect regenerated packages in the repo UI

Useful links per article are:
- commit link for the remediation slice
- article package tree
- `article.md`
- `validation.json`
- `historical-policy.json`
- when relevant for blocked/discarded cases, `micro-worthiness.md`
- report JSON under `state/reports/`

Recommended response pattern after each committed batch:
- start with the pushed commit SHA and GitHub commit URL
- list each article outcome (`current_law_compliant`, `blocked_not_publishable`, or still quarantined/failing)
- attach the clickable GitHub links under each article so the user can browse immediately

This is not just presentation polish; it materially improves operator review speed for GitHub-visible artifact packages.

### 17. Hermes task-runner output can regress by leaking activity-feed shell echoes into receipts

A later remediation batch exposed a Hermes-seam parser failure that is worth checking immediately if Curator or Extractor suddenly starts failing on `missing_frontmatter` despite apparently successful runs.

Observed failure mode:
- task receipts contained a leading activity-feed shell line such as:
  - `┊ 💻 $         date -u +"%Y-%m-%dT%H:%M:%SZ"  0.6s`
- the actual Curator/Extractor receipt followed underneath and was otherwise valid
- `normalize_output(...)` did not strip the line because it only knew classic box-drawing chrome and not the activity-feed prefix
- downstream `parse_markdown(...)` then failed with:
  - `missing_frontmatter`

Practical fix that worked:
- treat the activity-feed prefix `┊` as Hermes CLI chrome in `task_runner.normalize_output(...)`
- keep the cleaned payload starting at the first real frontmatter line, not at the shell echo
- add a regression test with a leading `┊ 💻 $ ...` line before a valid receipt and assert the normalized output starts with the receipt frontmatter

Operational rule:
- when a replay suddenly fails at Curator with `missing_frontmatter`, inspect the latest task-run receipt before blaming the persona contract
- if the receipt body is present but preceded by Hermes activity-feed noise, patch normalization first

### 18. Duplicate-rejected replay paths must refresh structured policy and authority surfaces

A later batch exposed an important terminal-state drift bug.

Observed failure mode:
- an imported article replayed into `duplicate-rejected`
- `article.md` was updated to the duplicate-rejected terminal surface
- but `historical-policy.json` and `publication-authority.json` were left stale from the previous lawful run
- this incorrectly left the package looking `current_law_compliant` even though it was now blocked from publication

Practical fix that worked:
- in the duplicate-conflict branch of `run_micro_article_lane.py`, do not only rewrite `article.md`
- also:
  - set terminal metadata such as `publication_status`, `duplicate_of_article_id`, and duplicate timestamp
  - zero `evidence_count` / `claim_count` for the blocked terminal surface
  - call `materialize_article_structured_bundle(...)` with the duplicate-rejected body before returning
- this refreshes:
  - `validation.json`
  - `historical-policy.json`
  - downstream `publication-authority.json` when reevaluated

Expected terminal outcome after the fix:
- `publication_status: duplicate-rejected`
- `historical-policy.json.policy_status: blocked_not_publishable`
- article publication authority verdict: `block`

Recommended verification:
- add a lane-level regression test where Curator keeps but `find_kept_canonical_conflict(...)` returns a duplicate
- assert the article becomes `duplicate-rejected`
- assert `historical-policy.json` changes to `blocked_not_publishable`
- assert validation still passes the duplicate check as a correctly blocked package

### 19. Extractor receipt parsing should tolerate a missing closing fence on the final evidence block

A later batch exposed another replay-path fragility in Extractor receipt parsing.

Observed failure mode:
- the final evidence block in an Extractor receipt could be otherwise complete but omit the closing triple-backtick at end-of-response
- `_CODE_BLOCK_RE` expected every block to end with an explicit closing fence
- result:
  - the last evidence unit was silently dropped during parsing
  - `parse_evidence_receipt_files(...)` returned one fewer evidence item than the declared count
  - the lane failed closed with `extractor_evidence_count_mismatch`

Practical fixes that worked:
- tighten the Extractor prompt to explicitly say the final evidence block must also close before stopping
- harden `_CODE_BLOCK_RE` / receipt parsing so the final block can still be parsed when it reaches end-of-string without the closing fence
- add a regression test where the last block lacks the final closing fence and parsing still returns the full evidence list

Operational rule:
- when Extractor fails with `extractor_evidence_count_mismatch` and the receipt visually looks almost correct, inspect whether the last block was dropped due to a missing final fence before assuming the evidence count itself is wrong

### 13. When replay surfaces a clear contract bug, fix it proactively before continuing the batch

A later user correction clarified the expected Piter/operator behavior during remediation:
- if a batch failure clearly points to a prompt/contract bug in the current replay path, do not stop at reporting the error
- patch the contract promptly, rerun the affected article, and only then continue the historical batch campaign

Concrete example that should now be treated as routine:
- Extractor emitted a receipt for `art-2026-03-04-029` with `evidence_count: 14`
- but the receipt body actually contained 18 evidence file blocks
- the lane correctly failed closed with `extractor_evidence_count_mismatch`

Preferred fix pattern:
- strengthen `jobs/extractor/evidence.md` so Extractor drafts evidence blocks first and sets `evidence_count` last
- explicitly instruct: count the final `### file:` blocks and copy that exact integer into `evidence_count`
- rerun the failed article immediately after the prompt patch
- if the rerun succeeds, commit the prompt fix and regenerated package in the same slice so the fix is tied to a real recovered artifact

Operational rule:
- treat obvious contract drift like this as a system bug to repair, not just an article outcome to log
- preserve fail-closed runtime checks, but also close the loop by hardening the prompt/contract that produced the bad receipt

## Good next steps after this skill

With real Synthesist contradiction/mechanism review steps now present, the next likely step is:
- keep `validation.json` as the canonical package-level result surface
- backfill structured internals across existing imported article packages
- materialize `historical-policy.json` so imported legacy packages are explicitly classified as quarantined, blocked, or current-law compliant
- migrate the live article lane from micro compatibility prompts onto bounded Curator admission, Extractor evidence, Synthesist article-claims, and Synthesist article-write jobs
- tighten the article artifact contract so public `article.md` surfaces dense empirical findings, contradiction/tension, mechanism-or-bounds, and Sapho-relevance directly
- let fail counts shrink only when those charter-native outputs actually exist on each eligible package
