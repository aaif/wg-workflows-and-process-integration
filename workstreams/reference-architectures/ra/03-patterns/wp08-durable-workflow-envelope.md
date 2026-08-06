# WP08 — Durable Workflow Envelope

Status: Mature

## Problem
Long-running workflows must survive process restarts, wait for external events
or human decisions, and be reconstructable after failure. Patterns that hold
state only in memory lose progress on any interruption. This pattern wraps other
patterns in a durable envelope with checkpointing, resumable waits, and an event
history that is the system of record.

## When to use / not use
- Use whenever a run spans restarts, long waits, or external callbacks.
- Use to wrap effectful or human-gated patterns that must be recoverable.
- Do not use for a single short, purely in-memory computation (see [WP00](wp00-deterministic-baseline.md)).
- Do not treat it as a replacement for idempotency on the effects it wraps.

## Structure
Each step checkpoints; waits are durable and resumable; the event history is
authoritative and lets the run replay to its current point after a restart.

```mermaid
flowchart LR
  TRG --> CHK --> WAI
  WAI -->|event| CHK2[CHK] --> TXN --> EVH
  EVH --> OUT
```

## Primitives
- `CHK` — checkpoint durable state at step boundaries.
- `WAI` — durable, resumable wait for time, event, or human decision.
- `TMO` — timeout guarding a wait.
- `EVH` — event history serving as the system of record.
- `TXN` — the wrapped protected effect.
- `AUD` — audit trail derived from history.

## Authority allocation
| Authority | Holder |
|---|---|
| Control-flow | workflow (durable engine) |
| Decision | inherited from wrapped pattern |
| Action-authorisation | inherited from wrapped pattern |
| Execution | workflow |
| State | workflow (authoritative durable store) |

## Invariants and rules
- INV-002 — the durable store is the authoritative state owner.
- INV-004 — the run boundary is explicit and durable.
- INV-003 — only accepted transitions are persisted to history.
- OV-04 — durable-wait overlay; OV-07 — execution-history overlay.
- DP-08 — make waits and durability explicit.

## Coordinates
```yaml
nondeterminism: ND1
control_flow_authority: workflow
actor_topology: single_agent
flow_shape: FS7
durability: DUR3
effect_level: EF3
assurance: AS2
impact: IM3
```

## Failure modes
- Non-deterministic replay: side effects during replay diverge from history.
- Unbounded waits without `TMO` stall runs indefinitely.
- History not authoritative: state read from a source other than `EVH`.

## Consequences
- Benefits: runs survive restarts and long human/external waits.
- Benefits: replayable history gives strong auditability and recovery.
- Costs: requires deterministic replay discipline and a durable backend.

## Example
In [invoice processing](../../examples/invoice-processing/README.md), the run must
survive the human-review wait: after producing the draft, the workflow `CHK`
checkpoints and enters a durable `WAI` for the approval event, guarded by `TMO`.
If the host restarts during the wait, the run resumes from `EVH` at exactly the
point it paused, and the wrapped approval-and-post ([WP07](wp07-human-supervised-action.md)) completes without redoing prior work.
