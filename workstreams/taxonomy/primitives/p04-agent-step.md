# P4 AgentStep

**Obligation:** MUST

## Definition

The bounded, non-deterministic step: this RA's central object. The workflow owns the process; the `AgentStep` is a contracted, bounded piece of it, not the other way around.

Every `AgentStep` MUST declare eight elements before it is fit to run in production:

1. Goal specification
2. Input contract
3. Output contract
4. Tool scope
5. Budget
6. Termination conditions
7. Identity and delegated authority
8. Observability contract

Each is a required field on the contract, not an optional enhancement. The full, normative text of all eight elements is specified in [`../contracts/agent-step-boundary.md`](../../reference-architectures/contracts/agent-step-boundary.md) and is not restated here. This file names the elements only so the argument below is legible without cross-referencing.

## Why it exists

Without a bounded container with its own contract, agent reasoning either becomes the top-level orchestrator (this RA's first anti-pattern, which inverts the ownership model and means the workflow can no longer enforce budgets, gates, or audit from outside the model's own control flow), or agent behaviour is scattered across steps with no single place to enforce budget, tool scope, or termination. `P4` is the central object; the eight-element boundary contract is meaningless without a named container to attach it to.

The deeper argument is architectural, not a matter of model quality. Consider an agent given unbounded tool scope, no budget, no confidence signal on its output, and no termination predicate evaluated outside its own reasoning. That agent will fail in production: not eventually, but characteristically, and not because the underlying model is insufficiently capable. A better model does not add a budget where none was declared; it does not add a confidence field to an output schema that was never specified; it does not stop an unbounded tool-use loop that no external mechanism is watching. Each of these is a structural absence, not a competence gap, and improving the model that sits inside an unbounded structure improves how confidently it fails, not whether it fails. This is the case for a reference architecture (a specification of what has to exist *around* the model) rather than a better prompt or a better agent framework. A framework improves the model's tools and ergonomics but does not, by itself, obligate a project team to declare a budget, a tool allowlist, or a termination condition; nothing stops a team from using any given framework and still shipping an unbounded agent inside it.

### Effect classification is a workflow-level concern

The tool-scope element of the boundary contract requires every tool available to an agent to be classified by effect (`read_only`, `reversible_write`, `irreversible`), asserted by the workflow's own tool registry rather than inferred at call time from server-supplied hints alone. This is not a preference for redundancy; it follows directly from what MCP itself says about its own protocol. The [MCP specification](https://modelcontextprotocol.io/specification/2025-06-18) states that tool annotations from untrusted servers "should be considered untrusted," and that MCP "itself cannot enforce these security principles at the protocol level." A protocol that explicitly declines to be the enforcement layer for its own trust claims cannot then be treated as the enforcement layer by something built on top of it. If MCP will not vouch for a server's self-description, the workflow calling that server through MCP cannot either, without doing its own independent check.

The practical consequence: effect classification has to be a workflow-level concern, asserted once, centrally, by whoever configures the workflow's tool registry, not a server-level concern where each MCP server's own annotation is trusted at face value. A misconfigured or actively malicious MCP server could annotate an `irreversible` action as read-only, and nothing in MCP's own protocol design would catch that. The annotation is a hint the server offers about itself, not a claim any independent party has verified. The workflow's own registry, populated by whoever configured the deployment having done some out-of-band verification of what the tool actually does, is the only party in this chain with both the incentive and the position to get the classification right, which is why the RA places authority there rather than at the tool server.

### Anti-patterns at this boundary

Several of this RA's named anti-patterns are violations of the `P4` boundary specifically, not of the RA in general:

- **Agent as the top-level orchestrator, with the workflow inside it.** Inverts the ownership model; the workflow can no longer enforce budgets, gates, or audit from outside the model's own control flow.
- **Unbounded tool scope.** A denylist, or "grant access and see," means the workflow never classifies effect, so it never knows where to put a gate. Irreversible actions become reachable with no `HumanCheckpoint` in front of them.
- **Confidence-free output.** Forces every downstream consumer to trust all `AgentStep` output equally, so `P3 Decision` has nothing to route on.
- **Retry logic inside the agent.** Agents retry non-idempotently and without the orchestrator's visibility; a failed tool call retried by the model can double-execute a `reversible_write`, or worse.
- **Irreversible tool with no gate.** The most consequential violation of tool-scope contract element 4.
- **"The prompt is the guardrail."** The MCP specification itself states it "cannot enforce these security principles at the protocol level," and a prompt is not enforcement either. It is a request the model MAY ignore, misread, or be steered around.

## AgentStep in practice: the BPMN ad-hoc sub-process precedent

Camunda 8's [ad-hoc sub-process](https://docs.camunda.io/docs/components/modeler/bpmn/ad-hoc-subprocesses/) is the strongest existing evidence that BPMN 2.0 can host a bounded `AgentStep` without a new element type.

An ad-hoc sub-process (marked with a tilde `~`) is an embedded sub-process whose inner elements are not connected to start or end events: each MAY execute multiple times, in any order, or be skipped. It MUST have at least one activity and MUST NOT have start or end events. It has two implementations: handled internally by Zeebe, or by a **job worker**, which decides which elements to activate and completes the sub-process's job with an `adHocSubProcess` job result. Camunda's own [AI Agent Sub-process connector](https://docs.camunda.io/docs/components/connectors/out-of-the-box-connectors/agentic-ai-aiagent-subprocess) uses exactly this job-worker implementation to let an agent dynamically select and invoke tools.

Mapped onto this RA's primitives: the ad-hoc sub-process itself is the `P4 AgentStep` container; the elements it can activate are `P5 ToolCall` candidates; and its optional `completionCondition` (a boolean expression evaluated each time an inner element completes, with `cancelRemainingInstances` (default `true`) controlling whether other active instances are terminated) is the closest existing termination mechanism in a pre-agentic standard.

What it does **not** provide is equally instructive: no `P13 Budget` primitive (Camunda's closest built-in guard is a configurable limit on model calls in the AI Agent connector); no machine-readable confidence signal on output; and, for the internally-handled implementation, elements are documented as unable to be activated dynamically **after** the sub-process is activated, only on entry. This RA treats the ad-hoc sub-process as proof that the container can be expressed in BPMN today, while treating budget, confidence, and mid-execution re-scoping as gaps this RA fills at the contract level rather than the notation level.

Four independent engineering organizations (Camunda, n8n, LangGraph, and Temporal), starting from four different notations and runtimes, converged independently on the same shape: a bounded container, a tool-attachment mechanism, and a durable-pause mechanism around a non-deterministic reasoning loop. That convergence is the strongest empirical evidence available that `P4 AgentStep` names a description of what production systems already needed to build, not an invention.

## Prior art

| System | Nearest equivalent |
| --- | --- |
| BPMN 2.0 | Ad-hoc sub-process, job-worker implementation |
| n8n | AI Agent node |
| AWS Step Functions | Task invoking an agent runtime |
| Temporal | Activity or child workflow |
| LangGraph | Subgraph / `create_react_agent` |

Nearest equivalent is editorial judgment, not a conformance claim.

## Relationship to other primitives

- [P5 ToolCall](p05-tool-call.md): the tool-scope allowlist's candidates.
- [P13 Budget](p13-budget.md): boundary contract element 5; enforced by the orchestrator, not requested in the prompt.
- [P14 OutcomeContract](p14-outcome-contract.md): the termination classification an `AgentStep` resolves to.
- [P6 HumanCheckpoint](p06-human-checkpoint.md): required in front of any `irreversible` tool, per tool scope.
- [P9 ErrorBoundary](p09-error-boundary.md): typed failure capture for the step, evaluated outside the model.
- [P19 EvaluationGate](p19-evaluation-gate.md): the machine-checkable predicate an iterating `AgentStep` evaluates its own output against, required whenever the step iterates against a checkable predicate.
- Identity & Trust WG: this RA requires that every `AgentStep` declare an identity/delegation attribute (contract element 7); the authentication mechanism, delegation protocol, and revocation model are that WG's domain.
- Accuracy & Reliability WG: this RA requires the output contract's confidence signal (contract element 3); how confidence is computed and how reasoning quality is evaluated is that WG's domain.

## Open questions

- How much of the `AgentStep` boundary contract can be expressed in BPMN `extensionElements` (as Camunda's `zeebe:adHoc` element does for activation configuration) versus requiring a new BPMN element altogether.
- Whether the supervisor role in the multi-agent RA's T1 topology is best modelled as a constrained instance of `P4 AgentStep`, or deserves to be a distinct primitive in its own right, given how central the "supervisor MAY be deterministic" variant is to that RA's default recommendation.
