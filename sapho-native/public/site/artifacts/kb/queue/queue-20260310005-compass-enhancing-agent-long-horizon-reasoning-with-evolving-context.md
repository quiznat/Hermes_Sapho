<details class="traceability-panel">
<summary>Traceability</summary>
<div class="traceability-body">
<ul>
  <li><strong>Source:</strong> <a href="https://arxiv.org/pdf/2510.08790" target="_blank" rel="noopener">https://arxiv.org/pdf/2510.08790</a></li>
  <li><strong>Intake queued:</strong> 2026-03-10T04:03:59Z</li>
  <li><strong>Source captured:</strong> 2026-03-10T06:02:42Z</li>
  <li><strong>Curated:</strong> 2026-04-09T11:54:11Z</li>
  <li><strong>Artifact finalized:</strong> 2026-04-09T11:56:42Z</li>
  <li><strong>Artifact published:</strong> 2026-04-09T12:05:36Z</li>
</ul>
</div>
</details>

# COMPASS: Enhancing Agent Long-Horizon Reasoning with Evolving Context

## Core Thesis

COMPASS argues that long-horizon agent failure is not mainly a problem of raw model intelligence but of context control: as tasks stretch across many interdependent steps, the active working state expands until relevant information no longer fits cleanly inside the model window. Its answer is to separate execution, strategic oversight, and context rebuilding into distinct roles, then refresh the agent context continuously rather than letting the trajectory accumulate unchecked.

## Why It Matters for Sapho

This matters because it shifts evaluation away from the easy story that better agents simply require bigger base models or more agent replicas. The paper presents bounded evidence that context architecture itself can materially change long-horizon performance and efficiency. For Sapho, that strengthens a doctrine that mechanism visibility matters: if an agent succeeds, we should ask how it preserves task-relevant state, how it decides when to reflect or terminate, and where gains come from before treating the result as evidence of general reasoning progress.

## Key Findings

- The paper frames context growth as the central bottleneck in long-horizon tasks, defining those tasks as substantial sequences of interdependent reasoning and action steps, often more than 10, where dynamic execution context grows roughly linearly with time until it exceeds a finite context window.
- COMPASS splits the system into a MainAgent for tactical execution, an asynchronous Meta-Thinker for strategic signals, and a ContextManager that rebuilds refreshed context from persistent notes, the current trajectory, and those signals.
- Across GAIA, BrowseComp, and Humanity's Last Exam, the paper reports up to 20% accuracy improvement over both single-agent and multi-agent baselines in its tested settings.
- With Gemini 2.5 Pro, the reported full-system Pass@1 scores are 35.4 on BrowseComp, 67.8 on GAIA, and 31.7 on Humanity's Last Exam.
- The strongest component-level support for strategic oversight appears on BrowseComp, where removing the Meta-Thinker drops Pass@1 from 35.4 to 15.2.
- The paper also presents bounded scaling and efficiency evidence: in test-time scaling experiments, gains rise from 1 to 8 samples but reportedly plateau around 4, and a smaller Context-12B setup performs comparably to larger models such as Gemini 2.5 Flash on BrowseComp while using 70% of their tokens.

## Evidence and Findings

- The source identifies long-horizon tasks as multi-step, interdependent problems and argues that their working context grows roughly linearly with execution time. That supports the conclusion that context overflow is a structural failure mode rather than a sporadic prompt-quality issue, which matters because it makes memory management a first-class design variable for agent systems.
- COMPASS operationalizes that diagnosis through role separation: the MainAgent keeps acting, the Meta-Thinker monitors asynchronously for anomalies, completion, reflection, and verification needs, and the ContextManager reconstructs the next context window from notes, trajectory, and strategic signal. This supports the conclusion that the system is designed to intervene on context drift without stalling task execution, which matters because it offers a concrete mechanism rather than a vague “more reasoning” claim.
- The reported evaluation spans three named benchmarks with substantial scale in at least two cases: BrowseComp uses 1,266 web-navigation tasks and Humanity's Last Exam uses 2,158 questions after excluding image-based items. On Gemini 2.5 Pro, the system reaches 35.4 Pass@1 on BrowseComp, 67.8 on GAIA, and 31.7 on HLE, supporting the conclusion that the architecture yields meaningful gains across multiple difficult settings rather than a single narrow demo.
- The BrowseComp ablation is especially consequential: removing the Meta-Thinker cuts Pass@1 from 35.4 to 15.2. That supports the conclusion that strategic oversight is not decorative but materially load-bearing in at least one benchmark, which matters because it ties performance to a specific subsystem rather than leaving the gain fully entangled with backbone quality.
- The context-focused scaling evidence is narrower but still decision-relevant. In COMPASS-TTS, accuracy rises monotonically from n=1 to n=8 samples while plateauing around n=4, supporting the conclusion that additional controlled sampling improves outcomes up to a point but does not buy unlimited returns. That matters because it suggests a usable test-time scaling regime with visible diminishing returns.
- The efficiency result around Context-12B is also bounded but notable: the smaller context model reportedly performs comparably to larger models such as Gemini 2.5 Flash on BrowseComp while using 70% of their tokens. That supports the conclusion that specialized context management can narrow capability gaps at lower token cost, which matters because it points to architecture and state control as partial substitutes for brute-force model scale.

## Contradictions and Tensions

- The paper’s strongest direct subsystem evidence is benchmark-specific rather than universal. The large Meta-Thinker ablation effect is shown on BrowseComp, but the provided evidence does not establish an equally explicit component contribution on every benchmark, so the architectural story is stronger there than across the full evaluation suite.
- The paper reports gains across GAIA, BrowseComp, and HLE, but it also limits evaluation to controlled settings with search, text-based browsing, and code execution tools, primarily using proprietary frontier models. That creates a real tension between strong benchmark performance and unclear transfer to messier open-world deployments or open-source model regimes.
- The test-time scaling result is positive but not open-ended: performance improves as samples increase, then plateaus around four. That cuts against any simple interpretation that more sampling will keep compounding linearly.
- The efficiency framing is promising but only partially isolated. A smaller context-focused model using 70% of the tokens of larger models on BrowseComp is important, yet the evidence does not fully separate how much of that gain comes from the context manager itself versus the broader system design and benchmark conditions.

## Mechanism or Bounds

The supported mechanism is architectural separation plus iterative context reconstruction. The MainAgent continues tactical work, the Meta-Thinker watches the run asynchronously and emits reflection, termination, or verification signals, and the ContextManager rebuilds the active context from persistent notes, current trajectory, and strategic guidance. The bounded claim is that this reduces the damage from trajectory sprawl in long-horizon tasks where relevant state would otherwise outgrow the model window. The evidence supports this mechanism most concretely through the BrowseComp ablation and the reported cross-benchmark gains, but the mechanism remains benchmark-bound and tested mainly in environments with search, browsing, and code tools rather than fully open-ended agent settings.

## Limits

The paper’s core diagnosis of context bottlenecks is plausible and operationally useful, but the provided evidence does not fully isolate causality between context management, strategic oversight, model choice, and benchmark-specific tooling.
The strongest architectural support is concentrated in the reported BrowseComp ablation rather than uniformly demonstrated across all evaluated tasks.
The broader “matches Deep Research agents” framing is weaker than the concrete reported scores, token-use result, and test-time scaling curve.
Evaluation is limited to controlled tool-enabled settings and primarily proprietary frontier models, so external validity to open-world use and open-model stacks remains unresolved.
The scaling evidence shows diminishing returns around four samples, which bounds how far test-time compute alone can carry performance.
