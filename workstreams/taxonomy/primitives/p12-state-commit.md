# P12 StateCommit

**Obligation:** MUST

## Definition

A durable checkpoint from which execution can resume.

## Why it exists

Without a durable checkpoint, a crash mid-`AgentStep` loses not just progress but the ability to prove what happened before the crash. Resumability and auditability both depend on the same commit point.

`P12` is the mechanism that makes long-running, stateful agent execution possible at all. Every system surveyed already has some version of it, which is why this RA treats it as a MUST rather than a novel ask: the enforcement burden here is naming the checkpoint as a distinct primitive with a workflow-level contract, not inventing the mechanism.

## Prior art

| System | Nearest equivalent |
| --- | --- |
| BPMN 2.0 | Engine-persisted process instance state (implementation-specific) |
| n8n | Execution data |
| AWS Step Functions | Execution history |
| Temporal | Event history |
| LangGraph | Checkpointer + thread |

Nearest equivalent is editorial judgment, not a conformance claim.

## Relationship to other primitives

- [P1 Trigger](p01-trigger.md): the point a workflow instance's durable state is first keyed against.
- [P15 AuditRecord](p15-audit-record.md): shares its underlying persistence mechanism in most systems surveyed, but is a distinct, workflow-level concern.
- [P14 OutcomeContract](p14-outcome-contract.md): the commit that precedes a workflow's terminal classification.
