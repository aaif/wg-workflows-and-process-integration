# Global invariants

These properties MUST hold no matter which topology a multi-agent workflow uses. They are the load-bearing claims of [`multi-agent.md`](../architectures/multi-agent.md); the [topology catalogue](../topologies/README.md) is one way to satisfy them, not the source of them.

1. **Single global budget ceiling.** A workflow MUST have exactly one [`P13 Budget`](../../taxonomy/primitives/p13-budget.md) ceiling at the top level. Every per-agent or per-handoff budget is a sub-allocation drawn against that ceiling, never an independent grant: see the [handoff contract](../contracts/handoff.md)'s budget-transfer element for why this matters concretely.

2. **Guaranteed termination.** Every topology MUST have a deterministic path to a [`P14 OutcomeContract`](../../taxonomy/primitives/p14-outcome-contract.md) classification that does not depend on any agent choosing to stop. [`P8 TimerDeadline`](../../taxonomy/primitives/p08-timer-deadline.md), `P13 Budget` exhaustion, and deterministic stopping rules ([T6](../topologies/t6-generator-critic.md)) are the mechanisms that make this true; an agent's own judgement that it is "done" is never sufficient on its own.

3. **Monotonic authority.** No [`P16 Handoff`](../../taxonomy/primitives/p16-handoff.md) MAY widen tool scope or delegated authority relative to the transferring step without passing through a deterministic policy gate. Authority MUST be monotonically non-increasing across a chain of handoffs unless a gate explicitly and deliberately re-grants it.

4. **Reconstructable audit.** The full execution graph, including every handoff, MUST be reconstructable from [`P15 AuditRecord`](../../taxonomy/primitives/p15-audit-record.md)s alone. This is workflow-level audit and execution history, which is this WG's scope; it is distinct from runtime tracing and telemetry, which belongs to the **Observability & Traceability WG** (see [Boundaries with other working groups](wg-boundaries.md)).

5. **Deterministic arbitration.** Conflicts between agent outputs MUST be resolved by [`P18 ArbitrationPolicy`](../../taxonomy/primitives/p18-arbitration-policy.md), never by further agent negotiation. If two agents disagree, adding a third agent to mediate does not produce a deterministic resolution. It produces a more complex negotiation with the same unbounded-disagreement problem one level up.

6. **Bounded fan-out.** The maximum number of concurrent `AgentStep`s MUST be statically bounded. Recursive or agent-chosen spawning of further `AgentStep`s MUST have a depth limit enforced outside the spawning agent's own reasoning.

7. **Irreversibility gate.** No `irreversible` tool (per the `AgentStep` [effect classification](../contracts/agent-step-boundary.md): `read_only` / `reversible_write` / `irreversible`) MUST be reachable from any agent without passing through a deterministic gate or a [`P6 HumanCheckpoint`](../../taxonomy/primitives/p06-human-checkpoint.md). **This MUST hold transitively through handoffs**: it is the subtle failure. A handoff chain of three `AgentStep`s in which each individual step's tool scope looks safe can still end in an irreversible action if the chain's authority was allowed to compose without re-checking the gate at each transfer. Invariant 3 (monotonic authority) and invariant 7 (irreversibility gate) are related but not the same claim: monotonicity bounds how far authority can grow across a handoff, while transitivity here requires that the irreversibility check itself be re-applied at every hop, not only at the first one.

## Related

- [Multi-agent checklist](checklist-multi-agent.md): steps 5–7 are how a practitioner names invariants 1, 2, and 5 before implementation.
- [Anti-patterns](anti-patterns.md)
- [Failure modes](failure-modes.md)
- [`../architectures/multi-agent.md`](../architectures/multi-agent.md)
