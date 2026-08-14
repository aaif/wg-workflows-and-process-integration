# P1 Trigger

**Obligation:** MUST

## Definition

The bounded entry point at which a workflow instance begins: an event, a schedule, an API/Tool call, or a human submission.

## Why it exists

Without a declared entry point, there is no bounded unit for a budget, an idempotency key, or an audit record to attach to. "When did this run begin" ends up answered differently by every caller, which breaks retry and dedup logic that assumes a single start.

Every system surveyed already has some construct that plays this role, under a different name. Naming it gives the rest of the primitive set a fixed point to anchor against: a `P13 Budget` ceiling, a `P15 AuditRecord`, and a `P12 StateCommit` all need a single, unambiguous moment at which the clock starts.

## Prior art

| System | Nearest equivalent |
| --- | --- |
| BPMN 2.0 | Start event / message start event |
| n8n | Trigger node |
| AWS Step Functions | Execution start |
| Temporal | Workflow start |
| LangGraph | Graph invoke |

Nearest equivalent is editorial judgment, not a conformance claim.

## Relationship to other primitives

- [P2 DeterministicTask](p02-deterministic-task.md) — typically the first step after a trigger, doing deterministic pre-processing before any routing decision.
- [P12 StateCommit](p12-state-commit.md) — the trigger establishes the point a workflow instance's durable state is keyed against.
- [P15 AuditRecord](p15-audit-record.md) — the audit trail's first entry.
