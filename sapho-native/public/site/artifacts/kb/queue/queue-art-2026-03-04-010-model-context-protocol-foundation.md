# Queue Artifact — art-2026-03-04-010

Source URL: https://modelcontextprotocol.io/  
Canonical URL: https://modelcontextprotocol.io/  
Lane: agent-memory  
Decision: retain

## Thesis

MCP should be treated as foundational interface infrastructure for agent systems: a standardized protocol boundary between AI hosts and external tools/data, rather than ad-hoc connector logic per application.

## Mechanism summary

MCP defines explicit host/client/server roles over a JSON-RPC data layer plus transport layer, with core primitives (tools, resources, prompts) and lifecycle/capability negotiation. The architectural value is separation of durable system state from invocation-time context and standardized retrieval/action surfaces, enabling interoperability, composability, and observability across local/remote integrations.

## Confidence

Medium-high. This is the official protocol documentation (normative/authoritative for interface semantics), though not a third-party empirical benchmark.

## Why it matters for Sapho

Directly relevant to Sapho memory and orchestration design: enforce protocol-level contracts for context exchange, scoped capability exposure, and auditable tool/data interactions across heterogeneous agent components.
