# P10 Budget

**Obligation:** MUST \
**Used in patterns:** [Bounded convergence loop](../patterns/bounded-convergence-loop.md)

## Definition

A hard limit on how much an agent can consume, in four dimensions: iterations,
tool calls, tokens or cost, and wall-clock time.

## Why it exists

You can tell what a deterministic task will cost from its design. You only
find out what an agent task costs by running it, because the number of tool
calls and reasoning turns is decided at run time. So the workflow has to
declare the limit and the orchestrator has to enforce it. A budget written in
the prompt is a suggestion the model can talk itself past. A budget the engine
enforces is a hard stop.

None of the runtimes we reviewed has a native limit on resource consumption.
For most primitives we are just naming a construct that already exists. For
`P10`, we are writing down a requirement that no runtime covers yet.

## How the patterns use it

- **Bounded convergence loop.** Every retry has a declared budget: at least an
  iteration limit plus a time or cost limit. Each attempt (one `P3` run) has
  its own budget, and the loop's budget caps all attempts together. A restart
  must not reset either.

Budgets multiply. The most an agent can spend in one run is its per-attempt
budget times the number of attempts allowed. Setting a sensible per-attempt
budget with no cap on attempts leaves the total unbounded. The same applies to
any loop that sends work back to an agent, such as a reject-with-feedback
cycle.

Waiting on a person isn't part of the budget. `P6 TimerDeadline` limits that.

The right values are a governance call for the Governance, Risk & Regulatory
Alignment WG. This primitive only requires that the limits exist and are
enforced.

## Implementation approaches (illustrative, not requirements)

| Runtime | Construct | Notes |
| --- | --- | --- |
| BPMN 2.0 | No native primitive | `completionCondition` limits instances, not consumption |
| n8n | No native primitive | |
| AWS Step Functions | No native primitive | |
| Temporal | No native primitive | Activity and workflow timeouts cover wall clock only |
| LangGraph | No native primitive | |

The closest built-in guard we found is a configurable limit on model calls in
Camunda's AI Agent connector, which covers one of the four dimensions. In
practice the implementation keeps counters in the agent task and stops when a
limit is hit.

## Relationship to other primitives

- [P3 AgentTask](p03-agent-task.md): the budget is contract element 5.
- [P7 ErrorBoundary](p07-error-boundary.md): retries and re-runs draw from
  these limits.
- [P6 TimerDeadline](p06-timer-deadline.md): limits time spent waiting on a
  person.
- [P11 OutcomeContract](p11-outcome-contract.md): how running out is
  classified.

## Open questions

- How should `P10` be represented in a portable way, given no runtime we
  reviewed has a native equivalent?
