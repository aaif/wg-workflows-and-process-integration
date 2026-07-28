# Autonomous Maintenance Run ("night shift")

Status: Trial exemplar (descriptor-level)

## What this is

A schema-valid **Workflow Design Specification** produced to test WERA against a *new*
use case from the WG use-case landscape (SDLC category, "Autonomous maintenance run"). It
is the **autonomous** end of a deliberate autonomy-spectrum pair; its twin is the
[gated delivery pipeline](../gated-delivery-pipeline/README.md). Same class of work
(software delivery by an agent), opposite amount of human-in-the-loop.

For each bounded maintenance task (dependency bump, lint/type fix, spec/doc drift), an
agent produces a change that makes a deterministic gate (CI + contract/eval checks) go
green in an isolated sandbox, then opens a pull request. The run never merges and never
touches production — a green gate plus an open PR is the success state.

This is a **trial exemplar**: it has a WDS but not yet the full
`use-case`/`rationale`/`solution` triad of a complete [worked example](../invoice-processing/README.md).

## The output

**[autonomous-maintenance-run.wera.yaml](autonomous-maintenance-run.wera.yaml)** — the
machine-readable WDS, validated against the
[schema](../../descriptor/workflow-descriptor.schema.json).

## At a glance

| Attribute | Value |
|---|---|
| Profile | [`EP4`](../../ra/04-profiles/ep4-agent-directed.md) — agent-directed under constraints |
| Primary pattern | [`WP09`](../../ra/03-patterns/wp09-bounded-agentic-region.md) — bounded agentic region |
| Embedded patterns | [`WP04`](../../ra/03-patterns/wp04-generate-validate-repair.md) (convergence loop), `WP00` |
| Lifecycle envelope | [`WP08`](../../ra/03-patterns/wp08-durable-workflow-envelope.md) |
| Control-flow authority | `agent` (bounded by an envelope) |
| Assurance | `AS2` — a deterministic gate is the sole arbiter |
| Highest effect | `EF2` — a pull request (reversible proposal); never a merge |
| Readiness / conformance | `RT2` / `CL2` |

## Why it is in the pair

Its distinctive coordinate is `control_flow_authority: agent` with `AS2` (a deterministic
gate carries assurance). The [gated pipeline](../gated-delivery-pipeline/README.md) does
the same class of work but keeps `control_flow_authority: workflow` with `AS5`
multi-party sign-off — **7 of 8 axes differ**. See the [examples index](../README.md).
