# P8 TimerDeadline

**Obligation:** MUST

## Definition

A wall-clock bound on a step, a handoff, or the workflow as a whole.

## Why it exists

Without a wall-clock bound, a `HumanCheckpoint` or a cross-organisational `Handoff` can wait indefinitely. That is exactly the "deadlock waiting on a peer" failure mode: a `delegate_and_wait` handoff that never returns because the receiver never completes and no deadline was set.

`P8` is the one primitive in this set that every reviewed system already implements natively, unlike `P13 Budget`, which no reviewed system has. That makes skipping a timer a pure design oversight rather than an unsolved problem: every `P16 Handoff` MUST carry its own deadline, with no exception for "the receiver is trusted" or "the receiver is usually fast."

## Prior art

| System | Nearest equivalent |
| --- | --- |
| BPMN 2.0 | Timer boundary event |
| n8n | Wait node |
| AWS Step Functions | Wait state / timeouts |
| Temporal | Durable timer |
| LangGraph | No first-class primitive, composed around the graph |

Nearest equivalent is editorial judgment, not a conformance claim.

## Relationship to other primitives

- [P6 HumanCheckpoint](p06-human-checkpoint.md): a checkpoint with no deadline can stall the workflow indefinitely.
- [P16 Handoff](p16-handoff.md): a mandatory deadline is one of the handoff contract's seven declared elements.
- [P10 Escalation](p10-escalation.md): the usual destination when a timer fires with no response.
