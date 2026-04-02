# Queue Artifact — art-2026-03-04-031

Source URL: https://arxiv.org/abs/2601.15153  
Canonical URL: https://arxiv.org/abs/2601.15153  
Lane: agent-memory  
Decision: retain

## Thesis

A practical path to expert-grade agent outcomes is to codify tacit human domain knowledge (rules, design principles, request routing logic) into explicit system components rather than relying on generic LLM prompting alone.

## Mechanism summary

The paper proposes a software-engineering framework combining request classification, RAG-backed code generation, codified expert rules, and visualization design principles. In an industrial simulation-visualization case study, evaluators report substantial quality gains over baseline. The mechanism is knowledge externalization: translate scarce expert heuristics into machine-actionable contracts and retrieval components so non-experts can produce higher-quality outputs.

## Confidence

Medium-high. Primary source with an applied case study and quantified comparative outcomes; generalization beyond this setting still needs broader replication.

<!-- canonical-empirical-findings -->

## Empirical Findings (Data Snapshot)

| Novel finding | Quantitative result | Experimental setup/sample | Metric/outcome | Caveat/limit |
|---|---|---|---|---|
| Codifying expert domain knowledge into classifier + RAG + rule/principle components can lift non-expert output quality to expert-rated levels in specialized workflows. | Reported **206% improvement** in output quality; evaluation spans **5 scenarios** with **12 evaluators**. | Industrial case study in simulation-data visualization comparing proposed agent framework vs baseline workflow. | Output quality ratings and code-quality variance; framework reported expert-level ratings across all evaluated scenarios. | Single-domain case study; replication across additional domains/teams is needed before broad generalization. |

## Why it matters for Sapho

Directly supports Sapho’s contract-first memory strategy: codify expert judgment into durable artifacts and retrieval/routing pipelines to reduce expert bottlenecks while maintaining quality controls.
