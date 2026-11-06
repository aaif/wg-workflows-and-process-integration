# P7 ErrorBoundary

**Obligation:** MUST \
**Used in patterns:** [Proposal/execution split](../patterns/proposal-execution-split.md) · [Bounded convergence loop](../patterns/bounded-convergence-loop.md) · [Deterministic acceptance gate](../patterns/deterministic-acceptance-gate.md)

## Definition

A declared place around a task where the workflow catches typed failures and
routes them to a handler.

## Why it exists

If failures aren't typed, the orchestrator sees them all as the same thing,
and retry logic drifts into the agent because the agent was the only one that
noticed. Agent retries aren't idempotent and the orchestrator can't see them.
`P7` makes the workflow responsible for catching a failure, classifying it,
and deciding what happens next.

## How the patterns use it

- **Proposal/execution split.** Execution retries reuse the same idempotency
  key so the effect isn't repeated. When the outcome is unknown (a timeout or a
  lost response), the boundary retries idempotently or reconciles against the
  target before deciding whether the effect happened.
- **Bounded convergence loop.** A failed attempt can only lead to a bounded
  retry, escalation, abstention, or a recorded failure. The boundary is where
  that choice is made, using the loop's retry criteria.
- **Deterministic acceptance gate.** A gate that fails, times out, or returns
  something ambiguous is a typed failure, and it never counts as acceptance.

Some failures aren't errors. An agent saying it can't produce a result is a
declared outcome, so it isn't retried.

## Implementation approaches (illustrative, not requirements)

| Runtime | Construct | Notes |
| --- | --- | --- |
| BPMN 2.0 | Error boundary event / event sub-process | |
| n8n | Error-output connection on a node | |
| AWS Step Functions | `Catch` / `Retry` | Errors are matched by name |
| Temporal | Activity retry policy | Non-retryable error types can be listed |
| LangGraph | Graph-level exception handling | |

All of these catch and retry. Reconciling an unknown outcome against the
target system is always the implementation's job.

## Relationship to other primitives

- [P2 DeterministicTask](p02-deterministic-task.md): retries and idempotency
  are orchestrator work.
- [P10 Budget](p10-budget.md): caps how many retries and re-runs a boundary
  can spend.
- [P8 Escalation](p08-escalation.md): for failures that need a person rather
  than another retry.
- [P11 OutcomeContract](p11-outcome-contract.md): an unresolved failure ends
  the run as failed, with its class recorded.

## Open questions

- Should the *idempotent executor* be its own pattern entry or part of the
  proposal/execution split? Either way, `P2` and `P7` are what it's built
  from.
