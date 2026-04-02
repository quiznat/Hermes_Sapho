# Queue Item Processing — art-2026-03-13-046

## Source metadata
- URL: https://arxiv.org/html/2512.12730v1
- Source type: firehose-brave
- Lane tags: `agent-memory, agent-memory`
- Curated at (UTC): 2026-03-13T11:32:33Z
- Finalized at (UTC): 2026-03-13T20:08:17Z

## Source custody
- Source snapshot: `research/evidence/source-material/2026-03-13/art-2026-03-13-046.json`
- Clean text path: `research/evidence/source-material/2026-03-13/art-2026-03-13-046.txt`

## Core thesis
When agents must build complete installable Python libraries from an empty workspace using only one requirements document, current state-of-the-art systems perform poorly, indicating long-horizon coherence and planning remain major bottlenecks.

## Mechanism summary
NL2Repo-Bench introduces an execution-verified benchmark for long-horizon repository generation from a single natural-language specification. It reverse-engineers real Python repositories into structured task documents, evaluates generated repositories with strict Dockerized execution against upstream pytest suites, and analyzes performance and failure patterns under long interaction horizons without scaffolding or revealed tests. The benchmark contains 104 tasks with average input length around 18,800 tokens, stratifies difficulty by repository size, and applies explicit quality filters so tasks are grounded in mature, testable, recently active codebases.

## Why it matters for Sapho
This matters because it pushes evaluation beyond localized bug fixing or constrained repository edits into a setting closer to end-to-end software creation, where agents must sustain planning, architectural consistency, and implementation quality over long horizons. Its significance is that current coding agents appear much weaker when asked to generate whole repositories from scratch, making NL2Repo-Bench a useful indicator that long-horizon repository construction is still a major unsolved capability gap rather than an area of near-production reliability.

<!-- canonical-empirical-findings -->

## Empirical Findings (Data Snapshot)

| Novel finding | Quantitative result | Experimental setup/sample | Metric/outcome | Caveat/limit |
|---|---|---|---|---|
| State-of-the-art coding agents fail to achieve strong reliability on long-horizon full-repository generation. | The strongest agents achieve below 40% average test pass rates and rarely complete an entire repository correctly. | Agents receive a single natural-language requirements document and an empty workspace, then must autonomously design and implement a full installable Python library; outputs are validated by executing upstream pytest suites. | Long-horizon repository generation is reported as largely unsolved under strict execution-based evaluation. | The statement reports aggregate performance and does not provide exact per-model full-completion percentages in the provided excerpt. |
| NL2Repo-Bench is constructed at repository scale with high input-context demands. | The benchmark contains 104 tasks, and the average task input length is approximately 18,800 tokens (described as nearly 19k). | Tasks are derived from real-world Python libraries and evaluated as full repository reconstruction problems rather than localized edits. | The benchmark imposes substantially larger specification/context requirements than prior repository-level evaluations. | Coverage is restricted to Python repositories in this version. |
| Task difficulty is explicitly stratified by repository size, yielding a broad complexity mix. | Easy: ≤1500 LOC (26 tasks); Medium: 1500–4000 LOC (46 tasks); Hard: ≥4000 LOC (32 tasks). | Difficulty levels are assigned based on original project size and total lines of code for each benchmark task. | The dataset spans easy-to-hard repository-generation settings rather than a single complexity regime. | Difficulty labeling is LOC-based and follows the benchmark’s predefined thresholds. |
| Repository inclusion uses explicit quality filters to enforce realism, tractability, and verifiability before benchmark admission. | Selection requires 300–120,000 LOC, at least 10 GitHub stars, passing pytest-based tests on the official version, and creation/update within the past three years. | Candidate repositories are human-reviewed for structure/dependencies, then validated by running native tests; only repositories passing all native tests are retained. | Benchmark tasks are grounded in mature, testable, and currently relevant codebases. | These criteria intentionally exclude very small projects and extremely large systems beyond current context limits. |

## Confidence
high

Justification: The source is a primary arXiv benchmark paper with explicit benchmark-construction criteria, execution-based validation, and concrete quantitative scope and performance signals, so the evidence is strong for long-horizon repository-generation difficulty. The main caveats are that the benchmark is restricted to Python repositories and that the provided excerpt reports aggregate performance rather than exact per-model full-completion rates.
