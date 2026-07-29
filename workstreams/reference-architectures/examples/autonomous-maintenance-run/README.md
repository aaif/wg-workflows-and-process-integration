# Autonomous Maintenance Run (“night shift”)

Status: Design example

This example applies the reference architecture to one small, unattended maintenance task: dependency updates, lint/type repairs, or specification/documentation drift. The workflow gives an agent a fenced repair task in a fresh sandbox, requires a deterministic gate to turn green, and then opens a pull request for the exact validated change. It never merges or deploys.

```text
use-case.md → rationale.md → solution.md → autonomous-maintenance-run.wera.yaml
    input        method          design             machine-readable WDS
```

- [use-case.md](use-case.md) — business problem and safety requirements.
- [rationale.md](rationale.md) — the six design-method steps.
- [solution.md](solution.md) — the resulting design and conformance position.
- [autonomous-maintenance-run.wera.yaml](autonomous-maintenance-run.wera.yaml) — the Workflow Design Specification (WDS).

## Detailed views

- [Architecture](views/architecture.md)
- [Execution](views/execution.md)
- [Sequence](views/sequence.md)
- [Contracts and state](views/contracts-and-state.md)

## At a glance

| Attribute | Value |
|---|---|
| Profile | `EP3` — workflow with a bounded agentic region |
| Primary pattern | `WP09` — bounded agentic region |
| Embedded patterns | `WP00`, `WP04` |
| Lifecycle envelope | `WP08` — durable workflow envelope |
| Overlays | `OV-02`, `OV-03`, `OV-04`, `OV-06`, `OV-07` |
| Highest effect | `EF2` — reversible sandbox edit / pull-request creation |
| Readiness / conformance target | `RT2` / `CL2` |

The agent chooses repair steps only inside a bounded sandbox. Deterministic policy chooses task admission, gate success, PR admission, and every terminal outcome.
