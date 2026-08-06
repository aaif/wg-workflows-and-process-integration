# Readiness Tiers

Status: Mature

Readiness tiers (`RT#`) describe how production-ready a workflow is. A tier is chosen based on [impact](../02-architecture-model/classification.md) (`IM#`) and sets minimum expectations for controls and evidence. Readiness is about **operational maturity**; [conformance](conformance.md) is about **following the architecture** — they are separate.

| Code | Tier | Purpose | Allowed | Required | Not allowed |
|---|---|---|---|---|---|
| RT0 | Experiment | Explore feasibility in isolation | Synthetic or approved low-risk data; disposable state | Named owner, bounded cost, basic logging, no production credentials | Production data, production writes, high-impact effects |
| RT1 | Controlled pilot | Limited real use under supervision | Real data with restrictions; reversible effects (`EF≤2`) | Human review/approval on effects, `OV-07` history, rollback plan | Irreversible effects without approval |
| RT2 | Production | Routine business use | Effects per declared level with controls | `OV-02` protected effects, `OV-07` system of record (`RC-10`), reconciliation for `EF3`+, defined SLOs | Undeclared effects, unversioned approvals |
| RT3 | Business critical | High-value / hard-to-reverse | `EF3`/`EF4` with strong controls | `AS4`+ approval, segregation of duties, tested recovery, capacity plan | Single points of failure in the effect path |
| RT4 | Regulated or high impact | Regulated, safety, or severe-impact | Only with full evidence chain | `AS5` multi-party approval, full evidence, governance sign-off via `XB-04` | Any control gap; unreviewed model changes |

## Choosing a tier

Start from the run's `impact` coordinate: `IM0→RT0`, `IM1→RT1`, `IM2→RT2`, `IM3→RT3`, `IM4→RT4` is the floor. A workflow may be held to a higher tier than its impact floor, never lower.

## Evidence

Each tier expects the evidence its controls produce (approval records, effect confirmations, execution history, recovery tests). The [review checklist](../08-lifecycle/review-checklist.md) enumerates the required [architecture views](../08-lifecycle/review-checklist.md) (`VW-##`) per tier.

## Open questions

- Should latency/throughput objectives be part of the tier definition or a separate operational profile?
- How are model/instruction version changes gated between tiers (relates to `XB-05`)?
