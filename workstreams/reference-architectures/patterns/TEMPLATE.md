# Pattern Name — name the fix, not the use case

**Solves:** One-line problem statement \
**Used in:** Links to the architectures that compose this pattern \
**Requires capabilities:** Capability roles needed to implement the pattern \
**Related patterns:** Links to other entries in `patterns/`

*(Header convention: every field line ends with a trailing backslash except
the last; field values start capitalized.)*

## Problem

The recurring sub-problem, stated so a practitioner recognizes it from their
own system. Two or three sentences.

## Why this is hard

The pulls in different directions that rule out the naive solution. Bullets.

## Solution

The shape, in 2–4 boxes. Context-free: no deployment story, no product
names, no use-case specifics. If the diagram needs more than 4 boxes, it is
probably a reference architecture, not a pattern.

## Invariants (must hold in any implementation)

Properties any implementation must guarantee. Written so the sentence still
holds with any product name swapped in — if it stops making sense, it is one
product's mechanism and belongs in the runtimes table below.

## Failure modes when violated

What actually breaks, invariant by invariant. Concrete: "every deploy
silently kills pending approvals," not "reduced reliability."

## Implementation approaches (illustrative, not requirements)

Link to primary documentation for each named mechanism. Distinguish what the
runtime or platform actually provides from the controls an implementation must
add: no individual feature should be presented as satisfying every invariant
unless its documentation supports that claim.

Group entries by the dimension along which implementations *of this pattern*
genuinely differ — the axis is pattern-specific, so name it first (for a
continuation pattern it may be execution families; for a separation pattern,
enforcement points). Use 2–3 examples spanning more than one group so no
single approach reads as canonical. A pattern only one runtime can satisfy may
not be a shared pattern; a pattern only one *group* can satisfy may be that
group's feature wearing a pattern's name.

| (Axis) | Documented mechanism | What it provides | What the implementation must add |
|---|---|---|---|
| … | … | … | … |

## Known uses outside agents (optional)

Precedents older than agentic AI, doing two jobs. Evidence: the industry
converged on this shape before LLMs existed, so the pattern is discovered,
not invented. Transfer: the charter's core gap is translating deterministic
workflow knowledge into agentic workflows — so name what the reader's
organization already operates, then name the delta: what the agent changes
about it.
