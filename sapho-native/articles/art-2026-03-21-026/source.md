---
version: source-capture.v1
article_id: art-2026-03-21-026
ticket_id: ticket-import-art-2026-03-21-026
source_url: https://github.github.com/gh-aw/setup/quick-start/
canonical_url: https://github.github.com/gh-aw/setup/quick-start
source_title: Quick Start | GitHub Agentic Workflows
capture_kind: runtime-import
http_status: 200
content_type: text/html
captured_at_utc: '2026-03-23T01:11:30Z'
---
# Source Capture

## Title

Quick Start | GitHub Agentic Workflows

## Body

Quick Start | GitHub Agentic Workflows
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
GitHub Actions Primer
Reusing Workflows
Using Custom MCPs
Self-Hosted Runners
Ephemerals
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
Custom Safe Outputs
Environment Variables
FAQ
Footers
Frontmatter
Frontmatter (Full)
GH-AW Agent
GH-AW as MCP Server
GitHub (Checkout)
GitHub (Read Tools)
GitHub (Read Permissions)
GitHub (Integrity Filtering)
GitHub (Cross-Repository)
GitHub (Fork Support)
Glossary
Imports
Imports (APM)
Imports (Copilot Agent Files)
Imports (Dependabot)
Markdown
MCP Gateway
Network Access
Playwright
Rate Limiting
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
Workflow Structure
Troubleshooting Error Reference
Common Issues
Debugging Workflows
Debugging GHE Cloud with Data Residency
Editors
Quick Start Create Examples Docs FAQ Blog Peli's Agent Factory Quick Start Create Examples Docs FAQ Blog Peli's Agent Factory
GitHub RSS
Select theme Auto Dark Light
On this page Overview
Adding an Automated Daily Status Workflow to Your Repo
Prerequisites Step 1 - Install the extension
Step 2 - Add the sample workflow and trigger a run
Step 3 - Wait for the workflow to complete
Step 4 - Customize your workflow (optional)
What’s next?
On this page
Overview
Adding an Automated Daily Status Workflow to Your Repo
Prerequisites Step 1 - Install the extension
Step 2 - Add the sample workflow and trigger a run
Step 3 - Wait for the workflow to complete
Step 4 - Customize your workflow (optional)
What’s next?
Quick Start
Adding an Automated Daily Status Workflow to Your Repo
Section titled “Adding an Automated Daily Status Workflow to Your Repo”
Estimated time: 10 minutes
In this guide you will add an existing, pre-baked workflow to an existing GitHub repository where you are a maintainer - the automated Daily Repo Status Report , running in GitHub Actions.
Your browser doesn't support HTML5 video. Download the video here .
Install the extension, add a workflow, and trigger a run from the CLI
The aim here is to become familiar with automated AI : to install something that will run automatically , recurringly , in the context of your repository.
Prerequisites
Section titled “Prerequisites”
Before installing, ensure you have:
AI Account - GitHub Copilot , Anthropic Claude or OpenAI Codex
GitHub Repository - A repository where you have write access
GitHub Actions enabled - Check in Settings → Actions
GitHub CLI ( gh ) v2.0.0+ - Install here . Check version: gh --version
Operating System : Linux, macOS, or Windows with WSL
Step 1 - Install the extension
Section titled “Step 1 - Install the extension”
Install the GitHub Agentic Workflows extension:
gh extension install github/gh-aw
Tip
If you are encountering authentication issues, use this script instead:
curl -sL https://raw.githubusercontent.com/github/gh-aw/main/install-gh-aw.sh | bash
or login interactively:
gh auth login
Step 2 - Add the sample workflow and trigger a run
Section titled “Step 2 - Add the sample workflow and trigger a run”
From your repository root run:
gh aw add-wizard githubnext/agentics/daily-repo-status
This will take you through an interactive process to:
Check prerequisites - Verify repository permissions.
Select an AI Engine - Choose between Copilot, Claude, or Codex.
Set up the required secret - COPILOT_GITHUB_TOKEN , ANTHROPIC_API_KEY or OPENAI_API_KEY .
Add the workflow - Adds the workflow and lock file to .github/workflows/ .
Optionally trigger an initial run - Starts the workflow immediately.
Tip
Having trouble? Check your repository secrets , see the FAQ and Common Issues .
Step 3 - Wait for the workflow to complete
Section titled “Step 3 - Wait for the workflow to complete”
An automated workflow run can take 2-3 minutes.
Once your initial run is complete, a new issue will be created in your repository with a “Daily Repo Report”. The report will be automatically generated and will analyze:
Recent repository activity (issues, PRs, discussions, releases, code changes)
Progress tracking, goal reminders and highlights
Project status and recommendations
Actionable next steps for maintainers
The report will look something like this:
Step 4 - Customize your workflow (optional)
Section titled “Step 4 - Customize your workflow (optional)”
With GitHub Agentic Workflows, you are in control! Your repository automation is fully customizable. You should shape your repo automation to match your priorities and your needs.
To customize it now:
Open the workflow markdown file located at .github/workflows/daily-repo-status.md in your repository.
Edit the section “What to include” to list things you are having trouble with regularly in your repository: your issue blacklog, your CI setup, your testing, the performance of your software, your roadmap. Any or all of these, or anything else you want to improve. You can also customize the style and process sections to guide the coding agent’s behavior.
If you have changed the frontmatter, regenerate the workflow YAML from the frontmatter of your workflow by running:
gh aw compile
Commit and push to your repository.
Optionally trigger another run by running:
gh aw run daily-repo-status
After waiting for the workflow to complete, check the new issue created with your updated report!
What’s next?
Section titled “What’s next?”
There are hundreds of other ways to use GitHub Agentic Workflows! Explore some of these in Peli’s Agent Factory .
Continue learning with these resources:
Creating Agentic Workflows
How Agentic Workflows Work
Frequently Asked Questions
Previous Presentation Slides Next Creating Workflows
Community Feedback
llms.txt · Create Workflow · Install · Reference
Made with by GitHub Next & Microsoft Research • Terms · Privacy · Security

## Import Provenance

- imported_from: canonical-openclaw-runtime
- runtime_article_bundle_path: research/articles/art-2026-03-21-026.md
- runtime_source_snapshot_json: research/source-material/art-2026-03-21-026.json
- runtime_source_snapshot_text: research/source-material/art-2026-03-21-026.txt
- runtime_filter_state: pending
- runtime_last_stage: intake
- refreshed_live_source: false
