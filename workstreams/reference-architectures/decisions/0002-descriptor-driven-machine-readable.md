# ADR 0002: Descriptor-Driven, Machine-Readable WDS

## Status

Proposed

## Date

2026-07-27

## Context

The repository must serve two consumers — a human architect and an AI agent — who should reach the **same** Workflow Design Specification. Prose alone cannot be validated, diffed, or executed by a tool, and it makes the [acceptance test](../docs/acceptance-test.md) hard to run objectively.

## Options considered

- **Prose-only RA** — readable, but not checkable or comparable; AI output drifts.
- **Descriptor-driven RA** — the WDS is a machine-readable `*.wera.yaml` descriptor with a JSON Schema, and the vocabulary is published as data (`registry.yaml`).

## Decision

Make the **descriptor the primary output artifact**. The coded vocabulary is published as machine-readable data; the design is captured as a schema-valid descriptor; selection logic is encoded so an agent can execute it.

## Rationale

Authoring, conformance checking (`CL0`–`CL1`), and comparison of two WDS artifacts all become mechanical. A tiny AI prompt suffices because the knowledge lives in the repository, not the prompt. This directly enables the dual-mode acceptance test.

## Consequences

Every concept must carry a stable code and appear in [registry.yaml](../descriptor/registry.yaml) ([INV-017](../foundations/architecture-invariants.md)). Headings must avoid embedding codes to keep anchors stable. A schema-validation step joins the quality gate.

## Follow-up

Decide how strictly conformance tooling should enforce composition rules vs surface them as warnings.
