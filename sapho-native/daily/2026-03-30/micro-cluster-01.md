## Cluster Thesis

Current AI coding tools demand substantial human stewardship—from meticulously curated context to active supervision—to deliver value in real-world software engineering, revealing significant gaps between automation narratives and practical capability limits that only experienced practitioners can navigate.

## Shared Signals

- Human expertise remains indispensable: developers exercise active governance, whether through supervisory oversight or structured context curation, rather than delegating to autonomous systems.
- Context is the critical variable: AI assistant effectiveness depends heavily on how developers encode project constraints, conventions, and intent into machine-readable guidance.
- Real-world complexity exposes capability gaps: systems that succeed on isolated tasks fail when confronted with multi-file coordination, execution environments, and extended reasoning demands.
- Multi-agent workflows introduce fragility: the handoff between planning and execution agents creates systemic brittleness that requires targeted intervention to mitigate.

## Article Notes

- Controlled Collaboration: experienced developers maintain disciplined control over AI agents through meticulous planning and oversight, rejecting passive delegation in favor of active supervision that preserves software quality.
- Developer-Provided Context: practitioners systematically curate project-specific guidance through specialized "rule files" across five categories—Conventions, Guidelines, Project Information, LLM Directives, and Examples—transforming documentation practices for AI consumption.
- SWE-bench: a rigorous benchmark of 2,294 real GitHub issues demonstrates that resolving practical software engineering problems requires capabilities beyond code generation, including multi-file coordination and reasoning over extended contexts.
- Testing Multi-Agent Systems: fuzzing-based analysis reveals multi-agent code generation fails on 7.9%–83.3% of previously solved problems after minor mutations, with the planner-coder gap accounting for 75.3% of robustness failures.
