# NL2Repo-Bench: Towards Long-Horizon Repository Generation Evaluation of Coding Agents

## Core Thesis

NL2Repo-Bench tests a harder coding-agent problem than patch-level benchmarks: given only a natural-language requirements document and an empty workspace, the agent must build a fully installable Python library. On this setup, long-horizon repository generation is still not solved. The benchmark is large enough to matter, the inputs are long, and even the best reported system reaches only 40.2% overall pass rate, with performance falling sharply on harder tasks.

## Why It Matters for Sapho

This matters because it tightens Sapho's doctrine around coding-agent evaluation. Strong results on localized code-edit tasks do not yet demonstrate reliable repository construction from specification alone. NL2Repo-Bench makes that gap visible. It also shows that benchmark outcomes depend not just on model capability, but on workflow behavior and evaluation visibility: planning discipline appears associated with better results, while hidden tests materially suppress performance. For Sapho, that means agent claims should stay tied to task structure, autonomy constraints, and what the agent was actually allowed to see.

## Key Findings

- The benchmark evaluates a long-horizon repository-generation task in which an agent receives one natural-language requirements document plus an empty workspace and must produce a fully installable Python library.
- Development happens without project scaffolding, source code, or test cases; outputs are judged afterward with the upstream repository's pytest suite in a controlled environment.
- The final dataset contains 104 tasks across nine Python-library categories, with average task inputs of about 18,800 tokens.
- Repository selection is bounded rather than arbitrary: targets were filtered to 300-120,000 LOC, at least 10 GitHub stars, passing pytest-based tests in the official version, and recent creation or update within the past three years.
- The strongest reported result is Claude-Sonnet-4.5 in Claude Code at 40.2% overall pass rate, which is still far below reliable repository-generation performance.
- Difficulty matters materially: for that top system, pass rate falls from 51.8% on easy tasks to 44.5% on medium and 25.1% on hard tasks.
- Execution behavior appears consequential: task_tracker usage shows the strongest reported positive correlation with performance at 0.711.
- Evaluation visibility also matters: when all test cases are revealed, Claude-Sonnet-4.5 in Claude Code rises from 40.2% to 59.4% overall pass rate, and Pass@1 increases from 3 to 18.

## Evidence and Findings

- The benchmark is designed to test full repository construction rather than code repair: agents start from a requirements document and an empty workspace, with each specification organized into Project Description, Supports, API Usage Guide, and Implementation Nodes. That supports the conclusion that this is a genuinely long-horizon generation setting, not a thin wrapper around patching.
- NL2Repo-Bench has enough scale and structure to function as a meaningful evaluation surface: 104 tasks, nine library categories, and average inputs near 18,800 tokens. That matters because weak benchmark scale or toy prompts could explain poor results, but the paper instead presents a moderately sized, document-heavy testbed.
- The reported ceiling remains low. Even the best evaluated system reaches 40.2% overall pass rate, and the paper states that average test pass remains below about 40.5% even for the strongest agents. That supports the conclusion that end-to-end repository generation from specification alone is still unreliable.
- Performance degrades with task difficulty for the leading system, from 51.8% on easy tasks to 44.5% on medium and 25.1% on hard tasks. This supports a substantive difficulty gradient rather than a flat failure pattern, which matters because it indicates agents are not merely noisy but increasingly brittle as repository demands rise.
- Tooling behavior and execution discipline appear to matter inside the benchmark: task_tracker usage has the strongest reported positive correlation with performance at 0.711. That supports a bounded operational conclusion that planning or task-state management is associated with better long-horizon execution.
- Test visibility materially changes outcomes. Revealing all test cases lifts Claude-Sonnet-4.5 in Claude Code from 40.2% to 59.4% overall pass rate and raises Pass@1 from 3 to 18. That matters because part of the benchmark difficulty is not just synthesis but working under hidden-target conditions.

## Contradictions and Tensions

- The benchmark asks for autonomous repository completion, but some agent behaviors cut against that objective. GPT-5 averaged 78.4 interaction turns and was reported to frequently halt for user confirmation rather than finish autonomously. That creates tension between general coding ability and benchmark-fit under strict autonomy.
- Qwen3-Thinking reportedly terminated early in 49.0% of tasks and showed a 46.2% non-finish rate. This suggests that a large share of failure may come from execution control and completion behavior, not only from inability to write correct code.
- Hidden-test evaluation makes the benchmark more realistic in one sense, but the jump from 40.2% to 59.4% when all tests are revealed shows that outcome quality is highly sensitive to evaluation visibility. That complicates any simple reading that the remaining gap is purely core coding weakness.
- The benchmark relaxes some non-functional build constraints such as README or license-file checks to focus on functional software generation. That sharpens measurement of executable repository behavior, but it also means results do not fully represent untouched upstream packaging completeness.

## Mechanism or Bounds

The strongest supported mechanism is operational rather than fully causal. Long-horizon repository generation appears to depend in part on agents maintaining coherent task state across many steps, which is consistent with the positive 0.711 correlation between task_tracker usage and performance. The test-revelation result also supports a bounded explanation that hidden-target uncertainty is a major part of the challenge: when agents can see all tests, performance improves substantially. But these are not clean causal proofs across all systems. The planning result is correlational, and the benchmark-specific behavior failures—confirmation-seeking, early termination, non-finish patterns—show that measured performance is partly a product of autonomy fit and execution discipline under this evaluation design.

## Limits

The paper supports a clear benchmark judgment, but not a universal theory of why agents fail. The evidence shows low pass rates, a difficulty gradient, and behavior patterns associated with failure, yet it does not isolate one causal bottleneck shared across models.
The dataset is moderately sized and filtered by explicit repository criteria, but those criteria also bound representativeness; the benchmark covers 104 Python-library tasks rather than the full space of software projects.
The strongest behavior-related signal for planning is correlational, not experimental.
The large gain from revealing tests shows that benchmark scores mix repository-generation ability with hidden-evaluation difficulty, so the headline failure rate should not be read as a pure measure of coding competence alone.
The relaxed non-functional constraints mean the benchmark captures functional repository generation better than full real-world release completeness.
