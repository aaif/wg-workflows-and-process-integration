# Failure modes

The characteristic ways a multi-agent workflow breaks, and the primitive or [global invariant](global-invariants.md) that prevents each one.

| Failure mode | How it manifests | Primitive / invariant that prevents it |
|---|---|---|
| Context loss across handoff | Receiving `AgentStep` lacks information the sender had, producing an output that looks locally correct but is wrong given the full history | [`P16` element 2](../contracts/handoff.md) (declared context transfer) |
| Conflicting concurrent writes to `P17` | Two agents read the same shared state, act independently, and overwrite each other's result without either noticing | `P17`'s declared consistency model; [`P18`](../../taxonomy/primitives/p18-arbitration-policy.md) for the conflict itself |
| Unbounded critique loop | Generator-critic loop ([T6](../topologies/t6-generator-critic.md)) never converges because the critic can always find something more to critique | [`P13 Budget`](../../taxonomy/primitives/p13-budget.md) cap plus a deterministic stopping rule |
| Recursive spawning | An agent spawns sub-agents that spawn further sub-agents with no bound, exhausting budget and compute | [Global invariant 6](global-invariants.md) (bounded fan-out, static depth limit) |
| Duplicated side effects on handoff retry | A handoff is retried after an ambiguous failure and the receiver's irreversible action executes twice | Retried handoffs MUST be idempotent or compensated via [`P11 Compensation`](../../taxonomy/primitives/p11-compensation.md) |
| Privilege creep across handoffs | Each handoff in a chain grants the receiver slightly more than the sender had, "to be safe," until the chain's authority exceeds any single step's original grant | [Global invariant 3](global-invariants.md) (monotonic authority) and [`P16` element 3](../contracts/handoff.md) |
| Deadlock waiting on a peer | A `delegate_and_wait` handoff (T1, T4) never returns because the receiver never completes and no deadline was set | [`P16` element 6](../contracts/handoff.md) (mandatory `P8 TimerDeadline` on every handoff) |
| Diffusion of responsibility | No component is clearly accountable for the final outcome because every `AgentStep` believed another step, or the receiver of its last handoff, owned it | [`P16`](../contracts/handoff.md)'s sharp goal-transfer semantics: the transferring step's obligations end explicitly at handoff, so accountability is always assignable |
| Disagreement with no arbiter | Two agents produce conflicting outputs and the workflow has no rule to resolve the conflict, so it stalls or picks arbitrarily | [`P18 ArbitrationPolicy`](../../taxonomy/primitives/p18-arbitration-policy.md), deterministic and mandatory when agents can disagree |
| Audit gaps at organisational boundaries | A cross-org handoff (T4) crosses into a system this workflow's audit log cannot see into, breaking reconstructability | [`P16` element 7](../contracts/handoff.md) (audit continuity / correlation identifier); WG follow-up on A2A alignment |

## On the empirical case for and against multi-agent architectures

Published practitioner and research material has begun cataloguing multi-agent failure modes systematically, and there is a live, credible argument in the field on both sides: that multi-agent decomposition improves breadth-first, genuinely parallelisable work, but degrades on tasks that need one coherent shared context held across the whole task. The multi-agent RA's position (multi-agent as a cost with four legitimate justifications) is argued from first principles in its Purpose section rather than from a specific empirical study, and the sources below are named as directions for the WG to check rather than as confirmed citations.

## Related

- [Global invariants](global-invariants.md)
- [Anti-patterns](anti-patterns.md)
- [`P16 Handoff`](../../taxonomy/primitives/p16-handoff.md)
- [`../contracts/handoff.md`](../contracts/handoff.md)
- [`../architectures/multi-agent.md`](../architectures/multi-agent.md)
