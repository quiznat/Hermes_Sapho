---
version: article.v1
article_id: art-2026-03-04-023
ticket_id: ticket-import-art-2026-03-04-023
source_url: https://arxiv.org/abs/2310.06770
source_title: Published as a conference paper at ICLR 2024
queued_at_utc: '2026-03-04T03:59:01Z'
captured_at_utc: '2026-03-30T18:23:24Z'
canonical_url: https://arxiv.org/abs/2310.06770
curator_decision: kept
artifact_minted_at_utc: '2026-04-02T21:12:52Z'
evidence_count: 14
claim_count: 4
publication_status: ready-for-daily
imported_from_runtime_article_id: art-2026-03-04-023
imported_from_runtime_last_stage: facts
imported_from_runtime_filter_state: pending
curator_reason: This is a formal research paper introducing a benchmark with concrete
  evaluation results.
curated_at_utc: '2026-04-02T21:10:38Z'
curator_mode: agent
extracted_at_utc: '2026-04-02T21:12:52Z'
extractor_mode: agent
findings_mode: agent
summary_mode: agent
source_remediation_status: completed
source_remediated_at_utc: '2026-03-30T18:23:24Z'
artifact_publication_alias: '20260304023'
artifact_publication_status: published
artifact_publication_minted_at_utc: '2026-03-30T18:26:24Z'
artifact_publication_published_at_utc: '2026-03-30T18:26:29Z'
---
# Published as a conference paper at ICLR 2024

## Core Thesis

SWE-bench turns real GitHub maintenance episodes into a tightly filtered executable benchmark, and the result is a hard test of practical code-repair ability: from roughly 90,000 pull requests across 12 Python repositories, only 2,294 tasks survive the admission pipeline, and under the benchmark’s main BM25 retrieval setting the best reported model solves only about 2% of them.

## Why It Matters for Sapho

This matters because it sharpens two operating assumptions at once. First, “realistic” software-agent evaluation can still be highly selective: a benchmark built from real repository history may capture genuine maintenance structure while remaining narrow in task type. Second, current failure is not just about patch generation in the abstract. The paper makes retrieval and code localization look like central bottlenecks, which means Sapho should treat software-agent claims with suspicion unless they specify repository scope, retrieval regime, and verification rule rather than advertising raw coding competence.

## Key Findings

- SWE-bench is built from real issue–pull-request pairs in 12 popular Python repositories, but the benchmark is not a loose scrape: roughly 90,000 pull requests are narrowed to 2,294 executable task instances.
- Task admission is intentionally strict. Included cases must come from merged pull requests that resolve a GitHub issue, modify test files, contain at least one fail-to-pass test, and avoid installation or runtime errors.
- Success is also strict: a generated patch only counts if it applies cleanly and all associated unit and system tests pass.
- The benchmark instances are nontrivial in repository scope even when reference fixes are relatively compact: issue descriptions average 195 words, non-test codebases average 3,010 files and 438K lines, and reference solutions average edits to 1.7 files, 3.0 functions, and 32.8 lines.
- Test grounding is substantial rather than decorative. Every instance includes at least one fail-to-pass test, 40% include at least two, and the median instance runs 51 additional tests to check that unrelated behavior is preserved.
- Under the main BM25 retrieval setup, reported performance is extremely poor: Claude 2 resolves 1.97% of tasks, GPT-4-turbo 1.31%, ChatGPT-3.5 0.17%, and SWE-Llama 7b and 13b both 0.70%.
- Retrieval appears to be a major bottleneck. Claude 2 rises from roughly 2% under BM25 to 4.8% with oracle retrieval and 5.9% with oracle-collapsed retrieval.
- More context is not automatically better. At a 27,000-token limit, BM25 retrieves a superset of oracle files in about 40% of instances but retrieves none of the oracle files in nearly half, and increasing context improves recall while still reducing end-task performance.

## Evidence and Findings

- The benchmark’s realism comes from using actual software-maintenance episodes from public repositories, but its final task set is the product of severe narrowing: about 90,000 pull requests become 2,294 tasks across 12 Python repositories. That supports treating the benchmark as grounded in real work while also recognizing that it represents a filtered slice of software engineering rather than the whole field.
- The construction pipeline is procedural and execution-based rather than purely descriptive: repository selection and pull-request scraping feed attribute filtering and then execution filtering, and included tasks must resolve an issue, modify tests, include at least one fail-to-pass test, and avoid installation or runtime failures. This supports the conclusion that benchmark tasks are designed to be reproducible and machine-verifiable, which matters because it ties evaluation to concrete repository behavior rather than judge-style impression.
- The success rule is demanding: a model patch must apply successfully and then pass all associated unit and system tests. Combined with the fact that 40% of instances have at least two fail-to-pass tests and the median task runs 51 additional tests for preserved functionality, the benchmark is testing not just whether a model can trigger one desired behavior but whether it can repair the target bug without breaking nearby system behavior.
- The repository environment is large relative to the typical patch. Average issue descriptions are 195 words, average non-test codebases are 3,010 files and 438K lines, while reference fixes touch only 1.7 files, 3.0 functions, and 32.8 lines on average. That combination matters because it makes the task look less like open-ended code generation and more like high-precision localization inside a large search space.
- Under the main BM25 retrieval setting, every evaluated model performs badly, with the top result at 1.97% and the next strongest large model at 1.31%. This supports the conclusion that the benchmark exposes a major capability gap in practical repository-grounded repair, not a marginal performance shortfall.
- Retrieval quality materially changes outcomes. At a 27,000-token limit, BM25 retrieves a superset of oracle files in only about 40% of instances and misses all oracle files in nearly half; when Claude 2 is given oracle retrieval, performance rises to 4.8%, and to 5.9% with oracle-collapsed retrieval. That matters because it points to context selection and localization as decisive constraints, not just raw model size or patch-edit fluency.

## Contradictions and Tensions

- The benchmark is marketed as realistic because it comes from real repositories and real issue-resolution history, but its admission rules are highly selective. That creates a live tension between ecological validity and task-class narrowness: the benchmark is more realistic than synthetic exercises, yet it still excludes large regions of software work that do not present as merged bug-fix pull requests with executable fail-to-pass tests.
- Retrieval evidence cuts both ways. Larger context windows improve recall relative to oracle files, but the paper reports that performance still falls as context grows because models struggle to localize the relevant code. So “more code” helps the retriever see more of the truth while making the end-to-end agent worse at using it.
- Oracle retrieval materially improves Claude 2 from roughly 2% to 4.8% or 5.9%, which makes retrieval look like a real bottleneck, but the improved setting is less realistic than the main evaluation regime. The tension is that the paper shows access matters without proving that better practical retrieval alone would close most of the gap.
- The headline result is unmistakably poor, but it is also setup-bound. The benchmark demonstrates failure under the reported retrieval and execution conditions; it does not by itself prove that all stronger toolchains, alternative search methods, or different context-management systems would fail equally badly.

## Mechanism or Bounds

The strongest supported mechanism is a localization bottleneck inside large repositories. Tasks typically require small edits, but those edits sit inside codebases averaging 3,010 files and 438K lines, and BM25 often fails to retrieve the right files at all. Even when larger contexts improve retrieval recall, models appear to struggle to identify and use the relevant code within that expanded context. That gives a bounded operational explanation for the low success rates: the system often cannot reliably surface and focus on the right repair site before patch correctness is even fully tested.

The bounds are important. This mechanism is supported by the reported retrieval comparisons and context-size behavior, but it remains tied to the benchmark’s Python-only repository set, its strict task-admission filters, its 27,000-token retrieval regime, and the specific evaluated models and tooling. The evidence supports “retrieval and localization are major bottlenecks here,” not “all software-agent failure reduces to retrieval.”

## Limits

The benchmark captures a narrow executable slice of software maintenance, not general software engineering.
The reported results are strongly conditioned on the benchmark’s retrieval setup, repository mix, and success rule.
Oracle retrieval improves outcomes but still leaves success rates very low, so retrieval is important but not shown to be the only limiting factor.
The evidence does not cleanly separate failure modes among retrieval, code localization, patch synthesis, and test-satisfaction robustness.
One reported headline percentage varies slightly between the abstract and table presentation, with Claude 2 listed as 1.96% in summary text and 1.97% in Table 5, which does not change the conclusion but does matter for exact citation discipline.
