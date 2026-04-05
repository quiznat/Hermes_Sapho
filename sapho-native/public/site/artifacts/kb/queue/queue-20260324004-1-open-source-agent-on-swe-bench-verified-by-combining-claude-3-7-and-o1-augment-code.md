<details class="traceability-panel">
<summary>Traceability</summary>
<div class="traceability-body">
<ul>
  <li><strong>Source:</strong> <a href="https://www.augmentcode.com/blog/1-open-source-agent-on-swe-bench-verified-by-combining-claude-3-7-and-o1" target="_blank" rel="noopener">https://www.augmentcode.com/blog/1-open-source-agent-on-swe-bench-verified-by-combining-claude-3-7-and-o1</a></li>
  <li><strong>Intake queued:</strong> 2026-03-21T06:28:15Z</li>
  <li><strong>Source captured:</strong> 2026-03-21T22:52:56Z</li>
  <li><strong>Curated:</strong> 2026-04-04T04:42:09Z</li>
  <li><strong>Artifact finalized:</strong> 2026-04-04T04:44:13Z</li>
</ul>
</div>
</details>

# #1 open-source agent on SWE-Bench Verified by combining Claude 3.7 and O1 | Augment Code

## Core Thesis

Augment’s report argues that a high SWE-bench Verified score can be pushed upward by system composition rather than by a single model alone: its submitted setup reportedly reached 65.4% by using Claude Sonnet 3.7 as the main agent and OpenAI o1 as an ensembler, while also inferring a planning component absent from Anthropic’s published configuration. The article’s stronger lesson is not simply that the stack scored well, but that benchmark gains appear sensitive to orchestration choices, rollout instability, and benchmark-specific task structure.

## Why It Matters for Sapho

This matters because it pushes Sapho away from model-brand interpretation and toward system-level evaluation doctrine. The source presents coding-agent performance as a compound outcome shaped by planning, ensembling, search/navigation strategy, and benchmark quirks, not as a clean expression of one frontier model’s intrinsic capability. It also sharpens a live warning: benchmark wins can coexist with weak transfer to production settings, especially when the benchmark is Python-only, relatively short-horizon, and tolerant of simple repository navigation methods that break down in larger real-world codebases.

## Key Findings

- Augment reports a 65.4% success rate on SWE-bench Verified using Claude Sonnet 3.7 as the core driver and OpenAI o1 as the ensembler.
- The company says its main deltas from Anthropic’s published setup were reconstructing an unpublished planning tool and adding o1-based ensembling.
- Augment estimates ensembling contributes roughly 3% to 8% on SWE-bench Verified, but presents that as internal attribution rather than a controlled causal breakdown.
- Claude Sonnet 3.7 “thinking mode” reportedly did not improve SWE-bench performance, cutting against any simple assumption that more explicit deliberation automatically helps coding agents.
- A separate regression-fixing agent showed a split result: it corrected some regressions but also introduced new bugs into otherwise correct candidates, yielding no net score gain.
- The source says outcomes are unstable enough that two rollouts over 50 examples can differ materially, which is part of the rationale for ensembling.
- Augment reports that plain “grep” and “find” were sufficient for SWE-bench tasks, while also arguing that the same navigation pattern becomes inadequate in larger, more ambiguous production environments.
- The source highlights external-validity limits: SWE-bench Verified is Python-only, OpenAI reportedly found only 8.4% of its problems take an experienced engineer more than an hour, and some changes that helped customers did not improve benchmark scores.

## Evidence and Findings

- The article reports a 65.4% SWE-bench Verified result from a hybrid system with Claude Sonnet 3.7 driving the workflow and o1 serving as ensembler, supporting the conclusion that benchmark performance here is being framed as a systems-engineering outcome rather than a single-model result. That matters because leaderboard interpretation can otherwise collapse architecture into branding.
- Augment identifies two main differences from Anthropic’s published setup: inferred use of an unpublished planning tool and the addition of o1 ensembling. It further estimates ensembling adds 3% to 8%, which supports the narrower conclusion that aggregation across runs or candidates may be a material lever on this benchmark, even if the exact share attributable to each design change is not isolated.
- The source reports that Claude Sonnet 3.7 thinking mode did not help on SWE-bench. That negative result supports a bounded conclusion: extra deliberative mode is not automatically a free performance gain in agentic coding benchmarks, and benchmark success may depend more on execution structure, search behavior, or candidate selection than on simply invoking a more reflective inference mode.
- Augment says rollout variance is high enough that two samples over 50 examples can differ in outcome, and uses that instability to justify ensembling. This supports the view that benchmark scores here are noisy enough that single-run comparisons can mislead, which matters for Sapho because apparent leadership margins may partly reflect variance management rather than stable capability differences.
- On repository interaction, the source says “grep” and “find” were sufficient for SWE-bench, with embedding retrieval not the bottleneck, but also says that approach runs into limits in real-world settings with ambiguous user requests and large codebases. That supports a practical conclusion: the benchmark may reward narrow navigation competence that does not map cleanly onto production coding support.
- The article itself supplies reasons to bound transfer: SWE-bench includes only Python projects; it argues Python is easier for agents than Java or C++ because error messages are often more descriptive; and it cites a prior finding that only 8.4% of SWE-bench Verified tasks take an experienced software engineer more than an hour. Together these points support the conclusion that benchmark performance may overstate breadth, depth, and real-world labor substitution.

## Contradictions and Tensions

- The headline result is strong, but the source simultaneously argues that the benchmark is unstable enough for rollout variance to matter materially. That creates tension between leaderboard precision and actual confidence in small score differences.
- The article presents ensembling as a likely gain lever, yet does not cleanly separate how much of the final score came from ensembling versus planning-tool reconstruction or other implementation choices. The system wins, but the causal story remains partially unresolved.
- Claude Sonnet 3.7 thinking mode reportedly did not help, which runs against the common intuition that more explicit reasoning should improve agent outcomes. On this benchmark, added deliberation appears not to convert cleanly into higher pass rates.
- A dedicated regression-fixing agent improved some bad candidates but also damaged some good ones, leaving no net gain. That exposes a core agent-design tension: corrective subroutines can raise capability on one slice while degrading reliability on another.
- The source says simple command-line navigation works well on SWE-bench while also saying that the same pattern is insufficient in customer settings. Benchmark competence and production usefulness are therefore not aligned by default.
- Augment reports that some changes improving production agents in qualitative customer feedback did not improve SWE-bench scores. That is a direct warning that benchmark optimization can miss user-relevant capability.

## Mechanism or Bounds

The strongest supported mechanism is ensemble stabilization under noisy benchmark conditions. If rollouts vary enough that repeated samples over 50 examples produce different outcomes, then selecting or aggregating across candidates can raise observed performance without requiring a uniformly stronger base policy on every run. A second bounded mechanism is task-structure fit: SWE-bench appears navigable with lightweight tools such as “grep” and “find,” which implies that retrieval complexity is not the main constraint in this environment. But these mechanisms are benchmark-bound. The source does not provide a controlled decomposition proving how much planning reconstruction, ensembling, or any other component individually caused the 65.4% result, and its own discussion limits transfer beyond Python-heavy, relatively constrained repository tasks.

## Limits

The article is self-reported by the system builder, so the main quantitative claims should be treated as reported outcomes, not independently replicated findings.
The causal account is incomplete: the source names key implementation changes but does not isolate their contributions with a clean ablation table.
The negative result for thinking mode is real but underexplained; the evidence does not show whether the failure came from task structure, prompt design, latency tradeoffs, or another runtime constraint.
External validity is materially limited by benchmark scope: Python-only tasks, relatively modest task difficulty, and repository navigation patterns that may not survive contact with larger, messier production codebases.
The source itself acknowledges a mismatch between benchmark gains and customer-facing usefulness, so the result should update beliefs about benchmark engineering more than beliefs about broad coding-agent deployment readiness.
