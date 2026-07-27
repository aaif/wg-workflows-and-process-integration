# EP4 — Agent-directed under workflow constraints

Status: Proposal

## Intent

An agent owns control-flow for the run: it chooses which steps to take next, in what order, using which tools, toward a goal. The workflow's role inverts — instead of sequencing steps it imposes an *envelope*: the goal, the allowed tools and effects, and the budgets the agent must operate within. Agency is high but not unbounded; the run is still fenced by [DP-09 (bound dynamic regions)](../foundations/design-principles.md). This is the profile for genuinely open-ended tasks that cannot be pre-sequenced.

## Authority sketch

| Authority | Holder | Distinctive point |
|---|---|---|
| control-flow | `agent` (bounded) | The agent decides the sequence for the whole run, not just a subregion — this is what separates EP4 from [EP3](ep3-bounded-agentic-region.md). |
| decision | `agent` | Branch and step choices are the agent's, subject to the envelope. |
| action-authorisation | `workflow` / `human` | Effects remain externally gated; the agent may act only within pre-authorised classes, escalating the rest. |
| execution | `single_agent` / `multi_agent` | One agent, or several under delegation ([WP10](../patterns/README.md)). |
| state | `workflow` | An external store stays the authoritative state owner (INV-002); the agent's working memory is not authoritative. |

The envelope is the whole point: control-flow is held by `agent` but *bounded* — a run without enforced budgets, tool allow-lists, and effect gates is out of scope for this profile.

## Characteristic coordinates

```yaml
control_flow_authority: agent           # bounded by a workflow-imposed envelope
actor_topology: single_agent            # or multi_agent under delegation
nondeterminism: ND6-ND8                 # open-ended, up to open goal
flow_shape: FS7-FS9
durability: DUR2-DUR4
effect_level: EF1-EF3                    # irreversible effects (EF4) should require escalation
assurance: AS3-AS5
impact: IM2-IM4
```

## Relationship to other profiles

- Against [EP3](ep3-bounded-agentic-region.md): EP3 confines agency to a subregion while the engine owns the run; EP4 gives the agent the run and confines it with an envelope instead of a sequence.
- Against [EP2](ep2-workflow-directed-model-assisted.md): a world apart — EP2's model proposes into engine-owned control-flow; EP4's agent *is* the control-flow.
- Composition: an EP4 run may itself invoke deterministic [EP1](ep1-workflow-directed.md) sub-workflows as tools, and may be launched from within an [EP3](ep3-bounded-agentic-region.md) region that decided its goal warranted full agent direction. Multi-agent structure uses `DLG` and [WP10](../patterns/README.md); budgets use [OV-06](../overlays/workflow-overlays.md).

## Open questions

- What makes an envelope *sufficient* — is there a checkable minimum (goal, tool allow-list, effect classes, `OV-06` budget, termination condition) below which the run should be refused?
- How is progress toward an open goal (ND8) evaluated so the run can be stopped for lack of progress rather than only on budget exhaustion?
- Where does authoritative state live when the agent reasons over large working memory — how much of `PLN`/`TSL`/`EVH` must be externalised to satisfy INV-002?
- For multi-agent EP4, how is `DLG` bounded recursively so sub-agents inherit but cannot widen the envelope (INV-008)?
- What is the human's role by default — supervisor of escalations only ([OV-01](../overlays/workflow-overlays.md)), or a required co-authoriser for any `EF4` effect?
