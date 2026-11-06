# P1 Trigger

**Obligation:** MUST \
**Used in patterns:** [Proposal/execution split](../patterns/proposal-execution-split.md) · [Durable wait](../patterns/durable-wait.md)

## Definition

The entry point where a workflow execution begins: an event, a schedule, an
API or tool call, or a human submission.

## Why it exists

Budgets, idempotency keys, and audit records all need a run to attach to, and
that run needs a single starting point. If every caller decides for itself when
a run began, retry and deduplication logic breaks.

The trigger has two jobs. It starts at most one run per logical request, so a
redelivered event lands on the existing run instead of creating a second one.
It also sets the run identity that every later record carries.

## How the patterns use it

- **Proposal/execution split.** The pattern requires intent, decision, and
  effect to share one run identity. The trigger is where that identity comes
  from.
- **Durable wait.** Resuming a parked run depends on routing the wake-up event
  to the right run. That correlation key is the identity the trigger set.

## Implementation approaches (illustrative, not requirements)

| Runtime | Construct | Notes |
| --- | --- | --- |
| BPMN 2.0 | Start event / message start event | |
| n8n | Trigger node | Deduplication is up to the workflow author |
| AWS Step Functions | `StartExecution` | Execution names are unique per state machine for a retention period, so the request key can go there |
| Temporal | Workflow start | Use the request key as the workflow ID with a conflict policy that attaches to the existing run |
| LangGraph | Graph invoke | Using the request key as the `thread_id` ties redeliveries to one thread; detecting a duplicate start is still up to the app |

In every case, the implementation chooses the request key. The runtime only
enforces uniqueness once it has one.

## Relationship to other primitives

- [P2 DeterministicTask](p02-deterministic-task.md): input validation usually
  runs right after the trigger.
- [P9 StateCommit](p09-state-commit.md): the run's state is keyed on the
  identity the trigger sets.
- [P12 AuditRecord](p12-audit-record.md): the first entry in the audit trail.

## Open questions

- The [core workflow terms](../../taxonomy/terms.md) say a *Trigger* can start
  **or advance** a workflow execution. `P1` only covers starting one. Should
  the term be narrowed, or should `P1` also cover resume events?
