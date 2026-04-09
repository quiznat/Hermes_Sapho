<details class="traceability-panel">
<summary>Traceability</summary>
<div class="traceability-body">
<ul>
  <li><strong>Source:</strong> <a href="https://blog.firetiger.com/postmortem-on-the-march-1-2026-ingest-incident/" target="_blank" rel="noopener">https://blog.firetiger.com/postmortem-on-the-march-1-2026-ingest-incident/</a></li>
  <li><strong>Intake queued:</strong> 2026-03-07T15:30:40Z</li>
  <li><strong>Source captured:</strong> 2026-03-07T19:27:22Z</li>
  <li><strong>Curated:</strong> 2026-04-09T04:37:53Z</li>
  <li><strong>Artifact finalized:</strong> 2026-04-09T04:40:29Z</li>
  <li><strong>Artifact published:</strong> 2026-04-09T10:25:36Z</li>
</ul>
</div>
</details>

# Incident postmortem in the age of AI agents

## Core Thesis

Firetiger’s March 1 ingest outage was not a generic cloud failure but a layered control failure: a CI race condition canceled a build, a later deploy treated missing artifacts as complete and pointed Lambda and ECS at a non-existent container image, Terraform then rejected part of the rollout after ECS definitions had already been mutated, and a separate alert-routing problem kept humans out of the loop for roughly eight hours even though automated systems noticed trouble within minutes.

## Why It Matters for Sapho

This matters because it is a clean case where agentic and automated operations did not fail at detection alone; they failed at bounded diagnosis, deployment atomicity, and escalation law. Sapho should treat this as evidence that “automation present” is not the same as “incident control present.” The field risk is not merely bad code generation or bad deploy logic. It is the combination of partial system mutation, machine reasoning that narrows too early, and notification policy states that silently block human intervention. Evaluation doctrine should therefore weight rollback integrity, cross-system consistency, and escalation visibility as first-class controls, not operational afterthoughts.

## Key Findings

- Firetiger’s ingest system for most customers was degraded for about 8 hours on March 1, 2026, and during that window it failed to accept OpenTelemetry data and GitHub webhooks.
- The initiating deployment fault came from a CI race condition on February 27, where aggressive concurrency control wrongly canceled a build during PR merge.
- A later deployment incorrectly believed artifacts were complete and pushed AWS Lambda and ECS definitions referencing a non-existent container ID.
- Terraform rejected the Lambda update as invalid, but only after ECS service definitions had already been changed, creating a split state rather than a clean failure.
- That partial mutation mattered operationally: new ECS tasks could not enter production, and once existing tasks exited they could not be restarted.
- Around 5:48 UTC on March 1, restarted ECS tasks failed to come up and ingest load balancers began returning 503s for all ingest events.
- Firetiger’s self-monitoring detected the incident at 6:00 UTC, 12 minutes after visible failure began, but the initial machine diagnosis narrowed the issue to GitHub webhook ingest rather than the broader ingest outage.
- By 7:47 UTC, internal triage had coalesced the signals and identified the bad ECR version as the root cause, yet normal human incident channels still did not surface the issue because alert visibility was suppressed by internal notification policy state.
- Recovery required locating the broken deployment, rebuilding the image, rerunning deploy scripts, and restoring service health.

## Evidence and Findings

- The postmortem shows a concrete eight-hour customer-facing degradation affecting most customers, with OpenTelemetry ingest and GitHub webhooks failing. That supports a real production outage with broad ingest impact, not an internal-only defect or narrow subsystem blip.
- The source describes a three-issue overlap, beginning with a CI race condition and aggressive concurrency control that erroneously canceled a build during a February 27 PR merge. This supports the conclusion that the outage originated in build-control logic, but also that the incident should not be reduced to a single triggering bug.
- A subsequent deploy falsely treated artifacts as complete and updated Lambda and ECS definitions to a non-existent container ID. That matters because the system crossed from “bad build outcome” into “bad production reference state”: deployment automation promoted configuration that pointed at an image that did not exist.
- Terraform rejected the Lambda change as invalid and aborted, but ECS service definitions had already been mutated. This supports a decisive operational conclusion: the deploy path was not effectively atomic, so rejection did not restore consistency and instead left production in a broken intermediate state.
- The broken ECS definitions prevented replacement tasks from entering production, and around 5:48 UTC restarted tasks failed to come up while ingest load balancers returned 503s for all ingest events. That shows how a latent bad deployment state became a live outage only when task churn forced the system to rely on the invalid definitions.
- Detection was not absent: self-monitoring noticed the issue at 6:00 UTC, and by 7:47 UTC internal triage had identified the bad ECR version. The decisive failure was that alert-routing policy hid notifications from normal incident management channels for about eight hours, so early machine awareness did not convert into timely human response.

## Contradictions and Tensions

- The strongest tension is between fast automated detection and slow human response. The system noticed trouble 12 minutes after visible failure, yet operators were still not notified through normal channels for about eight hours.
- The integration-checking agent was directionally right but operationally narrow: it detected an ingest problem, then initially scoped it to GitHub webhook ingest even though the outage also affected broader ingest paths including OpenTelemetry. This is a misdiagnosis-by-under-scoping problem, not a pure miss.
- The deployment pipeline both failed and succeeded in the wrong places. Terraform rejected the invalid Lambda update, which sounds like a safety catch, but that rejection came after ECS definitions had already been mutated, so the safeguard preserved inconsistency rather than preventing it.
- The incident is described as requiring three overlapping issues, which cuts against any easy narrative that one bug or one bad deploy alone explains the outage. The evidence supports a major causal chain, but it also bounds single-cause interpretations.

## Mechanism or Bounds

The supported mechanism is a layered failure chain. A CI race condition, amplified by aggressive concurrency control, canceled a build during merge. A later deploy then misclassified artifacts as complete and published infrastructure references to a non-existent container image. Terraform rejected the Lambda portion of that rollout, but only after ECS service definitions had already changed, leaving production in a partially mutated state. That state did not immediately collapse everything; instead, it created a latent restart trap where any exiting ECS task could not be replaced. When task restarts occurred around 5:48 UTC on March 1, ingest load balancers began returning 503s. Separately, automated systems detected the issue quickly, but machine diagnosis initially narrowed the problem too much and notification policy state blocked normal human escalation. The bounds matter: this is a postmortem-supported causal path for a specific incident, not a general proof about all agentic systems, and the evidence does not quantify exactly how much each overlapping issue contributed relative to the others.

## Limits

The postmortem supports the main outage chain, but it does not fully apportion causality across the three overlapping issues, so the exact marginal contribution of each failure remains unresolved.
The evidence shows that ECS became unable to restart replacement tasks, but it does not quantify how many task exits or what pattern of churn was required before service failure became effectively total.
The alerting section establishes that machine detection was early and human notification was delayed, but it does not cleanly separate how much delay came from mis-scoped diagnosis versus hidden-notification policy.
The remediation account shows successful use of agent-assisted tooling in recovery, but this source is not comparative evidence that AI-assisted response was faster or better than an alternative human-only path.
