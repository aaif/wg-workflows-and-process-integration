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

- [Invoice processing and coding](invoice-processing/README.md) — the complete worked example for this snapshot. Profile `EP2`; patterns `WP00`+`WP02`+`WP07` in a `WP08` envelope.

## Choosing future examples

Future examples should be chosen because they **stress architecture areas not yet covered** (fan-out/aggregation, bounded-agentic investigation, cross-runtime handoff), not because they repeat the same control model in a new domain. See the [roadmap](../ROADMAP.md).
