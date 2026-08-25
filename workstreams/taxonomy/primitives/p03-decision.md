# P3 Decision

**Obligation:** MUST

## Definition

A branch resolved by an explicit rule.

## Why it exists

Without an explicit, reviewable branch construct, routing logic ends up buried inside prompts or scattered across ad hoc code. This RA depends on a clear pattern: `AgentStep` output flows into a `Decision`, which then routes to a `HumanCheckpoint` or auto-completes.

`P3` is the deterministic counterpart to `P4 AgentStep`. Anywhere this RA says "route on confidence" or "route among a known set of handlers," that's a `P3` at work. It's also what the determinism-hints guidance means by "routing among a known set of handlers": if the handler set is enumerable, a `Decision` is what resolves it, and agent judgment gets reserved for the one case that doesn't fit any known handler.

## Prior art

| System | Nearest equivalent |
| --- | --- |
| BPMN 2.0 | Gateway + business rule task (DMN) |
| n8n | IF / Switch node |
| AWS Step Functions | Choice state |
| Temporal | Ordinary code branch |
| LangGraph | Conditional edge |

Nearest equivalent is editorial judgment, not a conformance claim.

## Relationship to other primitives

- [P4 AgentStep](p04-agent-step.md) — the output contract's confidence signal is what makes a confidence-based `Decision` possible after an agent step.
- [P6 HumanCheckpoint](p06-human-checkpoint.md) — the typical low-confidence branch target.
- [P14 OutcomeContract](p14-outcome-contract.md) — decisions downstream of an `AgentStep` are deterministic all the way to the outcome classification.
