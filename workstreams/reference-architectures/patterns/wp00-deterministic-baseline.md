# WP00 — Deterministic Baseline

Status: Mature

## Problem
Many workflow steps have a well-defined, closed specification and require no
inference at all. Reaching for a model where deterministic logic suffices adds
nondeterminism, cost, and assurance burden for no benefit. This pattern is the
floor that every design starts from before any semantic capability is
introduced.

## When to use / not use
- Use when the transformation is fully specified by rules, schemas, or lookups.
- Use as the default path; only escalate to a semantic pattern when a genuine
  inference need is demonstrated (see [design principles](../foundations/design-principles.md), DP-02).
- Do not use when inputs are open-ended natural language or when the correct
  output cannot be expressed as a closed rule set.

## Structure
The step reads typed input, applies deterministic definition, business rules,
and transforms, then emits validated typed output. No semantic primitive
participates. Composition is a plain sequence or deterministic branch.

```mermaid
flowchart LR
  TRG --> INP --> DFN --> BRL --> XFM --> SCH --> OUT
```

## Primitives
- `TRG` — entry trigger for the step.
- `INP` — typed, validated input binding.
- `DFN` — deterministic definition/lookup.
- `BRL` — business-rule evaluation over a closed rule set.
- `XFM` — pure data transform.
- `SCH` — schema check on the produced value.
- `SEQ` / `DBR` — sequential and deterministic-branch composition.
- `OUT` — typed output binding.

## Authority allocation
| Authority | Holder |
|---|---|
| Control-flow | workflow |
| Decision | workflow (rules) |
| Action-authorisation | workflow |
| Execution | workflow |
| State | workflow |

## Invariants and rules
- INV-002 — the workflow is the authoritative state owner throughout.
- INV-003 — only accepted transitions occur; rules define the closed set.
- INV-005 — outcomes are distinguishable and typed.
- INV-016 / INV-017 — implementation-neutral and coded per the
  [classification model](../model/classification.md).
- DP-02 — deterministic baseline first; DP-07 — prefer closed sets.

## Coordinates
```yaml
nondeterminism: ND0
control_flow_authority: workflow
actor_topology: none
flow_shape: FS2
durability: DUR1
effect_level: EF2
assurance: AS2
impact: IM1
```

## Failure modes
- Rule gaps: an unmodeled input falls through the closed set.
- Silent drift when upstream schemas change without versioning.
- Over-application: forcing an inference-shaped problem into rigid rules.

## Consequences
- Benefits: maximal predictability, replayability, and lowest assurance cost.
- Benefits: cheapest to test and reason about.
- Costs: cannot absorb ambiguity; every new case needs an explicit rule.

## Example
In [invoice processing](../examples/invoice-processing/README.md), a
purchase-order match with clean, structured supplier data resolves entirely on
the deterministic path: `DFN`/`BRL` match line items and totals against the PO
and emit a coded outcome without ever invoking the model. This is the baseline
that the semantic patterns escalate from only when the PO match fails.
