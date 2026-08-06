# Gated Delivery Pipeline — Execution

## Stage semantics

1. **Intake and classify:** bind request and provenance; deterministic policy selects short or full track.
2. **Requirements:** a bounded worker proposes requirements; schema, scope, and per-language checks run before checkpointing.
3. **Design:** full-track runs produce a design artifact; short-track skips only the explicitly policy-approved stages.
4. **Build and review:** build/test and independent review fan out in parallel. `PAR` has a mandatory join; missing or failed branch evidence blocks the gate.
5. **QA:** per-language verification and integration checks validate the candidate.
6. **Human gate:** a named approver sees the exact artifact set and digest. Approve, reject, request change, timeout, and escalation are distinct outcomes.
7. **Deploy:** approval releases only the signed digest. An idempotency key protects retries; an ambiguous result enters reconciliation, not blind retry.
8. **Postcondition and retro:** verify the deployment. On failure, invoke rollback/compensation and record `COMPENSATED` or `FAILED_TECHNICAL`; then produce and store the retrospective.

Every stage checkpoints state and emits an artifact plus gate record. A changed artifact creates a new digest and invalidates downstream approvals. A restart replays accepted transitions from execution history rather than repeating effects.

## Failure endings

A rejected gate ends `REJECTED`; a request withdrawal ends `CANCELLED`; authority or policy gaps end `ESCALATED`; infrastructure failures end `FAILED_TECHNICAL`; a successful rollback ends `COMPENSATED`; only a verified deployment ends `COMPLETED`.
