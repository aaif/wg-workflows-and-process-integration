# Roadmap

Status: Proposal

The repository evolves through **examples**, not by completing every abstract section up front. A section stays a labelled Proposal until a worked example forces it to be nailed down.

## Current snapshot: descriptor-driven, invoice-anchored

**Mature in this snapshot**

- architecture principles, design principles (`DP-##`), invariants (`INV-###`);
- core concepts: workflow run, five authorities, state, effects, actor topology;
- classification (the eight coordinate axes) and primitive catalog;
- patterns needed by the example: `WP00`, `WP01`, `WP02`, `WP07`, `WP08`;
- profiles `EP1`, `EP2`;
- overlays `OV-01` (human approval), `OV-02` (protected effect), `OV-07` (execution history);
- the machine-readable descriptor: schema, registry, and the invoice `*.wera.yaml`;
- the Workflow Design Method and AI-agent instructions;
- the invoice-processing worked example (also a few-shot exemplar).

**Proposal-level only**

- reliability semantics breadth; `OV-03` reconciliation, `OV-04` durable wait, `OV-05` compensation, `OV-06` budgets;
- patterns `WP03`–`WP06`, `WP09`–`WP11`;
- profiles `EP3`–`EP7`;
- full runtime-component and composition-rule catalogues;
- required-views catalogue (`VW-##`).

## The acceptance test drives every iteration

Each iteration is judged by [the acceptance test](docs/acceptance-test.md): can a human or an AI produce a quality WDS for a **new** use case using only this repository? Gaps found there — not page count — set the next priorities.

## Suggested next iterations

1. Add a **multi-source activity-summary** example to mature fan-out, aggregation, completeness, and partial-result handling (`WP04`, parallel joins).
2. Add a **bounded agentic investigation** example to mature planning, delegation, control transfer, and budgets (`WP09`, `EP3`/`EP4`, `OV-06`).
3. Add a **cross-runtime handoff** example to mature `WP11`/`EP7` and the interoperability contracts in the descriptor.
4. Run the acceptance test with an external reviewer + an AI agent; promote whichever Proposal documents the exercise proves necessary.
