# Multi-agent checklist

A numbered walkthrough for deciding whether, and how, to use [`multi-agent.md`](../architectures/multi-agent.md).

1. Name the specific task or workflow under discussion, in one sentence.
2. Check the four reasons in that RA's Purpose section against it: context isolation, independent parallelism, organisational/trust boundary, heterogeneous capability or authority. If none applies, **stop, return to [`single-agent.md`](../architectures/single-agent.md).** This is the most common correct outcome of this checklist.
3. If at least one reason applies, name which one(s), explicitly, in the workflow's design notes. "Because it felt more natural" is not one of the four and does not count.
4. Choose a topology from `T1`–`T6` using the [selection table](../topologies/README.md#selection-table). Default to `T1` unless a specific characteristic of the work (staged output contracts, genuine independence, a cross-org boundary, a shared artifact, or an iterative quality loop) points to `T2`–`T6`.
5. Before writing any code: name the workflow's [`P18 ArbitrationPolicy`](../../taxonomy/primitives/p18-arbitration-policy.md), the deterministic rule that resolves disagreement, even if disagreement is expected to be rare. If agents in this workflow can disagree and no arbitration policy can be named, the design is not ready.
6. Name the workflow's single global [`P13 Budget`](../../taxonomy/primitives/p13-budget.md) ceiling, and confirm every per-agent or per-handoff budget is a stated sub-allocation against it, not an independent number.
7. Name the workflow's guaranteed termination path: the deterministic condition under which the workflow reaches a [`P14 OutcomeContract`](../../taxonomy/primitives/p14-outcome-contract.md) classification regardless of what any agent decides. If this cannot be named, the design is not ready.
8. Only once 5–7 are answered, proceed to specify each [`P16 Handoff`](../contracts/handoff.md)'s seven elements and each `P17 SharedContext`'s consistency model, as applicable to the chosen topology.

This checklist routes the reader back to the single-agent RA at step 2 deliberately, and often. Reaching step 4 or beyond should be the exception, not the default path through this document.

## Related

- [Single-agent checklist](checklist-single-agent.md)
- [Global invariants](global-invariants.md): steps 5–7 are this checklist's way of forcing invariants 1, 2, and 5 to be named before implementation.
- [Anti-patterns](anti-patterns.md)
- [`../architectures/multi-agent.md`](../architectures/multi-agent.md)
