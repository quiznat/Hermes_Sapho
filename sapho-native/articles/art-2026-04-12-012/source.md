---
version: source-capture.v1
article_id: art-2026-04-12-012
ticket_id: ticket-import-art-2026-04-12-012
source_url: https://github.blog/ai-and-ml/github-copilot/github-copilot-cli-combines-model-families-for-a-second-opinion/
canonical_url: https://github.blog/ai-and-ml/github-copilot/github-copilot-cli-combines-model-families-for-a-second-opinion
source_title: GitHub Copilot CLI combines model families for a second opinion - The
  GitHub Blog
capture_kind: html
http_status: 200
content_type: text/html
captured_at_utc: '2026-04-12T12:15:00Z'
linked_paper_urls: []
---
# Source Capture

## Title

GitHub Copilot CLI combines model families for a second opinion - The GitHub Blog

## Body

Home / AI & ML / GitHub Copilot

GitHub Copilot CLI combines model families for a second opinion

Discover how Rubber Duck provides a different perspective to GitHub Copilot CLI.

Nick McKenna & Bartek Perz

April 6, 2026
| 5 minutes

Share:

When you ask a coding agent to build a data pipeline, it may not use the best structure. But what if the agent got a second opinion before it executed the plan?

Today, in GitHub Copilot CLI , we’re introducing Rubber Duck in experimental mode . Rubber Duck leverages a second model from a different AI family to act as an independent reviewer, assessing the agent’s plans and work at the moments where feedback matters most.

To catch different kinds of errors, a different perspective matters. Our evaluations show that Claude Sonnet + Rubber Duck makes up 74.7% of the performance gap between Sonnet and Opus alone, achieving better results for tackling difficult multi-file and long-running tasks. Use /experimental in Copilot CLI to access Rubber Duck alongside our other experimental features.

The problem: Confident mistakes can compound

Today’s coding agents follow a clear loop. First, the agent assesses the task, then drafts a plan, implements, tests, and iterates if necessary. It’s a powerful flow that works well, but it has blind spots. Any decision an agent makes early on, especially in the planning stage, is the foundation you’re building upon. Assumptions and inefficiencies become dependencies, and by the time you notice, you may have to fix more than just the small mistake at the start.

Using self-reflection and having the agent review its own output before moving forward is a proven technique. However, a model reviewing its own work is still bounded by its own training biases: the same training data and techniques, the same blind spots.

Rubber Duck adds a second perspective

Rubber Duck is a focused review agent, powered by a model from a complementary family to your primary Copilot session. When you’ve selected a Claude model from the model picker to use as your orchestrator, Rubber Duck will be GPT-5.4. As we experiment with Rubber Duck, we are exploring other model families for the orchestrator and for the Rubber Duck. The job of Rubber Duck is to check the agent’s work and surface a short, focused list of high-value concerns: details that the primary agent may have missed, assumptions worth questioning, and edge cases to consider.

When does the cross-family review help?

We evaluated Rubber Duck on SWE-Bench Pro , a benchmark of large, difficult, real-world coding problems drawn from open-source repositories. Here’s what we found:

Claude Sonnet 4.6 paired with Rubber Duck running GPT-5.4 achieved a resolution rate approaching Claude Opus 4.6 running alone, closing 74.7% of the performance gap between Sonnet and Opus.

We noticed that Rubber Duck tends to help more with difficult problems, ones that span 3+ files and would normally take 70+ steps. On these problems, Sonnet + Rubber Duck scores 3.8% higher than the Sonnet baseline, and 4.8% higher on the hardest problems identified across three trials. Here are a few examples of what Rubber Duck finds:

Architectural catch (OpenLibrary/async scheduler) : Rubber Duck caught that the proposed scheduler would start and immediately exit, running zero jobs—and that even if fixed, one of the scheduled tasks was itself an infinite loop.

One-liner bug, big impact (OpenLibrary/Solr) : Rubber Duck caught a loop that silently overwrote the same dict key on every iteration. Three of four Solr facet categories were being dropped from every search query, with no error thrown.

Cross-file conflict (NodeBB/email confirmation) : Rubber Duck caught three files that all read from a Redis key which the new code stopped writing. The confirmation UI and cleanup paths would have been silently broken on deploy.

When does Rubber Duck activate?

GitHub Copilot can call Rubber Duck automatically , both proactively and reactively , and it can be triggered by a user at any time to critique and revise its work.

For complex work, GitHub Copilot may seek a critique automatically at the checkpoints where feedback has the highest return:

After drafting a plan: This is where we expect developers will see the biggest wins, because catching a suboptimal decision early avoids compounding errors downstream.

After a complex implementation: This is when a second set of eyes on complex code can help catch edge cases.

After writing tests, before executing them: This is a chance to catch gaps in test coverage or flawed assertions, before self-reinforcing that “everything passes.”

The agent can also seek a critique reactively if it gets stuck in a loop or can’t make progress. Consulting Rubber Duck can break the logjam.

As a user, you can request a critique at any point. Copilot will query Rubber Duck, reason over the feedback, and show you what changed and why.

We made a key design choice: the agent invokes Rubber Duck sparingly, targeting the moments where the signal is highest, without getting in the way. For the technically curious: Rubber Duck is invoked through Copilot’s existing task tool—the same infrastructure used for other subagents.

For now, we are enabling Rubber Duck for all Claude family models (Opus, Sonnet, and Haiku) used as orchestrators in the model picker. We are already exploring other model families for the Rubber Duck to pair with GPT-5.4 as the orchestrator.

Getting started

Rubber Duck is available today in experimental mode .

To start using it, install GitHub Copilot CLI , and run the /experimental slash command. Rubber Duck will be available when you select any Claude model from the model picker and have access enabled to GPT-5.4. You’ll see critiques surface in two ways:

Automatically, when Copilot decides a checkpoint warrants a second opinion: after planning, after complex implementations, or after writing tests.

On demand, whenever you ask. Just tell Copilot to critique its work, and it will invoke Rubber Duck, incorporate the feedback, and show you exactly what changed.

Where Rubber Duck helps most:

Complex refactors and architectural changes

High-stakes tasks where a miss is costly

Ensuring comprehensive test coverage

Any time you want a second opinion on a plan before committing to it

Rubber Duck in GitHub Copilot CLI is now available in experimental mode. Share your feedback with us in the discussion .

Tags:

AI agents

GitHub Copilot

GitHub Copilot CLI

Written by

Nick McKenna

@nick-thinks

Applied Researcher III

Bartek Perz

@bartekperz

Principal Applied Science Manager
