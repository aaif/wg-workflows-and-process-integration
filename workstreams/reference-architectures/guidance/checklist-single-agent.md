# Single-agent checklist

A practitioner brings a use case. Walk it through in order:

1. **Can the task be fully enumerated at design time**: a fixed set of paths, rules, and thresholds? If yes: **pure deterministic workflow.** No `AgentStep` needed. State this plainly. This is the most common correct answer, regardless of how "AI-native" the initiative is framed.
2. **If not fully enumerable, is there exactly one point** where the input space is genuinely open (free text, unstructured evidence, an unbounded subtask set), with everything else fixed? If yes: **a single `AgentStep` in an otherwise deterministic workflow.** Contract that one step per the [`AgentStep` boundary contract](../contracts/agent-step-boundary.md); leave the rest deterministic.
3. **Are there multiple such points**, each independently boundable with its own contract, that do not need to negotiate with each other or hand off partial state directly? If yes: **multiple `AgentStep`s in one workflow, still this RA.** Each `AgentStep` is independently contracted; the workflow, not the agents, coordinates them.
4. **Do the steps need to negotiate, delegate to each other, or converse among themselves**: does control pass agent-to-agent rather than always returning to the orchestrator? If yes: **this RA does not cover it.** See [`../architectures/multi-agent.md`](../architectures/multi-agent.md) and its own [checklist](checklist-multi-agent.md).

Filtering question, asked before any of the above: **is there already a reviewable, bounded rule that solves this?** If a subject-matter expert can state the rule in a sentence, write the rule. An agent is not warranted merely because the input happens to be text, or because a stakeholder wants "AI" somewhere in the process. This is the single most common misapplication this RA exists to prevent.

## Related

- [Determinism hints](determinism-hints.md): the decision table that backs step 1 and 2 above.
- [Anti-patterns](anti-patterns.md)
- [`../architectures/single-agent.md`](../architectures/single-agent.md)
- [Multi-agent checklist](checklist-multi-agent.md)
