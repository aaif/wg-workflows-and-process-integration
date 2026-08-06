# EP3 — Workflow with bounded agentic region

Status: Proposal

## Intent

A workflow engine directs the run overall, but at one clearly delimited point it *delegates a goal* into a bounded agentic region and waits for a result. Inside the region an agent may plan and choose steps; outside it, the engine still owns the run. The region is a container with hard edges — entry, exit, and budgets — so that agency is scoped rather than pervasive. This is the smallest step beyond [EP2](ep2-workflow-directed-model-assisted.md): the model stops merely proposing and starts *acting toward a goal*, but only within a fence.

## Authority sketch

| Authority | Outside region | Inside region | Distinctive point |
|---|---|---|---|
| control-flow | `workflow` | `agent` (delegated) | Control-flow is *lent*, not transferred; it returns at the region boundary. |
| decision | `workflow` | `agent` | The agent decides local steps; the engine decides what to do with the region's result. |
| action-authorisation | `workflow` | `workflow` (bounded) | Effects inside the region stay gated by engine-imposed rules and budgets. |
| execution | `bounded_agentic_region` | `bounded_agentic_region` | An agent (or small set) executes toward the delegated goal. |
| state | `workflow` | `workflow` | The engine remains authoritative state owner (INV-002); the region reports back. |

The defining moves are `DLG` (delegate goal) at entry and a result/`HND` back at exit, realising [WP09 bounded agentic region](../03-patterns/README.md) under [INV-008 (bounded delegation)](../01-foundations/architecture-invariants.md) and [DP-09 (bound dynamic regions)](../01-foundations/design-principles.md).

## Characteristic coordinates

```yaml
control_flow_authority: workflow        # overall; agent within the region
actor_topology: bounded_agentic_region
nondeterminism: ND4-ND6                 # bounded plan+execute inside the fence
flow_shape: FS5-FS7
durability: DUR2-DUR4
effect_level: EF1-EF3
assurance: AS2-AS4
impact: IM1-IM3
```

## Relationship to other profiles

- Against [EP2](ep2-workflow-directed-model-assisted.md): EP2's model proposes and returns a value; EP3's region receives a *goal* (`DLG`) and may take multiple self-chosen steps before returning.
- Against [EP4](ep4-agent-directed.md): in EP3 the engine still owns the run and the agentic part is a bounded subregion; in EP4 the agent owns control-flow for the run as a whole.
- A single EP2 run commonly *contains* an EP3 region: the engine reaches a step, delegates a bounded goal, and resumes deterministically with the result. Budgets come from [OV-06 (budget/quota)](../06-overlays/workflow-overlays.md); the plan-and-execute inside typically follows [WP05](../03-patterns/README.md).

## Open questions

- What is the minimal, enforceable contract for a region boundary (goal spec, budget, allowed effects, result schema) so that INV-008 is machine-checkable?
- How should partial progress be surfaced if a region exhausts its `OV-06` budget mid-goal — compensate, checkpoint (`CHK`) and resume, or fail closed?
- Who authorises effects the agent proposes inside the region that exceed the pre-negotiated envelope — silent denial, or escalation to a human ([OV-01](../06-overlays/workflow-overlays.md))?
- Can nested regions (an EP3 region that itself delegates) be permitted, and if so how deep before it is really [EP4](ep4-agent-directed.md)?
- How is the region's internal `PLN`/`TSL` activity recorded in [execution history](../01-foundations/core-concepts.md) without leaking non-authoritative scratch state into the authoritative store?
