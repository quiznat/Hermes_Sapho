<details class="traceability-panel">
<summary>Traceability</summary>
<div class="traceability-body">
<ul>
  <li><strong>Source:</strong> <a href="https://www.anthropic.com/research/labor-market-impacts" target="_blank" rel="noopener">https://www.anthropic.com/research/labor-market-impacts</a></li>
  <li><strong>Intake queued:</strong> 2026-04-12T12:03:06Z</li>
  <li><strong>Source captured:</strong> 2026-04-12T12:25:37Z</li>
  <li><strong>Curated:</strong> 2026-04-12T12:26:03Z</li>
  <li><strong>Artifact finalized:</strong> 2026-04-12T12:28:28Z</li>
</ul>
</div>
</details>

# Labor market impacts of AI: A new measure and early evidence

## Core Thesis

This paper argues that labor-market analysis improves when AI exposure is measured through realized, work-related model use rather than theoretical capability alone. Its central move is to build an "observed exposure" metric that counts tasks as exposed when they are both LLM-feasible in theory and actually present in Claude usage, with heavier weight on automation than augmentation. On that basis, the paper finds a sharper link between AI exposure and weaker projected employment growth than theory-only measures show, while also showing that near-term realized labor-market damage remains limited and uneven.

## Why It Matters for Sapho

Sapho should treat capability maps and real deployment maps as different objects. This paper shows that theory-only exposure can materially overstate where labor pressure is already arriving, even inside highly exposed fields, and that observed usage can carry more decision value than broad capability claims when judging labor displacement risk. It also matters methodologically: the strongest current signal is not "AI is already broadly collapsing jobs," but "real-world adoption is concentrated, measurable, and more predictive than abstract feasibility, with early adverse signals showing up more clearly at the margin and among younger entrants."

## Key Findings

- The paper constructs an observed-exposure measure by intersecting theoretical task feasibility with real-world work-related Claude usage, weighting full automation more heavily than augmentation, and aggregating to occupations by task time share.
- Observed Claude usage is heavily concentrated in tasks prior theory already marked as LLM-feasible: 97% of observed tasks from prior Economic Index reports fall into feasibility categories rated 0.5 or 1.0, and fully automatable tasks alone account for 68% of observed usage.
- The fit between theory and practice is strong but not clean: tasks rated infeasible still account for 3% of observed Claude usage, which means theoretical exclusion does not perfectly bound real use.
- In Computer & Math work, theoretical LLM scope reaches 94% of tasks, but current observed Claude coverage is only 33%, indicating a large adoption gap between what models could plausibly do and what workers are actually using them for.
- Exposure is uneven even within highly exposed work: Computer Programmers reach 75% coverage and Data Entry Keyers 67%, while 30% of workers fall into zero coverage because their tasks appear too rarely in the data to clear the paper's minimum threshold.
- At the occupation level, each 10 percentage point increase in observed exposure is associated with a 0.6 percentage point lower projected employment growth rate from 2024 to 2034, while the theoretical exposure measure alone shows no correlation with projected growth.
- Realized near-term labor effects remain weak at the aggregate level: since ChatGPT's release, the unemployment-gap change between top-exposure workers and unexposed workers is small and statistically insignificant overall.
- The sharper near-term concern appears among younger workers: for ages 22 to 25, the estimated job-finding rate into exposed occupations falls 14% relative to 2022, but the paper describes that result as only barely statistically significant.

## Evidence and Findings

- The paper's main contribution is a measurement design, not a labor-market causal proof: it marks tasks as exposed only when theoretical feasibility and sufficient work-related Claude usage coincide, weights automation more than augmentation, and rolls exposure up by task time share. That supports a more grounded exposure metric, but it does not by itself validate the metric against external labor outcomes.
- The usage distribution strongly supports the claim that real work adoption is landing where prior LLM theory said it should land. Ninety-seven percent of observed tasks fall into categories previously rated feasible, and tasks in the fully automatable category account for 68% of observed Claude usage. This matters because it suggests current use is not random experimentation spread evenly across occupations; it is clustering in the task bands where language models were already expected to matter most.
- The same evidence also blocks an overly clean theory-to-practice story. Tasks rated infeasible still represent 3% of observed usage, which implies either task mapping noise, capability drift, or real-world use cases that theory did not cleanly capture. That matters because it weakens any doctrine that treats capability taxonomies as exact operational boundaries.
- The computer-work results show the difference between latent scope and realized penetration. Theoretical feasibility covers 94% of Computer & Math tasks, but observed Claude coverage is only 33% for the category. Even the most exposed occupations are partial rather than saturated, with Computer Programmers at 75% and Data Entry Keyers at 67%. This supports the conclusion that adoption remains materially incomplete even where the technical fit is strongest.
- The labor-market association is specific to observed exposure. A 10-point increase in observed exposure is associated with 0.6 points lower BLS projected employment growth over 2024-2034, while the theoretical exposure measure alone has no correlation with projected growth. That matters because it suggests realized deployment may be a better leading indicator of labor pressure than capability-only estimates.
- The realized post-ChatGPT signal is still narrow and tentative. Aggregate unemployment-gap differences between highly exposed and unexposed workers are small and statistically insignificant, while the clearest adverse result is a 14% decline in job-finding into exposed occupations for workers aged 22 to 25, described as barely statistically significant and vulnerable to alternative interpretation. This supports caution: there is an early warning signal, but not a settled short-run displacement verdict.

## Contradictions and Tensions

- The paper's strongest methodological tension is that theory explains most observed use but not all of it. If 97% of observed tasks sit inside theoretically feasible categories, the alignment is strong; if 3% still sit in infeasible categories, the alignment is not exact enough to treat theory as a hard boundary.
- The computer-work results show a sharp gap between what models appear able to do and what workers actually use them for: 94% theoretical scope versus 33% observed coverage in Computer & Math. That cuts against any easy reading that technical feasibility automatically becomes broad labor exposure.
- The labor-market story is mixed rather than linear. Observed exposure is associated with weaker projected employment growth, but post-ChatGPT realized unemployment differences are small and statistically insignificant overall. The forward-looking signal is negative; the near-term realized signal is muted.
- The strongest adverse near-term effect appears among younger workers entering exposed occupations, not across the whole labor market. That creates an age- and transition-specific warning rather than a broad confirmed displacement pattern.
- The paper also contains a data-pipeline tension: 30% of workers receive zero coverage because their tasks appear too rarely to pass the observation threshold. Zero exposure here can therefore mean insufficient observed frequency, not necessarily true insulation from AI.

## Mechanism or Bounds

The supported mechanism is a bounded measurement story: labor pressure appears more legible when exposure is tied to actual work-related model use rather than to theoretical capability alone. The paper does not establish that observed exposure causes lower employment growth; it shows that realized usage is more closely associated with projected weakness than abstract feasibility is. Operationally, this implies a two-stage path: many tasks may be technically within LLM scope, but labor relevance depends on uneven adoption, uneven workflow integration, and the share of task time actually touched by model use. The evidence is therefore strongest as a bound on current penetration and a guide to where labor effects may emerge first, not as a full causal account of displacement.

## Limits

- The exposure metric is source-constructed and not externally validated here as a definitive measure of occupational AI penetration.
- The labor-market findings are associational. The projected-growth result does not prove AI is the cause of lower employment growth.
- Near-term realized effects are limited in the aggregate, with the unemployment-gap result statistically indistinguishable from zero.
- The youth job-finding result is only barely statistically significant and is presented by the paper itself as suggestive rather than conclusive.
- Zero-coverage classifications partly reflect minimum observation thresholds, so absence of measured exposure can reflect sparse data rather than genuine absence of AI-relevant tasks.
- The paper shows concentration and partial adoption, but it does not fully explain why some theoretically exposed tasks or occupations convert into real use faster than others.
