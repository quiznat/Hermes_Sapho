<details class="traceability-panel">
<summary>Traceability</summary>
<div class="traceability-body">
<ul>
  <li><strong>Source:</strong> <a href="https://arxiv.org/abs/2512.14012" target="_blank" rel="noopener">https://arxiv.org/abs/2512.14012</a></li>
  <li><strong>Intake queued:</strong> 2026-03-04T03:59:01Z</li>
  <li><strong>Source captured:</strong> 2026-03-30T17:50:01Z</li>
  <li><strong>Curated:</strong> 2026-04-02T21:13:32Z</li>
  <li><strong>Artifact finalized:</strong> 2026-04-02T21:15:25Z</li>
  <li><strong>Artifact published:</strong> 2026-03-30T17:55:39Z</li>
</ul>
</div>
</details>

# Professional Software Developers Don’t Vibe, They Control: AI Agent Use for Coding in 2025

## Core Thesis

Among experienced developers, AI coding agents are treated as supervised productivity tools rather than autonomous replacements. The paper’s central finding is not that professionals hand work over to agents, but that they preserve control through planning, close supervision, output validation, and explicit quality standards, while confining agent use to tasks that are clear and straightforward.

## Why It Matters for Sapho

This matters because it cuts against the strongest automation story now circulating around agentic coding. For Sapho, the relevant lesson is that positive field sentiment does not establish autonomous reliability. The operative advantage appears to come from expert-guided control loops, not from removing the human from design and implementation. That shifts evaluation doctrine toward task-bounded usefulness, supervision cost, and quality-preserving workflow discipline rather than headline claims of replacement.

## Key Findings

- The study reports that experienced developers saw AI agents as a productivity boost, but not as substitutes for their own judgment or ownership of the code.
- Developers retained agency over software design and implementation by planning work in advance, supervising agent behavior, and validating every agent-produced output.
- Control was not merely cultural preference; it was tied to insistence on core software quality attributes, with developers using their expertise to keep outputs inside acceptable standards.
- Agent usefulness was sharply bounded by task type: developers found agents suitable for well-described, straightforward work and unsuitable for complex tasks.
- Positive sentiment was conditional rather than unconditional. Developers were favorable when they believed their own expertise could compensate for agent weaknesses.
- The study base is qualitative and bounded: 13 field observations plus a survey of 99 experienced developers, with “experienced” defined as at least three years of professional development experience.

## Evidence and Findings

- The source’s main empirical result is that professional developers did not “vibe code”; they controlled agents through planning and supervision. That supports the conclusion that agent adoption in professional settings can coexist with strong human authority rather than dissolve it, which matters because many public narratives imply the opposite.
- Developers reported planning before implementation and validating all agentic outputs. This supports the claim that productivity gains here depend on oversight work and verification discipline, which matters because any performance benefit must be read net of the human control burden.
- The study links retained control to developers’ own expertise and their insistence on fundamental software quality attributes. That supports a bounded mechanism: agents become usable when skilled operators can constrain them against established quality expectations, which matters because the tool’s apparent value is inseparable from operator competence.
- The task boundary is explicit: agents were seen as suitable for well-described, straightforward tasks and not suitable for complex tasks. This supports the conclusion that usefulness is conditional on task clarity and low ambiguity, which matters for deployment decisions because capability claims should not be generalized across the full software lifecycle.
- Positive sentiment toward agents was tied to developers’ belief that they could complement agent limitations. That supports a conditional interpretation of developer optimism, which matters because favorable attitudes here do not amount to trust in autonomous execution.
- The paper itself situates its findings against less favorable prior real-world results, including a randomized trial where experienced open source maintainers were slowed by 19% with AI access and an issue-tracker deployment where only 8% of invocations produced a merged pull request. This matters because it shows that “developers like agents” and “agents perform well in production-like settings” are not interchangeable claims.

## Contradictions and Tensions

- The clearest tension is between positive developer sentiment in this study and prior cited human-study results showing worse outcomes in other real-world contexts, including a 19% slowdown for experienced open source maintainers and only 8% merge success in one issue-tracker deployment.
- There is also an internal practical tension between calling agents a productivity boost and requiring planning, supervision, and validation of all outputs. The paper supports benefit, but the benefit is not frictionless; it appears to depend on additional expert control work.
- Agent value is affirmed and restricted at the same time: developers report usefulness, yet narrow that usefulness to well-described, straightforward tasks and reject suitability for complex work. That means “works for coding” is too coarse a conclusion.
- The paper presents control as a strength, but that strength may also imply a transfer problem: the same conditions that make agents workable for experienced developers may limit whether similar outcomes hold for less experienced operators or weaker governance settings.

## Mechanism or Bounds

The strongest supported mechanism is not autonomous agent competence but expert-mediated control. Developers appear to obtain value by decomposing work in advance, assigning agents bounded tasks, supervising behavior during execution, and validating outputs against fundamental software quality standards. In that sense, the effective system is developer-plus-agent, not agent alone.

The bounds are equally important. This evidence comes from 13 field observations and a qualitative survey of 99 experienced developers, where “experienced” means at least three years of professional practice. The findings support a workflow-bound explanation for success among experienced practitioners, not a general claim that coding agents perform reliably across complex tasks, across novice users, or without intensive human oversight.

## Limits

The study supports bounded claims about experienced developers’ practices and attitudes, not universal claims about software teams or coding agents in general.
It does not quantify the magnitude of the reported productivity boost in the provided evidence context.
Its positive conclusions are partly in tension with prior real-world studies the paper cites, which reported slowdown and low merge success.
The mechanism is operational rather than deeply causal: the paper shows that planning, supervision, and validation matter, but does not fully resolve which parts of that control loop produce the gains or where the overhead cancels them out.
The usefulness claim is task-limited; the evidence does not support extending these results from straightforward tasks to complex software work.
