# LLM-based Evolution as a Universal Optimizer

## Source metadata
- Title: LLM-based Evolution as a Universal Optimizer
- URL: https://imbue.com/research/2026-02-27-darwinian-evolver/
- Source type: Sapho Daily artifact
- Curated at (UTC): 2026-03-22T18:24:58Z
- Finalized at (UTC): 2026-03-27T17:04:41Z

## Core thesis
Imbue has developed LLM-driven evolution as a general-purpose optimization method that sidesteps the manual, tedious work typically required to refine LLM-based systems. By treating code and agent behavior as evolvable populations rather than fixed prompts, the approach achieved substantial gains where conventional optimization techniques failed due to context constraints.

## Why it matters for Sapho
Existing prompt optimization frameworks like DSPy's MIPRO rely heavily on few-shot prompting, which becomes infeasible for complex agent systems with tight context limits. This evolutionary approach not only enabled the creation of Vet—a coding agent verifier that uses LLMs to review and improve another agent's work—but also more than doubled reasoning performance on ARC-AGI benchmarks, offering a scalable alternative for end-to-end LLM system optimization.

## Key findings
- LLM-driven evolution proved to be an efficient, general method for optimizing both code and agent behavior
- The technique was instrumental in developing Vet, a system that deploys LLMs and agents to verify and suggest improvements on the work of separate coding agents
- Code evolution more than doubled model reasoning performance on ARC-AGI tasks
- The Darwinian Evolver tool is being released as open source

## Limits
The findings presented are drawn from a partial excerpt and may not reflect the full experimental scope, methodological constraints, or broader limitations discussed in the complete article.
