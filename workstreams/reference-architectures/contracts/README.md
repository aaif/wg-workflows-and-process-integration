# Contracts

A contract, in this reference-architecture set, is a declaration that a step or an edge in a workflow MUST carry before it is fit to run in production. It is not documentation of behaviour observed after the fact. It is a required, checkable set of elements the workflow can validate before the step executes or the handoff occurs.

Two contracts are defined in this RA:

- [AgentStep boundary contract](agent-step-boundary.md): the eight elements every [P4 AgentStep](../../taxonomy/primitives/p04-agent-step.md) MUST declare before it is fit to run in production: goal specification, input contract, output contract, tool scope, budget, termination conditions, identity and delegated authority, and observability contract.
- [Handoff contract](handoff.md): the seven elements every [P16 Handoff](../../taxonomy/primitives/p16-handoff.md) MUST declare when responsibility for a goal transfers from one `AgentStep` to another: goal transfer, context transfer, authority transfer, budget transfer, return contract, failure and timeout semantics, and audit continuity.

## Related

- [`single-agent.md`](../architectures/single-agent.md): defines `P4 AgentStep` and the shared primitive set `P1`–`P15`.
- [`multi-agent.md`](../architectures/multi-agent.md): defines `P16 Handoff`, `P17 SharedContext`, and `P18 ArbitrationPolicy`.
- [Topologies](../topologies/README.md): the six multi-agent shapes that compose these contracts.
