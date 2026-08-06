# EP1 — Workflow-directed

Status: Mature

## Intent

A fully deterministic run: a workflow engine owns every step and there is no model in the loop. Given the same inputs, the run always follows the same path and produces the same effects. This is the baseline against which every more-agentic profile is compared, and the target that [DP-01 (least-agentic)](../01-foundations/design-principles.md) pushes designs back toward whenever nondeterminism is not required.

## Authority allocation

| Authority | Holder | Notes |
|---|---|---|
| control-flow | `workflow` | The engine decides what runs next; no delegation. |
| decision | `workflow` | Branches are deterministic predicates over state. |
| action-authorisation | `workflow` | Effects are gated by static rules, not judgement. |
| execution | `workflow` | Steps are engine-invoked activities/tasks. |
| state | `workflow` | The engine is the single [authoritative state owner](../01-foundations/architecture-invariants.md) (INV-002). |

All five authorities are explicitly allocated to `workflow`, satisfying INV-006.

## Characteristic coordinates

```yaml
control_flow_authority: workflow
actor_topology: none
nondeterminism: ND0
flow_shape: FS1-FS3      # static sequence, branch, loop
durability: DUR2-DUR4    # persisted; often replayable
effect_level: EF0-EF3    # up to reversible/compensable side effects
assurance: AS0-AS2       # static gates, no adjudication needed
impact: IM0-IM3
```

## Typical patterns and primitives

- Patterns: [WP00 deterministic baseline](../03-patterns/wp00-deterministic-baseline.md), often wrapped in [WP08 durable envelope](../03-patterns/README.md).
- Primitives: `EVH` (execution history), `CHK` (checkpoint), `WAI` (wait) for timers and external signals.
- No `DLG`, `PLN`, or `TSL` — there is nothing to delegate and no model to plan or select tools.

## When to use / not use

- Use when the process is well-understood and every branch can be expressed as a rule over known state.
- Use when auditability, repeatability, and exact replay matter more than adaptability.
- Do not use when inputs are unstructured or open-ended enough to require judgement — that is [EP2](ep2-workflow-directed-model-assisted.md) or beyond.
- Do not bolt a model onto an EP1 run informally; crossing into model-assisted territory means explicitly moving to EP2 and re-allocating no authority you did not mean to.

## Failure modes

- Silent scope creep: a "small script" step grows into de-facto decision-making without a profile change.
- Brittleness at the edges: unmodelled input variants fall through deterministic branches and dead-end.
- Over-fitting the happy path: missing durable retries/compensation ([OV-04 durable wait](../06-overlays/workflow-overlays.md)) turns transient faults into stuck runs.

## Example

The [invoice processing example](../../examples/invoice-processing/README.md) becomes an EP1 run if the extraction/recommendation step is removed and every field is taken from a structured feed: receive, validate against rules, post, archive — no model, no adjudication. That stripped-down variant is the deterministic core that [EP2](ep2-workflow-directed-model-assisted.md) wraps a model-assisted step around.
