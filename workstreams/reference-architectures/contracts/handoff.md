# Handoff contract

Applies to: [P16 Handoff](../../taxonomy/primitives/p16-handoff.md)

## Purpose

`P16 Handoff` is the technical core of multi-agent coordination in this RA. A `ToolCall` (`P5`) returns control to its caller; a `Handoff` does not: it transfers responsibility for a goal from one `AgentStep` to another, and the transferring step's obligations end at the moment of transfer. This distinction is not cosmetic: a workflow that treats a handoff like a tool call will keep the transferring step "responsible" for an outcome it can no longer act on, which is precisely how diffusion of responsibility (see the Failure modes section of [`multi-agent.md`](../architectures/multi-agent.md)) happens. Nearest equivalents to `P16` in existing standards and frameworks: a BPMN call activity or a message flow between pools (see [OMG BPMN 2.0](https://www.omg.org/spec/BPMN/2.0/)); LangGraph's `Command(goto=...)` (see [LangGraph documentation](https://langchain-ai.github.io/langgraph/)); the OpenAI Agents SDK's handoff construct; and A2A task delegation to a remote agent (see [A2A Protocol specification](https://a2a-protocol.org/latest/)).

Every `P16 Handoff` MUST declare the following seven elements.

## Required elements

### 1. Goal transfer

What the receiving step is now responsible for: a goal specification in the same sense as element one of the `AgentStep` contract, not a restatement of the transferring step's own goal. A handoff that does not re-specify the goal for the receiver is really just forwarding a message, not transferring responsibility.

### 2. Context transfer

What state moves to the receiver, what is deliberately withheld, and why. Handoff is **lossy by default**: unless a workflow author actively decides otherwise, a receiving `AgentStep` does not have the transferring step's full context, and it should not be assumed to. That loss MUST be intentional and declared (the workflow MUST state what context crosses the boundary) rather than incidental, where the receiver simply gets whatever happened to be easy to serialize. An undeclared, incidental loss is how the "context loss across handoff" failure mode actually occurs in practice.

### 3. Authority transfer

The receiving step's tool scope and delegated identity. **The receiving step's authority MUST NOT be broader than the transferring step's, unless a deterministic policy gate explicitly authorises the widening.** This is a normative rule, not a guideline: a handoff is a natural place for privilege to creep upward, because it is easy to grant the receiver "whatever it needs to finish the job" without checking that against what the sender was actually allowed to do. If a workflow needs a receiver with broader authority than the sender, that widening MUST pass through a deterministic gate: never through the sender's own judgement, and never through the receiver simply asking for more.

### 4. Budget transfer

How the parent's `P13 Budget` is partitioned or sub-allocated to the receiver. The workflow MUST hold a single global budget ceiling above any per-agent allocation, because per-agent budgets compose multiplicatively rather than additively: a fan-out that hands each of five agents a "reasonable" budget, each of which may itself hand off to two more agents with their own "reasonable" budgets, does not sum to a reasonable total. It multiplies. Per-agent and per-handoff budgets MUST be modelled as sub-allocations drawn down against one global ceiling, never as independent grants.

### 5. Return contract

Whether control returns to the transferring step, and to whom. Three kinds cover the space:

- `delegate_and_wait`: the transferring step is blocked until the receiver completes or times out (used by T1, T4).
- `delegate_and_continue`: the transferring step proceeds without waiting for the receiver's result (used when the receiver's output is not on the transferring step's critical path).
- `transfer`: no return; the transferring step's obligations end entirely at handoff (used by T2).

### 6. Failure and timeout semantics

What the workflow does if the receiver never completes. A `P8 TimerDeadline` MUST exist on every handoff. There is no exception for "the receiver is trusted" or "the receiver is usually fast." Without a mandatory deadline, a `delegate_and_wait` handoff has no bound on how long the transferring step (and anything waiting on it) can be stuck, which is exactly the "deadlock waiting on a peer" failure mode.

### 7. Audit continuity

The correlation identifier that makes a `P15 AuditRecord` reconstructable across the handoff boundary. A2A defines `contextId` and `taskId` fields for related purposes on its task lifecycle, and aligning the workflow's own correlation identifier with these is WG follow-up work.

## Reference structure

This contract's enforcement points are not diagrammed on their own; they are the points of contact between topologies and the handoff mechanics above. Two diagrams elsewhere in this RA show them concretely:

- [T1 Supervisor](../topologies/t1-supervisor.md): the full supervisor workflow diagram shows the deterministic `PolicyGate` a handoff passes through before delegation, and the global budget governor and audit log that every handoff touches.
- [T4 Peer network](../topologies/t4-peer-network.md): the cross-organisational sequence diagram shows the mandatory `P8 TimerDeadline` and `P10 Escalation` path a handoff MUST carry when the receiver is outside the workflow's own trust boundary.

## Related

- [P16 Handoff](../../taxonomy/primitives/p16-handoff.md)
- [P13 Budget](../../taxonomy/primitives/p13-budget.md)
- [P8 TimerDeadline](../../taxonomy/primitives/p08-timer-deadline.md)
- [P15 AuditRecord](../../taxonomy/primitives/p15-audit-record.md)
- [AgentStep boundary contract](agent-step-boundary.md)
- [`multi-agent.md`](../architectures/multi-agent.md)
- [Topologies](../topologies/README.md)
