---
version: source-capture.v1
article_id: art-2026-03-21-025
ticket_id: ticket-import-art-2026-03-21-025
source_url: https://news.ycombinator.com/item?id=46934107
canonical_url: https://news.ycombinator.com/item?id=46934107
source_title: GitHub Agentic Workflows | Hacker News
capture_kind: runtime-import
http_status: 200
content_type: text/html
captured_at_utc: '2026-03-23T01:11:29Z'
---
# Source Capture

## Title

GitHub Agentic Workflows | Hacker News

## Body

GitHub Agentic Workflows | Hacker News
Hacker News new | past | comments | ask | show | jobs | submit
login
GitHub Agentic Workflows ( github.github.io )
302 points by mooreds 41 days ago | hide | past | favorite | 142 comments
onionisafruit 41 days ago | next [–]
I noticed this unusual line in go.mod and got curious why it is using replace for this (typically you would `go get github.com/Masterminds/semver/v3@v3.4.0` instead). replace github.com/Masterminds/semver/v3 => github.com/Masterminds/semver/v3 v3.4.0
I found this very questionable PR[0]. It appears to have been triggered by dependabot creating an issue for a version upgrade -- which is probably unnecessary to begin with. The copilot agent then implemented that by adding a replace statement, which is not how you are supposed to do this. It also included some seemingly-unrelated changes. The copilot reviewer called out the unrelated changes, but the human maintainer apparently didn't notice and merged anyway. There is just so much going wrong here. [0] https://github.com/github/gh-aw/pull/4469
spankalee 41 days ago | parent | next [–]
This happens with all agents I've used and package.json files for npm. Instead of using `npm i foo` the agent string-edits package.json and hallucinates some version to install. Usually it's a kind of ok version, but it's not how I would like this to work. It's worse with renaming things in code. I've yet to see an agent be able to use refactoring tools (if they even exist in VS Code) instead of brute-forcing renames with string replacement or sed. Agents use edit -> build -> read errors -> repeat, instead of using a reliable tool, and it burns a lot more GPU...
embedding-shape 41 days ago | root | parent | next [–]
> This happens with all agents I've used and package.json files for npm. Instead of using `npm i foo` the agent string-edits package.json and hallucinates some version to install. When using codex, I usually have something like `Never add 3rd party libraries unless explicitly requested. When adding new libraries, use `cargo add $crate` without specifying the version, so we get the latest version.` and it seems to make this issue not appear at all.
teaearlgraycold 41 days ago | root | parent | next [–]
Eventually this specific issue will be RLHF’d out of existence. For now that should mostly solve the problem, but these models aren’t perfect at following instructions. Especially when you’re deep into the context window.
girvo 41 days ago | root | parent | next [–]
> Especially when you’re deep into the context window. Though that is, at least to me, a bit of an anti-pattern for exactly that reason. I've found it far more successful to blow away the context and restart with a new prompt from the old context instead of having a very long running back-and-forward. Its better than it was with the latest models, I can have them stick around longer, but it's still a useful pattern to use even with 4.6/5.3
teaearlgraycold 41 days ago | root | parent | next [–]
Opus has also clearly been trained to clear the context fairly often through the plan/code/plan cycle.
catlifeonmars 40 days ago | root | parent | next [–]
Is it training, or prompting from the CLI?
root_axis 41 days ago | root | parent | prev | next [–]
> brute-forcing renames with string replacement That's their strategy for everything the training data can't solve. This is the main reason the autonomous agent swarm approach doesn't work for me. 20 bucks in tokens just obliterated with 5 agents exchanging hallucinations with each-other. It's way too easy for them to amplify each other's mistakes without a human to intervene.
richardw 41 days ago | root | parent | prev | next [–]
Totally. Surely the IDE’s like antigravity are meant to give the LLM more tools to use for eg refactoring or dependency management? I haven’t used it but seems a quick win to move from token generation to deterministic tool use.
port11 41 days ago | root | parent | next [–]
As if. I’ve had Gemini stuck on AG because it couldn’t figure out how to use only one version of React. I managed to detect that the build failed because 2 versions of React were being used, but it kept saying “I’ll remove React version N”, and then proceeding to add a new dependency of the latest version. Loops and loops of this. On a similar note AG really wants to parse code with weird grep commands that don’t make any sense given the directory context.
avereveard 41 days ago | root | parent | prev | next [–]
Worse still I created a mcp with refactoring tools and symbol based editing but because it's a) of of distribution for llm b) agent get their own heavy handed system prompts all the goodies get ignored
threecheese 41 days ago | root | parent | prev | next [–]
For the first, I think maintaining package-add instructions is table stakes, we need to be opinionated here. Agents are typically good at following them, if not you can fall over to a Makefile that does everything. For the second, I totally agree. I continue to hope that agents will get better at refactoring, and I think using LSPs effectively would make this happen. Claude took dozens of minutes to perform a rename which Jetbrains would have executed perfectly in like five seconds. Its approach was to make a change, run the tests, do it again. Nuts.
catlifeonmars 40 days ago | root | parent | next [–]
Does the agent have a way to interact with the lsp?
onionisafruit 40 days ago | root | parent | next [–]
I don’t know about other lsps, but gopls has an -mcp flag that makes it run an mcp server. There’s also a jetbrains plugin for claude that gives claude the ability to use a subset of your jetbrains IDE’s features. I usually have both of those configured when using claude on Go repos, and I still have the same frustrations as the comments above. Gopls has symbol search, but claude almost always uses grep to find uses instead.
catlifeonmars 39 days ago | root | parent | next [–]
Didn’t know about the go lsp builtin mcp server. That’s neat! Does preventing the agent from using a shell help at all with the grep issue?
bakibab 41 days ago | parent | prev | next [–]
They are trying to fix it using this comment but cancelled mid way. Not sure why. https://github.com/github/gh-aw/pull/14548
onionisafruit 41 days ago | root | parent | next [–]
Ha, they used my comment in the prompt. I love it.
resquawk 41 days ago | root | parent | next [–]
Thanks! We fixed this in another PR. Appreciate the feedback
awesome_dude 41 days ago | parent | prev | next [–]
This is more evidence of my core complaint with AI (and why it's not AGI at this point) The AI hasn't understood what's going on, instead it has pattern matched strings and used those patterns to create new strings that /look/ right, but fail upon inspection. (The human involved is also failing my Turing test... )
gloosx 41 days ago | parent | prev | next [–]
I like how it accumulated 3 such replacements before finally getting fixed as a reaction to this comment with PR 14543[0], but after review, two "fix unit tests" commits were added, one of which replaces claude with copilot and the second one messing up the docs markdown, getting merged after that. Agentic workflows are the battle... https://github.com/github/gh-aw/pull/14543
onionisafruit 40 days ago | root | parent | next [–]
I’m glad they are dogfooding this in public because it is a good indicator to stay far far away
Lucasoato 41 days ago | parent | prev | next [–]
It is so important to use specific prompts for package upgrading. Think about what a developer would do:
- check the latest version online;
- look at the changelog;
- evaluate if it’s worth to upgrade or an intermediate may be alright in case of code update are necessary; Of course, the keep these operations among the human ones, but if you really want to automate this part (and you are ready to pay its consequences) you need to mimic the same workflow.
I use Gemini and codex to look for package version information online, it checks the change logs from the version I am to the one I’d like to upgrade, I spawn a Claude Opus subagent to check if in the code something needs to be upgraded. In case of major releases, I git clone the two packages and another subagents check if the interfaces I use changed. Finally, I run all my tests and verify everything’s alright. Yes, it might not still be perfect, but neither am I.
pnvdr 41 days ago | parent | prev | next [–]
Kinda reminds of secure sleep command in GitHub actions
huevosabio 41 days ago | prev | next [–]
Github should focus on getting their core offerings in shape first. I stopped using GH actions when I ran into this issue: https://github.com/orgs/community/discussions/151956#discuss... That was almost a year ago and to this date I still get updates of people falling into the same issue.
lloydatkinson 41 days ago | parent | next [–]
This reminds me slightly of some copilot nonsense I get. I don’t use copilot. Every few days when I’m on the GitHub homepage the copilot chat input (which I don’t want on my homepage anyway) tells me it’s disabled because I’ve used up my monthly limit of copilot. I literally do not use it, and no my account isn’t compromised. Trying to trick people into paying? Seems cartoonishly stupid but…
raxxorraxor 41 days ago | parent | prev | next [–]
I cannot recommend Gitea enough. It is easy to install, can be very well integrated into the usual corporate Microsoft networks (ldap/adfs) and has very simple workers, which just reliably execute the actions defined in the .gitea folder of your repository. Installing workers is an extra step, but you don't really need a PhD to get it running. You can build a very efficient and reliable CI pipeline this way and you are not dependent on third parties at all. The interface is mostly 1:1 Github. Just the bullshit is ripped out.
pydry 41 days ago | parent | prev | next [–]
Well, this behavior makes sense. They're a bluechip trying to maintain the illusion that theyre a growth stock juuuust a little bit longer.
SkyPuncher 41 days ago | parent | prev | next [–]
Ah, the critical problem dilemma. Some percentage of free users become paid users, but the free users take up an unreasonable amount of your time/energy/support. The solution seems simple. Buy their product.
huevosabio 41 days ago | root | parent | next [–]
I don't follow, we pay them for the actions and everything and still ran into this issue. That's why it's an issue .
antonvs 41 days ago | root | parent | next [–]
What's the issue, as you see it? I've quoted the response on that ticket below. Is there something you disagree with? The "issue" is that usage exceeds the amount that's been paid. The solution sounds pretty simple: pay for your usage. Is your experience different somehow? > If usage is exceeded, you need to add a payment method and set a spending limit (you can even set it to $0 if you don’t want to allow extra charges). > If you don’t want to add billing, you’ll need to wait until your monthly quota resets (on the first day of the next month). Edit: also, one of the other comments says this: > If you’re experiencing this issue, there are two primary potential causes: > Your billing information is incorrect. Please update your payment method and ensure your billing address is correct. > You have a budget set for Actions that is preventing additional spend. Refer to Billing & Licensing > Budgets.
huevosabio 41 days ago | root | parent | next [–]
I paid or tried to for the extra billing, I followed all the instructions and still got the same error. Attempts to get help land you in that catch-all issue. Its a problem with their own systems and it's easier to role out your own alternative than to get a handle of a support person.
wasmainiac 41 days ago | root | parent | prev | next [–]
> The solution seems simple. Buy their product. Buying half baked software would probably encourage this. Quarter baked software!
elAhmo 40 days ago | root | parent | prev | next [–]
GitHub made more things free than in the past after MS acquisition, so this is driven by them, not just by users, making your 'buy their product' not really viable in this case. I remember having to pay to have private repos in the past, but I guess MS didn't want my money and now I am a free user. If they offer stuff for free, doesn't mean it should be unreliable and best effort.
catlifeonmars 40 days ago | root | parent | prev | next [–]
Looks like the issue linked above affected both paid and free users.
antonvs 41 days ago | parent | prev | next [–]
"In shape" in what sense? This is just hitting the limits of a free account, and the message clearly states that. > people falling into the same issue. Every SaaS provider with a free tier has this issue. How do you suggest it should be addressed?
huevosabio 41 days ago | root | parent | next [–]
As I stated above, the problem is that even when I tried to pay, it was still failing under the same error. I don't mind paying for software, I hate paying for half-assed, unsupported software.
catlifeonmars 40 days ago | root | parent | prev | next [–]
This affected (probably still affects) paid and free tier users. There’s obviously some corrupt state for some accounts on the backend. As stated in the issue, if you are successfully able to engage support they’re gonna run a script to get your account unstuck. I’m reading between the lines a bit, but that seems to be the gist of it.
nozzlegear 41 days ago | parent | prev | next [–]
I've been a paying Github user for years now, and as an open source maintainer who uses Github Actions, I'm annoyed that my money has been funding AI bullshit instead of fixes and improvements for their core offering.
onionisafruit 41 days ago | prev | next [–]
This is an extension for the gh cli that takes markdown files as input and creates github actions workflow files from them. Not just any workflow files, but 1000-line beasts that you'll need an LLM to explain what they do. I tried out `gh aw init` and hit Y at the wrong prompt. It created a COPILOT_GITHUB_TOKEN on the github repo I happened to be in presumably with a token from my account. That's something that really should have an extra confirmation.
resquawk 41 days ago | parent | next [–]
Thanks, this has been changed (no use of local token) and there are now extra confirmations too.
catlifeonmars 40 days ago | root | parent | next [–]
Is this thing production ready?
lemonlime227 41 days ago | prev | next [–]
Alternative, less phishy link: https://github.com/github/gh-aw This is on GitHub's official account. For some reason GitHub is deploying this on GitHub pages without a different domain?
dcchuck 41 days ago | parent | next [–]
This is a github pages feature. Given an account with the name "example", they can publish static pages to example.github.io So this being from github.github.io implies it's published by the "github" account on github.
eddythompson80 41 days ago | parent | prev | next [–]
Why would that be phishy? They own the GitHub org on GitHub, hence github.github.io. I always thought it was a neat recursive/dogfood type thing even if not really that deep. Like when Reddit had /r/reddit.com or twitter having @twitter
embedding-shape 41 days ago | root | parent | next [–]
When they launched github.io, they said it was for user-generated content, and official stuff will be on github.com. Seemingly that's changed/they forgot, but users seems to have remembered. Microsoft isn't famous for their consistency, so not unexpected exactly.
jen20 41 days ago | root | parent | next [–]
When GitHub pages was launched, IIRC it was _on_ GitHub.com and only moved later. User content that is _not_ pages is on githubusercontent.com to this day.
eddythompson80 41 days ago | root | parent | prev | next [–]
I’m pretty sure they have used it before, or maybe it was githubnext. I’m also pretty sure I have seen many large companies and organizations launch developer facing tools and stuff through GitHub pages. The structure of GitHub pages is pretty simple. You know the user/org from the domain. I’m still not sure what’s phishy about it. Is it a broken promise?
DSMan195276 41 days ago | root | parent | next [–]
It's phishy because it's breaks the rules people are generally told for avoiding phishing links, mainly that they should pay attention to the domain rather than subdomains. Browser even highlight that part specifically so that you pay attention to it, because you can't fake the real domain. The problem with what GitHub does here is that while `github.github.io` might be the real GitHub, `foobar-github.github.io` is not because anybody can get a github.io via their username, that was part of why they made github.io separate. Additionally they could easily host this via GitHub Pages but still use a custom domain back to github.com, they just don't. I would say that GitHub is particularly bad about this as they also use `github.blog` for announcements. I'm not sure if they have any others, but then that's the problem, you can't expect people to magically know which of your different domains are and aren't real if you use more than one. They even announced the github.com SSH key change on github.blog.
resquawk 41 days ago | root | parent | next [–]
Hey, sorry, yes the better link is
https://github.github.com/gh-aw/ but we had a redirect set to
https://github.github.io/gh-aw/ Both work and we've fixed the redirect now, thanks
pixl97 41 days ago | root | parent | prev | next [–]
>It's phishy because it's breaks the rules people are generally told for avoiding phishing links Bank: Avoid phishing links, this is what they look like. Also bank: Here is an link from our actual marketing department that looks exactly like phishing.
dwroberts 41 days ago | root | parent | prev | next [–]
I’ve never seen github.github in the URL before, and without additional info I would have assumed it was someone pulling a trick to impersonate their org
resquawk 41 days ago | parent | prev | next [–]
Hey, sorry, yes the better link is
https://github.github.com/gh-aw/
but we had a redirect set to
https://github.github.io/gh-aw/ Both work and we've fixed the redirect now, thanks
hmokiguess 41 days ago | parent | prev | next [–]
So them using their own product makes it phishy? I don’t get it It’s not like someone else can or could own this link, could they?
idan 41 days ago | parent | prev | next [–]
Any github pages site is, by default, ORGNAME.github.io. We recently moved this out of the githubnext org to the github org, but short of dedicating some route in github.com/whatever, github.github.io is the domain for pages from the github org.
SkyPuncher 41 days ago | parent | prev | next [–]
Looks like a pre-release product. This is to lower the branding and reputational risk.
ogig 41 days ago | prev | next [–]
What timing. I used the whole weekend building a CI agentic workflow where I can let CC run wild with skip-permissions in isolated vms while working async on a gitea repo. I leave the CC instance with a decent sized mission and it will iterate until CI is green and then create a PR for me to merge. I'm moving from talking synchronously to one Clade Code to manage a small group of collaborating Claudes.
nine_k 41 days ago | parent | next [–]
How much does it cost you?
raxxorraxor 41 days ago | root | parent | next [–]
I do it similarly and it only costs me my working time. I do some of these things outside my official working times for free, but that is because I like the topic and like to have a good deployment pipeline. But I doubt it is in any way more significant time investment than administration of Github. In the end you need to write your deployments scripts yourself anyway, which takes the most time. Otherwise for installation, the most time consuming task is probably ssh key management of your users, if you don't have any fitting infrastructure.
nine_k 40 days ago | root | parent | next [–]
I mean, agents don't run for free for any significant time. Tokens cost money.
raxxorraxor 39 days ago | root | parent | next [–]
I meant the CI agents, not AI agents. These are just runners that execute the stuff that needs to be done for deployment/testing or general CI. These rarely call AI agents because these tasks need to be deterministic. If so, you probably want to call a local model under your control running on your own compute power.
qwertox 41 days ago | parent | prev | next [–]
Crazy times.
CuriouslyC 41 days ago | prev | next [–]
Stuffing agents somewhere they don't belong rather than making the system work better with the agents people already use. Obvious marketing driven cash grab.
maccard 41 days ago | parent | next [–]
> Stuffing agents somewhere they don't belong rather than making the system work better with the agents people already use. I'm not bullish on LLM based agentic coding, but if there was ever a place to put an agent it would be in a centralised provider that has access to your CI, issues and source code. It seems like a perfect fit.
mcintyre1994 41 days ago | parent | prev | next [–]
I keep wondering if this is what kills GitHub. Anthropic have done a pretty good job of making Claude work well with GitHub, and it makes all the GitHub agent stuff feel pointless to me. But they keep adding it in more and more places, and I’m guessing most people just keep ignoring it and using Claude. Would they think it’s worth introducing restrictions to make it harder to use Claude with GitHub in the hopes that it forces us to use their endless collection of agent stuff instead? I think they probably would choose that tradeoff.
siscia 41 days ago | prev | next [–]
I am somehow close to what MSFT and GitHub are doing here, mostly because I believe it is a great idea, and I am experimenting on it myself. Especially on the angle of automatic/continuos improvement ( https://github.github.io/gh-aw/blog/2026-01-13-meet-the-work... ) Often code is seen as an artifact, that it is valuable by itself. This was an incomplete view before, and it is now a completely wrong view. What is valuable is how code encode the knowledge of the organization building it. But what it is even more valuable, is that knowledge itself. Embedded into the people of the organization. Which is why continuos and automatic improvement of a codebase is so important. We all know that code rot with time/features requests. But at the same time, abruptly change the whole codebase architecture destroys the mental model of the people in the organization. What I believe will work, is a slow stream of small improvements - stream that can be digested by the people in the organization. In this context I find more useful to mix and control deterministic execution with a sprinkle of intelligence on top.
So a deterministic system that figure out what is wrong - with whatever definition of wrong that makes sense.
And then LLMs to actually fix the problem, when necessary.
threecheese 41 days ago | parent | next [–]
We are missing some building blocks IMO. We need a good abstraction for defining the invariants in the structure of a project and communicating them to an agent. Even if we had this, if a project doesn’t already consistently apply those patterns the agent can be confused or misapply something (or maybe it’s mad about “do as I say not as I do”). I expend a lot of effort preparing instructions in order to steer agents in this way, it’s annoying actually. Think Deep Wiki-style enumeration of how things work, like C4 Diagrams for agents.
resquawk 41 days ago | parent | prev | next [–]
Yes, great points. Agentic workflows can mix algorithmic + agentic steps. There's a design pattern we call "DataOps" which is all about this - algorithmic extraction then an agentic step delivering a safe output. See https://github.github.com/gh-aw/patterns/dataops/
amluto 41 days ago | prev | next [–]
> GitHub Agentic Workflows deliver this: repository automation, running the coding agents you know and love, in GitHub Actions, with strong guardrails and security-first design principles. GitHub Actions is the last organization I would trust to recognize a security-first design principle.
taejavu 41 days ago | parent | next [–]
Indeed, the last sentence on the page is "Use it with caution, and at your own risk."
clarkdale 41 days ago | prev | next [–]
I feel like this solution hallucinated the concept of Workflow Lock File (.lock.yml), which is not available in Github Actions. This is a missing feature that would solve the security risk of changing git tag references when calling to actions like utility@v1
woodruffw 41 days ago | parent | next [–]
I think in this context they mean “lock” as in “these are the generated contents corresponding to your source markdown,” not as in “this is a lockfile.” But I think that’s a pretty confusing overlap for them to have introduced, given that a lack of strong dependency pinning is a significant ongoing pain point in GHA.
acedTrex 41 days ago | parent | prev | next [–]
You can already hardcode the sha of a given workflow in the ref, and arguably should do that anyways.
chippiewill 41 days ago | root | parent | next [–]
It doesn't work for transitive dependencies, so you're reliant on third party composite actions doing their own SHA locking.
eddythompson80 41 days ago | root | parent | prev | next [–]
You can also configure a policy for it [0] and there are many oss tools for auto converting your workflow into a pinned hash ones. I guess OP is upset it’s not in gh CLI? Maybe a valid feature to have there even if it’s just a nicety [0] https://github.blog/changelog/2025-08-15-github-actions-poli...
SkyPuncher 41 days ago | prev | next [–]
The landing page doesn't make it clear to me what value this is providing to me (as a user). I see all of these things that I can theoretically do, but I don't see (1) actual examples of those things (2) how this specific agentic workflow helps.
idan 41 days ago | parent | next [–]
https://github.github.io/gh-aw/#gallery down the page has a list of concrete applications For examplpe, https://github.github.io/gh-aw/blog/2026-01-13-meet-the-work... has several examples of agentic workflows for managing issues and PRs, and those examples link to actual agentic workflow files you can read and use as a starting point for your own workflows. The value is "delegate chores that cannot be handled by a heuristic". We're figuring out how to tell the story as we go, appreciate the callout!
mook 41 days ago | root | parent | next [–]
Unfortunately only the first one (arborist) actually links to something that the workflow outputs (a created issue), so it's hard to see actual examples of what those things do. Some of the earlier comments said they output giant workflow files, but there weren't really any examples either. Basically it feels like a long article that says "we have this new thing that does cool things", but never gives enough concrete details. It probably worked great for you, but it needs to communicate to random people off the street what the win is.
resquawk 41 days ago | root | parent | next [–]
These contain links to sample outputs: * Quality/Hygiene: https://github.github.com/gh-aw/blog/2026-01-13-meet-the-wor... * Documentation: https://github.github.com/gh-aw/blog/2026-01-13-meet-the-wor... * Code improvement: https://github.github.com/gh-aw/blog/2026-01-13-meet-the-wor... * Refactoring: https://github.github.com/gh-aw/blog/2026-01-13-meet-the-wor...
julius-fx 41 days ago | prev | next [–]
I’d appreciate if they fix the log viewer in GH actions. That would have a larger impact, by far.
kaicianflone 41 days ago | prev | next [–]
This is a solid step forward on execution safety for agentic workflows. Permissions, sandboxing, MCP allowlists, and output sanitization all matter. But the harder, still unsolved problem is decision validation, not execution constraints. Most real failures come from agents doing authorized but wrong things with high confidence. Hallucinations, shallow agreement, or optimizing for speed while staying inside the permission box. I’m working on an open source project called consensus-tools that sits above systems like this and focuses on that gap. Agents do not just act, they stake on decisions. Multiple agents or agents plus humans evaluate actions independently, and bad decisions have real cost. This reduces guessing, slows risky actions, and forces higher confidence for security sensitive decisions. Execution answers what an agent can do. Consensus answers how sure we are that it should do it.
sidpatil 41 days ago | prev | next [–]
Does this products directly compete with GitHub Models [1]? [1] https://github.com/marketplace?type=models
simonw 41 days ago | parent | next [–]
I think it makes use of GitHub models.
idan 41 days ago | root | parent | next [–]
Nope, it uses Copilot CLI under the hood (with your token)
resquawk 41 days ago | root | parent | next [–]
It uses Copilot, Claude Code or OpenAI Codex. Custom engines/coding agents also possible.
r2vcap 41 days ago | prev | next [–]
I tested it a bit yesterday, and it looks good—at least from a structural perspective. Separating the LLM invocation from the apply step is a great idea. This isn’t meant to replace our previous deterministic GitHub Actions workflow; rather, it enables automation with broader possibilities while keeping LLM usage safer. Also, a reminder: if you run Codex/Claude Code/whatever directly inside a GitHub Action without strong guardrails , you risk leaking credentials or performing unsafe write actions.
resquawk 41 days ago | parent | next [–]
> Separating the LLM invocation from the apply step is a great idea Thanks, yes, this is crucial.
qwertox 41 days ago | prev | next [–]
I want to see where we're at in 2 years, because these last couple of months have been pretty chaotic (but in a good sense) in terms of agents doing things with other agents. I think this is the real wake-up-call, that these dumb and error-prone agents can do self-correcting teamwork, which they will hopefully do for us. Two years, then we'll know if and how this industry has completely been revolutionized. By then we'd probably have an AGI emulator, emulated through agents.
dboreham 41 days ago | parent | next [–]
Spoiler: this is how humans always worked. Even Einstein had his wife, Marcel Grossmann and Hilbert, among others.
thulah 41 days ago | root | parent | next [–]
And Stalin had Lysenko.
monkaiju 41 days ago | prev | next [–]
Wasnt GitHub supposed to be doing a feature freeze while they move to Azure?(1)
They certainly could use it as their stability has plummeted. After moving to a self-hosted Forgejo I'll never go back. My UI is instant, my actions are faster than they ever were on GH (with or without accelerators like Blacksmith.sh), I dont constantly get AI nonsense crammed into my UI, and I have way better uptime all with almost no maintenance (mostly thanks to uCore)... GH just doesnt really have much a value proposition for anything that isnt a non-trivial, star gathering obsessed, project IMO... 1: https://thenewstack.io/github-will-prioritize-migrating-to-a... Edit: typo
woodruffw 41 days ago | prev | next [–]
I find this confusing: I can see the value in having an LLM assist you in developing a CI/CD workflow, but why would you want one involved in any continuous degree with your CI/CD? Perhaps it’s not as bad as that given that there’s a “compilation” phase, but the value add there isn’t super clear either (why would I check in both the markdown and the generated workflow; should I always regenerate from the markdown when I need changes, etc.). Given GitHub’s already lackluster reputation around security in GHA, I think I’d like to see them address some of GHA’s fundamental weaknesses before layering additional abstractions atop it.
blibble 41 days ago | parent | next [–]
> but why would you want one involved in any continuous degree with your CI/CD because helping you isn't the goal the goal is to generate revenue by consuming tokens and a never ending swarm of "AI" "agents" is a fantastic way to do that
zozbot234 41 days ago | parent | prev | next [–]
> I find this confusing: I can see the value in having an LLM assist you in developing a CI/CD workflow, but why would you want one involved in any continuous degree with your CI/CD? The sensible case for this is for delivering human-facing project documentation, not actual code. (E.g. ask the AI agent to write its own "code review" report after looking at recent commits.) It's implemented using CI/CD solutions under the hood, but not real CI/CD.
woodruffw 41 days ago | root | parent | next [–]
Sorry, maybe I phrased my original comment poorly: I agree there's value in that kind of "self" code-review or other agent-driven workflow; I'm less clear on how that value is produced (performantly, reliably, etc.) by the architecture described on the site.
resquawk 41 days ago | root | parent | next [–]
For Continuous Documentation examples, see https://github.github.io/gh-aw/blog/2026-01-13-meet-the-work...
wiether 41 days ago | parent | prev | next [–]
I thought that it was to allow non-tech people to start making their own workflows/CI in a no/low-code way and compete against successful companies on this market. But the implementation is comically awful. Sure, you can "just write natural language" instructions and hope for the best. But they couldn't fully get away from their old demons and you still have to pay the YAML tax to set the necessary guardrails. I can't help but laugh at their example: https://github.com/github/gh-aw?tab=readme-ov-file#how-it-wo... They wrote 16 words in Markdown and... 19 in YAML. Because you can't trust the agent, you still have to write tons on gibberish YAML. I'm trying to understand it, but first you give permissions, here they only provide read permissions. And then give output permissions, which are actually write permissions on a smaller scope than the previous ones. Obviously they also absolve themselves from anything wrong that could happen by telling users to be careful. And they also suggest to setup an egress firewall to avoid the agents being too loose: https://github.com/github/gh-aw-firewall Why setting-up an actual workflow engine on an infra managed by IT with actual security tooling when you can just stick together a few bits of YAML and Markdown on Github, right?
resquawk 41 days ago | root | parent | next [–]
The egress firewall is active by default, see https://github.github.io/gh-aw/introduction/architecture/ We've fixed the example on the README to be a link, it should be clearer now what's going on.
mickdarling 41 days ago | parent | prev | next [–]
I use an LLM behavior test to see if the semantic responses from LLMs using my MCP server match what I expect them to. This is beyond the regex tests, but to see if there's a semantic response that's appropriate. Sometimes the LLMs kick back an unusual response that technically is a no, but effectively is a yes. Different models can behave semantically different too. If I had a nice CI/CD workflow that was built into GitHub rather than rolling my own that I have running locally, that might just make it a little more automatic and a little easier.
ljm 41 days ago | parent | prev | next [–]
I don't personally want any kind of workflow that spams my repo with gen AI refactorings or doc maintenance either. That is literally just creating overhead for me and it sounds like an excuse to shoehorn AI in to a workflow more than anything else.
resquawk 41 days ago | root | parent | next [–]
You are 100% in control.
resquawk 41 days ago | parent | prev | next [–]
We've added an FAQ on determinism here: https://github.github.io/gh-aw/reference/faq/#determinism
mickdarling 41 days ago | prev | next [–]
It looks like it does have an MCP Gateway https://github.com/github/gh-aw-mcpg so I may see how well it works with my MCP server. One of the components mine makes are agent elements with my own permissioning, security, memory, and skills. I put explicit programatic hard stops on my agents if they do something that is dangerous or destructive. As for the domain, this is the same account that has been hosting Github projects for more than a decade. Pretty sure it is legit. Org ID is 9,919 from 2008.
anupamchugh 41 days ago | prev | next [–]
Agents don't need full logs to learn from failures — they need structured error patterns. Compact
logs older than 7 days into summaries (status, errors, token count, 1-line context). Saves 80-90%
tokens for 30-day trend analysis. Like materializing aggregates instead of re-querying raw tables.
Opened an RFC for this: https://github.com/github/gh-aw/issues/14603
jrjeksjd8d 41 days ago | prev | next [–]
It feels like every cloud product I use is accumulating more of these peripheral features I don't want, while the core functionality is stagnant or even degrading. I'm assuming this is a Conway's Law situation where the company has to grow, and they hire more devs, but those devs can't all work on the core product so they make new greenfield stuff instead. Until we stop chasing endless growth for it's own sake we're doomed to be stuck these enshittified products.
abracos 41 days ago | prev | next [–]
Link to github.com: https://github.github.com/gh-aw/
siva7 41 days ago | prev | next [–]
Somehow i want to ask what's the actual job of those former software engineers. Agents everywhere, on your local machine, in the pipeline, on the servers, and they are doing everything. Yes, the specs also.
samuelknight 41 days ago | parent | next [–]
Someone still has orchestrate the shit show. Like a captain at the helm in the middle of a storm. Or you can be full accelerationist and give an agent the role of standing up all the agents. But then you need someone with the job of being angry when they get a $7000 cloud bill.
ivanjermakov 41 days ago | parent | prev | next [–]
What is the job of a truck driver, if it's the truck that delivers goods?
microflash 41 days ago | prev | next [–]
Soon: AgentHub Git Workflows
onionisafruit 41 days ago | parent | next [–]
Copilot Hub Enterprise With Copilot
throwup238 41 days ago | parent | prev | next [–]
At which point the AI figures out its easier to just switch to jj
aaronharnly 41 days ago | parent | prev | next [–]
WorkHub Agent Gitflows?
snowstormsun 41 days ago | prev | next [–]
Surely this won't be a security nightmare.
wiether 41 days ago | parent | next [–]
Don't worry, you can just setup an Agentic Workflow Firewall! https://github.com/github/gh-aw-firewall
resquawk 41 days ago | root | parent | next [–]
This firewall is enabled by default
igorpcosta 41 days ago | prev | next [–]
Cool concept, however relying on Actions are really not guaranteed execution all the time.
guluarte 40 days ago | prev | next [–]
It's funny but the webpage look completely 100% AI generated.
mbrumlow 41 days ago | prev | next [–]
I think it is funny they all these companies are spending a ton and racing to have a AI story. It’s almost like none of the executives understand AI. If you are changing your product for AI - you don’t understand AI. AI doesn’t need you to do this, and it doesn’t make you a AI company if you do. AI companies like Anthropic, OpenAI, and maybe Google, simply will integrate at a more human leave and use the same tools humans used in the past, but do so at a higher speed, reliability. All this effort wasted, as AI don’t need it, and your company is spending millions maybe billions to be an AI company that likely will be severely devalued as AI advances.
dgxyz 41 days ago | prev | next [–]
Apologies for the bad language but this can fuck off. They need to fix everything before pasting more shit on top. I’m getting to the point of throwing Jenkins back in it’s that bad. GitHub gives git a bad name and reputation.
AmbroseBierce 41 days ago | prev | next [–]
Now we just need AIs that can create agentic workflows, and then we create workflows that can create many of those AIs, just imagine the (billing) possibilities.
idan 41 days ago | prev | next [–]
Hello HN! The Agentic Workflows project has been on the githubnext.com website for a while, and we recently moved the documentation and repo over to the `github` org. This is early research out of GitHub Next building on our continuous AI [1] theme, so we'd love for you to kick the tires and share your thoughts. We'd be happy to answer questions, give support, whatever you need. One of the key goals of this project is to figure out how to put guardrails around agents running in GitHub actions. You can read more about our security architecture [1], but at a high level we do the following: - We run the agent in a sandbox, with minimal to no access to secrets - We run the agent in a firewall, so it can only access the sites you specify - We have created a system called "*safe outputs*" that limits what write operations the agent can perform to only the ones you specify. For example, if you create an Agentic Workflow that should only comment on an issue, it will not be able to open a new issue, propose a PR, etc. - We run MCPs inside their own sandboxes, so an attacker can’t leverage a compromised server to break out or affect other components We find that there's something very compelling about the shape of this — delegating chores to agents in the same way that we delegate CI to actions. It's certainly not perfect yet, but we're finding new applications for this every day and teams at GitHub are already creating agentic workflows for their own purposes, whether it's engineering or issue management or PR hygiene. > Why is it on github.github.io and not github.com? GitHub Pages domains are always ORGNAME.github.io. Now that we've moved the repo over to the `github` org, that's the domain. When this graduates from being a technology preview to a full-on product, we imagine it'll get a spot on github.com/somewhere. > Why is GitHub Next exploring this? Our job at GitHub is to build applications that leverage the latest technology. There are a lot of applications of _asynchronous_ AI which we suspect might become way bigger than _synchronous_ AI. Agentic Workflows can do things that are not possible without an LLM. For example, there's no linter in existence that can tell me if my documentation and my code has diverged. That's just one new capability. We think there's a huge category of these things here and the only way to make it good is to … make it! > Where can I go to talk with folks about this and see what others are cooking with it? https://gh.io/next-discord in the #continuous-ai channel! [1] https://githubnext.com/projects/continuous-ai/ [2] https://github.github.io/gh-aw/introduction/architecture/ (edit: right I forgot that HN doesn't do markdown links)
tuananh 41 days ago | prev | next [–]
since generation is not deterministic, how do they verify the lock file?
resquawk 41 days ago | parent | next [–]
Generation of the lock file is deterministic. See here for information about determinism https://github.github.com/gh-aw/reference/faq/#determinism
onionisafruit 41 days ago | parent | prev | next [–]
The generation of the workflow file from the input markdown file is deterministic. It's what the agent does when running the workflow that is non-deterministic.
enmyj 41 days ago | prev | next [–]
GitHub fix your uptime then come talk to me about agentic workflows
TZubiri 41 days ago | prev | next [–]
Not confirmed that it's by Github, phishy domain.
embedding-shape 41 days ago | parent | next [–]
Very weird of them to not use github.com but instead use the domain they otherwise use for non-github/user content. Phishy indeed, and then people/companies go ahead and blame users for not taking care/checking, yet banks and more continuously deploy stuff in a way to train users to disregard those things.
throwup238 41 days ago | parent | prev | next [–]
Why is it phishy? Github.io has been the domain they use for all GH pages for a long time with subdomains mapping to GH usernames. It’s standard practice to separate user generated content from the main domain so that it doesn’t poison SEO.
TZubiri 41 days ago | root | parent | next [–]
Correct. First of all, any subdomain system domain is already a bit phishy because you need to somehow parse whether github.io is officially part of github.com and not say something like git-hub.xyz by a phisher or whatever new TLD there. These things are used by sysadmin/project pairs that can't budget 1$/month for a domain name, so it's 100% a security/price tradeoff. Second of all, the actual domain host is publishing as one of these untrusted users on their alternate subdomain, so it could be a phisher using a subdomain of the official alternate domain with malicious material Thirdly, even if it is all legit, it is still a problem, because it weakens security posture, it trains users to ignore domain names. I understand if it appears subtle, but I wish that we lived in a world where whoever is responsible for this gets put on a PIP
throwup238 41 days ago | root | parent | next [–]
I get your general objections, but not in this specific case. Github has been using Github.io for pages since 2013 and it's been the de facto developer platform at least as long (and all other developer tools follow the same pattern when publishing user generated content). Unless GH has a massive vulnerability that hasn't been discovered yet, no one is publishing to *.github.github.io except for the official Github organization. That has been more stable than Linux syscalls and Windows GUI frameworks. Would it really make a difference if they just added a CNAME from foobar.github.com to point at github.github.io?
TZubiri 39 days ago | root | parent | next [–]
Would it really make a difference if they just added a CNAME from foobar.github.com to point at github.github.io? Yes, that would help, but it's not very discoverable. I think a certificate mechanism would be much more appropriate for that. The SSL certificate should be emitted for github.com and github.io Of course since github.io is rented out, it doesn't make sense. But if you ever have an alias, that's the way to do it, if I get a link to getproduct.com and it gets redirected to product.com I can check the cert and see that it was issued for both domains.
rendx 41 days ago | parent | prev | next [–]
Agreed, but looks like it: https://github.com/github/gh-aw
resquawk 41 days ago | parent | prev | next [–]
It's GitHub, using GitHub Pages for docs, https://github.github.com/gh-aw/
served as GitHub Pages from https://github.com/github/gh-aw
hmokiguess 41 days ago | parent | prev | next [–]
How is it not confirmed? GitHub cannot use their own product? Them using GitHub pages changes something? I don’t get it
TZubiri 41 days ago | root | parent | next [–]
I see a lot of people confused, and it is confusing. Here's my best take at clarifying the issue for you: It's as if Google sent you an official email from an @gmail address. Like "gmail-invoices@gmail.com" Surely it would look suspicious, and if it turns out it is official, it doesn't somehow mean there's no issue, if anything it's worse because it untrains users' security protocols. Personally I'd ignore anything that comes out of one of these domains, even if it turns out an actual employee pushed it, if you can't publish something on the main domain, you don't have enough authority to speak for the company, may be skunkworking to avoid an internal protocl, I don't know, I don't care, it's not official, don't need to read it.
hmokiguess 37 days ago | root | parent | next [–]
I don't think this is the same thing though, in their documentation the subdomain has to be for the owner or organization, so if it's `github.github.io` then it belongs to the `github` organization [1] Though I guess I do get your point, meaning that this leads to people trusting the domain name if they are uneducated about how GitHub Pages works. [1] https://docs.github.com/en/pages/getting-started-with-github...
rootnod3 41 days ago | prev | next [–]
Ah yes, lovely. That's what I want in my CI/CD...hallucinations that then churn through I don't know how many tokens trying to "fix it".
thulah 41 days ago | prev | next [–]
This is insane stuff. Why are they pushing this nonsense on developers when the real money is in surveillance and web indexing? People like Nadella must think that developers are the weakest link: Extreme tolerance for Rube Goldberg machines, no spine, no sense of self-protection. I'll cancel my paid GitHub account though.
andrewmcwatters 41 days ago | prev | next [–]
There's a lot of hate in this thread, but there are plenty of engineers chomping at the bit for autonomous workflows, because browser-use isn't there yet, and cloud expenses from major providers are also unappealing with so much relatively powerful local compute.
catlifeonmars 40 days ago | parent | next [–]
It’d be fine if they included a big disclaimer at the top that this is beta software and they’re not liable for blah blah blah, but without such a disclaimer it’s reasonable to assume the software is ready for production. I think much of the hate is coming from GH misrepresenting its software and people being surprised by the many minor bugs.
resquawk 40 days ago | root | parent | next [–]
Thanks! We've moved the disclaimer up the page :)
ewuhic 41 days ago | prev [–]
Go: check YAML: check Markdown: check Wrong level of abstraction: check Shit slop which will be irrelevant in less than a year time: check Manager was not PIP'd: check
Guidelines | FAQ | Lists | API | Security | Legal | Apply to YC | Contact
Search:

## Import Provenance

- imported_from: canonical-openclaw-runtime
- runtime_article_bundle_path: research/articles/art-2026-03-21-025.md
- runtime_source_snapshot_json: research/source-material/art-2026-03-21-025.json
- runtime_source_snapshot_text: research/source-material/art-2026-03-21-025.txt
- runtime_filter_state: pending
- runtime_last_stage: intake
- refreshed_live_source: false
