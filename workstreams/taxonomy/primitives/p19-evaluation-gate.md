# P19 EvaluationGate

**Obligation:** MUST when an `AgentStep` iterates against a checkable predicate

## Definition

A machine-checkable predicate an `AgentStep` can evaluate its own output against, without human involvement, to decide whether to iterate again or terminate. Tests, evals, schema validation, a scoring dataset, a compile-or-lint gate: the primitive is the declared slot, not any particular technique.

## Why it exists

This is the primitive that makes a bounded iteration loop *closable*. The `P4 AgentStep` boundary contract requires termination conditions evaluated outside the model, but a termination condition with nothing to evaluate against degenerates into either a fixed iteration count or the model self-reporting success, and the boundary contract already rejects the latter. `P19` is what a termination predicate reads. Without it, an agent that iterates has only `P13 Budget` standing between it and an unbounded loop, which means every iterating step exits by exhaustion rather than by success. That is the difference between a loop that converges and a loop that merely stops.

The corollary is worth stating directly: the presence or absence of a `P19` gate is the single best predictor of whether an `AgentStep` can be given a long budget safely. A step with a strong gate can be given a large budget because it will exit when it succeeds; a step with no gate must be given a small one because exhaustion is its only exit.

### Scope boundary

State this explicitly and prominently: per the charter, evaluation of model reasoning quality and accuracy belongs to the **Accuracy & Reliability WG**. This RA requires only that the *slot* exist and be declared, and that the predicate be evaluable by the orchestrator rather than asserted by the agent. What constitutes a good eval, how quality is measured, and how gates are validated is that WG's domain, not this one's. This mirrors how `P4`'s boundary contract handles identity: the RA requires the attribute, another WG owns the mechanism.

## Prior art

| System | Nearest equivalent |
| --- | --- |
| BPMN 2.0 | `completionCondition` on an ad-hoc or multi-instance activity is the closest structural equivalent, though BPMN has no notion of the predicate being a test suite |
| n8n | No native equivalent: a workflow author wires validation nodes by hand |
| AWS Step Functions | A `Choice` state can read a validation `Task`'s output, so it is expressible but not a first-class construct |
| Temporal | Expressible as an activity whose result the workflow branches on |
| LangGraph | A conditional edge reading a validation node's output |

Nearest equivalent is editorial judgment, not a conformance claim. In every system surveyed this primitive is expressible but not named, which is precisely the argument for naming it here.

## Relationship to other primitives

- [P4 AgentStep](p04-agent-step.md): the boundary contract's termination-conditions element is what a `P19` gate feeds.
- [P13 Budget](p13-budget.md): a gate that fails at budget exhaustion produces `budget_exhausted`; one that fails on the predicate produces `failed`. These are different classifications requiring different remediation. The presence of a strong gate is the best predictor of whether a step can safely carry a large budget.
- [P14 OutcomeContract](p14-outcome-contract.md): see above; the gate's failure mode determines which of the seven classifications applies.
- [P6 HumanCheckpoint](p06-human-checkpoint.md): a `P19` gate is what lets the workflow *not* need a human in the inner loop.
- See [`../guidance/loop-tiers.md`](../../reference-architectures/guidance/loop-tiers.md): each loop tier an `AgentStep` runs may need its own gate, evaluated at that tier.
