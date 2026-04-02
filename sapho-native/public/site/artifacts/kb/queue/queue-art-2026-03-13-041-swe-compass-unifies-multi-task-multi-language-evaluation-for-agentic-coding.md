# Queue Item Processing — art-2026-03-13-041

## Source metadata
- URL: https://arxiv.org/html/2511.05459v3
- Source type: firehose-brave
- Lane tags: `agent-factory, agent-factory`
- Curated at (UTC): 2026-03-13T10:03:01Z
- Finalized at (UTC): 2026-03-13T20:06:23Z

## Source custody
- Source snapshot: `research/evidence/source-material/2026-03-13/art-2026-03-13-041.json`
- Clean text path: `research/evidence/source-material/2026-03-13/art-2026-03-13-041.txt`

## Core thesis
Current coding benchmarks are too narrow, often centered on Python bug fixing, so SWE-Compass builds a broader, production-aligned benchmark that evaluates agentic coding across diverse tasks, scenarios, and languages under reproducible execution settings.

## Mechanism summary
The benchmark is built in five stages—user analysis, data collection, environment building, task building, and validation—using active-learning taxonomy discovery on real coding discussions, strict repository and pull-request quality filters, Dockerized executable environments, and strategy-specific task-construction pipelines by task type. It reports 2,000 instances across 8 task types, 8 programming scenarios, and 10 programming languages, sourced from authentic GitHub pull requests. The pipeline preserves approximately 50,000 filtered PRs for candidate generation, but executable environment construction is a major constraint: initial automated Docker build success is around 2%, expert-assisted retries by 30 annotators raise retention to approximately 8%, and the process yields about 4,000 runnable Docker images.

## Why it matters for Sapho
This matters because it addresses a structural blind spot in coding-agent evaluation: narrow benchmarks can overstate capability by concentrating on a small slice of software work. Its significance is twofold: it expands evaluation coverage to a more realistic spread of tasks and languages, and it quantifies how environment reproducibility, not just task design, is a limiting factor in benchmark construction, making it useful both as an evaluation asset and as evidence that scalable agent benchmarking depends heavily on infrastructure and environment engineering.

<!-- canonical-empirical-findings -->

## Empirical Findings (Data Snapshot)

| Novel finding | Quantitative result | Experimental setup/sample | Metric/outcome | Caveat/limit |
|---|---|---|---|---|
| SWE-Compass expands benchmark coverage beyond bug-fixing by jointly scaling task, scenario, and language axes. | The benchmark contains 2,000 instances across 8 task types, 8 programming scenarios, and 10 programming languages; Table 1 reports 40 repositories and 4.7 average modified files per instance. | Instances are curated from authentic GitHub pull requests and organized under a structured taxonomy for unified evaluation. | Compared with prior benchmarks listed in Table 1, SWE-Compass provides higher combined breadth of language/task coverage and repository-grounded complexity. | The provided text includes one earlier sentence mentioning 10 programming scenarios, while core sections repeatedly describe 8 scenarios. |
| The data foundation is built from heavily filtered, high-quality repositories and pull requests at substantial scale. | Repository filtering required at least 500 stars, active maintenance within 6 months, at least 3 contributors, more than 1000 issues/PRs, more than 200 forks, and executable unit tests; after multi-stage filtering, approximately 50,000 PRs were retained. | The pipeline first maps existing benchmarks to the new taxonomy, then supplements with GitHub repository/PR mining under strict quality criteria. | This yields a large PR pool with richer task semantics for downstream environment and task construction. | The PR count is approximate and depends on the specified filtering thresholds. |
| Executable environment construction is a major bottleneck, requiring expert intervention to achieve acceptable retention. | Initial automated Docker build success was around 2%; 30 expert annotators performed targeted fixes; retention increased to approximately 8%; final output was about 4,000 runnable Docker images. | For each PR, dependencies were extracted from repo config files, Docker images were built, then validated via native test execution with F2P/P2P consistency checks. | Human-assisted retries materially improved reproducibility coverage, enabling a sizable executable benchmark base. | Success/retention rates are tied to this repository mix and toolchain fragility in real-world projects. |
| Task/scenario/language taxonomy was derived via iterative active learning over real developer conversations. | Using Qwen3-Coder-30B-A3B-Instruct as annotator, five iterations were run, yielding 8 task types, 8 programming scenarios, and 10 major languages. | Repository-level discussions from Stack Overflow and GitHub were labeled with ICL-based annotation, then refined through tag clustering and LLM-guided seed updates until convergence. | The process produced a structured taxonomy used to drive benchmark construction and balance. | Taxonomy outcomes depend on initial seed topics and the chosen annotator model. |

## Confidence
high

Justification: The source is a primary arXiv benchmark paper with explicit construction methodology, benchmark-scope statistics, and concrete quantitative evidence about data filtering and environment-retention bottlenecks. Confidence is high because the evidence is directly result-bearing and methodologically detailed, with the main caveat being minor internal ambiguity in scenario-count wording and the benchmark’s dependence on the chosen taxonomy and repository mix.
