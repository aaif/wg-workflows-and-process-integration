# P12 AuditRecord

**Obligation:** MUST \
**Used in patterns:** [Proposal/execution split](../patterns/proposal-execution-split.md) · [Human approval gate](../patterns/human-approval-gate.md) · [Bounded convergence loop](../patterns/bounded-convergence-loop.md) · [Deterministic acceptance gate](../patterns/deterministic-acceptance-gate.md)

## Definition

Workflow-level execution history: step outcomes, decision points, tool calls,
budget consumption, and human interventions.

## Why it exists

Something has to answer "what did the workflow decide, who authorized it, and
what ran?" Runtime traces don't, and they belong to the Observability &
Traceability WG anyway. `P12` is the system of record, kept separate from
traces and metrics.

## How the patterns use it

| Pattern | What it records |
| --- | --- |
| Proposal/execution split | The proposal, the authorization evidence (who or which policy version), and the effect, all under one run identity |
| Human approval gate | Approver identity, decision, proposal version, and time |
| Bounded convergence loop | Attempt number, gate result, and the reason for each retry or terminal outcome |
| Deterministic acceptance gate | Check inputs, outcome, and the candidate version or digest they apply to |

For these records to be useful:

- **Every event carries the same run identity.** If the records can't be
  joined afterward, the gate proves nothing.
- **Proposer, approver, and executor have different identities.** Otherwise
  the trail can't show separation of duties.
- **Appends are idempotent per run and activity**, so a retried write doesn't
  duplicate history.

## Implementation approaches (illustrative, not requirements)

| Runtime | Construct | Notes |
| --- | --- | --- |
| BPMN 2.0 | Engine execution log | Implementation-specific |
| n8n | Execution data | Same store as `P9` |
| AWS Step Functions | Execution history | Same store as `P9` |
| Temporal | Event history | Same store as `P9` |
| LangGraph | Checkpointer history | Same store as `P9` |

Every runtime we looked at stores `P12` and `P9` in the same place. They are
still separate primitives because one exists for auditing and the other for
resuming. Runtime history is also rarely enough as a business system of
record, so most implementations write domain events to their own store.

## Relationship to other primitives

- [P9 StateCommit](p09-state-commit.md): usually the same storage, used for a
  different purpose.
- [P1 Trigger](p01-trigger.md): sets the run identity every event carries.
- [P11 OutcomeContract](p11-outcome-contract.md): the last event.
- Observability & Traceability WG: this primitive marks where traces can hook
  in (task entry and exit, each tool call). It doesn't produce telemetry.

## Open questions

- Does everyone read the boundary between the audit log and the Observability
  WG's work the same way?
