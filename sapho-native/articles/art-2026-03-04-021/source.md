---
version: source-capture.v1
article_id: art-2026-03-04-021
ticket_id: ticket-import-art-2026-03-04-021
source_url: https://arxiv.org/abs/2512.14012
canonical_url: https://arxiv.org/abs/2512.14012
source_title: "Professional Software Developers Don\u2019t Vibe, They Control: AI\
  \ Agent Use for Coding in 2025"
capture_kind: arxiv_html
http_status: 200
content_type: text/html
captured_at_utc: '2026-03-30T17:50:01Z'
linked_paper_urls: []
---
# Source Capture

## Title

Professional Software Developers Don’t Vibe, They Control: AI Agent Use for Coding in 2025

## Body

Professional Software Developers Don’t Vibe, They Control: AI Agent Use for Coding in 2025

Ruanqianqian (Lisa) Huang r6huang@ucsd.edu UC San Diego USA , Avery Reyna avery.reyna16@gmail.com Independent USA , Sorin Lerner sorin.lerner@cornell.edu Cornell University USA , Haijun Xia haijunxia@ucsd.edu UC San Diego USA and Brian Hempel bhempel@ucsd.edu UC San Diego USA

( 2018 )

Abstract.

The rise of AI agents is transforming how software can be built.
The promise of agents is that developers might write code quicker, delegate multiple tasks to different agents, and even write a full piece of software purely out of natural language. In reality, what roles agents play in professional software development remains in question.
This paper investigates how experienced developers use agents in building software, including their motivations, strategies, task suitability, and sentiments.
Through field observations (N=13) and qualitative surveys (N=99), we find that while experienced developers value agents as a productivity boost, they retain their agency in software design and implementation out of insistence on fundamental software quality attributes, employing strategies for controlling agent behavior leveraging their expertise.
In addition, experienced developers feel overall positive about incorporating agents into software development given their confidence in complementing the agents’ limitations.
Our results shed light on the value of software development best practices in effective use of agents, suggest the kinds of tasks for which agents may be suitable, and point towards future opportunities for better agentic interfaces and agentic use guidelines.

† † copyright: acmlicensed † † journalyear: 2018 † † doi: XXXXXXX.XXXXXXX † † conference: Make sure to enter the correct
conference title from your rights confirmation email; June 03–05,
2018; Woodstock, NY † † isbn: 978-1-4503-XXXX-X/2018/06

1. Introduction

I’ve been a software developer and data analyst for 20 years and there is no way I’ll EVER go back to coding by hand. That ship has sailed and good riddance to it.

- Developer in Our Survey (S28)

AI is rapidly changing the practice of programming.
Already, about half of professional software developers are using AI tools daily ( stackoverflow2025survey ) .
Large language models (LLMs) are particularly good at writing code, and are becoming more skillful every year.
Originally, in 2021, LLMs only provided coding assistance as super-charged autocomplete ( GitHubCopilot ) .
But more recently, their capabilities have advanced to accessing, modifying, and testing whole codebases in autonomous, step-by-step actions—we are now in the agentic coding era.
There are many open questions about how capable these agents are and how best to use them.
Anecdotally, we sometimes hear from people that they tried it once and it didn’t work out so well.
But this contrasts with what one reads on social media: some online users claim to use dozens of agents at once to autonomously construct massive software ( e.g. , ( thermo2025dozenAgents ; yegge2025dozenAgents ) ), a claim so intriguing but potentially incredulous that it is parodied ( ivibemorethanyoudotcom ) . What is really happening?

Human studies of agentic coding are emerging but still sparse. A notable randomized trial found that experienced open source maintainers were actually slowed down by 19% when allowed to use AI ( becker2025early2025 ) , and an agentic system deployed in an issue tracker saw only 8% of its invocations resulting in complete success (a merged pull request) ( takerngsaksiri2025hula ) .
These results suggest that perhaps agentic AI is not as useful as it might first sound, but still about a quarter of professional developers report that they already use AI agents at least weekly ( stackoverflow2025survey ) .
There have been a few recent investigations ( sarkar2025vibe ; fawzy2025vibeCoding ; pimenova2025goodVibrations ; geng2025studentVibe ) of “vibe coding” ( karpathy2025vibecoding ) . Although the term is sometimes used to mean any coding with AI agents, these papers investigate “vibe coding” as a particular form of agent use that aims for an experience of “flow and joy” by trusting the AI instead of carefully reviewing the generated code ( pimenova2025goodVibrations ) , “where you fully give in to the vibes”, “forget that the code even exists”, and “don’t read the diffs anymore” ( karpathy2025vibecoding ) .
There is a tacit acknowledgment by its practitioners that vibing produces lower quality code ( fawzy2025vibeCoding ) .
As such, vibing may not be the most successful approach to agentic coding, and may not be how experienced developers use agents. How, then, do experienced developers create quality software with AI agents?

This paper is an attempt to gain insight into the current practice of agentic coding by experts,
in order to understand what is and is not working.
Compared to prior work, we (a) do not limit the investigation to to vibe coding, and (b) examine experienced developers only, in the hopes that they have enough expertise to be insightfully critical of the agentic tools in real-world use.
We present a two-part study—13 field observations and a broader survey of 99 experienced developers—hoping to answer four research questions (RQs):

- RQ1 - Motivations.

What do experienced developers care about when incorporating agents into their software development workflow?

- RQ2 - Strategies.

What strategies do experienced developers employ when developing software with agents?

- RQ3 - Suitability.

What are software development agents suitable for, and when do they fail?

- RQ4 - Sentiments.

What sentiments do experienced developers feel when using agentic tools?

Our most salient finding is that, indeed, professional developers do not vibe code.
Instead, they carefully control the agents through planning and supervision. Specifically,
they are looking for a productivity boost while still valuing software quality attributes (RQ1), they plan before implementing and validate all agentic outputs (RQ2), they find agents suitable for well-described, straightforward tasks but not complex tasks (RQ3), and yet they generally enjoy using agents as long as they are in control (RQ4).

The rest of the paper is structured as follows: Sec. 2 describes the methodology of our two-part study; LABEL:sec:results details the findings, which are summarized in LABEL:sec:results-summary ;
we discuss the implications of our findings in LABEL:sec:discussion , relate our study to prior work in LABEL:sec:related , and conclude the paper in LABEL:sec:conclusion .

2. Methods

We define experienced developers as those with at least three years of professional development experience.
We define agentic tools or agents as AI tools integrated into an IDE or a terminal that can manipulate the code directly ( i.e. , excluding web-based chat interfaces).

We study the RQs through a two-part study: in depth via field observations ( Sec. 2.1 ), and in breadth via a qualitative survey ( Sec. 2.2 ).
Our institutional review board approved both parts.
Full replication package of the study materials can be found at https://osf.io/bxwv2/?view_only=25dfabc544fc497dae628d1ea8996896 .

2.1. Part 1: Field Observations

Participants. We recruited most participants via social media and personal networks, and one by snowball sampling.
We imposed the following screening constraints: (1) three or more years of verifiable professional software engineering experience (full-time, part-time, and internships included); (2) prior experience with agentic AI in creating software; and (3) the ability to demonstrate a realistic task as part of work or personal side projects to be done with agentic AI during the study.
Eventually, we recruited 13 participants (1 identifying as female, 12 as male) with years of professional experience ranging from 3 to 25. LABEL:tab:observation-participants details their use agentic tools, model use, and tasks during the study; we detail their tasks later in this subsection.

Procedure. Each study session included two parts: a 45-minute observation and a 30-minute semi-structured interview. We conducted the studies over Zoom, recording participants’ screens and audio for analysis.
The first two authors took turns to run the study. Sessions were run between August 1 and October 3, 2025.

During the observational portion, participants worked on tasks of their choosing using their preferred setup.
At the beginning, participants introduced their task, source of code base, agentic AI setup, and task relevance to their day-to-day work.
Then, we asked participants to think aloud as they worked.
We asked questions about each participant’s workflow and task to gain additional insights as needed, following prior practices ( groundedJupyter ) .
After about 45 minutes of observation, we asked the participant to start wrapping up their work.
We conducted a semi-structured interview afterward.
Our questions involved topics relevant to all our research questions and necessary follow-ups on the observation portion.
Participants received a $100 USD gift card after the study.

Tasks. Prior to each study, we asked participants to bring their own tasks where they would use their usual agentic workflows; tasks need not be completed during the study and could be something from scratch or ongoing.
Each participant worked on tasks that were part of their own ongoing work or side projects during the study.
Specifically, five worked on production software as part of their work (P2, P3, P6, P7, P13), three demonstrated exploratory work tasks given the R&D nature of their jobs (P4, P5, P10), and five pursued side projects, including three collaborative (P1, P9, P12) and two personal (P8, P11). Through answers to the question about task relevance to their day-to-day work, five out of 13 participants (P1, P4, P5, P9, P12) reported that their tasks were outside of their professional domains, as indicated in the “Familiar?” column in LABEL:tab:observation-participants .

2.2. Part 2: Invited Survey

Survey Structure. We designed a 15-minute qualitative survey.
After completing the survey, participants could join a drawing to win one of four $100 USD gift cards.
All questions in the survey were required, except for the last question for optional comments.
