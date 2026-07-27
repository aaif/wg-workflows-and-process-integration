# EP6 — Event-directed continuation

Status: Proposal

## Intent

The run advances because *external events arrive*. Control-flow authority rests with an event stream: the run persists, waits, and resumes each time a relevant signal is received. Between events the run is quiescent but durable. This is the profile for long-running, reactive processes — order lifecycles, saga-style coordination, device/telemetry-driven flows — where the shape of the run is dictated by what happens outside it, not by a pre-planned sequence.

## Authority sketch

| Authority | Holder | Distinctive point |
|---|---|---|
| control-flow | `event` | Continuation is triggered by external events; the engine reacts rather than drives. |
| decision | `workflow` | An event triggers *reconsideration*; a deterministic handler still decides what the event means for the run. |
| action-authorisation | `workflow` (+ `human`) | Effects triggered by events stay gated by rules; risky ones escalate. |
| execution | `workflow` (+ optional model) | Event handlers execute the mechanics of each continuation. |
| state | `workflow` | A durable store owns authoritative state across quiescent periods (INV-002). |

Crucial subtlety: an event *triggers* continuation but does not by itself *acquire* control-flow authority for anything beyond the handler — the run decides what to do with the event under [DP-04 (explicit authority)](../foundations/design-principles.md). The signature primitives are `WAI` on event conditions and `EVH`, over a [WP08 durable envelope](../patterns/README.md) with [OV-04 (durable wait)](../overlays/workflow-overlays.md).

## Characteristic coordinates

```yaml
control_flow_authority: event
actor_topology: any
nondeterminism: ND0-ND3                 # arrival is unpredictable; handling is deterministic
flow_shape: FS8                         # event-driven, long-running, quiescent-then-reactive
durability: DUR3-DUR4                   # must persist between events
effect_level: EF1-EF3
assurance: AS1-AS3
impact: IM1-IM3
```

## Relationship to other profiles

- Against [EP5](ep5-human-directed-continuation.md): both are continuation-driven, but EP5 waits on deliberate human acts and EP6 waits on system events; a human approval delivered as an event blurs the line — classify by what predominantly drives the run.
- Against [EP1](ep1-workflow-directed.md): an EP1 run is engine-sequenced end-to-end; an EP6 run is a sequence of engine-sequenced *reactions* stitched together by external timing.
- Composition: each event handler is often itself an [EP1](ep1-workflow-directed.md) or [EP2](ep2-workflow-directed-model-assisted.md) segment; an EP6 run can also open a bounded [EP3](ep3-bounded-agentic-region.md) region in response to a particular event. Handler activity is recorded via [OV-07 (execution history)](../overlays/workflow-overlays.md).

## Open questions

- How are out-of-order, duplicate, or late events reconciled against authoritative state (INV-002) without corrupting the run?
- What is the correlation contract that binds an incoming event to the right waiting run, and how is it made tamper-evident?
- When an event should trigger reconsideration that *widens* authority (e.g. spawn an agentic region), where is that escalation authorised rather than implied?
- How long may a run stay quiescent, and what distinguishes "still waiting" from "abandoned" for timeout/compensation purposes?
- How does event-directed continuation interact with budgets ([OV-06](../overlays/workflow-overlays.md)) when the number of events per run is unbounded?
