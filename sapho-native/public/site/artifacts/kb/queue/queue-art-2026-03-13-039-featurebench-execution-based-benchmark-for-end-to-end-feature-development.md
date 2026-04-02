# Queue Item Processing — art-2026-03-13-039

## Source metadata
- URL: https://arxiv.org/html/2602.10975v1
- Source type: firehose-brave
- Lane tags: `UI-design, UI-design`
- Curated at (UTC): 2026-03-13T10:01:33Z
- Finalized at (UTC): 2026-03-13T20:05:34Z

## Source custody
- Source snapshot: `research/evidence/source-material/2026-03-13/art-2026-03-13-039.json`
- Clean text path: `research/evidence/source-material/2026-03-13/art-2026-03-13-039.txt`

## Core thesis
Current agentic coding systems that perform strongly on bug-fix benchmarks remain weak on complex feature-level development when evaluated in executable, repository-grounded environments.

## Mechanism summary
FeatureBench introduces an execution-based benchmark for feature-oriented agentic coding built from real Python repositories using fail-to-pass and pass-to-pass tests, dynamic tracing over dependency graphs, code extraction with post-verification, and prompt generation with explicit callable interfaces; evaluation uses resolved rate, passed rate, and token I/O. The first version contains 200 evaluation tasks and 3825 executable environments from 24 open-source repositories, with a lighter 30-instance subset for cost-aware evaluation. Reported results show a sharp cross-benchmark drop from Claude 4.5 Opus at 74.4% resolved on SWE-bench to 11.0% on FeatureBench, while strong scaffold-model combinations such as GPT-5.1-Codex on Codex reach only 12.5% resolved on the full set despite multi-million-token executions.

## Why it matters for Sapho
This matters because it broadens coding-agent evaluation beyond bug fixing into feature development, where real software work often demands larger implementation scope, dependency coordination, and executable repository context. Its significance is that benchmark success on SWE-bench-style tasks does not translate into comparable performance on feature-completion workloads, which makes FeatureBench a useful corrective against overestimating production readiness from bug-fix benchmarks alone.

<!-- canonical-empirical-findings -->

## Empirical Findings (Data Snapshot)

| Novel finding | Quantitative result | Experimental setup/sample | Metric/outcome | Caveat/limit |
|---|---|---|---|---|
| Frontier agentic coding performance drops sharply when moving from SWE-bench-style results to FeatureBench feature-development tasks. | Claude 4.5 Opus is reported at 74.4% resolved on SWE-bench but only 11.0% resolved on FeatureBench. | FeatureBench evaluates end-to-end feature-oriented tasks with execution-based verification rather than only bug-fix issue resolution. | High benchmark scores on SWE-bench do not transfer to similarly high solved rates on FeatureBench. | The source reports this as a cross-benchmark comparison, so task distributions differ by benchmark design. |
| FeatureBench v1 is built at substantial scale with repository-grounded executable environments. | The first version contains 200 evaluation tasks and 3825 executable environments from 24 open-source repositories (created from May 2022 to September 2025). | Tasks are collected through an automated toolkit from real GitHub/PyPI repositories and validated in Dockerized environments. | The benchmark supports large-scale, executable, feature-level evaluation rather than small handcrafted sets. | The benchmark is restricted to Python repositories in this version. |
| The full benchmark uses explicit difficulty/quality filters and a lighter subset for cost-aware evaluation. | Full set: 200 instances with 5 P2P test files per instance, filtered to tasks with >100 lines of pending implementation and at least 10 F2P test points; Lite set: 30 randomly selected instances. | Benchmark configuration section defines full and lite partitions to balance challenge and evaluation cost. | FeatureBench enforces minimum task complexity while providing a cheaper evaluation entry point. | Lite-set results may not reflect full-set difficulty due to reduced sample size. |
| Even strong model-framework combinations show low full-set resolved rates and high token usage. | Reported full-set resolved rates include GPT-5.1-Codex (Codex scaffold) at 12.5%, Claude Opus 4.5 (Claude Code scaffold) at 11.0%, and Claude Opus 4.5 (OpenHands scaffold) at 10.5%; associated token I/O examples include 6.3M/39k and 7.5M/34k. | Table 2 reports Lite/Full results across multiple scaffolds (OpenHands, Gemini-CLI, Claude Code, Codex) and frontier models. | Performance remains low on full FeatureBench despite multi-million-token executions. | The provided source text is truncated, so only the visible table rows are extractable here. |

## Confidence
high

Justification: The source is a primary arXiv benchmark paper with explicit task-construction methodology, benchmark scale, and concrete quantitative performance results, so the evidence is strong for claims about feature-level evaluation difficulty. The main caveats are that the benchmark is restricted to Python repositories and that some visible performance extraction is limited to the table rows available in the provided snapshot.
