# Queue Item Processing — art-2026-03-13-009

## Source metadata
- URL: https://openreview.net/forum?id=41xrZ3uGuI
- Source type: firehose-brave
- Lane tags: `agent-factory, agent-factory`
- Curated at (UTC): 2026-03-13T19:59:10Z
- Finalized at (UTC): 2026-03-13T20:11:04Z

## Source custody
- Source snapshot: `research/evidence/source-material/2026-03-13/art-2026-03-13-009.json`
- Clean text path: `research/evidence/source-material/2026-03-13/art-2026-03-13-009.txt`

## Core thesis
FeatureBench argues that existing coding-agent benchmarks understate real software-development difficulty because they focus on narrower bug-fix tasks, while execution-based evaluation on multi-commit, feature-oriented tasks reveals much lower success rates for frontier agents.

## Mechanism summary
The abstract describes FeatureBench as an empirical benchmark for end-to-end feature-oriented agentic coding that automatically derives tasks from repositories by tracing from unit tests along a dependency graph, identifying feature-level tasks that can span multiple commits and pull requests while preserving functionality of other separated features. It reports that the first benchmark version contains 200 evaluation tasks and 3825 executable environments drawn from 24 open-source repositories, and cites a headline cross-benchmark comparison in which Claude 4.5 Opus achieves 74.4% resolved rate on SWE-bench but only 11.0% of tasks on FeatureBench. The abstract also states that the automated task-collection toolkit is intended to support scaling and updates over time to mitigate data leakage, while emphasizing execution-based evaluation rather than non-executable assessment.

## Why it matters for Sapho
This matters because it reframes coding-agent evaluation around feature completion and executable verification rather than narrow bug-fix success, which is closer to how real software work is experienced. Its significance is that a steep drop from a strong existing benchmark result to much lower feature-task success suggests many current coding benchmarks may overstate practical readiness for broader development work, even though the visible evidence here is limited to abstract-level claims and headline numbers.

<!-- canonical-empirical-findings -->

## Empirical Findings (Data Snapshot)

| Novel finding | Quantitative result | Experimental setup/sample | Metric/outcome | Caveat/limit |
|---|---|---|---|---|
| FeatureBench is built to evaluate end-to-end feature-oriented software development rather than narrow single-PR bug-fix tasks. | The first benchmark version contains 200 evaluation tasks and 3825 executable environments drawn from 24 open-source repositories. | Tasks are automatically derived by tracing from unit tests along a dependency graph to identify feature-level coding tasks spanning multiple commits and PRs, while checking that other separated features continue functioning. | The benchmark supplies a larger-scale, execution-based evaluation setting for complex feature development. | The excerpt gives only abstract-level construction details and does not provide repository-level composition or task-distribution breakdowns. |
| A frontier agent that performs strongly on SWE-bench collapses on FeatureBench, indicating a major cross-benchmark difficulty gap. | Claude 4.5 Opus is reported at 74.4% resolved rate on SWE-bench but only 11.0% of tasks on FeatureBench. | The abstract cites empirical evaluation of a state-of-the-art agentic model on FeatureBench and compares that result to the model's SWE-bench resolved rate. | The benchmark reveals that strong performance on existing coding benchmarks does not transfer to complex feature-development tasks. | The excerpt reports only a headline comparison for one model and does not provide broader model tables or variance estimates. |
| FeatureBench is designed to reduce data leakage risk by supporting automated scaling and updates over time. | The abstract does not provide a numeric leakage estimate, but explicitly states the benchmark can be scaled and updated over time. | This claim is tied to the automated task collection toolkit used to derive executable benchmark tasks from repositories with minimal human effort. | The benchmark construction method is intended to preserve freshness and reduce contamination pressure relative to more static benchmarks. | The source does not quantify how much leakage mitigation is achieved in practice. |
| The task-construction pipeline is explicitly built around executable evaluation rather than non-executable assessment. | The abstract contrasts FeatureBench with existing benchmarks that often rely on non-executable evaluations, but gives no numeric comparison for that limitation. | FeatureBench uses an execution-based evaluation protocol and a scalable test-driven task derivation process from code repositories. | Execution-based verification is presented as a core methodological advantage for measuring whether agents actually implement working features. | The excerpt does not detail the exact execution harness, scoring rubric, or pass criteria beyond the high-level description. |

## Confidence
high

Justification: The source is a primary benchmark abstract from OpenReview and contains concrete quantitative claims about benchmark scale and a headline performance gap, so the core framing is well grounded. Confidence is high for the benchmark’s stated contribution and reported abstract-level results, but limited by the lack of full methodological tables, broader model comparisons, and deeper execution details in the visible excerpt.
