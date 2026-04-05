---
version: source-capture.v1
article_id: art-2026-03-08-006
ticket_id: ticket-import-art-2026-03-08-006
source_url: https://github.com/boqiny/memory-probe
canonical_url: https://github.com/boqiny/memory-probe
source_title: "GitHub - boqiny/memory-probe: Diagnosing Retrieval vs. Utilization\
  \ Bottlenecks in LLM Agent Memory https://arxiv.org/abs/2603.02473 \xB7 GitHub"
capture_kind: runtime-import
http_status: 200
content_type: text/html
captured_at_utc: '2026-03-08T08:30:59Z'
---
# Source Capture

## Title

GitHub - boqiny/memory-probe: Diagnosing Retrieval vs. Utilization Bottlenecks in LLM Agent Memory https://arxiv.org/abs/2603.02473 · GitHub

## Body

GitHub - boqiny/memory-probe: Diagnosing Retrieval vs. Utilization Bottlenecks in LLM Agent Memory https://arxiv.org/abs/2603.02473 · GitHub
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
boqiny
/
memory-probe
Public
Notifications
You must be signed in to change notification settings
Fork
1
Star
8
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
boqiny/memory-probe
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
2 Commits
2 Commits
configs
configs
data
data
probes
probes
retrieval
retrieval
strategies
strategies
.gitignore
.gitignore
README.md
README.md
compute_metrics.py
compute_metrics.py
data_loader.py
data_loader.py
llm_client.py
llm_client.py
memory_store.py
memory_store.py
qa_engine.py
qa_engine.py
requirements.txt
requirements.txt
run_experiment.py
run_experiment.py
visualize_results.py
visualize_results.py
View all files
Repository files navigation
README
Memory Probe
📄 Paper: Diagnosing Retrieval vs. Utilization Bottlenecks in LLM Agent Memory
Diagnostic framework that tests whether LLM memory agents actually use their retrieved memories. Evaluates three memory strategies on the LOCOMO dataset using LLM-as-judge probes for retrieval relevance, memory utilization, and failure analysis.
Strategies
Default RAG — stores raw conversation chunks (3 turns each), no LLM at write time
Extracted Facts — LLM extracts structured facts per session with conflict resolution (A-MEM / Mem0 style)
Summarized Episodes — LLM summarizes each session into one entry (MemGPT style)
Setup
pip install -r requirements.txt
export OPENAI_API_KEY=your_key_here
Usage
# Pilot run (5 questions, 1 strategy)
python run_experiment.py --pilot --strategy basic_rag
# Full experiment (all strategies, all conversations)
python run_experiment.py
# Top-k ablation
python run_experiment.py --top-k 3 5 10
# Single strategy with custom workers
python run_experiment.py --strategy extracted_facts --workers 10
# Analyze results
python analyze_results.py results/results_TIMESTAMP.json
Citation
If you use this work in your research, please cite:
@misc { yuan2026diagnosingretrievalvsutilization ,
title = { Diagnosing Retrieval vs. Utilization Bottlenecks in LLM Agent Memory } ,
author = { Boqin Yuan and Yue Su and Kun Yao } ,
year = { 2026 } ,
eprint = { 2603.02473 } ,
archivePrefix = { arXiv } ,
primaryClass = { cs.AI } ,
url = { https://arxiv.org/abs/2603.02473 } ,
}
About
Diagnosing Retrieval vs. Utilization Bottlenecks in LLM Agent Memory https://arxiv.org/abs/2603.02473
Resources
Readme
Uh oh!
There was an error while loading. Please reload this page .
Activity
Stars
8
stars
Watchers
0
watching
Forks
1
fork
Report repository
Releases
No releases published
Packages
0
Uh oh!
There was an error while loading. Please reload this page .
Contributors
1
boqiny
Boqin Yuan
Languages
Python
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
- runtime_article_bundle_path: research/articles/art-2026-03-08-006.md
- runtime_source_snapshot_json: research/source-material/art-2026-03-08-006.json
- runtime_source_snapshot_text: research/source-material/art-2026-03-08-006.txt
- runtime_filter_state: pending
- runtime_last_stage: facts
- refreshed_live_source: false
