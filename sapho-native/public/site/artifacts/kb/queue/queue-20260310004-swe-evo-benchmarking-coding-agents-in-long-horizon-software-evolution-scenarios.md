<details class="traceability-panel">
<summary>Traceability</summary>
<div class="traceability-body">
<ul>
  <li><strong>Source:</strong> <a href="https://arxiv.org/html/2512.18470v1" target="_blank" rel="noopener">https://arxiv.org/html/2512.18470v1</a></li>
  <li><strong>Intake queued:</strong> 2026-03-10T04:03:59Z</li>
  <li><strong>Source captured:</strong> 2026-04-05T14:42:47Z</li>
  <li><strong>Curated:</strong> 2026-04-05T14:57:12Z</li>
  <li><strong>Artifact finalized:</strong> 2026-04-05T14:59:27Z</li>
  <li><strong>Artifact published:</strong> 2026-04-05T15:14:34Z</li>
</ul>
</div>
</details>

# SWE-EVO: Benchmarking Coding Agents in Long-Horizon Software Evolution Scenarios

## Core Thesis

SWE-EVO is a deliberately harder benchmark for coding agents: instead of short bug-fix tasks, it asks models to implement release-note changes inside full pre-release codebases, then grades them under strict no-regression rules. On that setup, strong agents that score well on SWE-bench Verified resolve far fewer tasks, which indicates that long-horizon software evolution remains substantially unsolved even when richer repository context is provided.

## Why It Matters for Sapho

This matters because it cuts against the easy story that coding-agent progress on established benchmarks transfers cleanly to real software evolution work. The paper shows that broader implementation scope, heavier verification burden, and instruction-following breakdowns can keep resolution rates low even for frontier models. For Sapho, that argues for evaluating agent capability under stricter, workflow-shaped conditions rather than taking short-horizon benchmark wins as sufficient evidence of operational readiness.

## Key Findings

- SWE-EVO contains 48 tasks from 7 mature open-source Python projects, with each task framed as implementing a release-note item against the full pre-release repository rather than fixing a narrow isolated defect.
- The benchmark’s gold patches are large by benchmark standards, averaging 610.5 edited lines across 20.9 files and 51.0 functions, which makes the tasks materially broader than typical short patch exercises.
- Verification is heavy: instances average 81.4 FAIL_TO_PASS tests and 874.0 total tests, so success requires surviving a substantial execution burden rather than merely producing a plausible-looking patch.
- gpt-5-08-07 resolved only 18.75% of SWE-EVO tasks in OpenHands and 20.83% in SWE-agent when given release-note plus PR/issue context, versus 65.00% on SWE-bench Verified.
- In the release-note-only setting, the same model resolved 14.58% in OpenHands and 16.67% in SWE-agent, so added PR/issue context helped, but only modestly.
- More than 60% of unresolved trajectories for gpt-5 were labeled as instruction-following failures, pointing to execution discipline and specification adherence as major observed failure modes, not just missing context.

## Evidence and Findings

- The benchmark is built around software evolution rather than narrow repair: the model receives a release-note item plus the full pre-release codebase, and the underlying gold solutions average 610.5 edited lines across 20.9 files and 51.0 functions. That supports the conclusion that SWE-EVO tests broader repository-scale change implementation, which matters because agent performance on compact bug-fix tasks may not carry over to this larger operational regime.
- SWE-EVO’s verification burden is substantial, with 81.4 FAIL_TO_PASS tests and 874.0 total tests per instance on average. This supports the conclusion that the benchmark pressures agents on correctness and regression avoidance at scale, which matters because many apparently reasonable patches can fail once subjected to full test execution.
- Performance drops sharply relative to a widely used prior benchmark: with release-note plus PR/issue context, gpt-5-08-07 resolves 18.75% of tasks in OpenHands and 20.83% in SWE-agent, compared with 65.00% on SWE-bench Verified. That supports the conclusion that long-horizon software evolution remains much harder than standard benchmark narratives imply, which matters because headline benchmark competence may overstate deployment readiness.
- Extra repository context helps only a little: release-note-only results were 14.58% in OpenHands and 16.67% in SWE-agent, rising only modestly when PR/issue context was added. This supports the conclusion that missing textual context is not the sole bottleneck, which matters because simply feeding agents more surrounding discussion is unlikely to close the capability gap.
- Failure analysis attributes more than 60% of unresolved gpt-5 trajectories to instruction-following failures. That supports the conclusion that a major part of the observed difficulty lies in faithfully executing the requested change process, which matters because agent weakness here is not just search or retrieval failure but breakdown in carrying the task through according to specification.
- The benchmark is intentionally conservative in both construction and scoring: it keeps only executable, testable candidates with at least one FAIL_TO_PASS test; counts a task as resolved only if all FAIL_TO_PASS and PASS_TO_PASS tests pass; and gives an instance a Fix Rate of 0 if any PASS_TO_PASS test regresses. That supports the conclusion that SWE-EVO is designed to punish partial wins that introduce regressions, which matters because low scores here are meant to reflect production-relevant strictness rather than relaxed patch plausibility.

## Contradictions and Tensions

- Richer PR/issue context improves results only modestly, even though one obvious interpretation of long-horizon failure is that agents lack enough surrounding context. The tension is that more context helps, but far too little to explain the full gap to SWE-bench Verified.
- The paper identifies instruction-following failure as a major contributor to unresolved runs, but that does not cleanly separate it from other burdens such as repository scale, test load, or task ambiguity. The tension is that the observed dominant failure label may be real without being the whole causal story.
- The benchmark is strict in ways that are decision-relevant, especially its no-regression scoring, but that same strictness can compress partial progress into very low visible scores. The tension is that the results are more operationally serious precisely because they are conservative, while also becoming harder to compare directly with looser benchmark regimes.
- Difficulty appears to rise with repository-history complexity, with mean pull-request counts of 14.84, 6.71, 3.57, and 1.67 from hardest to easiest groups. That is useful as a practical difficulty signal, but it is still only a proxy, creating tension between an intuitively plausible explanation and a fully established mechanism.

## Mechanism or Bounds

The strongest supported explanation is bounded rather than fully causal: SWE-EVO combines broader repository-scale change scope, high verification burden, and strict no-regression scoring, while many unresolved trajectories show instruction-following breakdowns. Together, that supports an operational picture in which agents struggle not only to locate relevant code but to carry out multi-file, specification-shaped changes without violating existing behavior. The evidence does not isolate which factor dominates, and the failure-mode analysis is attributional rather than experimental, so the mechanism should be read as a constrained explanation of observed benchmark behavior, not a definitive causal decomposition.

## Limits

The benchmark currently covers only Python projects, uses release notes as the task specification, and contains 48 instances, which the authors say limits statistical power for fine-grained comparisons. The instruction-following result comes from LLM-as-a-judge analysis of unresolved trajectories rather than direct causal intervention. Pull-request count is used as a practical proxy for difficulty, not a proven driver. The paper therefore supports a strong within-benchmark conclusion that long-horizon software evolution is hard under strict evaluation, but it does not by itself justify broad claims about all languages, all development workflows, or the precise cause of agent failure.
