# RA use-case validation — weekly staff schedule

**Reference Architecture:** [Bounded Autonomous Remediation](../architectures/bounded-autonomous-remediation.md)

**Use case:** Weekly staff schedule generation

**Evidence:** Working-session example; not yet included in the Critical Use Case
Inventory.

## Plain-language comparison

A small restaurant, salon, or shop needs the next week's employee schedule. The agent
reads employee availability, approved leave, qualifications, and informal preferences;
balances coverage and fairness; and generates a complete candidate schedule.

The workflow follows this loop:

`Generate → validate → repair → validate again → publish`

The **Schedule Acceptance Gate** evaluates these criteria:

- Every required shift is covered.
- Every assigned employee is available.
- Required roles and qualifications are present.
- No employee has overlapping shifts.
- Minimum rest periods are respected.
- Maximum weekly hours are respected.
- Approved time off is respected.
- Popular and unpopular shifts follow the agreed distribution rule.

The gate evaluates the complete schedule and passes only when all criteria are
satisfied for that same schedule (an AND condition). If any criterion fails, the
schedule is rejected.

The gate returns exact violations when a candidate fails. The agent uses that feedback
to generate another candidate. Only the exact passing schedule may be published.
Unresolved preference collisions, ambiguity, or failure to converge after the maximum
number of attempts escalates to the manager.

## Validation checks

| Check | If yes | If no | Current evidence |
|---|---|---|---|
| Is the task explicitly bounded before work starts? | Matches the RA's fixed task scope | Open-ended scheduling would not fit | **Yes** — one business, one week, known employees and shifts, declared availability, qualifications, leave, and scheduling rules |
| Can an independent deterministic gate evaluate the candidate? | Matches the RA's defining acceptance boundary | Agent self-acceptance or manager-only judgment would not fit | **Yes** — the gate checks all mandatory constraints and the declared popular/unpopular-shift distribution rule |
| Is the effect constrained, with a safe non-success route? | Matches exact-result execution and safe escalation | Unbounded attempts or unconstrained publication would not fit | **Yes** — only the exact passing schedule is published; unresolved preference collisions and exhausted attempts escalate to the manager |
