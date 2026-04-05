<details class="traceability-panel">
<summary>Traceability</summary>
<div class="traceability-body">
<ul>
  <li><strong>Source:</strong> <a href="https://arxiv.org/html/2510.21413" target="_blank" rel="noopener">https://arxiv.org/html/2510.21413</a></li>
  <li><strong>Intake queued:</strong> 2026-03-04T01:14:24Z</li>
  <li><strong>Source captured:</strong> 2026-03-07T19:27:14Z</li>
  <li><strong>Curated:</strong> 2026-04-02T18:14:51Z</li>
  <li><strong>Artifact finalized:</strong> 2026-04-02T18:17:10Z</li>
  <li><strong>Artifact published:</strong> 2026-03-29T03:09:24Z</li>
</ul>
</div>
</details>

# Context Engineering for AI Agents in Open-Source Software

## Core Thesis

Open-source repositories had low visible uptake of the agent-configuration formats this study examined, and the instruction files that do exist do not yet look like a settled engineering standard. Adoption was sparse in the sampled repositories, structure in AGENTS.md files was recurrent but not standardized, and maintenance patterns suggest many instruction files are created once and then lightly tended rather than continuously engineered.

## Why It Matters for Sapho

This matters because it cuts against any assumption that repository-native agent guidance is already a mature operating layer in software. For Sapho, the field signal is not “best practice has converged,” but “a thin, uneven, still-forming instruction surface is emerging.” That changes evaluation doctrine: Sapho should treat agent-facing repository context as a real but early coordination primitive, judge it by observed specificity and upkeep rather than by file presence alone, and remain alert to the gap between visible enthusiasm for agents and actual disciplined maintenance of instruction artifacts.

## Key Findings

- In a preliminary scan of 10,000 repositories drawn from a larger filtered pool of 49,311, only 466 repositories, 5%, contained at least one of the four examined agent-configuration file types: Copilot instructions, CLAUDE.md, AGENTS.md, or GEMINI.md.
- Among repositories that did use one of those files, TypeScript was the largest language group at 135 repositories, followed by Go and Python at 58 each, C# at 56, Java at 36, JavaScript at 34, C++ at 32, Rust at 29, PHP at 19, and C at 9.
- AGENTS.md files showed recurring topic clusters but not a shared template: the most common heading categories were conventions or best practices (50), contribution guidance (48), and architecture or project structure (47), yet the paper still reports wide variation in information content and presentation.
- Maintenance was often shallow. Of 155 AGENTS.md files examined for change history, 77 files, 50%, were never changed after the initial commit; 36, or 23%, changed once; and 32, or 21%, changed between two and seven times.
- Where AGENTS.md files were actively revised, edits were mostly instruction work rather than cosmetic churn: in the high-change subset, added instructions appeared 78 times and modified instructions 59 times.

## Evidence and Findings

- The source shows that only 466 out of 10,000 scanned repositories had at least one of four targeted agent-configuration file types. That supports a bounded claim of low visible adoption in this sample, and it matters because the practical baseline for repository-native agent context is still thin rather than widespread.
- The language distribution among repositories with these files was uneven but not monocultural: TypeScript led with 135 repositories, while Go and Python each had 58, C# had 56, and several other languages appeared at smaller counts. That supports a cross-language adoption pattern rather than a single-ecosystem phenomenon, and it matters because agent-context practices are spreading across software stacks without yet showing uniform depth or dominance.
- The heading analysis for AGENTS.md began with 155 files, excluded 15 created before 2025 and 5 without heading structure, and examined only level 1 and level 2 headings. Within that bounded view, conventions, contribution guidance, and architecture were the most common categories. This supports the conclusion that authors are converging on some repeated concerns, and it matters because the field seems to agree more on what problems instruction files should address than on how those files should actually be organized.
- The same source also reports that AGENTS.md files vary widely in content and presentation and do not exhibit a consistent structure. That supports a non-convergence claim despite recurring themes, and it matters because file existence cannot be treated as evidence of stable repository-to-agent interface quality.
- Change-history evidence shows a split pattern: half of the examined AGENTS.md files were never revised after creation, but a smaller high-change subset generated 169 commits across 10 files, with added and modified instructions dominating the coded changes. That supports the view that most projects treat these files as lightly maintained, while a more engaged minority uses them as live operational documents. This matters because maturity in the practice is concentrated, not general.
- Supporting detail from file-shape evidence points in the same direction: Copilot instruction files averaged 310 lines with standard deviation 127, while AGENTS.md averaged 142 lines with a much larger standard deviation of 231, and AGENTS.md plus CLAUDE.md was the most common co-occurring pair, appearing together in 25 repositories. These patterns support the conclusion that repository teams are experimenting with multiple context surfaces and varied document scope rather than following one settled format.

## Contradictions and Tensions

- The clearest tension is between recurring content themes and absent structural convergence. Repositories repeatedly cover conventions, contribution guidance, and architecture, but they do not package those topics into a consistent format. The field appears to agree on some needs without agreeing on the interface.
- There is also a maintenance tension between the full AGENTS.md set and the high-change subset. Most files were never revised after creation or changed only once, yet the most actively maintained files show repeated instruction additions and modifications. That implies two different operating modes: many projects treat agent guidance as static documentation, while a smaller minority treats it as an actively tuned control surface.
- Cross-language spread cuts against an easy “single ecosystem fad” reading, but the absolute prevalence figure remains low at 5% of the scanned sample. The practice is distributed enough to matter, yet still sparse enough that broad maturity claims would outrun the evidence.
- File co-occurrence creates another interpretive tension. The most common pair was AGENTS.md with CLAUDE.md, which suggests some projects are layering agent-context surfaces instead of standardizing on one. That may indicate richer context engineering, but it may also signal format fragmentation rather than progress toward a common convention.

## Mechanism or Bounds

The strongest supported explanation is operational rather than causal: repository teams appear to be using agent-instruction files as local coordination documents that encode conventions, contribution expectations, and project structure for machine-assisted development, but they are doing so through multiple file types and highly variable document designs. The evidence supports that bounded functional reading because repeated heading categories and instruction-change patterns point to practical guidance work, not merely decorative metadata.

The bounds are important. The prevalence result covers only four file formats supported by a specific GitHub Copilot coding-agent context, so it does not measure all forms of repository-native agent guidance. The structure analysis is limited to a filtered AGENTS.md subset and to level 1 and level 2 headings. The evolution analysis for detailed change categories rests on 10 high-change files and 169 commits, so it shows how active files evolve more than how the full population evolves.

## Limits

The paper does not establish why adoption is low, why TypeScript leads, or whether the observed language distribution simply mirrors the underlying repository population.

It also does not show how much these files improve agent performance, correctness, or developer outcomes. The study observes presence, structure, and change behavior, but not downstream effect.

Structural conclusions about AGENTS.md are bounded by filtering choices and heading-level restriction. A stronger claim about full-document organization or instruction semantics would not be justified from this evidence alone.

The change-history evidence is uneven: the broad set suggests stability or neglect, while the detailed annotation comes from a small high-change minority. That means the study can show a real split in maintenance behavior, but not a settled account of the dominant lifecycle for repository instruction files in open source.
