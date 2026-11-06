# P3 AgentTask

**Obligation:** MUST \
**Used in patterns:** [Proposal/execution split](../patterns/proposal-execution-split.md) · [Bounded convergence loop](../patterns/bounded-convergence-loop.md)

## Definition

The bounded, non-deterministic task. The workflow owns the process; the
`AgentTask` is a contracted, bounded piece of it.
Its internal reasoning loop is unspecified: deterministic and ReAct-style
internals are equal implementation choices inside the boundary.

## Why it exists

Without a container that has its own contract, one of two things happens.
Either the agent ends up as the top-level orchestrator, and the workflow can
no longer enforce budgets, gates, or audit from outside the model, or agent
behavior spreads across several tasks and there is no one place to enforce
tool scope, budget, or termination.

This is a structural problem, and a better model doesn't fix it. An agent with
open tool scope, no budget, and no termination check outside its own reasoning
will fail in production in predictable ways. A stronger model won't add a
budget nobody declared or stop a loop nobody is watching.

### The contract

Every `AgentTask` declares eight elements before it runs in production:

| # | Element | What it means |
| --- | --- | --- |
| 1 | Goal | What done looks like, in a form the workflow can check rather than the model's claim that it's finished |
| 2 | Input contract | A schema for what the task receives |
| 3 | Output contract | A schema for what it returns. Add a confidence signal only if something downstream routes on it automatically |
| 4 | Tool scope | An allowlist of tools, each with an effect class (see `P4`) |
| 5 | Budget | The `P10` limits, enforced by the engine |
| 6 | Termination conditions | Success, failure, and escalation conditions that the engine evaluates, not the model |
| 7 | Identity and delegated authority | Whose authority the agent acts under. How that is enforced belongs to the Identity & Trust WG |
| 8 | Observability contract | What it must emit as `P12` events |

## How the patterns use it

- **Proposal/execution split.** The agent task is the proposer. Its output is
  a proposal (immutable, versioned data) and never an action. Its tool scope
  excludes the protected-effect capability, and its identity can't obtain the
  executor's credentials. If a reviewer sends the proposal back with feedback,
  the task runs again and produces a new version, and any approval on the old
  version no longer counts.
- **Bounded convergence loop.** Each attempt is one run of the agent task. The
  agent can't declare convergence: its success condition is the gate's result,
  not its own judgment. Its budget covers each attempt, the loop's budget
  covers all of them, and a restart must not reset either.

A re-run after a crash may produce a different output. Both patterns tolerate
that because nothing has executed yet and a gate still stands between the
output and the effect.

### Anti-patterns

- **Agent as the top-level orchestrator.** The workflow can't enforce gates,
  budgets, or audit from outside the model.
- **Agent holds the protected-effect capability.** Approval can be bypassed.
- **Retry logic inside the agent.** The orchestrator can't see these retries
  and they aren't idempotent. Retries belong to `P7`.
- **"The prompt is the guardrail."** The model can ignore a prompt or be
  talked out of it.

## Implementation approaches (illustrative, not requirements)

| Runtime | Construct | Notes |
| --- | --- | --- |
| BPMN 2.0 | Ad-hoc sub-process, job-worker implementation | Camunda 8's [ad-hoc sub-process](https://docs.camunda.io/docs/components/modeler/bpmn/ad-hoc-subprocesses/) backs its AI Agent connector. No budget primitive |
| n8n | AI Agent node | |
| AWS Step Functions | Task invoking an agent runtime | |
| Temporal | Activity or child workflow running the agent loop | A child workflow keeps the agent loop's history apart from the parent's |
| LangGraph | Subgraph / `create_react_agent` | |

Several unrelated runtimes have arrived at the same shape: a bounded container,
attached tools, and a durable pause around the agent's loop. None of them
enforces the full contract above. Budget (element 5) and engine-evaluated
termination (element 6) are always the implementation's job.

## Relationship to other primitives

- [P4 ToolCall](p04-tool-call.md): what the tool-scope allowlist governs.
- [P10 Budget](p10-budget.md): contract element 5.
- [P7 ErrorBoundary](p07-error-boundary.md): typed failure capture around the
  task, outside the model.
- [P8 Escalation](p08-escalation.md): where the escalation condition leads.
- [P12 AuditRecord](p12-audit-record.md): contract element 8.

## Open questions

- How much of this contract fits in BPMN `extensionElements`, the way Camunda
  configures ad-hoc activation, and how much would need a new element?
