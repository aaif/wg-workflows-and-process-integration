# P5 ToolCall

**Obligation:** MUST

## Definition

A `ToolCall` is an agent-initiated invocation of a capability outside the agent itself: an API call, a query, a file write, a command, a MCP invocation, OS system call.  Every `ToolCall` carries two declared attributes: the tool it invokes (which MUST appear on the step's tool-scope allowlist) and that tool's effect classification: `read_only`, `reversible_write`, or `irreversible`.

A `ToolCall` always returns control to the calling `AgentStep`. This is what distinguishes it from a [P16 Handoff](p16-handoff.md), which transfers responsibility and does not return.

## Why it exists

The argument runs in three steps.

**1. Governance needs an anchor.** The single-agent RA's central safety rule (no `irreversible` effect without a deterministic gate or a [P6 HumanCheckpoint](p06-human-checkpoint.md) in front of it) is only enforceable if there is a declared point at which effects occur. If tool use is an undifferentiated part of "the agent doing its thing," there is nothing for the allowlist to govern, nothing for effect classification to attach to, and no moment at which a gate could interpose. Naming the primitive is what creates the enforcement point.

**2. The effect classification must come from somewhere trustworthy.** Two candidates exist: the tool's own self-description, or the workflow's tool registry. Tool protocols let a server describe its own tools (including hints about whether a tool is destructive or read-only), so it is tempting to inherit the classification from the tool itself.

**3. The tool cannot be that authority, and the leading tool protocol says so itself.** The [MCP specification (2025-06-18)](https://modelcontextprotocol.io/specification/2025-06-18) states that tool descriptions and annotations from untrusted servers should be considered untrusted, and that MCP "itself cannot enforce these security principles at the protocol level." A protocol that explicitly declines to vouch for a server's self-description cannot be treated as vouching for it by whatever is built on top. So the classification MUST be asserted by the workflow's tool registry (populated by whoever configured the deployment, having verified out-of-band what each tool actually does) and MUST NOT be inferred at call time from server-supplied hints alone. A server's annotation is, at best, a hint the registry may consider; it is never the ruling.

This is why `P5` is a workflow-level primitive rather than a detail delegated to the tool protocol: the one party positioned to classify effects honestly is the workflow, and the classification is only enforceable at the boundary the workflow controls.

## Prior art

| System | Nearest equivalent |
| --- | --- |
| BPMN 2.0 | Activity inside the ad-hoc sub-process |
| n8n | Sub-node attached to the AI Agent via a typed tool connection |
| AWS Step Functions | No dedicated state: nested Task invoked by the agent runtime |
| Temporal | Activity invoked from within the `AgentStep`'s Activity/child workflow |
| LangGraph | Tool node |

Nearest equivalent is editorial judgment, not a conformance claim. MCP is deliberately absent from this table: it is the wire protocol a `ToolCall` will most often travel over, not an orchestration-level equivalent of the primitive. That is the same distinction the RA draws between a step and the transport beneath it.

## Relationship to other primitives

- [P4 AgentStep](p04-agent-step.md): the tool-scope allowlist (contract element 4) governs which `P5 ToolCall`s an agent may make.
- [P6 HumanCheckpoint](p06-human-checkpoint.md): required in front of any `irreversible` tool call, unless a deterministic policy gate substitutes for it.
- [P9 ErrorBoundary](p09-error-boundary.md): a failed tool call MUST NOT be retried by the agent itself; retry is orchestrator-owned.
- [P11 Compensation](p11-compensation.md): the undo path when a `reversible_write` tool call turns out to be wrong.
- [P16 Handoff](p16-handoff.md): the contrast case: a `ToolCall` returns to its caller, a `Handoff` transfers responsibility and does not.
- Security & Privacy WG: this RA emits the effect classification and identity/delegation scope as the surface their threat modelling operates on; it does not perform that analysis itself.
