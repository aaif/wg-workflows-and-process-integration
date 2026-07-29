# Autonomous Maintenance Run — Contracts and State

Status: Design example

## Key contracts

- **Maintenance-task contract** — immutable task ID/digest, repository/ref, allowed maintenance category, allowed paths/dependency boundaries, expected gate suite, and exclusion rules. Issue text is evidence only; it cannot widen this contract.
- **Region-boundary contract** — delegated goal, fresh-sandbox identity, tool allow-list, credential scopes, maximum effect level (`EF2`), result schema, and task/iteration/token/tool/time/effect budgets. It is the enforceable boundary for bounded delegation.
- **Sandbox change manifest** — changed paths, dependency lockfile changes, commands executed, commit/change digest, and provenance for each attempt. It is validated against the task contract before PR admission.
- **Deterministic gate result** — gate suite/version, input change digest, pass/fail disposition, timestamps, CI correlation, and evidence links. A pass is accepted only when it applies to the same final digest.
- **PR intent** — task digest + validated change digest + base/head refs + generated evidence summary + idempotency key. It authorises one PR creation only; it contains no merge/deploy instruction.
- **Escalation package** — contract, sandbox manifest(s), gate results, budget consumption, and reason (`over-scope`, repeated failure, or technical condition) for human follow-up.

## Authoritative state checkpoints

The execution-history store is the workflow’s single state owner (`OV-07`). `CHK` checkpoints let it resume safely across restarts and `WAI` CI waits.

| Checkpoint | Recorded state |
|---|---|
| Run opened | Trigger, task candidate, run ID, task-contract digest. |
| Admission decided | Eligibility/scope/duplicate evidence and accepted disposition. |
| Sandbox created | Fresh sandbox identity/generation and fenced capability grant. |
| Attempt completed | Iteration number, manifest digest, tool/audit references, budget consumed. |
| Gate correlated | Gate suite/version, requested change digest, CI correlation and wait state. |
| Gate adjudicated | Deterministic gate result and scope-manifest validation. |
| Region exited | Validated result, escalation reason, or exhausted budget dimension. |
| PR effect | Idempotency key, exact intent/change digest, confirmation or reconciliation evidence. |
| Terminal closure | One terminal outcome and retained review/audit links; sandbox discard status. |

## Consistency and version rule

A gate pass is usable only if its declared input digest equals the final sandbox change digest and its gate-suite version equals the task contract’s required gate version. Any edit after a pass invalidates that pass and requires a new gate run. Likewise, a PR may be created only for the exact validated change digest that its idempotency key binds. Replaying the run may reconcile the same PR intent, but may never create a second PR or promote a newer sandbox change under an older green result.

Sandbox destruction is compensation for partial local work: it removes the only editable workspace when the run rejects, escalates, fails budget, or is cancelled. It does not attempt to undo a PR; a confirmed PR is left for normal review/closure, while the workflow records its identity and outcome.
