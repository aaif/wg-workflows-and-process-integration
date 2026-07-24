# Human Approval Gate

**Solves:** A named human must decide whether an exact proposal may cause a protected effect \
**Used in:** [Single-agent process with human approval](../architectures/single-agent-human-approval.md) \
**Requires capabilities:** Execution engine · human interaction surface · state/context store · audit log \
**Related patterns:** [Proposal/execution split](proposal-execution-split.md) · [durable wait](durable-wait.md)

## Problem

A workflow reaches an action whose risk, audit obligations, or ownership
requires judgment from an accountable person before the action occurs. The
decision must apply to exactly what the person reviewed, and the workflow must
remain safe while waiting for that decision.

## Why this is hard

- Human response time is longer than the lifetime of the process presenting
  the request.
- A generic "approved" flag does not prove who decided, what they saw, or
  whether they were authorized to decide.
- The proposal or its real-world preconditions can change while approval is
  pending.
- Queue pressure encourages default approval, shared accounts, and other
  shortcuts that quietly erase individual accountability.
- Duplicate or late decisions can race with timeout and escalation paths.

## Solution

```text
immutable proposal ──► present to authorized human ──► explicit decision
                              │                           │
                              └── durable wait ─────────┘
                                          │
                          decision record: who · what · when
```

Present an immutable proposal to a uniquely identified, authorized human.
Record an explicit approve or reject decision bound to that proposal version.
Until approval exists, the workflow remains parked and cannot reach the
protected effect. Timeout and escalation are explicit outcomes, never forms
of implicit approval.

## Invariants (must hold in any implementation)

- The approver is a uniquely identified human principal authorized for this
  class of decision; shared approval identities do not qualify.
- The interaction surface shows the exact, immutable proposal version to
  which the decision will bind.
- Approval and rejection are explicit decisions. Silence, timeout, delivery
  failure, and system error never mean approval.
- The decision record captures the proposal version, approver identity,
  decision, and timestamp under the same run identity.
- A changed or superseded proposal requires a new approval decision.
- Pending approval has a deadline and a defined expiry or escalation path.
- Duplicate, late, or conflicting decision events cannot resume or execute the
  run more than once.

## Failure modes when violated

- Shared approver account → the effect cannot be attributed to a person.
- Proposal changes after presentation → the human decides on something other
  than what executes.
- Timeout defaults to approval → lack of attention becomes authorization.
- Decision is recorded after resume → a crash can lose the evidence while
  allowing execution to continue.
- Superseded proposal retains approval → edits bypass human review.
- Duplicate decision resumes twice → the protected effect may execute more
  than once.

## Implementation approaches (illustrative, not requirements)

Implementations vary primarily in **where the human decision is captured**.
The examples below are mechanisms that can participate in the pattern; none
independently supplies identity enforcement, immutable proposal binding,
durability, and audit recording for every use case.

| Decision surface | Documented mechanism | What it provides | What the implementation must add |
|---|---|---|---|
| Workflow-native user task | [Camunda user tasks](https://docs.camunda.io/docs/components/modeler/bpmn/user-tasks/) | Stops the process instance, supports assignees and candidate groups, and captures structured form input | Authorization appropriate to the deployment and Tasklist version; immutable proposal/version display; decision audit fields; timeout and escalation modeling |
| External approval interaction | [Azure Durable Functions human interaction](https://learn.microsoft.com/en-us/azure/durable-task/common/durable-task-human-interaction) | Models the timer-versus-human-event race and keeps status while the orchestration waits | Authentication and authorization of the person sending the event; proposal-version binding; event deduplication; durable audit evidence |
| Target-native review control | [GitHub required pull-request reviews](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches#require-pull-request-reviews-before-merging) | Can require authorized reviewers and dismiss approval when the reviewed revision changes | Rules that prevent bypass; mapping from reviewer identity to the accountable organizational role; audit correlation for effects outside GitHub |

## Known uses outside agents

Pull-request review, production deployment approvals, payment release, and
change-management review all bind a named human decision to a proposed change
before execution. The agent-specific delta is the proposer: because a model
produces the proposal, the separation between proposing and approving must be
structural rather than a convention the proposer can bypass.
