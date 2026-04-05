# SWE Context Bench: A Benchmark for Context Learning in Coding

## Core Thesis

SWE-ContextBench reframes coding-agent evaluation around context reuse rather than isolated task solving by pairing 300 SWE-Bench Lite tasks with 99 manually verified related tasks from real issue and pull-request relationships. In the reported benchmark results, compact high-quality summaries of prior work improved resolution, runtime, and cost more than either no prior experience or reuse of full prior trajectories, while poor summary reuse made performance worse.

## Why It Matters for Sapho

This matters because it cuts against a naive "more context is better" doctrine for coding systems. The paper suggests that context only becomes operationally useful when it is compressed into the right form and selected well. For Sapho, that sharpens evaluation doctrine: systems should be judged not just on whether they solve tasks, but on whether they convert prior work into reliable, decision-relevant context without bloating runtime, cost, or failure rates.

## Key Findings

- The benchmark extends SWE-Bench Lite into a context-learning setting by starting from 300 real-world GitHub instances and linking them to 99 related tasks across 12 repositories using real issue and pull-request relationships with manual verification.
- Evaluation is not limited to task success: each related task is checked with FAIL_TO_PASS tests for issue resolution and PASS_TO_PASS tests for regressions, and the benchmark also tracks runtime and monetary cost.
- Across the 99 related tasks, the average instance includes 5.09 FAIL_TO_PASS tests and 128.32 PASS_TO_PASS tests, giving a relatively dense regression surface rather than a single-pass correctness check.
- Oracle summary reuse delivered the best reported resolution rate at 34.34%, ahead of the no-experience baseline at 26.26% and ahead of oracle full-experience reuse at 27.27%.
- Oracle summary reuse also had the best efficiency result, with the lowest average runtime at 356.95 seconds per task and the lowest average cost at $0.77 per instance.
- Summary length appears central to the result profile: summaries averaged 204.5 words, while full experience trajectories averaged 24,765 words.
- Summary reuse is not automatically helpful: free summary reuse fell below baseline at 22.22% resolved and produced the highest number of patch application failures, with 7 instances.

## Evidence and Findings

- The benchmark construction is grounded in real software-maintenance relationships rather than synthetic pairings: from 300 SWE-Bench Lite instances, the authors identified 89 interdependent task instances, then added 10 more through recursive expansion, yielding 99 related tasks across 12 repositories. That supports the claim that this is a context-learning benchmark built from real task adjacency, not a toy setup.
- The evaluation design measures whether a fix works and whether it breaks anything else. Related-task instances include a pre-fix base commit, a problem statement, and ground-truth code changes split into test_patch and solution_patch, then use FAIL_TO_PASS and PASS_TO_PASS tests for validation. That matters because it makes the benchmark about applied software repair under regression pressure, not only about text generation quality.
- The test burden is substantial: the average related task carries 5.09 FAIL_TO_PASS tests and 128.32 PASS_TO_PASS tests. That supports treating the reported results as more than anecdotal patch success, because performance is checked against both target-fix and non-regression criteria.
- In the reported outcomes, oracle summary reuse reached 34.34% resolution versus 26.26% for the no-experience baseline, while oracle full-experience reuse reached only 27.27%. This supports the paper's central empirical point that compact prior-task distillation can outperform both no reuse and raw trajectory reuse under the tested setup.
- Efficiency moved in the same direction as accuracy: oracle summary reuse posted the lowest average runtime at 356.95 seconds per task and the lowest average cost at $0.77 per instance. That matters because the winning condition here is not accuracy purchased by higher latency or spend, but a better joint operating point.
- The compression gap is extreme: summaries averaged 204.5 words, while full experience trajectories averaged 24,765 words. Alongside the performance results, this supports a bounded conclusion that the useful part of prior experience may be the distilled decision content rather than the full interaction trace.
- The negative result is equally important: free summary reuse resolved only 22.22% of tasks and produced 7 patch application failures, the highest among the reported settings. That supports the claim that summary quality and relevance matter; compressed context can help, but unreliable compression can actively degrade performance.

## Contradictions and Tensions

- The clearest tension is that full prior experience did not meaningfully outperform the no-experience baseline and lagged far behind oracle summaries. A simple "more prior context helps more" story does not survive the reported comparison.
- The paper's strongest positive result depends on oracle-quality summary reuse, while non-oracle summary reuse was worse than doing nothing. That creates a practical tension between the benchmark's promise and deployment reality: the useful form of context is also the form most sensitive to summary quality.
- The benchmark tracks accuracy, runtime, and cost together, and the best-performing summary condition was also the cheapest and fastest. That is encouraging, but it also raises an interpretive tension: the gains may reflect better information selection and lower processing burden at the same time, making it difficult to isolate which factor is carrying the improvement.
- Because the benchmark is built from 99 related tasks across 12 repositories, the results are meaningful but still bounded. A method that wins under these repository relationships and retrieval settings may not generalize cleanly to other codebases, task structures, or more weakly related context.

## Mechanism or Bounds

The strongest bounded explanation is that prior experience helps when it is distilled into short, task-relevant context that preserves decision-critical information while avoiding the overload and noise of full interaction histories. The reported length gap—204.5 words for summaries versus 24,765 words for full trajectories—fits that interpretation, and the resolution, runtime, and cost results all move in the same direction under oracle summary reuse.

But the paper does not prove a full causal mechanism. It shows a benchmark-specific pattern: compressed, reliable summaries outperform raw trajectories and poor summaries under the tested retrieval and evaluation setup. The evidence supports an operational rule—usefulness depends on relevance and quality of compression—not a universal law that summaries always beat full history in coding work.

## Limits

- The evidence establishes benchmark design and benchmark results, not broad real-world causal guarantees about how coding agents learn from context in production.
- The strongest performance result uses oracle summary reuse, which is not the same as showing that ordinary systems can reliably generate or retrieve summaries of comparable quality.
- The paper shows that free summary reuse can be harmful, but it does not fully pin down the failure pathway; misleading summaries, retrieval error, and degraded patch generation remain plausible but unresolved explanations.
- The benchmark covers 99 related tasks across 12 repositories, so external validity is constrained by repository mix, task dependence structure, and the specific evaluation setup used here.
- Test-based validation is stronger than subjective scoring, but it still captures only the dimensions the benchmark measures; it does not exhaustively represent all forms of real-world coding utility.
