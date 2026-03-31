# Execution Substrate Replacement Spec

Status: draft
Date: 2026-03-31
Author: Hermes
Purpose: define the replacement for the current OpenClaw disposable worker execution seam used by the Daily Rail.

## 1. Scope

This spec covers replacement of the current micro execution substrate only.

Current seam:
- `micro_common.py` -> `run_loose_agent()` -> `openclaw_pocket_agent.py`

Goal:
- preserve current rail behavior while swapping out the worker backend

Out of scope:
- broad redesign of higher-level production logic
- Canon execution patterns

## 2. Replacement goal

The replacement substrate must allow the current Daily Rail to keep doing the same cognitive steps:
- Curator worthiness
- Findings extraction
- Facts extraction
- Synthesist article summary
- Synthesist cluster/technical/executive daily outputs
- Conclave pass/block review

The first phase should be backend replacement, not business-logic reinvention.

## 3. Current behavior that must be preserved

The current substrate provides:
- role-based execution (`curator`, `extractor`, `synthesist`, `orchestrator/conclave`)
- one-shot isolated task execution
- timeout control
- plain-text output only
- output sanitization
- no dependency on agent persistence between calls
- compatibility with the existing prompt/job files

These properties should be preserved.

## 4. Core interface

The replacement substrate should expose one canonical interface:

`run_task(role, prompt, timeout, thinking, context=None) -> TaskResult`

### Input fields
- `role`: logical role name
- `prompt`: full instruction text to execute
- `timeout`: seconds
- `thinking`: provider/backend-specific reasoning mode hint
- `context` optional: structured metadata like article_id/date/stage for receipts and logging

### Output object: `TaskResult`
Required fields:
- `status`: `ok | error | timeout | malformed`
- `role`
- `raw_output`
- `clean_output`
- `started_at_utc`
- `finished_at_utc`
- `duration_seconds`
- `backend`
- `model`
- `error` optional

Rule:
`clean_output` is the canonical thing returned to micro jobs.

## 5. Compatibility adapter layer

The current micro code expects:
- `run_loose_agent(role, prompt, timeout, thinking) -> plain_text`

Therefore the first implementation step should be an adapter that preserves this shape.

Example logical layering:
- `micro_common.run_loose_agent()`
  -> `task_runner.run_task(...)`
  -> return `TaskResult.clean_output`

This allows higher-level scripts to stay unchanged initially.

## 6. Required functional properties

### 6.1 One-shot isolation
Each task invocation should be independent.
No hidden dependence on previous session state.

### 6.2 Role mapping
The replacement must support current logical roles:
- `curator`
- `extractor`
- `synthesist`
- `orchestrator`

Optional future extension:
- `mechanist`
- `adversary`

### 6.3 Prompt file compatibility
Existing prompt/job files should work without immediate rewrite.
The substrate must be able to accept the current plain-text prompts.

### 6.4 Timeout semantics
A timed-out task should produce:
- `status=timeout`
- structured error info
- no silent partial success

### 6.5 Sanitization semantics
The substrate must normalize outputs by at least:
- stripping code fences where configured
- stripping CLI noise or platform noise
- normalizing blank-line runs
- preserving plain text content intended for downstream parsers

### 6.6 No hidden workspace mutation
The substrate should not create invisible state that becomes required for future correctness.

## 7. Non-functional requirements

### 7.1 Determinism preference
Exact determinism is impossible, but the system should favor stable output behavior by:
- using role-stable prompt wrappers
- using constrained output contracts
- keeping temperature/reasoning defaults consistent per role where possible

### 7.2 Observability
Every invocation should be observable enough to debug failures.
Recommended task receipt fields:
- role
- stage
- article/date context
- timeout
- backend/model
- duration
- status
- optional prompt hash

### 7.3 Replaceability
The backend should be provider-agnostic enough that a future routing change does not require rewriting production scripts.

## 8. Suggested internal architecture

### Layer 1: role registry
Maps logical role to execution defaults.

Example fields per role:
- preferred model
- output mode
- timeout class
- reasoning mode default
- sanitizer profile

### Layer 2: task runner
Implements the `run_task()` interface.
Handles:
- invocation
- timing
- errors
- cleanup
- receipts

### Layer 3: output normalizer
Handles:
- plain-text cleanup
- code-fence stripping
- internal-id leakage checks where relevant
- malformed-output classification

### Layer 4: compatibility adapter
Exposes the current simple `run_loose_agent()` shape to the Daily Rail scripts.

## 9. Role default suggestions

### Curator
Characteristics:
- fast
- concise
- binary gate with rationale

Suggested defaults:
- low-latency model
- low reasoning
- strict text normalization

### Extractor
Characteristics:
- precise extraction
- structure-sensitive

Suggested defaults:
- extraction-friendly model
- moderate reasoning if needed
- stricter schema-oriented cleanup

### Synthesist
Characteristics:
- higher-quality prose and synthesis

Suggested defaults:
- stronger synthesis-capable model
- moderate reasoning
- preserve section formatting carefully

### Conclave / Orchestrator
Characteristics:
- judgment over frozen dossier

Suggested defaults:
- reliable reasoning model
- strict output contract
- low tolerance for malformed output

## 10. Failure model

The substrate should classify failures clearly.

### `error`
Examples:
- backend API failure
- missing credentials
- provider unavailable

### `timeout`
Examples:
- task exceeded timeout

### `malformed`
Examples:
- no usable output
- output violates required contract too severely to parse

### `ok`
Usable output available

Rule:
Malformed is a first-class status, not just an exception message.
This matters because Curator/Conclave failures may need explicit fallback policy.

## 11. Fallback behavior expectations

The substrate should not itself decide domain fallbacks like:
- default Curator to discard
- default Conclave to block

Those are rail/policy concerns above the substrate.

The substrate should only report:
- task succeeded
- task failed
- task timed out
- task output malformed

The Daily Rail scripts or validators can then apply policy fallback.

## 12. Receipt requirements

Each task run should emit a receipt or log entry with at least:
- `task_id`
- `role`
- `context`
- `backend`
- `model`
- `started_at_utc`
- `finished_at_utc`
- `duration_seconds`
- `status`
- `prompt_hash`
- `error` if any

Optional but useful:
- `output_hash`
- `sanitizer_profile`
- `thinking_mode`

These do not need to be public. They are operational receipts.

## 13. Migration plan

### Phase A: compatibility swap
Replace only the backend under `run_loose_agent()`.
No change to prompt files or higher-level scripts.

### Phase B: receipt hardening
Add richer task receipts and better malformed-output reporting.

### Phase C: schema-oriented role tuning
As upgraded persona output contracts land, tune the substrate for more structured outputs.

Important rule:
Do not couple Phase A to schema redesign. Keep the first cut narrow.

## 14. Success criteria

The replacement substrate is successful when:
- the current Daily Rail runs end-to-end without OpenClaw disposable workers
- task failures are easier to inspect than before
- output cleanliness is at least as good as current behavior
- higher-level scripts do not need a major rewrite for the first migration
- Piter 2.0 can debug and repair the substrate more easily than the current OpenClaw worker path

## 15. Anti-goals

Do not build:
- a giant autonomous planning runtime here
- persistent hidden agent state
- a new institution-wide orchestration fabric before the Daily Rail runs

This substrate should be narrow and boring.
That is its virtue.

## 16. Bottom line

The execution substrate replacement should be the smallest possible change that removes the main OpenClaw dependency while preserving the proven Daily Rail behavior.

Do the seam swap first.
Then improve structure, validation, and control-plane behavior above it.
