---
version: article.v1
article_id: art-2026-04-15-004
ticket_id: ticket-import-art-2026-04-15-004
source_url: https://github.blog/security/application-security/how-exposed-is-your-code-find-out-in-minutes-for-free/
canonical_url: https://github.blog/security/application-security/how-exposed-is-your-code-find-out-in-minutes-for-free
source_title: "How exposed is your code? Find out in minutes\u2014for free - The GitHub\
  \ Blog"
queued_at_utc: '2026-04-15T13:01:07Z'
captured_at_utc: '2026-04-15T13:02:11Z'
curator_decision: kept
artifact_minted_at_utc: '2026-04-15T13:04:59Z'
evidence_count: 13
claim_count: 4
publication_status: ready-for-daily
curator_reason: Vendor blog includes concrete operational metrics and remediation
  results, not just product description.
curated_at_utc: '2026-04-15T13:02:42Z'
curator_mode: agent
extracted_at_utc: '2026-04-15T13:04:59Z'
extractor_mode: agent
findings_mode: agent
summary_mode: agent
artifact_publication_alias: '20260415001'
artifact_publication_status: published
artifact_publication_minted_at_utc: '2026-04-15T13:04:59Z'
artifact_publication_published_at_utc: '2026-04-15T14:02:41Z'
---
# How exposed is your code? Find out in minutes—for free - The GitHub Blog

## Core Thesis

GitHub is positioning Code Security Risk Assessment as a fast, free entry-point security scan for organizations: a one-click, CodeQL-based pass over up to 20 of the most active repositories that produces an exposure dashboard rather than a full organizational audit. The practical claim is not that it proves total code security posture, but that it can quickly surface concentrated vulnerability patterns, repository hotspots, and candidates for automated remediation inside a bounded slice of the codebase.

## Why It Matters for Sapho

This matters because the field keeps selling “visibility” products as if partial scans equal comprehensive exposure understanding. GitHub’s framing is more useful when read precisely: the product lowers activation cost for security triage, but the evidence also shows hard scope bounds on who can run it, which repos are included, and what the dashboard can actually represent. For Sapho, the operational lesson is that lightweight security telemetry can be strategically valuable, but only if evaluation doctrine keeps partial coverage, access control, and vendor-reported remediation claims visibly separate from proven organization-wide risk reduction.

## Key Findings

- GitHub says the assessment is a free, one-click code security scan, with the free offer bounded to GitHub Enterprise Cloud and GitHub Team plans, and with scanning minutes not counting against GitHub Actions quota.
- Access is restricted to organization admins and security managers rather than all users, so the tool is institutionally gated as well as technically scoped.
- The scan covers up to 20 of an organization’s most active repositories and uses CodeQL, which means the assessment is explicitly partial and prioritizes active-repository coverage over full-repository completeness.
- The dashboard reports aggregate vulnerability totals across scanned repositories with severity splits across critical, high, medium, and low findings.
- The output also includes language-level views, security-rule classes with repository impact counts and severities, and identification of the most vulnerable repositories.
- GitHub says the dashboard shows which detected vulnerabilities are eligible for Copilot Autofix, linking triage output to possible automated remediation paths.
- GitHub pairs that eligibility signal with broader 2025 platform metrics: 460,258 security alerts fixed using Copilot Autofix, 50% of vulnerability alerts resolved directly in pull requests, and mean time to remediation of 0.66 hours with Copilot Autofix versus 1.29 hours for manual fixes.

## Evidence and Findings

- The source describes the assessment as a free, one-click scan and states that it is available on GitHub Enterprise Cloud and GitHub Team plans without consuming GitHub Actions minutes for the scan. That supports the conclusion that GitHub is trying to minimize adoption friction. What matters is that cost and setup barriers are part of the product pitch, not an independently validated measure of detection quality.
- The post states that only organization admins and security managers can run the assessment and that it scans up to 20 of the organization’s most active repositories using CodeQL. That supports the conclusion that the tool is a role-controlled, bounded sampling mechanism rather than an unrestricted or org-wide inspection layer. The significance is that “organizational exposure” here is inferred from a capped active-repo subset, not from complete repository coverage.
- GitHub says the dashboard reports total vulnerabilities across scanned repositories and breaks them down by critical, high, medium, and low severity, while also grouping results by language. That supports the conclusion that the assessment is designed for aggregate triage and pattern recognition rather than deep case-by-case incident analysis. This matters because severity and language clustering can guide prioritization even when the scan set is incomplete.
- The source says the dashboard surfaces security-rule classes, the number of repositories affected by each rule, rule severity, and the most vulnerable repositories. That supports the conclusion that the output is intended to help organizations identify repeated defect families and concentration points. The operational significance is that repeated rule hits across multiple repositories often indicate process-level weaknesses, not just isolated bugs.
- GitHub says the assessment identifies how many detected vulnerabilities are eligible for Copilot Autofix, and separately reports 2025 platform-wide figures of 460,258 security alerts fixed with Copilot Autofix, 50% of vulnerability alerts resolved in pull requests, and 0.66-hour mean time to remediation versus 1.29 hours for manual fixes. That supports the conclusion that GitHub is coupling detection with an automation story centered on faster fix throughput. What matters is that the automation argument is supported by large aggregate vendor metrics, but not by organization-specific outcomes from this assessment itself.

## Contradictions and Tensions

- The strongest tension is between the headline promise of showing how exposed an organization’s code is and the actual coverage model: only up to 20 of the most active repositories are scanned. That can surface serious exposure, but it cannot justify a clean reading of total organizational risk.
- The tool is framed as broadly accessible and free, yet eligibility is restricted both by plan type and by role. That lowers activation cost for some organizations while leaving clear access boundaries in place.
- The dashboard offers aggregate counts, severity splits, language views, and vulnerable-repository rankings, which are useful for triage, but those views are only as complete as the scanned subset. Strong-looking dashboards can therefore create a false sense of comprehensiveness if the coverage cap is ignored.
- The Copilot Autofix connection is decision-relevant but not fully closed: the assessment reports Autofix eligibility for detected findings, while the remediation-speed evidence comes from GitHub-wide 2025 metrics rather than from outcomes attributable to this assessment workflow. The result is a real but incomplete bridge between detection and fix performance.

## Mechanism or Bounds

The supported mechanism is a bounded triage pipeline: CodeQL scans up to 20 of the organization’s most active repositories, the system aggregates detected issues into severity, language, rule-class, and repository-level views, and it flags which findings are eligible for Copilot Autofix. In operational terms, the product is meant to compress time-to-visibility and potentially time-to-remediation by routing a selected repository set through a standardized analysis and then pointing users toward automation-ready fixes. The bounds are explicit: coverage is partial, access is role-limited, and the remediation gains cited are platform-level comparative metrics rather than causal proof that this specific assessment produces the same gains inside any given organization.

## Limits

The evidence base is a GitHub product announcement, so the strongest supported claims are about stated availability, scope, dashboard outputs, and vendor-reported metrics, not independent effectiveness validation.
The scan is capped at 20 active repositories, which leaves unclear how well the output reflects dormant, niche, legacy, or long-tail repositories that may still carry meaningful security risk.
The source does not provide methodology details for the 0.66-hour versus 1.29-hour remediation comparison, limiting confidence in how broadly that performance difference should be generalized.
The article supports a bounded claim about faster triage and possible remediation acceleration, but not a claim that the assessment gives complete organizational exposure measurement or guaranteed risk reduction.
