# Invoice Processing — Rationale

Status: Mature worked example

*This is the **Reasoning**: the six-step [Workflow Design Method](../../ra/08-lifecycle/workflow-design-method.md) applied to the [use case](use-case.md). It is the reasoning an AI agent should also produce.*

## Step 1 — Understand the business outcome

**Outcome:** a validated, unposted AP draft linked to the invoice and evidence, plus a final reviewer disposition for that exact draft version.

**Run boundary:** starts when an invoice submission is accepted; ends in one of `COMPLETED` (approved for handoff), `REJECTED`, `ABSTAINED`, `MANUAL_DISPOSITION`, or `FAILED_TECHNICAL` ([INV-004][architecture-invariants], [INV-005][architecture-invariants]).

**System of record:** the workflow execution store, linked to (not duplicating) the ERP draft identity ([INV-002][architecture-invariants]).

## Step 2 — Identify the deterministic baseline

Most of the work is deterministic and needs no model ([DP-02][design-principles], [WP00](../../ra/03-patterns/wp00-deterministic-baseline.md)): attachment security and de-duplication; schema and arithmetic validation of extracted data; PO lookup; vendor/legal-entity equality; price/quantity tolerances; receipt matching; PO coding inheritance; duplicate-invoice detection; active-account and dimension rules. This is the **least-agentic path** and it resolves the normal case.

## Step 3 — Identify semantic gaps

Two residual tasks resist rules:

1. **Extraction** of fields from an untrusted document → primitive `AIN`, validated by `SCH` ([WP01](../../ra/03-patterns/wp01-bounded-model-step.md)). Locus `ND1` (content).
2. **Coding of residual lines** the deterministic matcher cannot resolve → the *smallest* task is **selection from a bounded, validated candidate set**, not free generation ([DP-03][design-principles], [DP-07][design-principles]). Locus `ND3` (selection); abstention allowed.

The effect (creating an unposted draft) is a **reversible write** → `EF2`. Impact is material but correctable pre-payment → `IM2`. The run waits for a reviewer and must survive restarts → `DUR3`. Human approval is required before handoff → `AS4`.

This fixes the [coordinate](../../ra/02-architecture-model/classification.md):

```yaml
nondeterminism: ND3
control_flow_authority: workflow
actor_topology: single_agent
flow_shape: FS7
durability: DUR3
effect_level: EF2
assurance: AS4
impact: IM2
```

## Step 4 — Choose the execution profile

Control flow stays with the workflow; the model only proposes. That is [profile `EP2`](../../ra/04-profiles/ep2-workflow-directed-model-assisted.md) (workflow-directed + model-assisted). The [five authorities](../../ra/02-architecture-model/reference-model.md) allocate as:

| Authority | Holder |
|---|---|
| Control-flow | Workflow runtime (validated disposition rules) |
| Decision | AP policy + human reviewer |
| Action-authorisation | Policy for draft creation; reviewer for the exact version |
| Execution | ERP adapter (constrained credentials) |
| State | Workflow system of record |

The recommendation model holds **none** of these ([INV-006][architecture-invariants], [INV-007][architecture-invariants]).

## Step 5 — Apply patterns and overlays

- Primary: [`WP02`](../../ra/03-patterns/wp02-recommend-adjudicate.md) — recommend + deterministic adjudication (the residual-line coding).
- Embedded: [`WP00`](../../ra/03-patterns/wp00-deterministic-baseline.md) (baseline), [`WP01`](../../ra/03-patterns/wp01-bounded-model-step.md) (extraction), [`WP07`](../../ra/03-patterns/wp07-human-supervised-action.md) (approval gate).
- Envelope: [`WP08`](../../ra/03-patterns/wp08-durable-workflow-envelope.md) — durability across the review wait.
- Overlays: [`OV-01`][workflow-overlays] approval, [`OV-02`][workflow-overlays] protected effect, [`OV-07`][workflow-overlays] execution history.
- External boundaries: `XB-01` (untrusted input), `XB-02` (identity of reviewer/adapter), `XB-03` (trace signals), `XB-04` (audit/governance) — all referenced, none redefined ([INV-015][architecture-invariants]).

The primitive graph is built from these; ambiguous ERP results reconcile rather than blind-retry ([INV-011][architecture-invariants]).

## Step 6 — Produce the WDS

The design is assembled into the descriptor and validated. Target readiness `RT2`, conformance `CL2`. See the [solution](solution.md) and the machine-readable [WDS](invoice-processing.wera.yaml).

## Alternatives rejected

- **`WP04` generate-validate-repair** — no free-form generation is needed; selection suffices.
- **`WP09` bounded agentic region** — no tool/plan autonomy is required; adding it would violate [DP-01][design-principles].
- **`EF3` for the draft** — an unposted draft is reversible, so `EF2`; the `EF3`/`EF4` controls attach to the *later* posting/payment step, which is out of scope.

<!-- link definitions -->
[architecture-invariants]: ../../ra/01-foundations/architecture-invariants.md
[design-principles]: ../../ra/01-foundations/design-principles.md
[workflow-overlays]: ../../ra/06-overlays/workflow-overlays.md
