# Topologies

Six topologies cover the multi-agent shapes this RA recognises. Each entry gives a diagram, the primitives it uses, when to choose it, its characteristic failure mode, and where the deterministic boundary sits. All six compose `P1`–`P15` from [`single-agent.md`](../architectures/single-agent.md) with `P16`–`P18` defined in [`multi-agent.md`](../architectures/multi-agent.md); none of them requires a fourth new primitive.

## Standing instruction: confirm you need multi-agent at all

Multi-agent is a cost, not a feature. Before choosing a topology below, check the four legitimate reasons for crossing from one `AgentStep` to more than one, in the Purpose section of [`multi-agent.md`](../architectures/multi-agent.md): context isolation, independent parallelism, organisational or trust boundaries, and heterogeneous capability or authority. If none of these applies to the workflow in front of you, stop here and return to [`single-agent.md`](../architectures/single-agent.md). That is the most common correct outcome of reading this document.

## Topologies

- [T1 Supervisor / orchestrator-worker](t1-supervisor.md)
- [T2 Sequential pipeline with handoff](t2-sequential-pipeline.md)
- [T3 Concurrent fan-out with deterministic join](t3-concurrent-fan-out.md)
- [T4 Peer network / cross-organisational delegation](t4-peer-network.md)
- [T5 Shared-context / blackboard](t5-shared-context.md)
- [T6 Generator-critic / evaluator-optimizer](t6-generator-critic.md)

## Selection table

| Topology | Choose when | Avoid when | Required extra primitives |
|---|---|---|---|
| [T1 Supervisor / orchestrator-worker](t1-supervisor.md) | Sub-goals are known or discoverable by one coordinator; a single locus of control is acceptable | Subtasks belong to a different trust domain, or the decomposition changes the coordinator itself into an unbounded agent | `P16 Handoff` (down and back), `P7` if workers run concurrently, `P18` if workers can conflict |
| [T2 Sequential pipeline with handoff](t2-sequential-pipeline.md) | Stages are strictly ordered and each stage fully consumes the prior output | Stages need to run concurrently, or a later stage needs context from more than one stage back | `P16 Handoff` (`transfer`) per stage, `P8` per handoff |
| [T3 Concurrent fan-out with deterministic join](t3-concurrent-fan-out.md) | Subtasks are independent and latency to a combined result matters | Subtasks share mutable state, or one subtask's output should change what another does | `P7 FanOut/FanIn`, deterministic join with a declared `k`-of-`n` rule |
| [T4 Peer network / cross-organisational delegation](t4-peer-network.md) | The counterpart is owned or authorised by a different organisation; no shared orchestrator is possible | A shared orchestrator could exist: prefer T1 inside one trust boundary | `P16 Handoff` over A2A, mandatory `P8`, `P10 Escalation` |
| [T5 Shared-context / blackboard](t5-shared-context.md) | Multiple agents need to read/write one evolving artifact and the work is not naturally sequential | No consistency model can be agreed and declared | `P17 SharedContext` with a declared consistency model, `P18` for write conflicts |
| [T6 Generator-critic / evaluator-optimizer](t6-generator-critic.md) | Iterative quality improvement is worth the cost and a stopping rule can be stated up front | No independent arbiter is available, or the iteration count cannot be bounded | `P13 Budget` as a hard cap, `P18` as a deterministic stopping rule |

## Related

- [Contracts](../contracts/README.md)
- [`multi-agent.md`](../architectures/multi-agent.md)
- [`single-agent.md`](../architectures/single-agent.md)
