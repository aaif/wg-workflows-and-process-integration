# EP7 — Cross-agent / cross-runtime handoff

Status: Proposal

## Intent

The run crosses a boundary into another runtime and continues there. Control-flow authority is handed to an `external_runtime` — a different engine, agent framework, or organisational domain — via a portable envelope that carries goal, state reference, budget, and provenance. The originating run may wait for a result, or may cede the run entirely. This is the profile for federation and interoperability: where no single runtime owns the whole process and continuity depends on what travels across the seam.

## Authority sketch

| Authority | Holder | Distinctive point |
|---|---|---|
| control-flow | `external_runtime` | Authority moves *across a boundary*; the handoff, not a step, is the defining event. |
| decision | `external_runtime` | The receiving runtime decides subsequent steps under the terms it accepted. |
| action-authorisation | negotiated | Effect authority is carried in the envelope and honoured on the far side; unspecified effects must not be assumed. |
| execution | `cross_runtime` | Execution spans two or more runtimes joined only by the envelope. |
| state | `workflow` / shared reference | Authoritative state stays with an owner and is *referenced*, not blindly copied, to preserve INV-002 across the seam. |

The defining move is `HND` (handoff) of a portable envelope realising [WP11 cross-runtime handoff](../03-patterns/README.md), which depends on a shared, versioned descriptor for interoperability. Bounded delegation across the seam is still governed by [INV-008](../01-foundations/architecture-invariants.md).

## Characteristic coordinates

```yaml
control_flow_authority: external_runtime
actor_topology: cross_runtime
nondeterminism: ND2-ND8                  # depends on the receiving profile
flow_shape: FS6-FS9
durability: DUR3-DUR4                     # envelope and state reference must survive the crossing
effect_level: EF1-EF4
assurance: AS3-AS5                        # cross-domain trust often needs strong approval
impact: IM2-IM4
```

## Relationship to other profiles

- Against every other profile: EP1–EP6 all assume a single owning runtime; EP7 is the profile that exists *because* authority leaves it. On the far side of the seam the receiving runtime runs in some profile of its own (it might itself be [EP2](ep2-workflow-directed-model-assisted.md) or [EP4](ep4-agent-directed.md)).
- Against [EP3](ep3-bounded-agentic-region.md): EP3 delegates a goal to an agentic region *inside* the same runtime and boundary; EP7 delegates across a runtime/trust boundary via a portable envelope rather than an in-process `DLG`.
- Composition: an EP7 handoff can be issued from within any other profile — e.g. an [EP2](ep2-workflow-directed-model-assisted.md) step hands a subtask to a partner runtime and resumes on return. The `EVH` provenance must span both sides.

## Open questions

- What is the minimal portable envelope schema (goal, state reference, budget, effect authority, provenance) required for a receiving runtime to continue safely — and how is it versioned?
- How is authoritative state ownership preserved when two runtimes must both read and update it (INV-002) — shared reference, lease, or one-way transfer?
- How is trust established across the boundary, and how are the effect classes the far side may authorise negotiated and enforced?
- How does `EVH` remain continuous and tamper-evident when execution history is written on both sides of the seam?
- On failure in the far runtime, who is responsible for compensation, and how does control-flow authority return (or not) to the originator?
