# Workflow Primitives

> **Status:** Draft for working group review. Nothing here is locked.

A primitive is a named building block that a workflow definition is written
in: a trigger, a deterministic function, an agent function, a human checkpoint,
a timer. It names a role rather than an implementation. Most runtimes already
have a construct for most of these, each under its own name.

## Primitives, patterns, and architectures

| Layer | Answers | Example |
| --- | --- | --- |
| Primitive | What is the workflow built from? | `P5 HumanCheckpoint` |
| [Pattern](../patterns/) | How do a few primitives combine to solve one recurring problem? | [Human approval gate](../patterns/human-approval-gate.md) |
| [Reference architecture](../architectures/) | Which patterns and capabilities serve a practitioner job? | [Single-agent process with human approval](../architectures/single-agent-human-approval.md) |

Primitives map to patterns, in both directions. Each primitive file lists the
patterns that use it and what each pattern needs from it. Each pattern's
header lists the primitives it's built from, and its *Primitive composition*
section shows where each one sits, the same way an architecture's *Pattern
composition* section places its patterns. Architectures don't reference
primitives directly; they reach them through the patterns they compose.
Invariants and failure modes stay in the patterns, so the primitive files link
to them instead of repeating them.

## The primitive set

| ID | Primitive | Obligation | Used in patterns |
| --- | --- | --- | --- |
| P1 | [Trigger](p01-trigger.md) | MUST | Proposal/execution split, Durable wait |
| P2 | [DeterministicFunction](p02-deterministic-function.md) | MUST | Proposal/execution split, Deterministic acceptance gate |
| P3 | [AgentFunction](p03-agent-function.md) | MUST | Proposal/execution split, Bounded convergence loop |
| P4 | [ToolCall](p04-tool-call.md) | MUST | Proposal/execution split, Bounded convergence loop |
| P5 | [HumanCheckpoint](p05-human-checkpoint.md) | MUST | Human approval gate, Proposal/execution split |
| P6 | [TimerDeadline](p06-timer-deadline.md) | MUST | Human approval gate, Durable wait |
| P7 | [ErrorBoundary](p07-error-boundary.md) | MUST | Proposal/execution split, Bounded convergence loop, Deterministic acceptance gate |
| P8 | [Escalation](p08-escalation.md) | MUST | Human approval gate, Bounded convergence loop |
| P9 | [StateCommit](p09-state-commit.md) | MUST | Durable wait, Human approval gate, Bounded convergence loop |
| P10 | [Budget](p10-budget.md) | MUST | Bounded convergence loop |
| P11 | [OutcomeContract](p11-outcome-contract.md) | MUST | Bounded convergence loop, Human approval gate |
| P12 | [AuditRecord](p12-audit-record.md) | MUST | Proposal/execution split, Human approval gate, Bounded convergence loop, Deterministic acceptance gate |

Why each primitive is in the set, what was left out, and how IDs are assigned
are recorded in [decisions/initial-primitive-set.md](decisions/initial-primitive-set.md).

## Adding or changing a primitive

1. Show which pattern needs it and what breaks without it. A primitive that no
   pattern uses doesn't belong here yet.
2. Check that no existing primitive already covers it.
3. Record the decision with [decisions/TEMPLATE.md](decisions/TEMPLATE.md).
4. Write the entry with [TEMPLATE.md](TEMPLATE.md) and give it the next free ID.
5. Add it to the *Built from primitives* line and the *Primitive composition*
   table of each pattern that uses it.

## Implementation approaches across runtimes (illustrative, not requirements)

The nearest construct for each primitive in five widely used runtimes. These
are editorial judgments, not conformance claims. Where a cell says "no native
primitive", the runtime really has none. Each primitive file adds notes on
what you still have to build.

| Primitive | BPMN 2.0 | n8n | AWS Step Functions | Temporal | LangGraph |
| --- | --- | --- | --- | --- | --- |
| P1 Trigger | Start event / message start event | Trigger node | `StartExecution` | Workflow start | Graph invoke |
| P2 DeterministicFunction | Service task / script task | Action node | Task state | Activity | Node |
| P3 AgentFunction | Ad-hoc sub-process, job-worker implementation | AI Agent node | Task invoking an agent runtime | Activity or child workflow | Subgraph / `create_react_agent` |
| P4 ToolCall | Activity inside the ad-hoc sub-process | Tool sub-node attached to the AI Agent | No dedicated state; nested Task invoked by the agent runtime | Activity invoked from the agent's activity or child workflow | Tool node |
| P5 HumanCheckpoint | User task + gateway | `sendAndWait` operation | `.waitForTaskToken` | Signal | `interrupt()` |
| P6 TimerDeadline | Timer boundary event | Wait node | Wait state / timeouts | Durable timer | No first-class primitive |
| P7 ErrorBoundary | Error boundary event / event sub-process | Error-output connection on a node | `Catch` / `Retry` | Activity retry policy | Graph-level exception handling |
| P8 Escalation | Escalation event | No direct equivalent | No direct equivalent | No direct equivalent | No direct equivalent |
| P9 StateCommit | Engine-persisted process instance state | Execution data | Execution history | Event history | Checkpointer + thread |
| P10 Budget | No native primitive | No native primitive | No native primitive | No native primitive | No native primitive |
| P11 OutcomeContract | End events (success / error / terminate) | Execution status | Execution status | Workflow completion status | Graph termination state |
| P12 AuditRecord | Engine execution log | Execution data | Execution history | Event history | Checkpointer history |

## Notes

- Obligation levels use RFC 2119 keywords. They are proposals for WG review.
- The primitives use the [core workflow terms](../../taxonomy/terms.md). A
  *business task* is the request a workflow run handles, and the run handles
  it through *activities*. An activity can contain several primitives. `P2`
  and `P3` are functions, the unit inside an activity that does the work:
  either fixed code or an agent. An agent activity, for example, is a `P3`
  with its `P4` tool calls, `P10` budget, and `P7` error boundary.
- `P1` is narrower than the taxonomy's *Trigger*; see its open question.
