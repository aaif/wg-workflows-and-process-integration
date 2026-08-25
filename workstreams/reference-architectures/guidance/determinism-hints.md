# Determinism hints

A recurring mistake this RA set exists to prevent is reaching for an `AgentStep` where a cheaper, more testable deterministic mechanism already solves the problem. This table gives a practitioner a fast answer, by kind of work, for where to spend the cost of agentic reasoning and where determinism is strictly better.

| Kind of work | Recommendation | Reasoning |
|---|---|---|
| Closed-set classification with stable labels | DMN table or a trained classifier | An LLM is more expensive and less testable for identical output than a rule or classifier built for exactly this shape of problem. |
| Extraction from unstructured input | Agent (`AgentStep`) | Genuinely hard to do deterministically; free-text, document, or image extraction has no closed grammar to write rules against. |
| Arithmetic, eligibility, thresholds, entitlement | Deterministic, always | Never delegate arithmetic to a model. The correct answer is already computable exactly; an LLM is an unreliable calculator for a solved problem. |
| Routing among a known set of handlers | Deterministic first; agent only for the residual "none of the above" bucket | An enumerable handler set is exactly what a `P3 Decision` resolves exactly. Reserve agent judgment for the case that fits no known handler. |
| Planning over an open or unbounded set of subtasks | Agent | This is where autonomy earns its cost: the subtask set cannot be enumerated at design time. |
| Drafting, summarising, translating | Agent | Output is naturally reviewable text; determinism buys little for an inherently generative task. |
| Any irreversible or externally-visible commitment | Deterministic gate or `HumanCheckpoint`, never agent-decided alone | Consequences cannot be undone. The decision to commit MUST be verifiable independently of the model's own judgment. |
| Retry and idempotency logic | Workflow engine, not agent | Agents retry badly and non-idempotently. Retry semantics belong to `P9 ErrorBoundary` and the orchestrator's durable-execution layer. |

General heuristic: **put the LLM where the input space is open and the output is reviewable; keep determinism where the input space is closed or the output is irreversible.**

## Related

- [Single-agent checklist](checklist-single-agent.md): applies this table's logic to a specific use case, in order.
- [P2 DeterministicTask](../../taxonomy/primitives/p02-deterministic-task.md)
- [P3 Decision](../../taxonomy/primitives/p03-decision.md)
- [P4 AgentStep](../../taxonomy/primitives/p04-agent-step.md)
- [`../architectures/single-agent.md`](../architectures/single-agent.md)
