# Architecture Principles

## Purpose

These principles guide contributors and reviewers when they compose patterns, capability roles, and boundaries into a workflow reference architecture.

They are shared design guidance, not a prescription for a vendor, framework, deployment topology, or model provider. A concrete architecture should show how it applies them; a pattern should support them where relevant.

## 1. Design around practitioner jobs, not agent count

A reference architecture should describe a recognizable job and the guarantees it needs. “Single-agent” and “multi-agent” can be useful design characteristics, but they do not by themselves explain the job, risks, or required structure.

**In practice:** Name an architecture by the outcome or operational arrangement it serves, such as a human-approved operation or bounded autonomous remediation. Treat agent topology as a design decision inside that architecture.

## 2. Prefer the smallest safe amount of autonomy

Use deterministic workflow logic, explicit rules, validation, and policy where they provide the needed behaviour and guarantee. Add model or agent reasoning only where interpretation, judgment, or generation cannot be reliably expressed as rules. Give that reasoning no more authority than the job requires.

**In practice:** Keep admission, scope limits, policy checks, external effects, and terminal outcomes under workflow control. Let an agent interpret open-ended input or produce a candidate result, but do not make it own the whole run by default.

## 3. Make authority and external effects explicit

A workflow should make clear who may propose a result, decide whether it is acceptable, authorize an effect, execute that effect, and own the run state. Those roles may be implemented by one platform, but their responsibilities must remain understandable and enforceable.

**In practice:** An architecture should state what the agent may do and what remains workflow-controlled. Where an effect matters, identify the authority that permits it and the component that performs it.

## 4. Protect consequential effects structurally

A consequential external effect must not depend only on an agent following instructions. The architecture should use enforceable boundaries: a human or policy gate where needed, constrained credentials, a controlled executor, validation, idempotency or reconciliation, and recorded evidence.

**In practice:** An agent may prepare a proposal or candidate result, but it should not be able to bypass the path that authorizes and performs a protected effect.

## 5. Design for failure, recovery, and explicit outcomes

A workflow is not complete when its happy path works. It must define what happens when an input is invalid, a check fails, a process restarts, an event is duplicated or late, an effect result is uncertain, a budget is exhausted, or human intervention is needed.

**In practice:** List terminal outcomes and what is recorded for each. Where the run waits or has effects, explain how state, retries, reconciliation, timeout, stopping, or escalation remain safe.

## 6. Compose reusable patterns; do not duplicate their guarantees

A pattern owns the solution to one recurring problem, including its invariants and failure modes. A reference architecture composes patterns for a practitioner job and describes the new concerns that arise from their combination.

**In practice:** Link to the patterns used and explain where they sit in the architecture. Do not rewrite every pattern inside every architecture. Record only the composition-level risks, such as stale approval after a durable wait or a passing gate that is too weak for the permitted effect.

## 7. Keep requirements portable and implementation-neutral

The reference architecture should describe required behaviour and logical capability roles before product choices. Different runtimes may realize the same roles differently.

**In practice:** Say “durable state store,” “human interaction surface,” or “constrained effect executor,” rather than assuming a particular workflow engine, cloud provider, model host, or deployment topology. Product examples may illustrate an approach but must not become requirements.

## 8. Validate guidance against real scenarios

A scenario is evidence that an architecture fits—or does not fit—a real workflow. It is not automatically a generic reference architecture. No-fit and partial-fit results are valuable because they reveal missing patterns, variants, or new jobs.

**In practice:** Include at least one worked scenario and a validation record in each reference architecture. Keep the generic job, guarantees, and capability roles separate from the domain-specific details of the scenario.

## Applying the principles

When adding or reviewing a reference architecture, look for these principles in its routing checklist, structure, pattern composition, agent/workflow-control boundary, exit states, worked scenario, and validation record. If a principle does not apply, explain why rather than silently omitting it.
