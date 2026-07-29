# Autonomous Maintenance Run — Rationale

Status: Design example

This is the six-step [Workflow Design Method](../../ra/08-lifecycle/workflow-design-method.md) applied to the [use case](use-case.md).

## Step 1 — Understand the business outcome

**Outcome:** for exactly one bounded maintenance task, produce an open pull request containing the exact change that passed the deterministic CI/contract gate in a fresh sandbox — or record why no PR was safely produced. The workflow never merges, deploys, or writes to authoritative repository state directly.

**Run boundary:** the run starts when a schedule selects one eligible triage-labelled issue or when one eligible issue is directly submitted. It finishes in exactly one of `COMPLETED` (PR opened), `REJECTED` (ineligible or duplicate task), `ESCALATED` (over-scope or repeated non-convergence), `FAILED_BUDGET`, `FAILED_TECHNICAL`, or `CANCELLED` ([INV-004](../../ra/01-foundations/architecture-invariants.md), [INV-005](../../ra/01-foundations/architecture-invariants.md)).

**System of record:** the workflow execution-history store records accepted transitions and links task, sandbox, gate, change, and PR identities; it does not replace the Git host or CI as their authoritative records ([INV-002](../../ra/01-foundations/architecture-invariants.md)).

## Step 2 — Identify the deterministic baseline

The least-agentic path is substantial: schedule and select **one** task; verify its label, scope declaration, repository identity, and duplicate status; create a fresh sandbox; enforce a tool and credential allow-list; execute CI and contract/evaluation checks; interpret their deterministic pass/fail result; meter attempts, tokens, tool calls, and wall-clock time; validate the final scope manifest; construct the PR intent; create it idempotently; reconcile uncertainty; and record a terminal disposition.

This is the part done by plain rules, no model ([`WP00`](../../ra/03-patterns/wp00-deterministic-baseline.md), the Deterministic Baseline). It retains task admission, success adjudication, PR admission, and lifecycle control.

## Step 3 — Identify semantic gaps

The irreducible semantic work is not “maintain the repository” in the open. It is the smallest useful task: **within an admitted task contract, choose the next allowed diagnostic, edit, or gate invocation in response to current code and gate feedback.** Dependency and source drift cannot be exhaustively mapped to a fixed repair sequence.

That is local planning (`ND6`) and tool selection in a bounded region, not a whole-run open goal. Issue text, changelogs, CI logs, and repository content remain untrusted; they are data and feedback, never instructions that can widen the task or tool contract ([INV-018](../../ra/01-foundations/architecture-invariants.md)). The CI/contract gate is the sole deterministic success arbiter. The run is long-lived and must resume after restarts and CI waits (`DUR4`). Sandbox edits and opening a PR are reversible writes (`EF2`); wrong changes are material but correctable (`IM2`), and deterministic postcondition checks give `AS2` assurance.

## Step 4 — Choose the execution profile

The workflow keeps whole-run coordination, state, task selection, PR policy, and closure. It lends local control-flow to the agent only after a declared goal is delegated and receives a result back. This is [`EP3`](../../ra/04-profiles/ep3-bounded-agentic-region.md), a workflow with a bounded agentic region — the least-agentic profile that permits dynamic repairs.

| Authority | Holder |
|---|---|
| Control-flow | Workflow runtime overall; agent only inside the delegated sandbox region |
| Decision | Agent selects local repair steps; deterministic scope/gate/PR policy decides admission and outcome; human decides escalations |
| Action-authorisation | Workflow policy and the predeclared region contract |
| Execution | Ephemeral sandbox tool gateway; separate constrained Git-host PR adapter |
| State | Workflow execution-history store |

The agent cannot choose tasks, grant itself a wider effect, merge, deploy, or become the authoritative state holder ([INV-006](../../ra/01-foundations/architecture-invariants.md), [INV-008](../../ra/01-foundations/architecture-invariants.md), [INV-010](../../ra/01-foundations/architecture-invariants.md)).

## Step 5 — Apply patterns and overlays

- Primary: [`WP09`](../../ra/03-patterns/wp09-bounded-agentic-region.md), the bounded agentic region. Its entry contract fixes one goal, fresh sandbox, allow-listed capabilities, effect ceiling, result schema, and budgets.
- Embedded: [`WP00`](../../ra/03-patterns/wp00-deterministic-baseline.md) supplies policy, gate, and lifecycle logic. [`WP04`](../../ra/03-patterns/wp04-generate-validate-repair.md) shapes the repair → gate → feedback loop and forces a bounded exit.
- Envelope: [`WP08`](../../ra/03-patterns/wp08-durable-workflow-envelope.md) persists checkpoints across restarts and CI waits.
- Overlays: `OV-02` protects both reversible effects; `OV-03` gives idempotency and reconciliation for ambiguous writes; `OV-04` makes CI waits durable; `OV-06` bounds the dynamic region; `OV-07` makes execution history authoritative.
- External boundaries: `XB-01` security/privacy, `XB-02` identity/delegation, `XB-03` observability signals, `XB-04` governance/risk, and `XB-05` gate/evaluation quality are referenced as external concerns, not redefined ([INV-015](../../ra/01-foundations/architecture-invariants.md)).

## Step 6 — Produce the WDS

The resulting [WDS](autonomous-maintenance-run.wera.yaml) selects `EP3` / `WP09`, embeds `WP00` and `WP04`, sets `RT2` readiness and `CL2` conformance target, and declares the protected sandbox-edit and PR-creation effects. It validates against the descriptor schema.

## Alternatives rejected

- `EP2` with `WP04` alone cannot express the agent’s dynamic choice of diagnostic and edit tools.
- `EP4` makes the agent the whole-run director, unnecessarily giving up deterministic task intake, durable waits, PR admission, and closure.
- A human-approval gate before each PR conflicts with the stated autonomous-PR objective; humans receive escalations for over-scope and non-convergent work instead.
- Merge/deploy controls are intentionally absent because those effects are out of scope.
