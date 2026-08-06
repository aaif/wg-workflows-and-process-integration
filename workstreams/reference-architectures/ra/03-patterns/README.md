# Pattern Catalogue

Status: Index

A **pattern** (`WP##`) is a reusable sub-solution to a recurring workflow problem, with clear invariants, authority boundaries, failure modes, and consequences ([architecture principle 14](../../docs/architecture-principles.md)). Patterns are ordered along the determinism spectrum, from fully deterministic (`WP00`) to cross-runtime (`WP11`).

A pattern is **not** the same as a [profile](../04-profiles/README.md): a profile describes a whole-run authority arrangement; a pattern is a building-block composition you drop into a run.

## The catalogue

Each row carries a stable anchor (e.g. `#wp09`) so other documents can facade-link to a
pattern through this catalogue rather than deep-linking its file directly.

| Code | Pattern | Spectrum position | Status |
|---|---|---|---|
| <a id="wp00"></a>[WP00](wp00-deterministic-baseline.md) | Deterministic Baseline | No nondeterminism (`ND0`) | Mature |
| <a id="wp01"></a>[WP01](wp01-bounded-model-step.md) | Bounded Model Step | Content/label (`ND1`–`ND2`) | Mature |
| <a id="wp02"></a>[WP02](wp02-recommend-adjudicate.md) | Recommend + Deterministic Adjudication | Selection (`ND3`) | Mature |
| <a id="wp03"></a>[WP03](wp03-model-selected-branch.md) | Model-Selected Deterministic Branch | Branch (`ND4`) | Proposal |
| <a id="wp04"></a>[WP04](wp04-generate-validate-repair.md) | Generate–Validate–Repair | Content (`ND1`) | Proposal |
| <a id="wp05"></a>[WP05](wp05-bounded-plan-execute.md) | Bounded Plan + Deterministic Execute | Plan (`ND6`) | Proposal |
| <a id="wp06"></a>[WP06](wp06-model-assisted-exception.md) | Model-Assisted Exception Handling | Exception-only (`FS6`) | Proposal |
| <a id="wp07"></a>[WP07](wp07-human-supervised-action.md) | Human-Supervised Action | Any + `APR` | Mature |
| <a id="wp08"></a>[WP08](wp08-durable-workflow-envelope.md) | Durable Workflow Envelope | Durability (`DUR2`+) | Mature |
| <a id="wp09"></a>[WP09](wp09-bounded-agentic-region.md) | Bounded Agentic Region | Tool/plan (`ND5`–`ND6`) | Proposal |
| <a id="wp10"></a>[WP10](wp10-multi-agent-delegation.md) | Multi-Agent Delegation | Delegation (`ND7`) | Proposal |
| <a id="wp11"></a>[WP11](wp11-cross-runtime-handoff.md) | Cross-Runtime Handoff | `cross_runtime` topology | Proposal |

## How patterns compose

`WP08` (Durable Workflow Envelope) commonly *wraps* another pattern to give it durability and recovery. `WP07` (Human-Supervised Action) commonly *gates* a protected effect produced by `WP02` or `WP09`. The [invoice example](../../examples/invoice-processing/README.md) combines `WP00` + `WP02` + `WP07` inside a `WP08` envelope.

## Pattern document shape

Every pattern eventually defines: problem, context/forces, structure (primitives + flow), invariants referenced, authority allocation, failure modes, consequences, and an example. Proposal-level patterns state the problem and candidate structure with open questions.
