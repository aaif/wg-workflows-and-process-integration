# Overlays and Boundaries

Status: Index

Cross-cutting controls that apply across many patterns. WERA splits them into two kinds, and the split is deliberate ([INV-015](../foundations/architecture-invariants.md)):

- **[Workflow overlays](workflow-overlays.md) (`OV-##`)** — controls this WG **owns** and defines, because they are intrinsic to workflow execution (approval, protected effects, idempotency, durable waits, compensation, budgets, execution history).
- **[External boundaries](external-boundaries.md) (`XB-##`)** — concerns owned by **other AAIF working groups** (security, identity, observability, governance, accuracy). WERA references them at the boundary and does not restate their requirements.

Defining an overlay once and reusing it keeps patterns lean: a pattern says "apply `OV-02`" instead of re-describing effect protection each time.
