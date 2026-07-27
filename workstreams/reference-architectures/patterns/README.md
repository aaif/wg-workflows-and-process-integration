# Pattern Catalogue

Status: Index

A **pattern** (`WP##`) is a reusable sub-solution to a recurring workflow problem, with clear invariants, authority boundaries, failure modes, and consequences ([architecture principle 14](../docs/architecture-principles.md)). Patterns are ordered along the determinism spectrum, from fully deterministic (`WP00`) to cross-runtime (`WP11`).

A pattern is **not** the same as a [profile](../profiles/README.md): a profile describes a whole-run authority arrangement; a pattern is a building-block composition you drop into a run.

## The catalogue

| Code | Pattern | Spectrum position | Status |
|---|---|---|---|
| [WP00](wp00-deterministic-baseline.md) | Deterministic Baseline | No nondeterminism (`ND0`) | Mature |
| [WP01](wp01-bounded-model-step.md) | Bounded Model Step | Content/label (`ND1`–`ND2`) | Mature |
| [WP02](wp02-recommend-adjudicate.md) | Recommend + Deterministic Adjudication | Selection (`ND3`) | Mature |
| [WP03](wp03-model-selected-branch.md) | Model-Selected Deterministic Branch | Branch (`ND4`) | Proposal |
| [WP04](wp04-generate-validate-repair.md) | Generate–Validate–Repair | Content (`ND1`) | Proposal |
| [WP05](wp05-bounded-plan-execute.md) | Bounded Plan + Deterministic Execute | Plan (`ND6`) | Proposal |
| [WP06](wp06-model-assisted-exception.md) | Model-Assisted Exception Handling | Exception-only (`FS6`) | Proposal |
| [WP07](wp07-human-supervised-action.md) | Human-Supervised Action | Any + `APR` | Mature |
| [WP08](wp08-durable-workflow-envelope.md) | Durable Workflow Envelope | Durability (`DUR2`+) | Mature |
| [WP09](wp09-bounded-agentic-region.md) | Bounded Agentic Region | Tool/plan (`ND5`–`ND6`) | Proposal |
| [WP10](wp10-multi-agent-delegation.md) | Multi-Agent Delegation | Delegation (`ND7`) | Proposal |
| [WP11](wp11-cross-runtime-handoff.md) | Cross-Runtime Handoff | `cross_runtime` topology | Proposal |

## How patterns compose

`WP08` (Durable Workflow Envelope) commonly *wraps* another pattern to give it durability and recovery. `WP07` (Human-Supervised Action) commonly *gates* a protected effect produced by `WP02` or `WP09`. The [invoice example](../examples/invoice-processing/README.md) combines `WP00` + `WP02` + `WP07` inside a `WP08` envelope.

## Pattern document shape

Every pattern eventually defines: problem, context/forces, structure (primitives + flow), invariants referenced, authority allocation, failure modes, consequences, and an example. Proposal-level patterns state the problem and candidate structure with open questions.
