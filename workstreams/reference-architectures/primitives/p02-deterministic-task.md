# P2 DeterministicTask

**Obligation:** MUST \
**Used in patterns:** [Proposal/execution split](../patterns/proposal-execution-split.md) · [Deterministic acceptance gate](../patterns/deterministic-acceptance-gate.md)

## Definition

A fixed-function task. Given the same input, it always takes the same path.

## Why it exists

If plain deterministic work has no name of its own, it tends to get folded into
an agent task because that's convenient. Arithmetic, eligibility checks,
thresholds, entitlements, lookups, transforms, and any validation with a rule
you can write down belong here. So do retries and idempotency, which the
orchestrator owns.

## How the patterns use it

- **Proposal/execution split.** The workflow-controlled executor is a `P2`. It
  holds the capability and credentials the agent doesn't have, performs exactly
  the authorized proposal, and is idempotent so a retry doesn't repeat the
  effect. It can also re-check preconditions before acting, which is one way
  to deal with an approval that has gone stale.
- **Deterministic acceptance gate.** The checks the gate runs (tests, schema
  validation, policy rules) are `P2` tasks. They have to be independent of the
  agent that produced the candidate, and they evaluate the exact candidate
  version they were given.

## Implementation approaches (illustrative, not requirements)

| Runtime | Construct | Notes |
| --- | --- | --- |
| BPMN 2.0 | Service task / script task | |
| n8n | Action node | |
| AWS Step Functions | Task state | Retries are declared on the state |
| Temporal | Activity | Retry policy and timeouts are declared per activity |
| LangGraph | Node | Retry and idempotency are up to the node's code |

Every runtime runs a deterministic task. Idempotency keys for side effects are
always the implementation's job.

## Relationship to other primitives

- [P3 AgentTask](p03-agent-task.md): the non-deterministic counterpart.
- [P4 ToolCall](p04-tool-call.md): agent-initiated, so it can't stand in for
  the executor.
- [P7 ErrorBoundary](p07-error-boundary.md): owns retries and idempotency.
- [P5 HumanCheckpoint](p05-human-checkpoint.md): when a person is the
  authority, the executor runs only after their explicit approval.
