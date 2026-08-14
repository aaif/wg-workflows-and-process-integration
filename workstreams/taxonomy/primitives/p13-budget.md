# P13 Budget

**Obligation:** MUST

## Definition

An enforced ceiling on an agent's resource consumption, covering four dimensions: iterations, tool calls, tokens/cost, and a wall-clock deadline.

## Why it exists

Every orchestrator surveyed already has *some* retry construct, *some* parallel-execution construct, and *some* human-pause construct, just under a different name in each system. `P13` is the one primitive where that pattern breaks down completely: none of the systems surveyed has a resource-consumption ceiling construct *at all*, under any name. This is not a vocabulary-fragmentation problem like the others in this primitive set. It is a genuine, structural absence, and it is worth being precise about the difference. Naming a primitive that every system already half-has is a translation exercise; naming `P13` is closer to specifying a requirement no reviewed system has yet chosen to meet.

BPMN, DMN, CMMN, the cloud state machines, and the durable-execution engines were all designed for control flow whose step count is knowable from the model of the process itself: a BPMN process with no loop construct executes a bounded number of steps; a multi-instance activity's iteration count is the size of its input collection, known before the first iteration runs; a Step Functions `Map` state's fan-out is the size of its input array. None of these needed a resource-consumption ceiling as a distinct construct, because the ceiling was already implied by the model: you cannot "run away" past a step count the model itself fixes in advance.

An `AgentStep`'s step count has no such property. The number of tool calls, reflection iterations, or reasoning turns an agent takes to reach its goal is discovered at run time, by the model's own reasoning, and is not derivable from the `AgentStep`'s definition. The structural difference here is that a deterministic step's cost is a property of its design; an agentic step's cost is a property of its execution. Therefore the ceiling on that cost has to be declared externally, by the workflow, and enforced by the orchestrator during execution.

BPMN's `completionCondition` (both the plain form and the multi-instance form) stops a collection of activities early once a boolean expression is satisfied, but it has no concept of token cost, dollar cost, or aggregate wall-clock spend across a whole `AgentStep`'s internal loop; it bounds *instances*, not *resource consumption*. Camunda's own AI Agent connector documents a configurable limit on the number of model calls the agent may make (the closest built-in guard surveyed anywhere in this landscape, and still only one dimension of four): it caps call count, not token spend or dollar cost, and cost is now a first-class operational failure mode in its own right, independent of whether the agent's reasoning ever goes wrong. None of these mechanisms is a *budget* in the sense `P13` requires, because none of them was designed to answer "how much may this cost, in total, across every dimension that matters to whoever is paying for it."

The `AgentStep` boundary contract's fifth element states the enforcement requirement directly: the `P13` ceilings (max iterations, max tool calls, max tokens/cost, wall-clock deadline) are what element 5 requires every `AgentStep` to declare.

A multi-agentic workflow MUST have exactly one global `P13 Budget` ceiling at the top level. Every per-agent or per-handoff budget is a sub-allocation drawn against that ceiling. A fan-out that hands each of five agents a "reasonable" budget, each of which may itself hand off to two more agents with their own "reasonable" budgets, does not sum to a reasonable total. Multi agent budget is multiplicative and not additive for this reason. This is the budget-transfer element of the `P16 Handoff` contract, and it is one of the global invariants every multi-agent topology must hold regardless of which topology is chosen.

A `P13` ceiling is not a single flat number even within one `AgentStep`. In case of loops, an outer iteration loop, an inner tool-call loop, and a generator-critic loop nested inside a single step each consume budget at a different tier, and each tier needs its own sub-allocation rather than sharing one undifferentiated ceiling. See [`../guidance/loop-tiers.md`](../../reference-architectures/guidance/loop-tiers.md) for how tiers decompose a single `P13` ceiling.

### Anti-patterns this primitive exists to prevent

- **No budget.** The characteristic agentic failure mode: iteration loops that terminate only when cost or time is exhausted in production, not by design.
- **Per-agent budgets with no global ceiling.** Consequence: budgets compose multiplicatively across fan-out and handoffs; the actual total cost or risk exposure is unbounded even though every individual allocation looked reasonable.

### Boundary with the Governance, Risk & Regulatory Alignment WG

Budget exhaustion is a policy-relevant event, not merely an operational one: an organisation's tolerance for how much an agentic workflow may spend before halting is itself a governance decision in many regulated contexts. This RA specifies the enforcement mechanism and the classification (`budget_exhausted`); it does not specify what ceiling is appropriate for a given regulatory regime, which it treats as an external input from that WG.

## Prior art

| System | Nearest equivalent |
| --- | --- |
| BPMN 2.0 | No native primitive: `completionCondition` is the closest mechanism |
| n8n | No native primitive |
| AWS Step Functions | No native primitive |
| Temporal | No native primitive |
| LangGraph | No native primitive |

Nearest equivalent is editorial judgment, not a conformance claim. Every system surveyed lacks a native resource-consumption ceiling. This is not an oversight in the survey, it is the finding: no reviewed engine or framework has a native equivalent to `P13`, and Camunda's documented model-call limit in its AI Agent connector is the closest built-in guard found anywhere in the landscape, covering only one of `P13`'s four dimensions.

## Relationship to other primitives

- [P4 AgentStep](p04-agent-step.md): the budget ceilings are boundary contract element 5; unbounded agent loops are this RA's characteristic named anti-pattern, and `P13` is the primitive that closes it.
- [P7 FanOut/FanIn](p07-fan-out-fan-in.md): bounds the maximum concurrent count, so a fan-out cannot itself become an unbounded multiplier on total spend.
- [P16 Handoff](p16-handoff.md): budget transfer (contract element 4), sub-allocated against one global ceiling, never granted independently, precisely because per-agent allocations compose multiplicatively across a chain of handoffs.
- [P18 ArbitrationPolicy](p18-arbitration-policy.md): a generator-critic loop needs both a hard `P13` iteration cap and a deterministic `P18` stopping rule; neither is sufficient alone.
- [P14 OutcomeContract](p14-outcome-contract.md): `budget_exhausted` is one of the seven canonical classifications, distinct from `failed`, because the correct remediation instinct differs sharply between the two.
- [P19 EvaluationGate](p19-evaluation-gate.md): the presence or absence of a strong evaluation gate is the single best predictor of whether a step can safely be given a large budget: a step with a strong gate exits on success, one without exits only by exhaustion.
- See [`../guidance/loop-tiers.md`](../../reference-architectures/guidance/loop-tiers.md): each loop tier inside an `AgentStep` needs its own budget allocation, not a single undifferentiated ceiling.

## Open questions

- How to represent `P13 Budget` portably, given no reviewed engine or framework (BPMN, n8n, Step Functions, Temporal, LangGraph) has a native equivalent.
- What would a portable, cross-runtime representation of `P13 Budget` and `P18 ArbitrationPolicy` actually look like in a concrete schema, and should it be proposed as an extension to an existing standard (BPMN `extensionElements`, an MCP extension, an A2A extension) or as new, WG-owned notation?
