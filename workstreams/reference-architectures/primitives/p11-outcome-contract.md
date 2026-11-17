# P11 OutcomeContract

**Obligation:** MUST \
**Used in patterns:** [Bounded convergence loop](../patterns/bounded-convergence-loop.md) · [Human approval gate](../patterns/human-approval-gate.md)

## Definition

A typed result plus an explicit termination classification. Every run ends in
exactly one declared classification, and that classification is recorded.

## Why it exists

If every non-success ends up as a generic "failed", automated remediation
can't work and the audit trail is misleading. Two distinctions matter most.

**Rejected vs. failed.** A rejection means someone with authority looked at a
specific proposal and said no. The system did its job, and it should not retry
automatically unless the request changes. A failure means something broke,
and a retry might help. A retry policy that can't tell these apart will keep
asking a question that was already answered.

**Budget exhausted vs. failed.** Running out of budget means the agent hit an
externally set limit, and a bigger budget or a narrower goal might succeed.
A failure means the approach itself broke, and more budget may just cost more.

None of the runtimes we reviewed makes these distinctions. Their terminal
states (end events, execution status, completion status) have nothing for
rejection, policy, or budget.

## How the patterns use it

- **Bounded convergence loop.** The pattern requires a defined non-success
  outcome: escalation, abstention, or recorded failure, along with the reason.
- **Human approval gate.** Timeout and escalation are explicit outcomes, never
  forms of approval, and a rejection is recorded as a rejection.

An architecture declares its full set of exit states and records exactly one
per run. A failed run should also record its failure class, so budget
exhaustion and other failures stay distinguishable.

An earlier draft proposed one shared set of seven values: `completed`,
`completed_with_exceptions`, `escalated`, `rejected_by_policy`,
`budget_exhausted`, `failed`, `cancelled`. Checked against these patterns, it
has gaps. A human approval gate can end as expired, and a bounded convergence
loop can end in abstention; neither has a value in the set.

## Implementation approaches (illustrative, not requirements)

| Runtime | Construct | Notes |
| --- | --- | --- |
| BPMN 2.0 | End events (success / error / terminate) | |
| n8n | Execution status | |
| AWS Step Functions | Execution status | |
| Temporal | Workflow completion status | The workflow's typed return value can carry the classification |
| LangGraph | Graph termination state | |

Every runtime has a terminal status, but the classification itself is
usually a typed value the workflow returns and records.

## Relationship to other primitives

- [P5 HumanCheckpoint](p05-human-checkpoint.md): produces rejections.
- [P6 TimerDeadline](p06-timer-deadline.md) and
  [P8 Escalation](p08-escalation.md): produce expired and escalated outcomes.
- [P7 ErrorBoundary](p07-error-boundary.md) and [P10 Budget](p10-budget.md):
  produce failures, with a failure class.
- [P12 AuditRecord](p12-audit-record.md): where the outcome and its evidence
  are recorded.

## Open questions

- Should the shared set gain `expired` and `abstained`, or should each
  architecture keep its own exit-state set?
- Is `rejected_by_policy` the right name when a person rejects? Human approval
  and policy authorization are treated as separate cases elsewhere.
