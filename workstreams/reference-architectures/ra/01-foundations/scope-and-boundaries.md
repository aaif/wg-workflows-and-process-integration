# Scope and Boundaries

Status: Mature

## What WERA covers

WERA is a vendor-neutral reference architecture for **workflow execution** across the full determinism spectrum:

- fully deterministic automation;
- deterministic workflows with model-assisted steps;
- hybrid workflows mixing rules and semantic judgement;
- workflows containing bounded agentic regions;
- multi-agent delegation within a workflow;
- workflows that hand off across agents or runtimes.

It covers the concepts, contracts, classification, patterns, profiles, controls, readiness, and a machine-readable descriptor needed to design and assess such workflows.

## Level of abstraction

WERA defines **concepts, responsibilities, contracts, and observable behaviour** at the component and relationship level. It does not prescribe a workflow engine, agent framework, model provider, database, protocol, or cloud, and it does not specify an agent's internal reasoning loop.

## What WERA deliberately does not own

Several concerns are essential to real workflows but are owned by **other AAIF working groups**. WERA references them as [external boundaries](../06-overlays/external-boundaries.md) (`XB-##`) and does not restate their requirements:

| Concern | Owning WG | WERA touch-point |
|---|---|---|
| Security, privacy, attack surface | Security & Privacy | `XB-01` |
| Agent identity, delegation, authorization | Identity & Trust | `XB-02` |
| Tracing, telemetry, debugging signals | Observability & Traceability | `XB-03` |
| Governance, risk, regulatory alignment | Governance, Risk & Regulatory | `XB-04` |
| Model reasoning quality and evaluation | Accuracy & Reliability | `XB-05` |

Note the deliberate distinction (charter Scope B): workflow-level **execution history / system of record** (accepted transitions, decision points, effect records) is **in scope** here, and is different from runtime **observability** signals (traces, metrics), which are the Observability WG's domain.

## Relationship to the charter

This workstream delivers against charter scope areas A–F and the four planned deliverables. The mapping is maintained in [charter-traceability.md](../../charter-traceability.md).

## In scope / out of scope summary

**In scope**

- workflow-run model, execution semantics, state and durability;
- primitives, patterns, profiles, composition rules;
- human-in-the-loop, waits, events, retries, reconciliation, compensation;
- portable workflow description and interchange (the descriptor);
- production readiness and conformance to this architecture.

**Out of scope**

- model training, LLM architecture, prompt-engineering methodology;
- the internal reasoning loop of an agent;
- the concerns owned by other WGs listed above (referenced, not defined).

## Open questions

- Where exactly is the boundary between a "bounded agentic region" and "multi-agent" for classification purposes? (see [classification](../02-architecture-model/classification.md))
- Which interchange guarantees must hold across runtimes? (see [descriptor](../../descriptor/README.md))
