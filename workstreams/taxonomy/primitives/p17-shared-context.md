# P17 SharedContext

**Obligation:** SHOULD

## Definition

A coordination mechanism through which multiple `AgentStep`s read and write a common evolving artifact, governed by a declared consistency model, rather than coordinating through direct handoffs.

## Why it exists

Without a declared consistency model, concurrent conflicting writes happen silently. Nothing in a blackboard-style architecture forces two agents to notice they overwrote each other. Shared mutable state is already common in practice; "eventually consistent" is not itself an answer to what an agent should do on conflict, and `P17` forces that answer to be written down. A workflow using this primitive MUST declare its consistency model (for example, last-writer-wins with a version check, append-only with no overwrite, or single-writer-at-a-time enforced by a lock) before it is used.

CMMN's case-file model is the closest conceptual match, in any pre-agentic standard, to "the agent chooses what to do next against a common evolving artifact." A CMMN case operates over a case file through a case plan model composed of stages, which can contain discretionary items: tasks and sub-stages available to be planned into the case at a case worker's discretion, rather than fixed into the plan in advance. A discretionary item is, structurally, a menu of things a competent actor *may* choose to do given the current state of the case file, which is a reasonable description of what an `AgentStep`'s tool scope is: a bounded menu of `P5 ToolCall` candidates the agent may select from, given the current state of its input contract. CMMN never had to solve `P17`'s specific problems. There is no CMMN notion of a token budget on how many discretionary items a case worker may plan in, no confidence signal on a case worker's choice, and no compensation handler tied to a discretionary item the way BPMN ties one to an activity, but the shape of "bounded, declared menu of eligible next actions, chosen by an actor rather than fixed by a graph" is exactly the shape this primitive reaches for. CMMN predates the agentic era by over a decade and was solving a human-case-worker version of the same structural problem `P17` solves for a set of agents.

## Prior art

| System | Nearest equivalent |
| --- | --- |
| CMMN | Case file: the nearest standards concept for a shared evolving artifact multiple actors read and write |
| LangGraph | Channels-with-reducers model: the nearest framework concept |

Nearest equivalent is editorial judgment, not a conformance claim. BPMN 2.0, n8n, AWS Step Functions, and Temporal have no named nearest equivalent for `P17` in the material surveyed for this RA. None of them models a shared, concurrently-writable artifact as a first-class construct distinct from ordinary process or execution data.

## Relationship to other primitives

- [P18 ArbitrationPolicy](p18-arbitration-policy.md): required for resolving conflicting writes to shared state.
- [P15 AuditRecord](p15-audit-record.md): writes to shared state must themselves be auditable.
- [P4 AgentStep](p04-agent-step.md): each writer to a `P17` store is a bounded, contracted step, not an unscoped participant.

## Open questions

- Does `P17 SharedContext` need one WG-standard consistency model, or should the RA only require that each workflow declare its own per-workflow model?
