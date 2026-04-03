---
version: article.v1
article_id: art-2026-03-04-024
ticket_id: ticket-import-art-2026-03-04-024
source_url: https://arxiv.org/abs/2510.10460
source_title: Testing and Enhancing Multi-Agent Systems for Robust Code Generation
queued_at_utc: '2026-03-04T03:59:01Z'
captured_at_utc: '2026-03-30T17:59:36Z'
canonical_url: https://arxiv.org/abs/2510.10460
curator_decision: kept
artifact_minted_at_utc: '2026-04-02T13:36:26Z'
evidence_count: 14
claim_count: 4
publication_status: ready-for-daily
imported_from_runtime_article_id: art-2026-03-04-024
imported_from_runtime_last_stage: intake
imported_from_runtime_filter_state: pending
curator_reason: This preprint reports concrete robustness experiments and repair evaluations
  for multi-agent code generation systems.
curated_at_utc: '2026-04-02T13:33:47Z'
curator_mode: agent
extracted_at_utc: '2026-04-02T13:36:26Z'
extractor_mode: agent
findings_mode: agent
summary_mode: agent
artifact_publication_status: published
artifact_publication_minted_at_utc: '2026-03-30T18:03:06Z'
artifact_publication_published_at_utc: '2026-03-30T18:03:07Z'
artifact_publication_alias: '20260304024'
source_remediation_status: completed
source_remediated_at_utc: '2026-03-30T17:59:36Z'
---
# Testing and Enhancing Multi-Agent Systems for Robust Code Generation

## Core Thesis

Current code-generation multi-agent systems are materially less robust than headline solve rates suggest: when prompts are rewritten in meaning-preserving ways, systems that had already solved a problem newly fail on 7.9% to 83.3% of those same problems. The paper’s main practical finding is that many of these breakdowns arise not from the planner producing obviously wrong logic, but from the handoff between planning and coding, and that a repair loop built around prompt diversification plus a monitor agent can recover a meaningful share of those failures without making the systems generally reliable.

## Why It Matters for Sapho

This matters because Sapho should not treat multi-agent code performance as a simple capability number. The paper shows that surface-stable task meaning is not enough to preserve behavior: small semantic-preserving changes in wording can trigger large failure swings, which means benchmark wins can mask brittle execution paths. It also sharpens evaluation doctrine. If the dominant break is the planner-coder handoff rather than pure planning incompetence, then audit, monitoring, and adversarial robustness checks belong upstream of any confidence claims about autonomous coding systems. Just as important, the proposed fix is useful but bounded, which argues against treating repair loops as a blanket reliability solution.

## Key Findings

- Across three multi-agent systems, three backend language models, and four datasets, semantic-preserving prompt mutations caused systems to lose previously achieved solves on 7.9% to 83.3% of problems.
- The evaluation used four mutation operators — Rephrase, Insert, Expand, and Condense — and measured robustness with Pass@10 over 10 runs per question, reducing the chance that the result is just single-run noise.
- The worst reported robustness drop was 83.3% for MetaGPT with Deepseek on CodeContest; the best reported case still lost 7.9% for PairCoder with GPT-4o on MBPP ET.
- In a manual analysis of a random 20% sample from more than 700 failures, planner-coder gap made up 75.3% of failures, versus 15.3% for plan logic errors and 9.3% for invalid cases.
- That failure analysis reported Cohen’s kappa = 0.88, which supports the reliability of the taxonomy even though the analysis is still sample-bounded.
- The proposed repair method — multi-prompt generation plus a monitor agent for plan interpretation and code checking — solved 40.0% to 88.9% of fuzzing-identified failures across evaluated settings.
- In one reported slice, the repair was highly selective rather than general: for SCCG with GPT-3.5 it fixed 83.9% of planner-coder-gap failures but 0.0% of invalid cases.
- After repair, re-running fuzzing reduced failure counts by as much as 85.7%, showing real robustness gains without showing that the underlying brittleness disappears.

## Evidence and Findings

- The paper stress-tests code-generation multi-agent systems with four semantic-preserving prompt mutations and finds that systems often break on tasks they had already solved, with post-fuzzing failure rates spanning 7.9% to 83.3%. This supports the conclusion that apparent coding competence is highly sensitive to prompt form, not just task meaning, which matters because benchmark pass rates alone understate operational fragility.
- The robustness result is not built on a narrow setup: the study spans three agent systems, three backend models, and four datasets, and evaluates with Pass@10 over 10 runs per question. This supports reading the brittleness finding as cross-configuration rather than anecdotal, which matters because it raises questions about the general reliability of current multi-agent coding stacks rather than a single implementation bug.
- The paper’s failure analysis finds that planner-coder gap dominates observed breakdowns at 75.3%, far above plan logic errors at 15.3% and invalid cases at 9.3%, based on a random 20% sample of more than 700 failures with Cohen’s kappa = 0.88. This supports the conclusion that the main weakness is frequently in execution transfer from plan to code rather than in first-order reasoning alone, which matters because it redirects intervention effort toward handoff fidelity and interpretation control.
- The authors’ explanation for that dominant failure mode is concrete: plans are often logically correct but too brief or abstract, while coders misread expressions or fail on complex logic without sufficient detail. This supports a bounded operational account in which the system’s decomposition layer produces under-specified guidance that downstream coding cannot reliably operationalize, which matters because it identifies a tractable reliability target even without full causal proof.
- The repair method combines multi-prompt generation with a monitor agent that interprets plans and checks code, and it solves 40.0% to 88.9% of fuzzing-identified failures across tested settings. This supports the conclusion that targeted monitoring and prompt diversity can recover a substantial share of robustness losses, which matters because it shows that some brittleness is remediable rather than purely intrinsic.
- The repair is sharply uneven by failure type: in the reported SCCG with GPT-3.5 setting, it fixes 83.9% of planner-coder-gap failures but 0.0% of invalid cases, and overall post-repair failure counts fall by up to 85.7%. This supports the conclusion that the intervention is effective mainly where the failure pathway matches plan interpretation and checking, which matters because it rules out reading the method as a general-purpose cure for multi-agent coding errors.

## Contradictions and Tensions

- The headline robustness result is strong, but it is also highly heterogeneous. A system can lose only 7.9% of prior solves in one setting and 83.3% in another, so “multi-agent systems are brittle” is true but too coarse unless paired with the fact that brittleness is configuration-sensitive.
- The systems are described as failing under semantic-preserving mutations, yet the mutation operators change prompt expression style in ways that may differentially burden planning, parsing, or execution handoff. That creates an important interpretation tension: the paper shows instability under meaning-preserving rewrites, but it does not prove that every failure reflects the same underlying weakness.
- The dominant failure mode is planner-coder gap, not plan logic error, which cuts against the easy story that better planning alone is the main route to robustness. The tension is that agent architectures often emphasize decomposition as a strength, while the evidence suggests the decomposition boundary itself is a major liability.
- The repair results are substantial, but their success range of 40.0% to 88.9% is wide, and the method appears much stronger on planner-coder-gap failures than on invalid cases. The practical tension is that a method can look highly effective in aggregate while remaining structurally narrow in what it actually fixes.
- The paper offers a mechanism for planner-coder gap, but that mechanism comes from sampled manual analysis rather than a controlled causal intervention. This creates a useful but unresolved tension between a plausible operational explanation and stronger causal claims that the evidence does not fully warrant.

## Mechanism or Bounds

The strongest supported mechanism is a bounded handoff failure. The planner often produces logic that is directionally correct but too compressed or abstract for reliable execution, and the coder then misinterprets expressions or mishandles complex logic because the plan does not carry enough operational detail. The repair method aligns with that pathway: multi-prompt generation broadens candidate trajectories, while the monitor agent interprets the plan and checks the code, helping close failures that originate in plan-to-code translation.

The bounds are important. This is not a full causal decomposition of all failure sources; the failure taxonomy comes from a random 20% sample of more than 700 failures, not the entire population, even though the reported inter-rater agreement is strong. The intervention evidence more directly supports effectiveness across tested settings than the independent causal contribution of each component. And because the method performs far better on planner-coder-gap failures than on invalid cases, the mechanism should be read as pathway-specific rather than general.

## Limits

The paper establishes robustness loss under the tested mutation and evaluation setup, but it does not show that the same failure rates will hold across all agent frameworks, all model families, or all real-world coding workflows.
The failure mechanism is inferred from sampled manual analysis rather than isolated by controlled experiment, so the causal story is plausible and useful but not fully proven.
The repair method is clearly bounded: its gains vary materially by setting, and the reported subtype result shows near-total failure on invalid cases even where planner-coder-gap recovery is strong.
Because the study uses semantic-preserving rewrites as the perturbation model, it demonstrates sensitivity to wording-preserving variation, but not robustness to every other form of task shift or environmental complexity.
The paper improves the evaluation of multi-agent coding reliability, but it does not eliminate the underlying risk that strong average performance can coexist with brittle, hard-to-predict failure surfaces.
