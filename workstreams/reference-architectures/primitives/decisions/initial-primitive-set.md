# Introduce an Initial Set of Workflow Primitives

## Date

2026-11-12

## Status

Proposed for working group review. Not yet adopted.

## Context

The patterns in this workstream describe their solutions in terms of building
blocks (a proposer, an executor, a durable wait, a deadline, a gate) without a
shared name for each one. The same block shows up in several patterns under
different wording, and a reader has no single place to see what it is or how
runtimes implement it. The single-agent human-approval architecture also noted
that "the workflow-level building blocks a definition is written in" were a
separate list that hadn't been written yet.

## Decision

Add a primitive layer under `primitives/` with 12 primitives, numbered `P1` to
`P12`. A primitive is included only if at least one existing pattern needs it.
Primitives map to patterns, and architectures reach them through the patterns
they compose.

## Why each one is required

| Primitive | Pattern that needs it | What breaks without it |
| --- | --- | --- |
| P1 Trigger | Proposal/execution split, Durable wait | No single run identity, so redelivered requests start duplicate runs and wake-up events can't find their run |
| P2 DeterministicFunction | Proposal/execution split, Deterministic acceptance gate | The executor and the gate checks get folded into the agent |
| P3 AgentFunction | Proposal/execution split, Bounded convergence loop | Agent work has no contract, so there's nowhere to enforce scope, budget, or termination |
| P4 ToolCall | Proposal/execution split, Bounded convergence loop | Nothing to attach the tool allowlist and effect class to |
| P5 HumanCheckpoint | Human approval gate, Proposal/execution split | Human decisions happen in a side channel that can't be resumed or audited |
| P6 TimerDeadline | Human approval gate, Durable wait | Waits never end and nobody notices |
| P7 ErrorBoundary | Proposal/execution split, Bounded convergence loop, Deterministic acceptance gate | Retries drift into the agent, and a failed gate can be read as a pass |
| P8 Escalation | Human approval gate, Bounded convergence loop | Escalation collapses into error handling or a routine review |
| P9 StateCommit | Durable wait, Human approval gate, Bounded convergence loop | A crash loses parked runs, decision evidence, or the attempt count |
| P10 Budget | Bounded convergence loop | Agent loops end only when someone notices the bill |
| P11 OutcomeContract | Bounded convergence loop, Human approval gate | Rejections, expiries, and failures all look the same, so retries go wrong |
| P12 AuditRecord | Proposal/execution split, Human approval gate, Bounded convergence loop, Deterministic acceptance gate | Nothing can show who authorized what and what ran |

## Rationale

Tying each primitive to a pattern keeps the set small and stops primitives
being added because they seem useful in general. Patterns are already where
the workstream records invariants and failure modes, so a primitive only needs
to say what the block is and how runtimes implement it.

The two primitives that do the work are called *functions*: `P2
DeterministicFunction` and `P3 AgentFunction`. The repository already uses
the other candidate words for something else. A *business task* is the request
a workflow run handles, and the run handles it through *activities*, which can
contain several primitives. PRs #31, #32, and #33 replaced "step" with
"activity". A function is the unit inside an activity that does the work,
either with fixed code or with an agent. Like any function, it takes a
defined input and returns a result; the deterministic one always returns the
same result for the same input, and the agent one may not. It maps to a
Temporal activity, an n8n node, a BPMN service task, or a Step Functions task
state.

IDs are contiguous. Once the WG accepts the set, an ID is never renumbered or
reused, and new primitives take the next free number.

## Consequences

- Each primitive file lists the patterns that use it and maps the primitive
  to constructs in BPMN 2.0, n8n, AWS Step Functions, Temporal, and LangGraph.
- Each pattern lists the primitives it's built from in its header and shows
  where each one sits in a *Primitive composition* section. The pattern
  template has both. Architectures don't reference primitives directly.
- Adding a primitive now needs a decision record from
  [TEMPLATE.md](TEMPLATE.md) that names the pattern requiring it.

## Alternatives considered

- **Adopt the earlier 19-primitive draft.** Most of it had no pattern in this
  repository that needed it. These were left out for now:
  - rule-based branching on agent output, such as confidence routing (no
    pattern routes on agent confidence);
  - parallel fan-out and fan-in (no pattern runs work in parallel);
  - compensation (no pattern undoes a completed effect);
  - handoff, shared context, and arbitration (multi-agent concerns with no
    pattern yet);
  - a dedicated evaluation gate (the deterministic acceptance gate runs its
    checks as `P2` functions for now).
- **Map primitives to architectures instead of patterns.** That ties a
  reusable building block to one job and repeats the mapping in every
  architecture. Patterns are the reusable layer, so the mapping belongs there.
- **Name the two primitives AgentStep, AgentTask, AgentActivity, or
  BusinessTask.** Each of these words already means something else in the
  repository; see Rationale.
- **Name them AgentWorkItem or AgentOperation.** Many BPM tools use "work item"
  for work assigned to a person, which clashes with `P5 HumanCheckpoint`.
  "Operation" was also considered and is reasonable, but function says more
  plainly that the thing takes an input and returns a result.

## Follow-up

Questions this decision leaves open for the WG:

1. **What if the approver isn't a person?** The proposal/execution split lets a
   versioned policy approve an effect instead of a human. `P5 HumanCheckpoint`
   only covers the human case, so the policy case has no primitive yet.
2. **Does the acceptance gate need its own primitive?** Today the
   deterministic acceptance gate runs its checks as ordinary `P2` functions. The
   earlier draft had a separate evaluation-gate primitive, and it isn't clear
   yet whether that adds anything.
3. **Which outcome values should be shared?** The seven values proposed in
   `P11` have nothing for an approval that expired or a loop that gave up
   (abstained). Either the list grows, or each architecture keeps its own exit
   states.
4. **Add *function* to the taxonomy.** `terms.md` defines an activity as "a
   single, bounded task". Here an activity can contain several primitives, and
   the function is the part that does the work. The taxonomy should define
   function and say how it relates to activity and business task.
