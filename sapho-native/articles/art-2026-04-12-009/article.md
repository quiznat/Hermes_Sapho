---
version: article.v1
article_id: art-2026-04-12-009
ticket_id: ticket-import-art-2026-04-12-009
source_url: https://github.blog/news-insights/company-news/github-availability-report-march-2026/
canonical_url: https://github.blog/news-insights/company-news/github-availability-report-march-2026
source_title: 'GitHub availability report: March 2026 - The GitHub Blog'
queued_at_utc: '2026-04-12T12:03:06Z'
captured_at_utc: '2026-04-12T12:12:28Z'
curator_decision: kept
artifact_minted_at_utc: '2026-04-12T12:19:22Z'
evidence_count: 20
claim_count: 4
publication_status: ready-for-daily
curator_reason: It reports concrete operational incidents with quantified service
  impact and mitigations.
curated_at_utc: '2026-04-12T12:16:14Z'
curator_mode: agent
extracted_at_utc: '2026-04-12T12:19:22Z'
extractor_mode: agent
findings_mode: agent
summary_mode: agent
---
# GitHub availability report: March 2026 - The GitHub Blog

## Core Thesis

GitHub reported four separate availability incidents in March 2026, with one broad platform degradation on March 3 and later incidents that were narrower but still severe. The report supports a specific operating lesson: platform instability did not come from one repeating global failure mode, but from distinct service-level faults, including cache-write amplification, Redis traffic misrouting, incomplete authentication remediation, and an upstream dependency outage.

## Why It Matters for Sapho

This matters because it argues against treating "availability" as a single platform property. The same month contained a cross-service cascade, a resiliency change that created a new failure, a repeated Copilot failure after an incomplete fix, and an upstream dependency break in Teams integrations. For Sapho's evaluation doctrine, that means vendor reliability claims need to be read at the level of mechanisms, service boundaries, and remediation quality, not just incident counts or aggregate uptime language.

## Key Findings

- GitHub reported four March 2026 incidents affecting different parts of the platform, showing a month of repeated degradation rather than a single isolated outage.
- The March 3 incident was broad but uneven: github.com request failures peaked around 40% and GitHub API failures around 43%, while Git over HTTP errors were about 6%, Copilot request errors about 21%, GitHub Actions impact stayed under 1%, and SSH was not impacted.
- GitHub attributed the March 3 degradation to a deployment that expired, recalculated, and rewrote every user's cache, raising load enough to trigger replication delays and then broader downstream service impact.
- The March 5 GitHub Actions incident was severe despite being service-specific: 95% of workflow runs failed to start within 5 minutes, average delay was 30 minutes, and 10% of runs failed with infrastructure errors.
- GitHub tied the March 5 Actions failure to a Redis load-balancer misconfiguration introduced during resiliency updates, with internal traffic routed to the wrong host.
- The Copilot Coding Agent failed twice on March 19 and March 20 because of datastore authentication problems; the first incident averaged about 53% errors and peaked near 93%, while the second averaged about 99% and peaked near 100%, with retry amplification making the recurrence worse.
- GitHub said the second Copilot incident happened because remediation after the first was incomplete, which turns the sequence into a remediation-quality failure as much as an authentication failure.
- A fourth March 24 incident hit GitHub's Microsoft Teams integrations: average error rate was 37.4%, peak error rate was 90.1%, and about 19% of installs failed to receive notifications, with GitHub attributing the break to an upstream dependency outage.

## Evidence and Findings

- The source shows that March 3 was not a flat whole-platform outage but an uneven cross-service degradation. github.com and the API each lost roughly two-fifths of requests at peak, while SSH stayed unaffected and Actions remained below 1% impact. That supports the conclusion that even broad incidents can propagate selectively across surfaces, which matters because platform-wide headlines can hide materially different operational risk by workflow.
- The source gives a concrete mechanism for March 3: a deployment meant to reduce write burden instead caused every user's cache to expire, recalculate, and rewrite, increasing load until replication delays cascaded into multiple services. That supports a bounded conclusion that internal optimization work in shared state paths can create platform-scale failure through load amplification rather than through a single edge-service crash.
- The March 5 Actions incident shows a different risk profile: 95% of workflow runs did not start within 5 minutes, average delay reached 30 minutes, and 10% failed with infrastructure errors. That supports the conclusion that service-specific incidents can still be operationally severe even when the broader platform is not broadly down, which matters for CI-dependent organizations that experience latency and queue collapse as a production failure.
- GitHub's reported cause for March 5 was a Redis load-balancer misconfiguration introduced during resiliency updates, with mitigation achieved by correcting the load balancer and then draining queued jobs. That supports the conclusion that "resiliency" changes are themselves a live source of fragility when rollout controls and routing validation are insufficient.
- The two Copilot Coding Agent incidents supply strong recurrence evidence: the first reached about 53% average errors with a 93% peak, and the second reached about 99% average errors with a 100% peak, alongside retry amplification. That supports the conclusion that incomplete remediation can turn an already severe incident into a near-total service failure on recurrence, which matters because post-incident closure language can overstate the actual state of repair.
- The March 24 Teams integration incident adds a further boundary case: notification delivery failed with 37.4% average errors, 90.1% peak errors, and roughly 19% of installs affected, with GitHub attributing it to an upstream dependency outage. That supports the conclusion that some GitHub reliability exposure sits outside GitHub's direct control plane, which matters when judging integrations that depend on external services and network paths.

## Contradictions and Tensions

- The March 3 event was platform-wide in scope but not in severity. github.com and the API were heavily degraded, while SSH was unaffected and Actions stayed below 1% impact. The tension is that "broad outage" is directionally true but analytically incomplete.
- The March 5 incident was caused by updates framed as resiliency work. The tension is direct: work meant to improve resilience instead created the routing failure that degraded GitHub Actions.
- The Copilot sequence contains the clearest contradiction between remediation posture and outcome. GitHub said credentials were rotated after the first incident, yet a second, worse incident followed because remediation was incomplete.
- The March 24 Teams integration failure was counted within GitHub's availability reporting, but the stated cause was an upstream dependency outage. That creates a decision tension between platform accountability and dependency-bounded reliability.

## Mechanism or Bounds

The strongest supported mechanism is on March 3: a faulty deployment triggered mass cache expiry, recalculation, and rewrite activity, increasing write load enough to cause replication delays that then cascaded into multiple dependent services. For March 5, the supported mechanism is narrower: Redis load-balancer misconfiguration routed traffic to the wrong host, degrading Actions startup and execution. For the two Copilot incidents, the supported mechanism is an authentication failure that blocked the service from reaching its backing datastore, with the second outage worsened by incomplete remediation and retry amplification. For the Teams integration incident, the mechanism is only bounded at the dependency level: GitHub attributed failures to an upstream outage producing HTTP 500s and connection resets, without a deeper internal causal account of that upstream system.

## Limits

The report is vendor-authored and its causal accounts are not independently verified.
The evidence supports incident counts, impact metrics, and bounded mechanism claims, but not a unified theory of GitHub platform fragility across all four incidents.
The March 3 account explains a load-amplification cascade, yet it does not provide a full service-by-service causal model for why severity differed so sharply across surfaces.
The Copilot incidents show recurrence after an attempted fix, but the report does not fully specify why the first remediation was incomplete or why retry amplification was not contained before the second event intensified.
The March 24 integration incident is mechanistically shallow because the failure is pushed upstream; the evidence supports dependency exposure more clearly than root cause.
