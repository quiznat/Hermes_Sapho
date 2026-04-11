---
version: article.v1
article_id: art-2026-03-11-017
ticket_id: ticket-import-art-2026-03-11-017
source_url: https://arxiv.org/html/2505.02133v1
source_title: 'Enhancing LLM Code Generation: A Systematic Evaluation of Multi-Agent
  Collaboration and Runtime Debugging for Improved Accuracy, Reliability, and Latency'
queued_at_utc: '2026-03-11T07:31:08Z'
captured_at_utc: '2026-04-11T13:15:13Z'
canonical_url: https://arxiv.org/abs/2505.02133
curator_decision: kept
artifact_minted_at_utc: '2026-04-11T13:17:53Z'
evidence_count: 10
claim_count: 4
publication_status: ready-for-daily
imported_from_runtime_article_id: art-2026-03-11-017
imported_from_runtime_last_stage: facts
imported_from_runtime_filter_state: pending
source_remediation_status: completed
source_remediated_at_utc: '2026-04-11T13:15:13Z'
curator_reason: This is a preprint reporting a multi-model empirical code-generation
  evaluation with benchmark results.
curated_at_utc: '2026-04-11T13:15:35Z'
curator_mode: agent
extracted_at_utc: '2026-04-11T13:17:53Z'
extractor_mode: agent
findings_mode: agent
summary_mode: agent
artifact_publication_alias: '20260311017'
artifact_publication_status: published
artifact_publication_minted_at_utc: '2026-04-11T13:17:53Z'
artifact_publication_published_at_utc: '2026-04-11T13:37:42Z'
---
# Enhancing LLM Code Generation: A Systematic Evaluation of Multi-Agent Collaboration and Runtime Debugging for Improved Accuracy, Reliability, and Latency

## Core Thesis

Adding runtime debugging to a simple multi-agent code-generation workflow improves results relative to the same workflow without debugging, but the gains are modest, not clearly superior to debugging alone on HumanEval, and do not support the broader story that more agentic complexity reliably produces better code.

## Why It Matters for Sapho

This matters because it cuts against an easy doctrine that more agents, more chaining, and more orchestration naturally buy reliability. The paper supports a narrower operating view: debugging carries real value, simple collaboration can help at the margin, and stricter evaluation can reverse apparent wins. For Sapho, that means code-agent systems should be judged on benchmark rigor, robustness under harder tests, and incremental value over strong debugging baselines rather than on architectural complexity alone.

## Key Findings

- Across 19 LLMs and two code-generation datasets, a simple Analyst-Coder plus debugging workflow improved mean accuracy over debugging alone by 0.68%, which supports a real but small aggregate gain rather than a large systems-level jump.
- On HumanEval, ACT+Debug reached 64.82% mean functional accuracy versus 57.16% for ACT alone, and the paper reports this improvement as statistically significant under its one-tailed paired t-test setup at alpha = 0.15.
- On the same HumanEval comparison, ACT+Debug scored 64.82% versus 63.86% for Debug alone, a mean gain of only 0.96%, and the paper reports that this difference was not statistically significant at alpha = 0.15.
- More orchestration did not reliably help: adding a three-agent Analyst-Coder-Tester workflow reduced accuracy for most models.
- Under stricter evaluation, the story worsened for the more elaborate setup: HumanEval+ uses 80 times more tests than HumanEval, AC+Debug posted the highest mean score, and ACT+Debug trailed it by 1.22% while also showing the largest robustness drop.
- The paper’s bounded explanation is that the tester phase can lean on visible test cases that miss edge cases, so apparent success under lighter evaluation can fail to carry over to stricter testing.

## Evidence and Findings

- The empirical base is broad enough to matter operationally: the study evaluates 19 LLMs on two code-generation benchmark datasets, so its conclusions are not resting on a single model anecdote or one narrow benchmark run.
- The strongest clean result is the value of adding debugging to ACT on HumanEval: mean functional accuracy rises from 57.16% to 64.82%, and the paper treats that gain as statistically significant at alpha = 0.15, which supports debugging as a meaningful corrective layer for that workflow.
- The stronger claim that ACT+Debug beats debugging alone is not carried by the evidence here: the mean advantage is just 0.96% on HumanEval, from 63.86% to 64.82%, and the paper says that difference is not statistically significant under the reported test setup.
- The paper still finds a modest aggregate case for simple collaboration: Analyst-Coder plus debugging improves mean accuracy by 0.68% over debugging alone across 19 models and two datasets, suggesting some value from role separation, but only at the level of a slight lift.
- The evidence against “more agents is better” is concrete rather than rhetorical: adding the three-agent Analyst-Coder-Tester workflow reduced accuracy for most models, which means extra structure can degrade output instead of stabilizing it.
- Stricter testing changes the ranking in a decision-relevant way: HumanEval+ expands HumanEval with 80 times more tests, AC+Debug leads there, and ACT+Debug performs 1.22% worse while suffering the largest robustness drop, indicating that some gains under lighter evaluation do not survive harsher edge-case coverage.

## Contradictions and Tensions

- The paper presents a visible tension between higher average performance and weak proof of superiority: ACT+Debug posts the best HumanEval mean among the listed approaches, yet its 0.96% edge over Debug alone is not statistically significant.
- There is a direct conflict between the intuitive “more agentic structure helps” narrative and the reported outcomes: the three-agent workflow reduces accuracy for most models, and the stricter HumanEval+ ranking puts the simpler AC+Debug above ACT+Debug.
- Benchmark strictness materially changes interpretation. A workflow that looks strongest on HumanEval also shows the largest robustness drop on HumanEval+, which means lighter benchmark wins can conceal fragility.
- The aggregate gain from simple collaboration exists but is small. That creates a tension between practical usefulness and doctrinal overstatement: the result is enough to justify attention, but not enough to justify sweeping claims about multi-agent superiority.

## Mechanism or Bounds

The paper supports a bounded operational mechanism rather than a fully established causal account. The key explanation is that the tester stage in ACT relies on visible test cases, and those test cases may miss edge cases. Under that condition, the workflow can appear stronger on a benchmark with narrower test exposure while failing to catch deeper errors that emerge under more rigorous evaluation. The study also reports an empirical pattern that combining agentic and debugging methods tends to help more when the baseline performance gap between them is small, but that pattern should be treated as study-specific guidance rather than a general law. Overall, the evidence supports benchmark-bound conclusions about observed performance differences, not a universal mechanism showing why added agents should improve code generation.

## Limits

The paper does not establish a strong causal mechanism for why the combined workflows help or fail beyond the bounded explanation about visible tests and missed edge cases.
The reported statistical support is limited by the paper’s own testing setup, including a one-tailed paired t-test and an alpha threshold of 0.15, which weakens any attempt to make stronger superiority claims.
The observed advantage of simple multi-agent collaboration over debugging alone is small, so it should not be generalized into a large expected effect.
The stricter HumanEval+ results show that benchmark wins can reverse when test coverage expands, leaving real uncertainty about how well these workflows transfer to harder or more adversarial coding conditions.
