# Workflow Descriptor — Field Reference

Status: Mature

Field-by-field documentation for a `*.wera.yaml` descriptor. The authoritative constraints are in [workflow-descriptor.schema.json](workflow-descriptor.schema.json); this document explains intent. Codes resolve against [registry.yaml](registry.yaml) and the [classification axes](../model/classification.md).

## Top level

| Field | Required | Meaning |
|---|---|---|
| `wera_version` | yes | Registry/schema version the descriptor targets. |
| `workflow` | yes | Identity, outcome, and run boundary. |
| `intake` | yes | The captured use case. |
| `design` | yes | The resolved architecture. |
| `recommendation` | no | Rationale and supporting detail. |

## `workflow`

| Field | Required | Meaning |
|---|---|---|
| `id`, `name` | yes | Stable identity for the workflow definition. |
| `owner` | no | Accountable team. |
| `intended_outcome` | yes | The business/operational result pursued. |
| `authoritative_decision_owner` | no | Who owns the authoritative decision. |
| `run_boundary.start` | yes | Start condition ([INV-004](../foundations/architecture-invariants.md)). |
| `run_boundary.terminal_outcomes` | yes | Subset of the closed [terminal-outcome set](../model/classification.md) ([INV-005](../foundations/architecture-invariants.md)). |

## `intake`

Captures the answers to the [wizard questions](../selection/wizard-questions.md).

- `inputs` — sources, schemas, `data_classification`, and whether `untrusted_content` is present (drives `XB-01`, [INV-018](../foundations/architecture-invariants.md)).
- `nondeterminism` — whether nondeterminism is `required`, the `smallest_semantic_task`, and `reason_rules_insufficient` ([DP-02](../foundations/design-principles.md), [DP-03](../foundations/design-principles.md)).
- `requested_authority` — booleans for branch/tool/write/delegate authority the design may grant.
- `assurance` — deterministic verification level, human review/approval, abstention.
- `side_effects` — highest `level` (`EF0`–`EF4`), reversibility, idempotency, compensation.
- `operations` — `target_readiness` (`RT#`), `impact` (`IM#`), objectives, budget, provenance.

## `design`

The resolved architecture; this is what conformance checks read.

- `coordinates` — one value per [classification axis](../model/classification.md) (all eight required).
- `authority_allocation` — the five authorities, each mapped to a holder ([INV-006](../foundations/architecture-invariants.md)).
- `primitive_graph` — `nodes` (each a [primitive](../model/primitive-catalog.md) with an id/label) and `edges` (with optional `condition`). This is the machine-readable workflow shape.
- `effects` — each externally visible effect with its `level`, `idempotency_key`, `authoriser`, `executor` ([INV-010](../foundations/architecture-invariants.md), [INV-012](../foundations/architecture-invariants.md)).
- `selected_profile` (`EP#`), `selected_pattern` (`WP##`), `embedded_patterns`, `lifecycle_envelope` (often `WP08` or null).
- `overlays` (`OV-##`), `external_boundaries` (`XB-##`), `runtime_components` (`RC-##`).
- `readiness_tier` (`RT#`), `conformance_target` (`CL#`).

## `recommendation`

- `deterministic_baseline` — the rules-only path before nondeterminism ([DP-02](../foundations/design-principles.md)).
- `agent_justification` — why the model/agent is needed, and how narrowly ([DP-01](../foundations/design-principles.md), [DP-03](../foundations/design-principles.md)).
- `selection_explanation` — how the coordinate led to the profile/patterns/overlays.
- `alternatives_rejected` — patterns/profiles considered and why not chosen.
- `mandatory_primitives` — primitives the design cannot omit.
- `required_views` — architecture views (`VW-##`) the [review checklist](../playbook/review-checklist.md) expects.
- `exceptions` — any rule consciously not met, with rationale and compensating control (see [conformance](../readiness/conformance.md)).

## Minimal valid descriptor

```yaml
wera_version: v2-descriptor-driven
workflow:
  id: example
  name: Example
  intended_outcome: Do the thing correctly.
  run_boundary:
    start: A request is accepted.
    terminal_outcomes: [COMPLETED, REJECTED, FAILED_TECHNICAL]
intake:
  inputs: { untrusted_content: false }
  nondeterminism: { required: false }
  side_effects: { level: EF0 }
design:
  coordinates:
    nondeterminism: ND0
    control_flow_authority: workflow
    actor_topology: none
    flow_shape: FS2
    durability: DUR1
    effect_level: EF0
    assurance: AS1
    impact: IM0
  authority_allocation:
    control_flow: Workflow runtime
    decision: Deterministic rules
    action_authorisation: Not applicable
    execution: Task worker
    state: Workflow system of record
  primitive_graph:
    nodes:
      - { id: n1, primitive: TRG, label: Start }
      - { id: n2, primitive: DFN, label: Compute }
      - { id: n3, primitive: FSK, label: Done }
    edges:
      - { from: n1, to: n2 }
      - { from: n2, to: n3 }
  selected_profile: EP1
  selected_pattern: WP00
```
