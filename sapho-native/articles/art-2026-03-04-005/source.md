---
version: source-capture.v1
article_id: art-2026-03-04-005
ticket_id: ticket-import-art-2026-03-04-005
source_url: https://github.com/Cluster444/agentic
canonical_url: https://github.com/Cluster444/agentic
source_title: "GitHub - Cluster444/agentic: An agentic workflow tool that provides\
  \ context engineering support for opencode \xB7 GitHub"
capture_kind: runtime-import
http_status: 200
content_type: text/html
captured_at_utc: '2026-03-07T19:27:14Z'
---
# Source Capture

## Title

GitHub - Cluster444/agentic: An agentic workflow tool that provides context engineering support for opencode · GitHub

## Body

GitHub - Cluster444/agentic: An agentic workflow tool that provides context engineering support for opencode · GitHub
Skip to content
Navigation Menu
Toggle navigation
Sign in
Appearance settings
Platform AI CODE CREATION GitHub Copilot Write better code with AI
GitHub Spark Build and deploy intelligent apps
GitHub Models Manage and compare prompts
MCP Registry New Integrate external tools
DEVELOPER WORKFLOWS Actions Automate any workflow
Codespaces Instant dev environments
Issues Plan and track work
Code Review Manage code changes
APPLICATION SECURITY GitHub Advanced Security Find and fix vulnerabilities
Code security Secure your code as you build
Secret protection Stop leaks before they start
EXPLORE Why GitHub
Documentation
Blog
Changelog
Marketplace
View all features
Solutions BY COMPANY SIZE Enterprises
Small and medium teams
Startups
Nonprofits
BY USE CASE App Modernization
DevSecOps
DevOps
CI/CD
View all use cases
BY INDUSTRY Healthcare
Financial services
Manufacturing
Government
View all industries
View all solutions
Resources EXPLORE BY TOPIC AI
Software Development
DevOps
Security
View all topics
EXPLORE BY TYPE Customer stories
Events & webinars
Ebooks & reports
Business insights
GitHub Skills
SUPPORT & SERVICES Documentation
Customer support
Community forum
Trust center
Partners
View all resources
Open Source COMMUNITY GitHub Sponsors Fund open source developers
PROGRAMS Security Lab
Maintainer Community
Accelerator
Archive Program
REPOSITORIES Topics
Trending
Collections
Enterprise ENTERPRISE SOLUTIONS Enterprise platform AI-powered developer platform
AVAILABLE ADD-ONS GitHub Advanced Security Enterprise-grade security features
Copilot for Business Enterprise-grade AI features
Premium Support Enterprise-grade 24/7 support
Pricing
Search or jump to...
Search code, repositories, users, issues, pull requests...
-->
Search
Clear
Search syntax tips
Provide feedback
-->
We read every piece of feedback, and take your input very seriously.
Include my email address so I can be contacted
Cancel
Submit feedback
Saved searches
Use saved searches to filter your results more quickly
-->
Name
Query
To see all available qualifiers, see our documentation .
Cancel
Create saved search
Sign in
Sign up
Appearance settings
Resetting focus
You signed in with another tab or window. Reload to refresh your session.
You signed out in another tab or window. Reload to refresh your session.
You switched accounts on another tab or window. Reload to refresh your session.
Dismiss alert
{{ message }}
Cluster444
/
agentic
Public
Notifications
You must be signed in to change notification settings
Fork
23
Star
374
Code
Issues
6
Pull requests
4
Actions
Security
0
Insights
Additional navigation options
Code
Issues
Pull requests
Actions
Security
Insights
Cluster444/agentic
master
Branches Tags
Go to file
Code Open more actions menu
Folders and files
Name
Name
Last commit message
Last commit date
Latest commit
History
38 Commits
38 Commits
.github/ workflows
.github/ workflows
.opencode/ command
.opencode/ command
agent
agent
command
command
docs
docs
scripts
scripts
src/ cli
src/ cli
.gitignore
.gitignore
.npmignore
.npmignore
AGENT.template.md
AGENT.template.md
AGENTS.md
AGENTS.md
CHANGELOG.md
CHANGELOG.md
LICENSE
LICENSE
README.md
README.md
THOUGHTS.md
THOUGHTS.md
TODO.md
TODO.md
bun.lock
bun.lock
package.json
package.json
tsconfig.json
tsconfig.json
View all files
Repository files navigation
README
MIT license
Agentic
Modular AI agents and commands for structured software development with OpenCode.
What It Does
Agentic is a context engineering tool that assists OpenCode in producing reliable software improvements.
Agentic is a workflow management system for AI-assisted software development using OpenCode. It provides:
Context Management : Organized "thoughts" directory structure for storing architecture docs, research, plans, and reviews
Modular AI Agents & Commands : Pre-configured prompts and specialized subagents that enhance OpenCode 's capabilities through task decomposition and context compression
Structured Development Workflow : A phased approach (Research → Plan → Execute → Commit → Review) for handling tickets and features
Distribution System : A CLI tool to distribute agent/command configurations to projects via .opencode directories
Purpose
The system aims to:
Make AI-assisted development more systematic and reproducible
Reduce context window usage through specialized subagents
Maintain project knowledge over time (architecture decisions, research, implementation history)
Provide guardrails for AI agents through structured workflows
Quick Start
Installation
From bun/npm (Recommended)
npm install -g agentic-cli
# or
bun add -g agentic-cli
From Source
git clone https://github.com/Cluster444/agentic.git
cd agentic
bun run build
bun install
bun link # Makes 'agentic' command available globally
Deploy globally
This will pull all agents/commands into your global ~/.config/opencode/ directory.
agentic pull -g
Deploy to Your Project
This will pull all agents/commands into a local .opencode directory.
cd ~ /projects/my-app
agentic pull
Development Workflow
Use the ticket command to work with the agent to build out ticket details
Use the research command to analyze the codebase from the ticket details
Use the plan command to generate an implementation plan for the ticket using the research
Use the execute command to implement the changes
Use the commit command to commit your work
Use the review command to verify the implementation
Between each phase it is important to inspect the output from each phase and ensure that it is actually in alignment with what you want the project do be and the direction it is going. Errors in these files will cascade to the next phase and produce code that is not what you wanted.
In OpenCode, these commands are invoked with a slash: /ticket , /research , /plan , /execute , etc.
Most of these commands want the ticket in question that you want to review, exceptions are ticket itself, and commit/review. Ticket you give an actual prompt that describes what you're trying to do, and commit/review are meant to work in the context window that you ran execute in so that it has all of the details of how the process itself went.
Documentation
Getting Started
Usage Guide - Complete guide to using Agentic
Development Workflow - Detailed workflow phases
Core Components
Agentic CLI - Command-line tool reference
Commands - Available OpenCode commands
Agents - Specialized AI subagents
Project Structure
Thoughts Directory - Knowledge management system
Architecture Docs - System design documentation
Requirements
Bun runtime
OpenCode CLI
Git
Contributing
This project is in active development. Contributions, ideas, and feedback are welcome!
License
MIT License - see LICENSE file for details
About
An agentic workflow tool that provides context engineering support for opencode
Topics
agentic
agentic-coding
context-engineering
Resources
Readme
License
MIT license
Uh oh!
There was an error while loading. Please reload this page .
Activity
Stars
374
stars
Watchers
3
watching
Forks
23
forks
Report repository
Releases
3
v0.1.9
Latest
Sep 2, 2025
+ 2 releases
Packages
0
Uh oh!
There was an error while loading. Please reload this page .
Contributors
2
Cluster444
Chris Covington
SirSilver
Askar
Languages
TypeScript
96.2%
Shell
3.8%
Footer
© 2026 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Community
Docs
Contact
Manage cookies
Do not share my personal information
You can’t perform that action at this time.

## Import Provenance

- imported_from: canonical-openclaw-runtime
- runtime_article_bundle_path: research/articles/art-2026-03-04-005.md
- runtime_source_snapshot_json: research/source-material/art-2026-03-04-005.json
- runtime_source_snapshot_text: research/source-material/art-2026-03-04-005.txt
- runtime_filter_state: pending
- runtime_last_stage: intake
- refreshed_live_source: false
