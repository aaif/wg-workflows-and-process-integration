# ADR 0006: Example-Driven Maturation

## Status

Proposed

## Date

2026-07-27

## Context

Completing every reference-architecture area before Working Group review would embed many untested design decisions and make the contribution look finished when it is not yet agreed.

## Options considered

- **Complete-everything-first** — impressive, but asks the WG to accept a large body of decisions wholesale and hides which parts are load-bearing.
- **Example-driven maturation** — establish the full structure, but mature concepts only when a worked example requires them; leave the rest as explicit proposals with open questions.

## Decision

Adopt **example-driven maturation**. The full skeleton exists; only the concepts and patterns the current worked example ([invoice processing](../../../examples/invoice-processing/README.md)) needs are marked **Mature**. Everything else is a labelled **Proposal**. Even proposal docs still carry their codes so [registry.yaml](../../../descriptor/registry.yaml) stays complete.

## Rationale

It is a better opening move for a group meant to *debate and co-own* the result: easy to challenge, honest about maturity, and it makes the [acceptance test](../../../docs/acceptance-test.md) — not page count — the driver of each iteration.

## Consequences

The repository is coherent but intentionally incomplete; the [ROADMAP](../roadmap.md) states what is deferred and why. Additional examples are the mechanism for maturing more of the model.

## Follow-up

Prioritise the next example by which architecture area is least tested (fan-out, bounded-agentic, cross-runtime).
