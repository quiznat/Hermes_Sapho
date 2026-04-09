<details class="traceability-panel">
<summary>Traceability</summary>
<div class="traceability-body">
<ul>
  <li><strong>Source:</strong> <a href="https://arxiv.org/html/2512.18470v1" target="_blank" rel="noopener">https://arxiv.org/html/2512.18470v1</a></li>
  <li><strong>Intake queued:</strong> 2026-03-10T04:03:59Z</li>
  <li><strong>Source captured:</strong> 2026-04-05T14:42:47Z</li>
  <li><strong>Curated:</strong> 2026-04-09T11:50:55Z</li>
  <li><strong>Artifact finalized:</strong> 2026-04-09T11:53:03Z</li>
  <li><strong>Artifact published:</strong> 2026-04-09T12:05:35Z</li>
</ul>
</div>
</details>

# SWE-EVO: Benchmarking Coding Agents in Long-Horizon Software Evolution Scenarios

## Core Thesis

SWE-EVO is a deliberately harder coding-agent benchmark built from real release-to-release software evolution work in seven mature Python repositories, and its results show that current agent stacks degrade sharply when tasks expand from localized bug repair into wider, regression-sensitive maintenance changes.

## Why It Matters for Sapho

This matters because it pushes against a flattering evaluation regime for coding agents. If agents score well on narrower repair benchmarks but fall from 65% on SWE-Bench Verified to 21% on SWE-EVO under the paper’s reported GPT-5 plus OpenHands setup, then Sapho should treat “software engineering ability” claims as benchmark-contingent rather than field-settled. The benchmark also sharpens evaluation doctrine: long-horizon code change is not just about generating a patch, but about surviving large change surfaces and heavy regression pressure at release boundaries.

## Key Findings

- The benchmark contains 48 tasks drawn from release-note-defined or SRS-defined changes across seven mature open-source Python projects, using version-tagged repository transitions rather than synthetic prompts.
- SWE-EVO instances are materially large change problems: the mean gold patch touches 20.9 files, 51.0 functions, and 610.5 edited lines.
- Evaluation is strict and execution-heavy: the mean instance has 81.4 FAIL_TO_PASS tests and 874.0 total tests, and a candidate receives a failed Fix Rate score if it breaks any PASS_TO_PASS test.
- Reported agent performance drops sharply relative to easier repair settings: GPT-5 with OpenHands scores 21% on SWE-EVO versus 65% on SWE-Bench Verified.
- Adding PR or issue context helps only modestly: with release-note plus PR or issue context, gpt-5-08-07 resolves 18.75% of SWE-EVO under OpenHands and 20.83% under SWE-agent, leaving most instances unsolved.
- The benchmark’s own scope is bounded: it covers only Python and only 48 instances, which the authors explicitly note limits fine-grained statistical comparison.

## Evidence and Findings

- The benchmark is built through a three-stage pipeline: repository selection and data scraping, candidate selection and filtering, and execution-based filtering. It seeds from SWE-bench and SWE-gym to inherit repository snapshots, executable environments, and tests tied to human-authored changes, then narrows to cases where a base commit exactly matches a version tag and the task is defined by the release-note or SRS delta to the next tagged version. That supports the claim that SWE-EVO is anchored in real release evolution work rather than arbitrary task invention.
- Task scale is not cosmetic. Table-level statistics show a mean gold patch of 610.5 edited lines across 20.9 files and 51.0 functions, and the abstract rounds this to roughly 21 files per task. That supports the judgment that these are structurally long-horizon software evolution problems with broad coordination surfaces, not small isolated edits.
- Validation burden is unusually high. The mean SWE-EVO instance carries 81.4 FAIL_TO_PASS tests and 874.0 total tests, and the evaluation rule assigns an instance score of zero under Fix Rate if any PASS_TO_PASS test regresses. That means partial repair is not enough: a candidate must both solve failing behavior and preserve existing behavior under substantial executable scrutiny.
- The benchmark is empirically harder for current coding-agent setups. In the paper’s reported experiments, GPT-5 with OpenHands reaches 21% on SWE-EVO versus 65% on SWE-Bench Verified, while release-note-plus-PR/issue context lifts resolution only to 18.75% under OpenHands and 20.83% under SWE-agent. This supports the conclusion that current agents lose substantial capability when software tasks become release-scoped, larger-surface, and regression-intolerant.
- Construction is also quality-gated before evaluation. Stage III retains only candidates with at least one FAIL_TO_PASS test and removes cases with installation or runtime errors. That matters because benchmark difficulty is not being driven simply by broken environments or non-executable instances; the benchmark is filtered toward tasks that can actually be run and judged.

## Contradictions and Tensions

- The evaluation regime creates a real tension between repair progress and benchmark success: a patch can fix some failing tests and still receive a zero instance score if it breaks any previously passing behavior. That makes the benchmark more faithful to maintenance constraints, but it also means headline success rates compress partial progress into failure.
- Added context does not solve the core difficulty. PR or issue context produces measurable improvement, but only modestly, which cuts against a simple story that current agents mainly fail because they lack enough surrounding documentation.
- The benchmark is presented as evidence of materially harder long-horizon software evolution, but its current empirical base is narrow: Python only, seven projects, 48 instances. That supports the direction of the claim while limiting confidence in stronger cross-language or cross-ecosystem generalization.
- The benchmark’s large edit surfaces and heavy test burden align with the observed performance drop, but the paper does not isolate which factor is doing the most causal work. Scope, coordination demands, validation strictness, and scaffold behavior remain entangled.

## Mechanism or Bounds

The strongest supported operational explanation is that SWE-EVO binds agents to release-scoped changes with wide edit surfaces and strict regression-sensitive execution checks. A system must interpret release deltas, coordinate modifications across roughly 21 files and 51 functions on average, and survive test suites averaging 874 checks without breaking previously passing behavior. That combination plausibly explains why performance is much lower than on narrower repair benchmarks. The causal account is still bounded, however: the evidence shows correlated difficulty under this benchmark design, not a clean ablation proving whether change scope, context form, scaffold limits, or fail-on-regression scoring is the dominant driver.

## Limits

The benchmark covers only Python projects and only 48 instances, and the authors explicitly note that this limits statistical power for fine-grained comparisons. The evidence supports a strong claim that current coding-agent setups struggle more under this benchmark than on SWE-Bench Verified, but it does not establish a universal ranking across agent architectures or software domains. The paper also does not fully disentangle why performance drops so sharply, so the mechanism remains operationally plausible rather than causally isolated.
