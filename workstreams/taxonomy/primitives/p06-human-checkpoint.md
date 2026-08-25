# P6 HumanCheckpoint

**Obligation:** MUST

## Definition

A point at which the workflow pauses, durably, for a human decision.

## Why it exists

Without a durable, named pause primitive, "human in the loop" becomes an informal side channel outside the workflow's own state machine: not resumable, not auditable, and not distinguishable from the workflow simply having stalled.

Wherever the Governance, Risk & Regulatory Alignment WG's analysis determines a human decision point is mandatory, only a state-machine-native pause can evidence that it happened; a side channel cannot. This RA does not specify which classes of task or tool require a mandatory checkpoint under a given regulatory regime. That threshold is an external input from that WG. What this RA does specify: an agent MUST NOT be granted an `irreversible` tool without either a `P6 HumanCheckpoint` or a deterministic policy gate in front of it, and the confidence signal required in every `AgentStep` output contract is what a low-confidence `P3 Decision` routes to a checkpoint on.

## Prior art

| System | Nearest equivalent |
| --- | --- |
| BPMN 2.0 | User task + gateway |
| n8n | `sendAndWait` operation |
| AWS Step Functions | `.waitForTaskToken` |
| Temporal | Signal |
| LangGraph | `interrupt()` |

Nearest equivalent is editorial judgment, not a conformance claim.

## Relationship to other primitives

- [P3 Decision](p03-decision.md): the low-confidence or irreversible-action branch typically routes here.
- [P4 AgentStep](p04-agent-step.md): tool scope element 4 requires a checkpoint or a deterministic gate in front of any `irreversible` tool.
- [P10 Escalation](p10-escalation.md): an escalation's usual destination.
- [P19 EvaluationGate](p19-evaluation-gate.md): a strong evaluation gate is what lets a bounded iteration loop *not* need a human in its inner loop.
