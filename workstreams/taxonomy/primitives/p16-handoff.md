# P16 Handoff

**Obligation:** MUST

## Definition

The transfer of responsibility for a goal from one `AgentStep` to another. Unlike a `ToolCall` (`P5`), which always returns control to its caller, a `Handoff` does not. The transferring step's obligations end at the moment of transfer.

The seven elements every `P16 Handoff` MUST declare:
- goal transfer
- context transfer
- authority transfer
- budget transfer
- return contract
- failure and timeout semantics
- audit continuity

This is further explained in [`Contract Handoff`](../../reference-architectures/contracts/handoff.md).

## Why it exists

`P16` is the technical core of the multi-agent RA. Treating a handoff like a tool call leaves the transferring step to be nominally "responsible" for an outcome it can no longer act on. This is "diffusion of responsibility" failure mode, where no component is clearly accountable for the final outcome because every `AgentStep` believed another step, or the receiver of its last handoff, owned it.

### P16 versus P5 ToolCall

The distinction is not cosmetic. Three things differ concretely between a handoff and a tool call:

- **Return semantics.** A tool call always comes back to the caller with a result. A `transfer`-type handoff never does, and even a `delegate_and_wait` handoff blocks on a different party's independent completion rather than a bounded function call returning.
- **Authority transfer.** A tool call executes under the calling agent's existing identity and tool scope. A handoff moves (or, per the monotonic-authority invariant, is explicitly barred from widening) the receiving step's own identity and tool scope, which is a different kind of event than invoking a function.
- **Audit correlation.** A tool call's result attaches naturally to its caller's own execution record. A handoff needs its own correlation identifier precisely because responsibility, not just data, crossed a boundary, and reconstructing "who was accountable for this outcome" requires that correlation to exist independently of either party's own log.

Several frameworks blur this distinction by letting one agent expose another as if it were an ordinary tool the calling agent invokes synchronously, rather than routing the interaction through a distinct handoff construct with its own semantics.

### Convenience with Agent-as-tool pattern

The convenience is real. The "agent as tool" pattern lets a developer add a sub-agent to a calling agent's toolset with almost no new code, since the framework already has a tool-calling loop it can just reuse. But for anything crossing a trust boundary, that convenience is an architectural mistake, because the three properties above don't actually change just because the framework's plumbing makes the call look like an ordinary tool invocation. Authority still moves. Responsibility still transfers. And the audit trail still needs to tell "I asked a tool for a value" apart from "I handed off a goal to a party with its own identity and its own scope." Making a handoff look like a tool call just hides the parts of the event (authority transfer, audit correlation, non-returning obligations) that a workflow crossing an organizational or trust boundary can't afford to leave unexamined. That's exactly why `P16` exists as its own primitive rather than a variant of `P5`.

### The three return contracts

The handoff contract's return-contract element requires every `P16 Handoff` to declare which of three kinds it is. This shapes the argument above about return semantics, so it is worth naming the three directly:

- **`delegate_and_wait`**: the transferring step is blocked until the receiver completes or times out. Used by the supervisor/orchestrator-worker topology and by cross-organisational delegation.
- **`delegate_and_continue`**: the transferring step proceeds without waiting for the receiver's result. Used when the receiver's output is not on the transferring step's critical path.
- **`transfer`**: no return; the transferring step's obligations end entirely at handoff. Used by the sequential pipeline topology.

Only `transfer` genuinely matches "the transferring step's obligations end at the moment of transfer" in the strongest sense; `delegate_and_wait` and `delegate_and_continue` still end the transferring step's *authority* over the goal at handoff, even though the step remains procedurally involved until the receiver responds or the wait is abandoned.

### Global invariants that govern every handoff

Two of the multi-agent RA's global invariants exist specifically to bound what a `P16 Handoff` may do, and they are related but not the same claim:

- **Monotonic authority.** No `P16 Handoff` MAY widen tool scope or delegated authority relative to the transferring step without passing through a deterministic policy gate. Authority MUST be monotonically non-increasing across a chain of handoffs unless a gate explicitly and deliberately re-grants it. This bounds how far authority can grow across a single handoff.
- **Irreversibility gate, transitively.** No `irreversible` tool MUST be reachable from any agent without passing through a deterministic gate or a `P6 HumanCheckpoint`, and this MUST hold transitively through handoffs. A handoff chain of three `AgentStep`s in which each individual step's tool scope looks safe can still end in an irreversible action if the chain's authority was allowed to compose without re-checking the gate at each transfer. Transitivity requires the irreversibility check itself be re-applied at every hop, not only at the first one.

### Failure modes this primitive prevents

| Failure mode | How it manifests | What prevents it |
| --- | --- | --- |
| Context loss across handoff | Receiving `AgentStep` lacks information the sender had, producing an output that looks locally correct but is wrong given the full history | The handoff contract's declared context-transfer element |
| Privilege creep across handoffs | Each handoff in a chain grants the receiver slightly more than the sender had, "to be safe," until the chain's authority exceeds any single step's original grant | Monotonic authority (above) plus the contract's authority-transfer element |
| Deadlock waiting on a peer | A `delegate_and_wait` handoff never returns because the receiver never completes and no deadline was set | The contract's mandatory `P8 TimerDeadline` element |
| Diffusion of responsibility | No component is clearly accountable for the final outcome because every `AgentStep` believed another step, or the receiver of its last handoff, owned it | The contract's sharp goal-transfer semantics: the transferring step's obligations end explicitly at handoff |
| Duplicated side effects on handoff retry | A handoff is retried after an ambiguous failure and the receiver's irreversible action executes twice | Retried handoffs MUST be idempotent or compensated via `P11 Compensation` |
| Audit gaps at organisational boundaries | A cross-org handoff crosses into a system this workflow's audit log cannot see into, breaking reconstructability | The contract's audit-continuity element; WG follow-up on A2A alignment |

## Prior art

| System | Nearest equivalent |
| --- | --- |
| BPMN 2.0 | Call activity / message flow between pools |
| LangGraph | `Command(goto=...)` |
| OpenAI Agents SDK | Native handoff construct: the most direct de facto implementation of `P16` found in the landscape surveyed |
| A2A Protocol | Task delegation to a remote agent |

Nearest equivalent is editorial judgment, not a conformance claim. n8n, AWS Step Functions, and Temporal have no named equivalent for a non-returning goal transfer in the material surveyed for this RA; each would have to compose one from existing constructs (a sub-workflow call, a nested state-machine invocation, or a child workflow, respectively) with nothing in the platform enforcing the authority-transfer and audit-continuity properties above. This document does not assert an equivalent it cannot source.

## Relationship to other primitives

- [P5 ToolCall](p05-tool-call.md): the primitive `P16` is most often mistaken for; see the distinction above.
- [P13 Budget](p13-budget.md): budget transfer is one of the handoff contract's seven elements; sub-allocated, never independently granted.
- [P8 TimerDeadline](p08-timer-deadline.md): a mandatory element of every handoff; there is no exception for a "trusted" receiver.
- [P11 Compensation](p11-compensation.md): retried handoffs MUST be idempotent or compensated, to prevent duplicated side effects.
- [P15 AuditRecord](p15-audit-record.md): the correlation identifier required by the audit-continuity element.
- [P14 OutcomeContract](p14-outcome-contract.md): every handoff chain MUST resolve to a deterministic outcome that does not depend on any agent choosing to stop.

## Open questions

- The exact field semantics of A2A's `contextId` and `taskId`, and how cleanly they map onto this primitive's audit-continuity requirement, were not confirmed against the [A2A Protocol specification](https://a2a-protocol.org/latest/) and need direct verification before this is treated as settled guidance.

- How audit correlation works across an organisational boundary when neither party trusts the other's log: is a shared correlation identifier alone sufficient, or does this require a trust mechanism this WG does not own?
