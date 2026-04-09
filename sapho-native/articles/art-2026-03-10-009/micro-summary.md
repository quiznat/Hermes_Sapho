# FeatureBench: Benchmarking Agentic Coding for Complex Feature Development

## Core Thesis

FeatureBench argues that current coding agents look much weaker once evaluation moves from relatively narrow bug-fix settings to executable feature-development tasks that span larger code surfaces, more files, more functions, and more tests. The benchmark is built to measure that harder regime directly, and the first reported results show a sharp drop in solved-task rates relative to SWE-bench.

## Why It Matters for Sapho

This matters because it cuts against the easy narrative that strong bug-fix benchmark performance means agents are close to dependable software-development autonomy. The paper suggests that feature-level work remains a different and harder operating domain, and that evaluation doctrine should stress test access to tests, interface visibility, and cross-file reasoning rather than treating code execution alone as the main bottleneck. For Sapho, the practical implication is clear: benchmark wins in narrow repair settings should not be read as field-wide proof of robust multi-file feature construction.

## Key Findings

- FeatureBench is explicitly designed to benchmark feature-level coding work rather than only single-PR bug fixing, using execution-based evaluation and a test-driven collection pipeline that traces unit tests through dependency graphs to isolate separable feature tasks.
- The first release is large enough to matter operationally: 200 evaluation tasks and 3825 executable or verifiable environments drawn from 24 open-source repositories, with tasks spanning changes from May 2022 through September 2025.
- Reported performance drops steeply when agents are tested on this benchmark: Claude Opus 4.5 falls from 74.4% resolved on SWE-bench to 11.0% on the full FeatureBench set.
- The difficulty gap is not just a repository-selection artifact. On repositories shared with SWE-bench, Claude Opus 4.5 is still reported at 74.40% on SWE-bench Verified versus 5.2% on the aligned FeatureBench subset.
- FeatureBench tasks are materially larger than the compared SWE-bench tasks: 4818.0 versus 195.1 words of problem text, 790.2 versus 32.8 gold-solution lines, 15.7 versus 1.7 files, 29.2 versus 3 functions, and 62.7 versus 9.1 fail-to-pass test points.
- The reported ablations suggest that access to tests and interface information is a major constraint on performance. On the lite set, showing unit tests raised Gemini-3-Pro-Preview from 10.0% to 60.0% and GPT-5.1-Codex from 20.0% to 63.3%, while removing explicit interface information pushed them down to 3.3% and 16.7%.

## Evidence and Findings

- The benchmark is structured to target feature development rather than narrow patch repair: it uses execution-based evaluation and a collection pipeline that follows unit tests through dependency graphs to carve out feature tasks that can span multiple commits and pull requests. That supports the paper's core claim that it is measuring a broader work unit than many earlier agentic coding benchmarks, which matters because benchmark scope changes what “agent coding ability” actually means.
- The release footprint is substantial: 200 evaluation tasks, 3825 executable or verifiable environments, 24 open-source repositories, and a source change window from May 2022 to September 2025. That scale supports treating the benchmark as a real executable testbed rather than a toy sample, while still leaving open the question of how representative those repositories are of the wider software ecosystem.
- The headline performance gap is large enough to force a re-rating of present capability. Claude Opus 4.5 is reported at 74.4% resolved on SWE-bench but 11.0% on the full FeatureBench benchmark, and the shared-repository comparison remains stark at 74.40% versus 5.2%. That supports the conclusion that feature-level coding remains far less solved than leading bug-fix scores imply.
- The paper also shows why the tasks are harder in practical terms. Compared with SWE-bench, the reported FeatureBench L1 tasks involve far longer problem statements, much larger gold solutions, many more files and functions, and roughly seven times as many fail-to-pass test points. This supports a bounded mechanism: the benchmark is harder in ways that compound planning, interface tracking, and cross-file coordination demands.
- The ablation results tie a large share of misses to missing tests and interface knowledge rather than mere inability to run code. When unit tests are exposed, performance jumps sharply; when explicit interfaces are removed, it collapses. That matters because it suggests the frontier weakness is not just generation quality in the abstract but disciplined navigation of code structure and expected behavior.
- Failure analysis sharpens that interpretation. NameError is reported as the dominant failure mode for Claude Opus 4.5, the paper links many TypeError and AttributeError failures to guessed or hallucinated interfaces across files, and AssertionError remains common among non-crash failures. Together these results support the view that many attempts execute far enough to be checked, but break on cross-file dependency resolution and interface understanding.

## Contradictions and Tensions

- The most important tension is between strong public benchmark optics and weak feature-development performance. A model can look highly capable at 74.4% on SWE-bench and still fall to 11.0% on the full FeatureBench set, so “state-of-the-art coding” depends heavily on which coding regime is being measured.
- The shared-repository result matters because it weakens the easy counterargument that FeatureBench is only harder because it samples different projects. Even when repository choice is partially aligned, the gap remains severe at 74.40% versus 5.2%, suggesting the task formulation itself carries much of the difficulty.
- Test visibility creates another tension. If showing unit tests can move GPT-5.1-Codex from 20.0% to 63.3% and Gemini-3-Pro-Preview from 10.0% to 60.0% on the lite set, then headline agent performance is highly sensitive to what the benchmark exposes. That is useful diagnostically, but it also means “ability” is entangled with how much scaffolding the evaluation provides.
- The paper points to cross-file reasoning failures, but the failure picture is not singular. NameError, TypeError, AttributeError, and AssertionError all matter, which suggests overlapping weaknesses: interface hallucination, dependency-resolution failure, and incomplete semantic correctness after code runs.
- The benchmark-construction pipeline is partly automated and supported by an LLM-based classifier with 81.03% precision, 89.24% recall, 84.94% F1, and 91.74% accuracy against expert annotations. That is strong enough to support the pipeline, but not perfect, so scale is gained with some residual extraction risk.

## Mechanism or Bounds

The strongest supported mechanism is that FeatureBench stresses capabilities that narrow bug-fix benchmarks underweight: cross-file dependency resolution, interface discovery, and coordination across larger feature surfaces. The paper supports this with concrete task-size differences, sharp gains when unit tests are visible, sharp losses when interface information is removed, and failure patterns dominated by unresolved names and incorrect cross-file interface assumptions.

That mechanism is still bounded. The evidence shows association and diagnostic pressure, not a clean causal decomposition of exactly how much of the performance gap comes from task length, file count, function count, interface ambiguity, or test structure. Some evidence is experimental ablation, but parts of the mechanism claim still rest on failure analysis and behavioral interpretation rather than fully isolated causal tests.

## Limits

The benchmark is large and executable, but the paper does not establish that its 24 repositories are broadly representative of all feature-development settings.

The comparison to earlier benchmarks relies partly on the paper's own characterization of those benchmarks as narrower and often bug-fix centered, rather than on an independent audit of the whole benchmark landscape.

The strongest failure-mechanism claim is inferential rather than complete. The ablations and error categories point toward cross-file reasoning and interface access as major constraints, but they do not rule out other interacting causes.

Some reported trends remain only qualitatively specified in the captured evidence, including the negative relationship between pass rate and required code length, so not every interpretive claim is equally quantified in the excerpted record.
