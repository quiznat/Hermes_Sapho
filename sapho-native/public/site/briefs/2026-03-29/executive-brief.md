# Executive Brief

## Executive Summary

Empirical research has displaced speculation in the discourse on AI-assisted software engineering. Across eight studies analyzing real developer behavior, configuration patterns, and system performance, a consistent pattern emerges: skilled practitioners treat AI tools as instruments requiring active configuration and strategic oversight, not as autonomous agents worthy of delegated authorship. Yet these same studies expose structural failure modes—coordination breakdowns in multi-agent systems, robustness gaps between planning and execution, and significant distances between laboratory benchmarks and production-grade reliability—that current metrics fail to capture. The field is shifting toward field-grounded methodology, large-scale artifact analysis, and systematic taxonomies of real-world usage, yielding a clearer picture of where AI coding tools deliver value and where they remain dangerously brittle.

## Signals To Watch

- **Configuration as Control**: Developers increasingly encode domain knowledge and constraints into local configuration files ("Cursor rules," Claude Code configs), treating AI tools as customizable instruments rather than oracles—watch for standardization of these patterns and their impact on team velocity.
- **The Planner-Coder Gap**: Multi-agent systems show critical robustness failures at the planning-execution boundary that headline accuracy metrics miss—coordination breakdowns here may limit autonomous coding agents to narrow, well-scoped tasks despite impressive individual component performance.
- **Benchmark-Production Divergence**: SWE-bench and similar real-world evaluation frameworks are revealing systematic gaps between laboratory performance and production software engineering—expect pressure on model providers to optimize for integration complexity, not just isolated task completion.
- **Empirical Turn in Research**: The shift from theoretical capability claims to large-scale analysis of commits, configs, and developer behavior suggests the field is maturing—watch for consolidation of findings into actionable engineering best practices and tooling standards.
- **Adoption vs. Integration Tension**: Evidence of coding agent adoption on GitHub exists, but the dominant pattern is human-maintained control structures—monitor whether enterprise adoption follows the "vibe coding" narrative or the "controlled instrumentation" reality documented in current research.
