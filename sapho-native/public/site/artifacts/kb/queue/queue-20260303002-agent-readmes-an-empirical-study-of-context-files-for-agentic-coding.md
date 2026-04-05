<details class="traceability-panel">
<summary>Traceability</summary>
<div class="traceability-body">
<ul>
  <li><strong>Source:</strong> <a href="https://arxiv.org/html/2511.12884v1" target="_blank" rel="noopener">https://arxiv.org/html/2511.12884v1</a></li>
  <li><strong>Intake queued:</strong> 2026-03-03T11:00:15Z</li>
  <li><strong>Source captured:</strong> 2026-03-07T19:27:13Z</li>
  <li><strong>Curated:</strong> 2026-04-02T15:28:33Z</li>
  <li><strong>Artifact finalized:</strong> 2026-04-02T15:31:04Z</li>
  <li><strong>Artifact published:</strong> 2026-03-28T00:19:32Z</li>
</ul>
</div>
</details>

# Agent READMEs: An Empirical Study of Context Files for Agentic Coding

## Core Thesis

Agent context files are not marginal setup artifacts. Across a large cross-repository sample, they appear to function as active operational guidance for coding agents: they differ meaningfully by ecosystem, they are revised as living documents rather than written once, and their content is weighted toward execution-facing instructions such as testing, implementation detail, architecture, process, and build/run behavior.

## Why It Matters for Sapho

This matters because it pushes agent guidance out of the realm of prompt folklore and into observable software practice. If context files are regularly maintained, structurally patterned, and concentrated on concrete execution constraints, Sapho should treat them as a real control surface for agent behavior rather than as decorative documentation. It also warns against simplistic doctrine: longer files are not automatically better, easier readability does not by itself prove higher utility, and sparse visibility for security or performance guidance may reflect both real omission and measurement limits. For Sapho, the lesson is to evaluate agent-control artifacts as bounded institutional infrastructure: what teams choose to encode, revisit, and foreground is itself evidence about where reliability pressure is being applied.

## Key Findings

- The study analyzes agent context files at meaningful scale: 2,303 files drawn from 1,925 repositories, starting from a broader pool of 8,370 starred AIDev repositories with at least 5 GitHub stars.
- The corpus spans 922 Claude Code files, 694 OpenAI Codex files, and 687 GitHub Copilot files, giving the comparison real cross-ecosystem breadth rather than a single-tool snapshot.
- File format differs by ecosystem. Median length is 535.0 words for GitHub Copilot, 485.0 for Claude Code, and 335.5 for OpenAI Codex; the source reports no statistically significant length difference between GitHub Copilot and Claude Code, but both are longer than OpenAI Codex.
- Readability also differs. Median Flesch Reading Ease scores are 16.6 for Claude Code, 26.6 for GitHub Copilot, and 39.6 for OpenAI Codex, making Codex files easier to read by this metric than the other two.
- These files are usually maintained rather than frozen. A majority were modified in multiple commits: 67.4% for Claude Code, 59.7% for GitHub Copilot, and 59.2% for OpenAI Codex.
- Update cadence can be fast: median intervals between revisions are 24.1 hours for Claude Code, 22.0 hours for OpenAI Codex, and 70.7 hours for GitHub Copilot, with all pairwise interval differences reported as significant at p < 0.001.
- Evolution is addition-heavy rather than rewrite-heavy. Deletions stay small, with median deletions below 15.0 words, while Claude Code commits add a median of 57.0 words.
- Instruction content is concentrated in immediate execution domains: Testing appears in 75.0% of the manually analyzed subset, Implementation Details in 69.9%, Architecture in 67.7%, Development Process in 63.3%, and Build and Run in 62.3%.
- Non-functional topics are much less visible in the labeled data: Security and Performance each appear in 14.5% of the manual subset, and UI/UX in 8.7%.

## Evidence and Findings

- The paper establishes unusual empirical scale for this topic by tracing 2,303 context files across 1,925 repositories after beginning with 8,370 starred AIDev repositories. That supports a serious descriptive map of current practice rather than anecdote, but only within the study’s sampling frame rather than the full universe of agent-using codebases.
- Cross-tool differences are concrete, not rhetorical. GitHub Copilot files are longest on median at 535.0 words, Claude Code follows at 485.0, and OpenAI Codex is shortest at 335.5, while median Flesch scores move in the opposite direction from 16.6 to 26.6 to 39.6. This supports the conclusion that ecosystems have distinct documentation styles, and it matters because prompt-control doctrine cannot be transferred across tools as if all context surfaces are interchangeable.
- Maintenance evidence is strong enough to reject the idea that these files are mostly one-time scaffolds. Between 59.2% and 67.4% of files are revised across multiple commits, and median update intervals fall to roughly a day for Claude Code and OpenAI Codex. That supports a living-document interpretation and matters because teams appear to adjust agent guidance alongside ongoing development rather than only at project setup.
- Commit behavior shows incremental accretion more than wholesale churn. The maintenance analysis spans 5,655 Claude Code commits, 2,767 OpenAI Codex commits, and 2,237 GitHub Copilot commits touching context files; deletions are typically under 15.0 words, while Claude Code commits add a median of 57.0 words. This supports the view that teams tune and extend instructions over time, which matters because control surfaces for agents may grow by local patching rather than by periodic redesign.
- The content distribution is heavily operational. In the manual analysis, Testing leads at 75.0%, followed by Implementation Details at 69.9%, Architecture at 67.7%, Development Process at 63.3%, and Build and Run at 62.3%. This supports the conclusion that teams mainly use context files to constrain execution and workflow, and it matters because practical reliability work appears to center on making agents behave correctly inside the build-test-dev loop.
- The apparent scarcity of non-functional instruction is real enough to notice but not clean enough to overread. Security and Performance each appear in 14.5% of the manual subset and UI/UX in 8.7%, yet the automatic classifier performs worse on abstract categories, with F1 scores of 0.48 for AI Integration and 0.42 for Project Management despite a 0.79 micro-average overall. That supports a bounded claim that non-functional concerns are less visible, while also warning that abstraction-heavy topics may be under-captured.

## Contradictions and Tensions

There is no direct headline contradiction in the paper’s main descriptive findings, but there are important tensions.

First, longer files are not obviously superior. GitHub Copilot files are longest on median, but OpenAI Codex files are shortest and also easiest to read by Flesch score. The study shows format differences, not a performance hierarchy.

Second, the maintenance story is mixed across ecosystems. GitHub Copilot files are often revised multiple times, yet their median update interval is much longer at 70.7 hours than Claude Code or OpenAI Codex. That points to shared maintenance behavior with different rhythms, not one uniform lifecycle.

Third, the low prevalence of security, performance, and UI/UX guidance may reflect genuine underemphasis, but it may also partly reflect measurement weakness on more abstract categories. The descriptive signal is useful, but it should not be mistaken for a complete census of all higher-level concerns encoded in these files.

## Mechanism or Bounds

The paper is descriptive, not causal. It shows how teams structure and revise agent context files, but it does not establish why particular ecosystems converge on different lengths, readability levels, or update cadences. The best supported mechanism is a bounded one: teams appear to use these files as evolving operational guidance, and they revise them as project knowledge, constraints, and preferred workflows change. Beyond that, explanations about platform norms, template defaults, author habits, or downstream effectiveness remain uncertain.

The content findings are also bounded by method. The strongest prevalence numbers come from a manual analysis of 332 Claude Code files with 2,069 final label assignments after disagreement resolution, not from a fully equivalent hand-coded sample across all tools. Automatic classification extends the analysis, but weaker performance on abstract categories limits how confidently one can infer absence from low label frequency.

## Limits

The sample is broad but not fully representative: it begins from 8,370 starred AIDev repositories with at least 5 GitHub stars and then retrieves files using documented naming conventions, so the findings do not automatically generalize to all agent-enabled repositories or undocumented file practices.

The paper does not connect context-file characteristics to downstream coding outcomes. It shows what these files look like and how they evolve, but not whether longer, shorter, denser, or more readable files produce better agent performance.

Readability metrics are only partial proxies. A higher Flesch score indicates easier reading under that formula, not greater usefulness, precision, or control quality for coding agents.

The content taxonomy is informative but incomplete. Low prevalence for non-functional concerns should be treated as a meaningful signal, not a closed verdict, because abstract categories were harder for the classifier to capture reliably.

Finally, the study supports disciplined claims about practice patterns, not publication law. It is strong evidence that context files matter operationally, but it does not settle what the best context-file doctrine should be.
