# P9 StateCommit

**Obligation:** MUST \
**Used in patterns:** [Durable wait](../patterns/durable-wait.md) · [Human approval gate](../patterns/human-approval-gate.md) · [Bounded convergence loop](../patterns/bounded-convergence-loop.md)

## Definition

A durable checkpoint that execution can resume from.

## Why it exists

If a crash happens with no durable checkpoint, you lose the progress and also
any way to prove what happened before the crash. Resuming and auditing both
rely on the same commit points. Every runtime we reviewed already has a
mechanism for this. What the patterns add is where the workflow commits and
what each commit has to contain.

## How the patterns use it

- **Durable wait.** Before parking, the run commits its position, its context,
  and its identity. While parked, the stored record is the run. On resume, the
  record gives back which activity it was on, what the next activity needs,
  and which run the wake-up event belongs to.
- **Human approval gate.** The decision is committed **before** the run
  resumes. Otherwise a crash after resume can lose the evidence while
  execution goes ahead.
- **Bounded convergence loop.** Attempt count, gate results, and budget spent
  are committed after each attempt, so a restart continues the loop instead of
  starting a fresh attempt or resetting the budget.

## Implementation approaches (illustrative, not requirements)

| Runtime | Construct | Notes |
| --- | --- | --- |
| BPMN 2.0 | Engine-persisted process instance state | Implementation-specific |
| n8n | Execution data | |
| AWS Step Functions | Execution history | |
| Temporal | Event history | Commits happen implicitly on every event |
| LangGraph | Checkpointer + thread | Needs a durable checkpointer in production |

Persisting state is only part of a durable wait. A system can save state after
every activity and still lose its pending waits on deploy if the waiting
happens in process memory.

## Relationship to other primitives

- [P1 Trigger](p01-trigger.md): sets the identity the state is keyed on.
- [P5 HumanCheckpoint](p05-human-checkpoint.md): the wait that most needs
  durability.
- [P6 TimerDeadline](p06-timer-deadline.md): pending timers are part of the
  parked record.
- [P12 AuditRecord](p12-audit-record.md): often stored the same way, but it
  serves auditing, while `P9` serves resuming.
