# Single-Agent Workflow

> The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** in this document are to be interpreted as described in BCP 14 (RFC 2119 / RFC 8174), and only when they appear in this capitalized form.

## Status

[Reference Architecture Proposal](`../../../Workflows-and-Processes-Reference-Architecture-Proposal.md`), established the layered view of deterministic orchestration owning the process and the agent runtime as a bounded, invoked step. This document specifies that boundary at the level of a single agent step.

## Purpose

The single-agent workflow RA answers one question: **what must exist around a non-deterministic agent step so that the workflow as a whole remains reliable, resumable, and auditable?**

The core architectural claim: **the workflow owns the process; the agent is a bounded, contracted step inside it.** This RA specifies the boundary (the contract between the deterministic workflow and the non-deterministic step), not the agent itself.

This RA IS:

- A checklist a practitioner walks a use case through to decide whether an agent step is warranted at all, and if so, how to bound it: see [`guidance/checklist-single-agent.md`](../guidance/checklist-single-agent.md).
- A shared vocabulary (the primitive set `P1`–`P15`) so that "agent step," "tool call," and "human checkpoint" mean the same thing whether the implementation is a BPMN engine, a workflow-as-code platform, or an agent framework.
- A statement of the eight elements every `AgentStep` MUST declare before it is fit to run in production: see [`contracts/agent-step-boundary.md`](../contracts/agent-step-boundary.md).

This RA IS NOT:

- **Not a framework.** It prescribes no engine, language, or runtime.
- **Not an agent design guide.** ReAct, plan-and-execute, reflection, and other internal reasoning loops are equally valid implementation choices *inside* the `AgentStep` boundary. This document is silent on which to use, deliberately, and does not revisit the point again.
- **Not a spec yet.** It is a draft for WG review. Whether it becomes a conformance profile with a test suite is an open question, not a commitment.

## Structure

### Primitives

The primitive set below is normative and shared with [`multi-agent.md`](multi-agent.md); IDs `P1`–`P15` MUST NOT be redefined between the two documents. Full definitions, prior-art mappings, and the relationships between primitives live one per file in [`primitives/`](../../taxonomy/primitives/README.md). This table is an index, not a restatement.

| ID | Primitive | Obligation | Defined in |
|----|-----------|-------------|--------------|
| P1 | Trigger | MUST | [p01-trigger.md](../../taxonomy/primitives/p01-trigger.md) |
| P2 | DeterministicTask | MUST | [p02-deterministic-task.md](../../taxonomy/primitives/p02-deterministic-task.md) |
| P3 | Decision | MUST | [p03-decision.md](../../taxonomy/primitives/p03-decision.md) |
| P4 | AgentStep | MUST | [p04-agent-step.md](../../taxonomy/primitives/p04-agent-step.md) |
| P5 | ToolCall | MUST | [p05-tool-call.md](../../taxonomy/primitives/p05-tool-call.md) |
| P6 | HumanCheckpoint | MUST | [p06-human-checkpoint.md](../../taxonomy/primitives/p06-human-checkpoint.md) |
| P7 | FanOut/FanIn | SHOULD | [p07-fan-out-fan-in.md](../../taxonomy/primitives/p07-fan-out-fan-in.md) |
| P8 | TimerDeadline | MUST | [p08-timer-deadline.md](../../taxonomy/primitives/p08-timer-deadline.md) |
| P9 | ErrorBoundary | MUST | [p09-error-boundary.md](../../taxonomy/primitives/p09-error-boundary.md) |
| P10 | Escalation | MUST | [p10-escalation.md](../../taxonomy/primitives/p10-escalation.md) |
| P11 | Compensation | SHOULD | [p11-compensation.md](../../taxonomy/primitives/p11-compensation.md) |
| P12 | StateCommit | MUST | [p12-state-commit.md](../../taxonomy/primitives/p12-state-commit.md) |
| P13 | Budget | MUST | [p13-budget.md](../../taxonomy/primitives/p13-budget.md) |
| P14 | OutcomeContract | MUST | [p14-outcome-contract.md](../../taxonomy/primitives/p14-outcome-contract.md) |
| P15 | AuditRecord | MUST | [p15-audit-record.md](../../taxonomy/primitives/p15-audit-record.md) |
| P19 | EvaluationGate | MUST when an `AgentStep` iterates against a checkable predicate | [p19-evaluation-gate.md](../../taxonomy/primitives/p19-evaluation-gate.md) |

### The AgentStep boundary contract

`P4 AgentStep` is this RA's central object. The eight elements every `AgentStep` MUST declare before it is fit to run in production (goal specification, input contract, output contract, tool scope, budget, termination conditions, identity and delegated authority, and observability contract) are specified in full in [`contracts/agent-step-boundary.md`](../contracts/agent-step-boundary.md), including the reference structure diagrams showing where the enforcement points sit relative to the agent boundary. The BPMN ad-hoc sub-process precedent for hosting `P4` inside an existing standard, and the argument that four independently-built engines converged on the same shape, are covered in [`primitives/p04-agent-step.md`](../../taxonomy/primitives/p04-agent-step.md), not repeated here.

### Loop tiers

An `AgentStep` that iterates does not run one undifferentiated loop. [`guidance/loop-tiers.md`](../guidance/loop-tiers.md) names four nested cadences (from the model's own reasoning loop up to a product-ownership decision that lives outside any single execution) and states the normative rule that they MUST NOT share a budget or a termination condition. Read it alongside `P13 Budget` and `P19 EvaluationGate` above: the presence of a strong `P19` gate is what makes a large `P13` allocation safe at the innermost tier, and the same logic does not automatically extend to the tiers above it.

### Determinism hints, the checklist, and anti-patterns

Not every problem that looks agentic needs an `AgentStep`. [`guidance/determinism-hints.md`](../guidance/determinism-hints.md) gives a decision table for where to spend the cost of agent reasoning and where a deterministic mechanism is strictly better, and [`guidance/checklist-single-agent.md`](../guidance/checklist-single-agent.md) turns that table into an ordered walkthrough a practitioner can run against one use case. [`guidance/anti-patterns.md`](../guidance/anti-patterns.md) names the failure patterns this boundary contract exists to prevent, so a reviewer has a checklist of its own for spotting a violation.

### Boundaries with other working groups

This RA defines interfaces other AAIF working groups' work plugs into; it does not perform their analysis. [`guidance/wg-boundaries.md`](../guidance/wg-boundaries.md) is the canonical statement of what this RA emits to, and consumes from, the **Security & Privacy WG**, the **Observability & Traceability WG**, the **Governance, Risk & Regulatory Alignment WG**, the **Accuracy & Reliability WG**, and the **Identity & Trust WG**, merged with the equivalent section in [`multi-agent.md`](multi-agent.md) so neither document restates it separately.

## Open questions

- Whether to define a conformance profile and test suite for this RA, or leave it descriptive.
- How to represent `P13 Budget` portably, given no reviewed engine or framework (BPMN, n8n, Step Functions, Temporal, LangGraph) has a native equivalent.
- Whether `P14`'s termination classifications should align to the A2A Protocol's task lifecycle states; cross-referencing the two is WG follow-up work, not resolved here.
- How much of the `AgentStep` boundary contract can be expressed in BPMN `extensionElements` (as Camunda's `zeebe:adHoc` element does for activation configuration) versus requiring a new BPMN element altogether.
- Memory and context assembly: the least standardised layer across every framework surveyed. This RA does not attempt to specify it.
- Whether the Tier 2 steering loop named in [`guidance/loop-tiers.md`](../guidance/loop-tiers.md) needs a budget primitive of its own. Today it has none, and re-running Tier 1 across repeated steering cycles has no declared ceiling at that scope.

## Notes

- Keep the architecture at the component and relationship level.
- Focus on the deterministic boundary around the agent step.
- Leave the agent's internal reasoning loop unspecified.
- Normative language throughout this document is RFC 2119, per BCP 14.
- Primitive IDs `P1`–`P15` are shared with `multi-agent.md`; they MUST NOT be redefined there.
- All cross-mapping tables in this RA set reflect editorial judgment, not a conformance claim.
