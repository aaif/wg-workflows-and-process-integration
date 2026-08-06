# The Reference Architecture (knowledgebase)

Status: Index

This folder **is** the Workflow Execution Reference Architecture — the knowledgebase
itself, in nine numbered chapters. Read them in order for the full picture, or jump to a
chapter by its number. The machine-readable form of every code defined here is published
as data in [registry.yaml](../descriptor/registry.yaml).

The chapters are grouped into the six themes below; the numbering is the reading order.

## Foundations

Purpose, scope, shared language, and the non-negotiable rules.

- [`01-foundations/`](01-foundations/scope-and-boundaries.md) — [scope and boundaries](01-foundations/scope-and-boundaries.md), [core concepts](01-foundations/core-concepts.md), [design principles](01-foundations/design-principles.md) (`DP-##`), [architecture invariants](01-foundations/architecture-invariants.md) (`INV-###`).

## Architecture model

The building blocks of a workflow run, how they are classified, and how they combine.

- [`02-architecture-model/`](02-architecture-model/README.md) — reference model, the eight-axis [classification](02-architecture-model/classification.md), [primitive catalog](02-architecture-model/primitive-catalog.md), runtime components (`RC-##`), composition rules (`CR-###`).

## Patterns and selection

The reusable solutions, the whole-run styles, and how to choose between them.

- [`03-patterns/`](03-patterns/README.md) — the pattern catalogue (`WP00`–`WP11`).
- [`04-profiles/`](04-profiles/README.md) — whole-run execution profiles (`EP1`–`EP7`).
- [`05-selection/`](05-selection/README.md) — wizard questions, [selection logic](05-selection/selection-logic.yaml), pattern coordinates.

## Enterprise readiness

The cross-cutting controls and how production-readiness is measured.

- [`06-overlays/`](06-overlays/README.md) — workflow overlays (`OV-##`) and external boundaries to other WGs (`XB-##`).
- [`07-readiness/`](07-readiness/readiness-tiers.md) — readiness tiers (`RT#`) and conformance levels (`CL#`).

## Lifecycle

How the architecture is actually used to design a workflow.

- [`08-lifecycle/`](08-lifecycle/workflow-design-method.md) — the [Workflow Design Method](08-lifecycle/workflow-design-method.md), [review checklist](08-lifecycle/review-checklist.md), [AI agent instructions](08-lifecycle/ai-agent-instructions.md).

## Evolution

What is unfinished, and why the important choices were made.

- [`09-evolution/`](09-evolution/roadmap.md) — the [roadmap](09-evolution/roadmap.md) and [decision records](09-evolution/decisions/README.md).

## Stable addresses

These chapter paths are **stable**: other documents (and `registry.yaml`) link to them by
address, so they should not be renumbered or moved without updating references. When you
cite a chapter from elsewhere, link to the chapter folder's index or a stable code anchor
rather than deep into a leaf file, so internal reorganisation stays cheap.
