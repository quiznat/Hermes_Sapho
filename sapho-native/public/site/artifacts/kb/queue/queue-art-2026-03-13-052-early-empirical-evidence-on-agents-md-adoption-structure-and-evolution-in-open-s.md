# Queue Item Processing — art-2026-03-13-052

## Source metadata
- URL: https://arxiv.org/html/2510.21413v4
- Source type: firehose-brave
- Lane tags: `agent-memory, agent-memory`
- Curated at (UTC): 2026-03-13T11:34:00Z
- Finalized at (UTC): 2026-03-13T20:09:20Z

## Source custody
- Source snapshot: `research/evidence/source-material/2026-03-13/art-2026-03-13-052.json`
- Clean text path: `research/evidence/source-material/2026-03-13/art-2026-03-13-052.txt`

## Core thesis
AI configuration files for coding agents are emerging but still immature as a practice: adoption is low, structure is not standardized, and projects iteratively refine instructions and sections over time.

## Mechanism summary
The study mines GitHub repositories selected via software-project filters, detects tool-specific AI configuration files, then performs focused qualitative and quantitative analysis on AGENTS.md content and commit histories. It finds that 466 of 10,000 scanned repositories, or 5%, had adopted at least one considered AI configuration format; among AGENTS.md files, heading structures are highly heterogeneous even though recurring categories such as conventions, contribution guidance, architecture, build commands, and testing instructions appear repeatedly. Evolution analysis shows that half of AGENTS.md files did not change after creation, while more active files were updated mainly through incremental instruction edits rather than wholesale restructuring.

## Why it matters for Sapho
This matters because it provides one of the first empirical baselines for real-world context-engineering practice rather than treating agent instruction files as a purely anecdotal convention. Its significance is that AGENTS.md and related artifacts appear to be early-stage coordination infrastructure: adoption is still limited, projects have not converged on a standard structure, and maintenance behavior suggests teams refine instructions locally as they learn what agents need, which makes these files an increasingly important but still immature interface for shaping agent behavior.

<!-- canonical-empirical-findings -->

## Empirical Findings (Data Snapshot)

| Novel finding | Quantitative result | Experimental setup/sample | Metric/outcome | Caveat/limit |
|---|---|---|---|---|
| Adoption of AI configuration files is currently limited among the sampled engineered open-source repositories. | 466 out of 10,000 scanned repositories (5%) had adopted at least one considered AI configuration format. | From a filtered pool of 49,311 repositories, the authors sampled 10,000, cloned default branches, and scanned for Copilot instructions, CLAUDE.md, AGENTS.md, and GEMINI.md. | The observed adoption baseline is low in this sample, indicating an early-stage ecosystem. | The scan covered only four commercial-tool file formats and one 10,000-repository subset of a larger candidate pool. |
| AI configuration file usage and document lengths vary by language and file type. | Language counts with detected files: TypeScript 135, Go 58, Python 58, C# 56, Java 36, JavaScript 34, C++ 32, Rust 29, PHP 19, C 9. Mean line counts: Copilot instructions M=310 (SD=127), CLAUDE.md M=287 (SD=112), AGENTS.md M=142 (SD=231), GEMINI.md M=106 (SD=65). | The authors summarized detected AI-config files across repositories and computed per-format length statistics. | AGENTS.md shows the highest dispersion, while Copilot and CLAUDE.md files are longer on average. | Counts reflect repositories with AI configuration files in the sampled dataset, not all repositories per language. |
| AGENTS.md information architecture is highly heterogeneous, though recurring content categories are emerging. | For RQ2, analysis started from 155 AGENTS.md files; 15 pre-2025 files and 5 files without headings were excluded for heading-structure analysis. Frequent level-1/2 heading categories include Conventions/Best Practices (50), Contribution Guidelines (48), Architecture/Project Structure (47), Build Commands (40), and Testing Instructions (32). | Section headings were normalized (lowercased, lemmatized), grouped via manual coding into conceptual categories, and counted at heading levels 1–2. | No established standard structure was found, but common topical clusters are visible across projects. | Initial coding focused on headings with minimum cross-repository frequency thresholds. |
| Half of AGENTS.md files did not evolve after creation, but highly active files show repeated instruction-level edits. | Of 155 AGENTS.md files: 77 (50%) had no post-initial changes, 36 (23%) changed once, and 32 (21%) changed 2–7 times. Deep-dive sample: 10 files (≥10 commits), 169 annotated commits (37% of 453 collected), with 111 commits (66%) mapped to a single change category. | Manual commit-level annotation used diffs, commit messages, and linked issues/PRs to induce change categories. | Evolution is often sparse overall, but active files undergo frequent localized instruction edits. | Detailed evolution coding was limited to files with at least 10 commits. |
| Instruction-level maintenance dominates AGENTS.md edits over structural rewrites. | Top change-category frequencies (Table 2): Add instruction(s) 78, Modify instruction(s) 59, Add section(s) 26, Remove instruction(s) 23. | Categories were induced and applied during manual coding of commit histories for highly active AGENTS.md files. | Most maintenance concentrates on incremental instruction updates rather than wholesale file restructuring. | Category counts indicate frequency across coded commits and do not distinguish single vs. multiple occurrences within one commit. |

## Confidence
high

Justification: The source is a primary arXiv empirical study with explicit sampling, quantitative adoption statistics, structured content analysis, and commit-history coding, so the evidence is strong for claims about current AGENTS.md practice. The main caveats are that the scan covers only a subset of repository formats and sampled repositories, and the deeper evolution analysis is limited to the more active AGENTS.md files.
