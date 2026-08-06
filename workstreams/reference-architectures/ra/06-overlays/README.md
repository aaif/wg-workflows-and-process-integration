# Overlays and Boundaries

Status: Index

Cross-cutting controls that apply across many patterns. WERA splits them into two kinds, and the split is deliberate ([INV-015](../01-foundations/architecture-invariants.md)):

- **[Workflow overlays](workflow-overlays.md) (`OV-##`)** — controls this WG **owns** and defines, because they are intrinsic to workflow execution (approval, protected effects, idempotency, durable waits, compensation, budgets, execution history).
- **[External boundaries](external-boundaries.md) (`XB-##`)** — concerns owned by **other AAIF working groups** (security, identity, observability, governance, accuracy). WERA references them at the boundary and does not restate their requirements.

Defining an overlay once and reusing it keeps patterns lean: a pattern says "apply `OV-02`" instead of re-describing effect protection each time.

## Code index

Each code carries a stable anchor here (e.g. `#ov-06`, `#xb-03`) so other documents can
facade-link to it through this index rather than deep-linking a heading that might be
reworded.

**Workflow overlays** — defined in [workflow-overlays.md](workflow-overlays.md):

| Code | Overlay |
|---|---|
| <a id="ov-01"></a>`OV-01` | Human approval |
| <a id="ov-02"></a>`OV-02` | Protected effect |
| <a id="ov-03"></a>`OV-03` | Idempotency and reconciliation |
| <a id="ov-04"></a>`OV-04` | Durable wait |
| <a id="ov-05"></a>`OV-05` | Compensation |
| <a id="ov-06"></a>`OV-06` | Budget and quota |
| <a id="ov-07"></a>`OV-07` | Execution history as system of record |

**External boundaries** — defined in [external-boundaries.md](external-boundaries.md):

| Code | Boundary | Owning WG |
|---|---|---|
| <a id="xb-01"></a>`XB-01` | Security & privacy | Security & Privacy |
| <a id="xb-02"></a>`XB-02` | Identity & delegation | Identity & Trust |
| <a id="xb-03"></a>`XB-03` | Observability signals | Observability & Traceability |
| <a id="xb-04"></a>`XB-04` | Governance & risk | Governance, Risk & Regulatory |
| <a id="xb-05"></a>`XB-05` | Accuracy & evaluation | Accuracy & Reliability |
