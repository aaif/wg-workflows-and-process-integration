# Workflow Primitives

This directory defines the primitive vocabulary shared by both reference architectures in this workstream: [`single-agent.md`](../../reference-architectures/architectures/single-agent.md) and [`multi-agent.md`](../../reference-architectures/architectures/multi-agent.md). A primitive is a named architectural role (a trigger, a bounded agent step, a budget ceiling, a termination classification), not an implementation. Primitive IDs are stable and shared across both RAs: neither document may redefine an ID that already exists here, and every new primitive gets the next unused number rather than reusing or renumbering an existing one. Each primitive's full treatment (its definition, the argument for why it exists, its nearest equivalents across the engines and frameworks this WG has surveyed, and its relationships to the rest of the set) lives in its own file, one per primitive, linked below.

## The primitive set

| ID | Primitive | Obligation | Defined in | Summary |
| --- | --- | --- | --- | --- |
| P1 | Trigger | MUST | [p01-trigger.md](p01-trigger.md) | Bounded entry point: event, schedule, API call, or human submission. |
| P2 | DeterministicTask | MUST | [p02-deterministic-task.md](p02-deterministic-task.md) | Fixed-function step; same input, same path. |
| P3 | Decision | MUST | [p03-decision.md](p03-decision.md) | Branch resolved by an explicit rule. |
| P4 | AgentStep | MUST | [p04-agent-step.md](p04-agent-step.md) | The bounded non-deterministic step; the RA's central object. |
| P5 | ToolCall | MUST | [p05-tool-call.md](p05-tool-call.md) | An agent-initiated effect on an external system. |
| P6 | HumanCheckpoint | MUST | [p06-human-checkpoint.md](p06-human-checkpoint.md) | Workflow pauses for a human decision. |
| P7 | FanOut/FanIn | SHOULD | [p07-fan-out-fan-in.md](p07-fan-out-fan-in.md) | Parallel execution and join. |
| P8 | TimerDeadline | MUST | [p08-timer-deadline.md](p08-timer-deadline.md) | Wall-clock bound on a step or the workflow. |
| P9 | ErrorBoundary | MUST | [p09-error-boundary.md](p09-error-boundary.md) | Typed failure capture and handler routing. |
| P10 | Escalation | MUST | [p10-escalation.md](p10-escalation.md) | Hands a stuck or out-of-policy execution to a human or higher authority. |
| P11 | Compensation | SHOULD | [p11-compensation.md](p11-compensation.md) | Semantic undo of a completed effect. |
| P12 | StateCommit | MUST | [p12-state-commit.md](p12-state-commit.md) | Durable checkpoint from which execution can resume. |
| P13 | Budget | MUST | [p13-budget.md](p13-budget.md) | Enforced ceiling on agent resource consumption: iterations, tool calls, tokens/cost, wall-clock deadline. |
| P14 | OutcomeContract | MUST | [p14-outcome-contract.md](p14-outcome-contract.md) | Typed result plus an explicit termination classification, drawn from a canonical seven-value set. |
| P15 | AuditRecord | MUST | [p15-audit-record.md](p15-audit-record.md) | Workflow-level execution history: step outcomes, decision points, tool invocations, budget consumption, human interventions. |
| P16 | Handoff | MUST | [p16-handoff.md](p16-handoff.md) | Transfers responsibility for a goal from one `AgentStep` to another; does not return control. |
| P17 | SharedContext | SHOULD | [p17-shared-context.md](p17-shared-context.md) | Coordination through a common evolving artifact, governed by a declared consistency model. |
| P18 | ArbitrationPolicy | MUST when agents can disagree | [p18-arbitration-policy.md](p18-arbitration-policy.md) | Deterministic rule that resolves disagreement between agent outputs. |
| P19 | EvaluationGate | MUST when an `AgentStep` iterates against a checkable predicate | [p19-evaluation-gate.md](p19-evaluation-gate.md) | Machine-checkable predicate an `AgentStep` evaluates its own output against to decide whether to iterate or terminate. |

## Cross-mapping: P1–P15 and P19

*Nearest equivalent, editorial judgment, not a conformance claim.* Cells marked "no native primitive" or "no direct equivalent" reflect this RA's argument that `P10`–`P14` (and now `P19`) are largely agentic-era additions rather than gaps in the survey. `P16`–`P18` are not repeated in this table because the source material does not give them a clean five-column mapping across all of BPMN 2.0, n8n, AWS Step Functions, Temporal, and LangGraph; each of those three primitives carries its own, partial prior-art table in its own file, with the absences noted as findings rather than papered over.

| Primitive | BPMN 2.0 | n8n | AWS Step Functions | Temporal | LangGraph |
|-----------|----------|-----|---------------------|----------|-----------|
| P1 Trigger | Start event / message start event | Trigger node | Execution start | Workflow start | Graph invoke |
| P2 DeterministicTask | Service task / script task | Action node | Task state | Activity | Node |
| P3 Decision | Gateway + business rule task (DMN) | IF / Switch node | Choice state | Ordinary code branch | Conditional edge |
| P4 AgentStep | Ad-hoc sub-process, job-worker implementation | AI Agent node | Task invoking an agent runtime | Activity or child workflow | Subgraph / `create_react_agent` |
| P5 ToolCall | Activity inside the ad-hoc sub-process | Sub-node attached to the AI Agent via a typed tool connection | No dedicated state: nested Task invoked by the agent runtime | Activity invoked from within the AgentStep's Activity/child workflow | Tool node |
| P6 HumanCheckpoint | User task + gateway | `sendAndWait` operation | `.waitForTaskToken` | Signal | `interrupt()` |
| P7 FanOut/FanIn | Parallel gateway / multi-instance activity | No dedicated node: composed from batching + merge | Parallel and Map states | Composed from child workflows / futures | `Send` API |
| P8 TimerDeadline | Timer boundary event | Wait node | Wait state / timeouts | Durable timer | No first-class primitive: composed around the graph |
| P9 ErrorBoundary | Error boundary event / event sub-process | Error-output connection on a node | Catch / Retry | Activity retry policy | Composed via graph-level exception handling |
| P10 Escalation | Escalation event | No direct equivalent: compose HumanCheckpoint + ErrorBoundary | No direct equivalent: compose Catch + human-task integration | No direct equivalent: compose Signal + retry exhaustion | No direct equivalent: compose `interrupt()` on error |
| P11 Compensation | Compensation handler | No equivalent: a real gap | No first-class primitive: compose Catch + compensating Task | Saga pattern | No equivalent: a real gap |
| P12 StateCommit | Engine-persisted process instance state (implementation-specific) | Execution data | Execution history | Event history | Checkpointer + thread |
| P13 Budget | No native primitive: `completionCondition` is the closest mechanism | No native primitive | No native primitive | No native primitive | No native primitive |
| P14 OutcomeContract | Process end events (success/error/terminate): no policy/budget classification | Execution status: no policy/budget classification | Execution status: no policy/budget classification | Workflow completion status: no policy/budget classification | Graph termination state: no policy/budget classification |
| P15 AuditRecord | Engine execution log (implementation-specific) | Execution data (same mechanism as P12) | Execution history (same mechanism as P12) | Event history (same mechanism as P12) | Checkpointer history (same mechanism as P12) |
| P19 EvaluationGate | `completionCondition` on an ad-hoc or multi-instance activity is the closest structural equivalent, though BPMN has no notion of the predicate being a test suite | No native equivalent: a workflow author wires validation nodes by hand | A `Choice` state can read a validation `Task`'s output, expressible but not first-class | Expressible as an activity whose result the workflow branches on | A conditional edge reading a validation node's output |

## Notes

- All cross-mapping tables in this directory reflect editorial judgment, not a conformance claim.
- Obligation levels (`MUST` / `SHOULD` / conditional `MUST`) are normative per RFC 2119 / BCP 14 and MUST NOT be changed without WG review. They are recorded once, in this table and in each primitive's own file, and are not repeated with different values anywhere else.
- The eight-element `AgentStep` boundary contract and the seven-element `Handoff` contract are specified in [`../contracts/agent-step-boundary.md`](../../reference-architectures/contracts/agent-step-boundary.md) and [`../contracts/handoff.md`](../../reference-architectures/contracts/handoff.md) respectively, not in this directory.
- Loop-tier budget guidance referenced from `P13 Budget` and `P19 EvaluationGate` lives in [`../guidance/loop-tiers.md`](../../reference-architectures/guidance/loop-tiers.md).
