---
version: article.v1
article_id: art-2026-03-03-013
ticket_id: ticket-import-art-2026-03-03-013
source_url: https://arxiv.org/html/2602.20478v1
source_title: 'Codified Context: Infrastructure for AI Agents in a Complex Codebase'
queued_at_utc: '2026-03-03T18:06:17Z'
captured_at_utc: '2026-04-02T16:17:59Z'
canonical_url: https://arxiv.org/abs/2602.20478
curator_decision: kept
artifact_minted_at_utc: '2026-04-02T16:20:22Z'
evidence_count: 15
claim_count: 4
publication_status: ready-for-daily
imported_from_runtime_article_id: art-2026-03-03-013
imported_from_runtime_last_stage: facts
imported_from_runtime_filter_state: pending
curator_reason: This preprint reports quantitative results and observational evidence
  from a real multi-session AI-assisted software project.
curated_at_utc: '2026-04-02T16:18:14Z'
curator_mode: agent
extracted_at_utc: '2026-04-02T16:20:22Z'
extractor_mode: agent
findings_mode: agent
summary_mode: agent
artifact_publication_status: published
artifact_publication_minted_at_utc: '2026-03-28T17:51:16Z'
artifact_publication_published_at_utc: '2026-03-29T03:09:17Z'
artifact_publication_alias: '20260303013'
source_remediation_status: completed
source_remediated_at_utc: '2026-04-02T16:17:59Z'
---
# Codified Context: Infrastructure for AI Agents in a Complex Codebase

## Core Thesis

The paper argues that AI-agent work in a large live codebase can be stabilized by splitting project context into tiers with different loading rules: a permanently loaded constitution for operating rules and routing, task-invoked specialist agents for focused domain behavior, and an on-demand knowledge base for broader project documentation. The strongest supported contribution is not a general performance law, but a concrete architecture for managing context pressure in one 108,000-line C# project.

## Why It Matters for Sapho

This matters because Sapho needs disciplined ways to keep governing rules hot, invoke specialized reasoning only when the task warrants it, and avoid flooding active context with the entire project archive. The paper supports the value of tiered context budgeting and explicit routing logic, but it also shows why retrieval quality and external validity must be treated cautiously: a keyword-matching knowledge layer is materially weaker than semantic recall, and descriptive project metrics are not the same thing as portable doctrine.

## Key Findings

- The reported system split context infrastructure into three layers: an always-loaded constitution, 19 specialized agents, and a cold-memory knowledge base containing 34 documents.
- The loading policy was explicit by tier: constitutional rules stayed resident, specialist agents were invoked per task, and documentation was fetched only when needed.
- Task routing was driven mainly by constitution trigger tables keyed to the files being changed, making dispatch rule-based rather than purely model-inferred.
- The retrieval layer was operational but limited: the MCP-served knowledge base exposed five search tools, yet the underlying retrieval relied on keyword substring matching rather than semantic search.
- The project context stack was substantial in its own right: about 54 files and 26,200 lines of context infrastructure against 108,000 lines of code, or 24.2% of code size.
- The paper explicitly warns against treating that 24.2% ratio as a target, and its evaluation remains bounded to one developer, one project, 283 sessions, 70 days of part-time work, and 148 commits.

## Evidence and Findings

- The source describes a three-part architecture consisting of a hot-memory constitution, 19 specialist agents, and a 34-document knowledge base, with each tier loaded differently. This supports the conclusion that the system’s main design move was deliberate context stratification rather than a single monolithic prompt, which matters because it shows one workable way to preserve governing rules while controlling context budget.
- Routing was not left to vague agent autonomy: the constitution contained trigger tables that selected specialist agents mainly from the files being modified. This supports the conclusion that task dispatch was codified and inspectable, which matters because reliable specialization in a complex codebase likely depends on explicit routing law rather than informal prompting alone.
- The retrieval layer was implemented through an MCP server with five search tools, including task-to-context and task-to-agent lookup, but the current implementation used keyword substring matching instead of semantic retrieval. This supports the conclusion that the knowledge base could provide relevant support only when wording aligned closely enough with stored documents, which matters because missed recall remains a live failure mode in any system that claims to surface the right context at the right time.
- More than half of each project agent specification was project-domain knowledge rather than behavioral instruction. This supports the conclusion that specialized agents in practice were carrying substantive local knowledge payload, not just style or role wrappers, which matters because the paper’s architecture depends on codified domain structure being written down somewhere rather than improvised at generation time.
- The paper reports 2,801 human prompts, 1,197 agent invocations, and 16,522 autonomous agent turns across 19,323 total interactions, alongside 283 sessions over 70 days. This supports the conclusion that the architecture was exercised repeatedly in real development rather than demonstrated in a toy example, which matters because it gives the design some operational credibility even though it does not establish controlled performance gains.
- The reported context infrastructure reached about 26,200 lines across 54 files, equal to 24.2% of the project’s 108,000 lines of code, and the author explicitly says that ratio should not be treated as a target. This supports the conclusion that context codification can become a major artifact in its own right, which matters because it reframes agent infrastructure as a serious maintenance surface rather than negligible overhead.

## Contradictions and Tensions

The paper does not present a direct contradiction to its core architectural claims, but there are important tensions.

The largest tension is between the ambition of a codified knowledge layer and the actual retrieval mechanism. The system offers structured retrieval tools, yet those tools rest on keyword substring matching, so the paper cannot support any broad claim that the knowledge base robustly surfaces all relevant context.

There is also tension between the precision of the reported metrics and their interpretability. The paper gives detailed counts, ratios, sessions, and interaction volumes, but it also says the 24.2% knowledge-to-code ratio is not a target and limits evaluation to one developer on one project without controlled experiments. That makes the numbers useful as descriptive scale markers, not as general guidance.

The case-study material points in a positive direction but remains non-causal. For example, the save-system specification was referenced in 74 sessions and 12 agent conversations, and the paper reports no save-related bugs across five later persistence features, yet that observation does not isolate the architecture as the sole cause.

## Mechanism or Bounds

The supported mechanism is context budgeting by tier. Constitutional rules stay continuously available, specialist behavior is loaded when task conditions are met, and broader documentation is retrieved only on demand. Within that design, routing is handled by explicit trigger tables keyed mainly to file modifications, giving the system a rule-based dispatch path instead of relying entirely on latent model judgment.

The bounds are equally important. Retrieval quality is limited by literal term overlap because the knowledge layer uses keyword substring matching rather than semantic search. The reported outcomes are also bounded by project scope and methodology: one developer, one codebase, no controlled comparison, and explicit acknowledgment that at least one headline ratio is descriptive rather than normative.

## Limits

The paper does not justify treating its context-to-code ratio, workflow mix, or observed outcomes as broadly valid performance guidance beyond this single project.

The retrieval layer is materially underpowered relative to stronger semantic systems, so claims about dependable context recovery should be treated as provisional.

The most prominent reported failure mode is specification staleness, which implies that codified context can decay and mislead if maintenance discipline slips.

Case studies show plausible value, including a concrete debugging fix and a reported absence of later save-related bugs, but they do not establish causal superiority over simpler workflows or alternative agent designs.

Overall, the paper supports tiered context architecture as a serious design pattern, but not as a settled or generally validated doctrine.
