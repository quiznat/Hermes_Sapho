---
version: source-capture.v1
article_id: art-2026-03-21-024
ticket_id: ticket-import-art-2026-03-21-024
source_url: https://github.github.com/gh-aw/introduction/overview/
canonical_url: https://github.github.com/gh-aw/introduction/overview
source_title: About Workflows | GitHub Agentic Workflows
capture_kind: runtime-import
http_status: 200
content_type: text/html
captured_at_utc: '2026-03-21T23:08:45Z'
---
# Source Capture

## Title

About Workflows | GitHub Agentic Workflows

## Body

About Workflows | GitHub Agentic Workflows
Skip to content GitHub Agentic Workflows
Search Ctrl K Cancel
Quick Start Create Examples Docs FAQ Blog Peli's Agent Factory Quick Start Create Examples Docs FAQ Blog Peli's Agent Factory
GitHub RSS
Select theme Auto Dark Light
Blog
Introduction About Workflows
How They Work
Security Architecture
Presentation Slides
Setup Quick Start
Creating Workflows
CLI Commands
Guides Agentic Authoring
Ephemerals
GitHub Actions Primer
Reusing Workflows
Self-Hosted Runners
Using MCPs
Web Search
Design Patterns CentralRepoOps
ChatOps
DailyOps
DataOps
DispatchOps
IssueOps
LabelOps
MultiRepoOps
Monitoring
Orchestration
ProjectOps
SideRepoOps
SpecOps
TaskOps
TrialOps
Reference AI Engines
Assign to Copilot
Authentication
Authentication (Projects)
Cache Memory
Command Triggers
Compilation Process
Concurrency
Cost Management
Copilot Agent Files
Cross-Repository
Custom Safe Outputs
Dependabot
Environment Variables
FAQ
Footers
Frontmatter
Frontmatter (Full)
GH-AW Agent
GH-AW as MCP Server
GitHub Lockdown Mode
GitHub Tools
Glossary
Imports
Markdown
MCP Gateway
Network Access
Permissions
Rate Limiting Controls
Repo Memory
MCP Scripts
MCP Scripts (Spec)
Safe Outputs
Safe Outputs (Pull Requests)
Safe Outputs (Spec)
Safe Outputs (Staged Mode)
Sandbox
Schedule Syntax
Templating
Threat Detection
Tools
Triggering CI
Triggers
WASM Compilation
Workflow Structure
Fork Support
Troubleshooting Error Reference
Common Issues
Debugging Workflows
Debugging GHE Cloud with Data Residency
Editors
Quick Start Create Examples Docs FAQ Blog Peli's Agent Factory Quick Start Create Examples Docs FAQ Blog Peli's Agent Factory
GitHub RSS
Select theme Auto Dark Light
On this page Overview
What are Agentic Workflows?
Coding agents, running with tools, in GitHub Actions
On this page
Overview
What are Agentic Workflows?
Coding agents, running with tools, in GitHub Actions
About Workflows
What are Agentic Workflows?
Section titled “What are Agentic Workflows?”
Agentic workflows are AI-powered automation that can understand context, make decisions, and take meaningful actions-all from natural language instructions you write in markdown.
Unlike traditional automation with fixed if-then rules, agentic workflows use coding agents (like Copilot CLI, Claude by Anthropic, or Codex) to:
Understand context : Read your repository, issues, and pull requests to grasp the current situation
Make decisions : Choose appropriate actions based on the context, not just predefined conditions
Adapt behavior : Respond flexibly to different scenarios without requiring explicit programming for each case
Coding agents, running with tools, in GitHub Actions
Section titled “Coding agents, running with tools, in GitHub Actions”
With coding agents, you describe your automation needs in plain language. GitHub Agentic Workflows makes this possible by running natural language markdown files as agents in GitHub Actions that are executed by AI coding agents (AI systems that execute your instructions).
Instead of writing intricate scripts to handle issue triage, code reviews, or release management, you simply describe what you want to happen. The AI agent understands your repository context, interprets the situation, and takes appropriate actions-all from a few lines of markdown.
Here’s a simple example:
---
on : # Trigger: when to run
issues :
types : [ opened ]
permissions : read-all # Security: read-only by default
safe-outputs : # Allowed write operations
add-comment :
---
# Issue Clarifier
Analyze the current issue and ask for additional details if the issue is unclear.
The YAML section at the top is called frontmatter -it configures when the workflow runs and what it can do. The markdown body contains your natural language instructions. See Workflow Structure for details.
The gh aw compile command this markdown file into a hardened GitHub Actions Workflow .lock.yml file (the compiled workflow that GitHub Actions runs) that embeds the frontmatter and loads the markdown body at runtime. This runs an AI agent in a containerized environment whenever a new issue is opened.
Compilation (converting markdown to GitHub Actions YAML) validates your configuration, applies security hardening, and generates the final workflow file that GitHub Actions can execute. Think of it like compiling code-you write human-friendly markdown, the compiler produces machine-ready YAML.
The AI agent reads your repository context, understands the issue content, and takes appropriate actions - all defined in natural language rather than complex code.
Workflows use read-only permissions by default, with write operations only allowed through sanitized safe-outputs (validated GitHub operations) that enable creating issues, comments, and PRs without giving the AI direct write access. Access can be gated to team members only, ensuring AI agents operate within controlled boundaries.
More sample workflows can be found in the Agentics collection .
Next How They Work
Community Feedback
llms.txt · Create Workflow · Install · Reference
Made with by GitHub Next & Microsoft Research • Terms · Privacy · Security

## Import Provenance

- imported_from: canonical-openclaw-runtime
- runtime_article_bundle_path: research/articles/art-2026-03-21-024.md
- runtime_source_snapshot_json: research/source-material/art-2026-03-21-024.json
- runtime_source_snapshot_text: research/source-material/art-2026-03-21-024.txt
- runtime_filter_state: pending
- runtime_last_stage: intake
- refreshed_live_source: false
