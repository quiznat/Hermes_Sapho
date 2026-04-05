<details class="traceability-panel">
<summary>Traceability</summary>
<div class="traceability-body">
<ul>
  <li><strong>Source:</strong> <a href="https://blog.firetiger.com/postmortem-on-the-march-1-2026-ingest-incident/" target="_blank" rel="noopener">https://blog.firetiger.com/postmortem-on-the-march-1-2026-ingest-incident/</a></li>
  <li><strong>Intake queued:</strong> 2026-03-07T15:30:40Z</li>
  <li><strong>Source captured:</strong> 2026-03-07T19:27:22Z</li>
  <li><strong>Curated:</strong> 2026-04-05T04:15:51Z</li>
  <li><strong>Artifact finalized:</strong> 2026-04-05T04:18:11Z</li>
  <li><strong>Artifact published:</strong> 2026-04-05T13:13:58Z</li>
</ul>
</div>
</details>

# Incident postmortem in the age of AI agents

## Core Thesis

Firetiger’s ingest outage was not a single-point failure but a chained operational failure: a CI race condition and deploy attribution error wrote a non-existent container ID into deployment state, partial deploy behavior left infrastructure inconsistently mutated instead of safely rolled back, invalid ECS task definitions later prevented replacement tasks from starting, and alerting detected the break quickly without reaching humans in time. Recovery was then accelerated by an AI-assisted operator workflow, but the postmortem’s real lesson is that agentic operations increase leverage on both sides of the incident curve: they can speed diagnosis and repair, but they also widen the blast radius of bad state and brittle escalation paths.

## Why It Matters for Sapho

This matters because it sharpens Sapho’s operating doctrine for AI-mediated systems. The relevant question is not whether AI agents “worked,” but where they amplified state mutation, where they failed to produce fail-closed behavior, and where human escalation remained a hard dependency despite nominal machine detection. The source supports a stricter view of evaluation: agentic tooling should be judged not just by remediation speed, but by whether deployment state stays coherent under partial failure, whether alerts cross the machine-to-human boundary reliably, and whether root-cause discovery is paired with controls that prevent invalid state from entering production in the first place.

## Key Findings

- Firetiger’s ingest system for most customers was degraded for about 8 hours on March 1, 2026, failing to accept OpenTelemetry data and GitHub webhooks.
- The initiating failure chain began on February 27, when aggressive CI concurrency handling wrongly canceled a build during a PR merge, and a later deploy job then treated that canceled build as complete.
- That second error pushed a non-existent container ID into AWS deployment state, updating Lambda and ECS definitions as if the image existed.
- Terraform rejected the Lambda portion of the change as invalid, but ECS service definitions had already been mutated, creating an inconsistent partial-failure state instead of a clean rollback.
- The outage became user-visible only when ECS tasks later restarted: once invalid task definitions were in place, exited tasks could not be replaced, and by about 5:48 UTC frontend ingest load balancers were returning 503s for ingest traffic.
- Separate self-monitoring detected the abnormality at 6:00 UTC, just 12 minutes after the visible failure began, but alert delivery to human operators failed.
- Early machine diagnosis was also scoped too narrowly: the detection agent initially treated the problem as isolated to GitHub webhook ingest rather than a broader ingest failure.
- Human operators were notified roughly 8 hours late because a notification-system misconfiguration had hidden alerts from normal incident-management channels.
- That notification failure was itself introduced during late-Friday testing of a deployment-attribution feature, when an engineer repeatedly deleted and recreated a policy document.
- At 7:47 UTC, Firetiger’s issue triage system successfully merged multiple ingest and traffic-drop signals into one incident view and identified the bad ECR version as root cause.
- After the report surfaced, operators used Claude Code with MCP, AWS access, and GitHub CLI access to locate the broken deployment, rebuild the image, rerun deploy scripts, and restore service.
- The postmortem supports AI-assisted remediation as operationally useful, but not as autonomous closure: the documented recovery still depended on correct problem surfacing and human-controlled execution.

## Evidence and Findings

- The source shows a two-step deployment-state corruption path: a CI race condition wrongly canceled a build, then a deploy attribution error later treated that canceled build as successful and propagated a non-existent container ID into Lambda and ECS definitions. This supports the conclusion that the outage conditions were created upstream in release machinery rather than by spontaneous runtime instability, which matters because it locates the primary control failure in state management and deploy validation.
- The source shows that Terraform rejected the Lambda update while ECS definitions were already changed, leaving the system partially mutated instead of safely rolled back. This supports the conclusion that deployment failure semantics were fail-open across components rather than fail-closed at the system boundary, which matters because partial infrastructure mutation can convert a detectable deploy error into a latent production outage.
- The source shows that once ECS task definitions were invalid, new tasks could not be put into production and exited tasks could not be restarted; around 5:48 UTC on March 1, restarted tasks failed to come up and frontend ingest load balancers began returning 503s for all ingest events. This supports the conclusion that the outage materialized at task-replacement time, not at the moment the bad state was written, which matters because latent invalid definitions can sit unnoticed until ordinary churn forces replacement.
- The source shows that self-monitoring detected the problem at 6:00 UTC, only 12 minutes after the visible failure started, but the detection agent initially scoped it as a GitHub webhook ingest issue and only attempted to notify humans through channels that were misconfigured. This supports the conclusion that machine detection existed but the escalation path was not operationally complete, which matters because observability without reliable human delivery does not provide real incident response.
- The source shows that human notification was delayed by about 8 hours because an internal alert-routing misconfiguration had been introduced during testing of a deployment-attribution feature late Friday. This supports the conclusion that secondary operational systems can dominate incident duration even when primary monitoring is fast, which matters because response resilience depends on notification-path integrity as much as on service telemetry.
- The source shows that by 7:47 UTC automated triage had coalesced multiple detections and identified the bad ECR version as root cause, and that later recovery used Claude Code with MCP, AWS access, and GitHub CLI access to locate the broken deployment, rebuild the image, rerun deploy scripts, and restore service. This supports the conclusion that AI-assisted operational tooling can compress diagnosis and repair once the incident is correctly surfaced, which matters because the practical value of agents here lies in accelerating bounded operator workflows, not replacing operational governance.

## Contradictions and Tensions

- The deployment both failed and succeeded in different ways: Terraform rejected the Lambda update, but ECS definitions were still changed. That is a concrete tension between nominal deploy failure and actual infrastructure mutation, and it is central because the system did not fail cleanly.
- Detection was fast in machine terms and slow in human terms. Firetiger detected the problem within 12 minutes, yet operators were informed about 8 hours late. The tension is not “monitoring absent” versus “monitoring present,” but monitoring present without dependable human delivery.
- Early incident understanding was directionally correct but too narrow. The first detection focused on GitHub webhook ingest, while the operational blast radius included broader ingest traffic. That mismatch matters because partial classification can slow the transition from anomaly detection to full incident framing.
- The invalid deployment state was created on February 27, but the visible outage did not occur until around 25 hours later when tasks restarted on March 1. This creates a tension between defect introduction time and user-visible failure time, showing how latent control-plane corruption can remain hidden until normal replacement behavior triggers it.
- The postmortem presents AI-assisted remediation as effective, but the same broader operational environment also contained the fragile CI, deploy attribution, and alert-routing paths that enabled the incident and prolonged it. The tension is that agentic systems can improve response while coexisting with, and potentially intensifying, failure complexity.

## Mechanism or Bounds

The strongest supported mechanism is a chained control-plane failure. First, CI concurrency logic incorrectly canceled a build during merge. Second, deploy attribution logic later misread that canceled build as completed and propagated a non-existent container ID into production deployment state. Third, deploy validation was component-inconsistent: Lambda rejected the invalid reference, but ECS definitions were still mutated. Fourth, the system stayed in a latent bad state until task replacement was needed; at that point invalid ECS definitions prevented new tasks from starting, and ingest requests began returning 503s. In parallel, the monitoring path functioned only partially: anomaly detection and later root-cause aggregation worked, but the machine-to-human notification path failed because alert routing had been misconfigured. The remediation evidence supports a bounded claim that AI tooling improved diagnosis and repair execution under human control; it does not support a broader claim that AI agents can autonomously secure incident response end to end.

## Limits

The source is a first-party postmortem, so the evidence is rich on sequence and operational detail but not independently verified.
It does not quantify customer count, total event loss, or recovery quality beyond the roughly 8-hour degradation window.
The remediation account supports successful AI-assisted recovery in this case, but it does not provide a counterfactual comparison against non-AI response, so claims about relative superiority are not warranted.
The causal account is strongest for the deploy-state corruption and alert-routing failures; it does not establish that no other system conditions influenced severity.
The mechanism is operationally well described, but broader generalization is bounded: this is evidence about one organization’s CI, deploy, ECS, Lambda, and notification stack, not a universal performance claim about AI agents in incident management.
