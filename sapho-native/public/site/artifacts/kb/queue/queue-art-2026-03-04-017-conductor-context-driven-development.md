# Queue Artifact — art-2026-03-04-017

Source URL: https://developers.googleblog.com/conductor-introducing-context-driven-development-for-gemini-cli/  
Canonical URL: https://developers.googleblog.com/conductor-introducing-context-driven-development-for-gemini-cli  
Lane: agent-memory  
Decision: retain

## Thesis

Conductor reframes AI coding workflow from chat-session memory to repository-native memory by requiring persistent specs and plans as first-class artifacts before implementation.

## Mechanism summary

The extension introduces a three-step loop: establish project context (`/conductor:setup`), generate track-scoped specs and plans (`/conductor:newTrack`), then execute against the approved plan (`/conductor:implement`). Because context and task state live in Markdown files committed alongside code, developers can pause/resume, collaborate across machines, and enforce team standards (testing strategy, stack conventions, product goals) without losing agent alignment. The strongest mechanism claim is on brownfield work: Conductor explicitly bootstraps architecture/guideline context for existing repositories, then updates it as work progresses.

## Confidence

Medium. The source is a product announcement (not independent benchmarking), but the workflow mechanics are concrete and implementation-specific.

## Why it matters for Sapho

This is directly aligned with Sapho Chapterhouse Institute doctrine that files are the durable control plane. It strengthens the lane thesis that agent reliability at scale depends on explicit, versioned context artifacts rather than transient chat memory.
