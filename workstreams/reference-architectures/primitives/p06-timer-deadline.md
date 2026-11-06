# P6 TimerDeadline

**Obligation:** MUST \
**Used in patterns:** [Human approval gate](../patterns/human-approval-gate.md) · [Durable wait](../patterns/durable-wait.md)

## Definition

A wall-clock limit on a task, a wait, or the whole workflow.

## Why it exists

A wait with no time limit can last forever. The run never fails and never
finishes, and nobody notices until an audit turns it up. Every runtime we
reviewed has native timers (unlike `P10 Budget`), so a missing deadline is a
design mistake rather than a hard problem.

## How the patterns use it

- **Human approval gate.** Every pending approval has a deadline. When it
  fires, the run goes to `P8 Escalation` or ends as expired. It never counts as
  approval.
- **Durable wait.** Every parked run carries a timeout and an escalation or
  expiry path. The timer is stored with the parked record (`P9`), so it
  survives restarts.

If the decision and the deadline arrive together, whichever is recorded first
wins and the other is dropped.

A timer can also limit how long an approval stays valid before execution. That
is one of two ways to deal with stale approvals; the other is having the
executor re-check preconditions (`P2`). A design may use an approval validity
window, executor-side precondition checks, or both. When both apply, both must
pass before execution. Rechecking preconditions or resuming the run does not
extend an expired approval.

## Implementation approaches (illustrative, not requirements)

| Runtime | Construct | Notes |
| --- | --- | --- |
| BPMN 2.0 | Timer boundary event | |
| n8n | Wait node | |
| AWS Step Functions | Wait state / `TimeoutSeconds` | Callback tasks also accept a heartbeat timeout |
| Temporal | Durable timer | Race it against a signal with a selector |
| LangGraph | No first-class primitive | Built around the graph by the application |

## Relationship to other primitives

- [P5 HumanCheckpoint](p05-human-checkpoint.md): needs a deadline so it can't
  stall the run.
- [P8 Escalation](p08-escalation.md): where an expired deadline usually leads.
- [P9 StateCommit](p09-state-commit.md): where pending timers are stored while
  the run is parked.
- [P10 Budget](p10-budget.md): includes the agent's wall-clock limit. Time
  spent waiting on a person is limited here, not there.

## Open questions

- If an approval's validity window lapses before execution, does the run go
  back to pending approval or end?
