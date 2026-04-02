# Executive Brief

## Executive Summary

Two studies demonstrate that LLM systems can break through static performance limits by embedding automated learning directly into their operational loops. The first shows evolutionary search outperforming few-shot prompting on specialized verifiers and ARC-AGI benchmarks. The second demonstrates a text-to-SQL system that accumulates institutional knowledge through continuous feedback without manual curation. Both achieve gains not by scaling models or refining prompts, but by architecting self-reinforcing loops that harvest and redeploy knowledge from prior runs. The implication: performance ceilings in constrained domains may be less about model capability and more about missing feedback infrastructure.

## Signals To Watch

- Production deployments separating inference from learning loops to enable continuous, unattended knowledge accumulation
- Evolutionary and genetic methods resurging as viable optimizers when fine-tuning or prompt engineering plateau
- Knowledge management systems shifting from manual documentation to automatic extraction from execution traces
- Vertical applications (code verification, SQL generation) outperforming generalist models through domain-specific feedback architectures
- Infrastructure investments prioritizing feedback loop latency and knowledge retrieval over raw model capacity
