# Gated Delivery Pipeline — Contracts and State

## Artifact contract

Each stage emits `{run_id, stage_id, track, source_digest, artifact_digest, schema_version, producer, evidence_refs, created_at}`. Artifacts are immutable; a revision receives a new digest.

## Gate record contract

A gate record contains `{run_id, gate_id, artifact_digest, policy_version, approver_id, decision, reason, decided_at}`. Valid decisions are explicit: `APPROVED`, `REJECTED`, `REQUESTED_CHANGE`, `ESCALATED`, `TIMED_OUT`, or `CANCELLED`. `APPROVED` is valid only when it matches the current artifact digest and the approver is authorised by consumed policy.

## Run state

The authoritative state store records request, selected track, current stage, artifact references, gate records, branch statuses, current release-candidate digest, deployment idempotency key, deployment identity, postcondition, compensation status, and terminal outcome. `EVH` is the replayable history of accepted transitions.

## Protected deployment

The deployment effect uses `run-id + release-candidate-digest + target-environment` as its idempotency key. The adapter returns an external deployment identity and version. The workflow confirms the identity and verifies a postcondition. Unknown results are reconciled against the deployment system before any retry. Rollback is a distinct compensating effect and is recorded with its own evidence.

## Invalidation and retention

Any source, artifact, policy, or configuration change after approval creates a new digest and invalidates affected approvals. Gate and deployment records remain linked to the version they describe, allowing replay and audit without treating the history store as a copy of the repository or deployment system.
