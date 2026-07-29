# Agent-Directed Autonomous Maintenance Run — Rationale

Status: Design example

## Steps 1–3 — Outcome, baseline, and semantic work

The outcome and closed terminal outcomes remain those of the [base use case](use-case.md): for one maintenance objective, create exactly one PR for the same sandbox change that passed the deterministic gate, or record rejection, escalation, budget exhaustion, technical failure, or cancellation. The execution-history store remains the single authoritative workflow state owner (`INV-002`).

The deterministic baseline (`WP00`) still fixes the immutable envelope, fresh sandbox, tool/credential allow-list, effect ceiling, deterministic gate execution, digest matching, budget accounting, idempotency, reconciliation, and audit trail. The semantic requirement is intentionally larger than the `EP3` variant: the agent selects the *whole run sequence* — interpreting the objective, planning, diagnostics, edits, retries, waits, and proposed exit — toward the gate (`ND6`). Untrusted issue text, changelogs, source, and CI feedback cannot amend the envelope (`INV-018`).

## Step 4 — Profile and authority

By design directive, this selects [`EP4`](../../ra/04-profiles/ep4-agent-directed.md): the agent owns control-flow for the entire run, bounded by an external envelope. This is an explicit exception to [`DP-01`](../../ra/01-foundations/design-principles.md), not an assertion that more agency is normally preferable.

| Authority | Holder |
|---|---|
| Control-flow | Agent, within enforced envelope |
| Decision | Agent for next step and proposed disposition; human for escalations |
| Action authorisation | Independent policy gateway |
| Execution | Scoped sandbox gateway and PR-only adapter |
| State | Workflow execution-history store |

The independent policy gateway is crucial: agent direction does not become agent self-authorisation (`INV-007`, `INV-010`).

## Steps 5–6 — Patterns, overlays, and WDS

`WP09` supplies the fence; `WP04` gives the bounded repair/gate feedback loop; `WP08` makes state and waits durable; `WP00` supplies deterministic checks. `OV-02` protects effects, `OV-03` prevents duplicate/ambiguous writes, `OV-04` preserves CI waits, `OV-06` meters the entire agent-directed run, and `OV-07` records accepted transitions. `OV-01` / `WP07` are used for mandatory human escalation and post-run review, not PR approval. The [WDS](autonomous-maintenance-run-agent-directed.wera.yaml) targets `RT2` / `CL2`.

## Cost of EP4 compared with EP3

The [EP3 design](../autonomous-maintenance-run/solution.md) keeps deterministic workflow ownership of task admission, sequencing, CI wait handling, PR policy, and closure. It therefore has a narrow, inspectable point at which agent autonomy begins and ends. This EP4 design gives up that deterministic sequencing and decision coverage: the agent can choose what to examine next, when to retry, when to wait, and when to propose closure. It increases path variability, audit/review burden, risk of goal drift, and reliance on external envelope enforcement. It must not be presented as more conformant merely because it is more autonomous.

No invariant is waived: `INV-002` state ownership, `INV-003` accepted transitions, `INV-004`/`INV-005` run boundary/outcomes, `INV-006` authority allocation, `INV-007` protected-effect separation, `INV-010` constrained credentials, `INV-011` duplicate protection, and `INV-018` containment remain required. Instead, safeguards become **stricter**: immutable envelope digest; deny-by-default capability gateway; lower independent limits for tokens, steps, tools, time, and effects; checkpoint after every effect/gate transition; gate-result-to-change-digest matching; mandatory escalation on repeated failure, scope risk, or budget risk; post-run human review; and PR-only credentials. These compensate for lost workflow sequencing, but do not eliminate the trade-off.

## Alternatives rejected

`EP3` is the preferred least-agentic operational design, but violates the directive. `EP2` does not give the agent run control. Unenveloped `EP4` violates `DP-09` and is unsafe.
