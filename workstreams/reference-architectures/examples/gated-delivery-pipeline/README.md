# Gated Multi-Stage Delivery Pipeline

Status: Trial exemplar (descriptor-level)

## What this is

A schema-valid **Workflow Design Specification** produced to test WERA against a *new*
use case from the WG use-case landscape (SDLC category, "Gated multi-stage delivery
pipeline"). It is the **gated** end of a deliberate autonomy-spectrum pair; its twin is
the [autonomous maintenance run](../autonomous-maintenance-run/README.md). Same class of
work (an agent doing software delivery), opposite amount of human-in-the-loop.

A delivery request moves through ordered stages — requirements, design, build, review,
QA, sign-off, deploy, retro — producing a deployed change plus a per-stage artifact and
gate record. The workflow runs itself between gates but stops at defined authority
boundaries where a named human must sign off before the next stage proceeds.

This is a **trial exemplar**: it has a WDS but not yet the full
`use-case`/`rationale`/`solution` triad of a complete [worked example](../invoice-processing/README.md).

## The output

**[gated-delivery-pipeline.wera.yaml](gated-delivery-pipeline.wera.yaml)** — the
machine-readable WDS, validated against the
[schema](../../descriptor/workflow-descriptor.schema.json).

## At a glance

| Attribute | Value |
|---|---|
| Profile | [`EP1`](../../ra/04-profiles/ep1-workflow-directed.md) — workflow-directed |
| Primary pattern | [`WP07`](../../ra/03-patterns/wp07-human-supervised-action.md) — human-supervised action |
| Embedded patterns | `WP00`, [`WP01`](../../ra/03-patterns/wp01-bounded-model-step.md), `WP08` |
| Lifecycle envelope | [`WP08`](../../ra/03-patterns/wp08-durable-workflow-envelope.md) |
| Control-flow authority | `workflow` (the pipeline owns stage sequencing) |
| Assurance | `AS5` — multi-party sign-off at each authority boundary |
| Highest effect | `EF3` — a transactional deploy |
| Readiness / conformance | `RT3` / `CL3` |

## Why it is in the pair

Its distinctive coordinate is `control_flow_authority: workflow` with `AS5` (humans carry
assurance at every boundary). The
[autonomous run](../autonomous-maintenance-run/README.md) does the same class of work but
hands the run to the agent with `AS2` deterministic-gate assurance — **7 of 8 axes
differ**. See the [examples index](../README.md).
