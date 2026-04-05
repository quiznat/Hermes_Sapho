<details class="traceability-panel">
<summary>Traceability</summary>
<div class="traceability-body">
<ul>
  <li><strong>Source:</strong> <a href="https://arxiv.org/abs/2602.10975" target="_blank" rel="noopener">https://arxiv.org/abs/2602.10975</a></li>
  <li><strong>Intake queued:</strong> 2026-03-10T06:02:29Z</li>
  <li><strong>Source captured:</strong> 2026-04-05T15:03:32Z</li>
  <li><strong>Curated:</strong> 2026-04-05T15:03:47Z</li>
  <li><strong>Artifact finalized:</strong> 2026-04-05T15:06:28Z</li>
  <li><strong>Artifact published:</strong> 2026-04-05T15:14:35Z</li>
</ul>
</div>
</details>

# FeatureBench: Benchmarking Agentic Coding for Complex Feature Development

## Core Thesis

FeatureBench argues that current coding-agent evaluation is materially easier than real feature development and introduces a larger execution-based benchmark aimed at feature-level work that spans broader repository context, longer specifications, and multi-file implementation demands. On the reported results, present-day agents that score strongly on SWE-bench degrade sharply on this benchmark, indicating that feature construction remains a much weaker capability than bug-fix-style benchmark performance suggests.

## Why It Matters for Sapho

This matters because benchmark wins on narrow software tasks can overstate actual engineering autonomy. If a benchmark better approximates feature construction rather than localized repair, then the field needs a stricter read on what “agentic coding” currently means in production terms. For Sapho, the paper supports a doctrine of separating patch-level competence from sustained feature-building competence, and of treating benchmark design details, prompt scaffolding, and repository structure as part of the evaluation claim rather than as background noise.

## Key Findings

- FeatureBench is positioned as a benchmark for feature-level software work rather than single-pull-request bug repair, using traced unit tests and repository dependency structure to recover tasks tied to larger implementations.
- The collection pipeline is mostly automated and test-driven: tasks are derived execution-first from repositories, while the only reported manual step is environment setup at about 3 minutes per repository, totaling under 1 hour across 24 repositories.
- The first release is substantial in size: 200 evaluation tasks, 3,825 executable environments, and 24 open-source repositories.
- Reported difficulty is far above SWE-bench. Claude 4.5 Opus is reported at 74.4% resolved on SWE-bench versus 11.0% on FeatureBench.
- The gap persists even under a tighter comparison. On a shared-repository subset, Claude Opus 4.5 resolves 74.40% of SWE-bench Verified tasks but only 5.2% of the FeatureBench subset.
- FeatureBench tasks are much larger than SWE-bench tasks: average problem text is 4,818.0 words versus 195.1 words, and average gold solutions span 790.2 lines, 15.7 files, and 29.2 functions versus 32.8 lines, 1.7 files, and 3 functions.
- The benchmark prompt is not withholding basic structure. Prompts explicitly provide interface definitions, import paths, expected behaviors, and require directly callable solutions.
- In the reported baseline, GPT-5.1-Codex with medium reasoning resolves 12.5% of task cases using the Codex agent scaffold.

## Evidence and Findings

- The benchmark is built to target broader software work than prior agentic coding benchmarks by tracing unit tests through dependency relationships to recover tasks linked to feature implementation across a repository. That supports the paper’s central claim that feature development needs a different evaluation surface than localized bug repair, and it matters because benchmark scope shapes what competence claims are even being tested.
- The construction pipeline is heavily automated and execution-based rather than annotation-heavy. The source reports automatic task derivation with repository setup as the only manual step, at roughly 3 minutes per repository and less than 1 hour total over 24 repositories. That supports the claim that benchmark collection can scale without large human labeling burdens, which matters if the field wants harder, fresher evaluation sets rather than small handcrafted suites.
- The released artifact is not a toy slice. The first version contains 200 tasks and 3,825 executable environments drawn from 24 open-source repositories. That supports the claim that the benchmark is already large enough to function as a serious evaluation object, while still leaving open whether those repositories are broadly representative of real software work.
- The measured performance collapse against SWE-bench is large. Claude 4.5 Opus is reported at 74.4% resolved on SWE-bench but 11.0% on FeatureBench, and on a shared-repository comparison the same model drops from 74.40% on SWE-bench Verified to 5.2% on the FeatureBench subset. That supports the claim that current agents do not transfer cleanly from benchmarked repair tasks to harder feature-level development, which matters because public benchmark strength may otherwise be misread as general engineering strength.
- The difficulty gap is backed by concrete task-scale differences, not just by headline solve rates. FeatureBench L1 problems average 4,818.0 words versus 195.1 words for SWE-bench, while gold solutions average 790.2 lines, 15.7 files, and 29.2 functions versus 32.8 lines, 1.7 files, and 3 functions. This supports the bounded explanation that cross-file scope and implementation size are part of what makes the benchmark harder, which matters because “agent failure” here is plausibly tied to software structure rather than to arbitrary scoring harshness alone.
- The benchmark does give agents useful interface guidance. Prompts include interface definitions, import paths, and expected behaviors, yet performance remains weak; meanwhile, removing explicit interface information reduces Lite-set results, and giving visible unit tests raises performance sharply, with GPT-5.1-Codex reaching 63.3% resolved and 80.9% passed and Gemini-3-Pro-Preview reaching 60.0% resolved and 80.6% passed. That shows the benchmark outcome is sensitive to how much ground-truth structure is exposed, which matters because benchmark design choices meaningfully affect what failure should be interpreted as reasoning failure versus information-access failure.

## Contradictions and Tensions

- The most important tension is between strong SWE-bench results and weak FeatureBench results for the same frontier systems. That supports the paper’s claim of higher difficulty, but it also warns that “coding-agent performance” is not a single stable quantity; it changes sharply with task form, scope, and prompt structure.
- The benchmark is presented as a test of feature development, but some of the performance gap may come from benchmark design differences rather than feature work alone. FeatureBench tasks are far longer and structurally larger, so the comparison mixes feature-level ambition with much heavier context and implementation load.
- Prompts already include explicit interfaces, yet removing those interfaces still hurts performance, and exposing full unit tests drives performance far upward. That creates an interpretive tension: poor results may reflect real weakness in planning and cross-file execution, but they also reflect how much hidden structure the benchmark requires agents to reconstruct.
- The paper interprets NameError-heavy failures as evidence of cross-file dependency resolution problems. That is plausible and decision-relevant, but it remains an interpretation rather than a fully isolated causal proof.
- The benchmark is large and low-touch to collect, but representativeness remains unsettled. A benchmark can be nontrivial in scale without yet establishing that it captures the full distribution of real-world feature development.

## Mechanism or Bounds

The strongest supported mechanism is that FeatureBench derives harder tasks by following tested objects and dependency relations outward from unit tests into larger implementation surfaces, then evaluates them in executable environments. On the performance side, the bounded explanation is that current agents struggle when they must coordinate much longer specifications with multi-file, multi-function, cross-file implementation demands. The evidence is consistent with that explanation: problem statements are far longer, gold solutions are much larger, and the authors observe NameError-heavy failures that fit dependency-resolution trouble. But the mechanism is only partial. The evidence does not cleanly separate cross-file reasoning failure from other contributors such as benchmark construction choices, prompt format, or the amount of hidden structure agents must infer without seeing tests.

## Limits

- The claim that prior benchmarks are narrower depends on the paper’s own characterization of the benchmark landscape.
- The benchmark statistics establish size and construction approach, not representativeness across all software domains or engineering workflows.
- The hardness claim is well supported descriptively by large solve-rate drops and larger task footprints, but the causal reason for the drop is not fully isolated.
- Interface exposure and test visibility materially change outcomes, so benchmark results should be read with care as measurements of performance under a specific information regime.
- The cross-file dependency explanation is plausible but not conclusively demonstrated as the dominant failure source.
- The benchmark filters for substantial tasks, including cases with more than 100 lines of pending implementation and at least 10 fail-to-pass test points, which helps target harder work but also narrows what kind of “feature development” is being measured.
