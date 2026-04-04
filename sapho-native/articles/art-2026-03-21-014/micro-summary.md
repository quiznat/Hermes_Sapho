# Testing AI coding agents (2025): Cursor vs. Claude, OpenAI, and Gemini | Render Blog

## Core Thesis

This benchmark points to a narrow but useful conclusion: Cursor looked strongest in the greenfield app-generation test and also performed well on one production backend refactor, but the benchmark as a whole does not justify a clean overall ranking because part of the production comparison was not standardized across tools. The durable signal is not that one agent has won the category, but that task type and codebase-context handling appear to matter more than headline model properties alone.

## Why It Matters for Sapho

Sapho should not treat coding-agent evaluations as single-number truth. This source is useful because it shows two operating lessons at once: first, end-to-end software delivery still depends on practical scaffolding details such as migrations, container setup, and repository-pattern matching; second, polished benchmark tables can hide weak comparability underneath. For evaluation doctrine, that means Sapho should privilege task-bounded evidence, visible execution details, and context-handling behavior over generic claims about model size or context window.

## Key Findings

- In the blank-repo Next.js app-generation task, Cursor scored 9/10, needed 3 follow-up error prompts, and was the only tool to produce both the required Docker Compose setup and the SQL migration script.
- Claude Code scored 7/10 in the same greenfield task, needed 4 follow-up prompts, and got deployed functionality working on the first try despite some Next.js-specific friction.
- OpenAI Codex scored 5/10, also needed 4 follow-up prompts, and missed both Docker Compose and SQL migration output in the app-generation test.
- Gemini CLI, despite using Gemini Pro 2.5 and a 1M-token context window, scored only 3/10 in the greenfield task, required 7 follow-up prompts, and failed to display error or success messages in the app.
- On the production Go backend refactor, Cursor completed the task on the first try while matching the repository’s dependency-injection and interface-returning patterns, though it needed a minor clarification about Kubernetes namespace sourcing.
- Gemini later completed that backend refactor on the first try after loading broad codebase context, suggesting that large context capacity may help repository-oriented work even though it did not rescue performance in the separate blank-repo test.
- The source’s final score table gives Cursor an 8.0 average, Claude Code 6.8, Gemini CLI 6.8, and OpenAI Codex 6.0, but those summary numbers rest partly on production-task judgments that were not run as identical like-for-like comparisons.

## Evidence and Findings

- The strongest empirical result in the source is the greenfield app-generation test: Cursor earned 9/10, needed only 3 follow-up error prompts, and alone shipped both the database-oriented Docker Compose configuration and the SQL migration script. That supports the conclusion that its edge, in this setting, was not just prose quality but more complete delivery of operational project scaffolding.
- Gemini’s greenfield result cuts against any simple “bigger context wins” story. Even with the largest listed context window at 1M tokens, it scored 3/10, needed 7 follow-up prompts, and left basic user-feedback behavior incomplete in the app. That matters because it shows that raw context capacity does not automatically convert into strong first-pass execution in a blank-repo build task.
- The production backend evidence points in a different direction than the blank-repo test. Cursor completed a backend refactor on the first try while adhering to existing dependency-injection and interface conventions, and Gemini also completed the refactor on the first try after loading broad repository context. That supports a bounded conclusion that codebase-context use may matter more in repository maintenance work than in greenfield generation.
- The author explicitly notes that Cursor’s local-filesystem, RAG-like context gathering could be an advantage. Combined with its pattern-matching success in the Go monorepo, that gives a plausible operational explanation for why it looked strong in production work, though the article does not isolate this as a controlled causal factor.
- The benchmark itself includes a methodological warning: production-code tasks were not identical across tools, and scoring there was based mainly on overall impression. That matters because the precise-looking final category scores and averages can support directional judgment, but not a strict apples-to-apples ranking across agents.
- The full comparison covered both a blank-repo Next.js build and production tasks in a large Go API monorepo plus an Astro.js site. That broader structure makes the article more useful than a single toy demo, but it also reinforces that different task classes can produce materially different tool orderings.

## Contradictions and Tensions

- The clearest tension is Gemini’s split profile: it had the largest context window and later completed the backend refactor on the first try after ingesting broad repository context, yet it performed worst in the blank-repo app-generation task with a 3/10 and 7 follow-up prompts. The article therefore undermines the idea that large context alone predicts strong coding-agent performance.
- Cursor’s strong showing is real inside this benchmark, but the source simultaneously offers a reason to doubt how far that result generalizes. It excelled in the greenfield test and looked strong in one production refactor, yet the production side of the benchmark was not standardized across tools, so the final averages imply more measurement precision than the method can fully support.
- The benchmark presents summary scores with decimal-ready clarity while also admitting that some of the most consequential production judgments were impression-based and drawn from different tasks. That creates a direct tension between the appearance of exact ranking and the looser comparison procedure underneath.
- The production evidence suggests codebase-context retrieval is valuable, but the article does not disentangle whether success came from retrieval quality, model behavior, task simplicity, or author prompting. The mechanism is plausible but not cleanly separated from surrounding conditions.

## Mechanism or Bounds

The strongest bounded mechanism in the article is context alignment with existing code. Cursor is described as using local-filesystem, RAG-like retrieval, and its successful backend refactor matched the repository’s dependency-injection and interface conventions on the first try. Gemini’s backend success after loading broad codebase context points in the same direction. The supported explanation, therefore, is that repository-aware context handling may improve pattern-conforming production edits.

But this mechanism is only partially supported. The article does not run a controlled test that isolates retrieval method, prompt quality, or model capability. It also shows that context scale by itself is not sufficient: Gemini’s 1M-token window did not prevent a weak result in the blank-repo app-generation task. The bound is clear: context handling appears useful for repository work, but neither context size nor benchmark summary score alone can stand in for general coding-agent capability.

## Limits

This is a four-tool comparison from a single source, not an exhaustive market survey.

The production-code comparison is methodologically limited because different tools were given different tasks and then judged mainly by overall impression rather than identical execution against the same rubric.

Some mechanism claims, especially the suggested advantage from Cursor’s local-filesystem retrieval, are author-inferred rather than experimentally proven.

The benchmark mixes greenfield app generation with production maintenance work, and the results themselves show that tool ordering can shift across those task types.

The final score table is therefore useful for directional reading, not for treating one average as a definitive field-wide ranking.
