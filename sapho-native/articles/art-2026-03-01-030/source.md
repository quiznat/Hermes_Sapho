---
version: source-capture.v1
article_id: art-2026-03-01-030
ticket_id: ticket-import-art-2026-03-01-030
source_url: https://github.com/snarktank/ralph
canonical_url: https://github.com/snarktank/ralph
source_title: "GitHub - snarktank/ralph: Ralph is an autonomous AI agent loop that\
  \ runs repeatedly until all PRD items are complete. \xB7 GitHub"
capture_kind: runtime-import
http_status: 200
content_type: text/html
captured_at_utc: '2026-03-22T18:24:58Z'
---
# Source Capture

## Title

GitHub - snarktank/ralph: Ralph is an autonomous AI agent loop that runs repeatedly until all PRD items are complete. · GitHub

## Body

GitHub - snarktank/ralph: Ralph is an autonomous AI agent loop that runs repeatedly until all PRD items are complete. · GitHub
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
GitHub Stars
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
snarktank
/
ralph
Public
Notifications
You must be signed in to change notification settings
Fork
1.4k
Star
13.5k
Code
Issues
31
Pull requests
29
Actions
Projects
Security
0
Insights
Additional navigation options
Code
Issues
Pull requests
Actions
Projects
Security
Insights
snarktank/ralph
main
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
20 Commits
20 Commits
.claude-plugin
.claude-plugin
.github/ workflows
.github/ workflows
flowchart
flowchart
skills
skills
.gitignore
.gitignore
AGENTS.md
AGENTS.md
CLAUDE.md
CLAUDE.md
LICENSE
LICENSE
README.md
README.md
prd.json.example
prd.json.example
prompt.md
prompt.md
ralph-flowchart.png
ralph-flowchart.png
ralph.sh
ralph.sh
ralph.webp
ralph.webp
View all files
Repository files navigation
README
MIT license
Ralph
Ralph is an autonomous AI agent loop that runs AI coding tools ( Amp or Claude Code ) repeatedly until all PRD items are complete. Each iteration is a fresh instance with clean context. Memory persists via git history, progress.txt , and prd.json .
Based on Geoffrey Huntley's Ralph pattern .
Read my in-depth article on how I use Ralph
Prerequisites
One of the following AI coding tools installed and authenticated:
Amp CLI (default)
Claude Code ( npm install -g @anthropic-ai/claude-code )
jq installed ( brew install jq on macOS)
A git repository for your project
Setup
Option 1: Copy to your project
Copy the ralph files into your project:
# From your project root
mkdir -p scripts/ralph
cp /path/to/ralph/ralph.sh scripts/ralph/
# Copy the prompt template for your AI tool of choice:
cp /path/to/ralph/prompt.md scripts/ralph/prompt.md # For Amp
# OR
cp /path/to/ralph/CLAUDE.md scripts/ralph/CLAUDE.md # For Claude Code
chmod +x scripts/ralph/ralph.sh
Option 2: Install skills globally (Amp)
Copy the skills to your Amp or Claude config for use across all projects:
For AMP
cp -r skills/prd ~ /.config/amp/skills/
cp -r skills/ralph ~ /.config/amp/skills/
For Claude Code (manual)
cp -r skills/prd ~ /.claude/skills/
cp -r skills/ralph ~ /.claude/skills/
Option 3: Use as Claude Code Marketplace
Add the Ralph marketplace to Claude Code:
/plugin marketplace add snarktank/ralph
Then install the skills:
/plugin install ralph-skills@ralph-marketplace
Available skills after installation:
/prd - Generate Product Requirements Documents
/ralph - Convert PRDs to prd.json format
Skills are automatically invoked when you ask Claude to:
"create a prd", "write prd for", "plan this feature"
"convert this prd", "turn into ralph format", "create prd.json"
Configure Amp auto-handoff (recommended)
Add to ~/.config/amp/settings.json :
{
"amp.experimental.autoHandoff" : { "context" : 90 }
}
This enables automatic handoff when context fills up, allowing Ralph to handle large stories that exceed a single context window.
Workflow
1. Create a PRD
Use the PRD skill to generate a detailed requirements document:
Load the prd skill and create a PRD for [your feature description]
Answer the clarifying questions. The skill saves output to tasks/prd-[feature-name].md .
2. Convert PRD to Ralph format
Use the Ralph skill to convert the markdown PRD to JSON:
Load the ralph skill and convert tasks/prd-[feature-name].md to prd.json
This creates prd.json with user stories structured for autonomous execution.
3. Run Ralph
# Using Amp (default)
./scripts/ralph/ralph.sh [max_iterations]
# Using Claude Code
./scripts/ralph/ralph.sh --tool claude [max_iterations]
Default is 10 iterations. Use --tool amp or --tool claude to select your AI coding tool.
Ralph will:
Create a feature branch (from PRD branchName )
Pick the highest priority story where passes: false
Implement that single story
Run quality checks (typecheck, tests)
Commit if checks pass
Update prd.json to mark story as passes: true
Append learnings to progress.txt
Repeat until all stories pass or max iterations reached
Key Files
File
Purpose
ralph.sh
The bash loop that spawns fresh AI instances (supports --tool amp or --tool claude )
prompt.md
Prompt template for Amp
CLAUDE.md
Prompt template for Claude Code
prd.json
User stories with passes status (the task list)
prd.json.example
Example PRD format for reference
progress.txt
Append-only learnings for future iterations
skills/prd/
Skill for generating PRDs (works with Amp and Claude Code)
skills/ralph/
Skill for converting PRDs to JSON (works with Amp and Claude Code)
.claude-plugin/
Plugin manifest for Claude Code marketplace discovery
flowchart/
Interactive visualization of how Ralph works
Flowchart
View Interactive Flowchart - Click through to see each step with animations.
The flowchart/ directory contains the source code. To run locally:
cd flowchart
npm install
npm run dev
Critical Concepts
Each Iteration = Fresh Context
Each iteration spawns a new AI instance (Amp or Claude Code) with clean context. The only memory between iterations is:
Git history (commits from previous iterations)
progress.txt (learnings and context)
prd.json (which stories are done)
Small Tasks
Each PRD item should be small enough to complete in one context window. If a task is too big, the LLM runs out of context before finishing and produces poor code.
Right-sized stories:
Add a database column and migration
Add a UI component to an existing page
Update a server action with new logic
Add a filter dropdown to a list
Too big (split these):
"Build the entire dashboard"
"Add authentication"
"Refactor the API"
AGENTS.md Updates Are Critical
After each iteration, Ralph updates the relevant AGENTS.md files with learnings. This is key because AI coding tools automatically read these files, so future iterations (and future human developers) benefit from discovered patterns, gotchas, and conventions.
Examples of what to add to AGENTS.md:
Patterns discovered ("this codebase uses X for Y")
Gotchas ("do not forget to update Z when changing W")
Useful context ("the settings panel is in component X")
Feedback Loops
Ralph only works if there are feedback loops:
Typecheck catches type errors
Tests verify behavior
CI must stay green (broken code compounds across iterations)
Browser Verification for UI Stories
Frontend stories must include "Verify in browser using dev-browser skill" in acceptance criteria. Ralph will use the dev-browser skill to navigate to the page, interact with the UI, and confirm changes work.
Stop Condition
When all stories have passes: true , Ralph outputs <promise>COMPLETE</promise> and the loop exits.
Debugging
Check current state:
# See which stories are done
cat prd.json | jq ' .userStories[] | {id, title, passes} '
# See learnings from previous iterations
cat progress.txt
# Check git history
git log --oneline -10
Customizing the Prompt
After copying prompt.md (for Amp) or CLAUDE.md (for Claude Code) to your project, customize it for your project:
Add project-specific quality check commands
Include codebase conventions
Add common gotchas for your stack
Archiving
Ralph automatically archives previous runs when you start a new feature (different branchName ). Archives are saved to archive/YYYY-MM-DD-feature-name/ .
References
Geoffrey Huntley's Ralph article
Amp documentation
Claude Code documentation
About
Ralph is an autonomous AI agent loop that runs repeatedly until all PRD items are complete.
x.com/ryancarson/status/2008548371712135632
Resources
Readme
License
MIT license
Uh oh!
There was an error while loading. Please reload this page .
Activity
Stars
13.5k
stars
Watchers
91
watching
Forks
1.4k
forks
Report repository
Releases
No releases published
Packages
0
Uh oh!
There was an error while loading. Please reload this page .
Contributors
5
Languages
TypeScript
62.9%
Shell
17.6%
CSS
14.6%
JavaScript
3.1%
HTML
1.8%
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
- runtime_article_bundle_path: research/articles/art-2026-03-01-030.md
- runtime_source_snapshot_json: research/source-material/art-2026-03-01-030.json
- runtime_source_snapshot_text: research/source-material/art-2026-03-01-030.txt
- runtime_filter_state: pending
- runtime_last_stage: intake
- refreshed_live_source: false
