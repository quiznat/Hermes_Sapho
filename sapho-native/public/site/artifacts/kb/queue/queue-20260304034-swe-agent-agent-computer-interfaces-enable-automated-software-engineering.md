<details class="traceability-panel">
<summary>Traceability</summary>
<div class="traceability-body">
<ul>
  <li><strong>Source:</strong> <a href="https://arxiv.org/abs/2405.15793" target="_blank" rel="noopener">https://arxiv.org/abs/2405.15793</a></li>
  <li><strong>Intake queued:</strong> 2026-03-04T03:59:01Z</li>
  <li><strong>Source captured:</strong> 2026-03-30T17:31:45Z</li>
  <li><strong>Curated:</strong> 2026-04-02T23:22:30Z</li>
  <li><strong>Artifact finalized:</strong> 2026-04-02T23:24:49Z</li>
  <li><strong>Artifact published:</strong> 2026-03-30T17:31:53Z</li>
</ul>
</div>
</details>

# SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering

## Core Thesis

Software-engineering agents improve materially when the model is not left to operate through a raw shell alone but is given a language-model-tailored interface for search, file viewing, and guarded editing. In this paper, that interface raises benchmark solve rates versus prior non-interactive and shell-only setups, but the gain is still bounded by low absolute success on real repository tasks and by persistent editing failure inside the same system.

## Why It Matters for Sapho

This matters because it shifts the relevant unit of evaluation from “which frontier model was used” to “what operating interface the model was allowed to use.” The paper supports a doctrine Sapho should take seriously: agent performance in software work is not just a model property but an interface-and-feedback property. At the same time, the results warn against smooth automation narratives. Better tooling around the model helps, but even improved interfaces still produce low solve rates on full SWE-bench and remain fragile around editing recovery, cost, and wasted steps.

## Key Findings

- With GPT-4 Turbo, the system solved 12.47% of 2,294 SWE-bench tasks, versus a prior reported 3.8% resolve rate from a non-interactive retrieval-augmented baseline.
- On SWE-bench Lite with the same base model, the tailored interface scored 18.00%, compared with 11.00% for a shell-only agent and 2.67% for a retrieval-augmented setup.
- The paper’s mechanism claim is not just rhetorical: the interface narrows action choices, caps search output to 50 results, limits file views to 100 lines at a time, and routes edits through lint-checked replacement with immediate feedback on invalid syntax.
- Internal ablations show some support for those design choices: summarized search reached 18.0% on SWE-bench Lite versus 12.0% for iterative search and 15.7% for no-search; editing with linting reached 18.0% versus 15.0% without linting and 10.3% with no editing.
- The gains are sharply bounded by editing instability. In GPT-4 Turbo runs, 1,185 of 2,294 trajectories, or 51.7%, had at least one failed edit.
- Once editing goes wrong, outcomes deteriorate fast: the probability of eventual success fell from 90.5% for runs with any edit attempt to 57.2% after one failed edit.
- Successful runs were also shorter and cheaper, with a median cost of $1.21 over 12 steps, while unsuccessful runs averaged $2.52 and 21 steps, indicating that failure consumes more trajectory budget rather than simply ending early.
- The interface appears portable across models, not uniquely tied to one vendor stack: with Claude 3 Opus, the same setup reached 10.46% on full SWE-bench and 13.00% on SWE-bench Lite.

## Evidence and Findings

- The strongest headline result is a benchmark jump on full SWE-bench: 12.47% solved out of 2,294 tasks with GPT-4 Turbo versus a cited 3.8% prior non-interactive baseline. That supports the conclusion that interactive agent-computer interfaces can materially outperform retrieval-only assistance on repository repair tasks, which matters because it reframes software-agent progress as an environment design problem rather than pure next-token capability.
- The Lite-split comparison is even cleaner for interface choice: 18.00% for the tailored setup, 11.00% for shell-only, and 2.67% for retrieval augmentation under the same model. That supports the claim that a default shell is not an adequate neutral substrate for agentic software work; interface design itself is part of the capability stack.
- The mechanism is only partially isolated, but the paper does provide operational evidence rather than just narrative. Search is structured through dedicated commands, output is capped at 50 results to avoid overload, file inspection is bounded to 100-line windows, and editing is line-ranged with immediate post-edit display. This supports a bounded conclusion that constrained observability and action formatting help the model stay on-task in large codebases.
- Ablations give the mechanism more weight but not full causal closure. Summarized search at 18.0% beats iterative search at 12.0% and no-search at 15.7%, suggesting that concise search feedback is useful while some search designs can actually underperform a simpler baseline. That matters because it shows interface quality, not merely interface presence, is what changes outcomes.
- Editing guardrails show a similar pattern. Lint-checked editing scores 18.0%, versus 15.0% without linting and 10.3% with no editing, supporting the conclusion that validation feedback helps convert model intent into executable repository changes. But the same system still records failed edits in 51.7% of trajectories, so the guardrail is helpful without being sufficient.
- Cost and step data sharpen the practical takeaway. Successful runs ended after a median of 12 steps and cost $1.21, while unsuccessful runs averaged 21 steps and $2.52. The supported conclusion is that failure is not just lower quality; it is also economically wasteful, which matters for any deployment case where repeated repair attempts compound cost.

## Contradictions and Tensions

- The paper argues that the tailored interface improves software-agent performance, and the benchmarks support that, but the absolute solve rate on full SWE-bench is still only 12.47%. The system is better than the cited baseline without being broadly reliable.
- Search helps, but not every search design helps equally. Summarized search outperforms iterative search, while no-search at 15.7% still beats iterative search at 12.0%. The tension is that adding more interaction is not automatically beneficial; badly structured interaction can be worse than less interaction.
- Lint-guarded editing improves benchmark scores, yet editing remains one of the main failure channels. More than half of GPT-4 Turbo trajectories saw at least one failed edit, and success probability dropped sharply after a failed edit. The same subsystem that enables progress is also a frequent point of collapse.
- The interface transfers to Claude 3 Opus, which supports portability, but the reported scores remain lower than the GPT-4 Turbo configuration on both full and Lite splits. That creates a bounded portability claim rather than a model-agnostic capability claim.
- Successful runs are cheaper and shorter than failed ones, which is good news for viable trajectories, but it also means the system burns more money and steps when it is off-course. Performance gains therefore come with a deployment tension: modest solve-rate improvements do not remove the operational cost of failure.

## Mechanism or Bounds

The strongest supported mechanism is that language-model-tailored interfaces reduce operating overload and prevent some invalid actions by constraining what the agent sees and how it acts. Dedicated search commands, capped result sets, bounded file views, structured line-range editing, and lint-mediated rejection of invalid edits collectively appear to make repository navigation and modification more tractable than a raw shell.

That mechanism is supported, but only in a bounded way. The paper provides benchmark comparisons and ablations, not a definitive isolation of every component’s causal contribution. The evidence supports “interface structure helps” more strongly than “this exact component is the decisive driver.” The data also show that the mechanism is incomplete: even with these guardrails, failed edits are common and strongly associated with lower success, so the interface improves the operating regime without solving trajectory fragility.

## Limits

The evidence is benchmark-bound and should not be read as proof of general autonomous software engineering competence.
The main full-benchmark result remains low in absolute terms at 12.47%, so the system is meaningfully better than prior reported baselines while still failing on most tasks.
The causal story is partial rather than closed; ablations support the value of interface design, but they do not fully isolate which components matter most or under what repository conditions.
Editing instability remains a major unresolved bottleneck, and the paper does not show that editing failure is the only or final cause of unsuccessful runs.
Cross-model transfer is encouraging but limited; portability does not erase performance differences across model backends.
Operationally, unsuccessful runs are longer and more expensive, so deployment value depends not only on peak success but on controlling failure trajectories.
