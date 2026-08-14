# P15 AuditRecord

**Obligation:** MUST

## Definition

Workflow-level execution history: step outcomes, decision points, tool invocations, budget consumption, and human interventions.

## Why it exists

Without workflow-level audit distinct from runtime tracing, this WG's own boundary with the Observability & Traceability WG collapses. There is no artifact left answering "what did the workflow decide and why." `P15` is the concrete mechanism for workflow-level audit logs and execution history, and it is explicitly distinct from, and does not substitute for, runtime traces and metrics.

Every `AgentStep` MUST emit what is needed for its `P15 AuditRecord` to be reconstructable: step outcome, decision points crossed, tool invocations with their effect class, budget consumption against the ceiling, and any human intervention. In a multi-agent workflow, the full execution graph (including every handoff) MUST be reconstructable from `AuditRecord`s alone.

## Prior art

| System | Nearest equivalent |
| --- | --- |
| BPMN 2.0 | Engine execution log (implementation-specific) |
| n8n | Execution data (same mechanism as `P12`) |
| AWS Step Functions | Execution history (same mechanism as `P12`) |
| Temporal | Event history (same mechanism as `P12`) |
| LangGraph | Checkpointer history (same mechanism as `P12`) |

Nearest equivalent is editorial judgment, not a conformance claim. In every system surveyed, `P15`'s mechanism is the same underlying construct as `P12 StateCommit`'s. The RA treats them as distinct primitives because they serve distinct contracts (resumability versus auditability), not because any surveyed system implements them separately.

## Relationship to other primitives

- [P12 StateCommit](p12-state-commit.md): same underlying mechanism in most systems, distinct contract.
- [P16 Handoff](p16-handoff.md): the audit-continuity element requires a correlation identifier that survives the handoff boundary.
- Observability & Traceability WG: this RA emits the attachment points (`AgentStep` entry/exit, each `ToolCall`) where traces and metrics instrument; it does not produce or consume runtime tracing itself.
