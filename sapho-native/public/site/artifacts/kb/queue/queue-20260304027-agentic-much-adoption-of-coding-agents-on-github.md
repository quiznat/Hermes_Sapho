# Agentic Much? Adoption of Coding Agents on GitHub

## Core Thesis

Coding-agent use on GitHub is already material rather than marginal, with the study estimating adoption at 15.85% to 22.60% across 129,134 projects. The central finding is not just that agent use is visible at scale, but that visible file traces alone miss a meaningful share of usage, so any governance or evaluation doctrine built only on obvious repository artifacts will understate how much agent-assisted coding is already happening.

## Why It Matters for Sapho

This matters because Sapho needs to reason about AI software production as an operational reality, not a speculative edge case. The paper supports a stricter doctrine for reading software ecosystems: repository-visible traces are useful, but absence of obvious file markers is not strong evidence of absence. For Sapho, that pushes evaluation toward multi-trace detection, explicit uncertainty about hidden use, and caution against treating neat surface signals as a full account of system behavior or adoption depth.

## Key Findings

- The study estimates coding-agent adoption on GitHub at 15.85% to 22.60% across 129,134 projects, indicating that agent-assisted development is already present in a substantial minority of public repositories.
- File-level heuristics alone identified 10,191 of 129,134 projects, or 7.89%, but a further sample of repositories that looked negative at the file level still showed 8.64% commit-level adoption, which means file traces materially undercount use.
- The adoption measure is built from four heuristic categories: file-based, author-based, branch-based, and label-based signals, making the result a structured observational estimate rather than a direct census.
- The methodology was deliberately conservative: ambiguous files such as CONVENTIONS.md were excluded, and AGENTS.md alone was treated as insufficient for tool-specific identification, which reduces false positives but leaves plausible use uncounted.
- Adoption is not evenly distributed. File-level adoption reached 21.17% in the youngest project age decile versus 4.69% in the oldest, and repositories from the top twenty organizations showed 10.18% adoption versus a 7.89% overall file-level baseline.
- Observed agent activity is concentrated rather than diffuse: the top five coding agents account for more than 80% of observed adoption, and Claude plus Copilot alone account for more than half.

## Evidence and Findings

- Across 129,134 projects, the paper estimates coding-agent adoption at 15.85% to 22.60%. That supports the conclusion that coding agents are already a live part of mainstream software production on GitHub, not an anecdotal niche, which matters because ecosystem judgments that assume human-only coding are increasingly miscalibrated.
- File-level heuristics found only 7.89% adoption, but among 15,783 repositories with no file-level signal, 1,364 still showed commit-level adoption, or 8.64%. This supports the conclusion that visible repository files capture only part of agent use, which matters because detection systems built around obvious configuration or instruction files will systematically miss real deployment.
- The detection pipeline combines four heuristic classes—file, author, branch, and label signals—and the paper explicitly frames them as heuristics rather than complete observation. That supports a bounded conclusion: the study offers a credible operational estimate of prevalence, but not an exhaustive map of all use, which matters because policy and measurement should treat the number as informative but incomplete.
- The authors intentionally excluded or discounted ambiguous traces, including excluding CONVENTIONS.md and refusing to treat AGENTS.md by itself as agent-specific proof. This supports the conclusion that the measurement strategy prioritized attribution precision over maximal capture, which matters because the headline estimate is more plausibly conservative than inflated.
- Adoption appears strongest in newer repositories, with 21.17% file-level adoption in the youngest age decile versus 4.69% in the oldest, and somewhat higher in major organizations, where the top twenty organizations reached 10.18% against a 7.89% overall file-level rate. This supports the conclusion that coding-agent use is not uniformly distributed across the software landscape, which matters because field-level averages hide where workflow change is arriving fastest.
- The paper also shows behavioral texture rather than just prevalence: AI-assisted commits were larger by median added lines, 34 versus 10 for human-authored commits, and in a random sample of 790 Claude Code commits, 35.7% were feature work and 29.9% were fixes. This supports the conclusion that observed agent use is tied to substantive implementation work rather than only trivial edits, which matters because it shifts the practical question from whether agents are used to how much meaningful production work they are already carrying.

## Contradictions and Tensions

- The clearest tension is between the 7.89% file-level adoption rate and the 8.64% commit-level adoption found inside projects that looked negative at the file level. The measurement surface says one thing if you inspect repository files and another if you inspect commit traces, so the paper simultaneously demonstrates adoption and the incompleteness of one of its own most legible signals.
- The study gains credibility by using conservative attribution rules, but that same conservatism creates an interpretive tradeoff. Excluding ambiguous files reduces false positives, yet it also means plausible agent use is left out, so stricter methodology improves trust in observed positives while weakening completeness.
- The distributional findings are strong enough to matter but not strong enough to explain themselves. Younger projects show much higher adoption than older ones, and large organizations sit above the overall file-level baseline, but the paper does not establish whether this is driven by project age, workflow modernity, organizational policy, repository visibility, or some other confound.
- Tool concentration is visible, with the top five agents accounting for more than 80% of observed adoption, yet exact attribution is still partly blurred because generic traces cannot always be mapped cleanly to a specific agent. That leaves a tension between clear market concentration and imperfect tool-level measurement.
- The adoption curve accelerates sharply through early and mid-2025, then slows slightly by late August 2025. That suggests rapid diffusion, but without a causal test it is hard to tell whether the slowdown reflects market saturation, measurement lag, changed repository behavior, or a temporary pause in visible trace creation.

## Mechanism or Bounds

The strongest supported mechanism is observational leakage across trace types. Some repositories leave detectable signs in commits, authors, branches, or labels without leaving clear agent-related files in the repository itself, so file-based inspection captures only a subset of actual use. The study therefore supports a bounded operational explanation: coding-agent adoption is partially visible through repository traces, but the visibility depends on how teams externalize agent use into artifacts that the detection system can see.

That mechanism is about measurement, not causation. The paper does not establish why newer projects or large organizations adopt more; it only shows that adoption differs across those groups under the study's heuristic frame. More broadly, the prevalence estimate is bounded by public GitHub repositories and by the four heuristic categories the authors could operationalize. Use that happens off-platform, in private workflows, in squashed histories, or without recognizable trace patterns can fall outside view.

## Limits

- The adoption estimate is heuristic rather than census-based, so it should be read as a structured lower-bound-leaning observation, not a definitive count of all coding-agent use on GitHub.
- The evidence strongly suggests undercounting, but it does not quantify the full size of the hidden layer; the true gap between observed and actual use remains unresolved.
- Group differences by repository age and organization size are descriptive only. The paper does not identify the causal drivers behind those differences.
- Tool-level attribution is incomplete where traces are generic or ambiguous, so concentration findings are directionally useful but not perfectly clean at the product level.
- Some behavioral findings, including the task-type sample of 790 Claude Code commits, are narrow slices rather than platform-wide behavioral measures, so they sharpen interpretation without fully characterizing all agent-mediated coding work.
