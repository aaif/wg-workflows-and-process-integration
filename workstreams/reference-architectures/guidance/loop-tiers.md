# Loop tiers

The RA as drafted models human involvement only as [`P6 HumanCheckpoint`](../../taxonomy/primitives/p06-human-checkpoint.md): a blocking pause *inside* one execution. It has no concept of iteration cadence, and no concept of a specification revised *across* executions. This document closes that gap.

Frame it as a tier model: four nested loops, each with its own cadence, its own authority over the continue-or-stop decision, its own budget allocation, and its own termination artifact.

The core normative claim: **these tiers MUST NOT share a budget or a termination condition.** A ceiling that bounds Tier 1 says nothing about how many times Tier 2 will re-run it. Treating "the budget" as one undifferentiated number across all four tiers is how a per-execution allocation that looked reasonable turns into an unreasonable total spend, discovered only after the fact.

## The four tiers

| Tier | Cadence | Who decides continue or stop | Budget | Termination artifact | RA coverage |
|---|---|---|---|---|---|
| 0: Reasoning loop | Seconds, inside a single `AgentStep` | The model | Covered only in aggregate, by the step's [`P13 Budget`](../../taxonomy/primitives/p13-budget.md) | None, internal to the step | Deliberately out of scope |
| 1: Verification loop | Seconds to minutes | The orchestrator | `P13 Budget` | [`P14 OutcomeContract`](../../taxonomy/primitives/p14-outcome-contract.md) | Fully in scope |
| 2: Steering loop | Tens of minutes to hours | The human | No budget primitive today, a gap | A new version of the goal specification | Partially in scope |
| 3: Outcome loop | Days to weeks | Whoever owns the product decision | Out of scope | Out of scope | Named for completeness, not specified |

### Tier 0: Reasoning loop

Inside a single `AgentStep`, on the order of seconds: the model decides whether to take another reasoning step.

- This RA is deliberately silent on Tier 0's internals: per the [workstream README](../README.md)'s "How to read the architectures" guidance, ReAct, plan-and-execute, and reflection are equal implementation choices inside the `AgentStep` boundary. Say so, and move on; this document does not revisit the point.
- `P13 Budget` bounds Tier 0 only in aggregate, as part of the step's overall iteration and tool-call ceiling. It does not, and is not meant to, distinguish a Tier 0 reasoning step from a Tier 1 verification pass: that distinction lives in this document, not in the primitive.

### Tier 1: Verification loop

The agent produces, tests its output against a [`P19 EvaluationGate`](../../taxonomy/primitives/p19-evaluation-gate.md), and iterates. Seconds to minutes.

- **The orchestrator decides**, because it is the orchestrator that evaluates the gate, not the agent. A gate the agent evaluates against itself is just the model self-reporting completion under a different name.
- Bounded by `P13 Budget`, and exits via `P14 OutcomeContract`.
- This tier is fully in scope and fully covered by the contract in [`../contracts/agent-step-boundary.md`](../contracts/agent-step-boundary.md).

### Tier 2: Steering loop

A human reviews the output and revises the goal specification, then re-runs. Tens of minutes to hours.

- The human decides.
- **This crosses execution boundaries, which is why it is not a `P6 HumanCheckpoint`**: the sharpest distinction this document has to offer, so state it plainly: `P6` blocks one execution mid-flight, waiting on a decision needed to let that same execution continue. Tier 2 happens *between* executions, after one has already finished.
- Tier 2 needs the goal specification to be a versioned, addressable artifact (see element 1 of [`../contracts/agent-step-boundary.md`](../contracts/agent-step-boundary.md)) rather than an inline prompt string. Without that, there is nothing to diff between one steering cycle and the next, and no way to attribute a change in outcome to a change in the spec.
- The RA has no budget primitive for this tier today. That is a gap, flagged here and in [`single-agent.md`](../architectures/single-agent.md)'s open questions, not resolved.

### Tier 3: Outcome loop

Real-world results change what should be built at all. Days to weeks. Whoever owns the product decision decides.

This tier is largely outside this RA's scope. It is named only so the tier model is complete, and so Tier 2 is not mistaken for the outermost loop it is not.

## Gate strength governs safe budget

The stronger the Tier 1 `P19` gate, the larger the budget that step can safely be given, because it will exit on success rather than on exhaustion. A step with no gate must be given a small budget, since exhaustion is its only exit.

This is the practical engineering rule the tier model yields: budget and gate strength are not independent dials. A large budget is only safe once there is a gate strong enough to make exhaustion the rare case rather than the normal one. See [`P13 Budget`](../../taxonomy/primitives/p13-budget.md) for the full argument.

## Cost compounds across tiers, multiplicatively

One Tier 2 revision re-runs the entire Tier 1 loop underneath it. A per-execution budget that looks reasonable in isolation is not a reasonable *total* once Tier 2 cycles are counted.

Five steering revisions do not cost one execution's budget five times over by coincidence; they cost it five times over by construction, because each revision restarts a fresh Tier 1 loop from the top. See [`P13 Budget`](../../taxonomy/primitives/p13-budget.md).

## Tiers are not topologies

[`T6` generator-critic](../topologies/t6-generator-critic.md) is a Tier 1 loop implemented with two agents, not a fourth tier. The generator-critic pattern changes *how many agents* participate in the verification loop; it does not change *which* loop it is or introduce a new cadence.

Confusing a topology with a tier conflates "how many agents are involved" with "how often does the continue-or-stop decision get made." These are orthogonal questions, and the tier model answers only the second one.

## Where each tier's audit lands

All four tiers' continue-or-stop decisions belong in [`P15 AuditRecord`](../../taxonomy/primitives/p15-audit-record.md): Tier 0's iteration count as part of the step's aggregate consumption, Tier 1's gate evaluations and their outcomes, Tier 2's spec revisions, and, where the RA's scope reaches that far, Tier 3's product decisions.

Tier 2's spec revisions are the ones most often lost in practice, because they happen outside any execution. There is no `AgentStep` running while a human edits the goal specification, so nothing in the reference structure diagrams elsewhere in this RA set naturally captures that edit unless the workflow deliberately routes it into the audit trail.

## Provenance

The tier model above is this document's own synthesis. Its prompt was the "loop engineering" framing in Andrew Ng's *The Batch* letter on three loops for building 0-to-1 products. That letter describes:

- An **agentic coding loop**: an agent given "a product specification and optionally a set of evals... write code, test its work, and keep iterating until the code is bug-free and meets its specification," operating over seconds to minutes.
- A **developer feedback loop**: a developer examining the product and steering the agent, operating over "tens of minutes and hours."

## Scope note

Ng's framing is drawn from 0-to-1 product building with coding agents. Generalising it to enterprise process orchestration (the subject of this RA set) is this RA's own editorial extension, not a claim in the source.

Where the analogy strains, the extension is doing the work, not the source: a regulated workflow where a Tier 2 revision to the goal specification is itself change-controlled looks very different from a developer freely re-steering a coding agent, and this document does not claim otherwise.

## Related

- [`P13 Budget`](../../taxonomy/primitives/p13-budget.md)
- [`P15 AuditRecord`](../../taxonomy/primitives/p15-audit-record.md)
- [`P19 EvaluationGate`](../../taxonomy/primitives/p19-evaluation-gate.md)
- [`../contracts/agent-step-boundary.md`](../contracts/agent-step-boundary.md)
- [`T6 Generator-critic`](../topologies/t6-generator-critic.md)
- [`../architectures/single-agent.md`](../architectures/single-agent.md)
- [`../architectures/multi-agent.md`](../architectures/multi-agent.md)
