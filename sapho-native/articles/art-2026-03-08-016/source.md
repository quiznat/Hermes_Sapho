---
version: source-capture.v1
article_id: art-2026-03-08-016
ticket_id: ticket-import-art-2026-03-08-016
source_url: https://dev.to/maximsaplin/long-horizon-agents-opencode-gpt-52-codex-experiment-1f4h
canonical_url: https://dev.to/maximsaplin/long-horizon-agents-opencode-gpt-52-codex-experiment-1f4h
source_title: 'Long-horizon agents: OpenCode + GPT-5.2 Codex Experiment - DEV Community'
capture_kind: runtime-import
http_status: 200
content_type: text/html
captured_at_utc: '2026-03-08T12:31:03Z'
---
# Source Capture

## Title

Long-horizon agents: OpenCode + GPT-5.2 Codex Experiment - DEV Community

## Body

Long-horizon agents: OpenCode + GPT-5.2 Codex Experiment - DEV Community
Skip to content
Powered by Algolia
Log in
Create account
DEV Community
Add reaction
Like
Unicorn
Exploding Head
Raised Hands
Fire
Jump to Comments
Save
Boost
Copy link
Copied to Clipboard
Share to X
Share to LinkedIn
Share to Facebook
Share to Mastodon
Share Post via...
Report Abuse
Maxim Saplin
Posted on Jan 22
Long-horizon agents: OpenCode + GPT-5.2 Codex Experiment
# ai
# agents
# programming
# productivity
Sequoia Capital has recently published a blog post arguing that AGI has been achieved because "Long-horizon agents are functionally AGI". About the same time Cursor team has published their experiments with long-running agents that coded a web browser from scratch.
And my recent reflections of the past year made me realize what a huge stride has AI coding made over the course of just one year.
Along the lines of agentic coding and long-horizon execution, here's my recent experiment using OpenCode and GPT-5.2 Codex (predominantly at high reasoning level, sometimes switching to medium and xhigh)...
Approach: the main dialogue (or session in terms of OpenCOde) is the an orchestrator agent; you explicitly ask it to delegate individual tasks to sub-agents (OpenCode uses task built in tool for that ), verify them, and integrate the results. Why? Cause we don't want to hit the context window limit of the model. Though it could be an interesting experiment, relying on one single long thread with compaction happening from time to time.
Task: rewrite a previously vibe-coded provider for litellm which implements a cascade of requests to several LLMs (implementing strategies, such Mixture-of-Agents or LLM Council strategies) before returning a final response.
Results:
About 4 hours of pure agent work time
Orchestrator session — $4.13, 157k tokens of dialogue length by the end of the task
16 sub-agent sessions — $9.73
Total spent $13.86, about 2M tokens
26 files changed in Git
Only 5 tests written (some Kiro+Sonnet/Opus would probably have gone wild and generated a hundred test doing no real work) — all green
The app works — the provider executes multiple llm queries aggregating the final respond, the Streamlit dashboard shows the recorded traces.
While doing he work agents did plenty of tools calls, scrawl the code-base, made file edits and most importantly tested the changes being made (often the changes didn't work and the agents had to fix what was broken):
For these ~4 hours of agent time, it took about half an hour of human effort and ~10 user messages. 6 major human-in-the-loop touchpoints:
Discuss the scope, formulate a requirements .MD
Kick off the work by explicitly asking to delegate to sub-agents and make sure the tests are green
Ask to run a real case with actual LLM interaction
At xhigh resoning level, ask to analyze real LLM interaction test case failure and give a fix plan
Run the fix loop with a real LLM interactions
Finishing touches asking to fix the failing tests and tidy up the docs
The orchestrator/subagents approach has effectively allowed to fit in 2 million tokens worth of work into 157K token long main thread with the orchestrator - there's still room given that GPT-5.2 Codex has a 400K context window.
P.S> I liked OpenCode a lot, more that I liked Codex.
Top comments (0)
Subscribe
Personal
Trusted User
Create template
Templates let you quickly answer FAQs or store snippets for re-use.
Submit
Preview
Dismiss
Code of Conduct
•
Report abuse
Are you sure you want to hide this comment? It will become hidden in your post, but will still be visible via the comment's permalink .
Hide child comments as well
Confirm
For further actions, you may consider blocking this person and/or reporting abuse
Maxim Saplin
Follow
ツ AI in Software Dev, Open-source
Education
Computer Science @BNTU, MBA @BSU
Work
EPAM, Delivery Partner
Joined
Oct 12, 2019
More from Maxim Saplin
Ran out of Cursor tokens and switched to GitHub Copilot: Side-by-Side
# ai
# githubcopilot
# programming
# productivity
Cursor-like Semantic Rules in GitHub Copilot
# githubcopilot
# cursor
# ai
# programming
AI Dev: Plan Mode vs. SDD — A Weekend Experiment
# showdev
# ai
# flutter
# productivity
💎 DEV Diamond Sponsors
Thank you to our Diamond Sponsors for supporting the DEV Community
Google AI is the official AI Model and Platform Partner of DEV
Neon is the official database partner of DEV
Algolia is the official search partner of DEV
DEV Community — A space to discuss and keep up software development and manage your software career
Home
About
Contact
MLH
Code of Conduct
Privacy Policy
Terms of Use
Built on Forem — the open source software that powers DEV and other inclusive communities.
Made with love and Ruby on Rails . DEV Community © 2016 - 2026.
We're a place where coders share, stay up-to-date and grow their careers.
Log in
Create account

## Import Provenance

- imported_from: canonical-openclaw-runtime
- runtime_article_bundle_path: research/articles/art-2026-03-08-016.md
- runtime_source_snapshot_json: research/source-material/art-2026-03-08-016.json
- runtime_source_snapshot_text: research/source-material/art-2026-03-08-016.txt
- runtime_filter_state: pending
- runtime_last_stage: facts
- refreshed_live_source: false
