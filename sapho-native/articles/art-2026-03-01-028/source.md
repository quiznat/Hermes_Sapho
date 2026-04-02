---
version: source-capture.v1
article_id: art-2026-03-01-028
ticket_id: ticket-import-art-2026-03-01-028
source_url: https://github.com/EveryInc/compound-engineering-plugin
canonical_url: https://github.com/EveryInc/compound-engineering-plugin
source_title: "GitHub - EveryInc/compound-engineering-plugin: Official Claude Code\
  \ compound engineering plugin \xB7 GitHub"
capture_kind: runtime-import
http_status: 200
content_type: text/html
captured_at_utc: '2026-03-22T18:24:58Z'
---
# Source Capture

## Title

GitHub - EveryInc/compound-engineering-plugin: Official Claude Code compound engineering plugin · GitHub

## Body

GitHub - EveryInc/compound-engineering-plugin: Official Claude Code compound engineering plugin · GitHub
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
EveryInc
/
compound-engineering-plugin
Public
Notifications
You must be signed in to change notification settings
Fork
861
Star
10.8k
Code
Issues
39
Pull requests
14
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
EveryInc/compound-engineering-plugin
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
471 Commits
471 Commits
.claude-plugin
.claude-plugin
.claude/ commands
.claude/ commands
.cursor-plugin
.cursor-plugin
.github
.github
docs
docs
plugins
plugins
scripts/ release
scripts/ release
src
src
tests
tests
.gitignore
.gitignore
AGENTS.md
AGENTS.md
CHANGELOG.md
CHANGELOG.md
CLAUDE.md
CLAUDE.md
LICENSE
LICENSE
PRIVACY.md
PRIVACY.md
README.md
README.md
SECURITY.md
SECURITY.md
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
Security
Compound Marketplace
A Claude Code plugin marketplace featuring the Compound Engineering Plugin — tools that make each unit of engineering work easier than the last.
Claude Code Install
/plugin marketplace add EveryInc/compound-engineering-plugin
/plugin install compound-engineering
Cursor Install
/add-plugin compound-engineering
OpenCode, Codex, Droid, Pi, Gemini, Copilot, Kiro, Windsurf, OpenClaw & Qwen (experimental) Install
This repo includes a Bun/TypeScript CLI that converts Claude Code plugins to OpenCode, Codex, Factory Droid, Pi, Gemini CLI, GitHub Copilot, Kiro CLI, Windsurf, OpenClaw, and Qwen Code.
# convert the compound-engineering plugin into OpenCode format
bunx @every-env/compound-plugin install compound-engineering --to opencode
# convert to Codex format
bunx @every-env/compound-plugin install compound-engineering --to codex
# convert to Factory Droid format
bunx @every-env/compound-plugin install compound-engineering --to droid
# convert to Pi format
bunx @every-env/compound-plugin install compound-engineering --to pi
# convert to Gemini CLI format
bunx @every-env/compound-plugin install compound-engineering --to gemini
# convert to GitHub Copilot format
bunx @every-env/compound-plugin install compound-engineering --to copilot
# convert to Kiro CLI format
bunx @every-env/compound-plugin install compound-engineering --to kiro
# convert to OpenClaw format
bunx @every-env/compound-plugin install compound-engineering --to openclaw
# convert to Windsurf format (global scope by default)
bunx @every-env/compound-plugin install compound-engineering --to windsurf
# convert to Windsurf workspace scope
bunx @every-env/compound-plugin install compound-engineering --to windsurf --scope workspace
# convert to Qwen Code format
bunx @every-env/compound-plugin install compound-engineering --to qwen
# auto-detect installed tools and install to all
bunx @every-env/compound-plugin install compound-engineering --to all
Local Development
When developing and testing local changes to the plugin:
Claude Code — add a shell alias so your local copy loads alongside your normal plugins:
# add to ~/.zshrc or ~/.bashrc
alias claude-dev-ce= ' claude --plugin-dir ~/code/compound-engineering-plugin/plugins/compound-engineering '
One-liner to append it:
echo " alias claude-dev-ce='claude --plugin-dir ~/code/compound-engineering-plugin/plugins/compound-engineering' " >> ~ /.zshrc
Then run claude-dev-ce instead of claude to test your changes. Your production install stays untouched.
Codex — point the install command at your local path:
bun run src/index.ts install ./plugins/compound-engineering --to codex
Other targets — same pattern, swap the target:
bun run src/index.ts install ./plugins/compound-engineering --to opencode
Output format details per target
Target
Output path
Notes
opencode
~/.config/opencode/
Commands as .md files; opencode.json MCP config deep-merged; backups made before overwriting
codex
~/.codex/prompts + ~/.codex/skills
Claude commands become prompt + skill pairs; canonical ce:* workflow skills also get prompt wrappers; deprecated workflows:* aliases are omitted
droid
~/.factory/
Tool names mapped ( Bash → Execute , Write → Create ); namespace prefixes stripped
pi
~/.pi/agent/
Prompts, skills, extensions, and mcporter.json for MCPorter interoperability
gemini
.gemini/
Skills from agents; commands as .toml ; namespaced commands become directories ( workflows:plan → commands/workflows/plan.toml )
copilot
.github/
Agents as .agent.md with Copilot frontmatter; MCP env vars prefixed with COPILOT_MCP_
kiro
.kiro/
Agents as JSON configs + prompt .md files; only stdio MCP servers supported
openclaw
~/.openclaw/extensions/<plugin>/
Entry-point TypeScript skill file; openclaw-extension.json for MCP servers
windsurf
~/.codeium/windsurf/ (global) or .windsurf/ (workspace)
Agents become skills; commands become flat workflows; mcp_config.json merged
qwen
~/.qwen/extensions/<plugin>/
Agents as .yaml ; env vars with placeholders extracted as settings; colon separator for nested commands
All provider targets are experimental and may change as the formats evolve.
Sync Personal Config
Sync your personal Claude Code config ( ~/.claude/ ) to other AI coding tools. Omit --target to sync to all detected supported tools automatically:
# Sync to all detected tools (default)
bunx @every-env/compound-plugin sync
# Sync skills and MCP servers to OpenCode
bunx @every-env/compound-plugin sync --target opencode
# Sync to Codex
bunx @every-env/compound-plugin sync --target codex
# Sync to Pi
bunx @every-env/compound-plugin sync --target pi
# Sync to Droid
bunx @every-env/compound-plugin sync --target droid
# Sync to GitHub Copilot (skills + MCP servers)
bunx @every-env/compound-plugin sync --target copilot
# Sync to Gemini (skills + MCP servers)
bunx @every-env/compound-plugin sync --target gemini
# Sync to Windsurf
bunx @every-env/compound-plugin sync --target windsurf
# Sync to Kiro
bunx @every-env/compound-plugin sync --target kiro
# Sync to Qwen
bunx @every-env/compound-plugin sync --target qwen
# Sync to OpenClaw (skills only; MCP is validation-gated)
bunx @every-env/compound-plugin sync --target openclaw
# Sync to all detected tools
bunx @every-env/compound-plugin sync --target all
This syncs:
Personal skills from ~/.claude/skills/ (as symlinks)
Personal slash commands from ~/.claude/commands/ (as provider-native prompts, workflows, or converted skills where supported)
MCP servers from ~/.claude/settings.json
Skills are symlinked (not copied) so changes in Claude Code are reflected immediately.
Supported sync targets:
opencode
codex
pi
droid
copilot
gemini
windsurf
kiro
qwen
openclaw
Notes:
Codex sync preserves non-managed config.toml content and now includes remote MCP servers.
Command sync reuses each provider's existing Claude command conversion, so some targets receive prompts or workflows while others receive converted skills.
Copilot sync writes personal skills to ~/.copilot/skills/ and MCP config to ~/.copilot/mcp-config.json .
Gemini sync writes MCP config to ~/.gemini/ and avoids mirroring skills that Gemini already discovers from ~/.agents/skills , which prevents duplicate-skill warnings.
Droid, Windsurf, Kiro, and Qwen sync merge MCP servers into the provider's documented user config.
OpenClaw currently syncs skills only. Personal command sync is skipped because this repo does not yet have a documented user-level OpenClaw command surface, and MCP sync is skipped because the current official OpenClaw docs do not clearly document an MCP server config contract.
Workflow
Brainstorm → Plan → Work → Review → Compound → Repeat
↑
Ideate (optional — when you need ideas)
Command
Purpose
/ce:ideate
Discover high-impact project improvements through divergent ideation and adversarial filtering
/ce:brainstorm
Explore requirements and approaches before planning
/ce:plan
Turn feature ideas into detailed implementation plans
/ce:work
Execute plans with worktrees and task tracking
/ce:review
Multi-agent code review before merging
/ce:compound
Document learnings to make future work easier
The /ce:ideate skill proactively surfaces strong improvement ideas, and /ce:brainstorm then clarifies the selected one before committing to a plan.
Each cycle compounds: brainstorms sharpen plans, plans inform future plans, reviews catch more issues, patterns get documented.
Beta: Experimental versions of /ce:plan and /deepen-plan are available as /ce:plan-beta and /deepen-plan-beta . See the plugin README for details.
Philosophy
Each unit of engineering work should make subsequent units easier—not harder.
Traditional development accumulates technical debt. Every feature adds complexity. The codebase becomes harder to work with over time.
Compound engineering inverts this. 80% is in planning and review, 20% is in execution:
Plan thoroughly before writing code
Review to catch issues and capture learnings
Codify knowledge so it's reusable
Keep quality high so future changes are easy
Learn More
Full component reference - all agents, commands, skills
Compound engineering: how Every codes with agents
The story behind compounding engineering
About
Official Claude Code compound engineering plugin
every.to/guides/compound-engineering
Topics
engineering
compound
Resources
Readme
License
MIT license
Security policy
Security policy
Uh oh!
There was an error while loading. Please reload this page .
Activity
Custom properties
Stars
10.8k
stars
Watchers
82
watching
Forks
861
forks
Report repository
Releases
53
compound-engineering: v2.49.0
Latest
Mar 22, 2026
+ 52 releases
Packages
0
Uh oh!
There was an error while loading. Please reload this page .
Contributors
45
+ 31 contributors
Languages
TypeScript
81.2%
Python
7.5%
JavaScript
4.0%
Shell
4.0%
Ruby
3.3%
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
- runtime_article_bundle_path: research/articles/art-2026-03-01-028.md
- runtime_source_snapshot_json: research/source-material/art-2026-03-01-028.json
- runtime_source_snapshot_text: research/source-material/art-2026-03-01-028.txt
- runtime_filter_state: pending
- runtime_last_stage: intake
- refreshed_live_source: false
