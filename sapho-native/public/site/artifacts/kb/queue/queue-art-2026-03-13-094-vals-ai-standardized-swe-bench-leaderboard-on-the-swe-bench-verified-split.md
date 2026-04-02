# Queue Item Processing — art-2026-03-13-094

## Source metadata
- URL: https://www.vals.ai/benchmarks/swebench
- Source type: firehose-brave
- Lane tags: `agent-factory, agent-factory`
- Curated at (UTC): 2026-03-13T17:05:32Z
- Finalized at (UTC): 2026-03-13T20:09:54Z

## Source custody
- Source snapshot: `research/evidence/source-material/2026-03-13/art-2026-03-13-094.json`
- Clean text path: `research/evidence/source-material/2026-03-13/art-2026-03-13-094.txt`

## Core thesis
Using a common SWE-Agent-based harness on the 500-task SWE-bench Verified split, frontier coding models cluster in the high-70% range at the top, while long-horizon task difficulty and harness constraints materially shape comparative outcomes.

## Mechanism summary
The Vals benchmark page evaluates models on 500 human-validated SWE-bench Verified tasks using the same SWE-Agent harness, identical tool access, default provider settings except max token limit, and a fixed 150-step cap per task on a shared EC2 environment. Reported leaderboard results place Claude Opus 4.6 (Thinking) at 79.20%, GPT 5.4 at 77.20%, and Gemini 3 Flash (12/25) at 76.20%. The page also analyzes difficulty bands, noting that the three hardest tasks are estimated above four hours and are rarely solved by state-of-the-art models, while the clearest model separation appears in the 15-minutes-to-1-hour range; the 150-step budget was calibrated from the 42 tasks in the 1-to-4-hour category with an added buffer.

## Why it matters for Sapho
This matters as a comparative benchmark artifact because it isolates model differences under a shared harness rather than mixing base-model quality with provider-specific scaffolding choices. Its significance is twofold: first, frontier performance on SWE-bench Verified appears tightly clustered near the high-70% range under standardized conditions; second, the page makes clear that harness design, step budgets, and task-difficulty composition are central determinants of observed leaderboard outcomes, so these results are useful for apples-to-apples comparison but should not be mistaken for provider-optimized ceilings.

<!-- canonical-empirical-findings -->

## Empirical Findings (Data Snapshot)

| Novel finding | Quantitative result | Experimental setup/sample | Metric/outcome | Caveat/limit |
|---|---|---|---|---|
| The top of the Vals SWE-bench leaderboard is led by frontier closed-source models with scores near 80%. | Claude Opus 4.6 (Thinking) scores 79.20%, GPT 5.4 scores 77.20%, and Gemini 3 Flash (12/25) scores 76.20%. | These results are reported on the SWE-bench benchmark page using Vals AI's standardized evaluation framework. | Claude Opus 4.6 (Thinking) is listed as the highest-accuracy model among the models shown in the takeaways section. | The page reports leaderboard performance but does not include confidence intervals or run-to-run variance for these scores in the provided excerpt. |
| The benchmark difficulty distribution is not uniform; the most discriminative band is medium-to-long tasks rather than the very hardest tasks. | The three hardest tasks are estimated to take more than 4 hours, and SOTA models have been unable to solve more than one task in this category. The step-budget calibration set was the “1-4 hours” category comprising 42 instances. | Vals analyzes task difficulty categories and uses them to reason about step limits and model differentiation on SWE-bench. | Performance differences are clearest on tasks estimated to take between 15 minutes and 1 hour, while the >4 hour tasks remain mostly unsolved. | The time estimates are benchmark difficulty annotations rather than direct wall-clock measurements of human or model runtime. |
| Vals uses the full SWE-bench Verified split with a common harness and identical tool access across models. | The evaluation uses 500 high-quality test cases from SWE-bench Verified. | All models were run on the SWE-agent harness with the same available tools, default provider settings except max token limit, and the Verified subset released in August 2024. | The methodology is designed for apples-to-apples comparison across models rather than model-specific custom harness optimization. | The page notes that custom harnesses may yield better results for some providers, so these results reflect standardized rather than provider-optimized performance. |
| The evaluation imposes a fixed per-task step budget chosen from empirical analysis of harder tasks. | Models were constrained to a maximum of 150 steps per task, derived from the highest step count needed to resolve instances in the “1-4 hours” difficulty category with a 150% buffer added; that category comprised 42 instances. | Both larger and smaller models were evaluated under this 150-step limit within the SWE-agent framework on an 8 vCPU, 32GB RAM EC2 instance. | The step cap is intended to preserve fairness while covering the observed resolution range of harder but not extreme tasks. | A different harness or step budget could change relative scores, as the page explicitly notes custom harnesses may improve outcomes. |

## Confidence
high

Justification: The source is a direct benchmark surface with explicit harness settings, task set, and published model scores, so it strongly supports claims about standardized cross-model comparison on SWE-bench Verified. The main caveats are that the excerpt does not provide run-to-run variance and that results are conditional on the chosen standardized harness and 150-step budget rather than custom provider-optimized setups.
