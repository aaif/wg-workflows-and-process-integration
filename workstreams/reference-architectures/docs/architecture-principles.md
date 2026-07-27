# Architecture Principles

Status: Mature

## Why this document exists

These principles define the intended direction of the reference architecture. They are more stable than any individual diagram, pattern, or code, and they are the basis for reviewing future contributions. They are distinct from — and higher than — the [design principles](../foundations/design-principles.md) (`DP-##`, which guide day-to-day design choices) and the [architecture invariants](../foundations/architecture-invariants.md) (`INV-###`, which are testable rules).

## Principles

### 1. The workflow run is the central unit of execution

Architecture is organised around one coordinated execution toward an intended outcome, not around the number of agents involved or the framework used.

### 2. The full determinism spectrum is one architecture

Deterministic automation, model-assisted steps, hybrid workflows, bounded agentic regions, and multi-agent delegation are points on one spectrum, described with one set of concepts — not separate architectures.

### 3. Workflows own coordination

The workflow boundary owns accepted progress, pending work, completion, escalation, and recovery. An agent may reason or choose actions within a delegated boundary without silently becoming the entire business process.

### 4. Authority is explicit and separable

Control-flow, decision, action-authorisation, execution, and state authority may belong to different actors. They must not be collapsed into a vague statement that an actor is "in control."

### 5. State has an authoritative owner

A workflow run requires a system of record for accepted execution state. Model context, logs, traces, and conversation history may support execution but are not substitutes for authoritative workflow state.

### 6. Probabilistic output is a proposal until accepted

Model or agent output does not automatically become authoritative state. It must satisfy schema, policy, evidence, and authority boundaries before driving an accepted transition or effect.

### 7. Effects are protected

Externally visible actions are separated from reasoning and proposals. Their authorisation, execution, idempotency, and confirmation are explicit.

### 8. Humans are first-class workflow actors

Human review, approval, correction, and escalation are modelled as explicit tasks and state transitions, not as informal exceptions outside the architecture.

### 9. Dynamic behaviour remains bounded

Planning, delegation, and tool selection may be dynamic, but capability limits, budgets, allowed effects, exit states, and state ownership remain explicit.

### 10. Reliability semantics are designed, not assumed

Retries, replay, duplicate handling, reconciliation, timeouts, and compensation are defined in relation to state and effects.

### 11. The architecture is implementation-neutral

The model defines concepts, responsibilities, contracts, and observable behaviour. It does not require a particular workflow engine, model provider, agent framework, database, protocol, or cloud.

### 12. Cross-cutting concerns owned by other WGs are referenced, not redefined

Security, identity, observability, governance, and accuracy are the domains of other AAIF working groups. This architecture references them as **external boundaries** and does not restate their requirements as its own.

### 13. The vocabulary is coded and machine-readable

Every concept carries a stable code and is published as data, so both humans and AI agents can reason over the architecture consistently.

### 14. Patterns carry guarantees

A reusable pattern is valuable only when its invariants, authority boundaries, failure modes, and consequences are clear.

### 15. Examples drive maturity, and dual-mode usability is the test

Abstract concepts are validated through realistic worked examples. A section may remain intentionally incomplete until examples demonstrate what must be standardised. The measure of success is whether a human or an AI agent can produce a quality Workflow Design Specification from a new use case using only this repository. See [acceptance-test.md](acceptance-test.md).
