# AI Agent Instructions

Status: Mature

## Purpose

This is the entire instruction an AI agent needs to design a workflow with WERA. Everything else lives in the repository. The prompt is deliberately small — the reference architecture carries the knowledge, not the prompt.

## The prompt

```text
You are a workflow architect.

Read this repository. Follow the Workflow Design Method
(playbook/workflow-design-method.md).

Produce a Workflow Design Specification (a *.wera.yaml descriptor that validates
against descriptor/workflow-descriptor.schema.json) for the use case below.

Rules:
- Do not invent architectural concepts outside this repository.
- Use only codes present in descriptor/registry.yaml.
- Reuse existing patterns and profiles whenever possible.
- Prefer the least-agentic composition that satisfies the requirements (DP-01).
- If you must introduce a new concept, explain why existing concepts were
  insufficient.
- Reference cross-cutting concerns owned by other WGs as external boundaries
  (XB-##); do not redefine them.

Design workflow for:
<use case + requirements>
```

## What the agent should read, and in what order

1. [registry.yaml](../../descriptor/registry.yaml) — load the whole vocabulary as data.
2. [workflow-design-method.md](workflow-design-method.md) — the six steps to follow.
3. [selection-logic.yaml](../05-selection/selection-logic.yaml) — execute selection deterministically.
4. [workflow-descriptor.schema.json](../../descriptor/workflow-descriptor.schema.json) + [reference](../../descriptor/workflow-descriptor.reference.md) — the output contract.
5. [examples/](../../examples/README.md) — few-shot exemplars (use-case → rationale → solution + WDS).

## Expected output

A single valid `*.wera.yaml` descriptor with `intake`, `design`, and `recommendation` populated, plus a short natural-language summary that:

- states the deterministic baseline and the residual semantic task;
- names the chosen profile and patterns and why;
- lists the overlays and external boundaries triggered;
- states the readiness tier and conformance target;
- lists alternatives rejected.

## Self-check before returning

The agent SHOULD confirm, against the repository:

- every code used exists in [registry.yaml](../../descriptor/registry.yaml) ([INV-017][architecture-invariants]);
- the descriptor validates against the schema;
- all applicable [invariants][architecture-invariants] and [composition rules](../02-architecture-model/composition-rules.md) hold (target at least `CL1`);
- no cross-WG concern was redefined locally ([INV-015][architecture-invariants]);
- the least-agentic viable composition was chosen ([DP-01](../01-foundations/design-principles.md)).

## Why the prompt stays small

If an agent needs a large bespoke prompt to succeed, the *repository* is under-specified — that is a finding for the next iteration, per the [acceptance test](../../docs/acceptance-test.md), not a reason to grow the prompt.

<!-- link definitions -->
[architecture-invariants]: ../01-foundations/architecture-invariants.md
