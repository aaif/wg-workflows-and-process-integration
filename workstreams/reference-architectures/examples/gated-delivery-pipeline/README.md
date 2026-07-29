# Gated Multi-Stage Delivery Pipeline

A worked WERA design for software delivery where agents assist inside fixed stages, but the workflow and named humans retain control.

- [Use case](use-case.md) — business input and constraints
- [Rationale](rationale.md) — six-step design reasoning
- [Solution](solution.md) — architecture and safety properties
- [WDS](gated-delivery-pipeline.wera.yaml) — machine-readable descriptor
- [Architecture](views/architecture.md)
- [Execution](views/execution.md)
- [Sequence](views/sequence.md)
- [Contracts and state](views/contracts-and-state.md)

Profile: `EP2` (workflow-directed + model-assisted). Primary pattern: `WP07` (Human-Supervised Action), wrapped by `WP08` (Durable Workflow Envelope).
