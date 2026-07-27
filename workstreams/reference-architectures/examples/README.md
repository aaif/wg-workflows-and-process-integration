# Worked Examples

Status: Index

Examples serve two purposes at once:

1. they **validate** the architecture by exercising it on a realistic case; and
2. they are **few-shot exemplars** — a human or AI agent can read them as `Input → Reasoning → Architecture → Result` before designing something new.

## Exemplar shape

Every example follows the same triad, so it reads the same way for both audiences:

| File | Role | Corresponds to |
|---|---|---|
| `use-case.md` | Input — the business problem and requirements | what you are given |
| `rationale.md` | Reasoning — applying the six-step method | the [WDM](../playbook/workflow-design-method.md) |
| `solution.md` | Architecture + Result — the design and the WDS | the [descriptor](../descriptor/README.md) |

Detailed views (architecture, execution, sequence, contracts) sit alongside the triad for readers who want depth.

## Examples

- [Invoice processing and coding](invoice-processing/README.md) — the complete worked example for this snapshot, with the full triad and detailed views. Profile `EP2`; patterns `WP00`+`WP02`+`WP07` in a `WP08` envelope.

## Trial exemplars (descriptor-level)

These are schema-valid WDS artifacts produced to test WERA against *new* use cases from the WG use-case landscape. They exercise the **agentic** end of the spectrum that the invoice example deliberately avoids. They are descriptor-only for now (no `use-case`/`rationale`/`solution` triad yet), so they are exemplars rather than full worked examples.

They were chosen as a **deliberate autonomy-spectrum pair** — the same class of work (software delivery by an agent) at opposite human-in-the-loop settings — to check that the coordinate separates them using one vocabulary:

| WDS | Profile · pattern | The distinctive coordinate |
|---|---|---|
| [autonomous-maintenance-run.wera.yaml](../descriptor/examples/autonomous-maintenance-run.wera.yaml) | `EP4` · `WP09` (loop `WP04` in a `WP08` envelope) | `control_flow_authority: agent`, `AS2` deterministic gate, `EF2` PR only |
| [gated-delivery-pipeline.wera.yaml](../descriptor/examples/gated-delivery-pipeline.wera.yaml) | `EP1` · `WP07` | `control_flow_authority: workflow`, `AS5` multi-party sign-off, `EF3` deploy |

Same work; **7 of 8 axes differ**. The autonomy difference lands on *who owns control-flow* and *what carries assurance* — not on a different framework.

## Choosing future examples

Future examples should be chosen because they **stress architecture areas not yet covered**, not because they repeat the same control model in a new domain. With the pair above, the bounded-agentic/agent-directed region is now exercised; still open are **fan-out/aggregation** and **cross-runtime handoff** (`WP11`/`EP7`), and giving the two trial exemplars their full triad. See the [roadmap](../ROADMAP.md).
