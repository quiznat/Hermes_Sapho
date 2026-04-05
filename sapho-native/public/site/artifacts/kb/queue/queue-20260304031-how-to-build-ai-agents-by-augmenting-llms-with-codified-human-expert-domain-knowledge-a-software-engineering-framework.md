<details class="traceability-panel">
<summary>Traceability</summary>
<div class="traceability-body">
<ul>
  <li><strong>Source:</strong> <a href="https://arxiv.org/abs/2601.15153" target="_blank" rel="noopener">https://arxiv.org/abs/2601.15153</a></li>
  <li><strong>Intake queued:</strong> 2026-03-04T03:59:01Z</li>
  <li><strong>Source captured:</strong> 2026-03-30T18:14:24Z</li>
  <li><strong>Curated:</strong> 2026-04-02T23:16:10Z</li>
  <li><strong>Artifact finalized:</strong> 2026-04-02T23:18:14Z</li>
  <li><strong>Artifact published:</strong> 2026-03-30T18:20:02Z</li>
</ul>
</div>
</details>

# How to Build AI Agents by Augmenting LLMs with Codified Human Expert Domain Knowledge? A Software Engineering Framework

## Core Thesis

The paper argues that domain agents improve materially when an LLM is not left to improvise alone, but is coupled to explicit expert knowledge encoded as software, retrieval-backed code generation, and expert-guided design rules. In the reported evaluation, that combined architecture produced substantially higher-rated outputs and more consistent quality than the comparison baseline.

## Why It Matters for Sapho

This matters because it supports a practical doctrine Sapho should take seriously: strong domain performance may come less from asking a general model to “be an expert” and more from decomposing expertise into parts that can be formalized, retrieved, and enforced. It also matters as a warning against easy generalization. The reported gains are real within the tested setting, but the validation remains narrow, simulation-centered, and only partially explanatory about which architectural components actually drove improvement.

## Key Findings

- The proposed agent received a mean output-quality score of 2.60 versus 0.85 for the baseline on a 0-3 scale, which the paper summarizes as a 206% improvement.
- The system architecture combines four distinct pieces: a request classifier, retrieval-augmented code generation, codified expert rules implemented as executable functions, and expert-derived visualization principles supplied through augmentation.
- The proposed system was not just better on average; it was more stable. Human-evaluation standard deviations were reported at 0.29-0.58 versus 0.39-1.11 for the baseline.
- In all five evaluated cases, the proposed system reached expert-level modal ratings of 3, while the baseline received a modal rating of 0 in 4 of 5 scenarios.
- The empirical validation covered five scenarios and 12 evaluators, and the paper explicitly states that testing did not establish effectiveness outside simulation-based optimization contexts.

## Evidence and Findings

- The paper reports a direct quality jump from 0.85 to 2.60 on a 0-3 scale. That supports the conclusion that the combined expert-augmented architecture can outperform the baseline meaningfully in the tested tasks, and it matters because the gain is large enough to suggest more than marginal prompt tuning.
- The architecture does not rely on a single enhancement. It routes requests, uses retrieval for code generation, operationalizes expert rules as Python functions, and applies expert visualization principles through augmentation. That supports the conclusion that domain performance was pursued through structured division of labor rather than pure free-form generation, which matters for anyone building agents in constrained technical environments.
- The consistency signal is unusually important here. The proposed system achieved mode 3 in all evaluated cases, while the baseline had mode 0 in 4 of 5 scenarios, and reported score dispersion was also lower. That supports the conclusion that the system improved reliability as well as mean quality, which matters because operational users often care more about avoiding bad outputs than about occasional peak performance.
- The paper gives concrete examples of how expert knowledge was translated into enforceable behavior, including plot rules such as dashed lines for non-converged variables, solid lines for converged variables, and limiting displays to no more than two variables, objectives, or responses. That supports the conclusion that at least part of the gain may come from codifying narrow but high-value expert judgment into reproducible constraints, which matters because it shows a path from tacit craft knowledge to system behavior.
- Knowledge extraction was lightweight rather than industrial: two experts were interviewed for roughly 60-90 minutes each, with recordings transcribed and turned into rules and guidance. That supports the conclusion that useful expert augmentation may be feasible without massive annotation programs, which matters for organizations where expertise is scarce and concentrated.
- The evaluation boundary is explicit: five scenarios, 12 evaluators, and a practical-effectiveness setup involving one non-expert mechanical engineer with one year of simulation experience, a 30-minute orientation, and no visualization training, while a visualization expert with 20 years of experience judged the outputs. That supports the conclusion that the findings are promising but tightly scoped, which matters because the paper does not establish broad cross-domain agent effectiveness.

## Contradictions and Tensions

- The strongest tension is between the size of the reported performance gain and the narrowness of the validation. A 206% improvement and universal expert-level modal ratings are striking, but they come from only five scenarios in simulation-based optimization settings.
- The baseline comparison is not a pure test of “LLM alone versus expert augmentation.” The paper notes that standalone LLMs produced matplotlib and seaborn solutions incompatible with the target Simulation Analysis software environment, so the benchmark became LLM+RAG rather than a raw standalone model. That makes the comparison more realistic for the environment, but less clean as a claim about the independent value of each added module.
- The architecture is described as a composite system, yet the evidence does not isolate module-level contribution. The paper shows that the full stack works better than the baseline, but not how much of the gain came from codified rules, retrieval, routing, or visualization principles individually.
- The practical-effectiveness setup highlights usability ambition, but also fragility in inference. One non-expert user can show that the workflow is plausible, not that it is robust across users, organizations, or adjacent domains.

## Mechanism or Bounds

The strongest supported mechanism is structured expertise decomposition. Explicit procedural knowledge is converted into executable code, while less formal design judgment is carried through LLM augmentation and expert-authored principles. This division appears to reduce the burden on the model to infer all domain norms implicitly and likely explains at least part of the improvement in both output quality and variance.

The bounds are equally important. The paper supports this mechanism inside simulation-based optimization workflows, where software constraints, domain conventions, and visualization norms are specific enough to codify. It does not establish that the same approach will transfer cleanly to domains where expertise is less procedural, less stable, or harder to formalize.

## Limits

The evidence does not identify which architectural component produced how much of the measured gain.
The evaluation is small: five scenarios and 12 evaluators.
External validity is openly limited to simulation-based optimization contexts.
The practical-effectiveness test centers on one non-expert user, which is too narrow to establish general usability.
The comparison baseline was shaped by environment-compatibility problems in standalone LLM outputs, so the findings should be read as evidence for a particular engineered stack in a particular setting, not as a universal recipe for domain agents.
