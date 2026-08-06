# Charter Traceability

Status: Mature

This document maps the [charter](../../charter/charter.md) scope areas and deliverables to the WERA documents that satisfy them, so reviewers can confirm the workstream stays inside its mandate.

## Scope areas → documents

| Charter scope | WERA coverage |
|---|---|
| **A. Agent Workflow Models and Semantics** | [core-concepts](ra/01-foundations/core-concepts.md), [reference-model](ra/02-architecture-model/reference-model.md), [primitive-catalog](ra/02-architecture-model/primitive-catalog.md), [classification](ra/02-architecture-model/classification.md) |
| **B. Long-Running and Stateful Execution** | [core-concepts §execution state](ra/01-foundations/core-concepts.md), `OV-04` durable wait, `OV-07` execution history, [readiness](ra/07-readiness/readiness-tiers.md); reliability semantics is Proposal-level |
| **C. Tool Invocation and External Coordination** | `RC-06` tool gateway, `RC-07` effect executor, `OV-02` protected effect, [composition-rules](ra/02-architecture-model/composition-rules.md) |
| **D. Human-in-the-Loop Patterns** | `WP07` human-supervised action, `OV-01` human approval, [profiles EP5](ra/04-profiles/README.md) |
| **E. Portability and Interoperability** | [descriptor](descriptor/README.md) (the portable WDS), `WP11`/`EP7` cross-runtime handoff, `HND` primitive |
| **F. Operational Patterns for Production** | [readiness tiers](ra/07-readiness/readiness-tiers.md), [conformance](ra/07-readiness/conformance.md), `WP08` durable envelope |

## Deliverables → documents

| Charter deliverable | WERA coverage |
|---|---|
| **Workflow Taxonomy** | [classification](ra/02-architecture-model/classification.md) + [primitive-catalog](ra/02-architecture-model/primitive-catalog.md) + [registry.yaml](descriptor/registry.yaml) |
| **Workflow Best Practices** | [design-principles](ra/01-foundations/design-principles.md) + [playbook](ra/08-lifecycle/workflow-design-method.md) + [patterns](ra/03-patterns/README.md) |
| **Workflow Reference Architecture** | [foundations](ra/01-foundations/scope-and-boundaries.md) + [model](ra/02-architecture-model/README.md) + [profiles](ra/04-profiles/README.md) |
| **Horizontal Use Cases Landscape** | [examples](examples/README.md) (invoice processing today; more exemplars planned) |

## Boundaries → other WGs

The concerns in the charter's "Out of Scope" list are referenced through [external boundaries](ra/06-overlays/external-boundaries.md) (`XB-01`–`XB-05`) and are not redefined here (see [INV-015](ra/01-foundations/architecture-invariants.md)).
