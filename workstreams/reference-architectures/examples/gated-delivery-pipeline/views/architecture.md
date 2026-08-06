# Gated Delivery Pipeline — Architecture

## Architectural position

This is `EP2` (workflow-directed + model-assisted): the durable workflow runtime owns control-flow, while bounded model steps assist specialists. It is not `EP4` (agent-directed); agents never decide what runs next or authorise an effect.

## Scope

**In scope:** request intake, short/full track selection, ordered requirements/design/build/review/QA stages, build/review fan-out and join, per-language verification, exact-version human gates, signed deployment, postcondition verification, rollback, retrospective, and replayable history.

**Out of scope:** defining organisational approval policy, choosing a model host or CI/CD product, autonomous merge/deploy, or allowing an agent to bypass a gate.

## Responsibilities

| Actor | Responsibility | Limit |
|---|---|---|
| Workflow runtime | Drives fixed stages, branches, joins, waits, and terminal outcomes | Never delegates control-flow or approval |
| Specialist model workers | Propose bounded stage artifacts | Cannot call deployment or approve |
| Deterministic validators | Run schemas, tests, language checks, digest and policy checks | Reject/escalate rather than guess |
| Human approver | Approve/reject the exact artifact digest | Cannot approve a different version |
| Build/review adapters | Produce and verify artifacts | Scoped to the stage contract |
| Deployment adapter | Deploy approved digest and report postcondition | Constrained credentials; idempotent; rollback capable |
| State/history store | Own authoritative run state and audit history | Links to external artifacts; does not become a shadow repository |

## Logical flow

The request is classified deterministically, then passes fixed stage gates. Build and review run in parallel only after their shared inputs are checkpointed; a deterministic join prevents either branch from skipping the gate. Deployment is a protected transactional effect released only by approval of the exact release-candidate digest.
