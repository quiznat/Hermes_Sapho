# Queue Artifact — art-2026-03-02-023

Source URL: https://github.com/a2aproject/A2A  
Lane: agent-factory  
Decision: retain

A2A (Agent2Agent) is an open interoperability protocol for communication between independently built agentic systems. The core mechanism is protocol-level coordination rather than model-level consolidation: agents can discover each other via agent cards, negotiate interaction modalities, execute long-running collaboration patterns, and exchange rich payloads while preserving internal opacity (no mandatory exposure of private memory/tools).

For software-factory design, this matters because it formalizes a boundary between orchestration and implementation internals. It provides a practical route to multi-agent composition across heterogeneous frameworks (ADK/LangGraph/BeeAI and others) while maintaining enterprise requirements around auth, observability, and transport reliability (JSON-RPC over HTTP(S), streaming/async support).

The operating implication for Sapho-style factory systems is to treat cross-agent contracts as first-class governance artifacts. If inter-agent calls are standardized and capability discovery is explicit, orchestration can stay auditable while specialist agents evolve independently.
