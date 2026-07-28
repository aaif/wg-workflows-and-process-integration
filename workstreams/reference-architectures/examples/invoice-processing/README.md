# Invoice Processing and Coding

Status: Mature worked example

## Why this example

Invoice processing combines untrusted documents, extraction uncertainty, enterprise reference data, accounting rules, human approval, and an externally visible ERP write. It exercises the minimum architecture needed for a useful model-assisted business workflow **without** requiring autonomous planning — a clean demonstration of [DP-01 least-agentic composition](../../ra/01-foundations/design-principles.md).

## Read it as a few-shot exemplar

```text
use-case.md   →   rationale.md   →   solution.md
  (Input)          (Reasoning)        (Architecture + Result)
```

- **[use-case.md](use-case.md)** — the business problem and requirements (Input).
- **[rationale.md](rationale.md)** — the six-step [Workflow Design Method](../../ra/08-lifecycle/workflow-design-method.md) applied (Reasoning).
- **[solution.md](solution.md)** — the resulting design, linked to the machine-readable [WDS](invoice-processing.wera.yaml) (Architecture + Result).

## Detailed views

- [architecture.md](views/architecture.md) — logical architecture and actor responsibilities.
- [execution.md](views/execution.md) — stage-by-stage execution walkthrough.
- [sequence.md](views/sequence.md) — sequence diagram.
- [contracts-and-state.md](views/contracts-and-state.md) — key contracts and state checkpoints.

## At a glance

| Attribute | Value |
|---|---|
| Profile | `EP2` — workflow-directed + model-assisted |
| Primary pattern | `WP02` — recommend + deterministic adjudication |
| Embedded patterns | `WP00`, `WP01`, `WP07` |
| Lifecycle envelope | `WP08` — durable workflow envelope |
| Overlays | `OV-01`, `OV-02`, `OV-07` |
| Highest effect | `EF2` — reversible write (unposted ERP draft) |
| Readiness / conformance | `RT2` / `CL2` |

Approval in this example authorises a specific unposted AP draft version — **not** payment.
