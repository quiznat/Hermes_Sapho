<details class="traceability-panel">
<summary>Traceability</summary>
<div class="traceability-body">
<ul>
  <li><strong>Source:</strong> <a href="https://arxiv.org/html/2511.00872v1" target="_blank" rel="noopener">https://arxiv.org/html/2511.00872v1</a></li>
  <li><strong>Intake queued:</strong> 2026-03-11T07:31:08Z</li>
  <li><strong>Source captured:</strong> 2026-04-11T13:18:35Z</li>
  <li><strong>Curated:</strong> 2026-04-11T13:18:55Z</li>
  <li><strong>Artifact finalized:</strong> 2026-04-11T13:21:36Z</li>
  <li><strong>Artifact published:</strong> 2026-04-11T13:37:43Z</li>
</ul>
</div>
</details>

# Agent frameworks do not yield a stable winner across code-centric software engineering tasks

## Core Thesis

This evaluation shows that agent-framework performance in code-centric software engineering is task-dependent rather than unified under a single best system. Across software development, vulnerability detection, and program repair, the leading result shifts by task: OpenHands leads software-development quality at 0.47, GPTswarm leads vulnerability detection with 80 of 115 cases, and SE-Agent (Iter-3) leads program repair with 161 of 300 issues fixed. The evidence supports cross-task comparison under common conditions, but not a causal account of why leadership changes.

## Why It Matters for Sapho

Sapho should treat “best agent framework” claims in software engineering as benchmark-bounded unless they survive cross-task comparison. This paper pushes against framework-level winner narratives and instead supports a more operational doctrine: evaluate systems by task profile, inspect where metric leadership splits, and keep category-specific failure modes visible. It also matters because some apparent efficiency or capability signals break under closer inspection: low cost does not equal broad competence, strong aggregate detection does not remove class-specific blind spots, and repair success appears materially constrained by whether a framework can actually produce correct patch artifacts.

## Key Findings

- No framework leads all three evaluated tasks under the study’s common setup of seven agent frameworks, a 100-step cap, and the same backend model, DeepSeek-v3.1.
- In software development, OpenHands posts the top overall quality score at 0.47, but the best submetrics split across systems: AgentOrchestra leads completeness at 0.86, OpenHands leads executability at 1.00, and GPTswarm leads consistency at 0.85.
- In vulnerability detection, GPTswarm records the strongest overall result at 80 of 115 detections, reported as 78%, but Gas Limitation vulnerabilities remain rarely detected across the evaluated agents.
- In program repair, SE-Agent (Iter-3) leads with 161 of 300 repaired issues, reported as 54%, while frameworks reported as lacking patch tooling and correct diff-format patch generation perform poorly.
- Repair competence remains sharply bounded: no evaluated agent fixes any of the 3 Flask issues in SWE-bench Lite, despite Flask’s small issue count.
- Cost and usage do not map cleanly onto outcome: AgentOrchestra has the highest total reported cost at $370.19, GPTswarm the lowest at $16.29, and OpenHands uses the most tokens without becoming the most expensive because cached input tokens are cheaper.

## Evidence and Findings

- The study compares seven general-purpose agent frameworks across three distinct benchmarks: SRDD for 1,200 software-development prompts, LLM-SmartAudit for 115 vulnerability instances, and SWE-bench Lite for 300 program-repair instances. That breadth matters because the central result is not a single benchmark win but the instability of leadership across materially different software-engineering tasks.
- OpenHands reaches the highest software-development quality score at 0.47, where quality is defined as Completeness × Executability × Consistency. This supports the conclusion that it is the strongest overall system on that benchmark, but only in the aggregate sense, because the underlying submetrics are not dominated by one framework.
- The submetric split is decisive rather than cosmetic: AgentOrchestra leads completeness at 0.86, OpenHands leads executability at 1.00, and GPTswarm leads consistency at 0.85. That supports the stronger conclusion that software-development performance is multi-dimensional and that overall leadership can mask meaningful specialization.
- GPTswarm delivers the highest reported vulnerability-detection result at 80 of 115 cases, listed as 78% in the main table. This supports a real benchmark advantage in overall detection, but not a general claim of robust vulnerability coverage, because Gas Limitation cases remain rarely detected across agents.
- SE-Agent (Iter-3) reaches 161 of 300 repairs, the best result in program repair, and the paper ties weak repair performance for AgentOrchestra, OWL, and GPTswarm to absent patch tooling and failure to generate correct diff-format patches. This supports a bounded operational mechanism: repair performance depends materially on whether a framework can produce the artifact form the benchmark actually requires.
- The cost results sharpen the practical interpretation rather than overturn it. AgentOrchestra incurs the highest total cost at $370.19 while GPTswarm comes in lowest at $16.29, and OpenHands consumes the most tokens without the highest cost because cached input tokens are cheaper. That matters because raw token volume, dollar cost, and benchmark success do not collapse into one simple efficiency ranking.

## Contradictions and Tensions

- The paper cuts directly against the idea of a universal framework winner: the top result moves from OpenHands in software development to GPTswarm in vulnerability detection to SE-Agent (Iter-3) in program repair.
- Even within software development, “best” depends on what is being optimized. OpenHands leads overall quality and executability, but AgentOrchestra leads completeness and GPTswarm leads consistency, so aggregate victory hides a split capability profile.
- GPTswarm is simultaneously the strongest overall vulnerability detector and part of a field that still rarely detects Gas Limitation vulnerabilities. The top detector therefore does not remove a category-level weakness.
- Program repair shows a similar tension: SE-Agent (Iter-3) leads the benchmark overall, yet no evaluated agent repairs any of the 3 Flask issues. The leading system is therefore still bounded by a complete failure on at least one repository slice.
- Efficiency and capability do not align cleanly. GPTswarm is the lowest-cost framework at $16.29 and still leads vulnerability detection, but it is also among the frameworks reported to perform poorly in repair because of patch-generation constraints. Low cost can coexist with sharp task-specific weakness.
- OpenHands consumes the most tokens across tasks without becoming the most expensive because cached input tokens are cheaper. That means resource usage signals can mislead if interpreted without the pricing structure attached.

## Mechanism or Bounds

The strongest supported mechanism appears in program repair: frameworks that do not use patch tooling and fail to generate correct diff-format patches perform poorly, which indicates that artifact-generation capability is a material constraint on repair success. Outside repair, the evidence is more comparative than causal. The software-development results show that overall quality and component submetrics separate across frameworks, but they do not establish why completeness, executability, and consistency split the way they do. The vulnerability findings likewise support a bounded performance claim rather than a causal explanation: strong overall detection does not reliably extend to Gas Limitation cases. More broadly, all conclusions are benchmark-bound to SRDD, LLM-SmartAudit, and SWE-bench Lite under a shared backend model, DeepSeek-v3.1, with a 100-step limit.

## Limits

The paper supports cross-task comparison, not a general theory of agent effectiveness in software engineering.
The causal basis for why framework leadership changes by task is not established.
Some reported outcomes are benchmark-specific and may not transfer outside SRDD, LLM-SmartAudit, or SWE-bench Lite.
The vulnerability section contains a minor reporting wrinkle, with some summary text mentioning 77% while the main table reports 80 of 115, or 78%; the table value is the firmer quantitative anchor.
The repair mechanism is meaningful but partial: lack of patch tooling explains an important failure mode, not all observed failures.
The universal failure on the three Flask issues shows that even the strongest repair result leaves unresolved blind spots that the aggregate score can hide.
