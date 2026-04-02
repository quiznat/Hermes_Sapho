---
version: article.v1
article_id: art-2026-03-03-001
ticket_id: ticket-import-art-2026-03-03-001
source_url: https://arxiv.org/abs/2602.11988
source_title: '[2602.11988] Evaluating AGENTS.md: Are Repository-Level Context Files
  Helpful for Coding Agents?'
queued_at_utc: '2026-03-03T10:37:26Z'
captured_at_utc: '2026-03-13T03:00:58Z'
canonical_url: https://arxiv.org/abs/2602.11988
curator_decision: kept
artifact_minted_at_utc: '2026-04-02T03:21:03Z'
evidence_count: 15
claim_count: 4
publication_status: ready-for-daily
imported_from_runtime_article_id: art-2026-03-03-001
imported_from_runtime_last_stage: intake
imported_from_runtime_filter_state: pending
curator_reason: This is a preprint reporting benchmarked experimental results on coding
  agents with concrete measured outcomes.
curated_at_utc: '2026-04-02T03:18:38Z'
curator_mode: agent
extracted_at_utc: '2026-04-02T03:21:03Z'
extractor_mode: agent
findings_mode: agent
summary_mode: agent
artifact_publication_status: published
artifact_publication_minted_at_utc: '2026-03-27T17:37:36Z'
artifact_publication_published_at_utc: '2026-03-28T00:19:30Z'
artifact_publication_alias: '20260303001'
---
# Repository-level context files mostly add cost and activity overhead rather than improving coding-agent success

## Core Thesis

This study finds that repository-level context files, as currently used, usually do not help coding agents solve software tasks better. Across the evaluated agents and models, they generally lowered success rates relative to giving no repository context while raising inference cost by more than 20%. Developer-written files performed better than model-generated ones, but the gain over no context was small, and the added context still pushed agents into more work rather than faster contact with the right files.

## Why It Matters for Sapho

This matters because the field often treats repository guidance files as an obvious best practice for coding agents. The evidence here says that assumption is unsafe. More context is not automatically better context, and visible structure can still degrade outcomes if it induces extra searching, reading, testing, and tool use without materially improving task targeting. For Sapho, that shifts evaluation doctrine away from “context added” as a proxy for capability and toward a stricter question: does the added structure improve success under bounded cost, or does it merely produce more elaborate agent behavior.

## Key Findings

- Across the evaluated coding agents and language models, adding repository-level context files generally reduced task success relative to no repository context and increased inference cost by more than 20%.
- Developer-provided context files outperformed model-generated files and delivered only a modest average gain over no context, about 4%, with at least one clear exception: Claude Code did not improve over no context.
- Model-generated context files slightly hurt performance on average, with benchmark-level resolution-rate drops of 0.5% on SWE-bench Lite and 2% on AGENTbench, while increasing average cost by 20% and 23% respectively.
- The negative average result for model-generated files was not universal: when other repository documentation was removed after generation, those files improved performance by 2.7% on average and outperformed developer-written documentation.
- Context files did not meaningfully reduce the number of steps before agents first touched patch-relevant files, weakening the claim that they mainly help agents orient faster.
- With context files present, agents ran more tests, searched more files, read more files, wrote more files, and used more repository-specific tools; some models also consumed more reasoning tokens.

## Evidence and Findings

- In the main evaluation setting, repository context files produced a bad tradeoff: lower task success and more than 20% higher inference cost versus no repository context. That supports the conclusion that repository-level guidance can impose overhead rather than delivering net problem-solving benefit.
- Developer-written context files did better than model-generated ones across all four evaluated agents and improved over no-context baselines by about 4% on average. That supports a narrow claim that human-authored guidance can help somewhat, but only modestly and not consistently enough to justify broad optimism.
- The benchmark-level numbers for model-generated files are explicitly negative in the standard setting: average resolution fell by 0.5% on SWE-bench Lite and 2% on AGENTbench, while cost rose by 20% and 23%. That matters because it converts a vague skepticism about synthetic repository summaries into a concrete cost-performance penalty.
- The mechanism evidence points toward behavioral expansion rather than better targeting. Context files did not materially reduce steps to first interaction with files changed in the original patch, but agents with context files searched more, read more, tested more, wrote more, and invoked more repository-specific tools.
- Manual trace inspection strengthens that interpretation: GPT-5.1 mini sometimes searched for context files repeatedly and reread them even when they were already present in context. That supports the view that these files can trigger redundant workflow loops instead of efficient orientation.
- The strongest counterpoint appears when surrounding documentation is stripped away. In that altered setting, model-generated context files improved performance by 2.7% on average and beat developer-written documentation, showing that usefulness depends on the broader documentation environment rather than on a simple good/bad property of context files themselves.

## Contradictions and Tensions

The central tension is that repository context files are widely recommended, yet the main experimental result is negative on average. A second tension is internal to the paper: developer-written files slightly helped compared with no context, but the overall pattern across context-file use still leaned toward lower success and higher cost. A third tension is that model-generated files underperformed in the standard setting but became beneficial once other documentation was removed. So the evidence does not support a blanket rejection of repository context files; it supports a narrower warning that their value is conditional and can reverse depending on the surrounding documentation regime and the agent using them.

## Mechanism or Bounds

The best-supported mechanism is overhead induction, not accelerated orientation. Context files did not meaningfully shorten the path to patch-relevant files, but they did increase agent activity: more file search, more reading, more testing, more writing, more named-tool use, and for some models more reasoning-token expenditure. That pattern supports a bounded explanation that added repository guidance often expands the action surface and encourages extra work without proportional gains. But this remains a partial mechanism, not a full causal decomposition. The study shows what changed in behavior, not a complete account of why those changes reduced success.

## Limits

The evidence is benchmark-bound, not universal. The main developer-context evaluation uses AGENTbench, a 138-instance Python benchmark drawn from 12 niche repositories, so generalization beyond that task mix and ecosystem should be cautious. Some benchmark-construction claims, such as the absence of solution leakage, rest on partial manual inspection rather than exhaustive verification. The behavioral mechanism evidence is strong enough to bound explanation but not enough to fully separate distraction, prompt-budget pressure, tool-triggering effects, or model-specific planning failures. And because the positive result for model-generated files appears only after removing other documentation, the paper does not justify a simple deployment rule; it instead shows that repository guidance quality interacts with what other documentation agents already receive.
