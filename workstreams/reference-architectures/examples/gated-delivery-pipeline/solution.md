# Gated Multi-Stage Delivery Pipeline — Solution

Status: Designed solution

## Design in one picture

```mermaid
flowchart TD
 A[Delivery request] --> B[Classify short/full track]
 B --> C[Requirements]
 C --> D{Human gate: exact digest}
 D --> E[Design]
 E --> F[Build + review in parallel]
 F --> G[Join + per-language verification]
 G --> H{Human gate: exact candidate}
 H --> I[QA]
 I --> J{Human deploy approval]
 J --> K[Deploy signed digest]
 K --> L{Postcondition}
 L -->|pass| M[Retro + complete]
 L -->|fail| N[Rollback + compensate]
```

Agents produce bounded artifacts; the workflow owns sequencing, fan-out/join, validation, waits, and all transitions. A named human approves the exact digest before every authority boundary, especially deployment.

## Result — the WDS

The complete machine-readable design is [gated-delivery-pipeline.wera.yaml](gated-delivery-pipeline.wera.yaml).

| Field | Value |
|---|---|
| `selected_profile` | `EP2` — workflow-directed + model-assisted |
| `selected_pattern` | `WP07` — Human-Supervised Action |
| `embedded_patterns` | `WP00`, `WP01`, `WP08` |
| `lifecycle_envelope` | `WP08` — Durable Workflow Envelope |
| `overlays` | `OV-01`, `OV-02`, `OV-03`, `OV-04`, `OV-05`, `OV-07` |
| `external_boundaries` | `XB-01`–`XB-05` |
| `readiness_tier` | `RT3` — Business critical |
| `conformance_target` | `CL3` — Readiness conforming |

## Safety properties

- Approval records the exact artifact and digest; any later change invalidates it.
- Agents cannot choose the next stage, approve a gate, merge, or deploy.
- Build and review fan out only inside a fixed stage and must join before its gate.
- Deployment uses constrained credentials, an idempotency key, postcondition verification, and rollback/compensation.
- Checkpoints and execution history make hours-to-days runs replayable.

See the [architecture](views/architecture.md), [execution](views/execution.md), [sequence](views/sequence.md), and [contracts/state](views/contracts-and-state.md) views.
