# External Boundaries

Status: Mature

External boundaries (`XB-##`) are concerns essential to real workflows but **owned by other AAIF working groups**. WERA names the boundary, states what a workflow must hand across it, and stops there — it does not restate or fork the owning group's requirements ([INV-015](../01-foundations/architecture-invariants.md), [CR-017](../02-architecture-model/composition-rules.md)).

This keeps WERA inside its charter scope and avoids conflicting with sibling WGs.

| Code | Concern | Owning WG | What a workflow provides at the boundary | What it does NOT do here |
|---|---|---|---|---|
| XB-01 | Security & privacy | Security & Privacy | Trust-boundary declarations, untrusted-input tagging ([INV-018](../01-foundations/architecture-invariants.md)), least-privilege effect credentials | Define threat models, crypto, or attack-surface analysis |
| XB-02 | Identity & delegation | Identity & Trust | Actor/agent identity references, delegation and authorization context carried in handoffs (`HND`) | Define the identity protocol or token format |
| XB-03 | Observability signals | Observability & Traceability | Emit trace (`TRC`) and cost (`CST`) signals at defined points | Define tracing schemas, dashboards, or telemetry pipelines |
| XB-04 | Governance & risk | Governance, Risk & Regulatory | Policy hooks (`POL`), audit records (`AUD`), readiness/impact classification | Define governance frameworks or regulatory mappings |
| XB-05 | Accuracy & evaluation | Accuracy & Reliability | Evaluation hooks (`MVL`), confidence/abstention (`UNC`), feedback capture (`FDB`) | Define evaluation methodology or reasoning-quality metrics |

## How boundaries appear in a design

A [descriptor](../../descriptor/README.md) lists `external_boundaries: [XB-01, XB-03, ...]` for the boundaries a workflow touches, so reviewers and cross-WG liaisons can see exactly where coordination is needed — without WERA absorbing another group's mandate.

## Distinction worth repeating

`XB-03` (observability signals) is **not** the same as `OV-07` (execution history). Execution history — the workflow's accepted-transition system of record — is WERA-owned (charter Scope B). Traces and metrics for runtime observability belong to the Observability WG. A workflow emits both; only the former is defined here.
