# Gated Delivery Pipeline — Sequence

1. The request enters the workflow and receives a run ID, source snapshot, policy version, and provenance record.
2. Rules classify the change and select the short or full track.
3. Requirements are produced and validated; the workflow checkpoints them and waits for the named approver.
4. The approver approves or rejects the exact requirements digest. Rejection, timeout, escalation, cancellation, and approval are recorded separately.
5. On the full track, design is produced and validated. Build and review then run in parallel from the same source/design snapshot; their outputs join into one candidate package.
6. QA runs per-language checks and verifies the joined package. The workflow checkpoints the release-candidate digest and waits for deployment approval.
7. The named approver approves that exact digest. If any artifact changes, the digest changes and the approval is invalid; the workflow returns to the affected gate.
8. The adapter deploys with an idempotency key and constrained credentials. The workflow verifies the postcondition.
9. A failed postcondition triggers rollback/compensation. An ambiguous adapter response triggers reconciliation. The workflow records the final outcome, stores the retrospective, and closes the run.
