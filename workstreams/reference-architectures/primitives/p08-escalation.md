# P8 Escalation

**Obligation:** MUST \
**Used in patterns:** [Human approval gate](../patterns/human-approval-gate.md) · [Bounded convergence loop](../patterns/bounded-convergence-loop.md)

## Definition

Hands a stuck or out-of-policy execution to a person or a higher authority.

## Why it exists

Without its own primitive, escalation gets merged into error handling (`P7`)
or into an ordinary checkpoint (`P5`). An approver saying "this is above my
level", an agent saying it can't proceed, and a deadline running out each need
a different response from a transient error or a routine review. Four of the
five runtimes we reviewed have no native equivalent, so it has to be built
from other pieces.

## How the patterns use it

- **Human approval gate.** Pending approval needs an escalation or expiry path.
  Escalation starts when the approver chooses *escalate* or the deadline
  (`P6`) fires. It can go to another authorized approver at the same gate,
  with a new deadline, or hand the run to a human-owned process outside the
  workflow. If the path runs out, the run expires.
- **Bounded convergence loop.** When the retry criteria no longer allow
  another attempt, escalation is one of the permitted exits.

An agent task can also ask for escalation directly through its termination
conditions (`P3`).

Escalating is not approving. A run that stays in the workflow after escalation
still needs an explicit decision before any protected effect.

## Implementation approaches (illustrative, not requirements)

| Runtime | Construct | Notes |
| --- | --- | --- |
| BPMN 2.0 | Escalation event | The only native equivalent we found |
| n8n | No direct equivalent | Built from a checkpoint and an error output |
| AWS Step Functions | No direct equivalent | Built from `Catch` and a human-task integration |
| Temporal | No direct equivalent | Built from a signal and retry exhaustion |
| LangGraph | No direct equivalent | Built from `interrupt()` on error |

## Relationship to other primitives

- [P5 HumanCheckpoint](p05-human-checkpoint.md): can raise an escalation, and
  with a new assignee is also where one can land.
- [P6 TimerDeadline](p06-timer-deadline.md): the most common cause.
- [P3 AgentTask](p03-agent-task.md): escalation is one of its declared
  termination conditions.
- [P11 OutcomeContract](p11-outcome-contract.md): escalated and expired are
  separate outcomes.
- [P12 AuditRecord](p12-audit-record.md): records each hop of the escalation.
