# Queue Item Processing — art-2026-03-13-033

## Source metadata
- URL: https://arxiv.org/html/2511.00872v1
- Source type: firehose-brave
- Lane tags: `UI-design, UI-design`
- Curated at (UTC): 2026-03-13T07:34:03Z
- Finalized at (UTC): 2026-03-13T20:03:53Z

## Source custody
- Source snapshot: `research/evidence/source-material/2026-03-13/art-2026-03-13-033.json`
- Clean text path: `research/evidence/source-material/2026-03-13/art-2026-03-13-033.txt`

## Core thesis
General-purpose agent frameworks show moderate, task-dependent performance with strong trade-offs between effectiveness, execution dynamics, and token/cost overhead rather than a single dominant framework.

## Mechanism summary
The study evaluates seven general-purpose agent frameworks across software development, vulnerability detection, and program repair using SRDD, LLM-SmartAudit, and SWE-bench Lite benchmarks. It analyzes outcomes along three dimensions: task success, process efficiency through trajectory and correction behavior, and token/cost overhead distribution across workflow stages. Reported results show different leaders by task, including GPTswarm at 77% accuracy in vulnerability detection and OpenHands as the most balanced in software development, while efficiency patterns vary by orchestration style and overhead profiles differ substantially, with multi-agent workflows concentrating cost in planning and reflection and single-agent systems concentrating cost in execution and editing.

## Why it matters for Sapho
This matters as an empirical baseline for framework selection because it shows that choosing an agent framework is not just a question of peak task accuracy. Its significance is that real deployment decisions must weigh task fit, trajectory efficiency, and resource cost together, since a framework that looks strong in one workload or stage structure may be inefficient or underperform in another; this supports task-conditioned framework routing and cost-aware workflow design rather than assuming any general-purpose framework will transfer cleanly across code-centric jobs.

<!-- canonical-empirical-findings -->

## Empirical Findings (Data Snapshot)

| Novel finding | Quantitative result | Experimental setup/sample | Metric/outcome | Caveat/limit |
|---|---|---|---|---|
| Effectiveness is moderate overall and strongly task-dependent across frameworks, with different leaders by task. | GPTswarm leads vulnerability detection at 77% accuracy; in program repair, only a subset of agents repair about half of issues. | Seven general-purpose agent frameworks were evaluated across three tasks: software development, vulnerability detection, and program repair, using SRDD, LLM-SmartAudit, and SWE-bench Lite benchmarks. | No single framework dominates all tasks; OpenHands is described as the most balanced in software development while other frameworks lead specific tasks. | Program repair results remain limited, with substantial room for improvement reported by the authors. |
| Execution efficiency differs by orchestration style, and longer/more complex trajectories do not universally imply better outcomes. | SE-Agent (Iter-3) shows the longest steps across experiments; AgentOrchestra shows the longest correction sequences; OpenHands ranks second with stable and convergent behavior. | Efficiency analysis (RQ2) compares trajectory length, correction sequences, and correction-rate behavior across tasks and frameworks. | Efficiency depends more on reasoning depth, coordination strategy, and feedback integration than on agent count alone. | The provided excerpt reports relative rankings and qualitative efficiency patterns without full numeric step/correction tables. |
| Overhead profiles vary substantially across frameworks and workflow structures, with planning/reflection dominating multi-agent cost. | Software development is the most expensive task; AgentOrchestra is the most resource-intensive; OpenHands consumes the most tokens but benefits from caching; GPTswarm uniquely has more output than input tokens. | Overhead analysis (RQ3) examines token and monetary costs and stage-level token distribution patterns. | Multi-agent workflows concentrate cost in planning/reflection stages, while single-agent systems concentrate cost in execution/editing stages. | The excerpt provides directional and comparative overhead findings without full per-stage token totals. |

## Confidence
high

Justification: The source is a primary arXiv empirical comparison with explicit cross-task evaluation and structured analysis of effectiveness, efficiency, and overhead, which makes it strong evidence for framework trade-off claims. The main caveat is that some efficiency and overhead findings are comparative and directional in the provided excerpt rather than fully numeric, and performance remains benchmark- and scaffold-dependent.
