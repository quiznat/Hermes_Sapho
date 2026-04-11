---
version: article.v1
article_id: art-2026-03-12-004
ticket_id: ticket-import-art-2026-03-12-004
source_url: https://arxiv.org/html/2601.06112v1
source_title: 'ReliabilityBench: Evaluating LLM Agent Reliability Under Production-Like
  Stress Conditions'
queued_at_utc: '2026-03-12T20:35:02Z'
captured_at_utc: '2026-04-11T13:22:25Z'
canonical_url: https://arxiv.org/abs/2601.06112
curator_decision: kept
artifact_minted_at_utc: '2026-04-11T13:25:17Z'
evidence_count: 14
claim_count: 4
publication_status: ready-for-daily
imported_from_runtime_article_id: art-2026-03-12-004
imported_from_runtime_last_stage: intake
imported_from_runtime_filter_state: pending
source_remediation_status: completed
source_remediated_at_utc: '2026-04-11T13:22:25Z'
curator_reason: This preprint reports a concrete multi-model benchmark with measured
  reliability results under stress conditions.
curated_at_utc: '2026-04-11T13:22:42Z'
curator_mode: agent
extracted_at_utc: '2026-04-11T13:25:17Z'
extractor_mode: agent
findings_mode: agent
summary_mode: agent
artifact_publication_alias: '20260312004'
artifact_publication_status: published
artifact_publication_minted_at_utc: '2026-04-11T13:25:17Z'
artifact_publication_published_at_utc: '2026-04-11T13:37:44Z'
---
# ReliabilityBench: Evaluating LLM Agent Reliability Under Production-Like Stress Conditions

## Core Thesis

ReliabilityBench argues that agent quality cannot be read off a single clean run. It measures reliability as a stress surface across repeated-execution consistency, prompt perturbation robustness, and infrastructure-failure tolerance, then shows that even a strong reported configuration degrades materially once those production-like stresses are applied together.

## Why It Matters for Sapho

This matters because Sapho should treat single-run benchmark success as an incomplete signal for operational trust. The paper gives a more decision-relevant frame: ask whether an agent stays correct when instructions are perturbed, when failures are injected into the tool path, and when the same task is run again. It also reinforces a doctrine Sapho should keep: reliability claims must remain benchmark-bounded, because stress performance varies by architecture, domain, and fault type, and small episode counts understate uncertainty around rare failures.

## Key Findings

- The benchmark is built around three reliability dimensions: repeated-execution consistency, perturbation robustness, and infrastructure-failure fault tolerance, rather than a single pass/fail score on one clean attempt.
- Its unified reliability surface R(k, ε, λ) is a measurement frame for how consistency, perturbation stress, and fault stress interact, and its perturbation design judges equivalent end state rather than textual overlap.
- In the reported Gemini 2.0 Flash results, pass rate drops from 96.88% at baseline to 88.12% at ε=0.2, showing that prompt perturbation alone erodes reliability.
- Under combined stress for Gemini 2.0 Flash at k=2, measured pass rate falls further to 84.0%, indicating that perturbation and infrastructure faults compound degradation.
- ReAct outperforms Reflexion for Gemini 2.0 Flash in the reported setup: surface volume is 0.900 versus 0.875, ε=0.2 pass rate is 90.0% versus 86.3%, and recovery under λ=0.2 is 80.9% versus 67.3%.
- Reliability is heterogeneous rather than uniform: in one reported baseline setting, scheduling reaches 100% pass@1 and 100% pass² while travel reaches 87.5% pass@1 and 75.0% pass².
- The study covers Gemini 2.0 Flash and GPT-4o, ReAct and Reflexion, four domains, and 1,280 total episodes, but the paper explicitly notes that rare-failure estimation may require 10,000+ episodes for tight confidence intervals.

## Evidence and Findings

- The source shows a deliberate shift away from single-run evaluation toward a three-axis reliability frame spanning consistency, perturbation robustness, and fault tolerance. That supports the conclusion that production-like agent evaluation must ask how performance moves across repeated runs and stressors, not just whether one clean execution succeeds.
- The benchmark operationalizes this with a unified reliability surface R(k, ε, λ) and with action-based perturbation checks judged by equivalent end state rather than text similarity. That matters because tool-using agents should be assessed on whether they still complete the task correctly, not whether they reproduce the same wording.
- In Gemini 2.0 Flash, prompt perturbation is not cosmetic noise: pass rate declines from 96.88% at ε=0.0 to 88.12% at ε=0.2. This supports the conclusion that instruction variation alone can materially weaken apparent agent reliability even before infrastructure faults are added.
- The combined-stress point is worse: for Gemini 2.0 Flash at k=2, pass rate falls to 84.0% under joint perturbation and fault stress. That matters because systems that look strong in baseline conditions can lose a meaningful amount of reliability when real operating pressures stack rather than arrive in isolation.
- Architecture choice changes outcomes under the same reported conditions. ReAct beats Reflexion on surface volume, on stressed pass rate at ε=0.2, and on recovery at λ=0.2 with 38 successful recoveries out of 47 encountered faults versus 35 out of 52. That supports the conclusion that reliability is partly implementation-sensitive, not just model-sensitive.
- The paper also shows that reliability is uneven across domains and fault types: scheduling remains perfect in one baseline setting while travel is materially worse, and at λ=0.2 the rate-limit-only condition posts the lowest pass rate at 93.75%, 2.50 percentage points below the mixed-fault baseline of 96.25%. This matters because aggregate scores can hide where systems are actually brittle.

## Contradictions and Tensions

- The central tension is between very high clean-condition performance and visibly weaker stressed performance. A 96.88% baseline for Gemini 2.0 Flash can invite confidence that the system is reliable, but that confidence is cut down once perturbation pushes the score to 88.12% and combined stress pushes it to 84.0%.
- Reliability is not monotone across all task environments. Scheduling achieves 100% pass@1 and 100% pass² in the reported baseline setting, while travel falls to 87.5% pass@1 and 75.0% pass², which means “agent reliability” is partly a domain-composition statement rather than a single portable property.
- Fault difficulty is also uneven. The rate-limit-only condition is more damaging than the mixed-fault baseline at λ=0.2, suggesting that some seemingly narrower fault classes can be harder than broader synthetic bundles.
- The paper presents useful quantitative differences between ReAct and Reflexion, but not a demonstrated causal account of why the gap appears. The practical result is visible; the reason for it remains unresolved.
- The benchmark is designed to improve realism, yet the authors still concede that 1,280 episodes may be too small for tight estimation of rare failures. That creates a tension between methodological ambition and statistical precision exactly where production reliability claims are often most fragile.

## Mechanism or Bounds

The strongest supported mechanism here is methodological and operational rather than causal. ReliabilityBench treats reliability as an interaction across repeat count, perturbation magnitude, and fault intensity, and it evaluates perturbed tasks by whether the agent reaches an equivalent end state. That gives a stronger operational picture of agent stability than single-run success.

For the reported performance drops, the evidence supports a bounded explanation: Gemini 2.0 Flash is sensitive to prompt perturbation, and reliability degrades further when perturbation is combined with injected tool-path stress. For the ReAct-versus-Reflexion difference, the evidence establishes comparative advantage under the reported settings but does not establish why ReAct is stronger. All conclusions are benchmark-bound: they depend on the tested domains, architectures, fault injections, and episode counts rather than proving a general law of production reliability.

## Limits

The paper improves the measurement frame, but it does not prove that the benchmark fully captures real production reliability.
The fault injections are simulated production-like failures, not observed incident frequencies from a live deployment.
Architecture comparisons are descriptive within the reported setup and do not establish mechanism.
Performance varies materially by domain and fault type, so aggregate reliability claims can conceal important pockets of brittleness.
The authors explicitly note that 1,280 episodes may be inadequate for tight confidence intervals on rare failure modes, with 10,000+ episodes potentially needed for stronger estimation.
