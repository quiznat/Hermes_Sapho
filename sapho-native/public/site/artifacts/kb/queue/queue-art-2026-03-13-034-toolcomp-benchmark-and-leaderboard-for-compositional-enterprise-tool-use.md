# Queue Item Processing — art-2026-03-13-034

## Source metadata
- URL: https://labs.scale.com/leaderboard/tool_use_enterprise
- Source type: firehose-brave
- Lane tags: `UI-design, UI-design`
- Curated at (UTC): 2026-03-13T08:32:31Z
- Finalized at (UTC): 2026-03-13T20:04:16Z

## Source custody
- Source snapshot: `research/evidence/source-material/2026-03-13/art-2026-03-13-034.json`
- Clean text path: `research/evidence/source-material/2026-03-13/art-2026-03-13-034.txt`

## Core thesis
ToolComp is designed to evaluate whether LLM agents can correctly execute dependent multi-tool chains in realistic settings, using human-verified final answers and step-level process supervision rather than single-step tool invocation checks.

## Mechanism summary
The benchmark contains 485 examples split into ToolComp-Enterprise with 287 examples across 11 tools and ToolComp-Chat with 198 examples across 2 tools. It targets long-horizon tool composition, with about 85% of prompts requiring at least three tools and about 20% requiring seven or more tool calls. Labels are built through a hybrid human-AI ReAct workflow in which annotators mark steps correct or incorrect, edit incorrect steps, and continue generation until a correct finish is reached, producing one valid successful chain plus process-supervision annotations. Main leaderboard evaluation uses GPT-4-Turbo grading to assess final-answer correctness while treating both correct and correct-with-bad-formatting outputs as accurate; the top listed score is o1 (December 2024) at 70.14 ± 5.32.

## Why it matters for Sapho
This matters as a benchmark artifact because it moves tool-use evaluation closer to enterprise operating conditions, where success depends on chaining multiple dependent tools over longer trajectories rather than calling a single function correctly once. Its significance is methodological: the combination of constrained tool subsets, human-corrected process supervision, and semantic final-answer grading makes the benchmark useful for studying both execution correctness and workflow robustness, while also making clear that leaderboard scores are conditioned on specific allowed-tool settings and an LLM-judge evaluation regime.

<!-- canonical-empirical-findings -->

## Empirical Findings (Data Snapshot)

| Novel finding | Quantitative result | Experimental setup/sample | Metric/outcome | Caveat/limit |
|---|---|---|---|---|
| ToolComp explicitly targets dependent multi-tool composition and is split into enterprise and chat subsets with distinct tool access. | Total dataset size is 485 examples, split into 287 ToolComp-Enterprise examples (11 tools) and 198 ToolComp-Chat examples (2 tools). | Prompts require sequential tool dependency where outputs of earlier tools motivate inputs to later tools; only subset-allowed tools are permitted during generation, labeling, and evaluation. | The benchmark operationalizes enterprise-style tool orchestration by testing larger tool-selection spaces (11 tools) versus minimal chatbot tooling (2 tools). | Subset constraints mean evaluations are conditioned on allowed tool sets rather than unrestricted tool ecosystems. |
| Benchmark complexity is intentionally long-horizon, with most prompts requiring multi-step tool chains. | About 85% of prompts require at least three tools, and approximately 20% require seven or more tool calls. | Complexity is defined as number of tools required per prompt, with distribution summarized in Figure 6. | High-chain-depth tasks demand longer-context reasoning and stronger tool-chaining capability. | Complexity is measured by tool-call count, which may not fully capture semantic difficulty. |
| Process-supervision labels are produced through iterative human correction of ReAct steps rather than one-shot model outputs. | Each step (Action Plan and ReAct substeps) is labeled Correct/Incorrect; incorrect steps are edited by annotators and generation continues until a Correct Finish step is reached. | Hybrid human-AI labeling pipeline: LLM proposes plan and tool calls, annotators validate/correct each step, and corrected context is fed forward iteratively. | The final dataset includes one valid successful chain plus incorrect/correct step annotations for supervision. | Labels depend on annotator judgments and correction interventions during trajectory construction. |
| Main leaderboard evaluation uses LLM grading to prioritize semantic correctness over strict formatting. | Judge model is GPT-4-Turbo; labels are Incorrect, Correct with bad formatting, or Correct, and both Correct categories count as accurate. Top listed score is o1 (December 2024) at 70.14 ± 5.32. | Evaluated model generates action plan, performs native function calling, and outputs final answer; GPT-4-Turbo compares output against ground truth for grading. | Leaderboard emphasizes tool-use correctness while reducing penalties from answer-format variance. | Using an LLM judge introduces model-mediated grading assumptions; exact formatting is intentionally de-emphasized. |

## Confidence
high

Justification: The source is a direct benchmark surface with concrete dataset structure, process-labeling methodology, and published leaderboard statistics, so the evidence is strong for claims about benchmark design and evaluation regime. The main caveat is that results are conditioned on allowed tool subsets and an LLM-judge grading setup, which limits straightforward comparison to unrestricted or differently scored tool-use environments.
