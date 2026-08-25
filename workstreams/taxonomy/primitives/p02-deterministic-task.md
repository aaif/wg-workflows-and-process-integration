# P2 DeterministicTask

**Obligation:** MUST

## Definition

A fixed-function step: given the same input, it always takes the same path.

## Why it exists

Without a name for "this is not the agent" step, every step in the workflow looks equally suspect, and there's no clear answer when the checklist's most common verdict comes up: this is just a plain deterministic step, no `AgentStep` needed.

`P2` is the default, not the exception. It gets its own name so it doesn't quietly get rebuilt as an `AgentStep` just because it's convenient, or because someone wanted "AI" in the process somewhere. The determinism-hints guidance is clear on what belongs here: closed-set classification with stable labels, arithmetic, eligibility checks, thresholds, entitlement, and routing between known handlers. None of that should go to a model.

Retry and idempotency logic belong here too, owned by the orchestrator rather than the agent, since agents retry unpredictably and without the orchestrator's visibility into what happened.

## Prior art

| System | Nearest equivalent |
| --- | --- |
| BPMN 2.0 | Service task / script task |
| n8n | Action node |
| AWS Step Functions | Task state |
| Temporal | Activity (deterministic code path) |
| LangGraph | Node |

Nearest equivalent is editorial judgment, not a conformance claim.

## Relationship to other primitives

- [P3 Decision](p03-decision.md) — the deterministic branch a `P2` step often feeds into or follows.
- [P4 AgentStep](p04-agent-step.md) — the checklist's first question ("can the task be fully enumerated at design time?") routes here when the answer is yes.
- [P9 ErrorBoundary](p09-error-boundary.md) — retry and idempotency logic belongs to the orchestrator's deterministic layer, not to an agent.
