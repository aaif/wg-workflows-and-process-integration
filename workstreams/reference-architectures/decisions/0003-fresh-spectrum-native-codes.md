# ADR 0003: Fresh, Spectrum-Native Code System

## Status

Proposed

## Date

2026-07-27

## Context

An earlier draft (SAW-RA) built its classification codes around "one logical agent authority," with single-letter axes (`N/A/F/S/X/V/I`) and an `A0`–`A6` agent-authority axis as a first-class organising dimension. Reusing those verbatim would carry single-agent assumptions into an architecture meant to span the whole determinism spectrum.

## Options considered

- **Keep codes as-is, re-scope** — lowest churn, but single-agent assumptions leak through.
- **Generalise existing codes** — moderate; retains some baggage.
- **Fresh, spectrum-native codes** — design axes that are neutral from day one, borrowing the *style* (stable prefixes + coordinates) but not the specific IDs.

## Decision

Adopt a **fresh code system**: eight orthogonal [classification axes](../model/classification.md) where agent count is just `actor_topology`. Ordinal axes get prefixes (`ND`, `FS`, `DUR`, `EF`, `AS`, `IM`); categorical axes use enum strings. Patterns are `WP##`, profiles `EP#`, overlays `OV-##`, boundaries `XB-##`, readiness `RT#`, conformance `CL#`.

## Rationale

`EF` (effect) replaces the opaque `X`; `DUR` replaces `S`; `AS` replaces the overloaded `V`; the old `A` agent-authority axis is superseded by the five-authority model plus `actor_topology`. Every `EFn` now resolves to one published scale, fixing an earlier gap where effect codes had no single referent.

## Consequences

A one-time cost to re-mint IDs, offset by a vocabulary with no single-agent bias and no code collisions. All codes live in [registry.yaml](../descriptor/registry.yaml).

## Follow-up

If migrating older SAW-RA material, publish an old→new crosswalk.
