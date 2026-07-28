# Execution Profiles

Status: Index

An **execution profile** (`EP#`) names a coherent whole-run arrangement of the five authorities and a characteristic region of the [classification coordinate](../02-architecture-model/classification.md). Where a [pattern](../03-patterns/README.md) is a reusable sub-solution, a profile describes how an *entire* workflow run is governed.

Profiles are the answer to "what kind of workflow is this, overall?" — replacing the old single-agent/multi-agent split with a spectrum of authority arrangements.

## The profiles

| Code | Profile | Control-flow authority | Typical topology | Status |
|---|---|---|---|---|
| [EP1](ep1-workflow-directed.md) | Workflow-directed | `workflow` | `none` | Mature |
| [EP2](ep2-workflow-directed-model-assisted.md) | Workflow-directed + model-assisted | `workflow` | `single_agent` | Mature |
| [EP3](ep3-bounded-agentic-region.md) | Workflow with bounded agentic region | `workflow` (delegated regions) | `bounded_agentic_region` | Proposal |
| [EP4](ep4-agent-directed.md) | Agent-directed under workflow constraints | `agent` (bounded) | `single_agent` / `multi_agent` | Proposal |
| [EP5](ep5-human-directed-continuation.md) | Human-directed continuation | `human` | any | Proposal |
| [EP6](ep6-event-directed-continuation.md) | Event-directed continuation | `event` | any | Proposal |
| [EP7](ep7-cross-runtime-handoff.md) | Cross-agent / cross-runtime handoff | `external_runtime` | `cross_runtime` | Proposal |

## Profile vs pattern

- A **profile** is chosen once per run (though a run may contain sub-regions in other profiles, e.g. an `EP2` run delegating to an `EP3` region).
- A **pattern** is applied as many times as needed within a run.

The [invoice example](../../examples/invoice-processing/README.md) is an `EP2` run (workflow-directed with a model-assisted recommendation step) that uses patterns `WP00`, `WP02`, `WP07`, wrapped in `WP08`.

## Profile document shape

Every profile eventually defines: intent, authority allocation across the five authorities, characteristic coordinate ranges, typical patterns and primitives, when to use / not use, failure modes, and an example. Proposal-level profiles give intent, authority sketch, and open questions.
