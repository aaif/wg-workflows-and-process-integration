# Durable Wait

**Solves:** A run must wait longer than any process hosting it will live \
**Used in:** [Single-agent process with human approval](../architectures/single-agent-human-approval.md) · any architecture whose run must outwait the processes hosting it \
**Requires capabilities:** Execution engine · state/context store \
**Related patterns:** [Human approval gate](human-approval-gate.md) · [proposal/execution split](proposal-execution-split.md)

## Problem

A workflow needs to stop and wait — for a human approval, an external event,
a timer — for hours or days. The processes hosting it live for minutes, and
restarts and deploys happen on their own schedule. The wait must belong to
the *run*, not to any process.

## Why this is hard

- Holding the wait in process memory is the easy implementation and the
  fatal one.
- Event-driven resume is clean but the resume signal may be delivered more
  than once, late, or to a process with no memory of the run.
- A wait with no time bound is not persistence carried to an extreme; it is
  a stuck run nobody will ever find.
- Polling for wake-up conditions trades latency against cost; the pattern
  must permit either without changing the invariants.

## Solution

```text
run ──► record state + position ──► PARKED ⏸      (no process holds the run)
                                       │
     external event / timeout ────────┘──► load the record ──► resume
```

While parked, the record *is* the run: nothing in memory represents it.
Resume is triggered by an event or a timeout — never by a process that
happened to survive. What form the record takes is the implementation
family's choice: an execution history, a saga row, a process-instance
entry.

The essential move is turning a *physical* wait (a blocked thread or
process) into a *logical* one (a recorded fact: run X is parked, awaiting
event Y). Durable *state* is an ingredient, not the pattern: a system can
persist its state after every step and still lose every pending wait on
deploy, if the waiting itself lives in process memory.

Resume must restore three things, not just liveness:

- **Position** — which step the run was parked at
- **Context** — the inputs and intermediate results the continuation
  depends on
- **Identity** — which real-world request this is: the correlation that
  routes the wake-up event to the right run

## Invariants (must hold in any implementation)

- A parked run survives process death, restarts, and deploys.
- Resume restores position and context: the continuation runs with what the
  run already knew, not a reconstruction from scratch.
- Resume is idempotent: the same wake-up event delivered twice resumes once.
- A parked run is discoverable: after a restart, anything waiting on it (a
  pending approval, a subscription) can be found and acted on.
- A time limit is part of the wait: every parked run carries a timeout and
  an escalation or expiry path.

## Failure modes when violated

- Wait held in process memory → every deploy silently kills pending waits.
- Non-idempotent resume → the continuation runs twice (double execution when
  the continuation has side effects).
- Wake-up routed to a specific process instance → the run strands when that
  instance dies.
- No timeout → runs accumulate in PARKED forever; nobody notices until an
  audit does.

## Implementation approaches (illustrative, not requirements)

No framework is required. Runtime features provide parts of the pattern; the
complete implementation remains responsible for the invariants those features
do not enforce. The examples below span durable orchestration, persistent
graph runtimes, and managed workflow engines. Event-driven implementations
can satisfy the same pattern without a centralized engine: handlers carry the
continuation while a correlation store carries position, context, and run
identity.

| Family | Documented mechanism | What it provides | What the implementation must add |
|---|---|---|---|
| Durable orchestration | [Azure Durable Functions external events](https://learn.microsoft.com/en-us/Azure/Azure-functions/durable/durable-functions-external-events) | An orchestration can unload while waiting and resume when an event reaches its instance; durable timers can race the event | A unique event ID and deduplication, because delivery can be at least once; a deadline and explicit escalation or expiry; domain audit records |
| Persistent graph runtime | [LangGraph interrupts and persistence](https://docs.langchain.com/oss/python/langgraph/interrupts) | `interrupt()` checkpoints graph state, and the same thread ID resumes the saved position and context | A durable production checkpointer; an application-defined timeout and escalation path because interrupts wait indefinitely; idempotent handling of work repeated on resume |
| Managed workflow engine | [AWS Step Functions callback tasks](https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html) | A Standard Workflow task pauses until its task token returns via `SendTaskSuccess` or `SendTaskFailure`, or until configured timeout limits are reached | Protection and correlation of task tokens; an explicit timeout outcome; idempotency and domain-level audit records |

## Known uses outside agents

BPMN user tasks and timer events (Camunda, Flowable); message queues with
delayed redelivery; order-fulfillment sagas that park awaiting shipment or
payment confirmation. The industry converged on this shape long before LLMs.

The agent delta: the mechanism transfers unchanged — what the run waits *on*
is new. The parked record now holds an agent's proposal and the context that
produced it, so the wait must preserve enough context to make the eventual
resume (and its audit trail) meaningful.
