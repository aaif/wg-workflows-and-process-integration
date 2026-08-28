# RA use-case validation — autonomous maintenance run

**Reference Architecture:** [Bounded Autonomous Remediation](../architectures/bounded-autonomous-remediation.md)

**Use case:** [Critical Use Case Inventory — Autonomous maintenance run ("night shift")](../../critical-use-cases/use-case-inventory.md#sdlc)

**Evidence:** The inventory says the agent handles small dependency bumps, lint/type
fixes, and specification/documentation drift in an isolated sandbox. Each candidate is
checked by deterministic CI/contract gates and the agent keeps iterating until the gate
passes. Repeated failures and changes larger than allowed are escalated. Preconditions
include meaningful CI, a fresh isolated environment per task, scoped write credentials,
and a token limit. The resulting effect is opening a pull request.

## Plain-language comparison

The RA is for one small, bounded problem that an agent may attempt repeatedly. The agent
does not decide whether its own result is acceptable. An independent deterministic gate
makes that decision. Only an accepted result can cause a narrow effect, and failed or
out-of-scope work stops or escalates.

The maintenance use case describes that same structure: one bounded maintenance change
is attempted in a sandbox, CI independently checks it, failed checks cause another
attempt, an accepted change becomes a pull request, and repeated or oversized work goes
to a person.

## Validation checks

| Check | If yes | If no | Current evidence |
|---|---|---|---|
| Is each maintenance problem bounded before work starts? | Matches the RA's fixed task scope | Open-ended work would not fit bounded remediation | **Yes** — the inventory calls these “small bounded” changes, requires a fresh isolated environment per task and scoped write credentials, and escalates changes that are too large |
| Does an independent deterministic gate decide whether the candidate is acceptable? | Matches the RA's defining separation between agent work and acceptance | If the agent accepts its own output, the RA's core safety boundary is absent | **Yes** — deterministic contract/evaluation checks and CI assess each candidate; the agent iterates until the gate is green |
| Is the effect constrained, with a safe route when work does not converge? | Matches the RA's protected exact-result effect and safe non-success boundary | Unbounded retries or stronger direct effects would not fit | **Yes** — the agent works in a sandbox, the accepted effect is opening a pull request, and repeated failure or out-of-scope work escalates |

## Result

`Validated`

**Why:** The inventory clearly shows the RA's main job and defining boundaries for each
maintenance item: bounded and isolated work, independent deterministic acceptance,
iteration on failure, a constrained pull-request effect, and escalation when work cannot
converge safely.

## Scope of this result

This validates architectural fit. The surrounding backlog workflow is additional
composition detail and does not negate the demonstrated fit of the bounded-remediation
job.

## Validation-record row

| Scenario | Source | Result | Notes |
|---|---|---|---|
| Autonomous maintenance run ("night shift") | Critical Use Case Inventory (SDLC) | Validated | Each maintenance task is bounded and isolated; deterministic CI/contract gates decide acceptance; only the accepted change becomes a pull request; repeated failure or oversized work escalates. |

## Reviewer decision

Review this point before accepting the result:

- Does the inventory evidence clearly establish the bounded per-task remediation job and
  its independent gate? The proposed answer is **Yes**; backlog orchestration is not a
  required fact for this architectural-fit result.
