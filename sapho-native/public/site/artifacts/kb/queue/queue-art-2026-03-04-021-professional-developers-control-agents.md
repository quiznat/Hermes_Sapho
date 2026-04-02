# Queue Artifact — art-2026-03-04-021

Source URL: https://arxiv.org/abs/2512.14012  
Canonical URL: https://arxiv.org/abs/2512.14012  
Lane: agent-research  
Decision: retain

## Thesis

Experienced software developers do not use coding agents as unsupervised “vibe coding” engines; they use them as controlled productivity multipliers under explicit human oversight and quality discipline.

## Mechanism summary

This mixed-methods study (field observations + survey with experienced developers) finds that practitioners keep strong control over planning, verification, and design decisions while delegating bounded implementation work to agents. Reported fit is highest for well-scoped, clearly specified tasks; reliability drops on complex ambiguous tasks. The governing mechanism is expert process control: developers impose validation loops and software-quality constraints to offset agent limitations.

## Confidence

High for directional behavior findings from practitioner evidence; medium for broad generalization beyond the sampled populations.

<!-- canonical-empirical-findings -->

## Empirical Findings (Data Snapshot)

| Novel finding | Quantitative result | Experimental setup/sample | Metric/outcome | Caveat/limit |
|---|---|---|---|---|
| Experienced developers use coding agents as supervised copilots, not autonomous substitutes. | Study sample includes field observations **N=13** and qualitative survey responses **N=99** experienced developers. | Mixed-methods practitioner study on real agent use in professional software development workflows. | Reported adoption sentiment is overall positive, with persistent human control over design/quality decisions and strategy-level delegation. | `qualitative_only` for outcome deltas in this pass: abstract provides sample sizes and directional findings but not task-success/time % effect sizes. |

## Why it matters for Sapho

Strong support for Sapho’s fail-closed doctrine: maximize value via controlled delegation, explicit verification gates, and human authority over architecture/quality decisions.
