# Agent-Directed Maintenance Run — Contracts and State

## Contracts

- **Immutable objective envelope:** task/objective digest, repository/ref, scope/path/dependency boundaries, allowed tools, required gate suite/version, effect ceiling, budgets, escalation conditions, terminal outcomes. Untrusted text cannot alter it.
- **Agent action request:** selected action plus current state/checkpoint and requested capability. It is a request, not authority.
- **Gate evidence:** suite/version, input change digest, pass/fail, CI correlation, timestamps, and evidence references.
- **Effect intent:** exact sandbox edit or PR payload, envelope/change digest, idempotency key, and policy decision.
- **Escalation package:** objective envelope, action history, manifests, gate evidence, budget consumption, and reason.

## State checkpoints

`OV-07` execution history is authoritative; agent memory is disposable.

| Checkpoint | Required record |
|---|---|
| Envelope accepted | Digest, capabilities, ceilings, terminal set, sandbox generation. |
| Action proposed | Agent-selected action and causally prior evidence. |
| Capability/effect decision | Gateway/policy allow or deny decision, scope/budget evidence. |
| Gate/wait | CI correlation, durable wait state, returned result and input digest. |
| Effect confirmation | Idempotency key, target identity, confirmation or reconciliation. |
| Escalation / closure | Reason, human package, one terminal outcome, sandbox discard state. |

## Consistency rule

Only a gate pass for the identical final change digest and required gate-suite version can support the PR intent. Any edit invalidates prior green evidence. A PR intent binds that digest and may be reconciled on replay, never duplicated. The envelope’s budgets are monotonically consumed in authoritative state; agent-provided counters are advisory only.
