# Invoice Processing — Execution

Status: Mature worked example

*This is a **detailed view** of the [solution](../solution.md). It walks the run stage by stage, naming the work performed and the accepted transition plus the authority that permits it.*

## Stage walkthrough

Each stage lists the work and the transition it is allowed to make, together with the authority that owns that transition. Control-flow authority stays with the workflow runtime throughout; models only propose.

| Stage | Work performed | Accepted transition and authority |
|---|---|---|
| 1. Accept submission | `TRG` fires on an accepted submission; `INP` captures the payload and metadata. | Enter the run; workflow runtime opens the lifecycle ([INV-004][architecture-invariants]). |
| 2. Input and attachment controls | Enforce `XB-01` untrusted-input handling: attachment security scan and de-duplication of the submission. | Proceed on clean input, else reject-hold; deterministic controls (`WP00`). |
| 3. Immutable source and provenance | `DFN` fixes the immutable source artefact and provenance so every later value is traceable. | Register provenance; workflow runtime (state authority). |
| 4. Extract fields | `AIN` proposes header and line-item fields from the untrusted document. | Produce a candidate extraction (untrusted); extraction model (proposal only, `WP01`). |
| 5. Schema and arithmetic validation | `SCH` validates types, required fields, totals, and arithmetic of the extraction. | Accept valid extraction, else reject-hold; deterministic validation. |
| 6. Read reference context | `RET` reads vendor, purchase order, receipt, and GL / dimension reference data. | Load context; reference-data adapters (read-only). |
| 7. Deterministic matching and inheritance | `BRL` matches PO, checks vendor/legal-entity equality, applies price/quantity tolerances, matches receipts, inherits PO coding, and runs duplicate detection. | Resolve normal lines; deterministic baseline (`WP00`). |
| 8. Detect residual ambiguity | Determine whether any line remains uncoded after the baseline. | Branch: skip model if none residual, else enter `WP02`; workflow runtime. |
| 9. Recommend residual coding | `REC` proposes a **selection** from a bounded, validated candidate set for each residual line; `UNC` may signal abstention. | Produce a coding proposal (or abstain); recommendation model (proposal only). |
| 10. Adjudicate proposal | `DVL` checks candidate membership, active accounts, dimension rules, policy, and confidence. | Accept adjudicated coding, abstain, or reject; deterministic validation ([INV-008][architecture-invariants]). |
| 11. Determine disposition | `POL` decides the disposition and, when reviewable, authorises creation of an unposted draft. | Route to reject/hold/manual or to draft creation; policy and authorisation. |
| 12. Create unposted ERP draft | Following `OV-02` propose→validate→authorise→execute→confirm→reconcile, the ERP adapter creates an unposted draft as `TRW` at `EF2` with an `IDM` key; ambiguous results trigger `RCP`. | Draft created and its identity/version linked to the run; ERP adapter under authorisation; reconcile not blind-retry ([INV-011][architecture-invariants]). |
| 13. Checkpoint and await review | `CHK` persists durable resumable state and builds the review package; `WAI` holds for the reviewer across restarts (`WP08`). | Suspend durably pending review; workflow runtime (state authority). |
| 14. Approve and finish or revise | `APR` records approve / reject / request-change / timeout on the exact draft version and digest; `EVH` records history and `FSK` closes the run. A material change makes a **new** version and invalidates prior approval. | Finish in a terminal outcome, or revise into a new version; AP reviewer for the decision, workflow runtime for the transition ([INV-013][architecture-invariants], [INV-014][architecture-invariants]). |

The run ends in one of `COMPLETED`, `REJECTED`, `ABSTAINED`, `MANUAL_DISPOSITION`, or `FAILED_TECHNICAL` ([INV-005][architecture-invariants]).

## Least-agentic path

In the common case the deterministic baseline `WP00` resolves the invoice completely and stages 9 and 10 (the recommendation model and its adjudication) are **skipped**. The model is reached only when a residual line survives every rule. The following deterministic controls carry the normal path:

- Attachment security scan and submission de-duplication (`XB-01`).
- Schema and arithmetic validation of the extraction (`SCH`).
- Purchase-order lookup and vendor / legal-entity equality.
- Price and quantity tolerance checks.
- Receipt matching against the PO.
- PO coding inheritance onto matched lines.
- Duplicate-invoice detection.
- Active-account and accounting-dimension rules.

When all lines are resolved deterministically, control passes straight from stage 8 to stage 11, disposition is determined by `POL`, and the run proceeds to draft creation and review without any model proposal. This is the intended default: models close only the residual semantic gap, never the whole task ([DP-01](../../../ra/01-foundations/design-principles.md)).

## Related views

- [architecture.md](architecture.md) — logical architecture and actors.
- [sequence.md](sequence.md) — interaction sequence.
- [contracts-and-state.md](contracts-and-state.md) — contracts and state checkpoints.

<!-- link definitions -->
[architecture-invariants]: ../../../ra/01-foundations/architecture-invariants.md
