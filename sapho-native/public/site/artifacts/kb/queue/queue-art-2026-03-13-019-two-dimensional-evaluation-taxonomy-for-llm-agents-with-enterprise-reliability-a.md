# Queue Item Processing — art-2026-03-13-019

## Source metadata
- URL: https://arxiv.org/html/2507.21504v1
- Source type: firehose-brave
- Lane tags: `agent-memory, agent-memory`
- Curated at (UTC): 2026-03-13T05:00:58Z
- Finalized at (UTC): 2026-03-13T20:01:46Z

## Source custody
- Source snapshot: `research/evidence/source-material/2026-03-13/art-2026-03-13-019.json`
- Clean text path: `research/evidence/source-material/2026-03-13/art-2026-03-13-019.txt`

## Core thesis
LLM agent evaluation should be structured along two axes—what to evaluate and how to evaluate—because real-world deployment requires assessing behavior, capabilities, reliability, and safety through context-aware methods rather than relying on single-metric task success.

## Mechanism summary
The survey organizes evaluation objectives and evaluation process into a hierarchical taxonomy, mapping behavior, capabilities, reliability, and safety/alignment to representative metric families, benchmarks, and leaderboards. It also highlights enterprise-specific requirements such as strict repeatability criteria that distinguish pass@k from the stricter pass^k consistency framing, and long-horizon memory evaluations that span 40+ to 600+ turn dialogues, showing why evaluation must incorporate interaction mode, data, metrics, tooling, and context rather than task success alone.

## Why it matters for Sapho
This matters because it provides a practical design frame for building deployment-grade agent evaluation stacks instead of over-weighting one-shot benchmark wins. Its significance is that enterprise adoption depends on measuring not just whether an agent can solve a task once, but whether it does so consistently, over long horizons, and under policy and workflow constraints; the survey therefore helps align benchmark choice and metric design with real operational risk.

<!-- canonical-empirical-findings -->

## Empirical Findings (Data Snapshot)

| Novel finding | Quantitative result | Experimental setup/sample | Metric/outcome | Caveat/limit |
|---|---|---|---|---|
| The survey formalizes LLM-agent evaluation as a two-dimensional taxonomy separating evaluation objectives from evaluation process. | It defines 2 primary dimensions, with 4 objective categories (behavior, capabilities, reliability, safety/alignment) and 5 process components (interaction mode, evaluation data, metrics computation, tooling, contexts). | Conceptual synthesis across prior work, presented in Section 2 and summarized in a hierarchical taxonomy and Table 1. | Provides a structured mapping of objective categories to concrete metric families and representative benchmarks/leaderboards. | This is a survey taxonomy, not a single controlled experiment with newly reported model performance scores. |
| For reliability consistency, the source distinguishes pass@k from a stricter pass^k criterion and reports current-agent consistency weakness under the stricter metric. | pass@k measures success at least once over k attempts, while pass^k requires success in all k attempts. | Repeated execution of the same task; the source cites τ-benchmark applications in domains such as retail and airline booking. | The cited result is that current agents "struggle with consistency" when evaluated with pass^k-style strict repeatability. | No explicit numeric pass^k values are included in the provided snapshot text. |
| Long-horizon memory evaluation in agent benchmarks is explicitly quantified with extended multi-turn dialogue lengths. | The source states long-dialogue tests at 40+ turns (LongEval, SocialBench) and reports evaluations spanning 600+ turns (Maharana et al.). | Agents are given conversations spanning dozens to hundreds of exchanges and later queried for earlier details to test retention and coherence. | Memory performance is evaluated with metrics such as factual recall accuracy and consistency score (no contradictions between turns). | Quantitative lengths are reported from referenced studies; model-by-model performance numbers are not provided in this snapshot. |

## Confidence
high

Justification: The source is a primary arXiv survey with explicit taxonomy structure and concrete, source-grounded references to repeatability and long-horizon evaluation practice, so confidence is high for the synthesis about evaluation framing. The main caveat is that it is a survey rather than a single controlled benchmark with newly reported model scores, so its strongest contribution is conceptual integration rather than direct comparative performance evidence.
