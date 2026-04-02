# Queue Artifact — art-2026-03-02-025

Source URL: https://arxiv.org/abs/2512.08296  
Alternate surface: https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work  
Lane: agent-factory  
Decision: retain

This paper provides controlled empirical grounding for agent-system architecture choices, complementing the prior blog-level intake (`art-2026-03-02-008`) with benchmarked evidence. The study evaluates 180 configurations across five architecture families (single-agent plus four multi-agent topologies) and reports measurable interaction effects between model capability, coordination structure, task type, and compute budget.

The key operational signal is conditionality: multi-agent structure is not a universal upgrade. Reported results show strong gains in some settings (for example centralized coordination on parallelizable tasks) but degradation on others (notably sequential reasoning tasks), alongside explicit overhead and error-amplification patterns. In factory terms, topology selection should be policy-driven by task profile and baseline capability, not ideology.

For Sapho Chapterhouse Institute governance, this source strengthens a decision rule already emerging from retained corpus: require architecture selection gates that test for coordination benefit under task-specific constraints, and default to simpler single-agent flows once baseline performance crosses capability-saturation thresholds.

<!-- canonical-empirical-findings -->

## Empirical Findings (Data Snapshot)

| Novel finding | Quantitative result | Experimental setup/sample | Metric/outcome | Caveat/limit |
|---|---|---|---|---|
| Topology benefit is task-conditional, not universal | Centralized coordination improved parallelizable-task performance by **80.8%**; for web navigation, decentralized gained **+9.2%** vs centralized **+0.2%** | Controlled evaluation across **180 configurations**, **5 architectures**, **4 benchmarks**, **3 LLM families** | Relative performance uplift by topology and task type | Effect sizes are benchmark/task dependent; should not be applied as global defaults |
| Error amplification differs sharply by coordination pattern | Independent-agent setups amplified errors by **17.2x** vs **4.4x** under centralized coordination | Cross-topology comparison within same benchmarked configuration space | Error propagation multiplier | Amplification factor is sensitive to implementation details and coordination policy |
| Coordination value saturates with stronger single-agent baseline | Coordination returns became diminishing/negative once single-agent baselines exceeded **~45%** | Scaling analysis over agent quantity, topology, capability, and task properties | Coordination ROI regime boundary | Threshold is empirical in this study, not a universal constant |
| Coordination-aware predictors can generalize | Cross-validated predictor achieved **R²=0.524**; selected optimal strategy for **87%** of held-out configs; out-of-sample GPT-5.2 validation reported **MAE=0.071** | Coordination-metric predictive model trained on controlled config matrix and tested on unseen domains/model | Strategy selection accuracy + forecast error | Predictive reliability depends on feature quality and domain shift level |
