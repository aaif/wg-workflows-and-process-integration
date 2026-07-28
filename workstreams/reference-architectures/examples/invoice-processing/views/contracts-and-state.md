# Invoice Processing — Contracts and State

Status: Mature worked example

*This is a **detailed view** of the [solution](../solution.md). It defines the key contracts exchanged between components and the authoritative state the workflow records.*

## Key contracts

- **Canonical invoice** — the validated, normalised representation of the invoice after extraction and schema/arithmetic checks. Produced from the `AIN` extraction once `SCH` accepts it; every field carries provenance back to the immutable source (`DFN`). This is the trusted internal form; the raw document remains untrusted (`XB-01`).
- **Bounded recommendation request** — the input handed to the recommendation model for a residual line. It contains the line context and an **enumerated, pre-validated candidate set** of allowed GL accounts / PO lines. The model may only select from this set or abstain; it never receives an open-ended coding task ([DP-03](../../../ra/01-foundations/design-principles.md)).
- **Coding proposal** — the model's output for a residual line: a selection from the bounded set (or a `UNC` abstention), with confidence. It is a proposal only and holds no authority until adjudicated by `DVL` and `POL`.
- **ERP draft intent** — the exact, deterministic payload assembled from validated coding to create one unposted draft. It carries an `IDM` idempotency key and is executed as a `TRW` write at `EF2` under constrained credentials. It describes an unposted draft only — never a posting or payment.
- **Approval record** — the reviewer's disposition bound to one exact draft **version and digest**: approve, reject, request-change, or timeout. It authorises that specific unposted version and nothing else; it does not authorise payment ([INV-013][architecture-invariants], [INV-014][architecture-invariants]).

## Authoritative state checkpoints

The workflow state store is the system of record and records `EVH` execution history (`OV-07`); it links to (does not duplicate) the ERP draft identity ([INV-002][architecture-invariants]).

| Checkpoint | State recorded |
|---|---|
| Submission accepted | Run opened; submission metadata and `TRG` context. |
| Source fixed | Immutable source artefact identity and provenance (`DFN`); attachment-control result (`XB-01`). |
| Extraction validated | Canonical invoice after `AIN` + `SCH`, with per-field provenance. |
| Reference context read | Vendor / PO / receipt / GL snapshot used for matching (`RET`). |
| Baseline resolved | Deterministic match, tolerance, receipt, inheritance, and duplicate-detection outcomes; the set of residual lines (`WP00`). |
| Coding adjudicated | Accepted coding, or abstention, for each residual line after `REC` + `DVL` + `POL`. |
| Draft created | Linked ERP draft identity and version; `IDM` key; confirm/reconcile status of the `TRW` effect. |
| Review disposition | Approval record bound to the exact version and digest, or reject / request-change / timeout; terminal outcome and `FSK` closure. |

Durable resumable state is written at `CHK` so the run survives restarts across the review `WAI` (`WP08`).

## Version rule

A **material change** to a draft creates a **new draft version** and **invalidates any previous approval**. A change is material when it alters any of:

- coding (GL account or PO line selection),
- invoice or line amount,
- tax,
- vendor or legal entity,
- purchase order,
- accounting dimensions.

When a material change occurs after a draft was built or approved, the workflow produces a new version, links it to the run, and requires a fresh approval of that exact version and digest. A prior approval never carries forward to a changed draft ([INV-013][architecture-invariants], [INV-014][architecture-invariants]). Non-material edits that do not touch these fields do not invalidate an existing approval.

## Related views

- [architecture.md](architecture.md) — logical architecture and actors.
- [execution.md](execution.md) — stage-by-stage walkthrough.
- [sequence.md](sequence.md) — interaction sequence.

<!-- link definitions -->
[architecture-invariants]: ../../../ra/01-foundations/architecture-invariants.md
