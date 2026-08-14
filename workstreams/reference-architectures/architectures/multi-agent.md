# Multi-Agent Workflow

## Status

[`single-agent.md`](single-agent.md), which defines the shared primitive set `P1`–`P15` and the eight-element `P4 AgentStep` boundary contract. This document MUST NOT redefine any of `P1`–`P15` or the `AgentStep` contract; it references them throughout and adds exactly three new primitives (`P16 Handoff`, `P17 SharedContext`, `P18 ArbitrationPolicy`) that only become necessary once a workflow spans more than one `AgentStep`.

This document builds on the WG's [*Reference Architecture Proposal*](../../../Workflows-and-Processes-Reference-Architecture-Proposal.md) and is scoped by the [Working Group Charter](../../../charter/charter.md). Normative language is RFC 2119, per BCP 14.


**Multi-agent is a cost, not a feature.**

Every `AgentStep` added beyond the first introduces a coordination edge: a handoff, a piece of shared state, or a point where two agents' outputs must be reconciled. Every one of those edges is a place where a budget, an authority grant, or a termination guarantee can silently fail without anyone having designed for the failure. None of that cost buys anything on its own; it only pays for whatever crossing the agent boundary makes possible. The single-agent reference architecture in [`single-agent.md`](single-agent.md) SHOULD be the default topology for any workflow that needs agentic reasoning at all.

This document exists for the narrower set of cases where a single `P4 AgentStep` genuinely cannot do the job. Its most important job is not the topology catalog that follows. It is making the reader justify crossing the line from one agent to more than one.

There are four legitimate reasons to cross that line. If none applies to the workflow in front of you, stop here and return to `single-agent.md`; that is the most common correct outcome of reading this document.

1. **Context isolation**: the work does not fit inside one usable context window, or two subtasks would pollute each other's context if reasoned about together in a single `AgentStep`.
2. **Independent parallelism**: subtasks are genuinely independent of one another and latency to a combined result matters.
3. **Organisational or trust boundaries**: the agents are owned, operated, or authorised by different teams or different organisations, so they cannot be modelled as one `AgentStep` with one identity and one tool scope. This is the strongest reason, and the one where interoperability protocols such as A2A actually earn their existence: a peer-to-peer delegation protocol solves a real problem only when the peers do not share an orchestrator, a budget, or an identity provider.
4. **Heterogeneous capability or authority**: the subtasks genuinely require different tool scopes, different models, or different delegated authority that MUST NOT be merged into one grant. This is a security-adjacent argument as much as an architectural one: widening one agent's tool scope so a single `AgentStep` can cover work that actually needs two different authority levels is a privilege-escalation smell, not a simplification. Tool-scope and effect-classification risk of this kind is analysed in depth by the **Security & Privacy WG**; see the [OWASP Agentic Applications Top 10](https://owasp.org/www-project-agentic-skills-top-10/) as the relevant external reference. This document treats it as an interface, not a topic to resolve here.

If none of these four applies (if the real motivation on the table is that it "felt more natural" to give each concern its own agent), **the correct architecture is one `AgentStep` with a well-scoped tool set, not a multi-agent topology.**

The corollary: **"the agents will figure out how to coordinate" is not an architecture.** Every coordination edge in a multi-agent workflow MUST be a declared primitive (`P16 Handoff`, `P17 SharedContext`, or `P18 ArbitrationPolicy`) and MUST NOT be an emergent property of prompting two agents to cooperate. A workflow that cannot name which primitive governs a given coordination edge does not yet have an architecture at that edge.

## Structure

### Extra primitives

This RA adds exactly three primitives to the `P1`–`P15` set defined by [`single-agent.md`](single-agent.md): `P16 Handoff` ([definition](../../taxonomy/primitives/p16-handoff.md)), `P17 SharedContext` ([definition](../../taxonomy/primitives/p17-shared-context.md)), and `P18 ArbitrationPolicy` ([definition](../../taxonomy/primitives/p18-arbitration-policy.md)). Every multi-agent coordination edge this RA recognises is governed by one of these three; none of the topologies below requires a fourth.

### Topologies

Six topologies cover the multi-agent shapes this RA recognises, catalogued in [`topologies/README.md`](../topologies/README.md) with a diagram, a selection rule, a characteristic failure mode, and a deterministic-boundary statement for each. This is an index; the argument for each topology lives in its own file.

| Topology | Shape | Defined in |
|---|---|---|
| T1 | Supervisor / orchestrator-worker, the default | [t1-supervisor.md](../topologies/t1-supervisor.md) |
| T2 | Sequential pipeline with handoff | [t2-sequential-pipeline.md](../topologies/t2-sequential-pipeline.md) |
| T3 | Concurrent fan-out with deterministic join | [t3-concurrent-fan-out.md](../topologies/t3-concurrent-fan-out.md) |
| T4 | Peer network / cross-organisational delegation | [t4-peer-network.md](../topologies/t4-peer-network.md) |
| T5 | Shared-context / blackboard | [t5-shared-context.md](../topologies/t5-shared-context.md) |
| T6 | Generator-critic / evaluator-optimizer | [t6-generator-critic.md](../topologies/t6-generator-critic.md) |

`T1` SHOULD be the default: it keeps exactly one locus of control, and therefore exactly one place to enforce budget and termination. Choosing any of `T2`–`T6` instead should be a deliberate response to a specific characteristic of the work (staged output contracts, genuine independence, a cross-org boundary, a shared artifact, or an iterative quality loop), not a default in its own right.

### The handoff contract

`P16 Handoff` is this document's technical core: it transfers responsibility for a goal from one `AgentStep` to another, and, unlike a `ToolCall`, which always returns to its caller, the transferring step's obligations end at the moment of transfer. The seven elements every handoff MUST declare (goal transfer, context transfer, authority transfer, budget transfer, return contract, failure and timeout semantics, and audit continuity) are specified in full in [`contracts/handoff.md`](../contracts/handoff.md).

### Global invariants and failure modes

Independent of which topology a workflow uses, seven properties MUST hold: a single global budget ceiling, guaranteed termination, monotonic authority, reconstructable audit, deterministic arbitration, bounded fan-out, and a transitive irreversibility gate. These are the load-bearing claims of this RA; see [`guidance/global-invariants.md`](../guidance/global-invariants.md) for the full statement of each, and [`guidance/failure-modes.md`](../guidance/failure-modes.md) for the failure-mode table each invariant closes, plus the state of the empirical evidence for and against multi-agent architectures generally.

### Checklist, anti-patterns, and boundaries

[`guidance/checklist-multi-agent.md`](../guidance/checklist-multi-agent.md) is the numbered walkthrough for deciding whether, and how, to use this document. It routes the reader back to `single-agent.md` at step 2 more often than it proceeds past it. [`guidance/anti-patterns.md`](../guidance/anti-patterns.md) names this RA's failure patterns alongside the single-agent RA's. [`guidance/wg-boundaries.md`](../guidance/wg-boundaries.md) is the canonical statement of what this RA emits to, and consumes from, the **Security & Privacy WG**, the **Observability & Traceability WG**, the **Governance, Risk & Regulatory Alignment WG**, the **Accuracy & Reliability WG**, and the **Identity & Trust WG**.

## Interop layer

This RA maps `P1`–`P18` onto the open protocols this WG has agreed to build on, at the component level, and is explicit about where no such mapping exists yet.

**`P5 ToolCall` binds to MCP.** The [Model Context Protocol specification (2025-06-18)](https://modelcontextprotocol.io/specification/2025-06-18) states plainly that it cannot enforce its own security principles at the protocol level. Tool annotations from untrusted servers MUST NOT be relied upon as authoritative. The workflow, not the tool server, is therefore the authority on a tool call's effect classification and on what consent that classification requires; that governance MUST NOT be delegated to the tool server's self-description.

**`P16 Handoff` across organisational boundaries binds to A2A.** A2A is a project of the Linux Foundation, the same foundation umbrella under which AAIF itself was formed. Mapping this RA's `P14 OutcomeContract` classifications onto A2A's task lifecycle states is explicit WG follow-up work, not something this draft resolves.

**`P13 Budget` and `P18 ArbitrationPolicy` have no standard portable expression today.** Across the open specifications this RA builds on (BPMN 2.0, DMN, CMMN, MCP, and A2A) and across the workflow and agent runtimes referenced throughout this RA set, there is no shared, portable way to express a cross-agent budget ceiling or a deterministic arbitration rule that a workflow author could hand from one runtime to another. This is a concrete gap, and one this WG is specifically positioned to fill: a portable `P13`/`P18` representation would let a multi-agent workflow's budget ceiling and arbitration rule travel with the workflow definition across BPMN engines, MCP-tool-using agents, and A2A-delegated peers alike, instead of being reimplemented per runtime.

DMN decision tables are the natural existing mechanism for expressing the deterministic rule inside `P18 ArbitrationPolicy` where the rule is a bounded decision. The gap above is about the absence of a *cross-runtime, cross-agent* representation of the budget ceiling and the arbitration rule as first-class workflow constructs, not the absence of any deterministic-rule notation at all.

## Open questions

- Should `P14 OutcomeContract` classifications align directly to A2A task lifecycle states, or remain a separate vocabulary with an explicit mapping table?
- What would a portable, cross-runtime representation of `P13 Budget` look like, and could it be expressed as an extension to an existing standard (BPMN, MCP, A2A) rather than a new one?
- Does `P17 SharedContext` need one WG-standard consistency model, or should the RA only require that each workflow declare its own per-workflow model?
- How does audit correlation work across an organisational boundary when neither party trusts the other's log? Is a shared correlation identifier alone sufficient, or does this require a trust mechanism this WG does not own?
- Is the supervisor in `T1` best modelled as a constrained instance of `P4 AgentStep`, or does it deserve to be a distinct primitive in its own right given how central the "supervisor MAY be deterministic" variant is to this RA's default recommendation?

