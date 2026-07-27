# Review Checklist

Status: Mature

Use this to review a Workflow Design Specification — whether produced in human mode or AI mode. It doubles as the checklist for assessing an existing workflow. Items map to [invariants](../foundations/architecture-invariants.md), [composition rules](../model/composition-rules.md), and [conformance levels](../readiness/conformance.md).

## Boundary and outcome

- [ ] Run boundary is explicit: start condition + closed terminal-outcome set (`INV-004`, `INV-005`).
- [ ] A single authoritative system of record is named (`INV-002`).

## Baseline and nondeterminism

- [ ] The deterministic baseline is documented (`DP-02`, `CR-001`).
- [ ] Each nondeterministic step declares purpose, contracts, authority, timeout, failure behaviour (`INV-001`).
- [ ] The smallest viable semantic task was chosen; least-agentic composition (`DP-01`, `DP-03`).

## Authority

- [ ] All five authorities are allocated for each consequential step (`INV-006`).
- [ ] No actor is the sole authoriser of an effect it proposes (`INV-007`, `CR-004`).
- [ ] Delegated regions declare tools, data, effect ceiling, budgets, exit states, state owner (`INV-008`, `CR-010`).

## Proposals and effects

- [ ] Semantic output is validated before it becomes state (`INV-003`, `CR-002`).
- [ ] Effects at `EF2`+ carry idempotency; ambiguous results reconcile, not blind-retry (`INV-011`, `CR-005`).
- [ ] Effect payloads are versioned and confirmation is linked to the run (`INV-012`).
- [ ] Execution uses constrained, least-privilege credentials (`INV-010`).

## Humans

- [ ] Approval binds an exact version/digest; material change invalidates it (`INV-013`, `CR-012`).
- [ ] Approve/reject/request-change/timeout are all explicit outcomes (`INV-014`).

## Boundaries and neutrality

- [ ] Cross-WG concerns are referenced via `XB-##`, not redefined (`INV-015`, `CR-017`).
- [ ] Untrusted input is gated before any semantic step (`INV-018`, `CR-013`).
- [ ] No product/vendor lock-in in normative content (`INV-016`).

## Machine-readability

- [ ] Every relied-upon concept has a code in [registry.yaml](../descriptor/registry.yaml) (`INV-017`, `CR-020`).
- [ ] The descriptor validates against the [schema](../descriptor/workflow-descriptor.schema.json).

## Required architecture views

A WDS SHOULD be accompanied by these views (`VW-##`); the required subset rises with readiness tier.

| Code | View | Typical floor |
|---|---|---|
| VW-01 | Workflow context view | RT0 |
| VW-02 | Run-boundary and outcome view | RT0 |
| VW-03 | Primitive graph | RT1 |
| VW-04 | Coordinate summary | RT1 |
| VW-05 | Authority allocation matrix | RT1 |
| VW-06 | State and durability view | RT2 |
| VW-07 | Effect and protection view | RT2 |
| VW-08 | Human-task and approval view | RT2 |
| VW-09 | Reliability and recovery view | RT2 |
| VW-10 | Tool and capability matrix | RT2 |
| VW-11 | External-boundary map | RT2 |
| VW-12 | Dependency and failure view | RT3 |

## Verdict

Record the achieved [conformance level](../readiness/conformance.md) (`CL0`–`CL3`) and any documented exceptions.
