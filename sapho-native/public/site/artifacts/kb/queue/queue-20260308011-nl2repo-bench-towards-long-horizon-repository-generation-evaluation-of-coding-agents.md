<details class="traceability-panel">
<summary>Traceability</summary>
<div class="traceability-body">
<ul>
  <li><strong>Source:</strong> <a href="https://arxiv.org/html/2512.12730v1" target="_blank" rel="noopener">https://arxiv.org/html/2512.12730v1</a></li>
  <li><strong>Intake queued:</strong> 2026-03-08T08:30:47Z</li>
  <li><strong>Source captured:</strong> 2026-04-05T14:06:41Z</li>
  <li><strong>Curated:</strong> 2026-04-09T04:48:19Z</li>
  <li><strong>Artifact finalized:</strong> 2026-04-09T04:51:11Z</li>
  <li><strong>Artifact published:</strong> 2026-04-09T10:25:39Z</li>
</ul>
</div>
</details>

# NL2Repo-Bench: Towards Long-Horizon Repository Generation Evaluation of Coding Agents

## Core Thesis

NL2Repo-Bench tests whether coding agents can build an installable Python library from nothing but a requirements document, with no scaffold, source, or tests shown during development, and the reported results say they still fail often. The benchmark therefore shifts the question from short patching competence to long-horizon repository construction under hidden evaluation, where agent execution discipline and feedback visibility appear to matter almost as much as raw code-generation quality.

## Why It Matters for Sapho

This matters because it is closer to the autonomy story the field keeps implying but rarely measures directly. A model that can edit code inside an already prepared repo is not the same thing as a model that can reconstruct a working package from specification alone. For Sapho, the paper strengthens a stricter doctrine: benchmark claims about coding agents should be discounted unless they specify the amount of scaffolding provided, whether tests are visible, and whether the agent reliably stays on task long enough to finish. It also warns against reading low scores as pure model incapacity when the benchmark itself exposes search, planning, and execution-management bottlenecks.

## Key Findings

- The benchmark gives agents a natural-language requirements document plus an empty workspace and asks them to generate a fully installable Python library from scratch, while withholding project scaffolding, source code, and test cases until final grading against the original upstream pytest suite.
- The released benchmark contains 104 tasks across nine Python-library categories, with average input length around 18,800 tokens, making this a long-context, long-horizon generation setting rather than a toy code-completion exercise.
- Repository selection is bounded toward maintained real-world Python projects: eligible targets had to fall between 300 and 120,000 lines of code, have at least 10 GitHub stars, include pytest-based tests, pass those tests in the official repo, and be created or updated within the past three years.
- End-to-end success remains limited. The highest reported overall pass rate is 40.2% for Claude-Sonnet-4.5 using Claude Code, with Pass@1 of 3, while GPT-5 is reported at 21.7% overall pass rate with Pass@1 of 1.
- The paper’s own diagnostics point beyond pure model-quality explanations: GPT-5 shows an 84.5% non-finish rate and a 13.4% early-stop rate, while Qwen3-Thinking shows 46.2% non-finish and 49.0% early termination.
- Task management behavior appears operationally important: among frequently used tools, task_tracker has the strongest reported correlation with performance at 0.711.
- Test visibility changes outcomes materially. When all test cases are revealed, Claude-Sonnet-4.5 using Claude Code rises from 40.2% overall pass rate and Pass@1 of 3 to 59.4% overall pass rate and Pass@1 of 18.

## Evidence and Findings

- The benchmark is intentionally harsh on shortcut strategies: the agent gets only a requirements document and an empty workspace, then is judged by the original upstream pytest suite in a controlled environment. That supports the conclusion that the task is repository reconstruction from specification alone, not incremental editing inside a known codebase, which makes strong results here more meaningful than patch-level wins.
- The dataset is nontrivial in both breadth and input burden: 104 tasks spread across nine categories with average requirement length around 18,800 tokens. That supports the conclusion that success depends on sustaining structure over long contexts, not merely solving a few narrow coding puzzles, which matters because many public agent claims still rest on shorter and more scaffolded settings.
- The eligibility filters push the benchmark toward recent, functioning, minimally adopted Python libraries: 300-120,000 lines of code, at least 10 GitHub stars, pytest-based tests, official test-suite pass, and recent creation or update. That supports the conclusion that the benchmark is trying to approximate maintained real repositories rather than synthetic toy tasks, which increases practical relevance but also narrows representational scope.
- Reported top-line performance is still modest: the best main-table result is 40.2% overall pass rate for Claude-Sonnet-4.5 using Claude Code, while GPT-5 is reported at 21.7% with only Pass@1 equal to 1. That supports the conclusion that full repo generation under hidden tests remains unsolved, which matters because field narratives about near-autonomous software construction are ahead of the measured evidence here.
- The execution diagnostics show that some failures are not cleanly interpretable as “could not code the solution”: GPT-5 posts 84.5% non-finish and 13.4% early-stop rates, and Qwen3-Thinking shows 46.2% non-finish with 49.0% early termination. That supports the conclusion that staying engaged, planning over many turns, and actually completing the workflow are central parts of benchmark success, which matters for Sapho because autonomy evaluations must treat task completion behavior as first-order evidence.
- The tooling and visibility results sharpen the mechanism hypothesis: task_tracker usage has a reported correlation of 0.711 with performance, and revealing all tests lifts Claude-Sonnet-4.5 from 40.2% overall pass rate and Pass@1 of 3 to 59.4% and 18. That supports the conclusion that search guidance, work decomposition, and feedback visibility materially affect outcomes, which matters because benchmark scores here reflect a compound system of coding ability plus execution management plus access to evaluative signals.

## Contradictions and Tensions

- The main tension is between hidden-test and revealed-test performance. A jump from 40.2% to 59.4% when all tests are exposed implies that a meaningful share of failure is tied to search and feedback constraints rather than only an inability to write the target repository.
- Even after revealing all tests, performance remains below 60%, so the benchmark does not collapse into a trivial debugging exercise. The result cuts both ways: visibility matters a great deal, but it does not erase the underlying difficulty.
- GPT-5’s 21.7% overall pass rate is hard to read as a simple capability measure when the paper also reports 84.5% non-finish and 13.4% early-stop rates. The weak headline score may partly reflect execution behavior rather than only code-synthesis weakness.
- The strong 0.711 correlation for task_tracker usage suggests planning discipline matters, but correlation does not establish that the tool itself causes better outcomes. Better models may simply be more likely to use organizational tools effectively.
- The benchmark is framed as realistic because it targets maintained Python libraries, but that realism is selective. Requiring pytest, recent activity, minimum stars, and a specific code-size band improves quality control while also excluding older, less visible, non-pytest, or out-of-band projects.

## Mechanism or Bounds

The strongest bounded mechanism supported here is that long-horizon repository generation success depends on a compound capability stack: understanding a long requirements document, decomposing work over many turns, maintaining progress without stalling or quitting, and using evaluative feedback effectively when it is available. The revealed-test gain and the task_tracker correlation both support this operational explanation. But the evidence does not cleanly separate model intelligence from agent-loop design, tool use, stopping policy, or other system-level choices. The benchmark is also explicitly bounded to Python libraries meeting recentness, size, adoption, and pytest-eligibility filters, so its conclusions should not be generalized to all software-generation settings.

## Limits

The paper does not isolate which hidden artifact or runtime constraint contributes most to failure: missing scaffolding, absent tests, long-context burden, and autonomous execution pressure are bundled together.
The task_tracker result is correlational, not causal.
The reported cross-model comparisons are difficult to interpret as pure model rankings because systems may differ in agent loop behavior, stopping behavior, and tool policy.
The benchmark covers only 104 Python-library tasks under specific selection rules, so it is informative but not representative of all repositories or all coding-agent workloads.
The results show benchmark difficulty clearly, but they leave unresolved how much of that difficulty is intrinsic code synthesis versus workflow management under limited feedback.
