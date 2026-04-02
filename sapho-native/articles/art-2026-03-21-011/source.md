---
version: source-capture.v1
article_id: art-2026-03-21-011
ticket_id: ticket-import-art-2026-03-21-011
source_url: https://github.com/handrew/agentic_gpt
canonical_url: https://github.com/handrew/agentic_gpt
source_title: "GitHub - handrew/agentic_gpt: WIP: Modular, reliable, reproducible\
  \ LLM agents \xB7 GitHub"
capture_kind: runtime-import
http_status: 200
content_type: text/html
captured_at_utc: '2026-03-21T22:51:35Z'
---
# Source Capture

## Title

GitHub - handrew/agentic_gpt: WIP: Modular, reliable, reproducible LLM agents · GitHub

## Body

GitHub - handrew/agentic_gpt: WIP: Modular, reliable, reproducible LLM agents · GitHub
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
handrew
/
agentic_gpt
Public
Notifications
You must be signed in to change notification settings
Fork
1
Star
4
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
handrew/agentic_gpt
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
77 Commits
77 Commits
agentic_gpt
agentic_gpt
docs
docs
examples
examples
.gitignore
.gitignore
readme.md
readme.md
requirements.txt
requirements.txt
View all files
Repository files navigation
README
🪽 AgenticGPT
Nascent AGI architectures like BabyAGI and AutoGPT have captured a great deal of public interest by demonstrating LLMs' agentic capabilities and capacity for introspective step-by-step reasoning. As proofs-of-concept, they make great strides, but a few things wanting.
The primary contributions I would like to make are twofold:
Allowing an LLM to read from a corpus of information and act according to that information.
Enabling more robust reproducibility and modularity.
Conceptually, the user provides the AgenticGPT agent with an objective and a list of Action s that it can take, and then the agent figures out the rest, and asks the user for clarification when it needs help.
🏛️ Registry
You can contribute or use agents built on top of AgenticGPT in the registry . Right now the following AgenticGPT -based agents exist.
PlaywrightAgent : Uses AgenticGPT to automate browser actions.
🎬 Getting Started
🔨 Installation
pip install -r requirements.txt
Set up your OpenAI API key as the OPENAI_API_KEY environment variable.
🦭 Usage
AgenticGPT can be instantiated with the following signature:
AgenticGPT (
objective ,
actions_available = [],
memory_dict = {},
model = "gpt-3.5-turbo" ,
embedding_model = "text-embedding-ada-002" ,
ask_user_fn = ask_user_to_clarify ,
max_steps = 100 ,
verbose = False ,
)
All you have to do is give it a string objective , define a list of Action s, and optionally give it a memory_dict of name to text for it to remember. The agent is equipped with a few Action s by default, such as being able to ask you for clarification if necessary, and a memory which it can query to help achieve its objectives.
See some examples . TODO: If you want to run the examples, you have to move them into the root folder and then run python <example_file>.py .
🏃🏽 Creating actions and running
Example:
"""Example of using AgenticGPT to make a folder on the filesystem.
Also demonstrates how to ask the user for input and use it in the agent's
thoughts."""
import os
from agentic_gpt . agent import AgenticGPT
from agentic_gpt . agent . action import Action
def mkdir ( folder ):
os . mkdir ( folder )
actions = [
Action (
name = "mkdir" , description = "Make a folder on the filesystem." , function = mkdir
)
]
agent = AgenticGPT (
"Ask the user what folder they want to make and make it for them." ,
actions_available = actions ,
)
agent . run ()
Action s are instantiated with a name , description , and function . The name , description , and function signature are then injected into the agent prompt to tell them what they can do. Action results are stored in context as variables, unless a dict answer is given with {"context": } which sets the context accordingly.
♻️ Reusing saved routines
You can then save the steps that the LLM generated using
agent . save_actions_taken ( "mkdir.json" )
and reuse it using:
agent = AgenticGPT (
"Ask the user what folder they want to make and make it for them." ,
actions_available = actions ,
)
agent . from_saved_actions ( "mkdir.json" )
agent . replay ()
⚜️ Design
See request for comment for the original motivation for and considerations around building this.
TODO, add a diagram and explanation
🤔 Thoughts while building
I took some notes while building this project to document some of my thoughts on working with and taming LLMs . If you're curious about the development journey (and maybe some prompt engineering secret sauce), check out the linked journal.
🧱 TODO
Memory instantiation and routing of queries.
Add "query memory" and "add to memory" default functions.
Save and load routine to file.
Write some initial docs. Be sure to add emojis because people can't get enough emojis.
Create and document examples. Start setting up a library of actions.
Support sentencetransformers and gpt-4.
Don't make it incumbent on the user to make Actions return a context.
Figure out a more modular way to solicit the user for feedback, maybe a default ask_user_to_clarify hook.
Retry when there is an error.
Create logic to condense context window if you get an error from the API.
Create chatbot mode where it stops after every step and asks you how it's doing.
Make some diagrams describing the architecture.
Put on pypi.
Test Memory functions: adding a document, querying all, loading document.
🚨 Disclaimer
Be careful what tools you expose to the agent, because it is running autonomously.
Be careful what data you expose to the agent, because it may be processed by the LLM APIs under the hood.
About
WIP: Modular, reliable, reproducible LLM agents
Resources
Readme
Uh oh!
There was an error while loading. Please reload this page .
Activity
Stars
4
stars
Watchers
3
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
Uh oh!
There was an error while loading. Please reload this page .
Contributors
Uh oh!
There was an error while loading. Please reload this page .
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
- runtime_article_bundle_path: research/articles/art-2026-03-21-011.md
- runtime_source_snapshot_json: research/source-material/art-2026-03-21-011.json
- runtime_source_snapshot_text: research/source-material/art-2026-03-21-011.txt
- runtime_filter_state: pending
- runtime_last_stage: facts
