# Multi-Agent Workflow → see Execution Profiles

## Status

Superseded scaffold. Redirects to the profile model.

## Why this moved

WERA no longer organises the architecture by agent count. A multi-agent workflow is now described as an **execution profile** with `actor_topology: multi_agent` (or `cross_runtime`), using the same concepts as every other point on the spectrum. See [ADR 0001](../decisions/0001-workflow-run-central-unit.md).

## Where to go

- Multiple delegated agents coordinated by the workflow: [EP4 — Agent-directed under workflow constraints](../profiles/ep4-agent-directed.md) and pattern [WP10 — Multi-agent delegation](../patterns/wp10-multi-agent-delegation.md)
- Handoff across agents or runtimes: [EP7 — Cross-runtime handoff](../profiles/ep7-cross-runtime-handoff.md) and pattern [WP11 — Cross-runtime handoff](../patterns/wp11-cross-runtime-handoff.md)
- A single bounded agent region inside a workflow: [EP3 — Bounded agentic region](../profiles/ep3-bounded-agentic-region.md)
- Start here: [workstream README](../README.md) · [classification](../model/classification.md)
