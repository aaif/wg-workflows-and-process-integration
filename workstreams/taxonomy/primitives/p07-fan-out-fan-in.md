# P7 FanOut/FanIn

**Obligation:** SHOULD

## Definition

Parallel execution of independent branches, followed by a deterministic join.

## Why it exists

Without a declared join, "how many of `n` branches must return, and what happens to the rest" is undecided by default. That is the concurrent fan-out topology's characteristic failure mode: a single slow or failed branch either blocks the whole workflow or is silently dropped, and neither behaviour was actually decided by anyone.

`P7` is a SHOULD, not a MUST, because most single-`AgentStep` workflows need no concurrency at all. But whenever concurrency exists, the `k`-of-`n` rule has to be a declared decision (proceed once a quorum returns, wait for all `n`, or fail if fewer than `k` return) rather than an accident of whichever branch happens to return first.

## Prior art

| System | Nearest equivalent |
| --- | --- |
| BPMN 2.0 | Parallel gateway / multi-instance activity |
| n8n | No dedicated node, composed from batching + merge |
| AWS Step Functions | Parallel and Map states |
| Temporal | Composed from child workflows / futures |
| LangGraph | `Send` API |

Nearest equivalent is editorial judgment, not a conformance claim.

## Relationship to other primitives

- [P13 Budget](p13-budget.md): bounds the maximum concurrent count.
- [P18 ArbitrationPolicy](p18-arbitration-policy.md): required when the fanned-out branches' outputs can conflict.
- [P14 OutcomeContract](p14-outcome-contract.md): the join must be deterministic even though the fanned-out branches are not.
