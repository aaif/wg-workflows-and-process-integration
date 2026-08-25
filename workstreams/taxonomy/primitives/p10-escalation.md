# P10 Escalation

**Obligation:** MUST

## Definition

Hands a stuck or out-of-policy execution to a human or a higher authority.

## Why it exists

Without a distinct "hand this to a human or higher authority because it is stuck or out of policy" primitive, escalation collapses into `P9 ErrorBoundary` or `P6 HumanCheckpoint`, conflating states that need different operational responses. A budget exhaustion, an unresolved typed error, and a routine low-confidence review are not the same event and should not produce the same downstream action by default.

`P10` is the primitive this RA's own survey admits has no native equivalent in four of the five reviewed systems. It is a genuine gap this RA closes rather than merely documents.

## Prior art

| System | Nearest equivalent |
| --- | --- |
| BPMN 2.0 | Escalation event |
| n8n | No direct equivalent, compose `HumanCheckpoint` + `ErrorBoundary` |
| AWS Step Functions | No direct equivalent, compose Catch + human-task integration |
| Temporal | No direct equivalent, compose Signal + retry exhaustion |
| LangGraph | No direct equivalent, compose `interrupt()` on error |

Nearest equivalent is editorial judgment, not a conformance claim. Four of the five systems surveyed have no native equivalent for `P10` at all. It is the clearest gap this table records for any primitive besides `P13 Budget`.

## Relationship to other primitives

- [P9 ErrorBoundary](p09-error-boundary.md): the typical upstream trigger for an escalation.
- [P6 HumanCheckpoint](p06-human-checkpoint.md): escalation's usual destination.
- [P13 Budget](p13-budget.md): budget exhaustion is a common escalation trigger.
- [P14 OutcomeContract](p14-outcome-contract.md): `escalated` is one of the seven canonical classifications.
