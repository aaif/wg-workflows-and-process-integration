# Architecture Invariants

Status: Mature

Invariants (`INV-###`) are rules a conforming workflow MUST or MUST NOT violate, regardless of technology or domain. They use RFC 2119 language (MUST, MUST NOT, SHOULD, MAY). Conformance to invariants is the basis of the [`CL1` conformance level](../07-readiness/conformance.md).

Invariants are testable; where an invariant can be checked against a [descriptor](../../descriptor/README.md), the check is noted.

## Run and state

### INV-001 — Declared nondeterminism

Every nondeterministic step MUST declare its purpose, input contract, output contract, allowed authority, data classification, timeout, failure behaviour, and evaluation method.

### INV-002 — Authoritative state owner

Every workflow run MUST have exactly one authoritative system of record for accepted execution state. Model context, logs, and traces MUST NOT be the sole record of completed work, approved effects, or pending obligations.

### INV-003 — Accepted transitions only

Authoritative state MUST change only through an accepted transition. Validation, policy, authority, and effect controls MUST occur before or as part of that commit.

### INV-004 — Run boundary is explicit

Every run MUST declare its boundary (start condition and the set of terminal outcomes). A run MUST NOT be defined implicitly by a single request, model call, or message.

### INV-005 — Distinguishable outcomes

Technical completion MUST be distinguishable from business disposition. Terminal outcomes MUST be drawn from the closed set in [classification](../02-architecture-model/classification.md).

## Authority

### INV-006 — Five authorities allocated

For every consequential step, all five authorities (control-flow, decision, action-authorisation, execution, state) MUST be allocable to a named holder. They MUST NOT be collapsed into an unspecified "in control."

### INV-007 — No self-authorised protected effects

An actor that proposes a protected effect MUST NOT also be the sole authoriser of that effect. An agent MUST NOT approve its own proposal.

### INV-008 — Bounded delegation

A delegated goal or agentic region MUST declare allowed tools, allowed data, maximum effect level, budgets, exit states, and state owner before execution.

## Effects

### INV-009 — Proposals are not effects

Reasoning or recommendation MUST NOT directly cause an externally visible action. An effect MUST pass through explicit validation, authorisation, controlled execution, and confirmation.

### INV-010 — Constrained execution credentials

The component that proposes an effect MUST NOT hold unrestricted credentials to the target system. Execution MUST use least-privilege, effect-scoped credentials.

### INV-011 — Duplicate protection

Every effect at level `EF2` or higher MUST define idempotency or equivalent duplicate protection. An ambiguous execution result MUST lead to reconciliation, not blind retry.

### INV-012 — Versioned, digest-linked effects

An effect payload MUST be explicit and versioned, and its target-system confirmation MUST be linked to the workflow run.

## Humans and approval

### INV-013 — Approval binds to an exact version

A human approval MUST refer to an immutable version or digest of the reviewed artifact or action. A material change MUST invalidate prior approval. Approval MUST NOT be interpreted as authority beyond the reviewed action.

### INV-014 — Explicit approval outcomes

Approve, reject, request-change, and timeout MUST all be explicit, recorded outcomes. An approval timeout MUST NOT leave a run indefinitely ambiguous.

## Boundaries and neutrality

### INV-015 — Cross-WG concerns referenced, not redefined

A workflow MUST reference cross-cutting concerns owned by other WGs through an [external boundary](../06-overlays/external-boundaries.md) and MUST NOT restate or fork their requirements as WERA-owned content.

### INV-016 — Implementation neutrality

Normative content MUST NOT require a specific engine, framework, provider, database, protocol, or cloud. Product mappings MAY be provided as non-normative examples.

### INV-017 — Coded and machine-readable

Every WERA concept a workflow relies on MUST have a stable code present in the [registry](../../descriptor/registry.yaml). A workflow's design SHOULD be expressible as a schema-valid descriptor.

### INV-018 — Untrusted input is contained

Content from untrusted sources MUST be treated as data, not instructions, and MUST pass input controls before it can influence a decision or effect. (Deep treatment is a Security-WG concern referenced via `XB-01`.)
