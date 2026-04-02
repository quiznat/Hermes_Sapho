# Queue Item Processing — art-2026-03-01-006

## Source metadata
- URL: https://github.com/Leonxlnx/taste-skill
- Source type: GitHub repository
- Lane tags: `UI-design`, `agent-research`
- Processed at (UTC): 2026-03-01T20:25:00Z

## Enrichment artifacts consulted
- Repo landing page summary
- README: `https://raw.githubusercontent.com/Leonxlnx/taste-skill/main/README.md`
- Repo contents listing (GitHub API)
- Main skill artifact: `taste-skill/SKILL.md`

## Structured extraction

### What it is
A packaged set of prompt/skill instructions for frontend code generation quality control. The repository separates responsibilities into three skill files: a design-taste skill, a redesign skill, and an output-discipline skill.

### Mechanism worth retaining
The strongest reusable idea is explicit **control dials** that parameterize generation behavior (`DESIGN_VARIANCE`, `MOTION_INTENSITY`, `VISUAL_DENSITY`) instead of relying on vague style adjectives. This creates reproducible variation and easier team-level tuning.

### Additional useful design-governance patterns
- Anti-slop rules that ban common LLM output shortcuts (placeholder comments, incomplete code output).
- Dependency-verification guardrails before importing UI libraries.
- Performance guardrails for motion-heavy UI (transform/opacity preference, no layout-thrashing animations).
- Explicit anti-pattern bans (emoji use, cliché layout patterns), making style constraints testable.

## Lane interpretation
This is not core memory-system research, but it is high-signal for the **Design Lane** and for prompt-governance patterns that can be reused in broader agentic software-factory workflows.

## Decision
- Decision: **retain**
- Rationale: concrete, reusable prompt-engineering structure with parameterized controls and enforceable output constraints.
- Confidence: medium-high (clear artifacts and implementation detail in repository docs).

## Processing notes
Candidate follow-up: map this skill’s dial-and-guardrail design into a generic “quality policy layer” template for non-design coding agents.
