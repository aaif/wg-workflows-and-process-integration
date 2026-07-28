# ADR 0005: Split Workflow Overlays from Cross-WG Boundaries

## Status

Proposed

## Date

2026-07-27

## Context

The earlier draft bundled security, identity, observability, governance, and reliability into one "enterprise control overlays" catalogue owned by the RA. The charter explicitly assigns those concerns to **other AAIF working groups** (Security & Privacy, Identity & Trust, Observability & Traceability, Governance/Risk, Accuracy & Reliability). Owning them here would fork sibling WGs' mandates.

## Options considered

- **One overlay catalogue** — simple, but restates and risks conflicting with other WGs' work.
- **Split** — WERA defines only overlays intrinsic to workflow execution; everything owned elsewhere is a referenced boundary.

## Decision

Split cross-cutting controls into two families:

- **Workflow overlays** (`OV-##`) — owned and defined here: approval, protected effect, idempotency/reconciliation, durable wait, compensation, budget, execution history.
- **External boundaries** (`XB-##`) — owned by other WGs: security, identity, observability, governance, accuracy — **referenced, not redefined** ([INV-015](../../01-foundations/architecture-invariants.md)).

## Rationale

Keeps WERA inside its charter scope, avoids conflicting normative text, and gives cross-WG liaisons an explicit list (`XB-##` in each descriptor) of where coordination is needed. It also preserves the charter's careful distinction: workflow **execution history** (`OV-07`) is WERA-owned, while **observability signals** (`XB-03`) are the Observability WG's.

## Consequences

Patterns and descriptors reference `XB-##` rather than embedding another group's requirements. The [external-boundaries](../../06-overlays/external-boundaries.md) document is a boundary map, not a spec.

## Follow-up

Establish liaison touch-points so each `XB-##` points at the owning WG's current guidance.
