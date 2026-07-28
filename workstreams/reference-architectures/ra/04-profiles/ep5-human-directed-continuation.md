# EP5 — Human-directed continuation

Status: Proposal

## Intent

The run advances because *people act*. Control-flow authority rests with humans: each continuation waits for a human decision, approval, or input, and the run may sit idle for hours, days, or weeks between actions. The workflow and any models are in service of the humans — preparing options, holding durable state, and resuming when a person responds. This is the profile for case-management, review chains, and multi-party approvals where the human sequence *is* the process.

## Authority sketch

| Authority | Holder | Distinctive point |
|---|---|---|
| control-flow | `human` | Each next step is unlocked by a human action; the engine waits rather than drives. |
| decision | `human` | Substantive branch choices are human judgements, not rules or model output. |
| action-authorisation | `human` | Humans authorise effects directly, often via multi-party approval (`APR`). |
| execution | `workflow` (+ optional model) | The engine executes the mechanics once a human unlocks the next step. |
| state | `workflow` | A durable store owns authoritative state across long waits (INV-002); it must survive the idle periods. |

The signature is long-lived waiting on humans: `WAI` (wait) and `APR` (approval) over a [WP08 durable envelope](../03-patterns/README.md), governed by [OV-01 (human approval)][workflow-overlays] and [OV-04 (durable wait)][workflow-overlays].

## Characteristic coordinates

```yaml
control_flow_authority: human
actor_topology: any                     # none, single_agent, or multi_agent in support roles
nondeterminism: ND0-ND3                 # low: humans decide, machinery is deterministic/advisory
flow_shape: FS4-FS8                     # long-running, wait-gated, possibly event-nudged
durability: DUR3-DUR4                   # must persist across long idle periods
effect_level: EF1-EF4                   # humans may authorise irreversible effects
assurance: AS3-AS5                      # up to multi-party approval
impact: IM2-IM4
```

## Relationship to other profiles

- Against [EP2](ep2-workflow-directed-model-assisted.md): EP2 uses a human only to adjudicate a model proposal on risky steps; EP5 makes human action the *primary* engine of continuation for the whole run.
- Against [EP6](ep6-event-directed-continuation.md): both are continuation-driven and long-running, but EP5 waits on deliberate human acts while EP6 waits on external events; a human approval is itself a kind of event, so the profiles shade into each other.
- Composition: an EP5 run frequently *contains* other profiles — a human unlocks a step that runs an [EP1](ep1-workflow-directed.md) sub-workflow or an [EP2](ep2-workflow-directed-model-assisted.md) model-assisted step to prepare the next human decision. Approvals must respect [INV-013 (approval binds version)](../01-foundations/architecture-invariants.md).

## Open questions

- How long may a run wait, and what happens at the limit — escalate, expire, or auto-decide by policy (which would move authority away from `human`)?
- When an approval binds a version (INV-013) but the underlying artefact changes during a long wait, how is the human re-consulted without restarting the chain?
- How are delegation and reassignment modelled when the responsible human is unavailable, without silently transferring decision authority?
- What is the authoritative record of *who* acted and on what version, and how does it feed [execution history](../01-foundations/core-concepts.md) ([OV-07][workflow-overlays])?
- Where is the boundary with [EP6](ep6-event-directed-continuation.md) when human actions arrive as system events rather than direct interactions?

<!-- link definitions -->
[workflow-overlays]: ../06-overlays/workflow-overlays.md
