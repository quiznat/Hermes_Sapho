# Queue Artifact — art-2026-03-07-033

Source URL: https://blog.firetiger.com/postmortem-on-the-march-1-2026-ingest-incident/  
Canonical URL: https://blog.firetiger.com/postmortem-on-the-march-1-2026-ingest-incident/  
Lane: agent-factory  
Decision: retain

## Thesis

Agent-operated incident response can localize root causes quickly, but reliability still depends on deployment harness integrity and notification-path correctness; when those controls fail together, time-to-human-awareness dominates outage impact.

## Mechanism summary

The postmortem describes a layered failure chain: CI race/cancellation plus artifact attribution error triggered a partial Terraform/ECS deploy into invalid task definitions; delayed task restarts later converted this latent state into production ingest failure. Detection agents identified symptom clusters and root cause, but notification-channel misconfiguration prevented timely operator escalation.

<!-- canonical-empirical-findings -->

## Empirical Findings (Data Snapshot)

| Novel finding | Quantitative result | Experimental setup/sample | Metric/outcome | Caveat/limit |
|---|---|---|---|---|
| Customer impact window | approximately 8 hours of degraded ingest on 2026-03-01. | — | — | — |
| Affected surfaces | OpenTelemetry ingest and GitHub webhook intake. | — | — | — |
| Latency to visible outage onset after bad deploy mutation | ~25 hours before ECS restarts exposed failure mode. | — | — | — |
| System-detection lag from first customer-impact signal | ~12 minutes (problem materialized ~05:48 UTC, detected ~06:00 UTC). | — | — | — |
| Human-notification delay | ~8 hours due to internal notification policy misconfiguration. | — | — | — |
| Root-cause stack | CI race + erroneous artifact attribution + partial infra apply + notification routing failure. | — | — | — |

## Confidence

Medium-high. First-party incident write-up with explicit timeline and remediation details, but not independently audited.

## Why it matters for Sapho

Reinforces Sapho’s doctrine that autonomous diagnostics are insufficient without hardened escalation rails; notification-path integrity and deploy-guard invariants must be tested as first-class reliability controls.
