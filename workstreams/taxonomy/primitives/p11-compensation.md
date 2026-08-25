# P11 Compensation

**Obligation:** SHOULD

## Definition

The semantic undo of a completed effect.

## Why it exists

Without semantic undo, an agent-caused `reversible_write` that turns out wrong has no path back except manual cleanup outside the workflow's own record, which breaks the reconstructable-audit invariant this RA otherwise requires everywhere else.

BPMN's compensation handler ties a semantic undo to a specific activity, invoked when a compensation event fires against a process that already completed that activity. The undo is declared at design time, alongside the action it reverses, not bolted on afterward. Temporal's saga pattern generalizes the same idea to a sequence of steps in code: each step that performs an effect registers a compensating action, and if a later step fails, the saga runs the registered compensations in reverse order. Both mechanisms share the same shape this RA asks for: the undo is declared *with* the action, not written as ad hoc cleanup code discovered only after something has already gone wrong in production.

This is worth stating plainly rather than passing over: the agent-native frameworks that are, right now, where the industry is actually building agentic workflows, have regressed on a capability the pre-agentic durable-execution and process standards already had solved. BPMN has a compensation handler. Temporal has the saga pattern. A BPMN process or a Temporal saga that performs a reversible action and later needs to undo it has a declared, engine-supported path to do so. n8n and LangGraph, by contrast, have no equivalent at all (at the time of this writing): "a real gap," in this RA's own cross-mapping judgment. An n8n AI Agent node or a LangGraph agent that performs an equivalent reversible action has no framework-native undo; if it happens at all, it is bespoke code the workflow author has to write and wire in by hand, with no structural guarantee it is invoked when it should be.

This RA should refuse to accept that regression as an acceptable cost of adopting agentic frameworks. The multi-agent RA's own failure-mode table ties the absence of compensation directly to a concrete, common failure: "duplicated side effects on handoff retry," where a handoff retried after an ambiguous failure causes the receiver's irreversible action to execute twice. This is prevented only if retried handoffs are idempotent or compensated via `P11`. An agent that can perform a `reversible_write` (a tool class the RA's own effect taxonomy explicitly permits an agent to use without a mandatory `HumanCheckpoint` in front of every call) needs a real undo path when that write turns out to be wrong, precisely because the RA's own design deliberately allows that class of action to happen without human pre-approval.

`P11` is marked SHOULD rather than MUST in the primitive table today. The case above is an argument the WG should weigh directly, not evidence that the classification is already settled: whether `P11`'s obligation level should move from SHOULD to MUST for any `AgentStep` with a `reversible_write` tool in scope is a live question, named here but not resolved.

### What breaks without it, concretely

- A crash or an ambiguous failure mid-effect leaves a `reversible_write` half-done, with no declared record of what needs to be undone or by whom.
- A compliance reviewer reading the audit trail after the fact has no way to distinguish "this effect was undone on purpose, by a declared mechanism" from "this effect was never addressed at all."
- A retried handoff whose receiver already executed an irreversible action the first time has no structural guard against executing it twice. This is the specific mechanism behind the "duplicated side effects on handoff retry" failure mode.

### Where P11 sits in the tool-scope taxonomy

The tool-scope contract's three effect classes imply two different safety strategies, not one. An `irreversible` tool is handled by *prevention*: it MUST NOT be reachable without a `HumanCheckpoint` or a deterministic policy gate in front of it, because there is no undo to fall back on once it executes. A `reversible_write` tool doesn't get much scrutiny by design: the RA's taxonomy deliberately lets an agent perform one without requiring human pre-approval. That's exactly why it needs a mitigation strategy on the back end rather than a gate on the front end. `P11` is that mitigation strategy. Without it, the taxonomy's middle tier would be permissive going in and have nothing declared coming out. That's the specific asymmetry the SHOULD-to-MUST question above is really asking the WG to resolve.

### Failure mode this primitive prevents

| Failure mode | How it manifests | What prevents it |
| --- | --- | --- |
| Duplicated side effects on handoff retry | A handoff is retried after an ambiguous failure and the receiver's irreversible action executes twice | Retried handoffs MUST be idempotent or compensated via `P11` |
| Uncompensated `reversible_write` | An agent-caused write turns out wrong and has no declared undo path | A compensation handler declared alongside the action, per the BPMN/Temporal precedent above |

## Prior art

| System | Nearest equivalent |
| --- | --- |
| BPMN 2.0 | Compensation handler |
| n8n | No equivalent, a real gap |
| AWS Step Functions | No first-class primitive, compose Catch + compensating Task |
| Temporal | Saga pattern |
| LangGraph | No equivalent, a real gap |

Nearest equivalent is editorial judgment, not a conformance claim. n8n and LangGraph have no compensation equivalent at all. This RA treats that absence as a real regression relative to pre-agentic durable execution, not a neutral gap.

## Relationship to other primitives

- [P5 ToolCall](p05-tool-call.md): the `reversible_write` effect class this primitive exists to protect; `irreversible` tools are handled by prevention (a gate) rather than by `P11`'s mitigation.
- [P9 ErrorBoundary](p09-error-boundary.md): typed failure capture that may trigger a compensating action.
- [P16 Handoff](p16-handoff.md): retried handoffs MUST be idempotent or compensated via `P11`, per the multi-agent RA's failure-mode analysis of duplicated side effects on handoff retry.
- [P14 OutcomeContract](p14-outcome-contract.md): a compensated effect still needs a terminal classification distinct from an uncompensated failure.
- [P15 AuditRecord](p15-audit-record.md): a compensating action needs to be recorded as its own event, not folded silently into the original write's audit entry.

## Open questions

- Should `P11`'s obligation level move from SHOULD to MUST for any `AgentStep` with a `reversible_write` tool in scope? This is a live question for the WG; this document takes a position but does not have the authority to change the RA files' normative table.
- If the obligation level does move for the `reversible_write` case specifically, should the primitive table record a conditional obligation, the same style already used for `P18` ("MUST when agents can disagree") and `P19` ("MUST when an AgentStep iterates against a checkable predicate"), rather than a flat MUST or SHOULD?

