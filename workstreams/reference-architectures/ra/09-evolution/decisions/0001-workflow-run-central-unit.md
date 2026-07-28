# ADR 0001: Workflow Run as the Central Unit

## Status

Proposed

## Date

2026-07-27

## Context

Classifying the reference architecture primarily by "single-agent vs multi-agent" makes agent count appear more fundamental than execution, state, effects, and authority. It also forces two parallel architectures and leaves deterministic and hybrid workflows homeless.

## Options considered

- **Agent-count-first** — top-level split into single-agent and multi-agent RAs. Familiar, but fragments the model and privileges a secondary property.
- **Workflow-run-first** — one architecture centred on the run, with agent count as one classification axis.

## Decision

Use the **workflow run** as the central architectural unit. Treat agent count and actor topology as one classification axis (`actor_topology`), not the organising principle.

## Rationale

One conceptual centre covers the whole spectrum — deterministic, model-assisted, hybrid, bounded-agentic, multi-agent, cross-runtime — with a single vocabulary, and matches the charter's framing of workflows that coordinate agents, tools, and humans.

## Consequences

The prior `ra-single-agent` and `ra-multi-agent` scaffolds are superseded by [profiles](../../04-profiles/README.md): all concepts are defined once and specialised via coordinates rather than split by agent count.

## Follow-up

Confirm the profile catalogue (`EP1`–`EP7`) adequately covers what the two former RAs were meant to describe.
