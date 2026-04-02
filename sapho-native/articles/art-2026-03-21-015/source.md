---
version: source-capture.v1
article_id: art-2026-03-21-015
ticket_id: ticket-import-art-2026-03-21-015
source_url: https://www.augmentcode.com/blog/1-open-source-agent-on-swe-bench-verified-by-combining-claude-3-7-and-o1
canonical_url: https://www.augmentcode.com/blog/1-open-source-agent-on-swe-bench-verified-by-combining-claude-3-7-and-o1
source_title: '#1 open-source agent on SWE-Bench Verified by combining Claude 3.7
  and O1 | Augment Code'
capture_kind: runtime-import
http_status: 200
content_type: text/html
captured_at_utc: '2026-03-21T22:52:56Z'
---
# Source Capture

## Title

#1 open-source agent on SWE-Bench Verified by combining Claude 3.7 and O1 | Augment Code

## Body

#1 open-source agent on SWE-Bench Verified by combining Claude 3.7 and O1 | Augment Code
Skip to content
Product
Context Engine Pricing Docs Blog Resources
Sign in Install
Product Agent Intent Code Review Slack CLI Context Engine MCP Changelog
Context Engine Pricing Docs Blog Resources Customers Careers ContextWiki Status Page Trust Center Security
Talk to Sales Sign in
Install
Back to Blog #1 open-source agent on SWE-Bench Verified by combining Claude 3.7 and O1
Mar 31, 2025 •
Tongfei Chen, Colin Flaherty
We open-sourced how we got to #1 on SWE-bench verified - check it out here.
For the past couple months, we have been tracking and optimizing against SWE-bench, the industry standard for agentic code benchmarks. It’s clear that we’re now in an agentic era, and the ability of agents to perform accurately on real-world codebases will only become more important. Today, we are proud to share that we have achieved a 65.4% success rate on SWE-bench verified. We provide a technical breakdown below and have open-sourced our approach to hitting the top published spot on the leaderboard.
Check out our open-source repository here . It’s super simple and implements the entire SWE-bench pipeline end-to-end (agent runs in Docker containers, ensembling, evaluating candidate solutions).
At Augment, our mission is to build the best AI platform for professional software engineers and their teams. We employ a mix of closed-source and fine-tuned open-source models to deliver the best possible product experience. We obsessively test, tune, and optimize models for every part of the coding experience, choosing the best model for every interaction. This means engineering teams can harness the power of AI, without the overhead of knowing which model can do what today (which will all change again tomorrow). Sign up for Augment today to get access to powerful AI for coding in your IDE of choice (VSCode, JetBrains, and Neovim).
Summary of our approach
To achieve a 65.4% success rate on our first-ever SWE-bench submission we combined Claude Sonnet 3.7 as our core driver, along with OpenAI’s o1 as our ensembler. We deferred leveraging our own models to build a strong open-source baseline agent with off-the-shelf models.
Since Anthropic’s models are currently state-of-the-art on code, we used Claude Sonnet 3.7 as our agent’s core driver, and we forked our agent system architecture from Anthropic’s own blog post about SWE-bench . The main deltas in our implementation include figuring out what their unpublished “planning” tool was and using OpenAI’s o1 model as our ensembler. We were surprised to see some techniques that didn’t help such as Sonnet 3.7’s thinking mode and running a separate “fix regressions” agent after the implementation agent. While we explored some basic ensembling techniques like majority voting (e.g. more basic than the system that produced Anthropic’s 70.3% result), we decided not to investigate this direction further because it introduces significant extra cost that is not realistic for real-world usage at current model serving costs.
For next steps, we are fine-tuning our own models with reinforcement learning and proprietary data to significantly improve the user experience through significantly faster and cheaper agents, all while maintaining similar scores on SWE-bench Verified.
What's SWE-bench actually testing?
SWE-bench tests how well AI systems handle software engineering tasks pulled from actual GitHub issues in popular open-source projects. Some example problems can be found in OpenAI’s original blog post on the benchmark . Where most coding benchmarks focus on isolated Leetcode-style programming problems, SWE-bench involves codebase navigation, iterating against a suite of regression tests, and overall much more complexity.
For each problem in SWE-bench, the AI agent is supplied with a codebase (dependencies pre-installed) and a description of a task. It is not told what tests it must run to verify a working solution, but it instead must solve for this by finding relevant regression tests and writing its own reproduction script. It needs to figure out how to run tests on its own, which means it needs to “onboard” itself to each codebase just like a human programmer would. It must then navigate entirely on its own to apply a solution to the codebase. This involves editing files, running tests with a bash tool, running bash commands like “grep” and “ls”, creating reproduction scripts, and reflecting on its solution.
The benchmark then checks if the final solution submitted by the agent passes a suite of held-out new tests checking new functionality and regression tests checking existing functionality.
Pros and cons of SWE-bench as a benchmark
While SWE-bench is an incredible asset for the AI research community, no benchmark is perfect. SWE-bench leans heavily towards fixing small bugs rather than creating new features and the descriptions of tasks are significantly more descriptive and LLM-friendly than the prompts we find developers supply agents in real-life. It also only includes Python projects, missing the diversity of languages in actual development environments. Consider how error messages from failed tests tend to be significantly more descriptive in Python than in languages like Java and C++, which makes Python an easier language for agents to work with. Also, consider how production codebases are often orders of magnitude larger than open source codebases, requiring more sophisticated codebase awareness and navigation. Finally, OpenAI found that only 8.4% of problems in SWE-bench Verified take more than an hour to solve by an experienced software engineer.
Real-world software engineering involves collaboration, iteration, and context that no existing benchmark fully captures. Augment’s production coding agents benefit from integrations with 3rd party software like Linear, Jira, Notion, Google Search, Slack, and more. Our production agents are also able to ping the developer with questions when they get stuck. Finally, they memorize feedback and tips provided by developers, so their performance improves over time. None of these features can be tested by SWE-bench (in its current form).
At Augment, we care a lot about building the highest quality product experience for our customers, which includes the best AI technology under the hood. That is why we are always thinking about how to improve the state of benchmarks. For example, we recently shared with the world some details on AugmentQA , a benchmark designed to measure repository-aware code retrieval through realistic question-answering tasks directly sourced from real-world software development scenarios.
What we learned
We found that scores on SWE-bench verified are largely driven by the quality of the foundation model. Optimizing prompts was important but saturates as an axis for improvement. In addition to this, there is a gain of 3-8% to be had from ensembling techniques. It makes sense that ensembling helps as the agent’s results are highly unstable. We found that when sampling any two of our rollouts over 50 examples would have different outcomes between the two rollouts.
We were also impressed by how well agents can leverage tools like “grep” and “find” to navigate codebases in SWE-bench. However, while this codebase navigation technique works well for SWE-bench, we found that for real world use-cases, this approach to codebase awareness currently has limitations, due to its ability to handle ambiguous user inputs and large codebases. We found countless other examples like this where changes that improved the quality of our production coding agents (as measured by qualitative customer feedback) did not move the needle on SWE-bench.
Given these learnings, we think the right way to think about research as an application-layer AI coding company is to focus on dramatically improving cost and latency through finetuning open source models with reinforcement learning. By training dramatically faster agents that are cheap enough to run in larger swarms, categorically new AI coding experiences are made possible. There will be more to come from us on this point.
At same time, we recognize that quantitative evals for agents are deeply imperfect, just like evals for prior waves of AI technologies. There is a long tail of improvements that are needed to deliver a superior product that are not represented in evals like SWE-bench. We continue to focus on tracking down and optimizing all these issues.
How we did it: the deep dive
In short, we experimented with all the top models, tools, and test-time compute techniques, ultimately converging on a system that combines the best aspects of Anthropic’s Claude Sonnet 3.7 model and OpenAI’s O1 model.
In doing so, we further deepened our expertise in building agents. These insights have proven invaluable as we build out and perfect our agentic features, including IDE agents and other features on the horizon. For this first submission, we decided not to train our own model, but are investigating this as a possible next project to improve cost and latency of running agents.
To supplant Anthropic’s unpublished “planning” tool from their own SWE-bench blog post, we found using their “sequential thinking” MCP was effective. This was important because Sonnet’s 3.7 thinking mode is not effective within the context of SWE-bench. We experimented with variations to a string-replace based file editing tool, such as a smart paste model, but found this wasn’t a promising direction to improve scores. Similarly we also experimented with variations to the bash tool, but found the final score was not affected by these either. We explored adding various embedding-based retrieval tools but found that for SWE-bench tasks this was not the bottleneck – “grep” and “find” were sufficient. (In practice, we find that embedding-based tools are critical to deliver a great product experience.)
We explored some techniques to break up the agent workflow into separate agent runs with separate prompts. This included adding an initial orientation agent run that figures out how to run tests, and adding a final “fix regressions” agent run that fixes any regressions in existing tests introduced by the candidate solution. We found this direction of research ultimately wasn’t very fruitful either. While the “fix regressions” agent was able to find and fix some regressions, it also introduced bugs into otherwise correct candidates solutions, resulting in no net improvement to the final score.
For ensembling, we used a simple majority voting technique with OpenAI’s o1 model by showing it a list of candidate diffs, along with the problem statement, and asking it to pick the majority vote solution. We found providing extra context beyond the candidate diffs was not helpful. We found o1 was better than Sonnet 3.7 at ensembling by a couple percent. We did not investigate the ensembling route further because it is too expensive to use in real-world settings.
Here is our instruction we start each agent run with, forking from Anthropic’s instruction :
markdown
< uploaded_files >
{location}
</ uploaded_files >
I've uploaded a python code repository in the directory {location} (not in /tmp/inputs). Consider the following PR description:
< pr_description >
{pr_description}
</ pr_description >
Can you help me implement the necessary changes to the repository so that the requirements specified in the < pr_description > are met?
I've already taken care of all changes to any of the test files described in the < pr_description > . This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-tests files in the {location} directory to ensure the < pr_description > is satisfied.
Follow these steps to resolve the issue:
1. As a first step, it would be a good idea to explore the repo to familiarize yourself with its structure.
2. Create a script to reproduce the error and execute it with `python <filename.py>` using the BashTool, to confirm the error.
3. Use the sequential_thinking tool to plan your fix. Reflect on 5-7 different possible sources of the problem and distill those down to 1-2 most likely sources.
4. Edit the source code of the repo to resolve the issue.
5. Rerun your reproduction script and confirm that the error is fixed!
6. Think about edgecases and make sure your fix handles them as well
7. Run select tests from the repo to make sure that your fix doesn't break anything else.
GUIDE FOR HOW TO USE "sequential_thinking" TOOL:
- Your thinking should be thorough and so it's fine if it's very long. Set totalThoughts to at least 5, but setting it up to 25 is fine as well. You'll need more total thoughts when you are considering multiple possible solutions or root causes for an issue.
- Use this tool as much as you find necessary to improve the quality of your answers.
- You can run bash commands (like tests, a reproduction script, or 'grep'/'find' to find relevant context) in between thoughts.
- The sequential_thinking tool can help you break down complex problems, analyze issues step-by-step, and ensure a thorough approach to problem-solving.
- Don't hesitate to use it multiple times throughout your thought process to enhance the depth and accuracy of your solutions.
TIPS:
- You must make changes in the {location} directory in order to ensure the requirements specified in the < pr_description > are met. Leaving the directory unchanged is not a valid solution.
- Do NOT make tool calls inside thoughts passed to sequential_thinking tool. For example, do NOT do this: {{'thought': 'I need to look at the actual implementation of `apps.get_models()` in this version of Django to see if there\'s a bug. Let me check the Django apps module:\n\n < function_calls > \n < invoke name = " str_replace_editor " > \n < parameter name = " command " > view </ parameter > \n < parameter name = " path " > django/apps/registry.py </ parameter > </ invoke > ', 'path': 'django/apps/registry.py'}}
- Respect the tool specifications. If a field is required, make sure to provide a value for it. For example "thoughtNumber" is required by the sequential_thinking tool.
- When you run "ls" or variants of it, you may see a symlink like "fileA -> /data/vol/fileA". You can safely ignore the symlink and just use "fileA" as the path when read, editing, or executing the file.
- When you need to find information about the codebase, use "grep" and "find" to search for relevant files and code with the bash tool
- Use your bash tool to set up any necessary environment variables, such as those needed to run tests.
For more details on how we achieved the top leaderboard spot on SWE-bench, you can access our open-source implementation on GitHub here . Happy coding!
Written by
Tongfei Chen
Tongfei Chen is a Research Scientist at Augment Code focused on code generation and information retrieval. Previously, he spent four years at Microsoft working as a Senior Researcher. He earned a PhD in Computer Science from Johns Hopkins University.
Colin Flaherty
Colin Flaherty is a founding researcher at Augment working on AI agents and retrieval systems. Before that, he was a researcher at Facebook AI Research, where he coauthored a paper in Science on "Cicero"—an AI that mastered the game of Diplomacy, widely considered the next grand challenge in AI for games after Chess, Go, and Poker.
Ship code like the best teams
Install Augment
Get Started
Give your codebase the agents it deserves
Install Augment to get started. Works with codebases of any size, from side projects to enterprise monorepos.
Install Augment Contact Sales
PRODUCT
Agent
Intent
Code Review
Slack
CLI
Pricing
RESOURCES
Customers
Docs
Blog
Guides
Learn
Tools
AI Engineering Playbook
COMPANY
Careers
Press Inquiries
Press Kit
Contact Sales
Contact Support
Changelog
Privacy & Security
Trust Center
Status Page
LEGAL
Cookie Policy
Privacy Policy
SLA and Support Policy
Terms of Service
© 2026 Augment Code. All rights reserved.
DARK
LIGHT
SYSTEM

## Import Provenance

- imported_from: canonical-openclaw-runtime
- runtime_article_bundle_path: research/articles/art-2026-03-21-015.md
- runtime_source_snapshot_json: research/source-material/art-2026-03-21-015.json
- runtime_source_snapshot_text: research/source-material/art-2026-03-21-015.txt
- runtime_filter_state: pending
- runtime_last_stage: facts
