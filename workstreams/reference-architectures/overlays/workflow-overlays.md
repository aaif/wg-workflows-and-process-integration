# Workflow Overlays

Status: Mature for OV-01, OV-02, OV-07; Proposal for the rest

Workflow overlays (`OV-##`) are reusable control bundles intrinsic to workflow execution. Each overlay lists its **trigger**, the **primitives it adds**, its **key requirements/invariants**, and the **evidence** it produces.

## OV-01 — Human approval

- **Trigger:** a proposed artifact or action requires an authorised human decision before acceptance or effect.
- **Adds:** `HRV`, `APR`, `WAI` (when asynchronous), `AUD`; an artifact/action digest.
- **Requirements:** approver identity and role verified; approval binds an exact version/digest ([INV-013](../foundations/architecture-invariants.md)); explicit approve/reject/request-change/timeout outcomes ([INV-014](../foundations/architecture-invariants.md)); no self-approval ([INV-007](../foundations/architecture-invariants.md)); recheck immediately before execution.
- **Evidence:** approval record, digest, presented-evidence manifest, approver authority, execution correlation.
- Realised by pattern [WP07](../patterns/wp07-human-supervised-action.md).

## OV-02 — Protected effect

- **Trigger:** an externally visible action (`EF2`+) must be isolated from reasoning.
- **Adds:** `POL`, `DVL`, effect executor invocation (`TRW`/`TXN`/`THI`), `IDM`, `AUD`.
- **Requirements:** proposer holds no unrestricted target credentials ([INV-010](../foundations/architecture-invariants.md)); explicit versioned payload ([INV-012](../foundations/architecture-invariants.md)); proposer ≠ sole authoriser ([INV-007](../foundations/architecture-invariants.md)); maximum effect level declared before execution.
- **Evidence:** effect intent, authorisation record, target-system confirmation linked to the run.
- Six-role separation: **propose → validate → authorise → execute → confirm → reconcile** (roles may be co-located but stay distinct).

## OV-07 — Execution history as system of record

- **Trigger:** any workflow at readiness `RT2`+ (charter Scope B).
- **Adds:** `EVH`, `CHK`, `AUD`.
- **Requirements:** accepted transitions recorded to a single system of record ([INV-002](../foundations/architecture-invariants.md), [CR-014](../model/composition-rules.md)); distinct from observability signals, which are `XB-03`.
- **Evidence:** ordered, queryable record of accepted transitions, decisions, and effects.

## OV-03 — Idempotency and reconciliation

Status: Proposal.

- **Trigger:** effects at `EF2`+ that may be retried or whose result may be ambiguous.
- **Adds:** `IDM`, `RTY` (classified), `RCP`.
- **Open questions:** minimum reconciliation contract; who owns reconciliation when the target is a third-party system.

## OV-04 — Durable wait

Status: Proposal.

- **Trigger:** the run must pause for time, human, or event and may outlive its process (`DUR2`+).
- **Adds:** `WAI`, `CHK`, `TMO`.
- **Open questions:** minimum wait-state contract; correlation and late-event semantics; cancellation/expiry.

## OV-05 — Compensation

Status: Proposal.

- **Trigger:** a partially completed multi-effect sequence must be undone or forward-recovered.
- **Adds:** `CMP`, `RCP`, `AUD`.
- **Open questions:** when compensation is required vs forward recovery; who authorises it; representing irreversible effects.

## OV-06 — Budget and quota

Status: Proposal.

- **Trigger:** a dynamic region (`PLN`/`DLG`/`ABR`/`LOP`) needs bounded cost/time/steps ([DP-09](../foundations/design-principles.md), [CR-018](../model/composition-rules.md)).
- **Adds:** `CST`, `TMO`, `CAN`.
- **Open questions:** portable budget units across runtimes; behaviour on budget exhaustion (abstain vs escalate).
