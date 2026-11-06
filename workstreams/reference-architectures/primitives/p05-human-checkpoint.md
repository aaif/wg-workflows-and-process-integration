# P5 HumanCheckpoint

**Obligation:** MUST \
**Used in patterns:** [Human approval gate](../patterns/human-approval-gate.md) · [Proposal/execution split](../patterns/proposal-execution-split.md)

## Definition

A point where the workflow pauses, durably, until a person makes a decision.

## Why it exists

If the pause has no name in the workflow, "human in the loop" turns into a
side channel. It can't be resumed or audited, and from the outside it looks
the same as a stalled run. When a human decision is required, only a pause
that lives in the workflow's own state can show it happened. Which actions
need one under a given regulation is for the Governance, Risk & Regulatory
Alignment WG to say.

## How the patterns use it

- **Human approval gate.** This is the primitive the gate is built on. The
  checkpoint shows the exact proposal version the decision will apply to,
  accepts only explicit *approve*, *reject*, or *escalate* from a named and
  authorized person, records the decision before the run resumes (`P9`,
  `P12`), and ignores duplicate decision events. It always has a
  `P6 TimerDeadline`, and silence, timeout, or delivery failure never counts as
  approval.
- **Proposal/execution split.** When the authorization authority is a person,
  `P5` is that authority. When it's a versioned policy, no primitive covers it
  yet (see open questions).

After the decision: approval goes to the executor (`P2`), rejection stops the
run or sends the proposal back with feedback (`P3`), and escalation or an
expired deadline goes to `P8 Escalation`.

## Implementation approaches (illustrative, not requirements)

| Runtime | Construct | Notes |
| --- | --- | --- |
| BPMN 2.0 | User task + gateway | Engines such as Camunda support assignees and candidate groups |
| n8n | `sendAndWait` operation | |
| AWS Step Functions | `.waitForTaskToken` | The task token has to be protected and correlated |
| Temporal | Signal | Race it against a durable timer for the deadline |
| LangGraph | `interrupt()` | Waits indefinitely unless the application adds a timeout |

Each of these can host the pause. None of them alone checks approver identity,
binds the decision to a proposal version, deduplicates events, and writes the
audit record. The [human approval gate](../patterns/human-approval-gate.md)
pattern lists what you add for each.

## Relationship to other primitives

- [P3 AgentTask](p03-agent-task.md): produces the proposal and gets the
  feedback on re-entry.
- [P6 TimerDeadline](p06-timer-deadline.md): sets the decision deadline.
- [P8 Escalation](p08-escalation.md): handles escalation and expired deadlines.
- [P9 StateCommit](p09-state-commit.md): holds the parked run and the recorded
  decision.
- [P12 AuditRecord](p12-audit-record.md): who decided, on which version, and
  when.

## Open questions

- Policy authorization (a versioned rule set deciding instead of a person) has
  no primitive. Is it a variant of `P5`, or does it need its own?
