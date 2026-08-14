# P14 OutcomeContract

**Obligation:** MUST

## Definition

A typed result plus an explicit termination classification. Every `AgentStep`, and every multi-agent topology as a whole, MUST resolve to one of seven canonical classifications:

- `completed`
- `completed_with_exceptions`
- `escalated`
- `rejected_by_policy`
- `budget_exhausted`
- `failed`
- `cancelled`

**This file is now the single canonical source for that list.** Every other document that references the seven classifications should point back to this file rather than restate the list.

### Classification Meaning

| Classification | Meaning | Correct remediation instinct |
| --- | --- | --- |
| `completed` | The agent reached its goal within budget and policy | None needed |
| `completed_with_exceptions` | The goal was reached, but with deviations worth surfacing | Review the exceptions; do not treat as a clean success |
| `escalated` | Execution was stuck or out-of-policy and was handed to a human or higher authority | Await the escalation decision |
| `rejected_by_policy` | A deterministic gate or human explicitly declined to authorize a proposed action | Never retry automatically without a change in the request or the policy |
| `budget_exhausted` | The agent was making progress but ran out of an externally declared allowance | Very plausibly safe to retry with a larger budget or a narrower goal |
| `failed` | The approach itself broke down: an unrecoverable tool error, a malformed output | Retrying with more budget may just spend more to fail the same way |
| `cancelled` | Execution was terminated deliberately, not by failure or exhaustion | No automated remediation; confirm the cancellation was intended |

## Why it exists

Collapsing distinct failure and non-completion states into a generic `failed` makes automated remediation impossible and the audit trail misleading. 

Two distinctions carry the weight of this argument.

**`budget_exhausted` versus `failed` require opposite remediation instincts.** A `budget_exhausted` outcome means the agent was making progress toward its goal and ran out of an externally declared allowance before it finished. The correct automated response is very plausibly "retry with a larger budget, or retry with a narrower goal," because nothing about the outcome says the approach was wrong, only that it was not resourced to completion. A `failed` outcome (a tool call that errored out with no recovery path, a malformed output that could not be parsed against the schema) means the approach itself broke down, and retrying with more budget is not obviously going to help; it might just spend more to fail the same way again. An automated remediation system that cannot tell these two apart from the classification alone has no principled basis for deciding whether to retry, and a human reviewing the audit trail later has no principled basis for understanding what actually went wrong without re-reading the full execution history to reconstruct which case it was.

**`rejected_by_policy` versus `failed` is an even sharper case.** `rejected_by_policy` means a deterministic gate looked at what the agent wanted to do and refused. The agent worked correctly and proposed a specific action, and a human or a policy explicitly declined to authorize it. The correct remediation instinct here is "never retry this specific request automatically." Retrying a policy rejection without a change in the request or the policy is not transient-failure recovery, it is repeatedly asking the same question that was already answered no. Collapsing this into `failed` alongside a transient tool error makes an automated retry policy dangerous by default (it might retry a `rejected_by_policy` outcome as if it were a flaky network call) and makes the audit trail actively misleading to a compliance reviewer, who needs to be able to distinguish "the system tried and broke" from "the system asked permission and was refused" without inference.

**No system surveyed makes any of these distinctions natively.** Every reviewed system's terminal-state vocabulary (BPMN end events, execution status fields, workflow completion statuses, graph termination states) has no policy or budget classification.

## Prior art

| System | Nearest equivalent |
| --- | --- |
| BPMN 2.0 | Process end events (success/error/terminate), no policy/budget classification |
| n8n | Execution status, no policy/budget classification |
| AWS Step Functions | Execution status, no policy/budget classification |
| Temporal | Workflow completion status, no policy/budget classification |
| LangGraph | Graph termination state, no policy/budget classification |

Nearest equivalent is editorial judgment, not a conformance claim. Every system surveyed has *some* terminal-state vocabulary, but none makes the policy/budget distinctions `P14` requires. The gap is not the absence of a terminal state, it is the absence of the specific classifications this RA argues are operationally necessary.

## Relationship to other primitives

- [P13 Budget](p13-budget.md): `budget_exhausted` is the classification a budget-enforced halt produces.
- [P9 ErrorBoundary](p09-error-boundary.md) / [P10 Escalation](p10-escalation.md): feed `failed` and `escalated` respectively.
- [P16 Handoff](p16-handoff.md): every multi-agent topology MUST have a deterministic path to a `P14` classification that does not depend on any agent choosing to stop.
- [P19 EvaluationGate](p19-evaluation-gate.md): a gate that fails at budget exhaustion produces `budget_exhausted`; one that fails on the predicate itself produces `failed`, a different classification with different remediation.
- [P6 HumanCheckpoint](p06-human-checkpoint.md): a human decision that declines an action produces `rejected_by_policy`.
- [P18 ArbitrationPolicy](p18-arbitration-policy.md): an arbitrated conflict still resolves to one of the seven classifications, not a separate outcome vocabulary of its own.
- [P11 Compensation](p11-compensation.md): a compensated effect needs a terminal classification distinct from an uncompensated `failed`.

## Open questions

- Whether `P14`'s termination classifications should align to the A2A Protocol's task lifecycle states; cross-referencing the two is WG follow-up work, not resolved here.
