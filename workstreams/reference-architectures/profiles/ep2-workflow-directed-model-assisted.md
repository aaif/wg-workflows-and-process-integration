# EP2 — Workflow-directed + model-assisted

Status: Mature

## Intent

A workflow engine still directs the whole run, but a single model participates as an advisor at one or more bounded steps. The model *proposes* — extracts, recommends, classifies — and the workflow retains authority over control-flow, decisions, and state. This is the most common production-safe way to introduce a model: judgement is added without ceding the run. It is the profile of the [invoice processing example](../examples/invoice-processing/README.md).

## Authority allocation

| Authority | Holder | Notes |
|---|---|---|
| control-flow | `workflow` | The engine still sequences every step; the model never chooses what runs next. |
| decision | `workflow` | The model's output is an input to a deterministic branch, not the branch itself. |
| action-authorisation | `workflow` (+ `human`) | Effects are gated by rules; risky ones escalate to a human via [WP07](../patterns/README.md). |
| execution | `workflow` + `single_agent` | The model runs inside an engine-invoked step ([WP01/WP02](../patterns/README.md)). |
| state | `workflow` | Engine remains the single authoritative state owner (INV-002); model output is recorded, not authoritative until accepted. |

Authority stays with `workflow` except where explicitly and narrowly shared, honouring INV-006 and [DP-04 (explicit authority)](../foundations/design-principles.md).

## Characteristic coordinates

```yaml
control_flow_authority: workflow
actor_topology: single_agent
nondeterminism: ND1-ND3   # bounded model step, model-selected branch
flow_shape: FS2-FS5       # branch/loop with a model-influenced edge
durability: DUR2-DUR4
effect_level: EF1-EF3
assurance: AS1-AS3        # recommend+adjudicate, human approval on risk
impact: IM1-IM3
```

## Typical patterns and primitives

- Patterns: [WP00 deterministic baseline](../patterns/wp00-deterministic-baseline.md) for the spine, [WP02 recommend+adjudicate](../patterns/README.md) at the model step, [WP07 human-supervised action](../patterns/README.md) on risky effects — all wrapped in a [WP08 durable envelope](../patterns/README.md).
- Also common: [WP01 bounded model step](../patterns/README.md), [WP04 generate-validate-repair](../patterns/README.md), [WP06 model-assisted exception](../patterns/README.md).
- Primitives: `EVH`, `CHK`, `WAI`, `APR` (approval). No `DLG` — the model does not receive a goal, only a task.

## When to use / not use

- Use when a step needs judgement over unstructured input (extraction, classification, recommendation) but the overall path must stay engine-governed and auditable.
- Use when you can express the model's contribution as a proposal that a deterministic rule or a human can accept, adjust, or reject.
- Do not use when the model must choose the sequence of steps itself — that is [EP4 (agent-directed)](ep4-agent-directed.md), or a delegated [EP3 region](ep3-bounded-agentic-region.md).
- Do not let a "recommendation" quietly become the decision; if the branch is effectively the model's call, re-classify honestly.

## Failure modes

- Authority leakage: the adjudication gate degrades to auto-accept, silently promoting the model to decision authority.
- Approval drift: an approval captured against one model output is reused after the output changed — mitigate with [INV-013 (approval binds version)](../foundations/architecture-invariants.md) and [OV-01 human approval](../overlays/workflow-overlays.md).
- Unbounded model steps: missing token/time budgets ([OV-06 budget/quota](../overlays/workflow-overlays.md)) let a single step stall the run.
- Missing provenance: model output not written to [execution history](../foundations/core-concepts.md) ([OV-07](../overlays/workflow-overlays.md)) breaks auditability.

## Example

The [invoice processing example](../examples/invoice-processing/README.md) is the canonical EP2 run. A durable workflow ([WP08](../patterns/README.md)) receives an invoice, runs a model step to extract and recommend coding/approval routing ([WP02](../patterns/README.md)), gates high-value or low-confidence invoices to a human approver ([WP07](../patterns/README.md), `APR`), then posts and archives deterministically ([WP00](../patterns/wp00-deterministic-baseline.md)). The engine owns control-flow, decision, and state throughout; the model only ever proposes.
