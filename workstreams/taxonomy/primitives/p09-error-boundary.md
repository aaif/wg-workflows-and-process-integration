# P9 ErrorBoundary

**Obligation:** MUST

## Definition

Typed failure capture and handler routing.

## Why it exists

Without typed failure capture, every failure looks identical to the orchestrator, and "retry logic inside the agent" happens by default because the agent is the only thing that noticed the failure. This is an anti-pattern this RA calls out directly, since agents retry non-idempotently and without the orchestrator's visibility, and a failed tool call retried by the model can double-execute a `reversible_write`, or worse.

Retry and idempotency belong to the orchestrator, not the model, per the determinism-hints guidance. `P9` is the seam where that ownership is structurally asserted: it is the workflow's declared point for catching a typed failure and routing it, rather than leaving the agent to notice and react to its own errors.

## Prior art

| System | Nearest equivalent |
| --- | --- |
| BPMN 2.0 | Error boundary event / event sub-process |
| n8n | Error-output connection on a node |
| AWS Step Functions | Catch / Retry |
| Temporal | Activity retry policy |
| LangGraph | Composed via graph-level exception handling |

Nearest equivalent is editorial judgment, not a conformance claim.

## Relationship to other primitives

- [P10 Escalation](p10-escalation.md): where an unresolved error routes when retry is exhausted or inappropriate.
- [P11 Compensation](p11-compensation.md): the undo path for a completed effect when an error surfaces after the fact.
- [P2 DeterministicTask](p02-deterministic-task.md): retry and idempotency logic is orchestrator-owned, deterministic work.
