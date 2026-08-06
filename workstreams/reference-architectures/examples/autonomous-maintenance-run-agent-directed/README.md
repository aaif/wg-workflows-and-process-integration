# Agent-Directed Autonomous Maintenance Run

Status: Design example — explicit `EP4` variant

This is a deliberately more agent-directed counterpart to [autonomous-maintenance-run](../autonomous-maintenance-run/README.md). The architect requires the agent to own the whole run toward a green deterministic gate. This overrides the usual least-agentic preference (`DP-01`) and therefore requires stricter containment, not fewer controls.

- [Use case and directive](use-case.md)
- [Rationale](rationale.md)
- [Solution](solution.md)
- [Machine-readable WDS](autonomous-maintenance-run-agent-directed.wera.yaml)
- Views: [architecture](views/architecture.md), [execution](views/execution.md), [sequence](views/sequence.md), [contracts and state](views/contracts-and-state.md)

| Attribute | Value |
|---|---|
| Profile | `EP4` — agent-directed under workflow constraints |
| Primary pattern | `WP09` — bounded agentic region / fenced capability model |
| Embedded patterns | `WP00`, `WP04`, `WP07` |
| Envelope | `WP08` — durable workflow envelope |
| Overlays | `OV-01`–`OV-04`, `OV-06`, `OV-07` |
| Highest effect | `EF2` — reversible sandbox edit and PR creation |
| Readiness / conformance target | `RT2` / `CL2` |

The agent may direct the sequence; it cannot authorise its own effects, widen its envelope, merge, deploy, or make its working memory authoritative.
