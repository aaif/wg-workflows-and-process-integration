# Single-Agent Workflow → see Execution Profiles

## Status

Superseded scaffold. Redirects to the profile model.

## Why this moved

WERA no longer organises the architecture by agent count. A single-agent workflow is now described as an **execution profile** with `actor_topology: single_agent`, using one set of concepts that spans the whole determinism spectrum. See [ADR 0001](../decisions/0001-workflow-run-central-unit.md).

## Where to go

- Workflow-directed with a model-assisted step (the common "single-agent" case): [EP2 — Workflow-directed + model-assisted](../profiles/ep2-workflow-directed-model-assisted.md)
- Fully deterministic: [EP1 — Workflow-directed](../profiles/ep1-workflow-directed.md)
- A bounded agent given a delegated goal: [EP3 — Bounded agentic region](../profiles/ep3-bounded-agentic-region.md)
- Start here: [workstream README](../README.md) · [classification](../model/classification.md)
