---
version: source-capture.v1
article_id: art-2026-03-01-029
ticket_id: ticket-import-art-2026-03-01-029
source_url: https://github.com/snarktank/compound-product
canonical_url: https://github.com/snarktank/compound-product
source_title: "GitHub - snarktank/compound-product: A self-improving product system\
  \ that reads reports, identifies priorities, and autonomously implements fixes \xB7\
  \ GitHub"
capture_kind: runtime-import
http_status: 200
content_type: text/html
captured_at_utc: '2026-03-22T18:24:58Z'
---
# Source Capture

## Title

GitHub - snarktank/compound-product: A self-improving product system that reads reports, identifies priorities, and autonomously implements fixes · GitHub

## Body

GitHub - snarktank/compound-product: A self-improving product system that reads reports, identifies priorities, and autonomously implements fixes · GitHub
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
compound-product
Public
Notifications
You must be signed in to change notification settings
Fork
53
Star
501
Code
Issues
0
Pull requests
0
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
snarktank/compound-product
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
33 Commits
33 Commits
examples
examples
scripts
scripts
skills
skills
.gitignore
.gitignore
AGENTS.md
AGENTS.md
README.md
README.md
config.example.json
config.example.json
install.sh
install.sh
View all files
Repository files navigation
README
Compound Product
A self-improving product system that reads daily reports, identifies the #1 actionable priority, and autonomously implements it.
The concept: Your product generates reports about its performance. An AI agent analyzes those reports, picks the most impactful fix, creates a plan, and implements it—all while you sleep. You wake up to a PR ready for review.
Built on Kieran Klaassen's Compound Engineering methodology, Geoffrey Huntley's Ralph pattern , and Ryan Carson's implementation .
How It Works
flowchart TD
subgraph "Phase 0: Your System"
GEN[Generate Daily Report<br/>your code, cron, etc.]
GEN --> R[📊 reports/*.md<br/>metrics, errors, feedback]
end
subgraph "Phase 1: Analysis"
A[analyze-report.sh<br/>LLM API]
R --> A
A --> J[analysis.json<br/>priority + criteria]
end
subgraph "Phase 2: Planning"
B[Create Branch<br/>compound/feature-name]
J --> B
B --> PRD[AI Agent<br/>Load prd skill]
PRD --> MD[tasks/prd-feature.md]
MD --> TASKS[AI Agent<br/>Load tasks skill]
TASKS --> JSON[prd.json<br/>executable tasks]
end
subgraph "Phase 3: Execution Loop"
LOOP[loop.sh<br/>max N iterations]
JSON --> LOOP
LOOP --> PICK[Pick next task<br/>where passes: false]
PICK --> IMPL[AI Agent<br/>Implement task]
IMPL --> CHECK{Quality<br/>Checks?}
CHECK -->|Pass| COMMIT[Git Commit]
CHECK -->|Fail| FIX[Fix & Retry]
FIX --> CHECK
COMMIT --> UPDATE[Update prd.json<br/>passes: true]
UPDATE --> DONE{All tasks<br/>done?}
DONE -->|No| PICK
DONE -->|Yes| EXIT[Exit loop]
end
subgraph Output
EXIT --> PUSH[Git Push]
PUSH --> PR[🎉 Pull Request<br/>Ready for review]
end
click A "https://github.com/snarktank/compound-product/blob/main/scripts/analyze-report.sh" "View analyze-report.sh"
click LOOP "https://github.com/snarktank/compound-product/blob/main/scripts/loop.sh" "View loop.sh"
click PRD "https://github.com/snarktank/compound-product/blob/main/skills/prd/SKILL.md" "View PRD skill"
click TASKS "https://github.com/snarktank/compound-product/blob/main/skills/tasks/SKILL.md" "View Tasks skill"
Loading
Quick Start
Prerequisites
Amp CLI or Claude Code
agent-browser for browser-based testing ( npm install -g agent-browser )
jq installed ( brew install jq on macOS)
gh CLI installed and authenticated ( brew install gh )
One of these LLM providers configured:
Anthropic: export ANTHROPIC_API_KEY=sk-ant-...
OpenRouter: export OPENROUTER_API_KEY=sk-or-...
AI Gateway: export AI_GATEWAY_URL=https://... AI_GATEWAY_API_KEY=...
Installation
Compound Product installs into your existing project repository. It adds scripts and configuration that work alongside your codebase.
# Clone compound-product somewhere temporary
git clone https://github.com/snarktank/compound-product.git
cd compound-product
# Install into your project
./install.sh /path/to/your/project
Or tell your AI agent (from within your project):
Install compound-product from https://github.com/snarktank/compound-product into this repo
This creates:
scripts/compound/ - The automation scripts
compound.config.json - Configuration for your project
reports/ - Directory for your daily reports (you provide these)
Configuration
Copy and customize the config:
cp config.example.json config.json
Edit config.json :
{
"tool" : " amp " ,
"reportsDir" : " ./reports " ,
"outputDir" : " ./compound " ,
"qualityChecks" : [ " npm run typecheck " , " npm test " ],
"maxIterations" : 25 ,
"branchPrefix" : " compound/ "
}
Running
# Dry run - see what it would do
./scripts/compound/auto-compound.sh --dry-run
# Full run
./scripts/compound/auto-compound.sh
# Just run the loop (if you already have prd.json)
./scripts/compound/loop.sh 10
Report Format
Your report can be any markdown file. The AI will analyze it and pick the #1 actionable item.
Example report structure:
# Daily Report - 2024-01-15
## Key Metrics
- Signups: 45 (down 20% from yesterday)
- Errors: 12 TypeErrors in checkout flow
- User feedback: "Can't find the save button"
## Issues
1 . Checkout flow has JavaScript errors
2 . Save button is below the fold on mobile
3 . Email validation is too strict
## Recommendations
- Fix checkout JavaScript errors (blocking revenue)
- Move save button above fold
- Relax email validation
The Loop
Each iteration of the loop:
Reads prd.json to find the next task where passes: false
Implements the task
Runs quality checks (configurable in config.json )
Commits if checks pass
Updates prd.json to mark task as passes: true
Appends learnings to progress.txt
Repeats until all tasks complete or max iterations reached
Memory Between Iterations
Each iteration runs with fresh context. Memory persists via:
Git history - Previous commits show what was done
progress.txt - Learnings and patterns discovered
prd.json - Which tasks are complete
AGENTS.md - Long-term codebase knowledge (updated by agents)
Skills
Two skills are included for PRD creation and task generation:
PRD Skill
Creates a Product Requirements Document from a feature description.
Load the prd skill. Create a PRD for [your feature]
Tasks Skill
Converts a PRD markdown file to prd.json with granular, machine-verifiable tasks .
Key features:
Generates 8-15 small tasks (not 3-5 large ones)
Each acceptance criterion is boolean pass/fail
Browser tests use agent-browser commands
Investigation and implementation are separate tasks
Load the tasks skill. Convert tasks/prd-feature.md to prd.json
Customization
Custom Analysis Script
By default, analyze-report.sh uses the Anthropic API directly. To use your own:
{
"analyzeCommand" : " npx tsx ./my-custom-analyze.ts "
}
Your script must output JSON to stdout:
{
"priority_item" : " Fix checkout errors " ,
"description" : " ... " ,
"rationale" : " ... " ,
"acceptance_criteria" : [ " ... " , " ... " ],
"branch_name" : " compound/fix-checkout-errors "
}
Quality Checks
Configure your project's quality checks:
{
"qualityChecks" : [
" npm run typecheck " ,
" npm run lint " ,
" npm test "
]
}
Branch Prefix
All branches are created with a prefix:
{
"branchPrefix" : " compound/ "
}
⚠️ Security Considerations
This tool runs AI agents with elevated permissions. Understand the risks before using:
What the agents can do
Read and modify any file in your repository
Execute shell commands (build, test, git operations)
Make network requests (API calls, git push)
Create branches and PRs in your repository
Safeguards in place
PRs, not direct merges - All changes go through pull requests for human review
Quality checks - Configurable checks run before commits
Max iterations - The loop stops after N iterations to prevent runaway execution
Dry run mode - Test the analysis phase without making changes
Recommendations
Review PRs carefully before merging
Run in a separate environment (VM, container) if concerned about file access
Use API keys with limited scope where possible
Don't use on production branches - always target a feature branch
Monitor the first few runs to understand behavior
The --dangerously-allow-all flag
The scripts use --dangerously-allow-all (Amp) and --dangerously-skip-permissions (Claude Code) to allow autonomous operation. This means the agent bypasses normal confirmation prompts. This is intentional for automation but means you're trusting the agent to make good decisions.
Philosophy
Compound Product is based on the idea that each improvement should make future improvements easier:
Agents update AGENTS.md - Discovered patterns are documented for future iterations
Progress is logged - Each task records what was learned
Small tasks compound - Many small, correct changes beat large, risky ones
Human review remains - The loop creates PRs, not direct merges
Scheduling (macOS launchd)
To run Compound Product automatically (e.g., every night), use macOS launchd:
# Copy the example plist
cp examples/com.compound.plist.example ~ /Library/LaunchAgents/com.compound.myproject.plist
# Edit it with your project path and username
nano ~ /Library/LaunchAgents/com.compound.myproject.plist
# Load it
launchctl load ~ /Library/LaunchAgents/com.compound.myproject.plist
# Check status (last column is exit code, 0 = success)
launchctl list | grep compound
Important: PATH configuration
launchd runs with a minimal PATH. You must include the directories where your tools are installed:
# Find where your CLI is installed
which amp # e.g., /Users/you/.npm-global/bin/amp
which claude # e.g., /opt/homebrew/bin/claude
Update the PATH in your plist to include these directories. The example plist includes common locations.
Troubleshooting launchd:
# Check logs
tail -f /path/to/your/project/logs/compound.log
# Unload and reload
launchctl unload ~ /Library/LaunchAgents/com.compound.myproject.plist
launchctl load ~ /Library/LaunchAgents/com.compound.myproject.plist
# Test manually (should produce same result as launchd)
/bin/bash -c ' cd /path/to/project && ./scripts/compound/auto-compound.sh --dry-run '
Troubleshooting
Loop exits early
Check progress.txt for errors. Common issues:
Quality checks failing (fix the code or adjust checks)
Task too large (split into smaller tasks)
Context overflow (task description needs to be more focused)
Analysis fails
Ensure one of these LLM providers is configured:
# Option 1: Anthropic API
export ANTHROPIC_API_KEY=sk-ant-...
# Option 2: OpenRouter
export OPENROUTER_API_KEY=sk-or-...
# Option 3: AI Gateway (any OpenAI-compatible endpoint)
export AI_GATEWAY_URL=https://your-gateway.com/v1
export AI_GATEWAY_API_KEY=your-key
export AI_GATEWAY_MODEL=claude-sonnet-4-20250514 # optional
Agent can't find tools
For Amp, ensure skills are installed:
ls ~ /.config/amp/skills/
For Claude Code:
ls ~ /.claude/skills/
Contributing
PRs welcome! Please keep changes focused and include tests where applicable.
License
MIT
About
A self-improving product system that reads reports, identifies priorities, and autonomously implements fixes
Resources
Readme
Uh oh!
There was an error while loading. Please reload this page .
Activity
Stars
501
stars
Watchers
1
watching
Forks
53
forks
Report repository
Releases
No releases published
Packages
0
Uh oh!
There was an error while loading. Please reload this page .
Contributors
Uh oh!
There was an error while loading. Please reload this page .
Languages
Shell
100.0%
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
- runtime_article_bundle_path: research/articles/art-2026-03-01-029.md
- runtime_source_snapshot_json: research/source-material/art-2026-03-01-029.json
- runtime_source_snapshot_text: research/source-material/art-2026-03-01-029.txt
- runtime_filter_state: pending
- runtime_last_stage: intake
- refreshed_live_source: false
