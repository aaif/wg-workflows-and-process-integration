# Design Principles

Status: Mature

Design principles (`DP-##`) guide the day-to-day choices a designer makes when applying WERA to a specific workflow. They sit between the high-level [architecture principles](../../docs/architecture-principles.md) (direction) and the [architecture invariants](architecture-invariants.md) (`INV-###`, testable rules).

The governing design principle is **DP-01**.

## DP-01 — Least-agentic composition

Use the least-agentic composition that satisfies the workflow's semantic requirements. Keep control, authorisation, validation, durable state, and recovery deterministic wherever practical. Introduce a model, an agentic region, or multi-agent delegation only for the residual task that deterministic logic cannot handle.

## DP-02 — Deterministic baseline first

Document the deterministic baseline before adding any nondeterministic step, and record why each nondeterministic step is necessary.

## DP-03 — Smallest semantic task

When nondeterminism is justified, give the model the smallest, most bounded task that resolves the semantic gap — a closed candidate set rather than an open field wherever possible.

## DP-04 — Explicit authority allocation

Allocate all five authorities explicitly for every consequential step. Never leave "who decides / who authorises / who executes / who records" implicit.

## DP-05 — Proposals are validated before they become state

Treat every probabilistic output as a proposal. Validate schema, policy, evidence, and authority before committing an accepted transition.

## DP-06 — Protect effects proportionally

Match effect protection to effect level and impact. Higher `EF`/`IM` coordinates require stronger authorisation, idempotency, confirmation, and reconciliation.

## DP-07 — Prefer closed sets over open generation

Where a decision can be framed as selection from a validated candidate set, prefer it to free-form generation. It is easier to validate, review, and reproduce.

## DP-08 — Make waits and durability explicit

If a workflow may pause for time, humans, or events, or may outlive its process, model the durable wait and state persistence explicitly rather than assuming a single process lifetime.

## DP-09 — Bound every dynamic region

Every agentic region, plan, or delegation declares capability limits, allowed effects, budgets, exit states, and state ownership before it runs.

## DP-10 — Reuse patterns; justify novelty

Compose the workflow from existing [patterns](../03-patterns/README.md) and [profiles](../04-profiles/README.md). If you must introduce a concept not in this repository, explain why the existing concepts were insufficient — this is the same rule that applies to an AI agent.

## DP-11 — Reference cross-WG concerns, do not redefine them

For security, identity, observability, governance, and accuracy, point to the relevant [external boundary](../06-overlays/external-boundaries.md) rather than inventing local requirements.

## DP-12 — Design for both readers

A design should be expressible as a [descriptor](../../descriptor/README.md) so it is legible to humans and machines alike. If a design cannot be captured in the descriptor, that is a signal the design or the schema needs attention.
