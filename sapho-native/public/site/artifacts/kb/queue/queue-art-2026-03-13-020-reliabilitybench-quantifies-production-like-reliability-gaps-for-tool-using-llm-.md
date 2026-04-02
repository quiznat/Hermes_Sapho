# Queue Item Processing — art-2026-03-13-020

## Source metadata
- URL: https://arxiv.org/html/2601.06112v1
- Source type: firehose-brave
- Lane tags: `agent-factory, agent-factory`
- Curated at (UTC): 2026-03-13T05:03:43Z
- Finalized at (UTC): 2026-03-13T20:02:14Z

## Source custody
- Source snapshot: `research/evidence/source-material/2026-03-13/art-2026-03-13-020.json`
- Clean text path: `research/evidence/source-material/2026-03-13/art-2026-03-13-020.txt`

## Core thesis
Single-run agent success metrics overestimate production readiness; reliability should be evaluated jointly across repeated-run consistency, semantic perturbation robustness, and infrastructure fault tolerance because agents that look strong on clean runs degrade materially under stress.

## Mechanism summary
ReliabilityBench defines a three-dimensional reliability surface R(k, ε, λ) and evaluates agents across repeated-run consistency, action metamorphic perturbations, and injected tool/API faults. Across 1,280 episodes spanning scheduling, travel, support, and e-commerce, the benchmark shows pass rate declines from 96.88% at ε=0.0 to 88.12% at ε=0.2, and to 84.0% under combined perturbation and fault stress. It also reports that Gemini 2.0 Flash achieves 91.04% overall pass^2 versus GPT-4o at 90.42% while costing $0.12 versus $9.77, that ReAct outperforms Reflexion on reliability surface volume and fault recovery, and that rate limiting is the most damaging isolated fault type at λ=0.2.

## Why it matters for Sapho
This matters because it turns reliability from a vague intuition into a measurable deployment criterion under production-like stress. Its significance is that benchmark wins on clean tasks can mask brittle behavior, poor recovery, and unfavorable cost profiles once agents face perturbations and infrastructure faults, so model and architecture choices should be judged on robustness and cost-normalized reliability rather than nominal single-run success alone.

<!-- canonical-empirical-findings -->

## Empirical Findings (Data Snapshot)

| Novel finding | Quantitative result | Experimental setup/sample | Metric/outcome | Caveat/limit |
|---|---|---|---|---|
| Semantic perturbations materially reduce agent reliability even when baseline pass rates are high. | Pass rate drops from 96.88% at ε=0.0 to 88.12% at ε=0.2, an 8.8% decline. | Main experiments over 480 episodes per model with perturbation levels ε∈{0.0,0.1,0.2}, fault levels λ∈{0.0,0.2}, k=2 trials, across scheduling/travel/support/e-commerce. | Action metamorphic perturbations expose brittleness not visible in clean-input evaluation. | The paper states perturbation depth excludes heavy ε=0.3 combinations in the reported experiments. |
| GPT-4o shows no reliability advantage over Gemini 2.0 Flash despite dramatically higher evaluation cost. | Overall pass^2: Gemini 91.04% vs GPT-4o 90.42% (Δ -0.62% for GPT-4o); total cost: $0.12 vs $9.77, i.e., 82× higher for GPT-4o. | Table 5 and Table 10 aggregate 480 episodes per model across ReAct and Reflexion. | Cost-normalized reliability strongly favors Gemini 2.0 Flash for large-scale reliability evaluation. | Model coverage is limited to two models in this study. |
| Simpler ReAct architecture is more robust under stress than Reflexion in this benchmark. | Surface volume: ReAct 0.900 vs Reflexion 0.875; at ε=0.2 pass: 90.0% vs 86.3%; fault recovery at λ=0.2: 80.9% (38/47) vs 67.3% (35/52). | Gemini 2.0 Flash architecture comparison with perturbation/fault stress and separate recovery statistics. | ReAct maintains higher reliability surface and better recovery behavior under injected faults. | Architecture conclusions are based on the benchmark’s implemented ReAct/Reflexion variants and task set. |
| Rate limiting is the most damaging isolated fault type, while transient timeout is best handled. | At λ=0.2 ablation: Rate Limit Only pass rate 93.75% (2.5% below mixed baseline 96.25%); Timeout Only 98.75%; Partial Response Only 97.50%. | Fault type ablation over 320 episodes isolating timeout-only, rate-limit-only, partial-response-only, and mixed faults. | Reliability degradation is fault-type dependent, with backoff/retry handling for rate limits as a key weakness. | Ablation results are reported at one fault intensity level (λ=0.2). |
| Combined perturbation and fault stress further depresses reliability beyond clean baseline levels. | For Gemini 2.0 Flash at k=2, baseline (ε=0, λ=0) is 96.88%, degrading to 84.0% under combined stress points. | Measured reliability surface R(k=2, ε, λ) over grid points in Figure 3. | Joint stress evaluation captures compounded reliability loss not represented by single-axis metrics. | Reported surface is sampled at discrete ε and λ levels, not continuous exhaustive coverage. |

## Confidence
high

Justification: The source is a primary arXiv benchmark paper with explicit methodology, multi-axis evaluation design, and clear quantitative results across perturbation, fault, model, and architecture comparisons. Confidence is high because the evidence is structured and result-bearing, with the main caveats being limited model coverage and evaluation over sampled rather than exhaustive stress conditions.
