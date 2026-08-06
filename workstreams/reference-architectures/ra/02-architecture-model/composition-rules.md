# Composition Rules

Status: Mature

## Why this document exists

Composition rules (`CR-###`) constrain how primitives may be combined into a valid workflow. They turn the [invariants][architecture-invariants] and [design principles][design-principles] into concrete "you may / you must / you must not compose it this way" guidance. Rules use RFC 2119 language.

## Rules

### CR-001 — Deterministic baseline documented

The design MUST document the deterministic baseline and the reason each nondeterministic primitive (`AIN`, `CLS`, `GEN`, `REC`, `PLN`, `TSL`, `ABR`) is needed ([DP-02][design-principles]).

### CR-002 — Semantic output is validated before use

Any `AIN`/`CLS`/`GEN`/`REC`/`PLN` output that drives a transition or effect MUST be followed by `DVL`, `POL`, or `APR` before it is accepted ([INV-003][architecture-invariants]).

### CR-003 — No effect without authorisation

`TRW`, `TXN`, `THI` MUST be preceded by `POL` (and `APR` where impact requires) in the same accepted path ([INV-009][architecture-invariants]).

### CR-004 — Effect proposer ≠ sole authoriser

The primitive that proposes an effect MUST NOT be the only authoriser of it ([INV-007][architecture-invariants]).

### CR-005 — Writes carry idempotency

Every `TRW`/`TXN`/`THI` MUST be paired with `IDM`, and ambiguous results MUST route to `RCP`, not a bare `RTY` ([INV-011][architecture-invariants]).

### CR-006 — Retries only on classified failures

`RTY` MUST declare a retry class and MUST NOT wrap a non-idempotent effect without `IDM`.

### CR-007 — Waits are durable

Any `WAI` that can outlive the process MUST be backed by `CHK` and durable state (`DUR2`+) ([DP-08][design-principles]).

### CR-008 — Parallel needs a join

Every `PAR` MUST declare join semantics and late-result treatment.

### CR-009 — Loops are bounded

Every `LOP` MUST declare a maximum iteration count and a progress/exit condition.

### CR-010 — Delegation is bounded

Every `DLG` MUST declare allowed tools/data, maximum effect level, budgets, exit states, and state owner before execution ([INV-008][architecture-invariants]).

### CR-011 — Handoff carries a portable envelope

Every `HND` MUST carry run/task identity, accepted context, capability and effect permissions, budget/deadline, expected result, and state-ownership.

### CR-012 — Human approval binds a version

Every `APR` MUST bind to an immutable artifact version/digest; a material change MUST invalidate it ([INV-013][architecture-invariants]).

### CR-013 — Untrusted input is gated

`INP`/`RET` of untrusted content MUST pass input controls before any semantic primitive consumes it ([INV-018][architecture-invariants]).

### CR-014 — One system of record

Accepted state MUST be written through `EVH`/`CHK` to a single system of record; `SME`/`DME`/`TRC` MUST NOT be the sole record ([INV-002][architecture-invariants]).

### CR-015 — Terminal outcome required

Every run path MUST end in `FSK` with a terminal outcome from the closed set ([INV-005][architecture-invariants]).

### CR-016 — Effect level matches controls

The controls attached to an effect MUST match its `effect_level` coordinate (e.g. `EF4` requires `APR`/segregation) ([DP-06][design-principles]).

### CR-017 — Cross-WG concerns via boundaries

Security, identity, observability, governance, and accuracy needs MUST be expressed as `XB-##` references, not new local primitives ([INV-015][architecture-invariants]).

### CR-018 — Budgets on dynamic regions

Any region containing `PLN`/`DLG`/`ABR`/`LOP` MUST declare a `CST`/budget bound ([DP-09][design-principles]).

### CR-019 — Abstention is always available to semantic steps

Any `REC`/`CLS`/`AIN` that can be wrong in a consequential way MUST support `UNC` (abstain/escalate).

### CR-020 — Every relied-upon concept is coded

A composed workflow MUST use only codes present in the [registry](../../descriptor/registry.yaml); a new concept requires justification ([DP-10][design-principles], [INV-017][architecture-invariants]).

## Anti-patterns

Common invalid or risky compositions (`AP-##`). Each names a symptom, the risk, and the correction.

| Code | Anti-pattern | Symptom → Correction |
|---|---|---|
| AP-01 | Agent everywhere | Every step routed through a model → restore `WP00` for deterministic steps |
| AP-02 | Silent whole-process agent | An agent quietly owns the whole run → make control-flow authority explicit |
| AP-03 | Proposal as state | Model output written directly to the system of record → insert `DVL`/`POL` |
| AP-04 | Self-approval | Proposer authorises its own effect → apply `CR-004` |
| AP-05 | Blind retry on writes | `RTY` around a non-idempotent write → add `IDM`/`RCP` |
| AP-06 | Vague approval | Human approves a summary, not the exact version → apply `CR-012` |
| AP-07 | Context as record | `SME`/model context used as system of record → apply `CR-014` |
| AP-08 | Unbounded plan | `PLN`/`DLG` without budgets or exit states → apply `CR-010`/`CR-018` |
| AP-09 | Open generation where a closed set exists | Free-form `GEN` instead of `REC` over candidates → apply `DP-07` |
| AP-10 | Missing terminal outcome | Paths that neither complete nor fail explicitly → apply `CR-015` |
| AP-11 | Effect ceiling ignored | Tool selection can exceed the declared effect level → constrain `TSL` |
| AP-12 | Cross-WG fork | Re-implementing security/observability locally → apply `CR-017` |
| AP-13 | Hidden model in a service | Model behaviour concealed behind a "deterministic" contract → declare it (`INV-001`) |
| AP-14 | Durable wait without durability | `WAI` on ephemeral state → apply `CR-007` |
| AP-15 | Parallel without join | `PAR` with no join/late-result rule → apply `CR-008` |
| AP-16 | Unlogged decision | Consequential decision with no `AUD`/`EVH` → add audit |
| AP-17 | Uncoded concept | Design invents a concept absent from the registry → apply `CR-020` |
| AP-18 | Approval reused across changes | One approval covers later materially different actions → apply `CR-012`/`INV-013` |

<!-- link definitions -->
[architecture-invariants]: ../01-foundations/architecture-invariants.md
[design-principles]: ../01-foundations/design-principles.md
