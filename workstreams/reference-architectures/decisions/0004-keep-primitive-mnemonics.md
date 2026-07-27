# ADR 0004: Keep the Three-Letter Primitive Mnemonics

## Status

Proposed

## Date

2026-07-27

## Context

ADR 0003 mints fresh codes for the classification axes and higher-level constructs. The question remained whether to also re-mint the ~46 three-letter primitive mnemonics (`TRG`, `INP`, `GEN`, `CHK`, `IDM`, `AUD`, `HRV`, `APR`, …) inherited from the earlier draft.

## Options considered

- **Re-mint all primitives** — maximal uniformity with the fresh scheme, but discards a large, already-reviewed, and semantically neutral asset for little gain, and needs a crosswalk.
- **Keep the mnemonics** — preserve them verbatim, re-rooting only their prose onto the workflow-run spectrum.

## Decision

**Keep** the three-letter primitive mnemonics. Add exactly two for the agentic/cross-runtime end of the spectrum: `DLG` (delegate goal) and `HND` (handoff / control transfer).

## Rationale

The mnemonics describe **capabilities**, not agent count, so they carry no single-agent assumption. They are the most reusable and most-reviewed part of the prior work. Keeping them lowers churn and preserves recognisability while the fresh axes do the spectrum-neutral organising.

## Consequences

The [primitive catalog](../model/primitive-catalog.md) and [registry.yaml](../descriptor/registry.yaml) list the kept mnemonics plus `DLG`/`HND`. New primitives require justification ([DP-10](../foundations/design-principles.md)).

## Follow-up

Review whether any kept primitive needs its prose adjusted for multi-agent contexts.
