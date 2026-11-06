# P4 ToolCall

**Obligation:** MUST \
**Used in patterns:** [Proposal/execution split](../patterns/proposal-execution-split.md) · [Bounded convergence loop](../patterns/bounded-convergence-loop.md)

## Definition

An agent-initiated call to a capability outside the agent, such as an API
call, a query, a file write, a command, or an MCP invocation. Every
`ToolCall` declares two things: the tool, which must be on the
`P3 AgentTask`'s allowlist, and the tool's effect class (`read_only`,
`reversible_write`, or `irreversible`).

A `ToolCall` always returns control to the `AgentTask` that made it.

## Why it exists

A rule like "no protected effect without approval" can only be enforced if
there is a defined point where agent effects happen. When tool use is just
part of whatever the agent does, an allowlist has nothing to attach to.

The effect class has to come from the workflow. The
[MCP specification (2025-06-18)](https://modelcontextprotocol.io/specification/2025-06-18)
says tool annotations from untrusted servers should be treated as untrusted,
and that MCP "itself cannot enforce these security principles at the protocol
level." So a server's description of its own tools is a hint at best. The
workflow's tool registry assigns the effect class, and whoever configures the
deployment is responsible for checking what each tool really does.

## How the patterns use it

- **Proposal/execution split.** Any tool that can cause the protected effect
  is kept out of the agent's scope, whatever its effect class. A
  `reversible_write` that goes straight to the protected system still causes
  the effect, so the registry records two facts per tool: its effect class,
  and whether it can reach the protected target. Only tools that can't are
  eligible. The agent can read and can write to draft or staging stores.
- **Bounded convergence loop.** The agent gets only the tools its bounded task
  needs, normally working in an isolated or non-authoritative area. A gate
  result that passes but touched something outside that scope still can't
  proceed.

Retrying a call that has side effects is the orchestrator's job
(`P7 ErrorBoundary`). The agent can see a tool error and change its approach.

## Implementation approaches (illustrative, not requirements)

| Runtime | Construct | Notes |
| --- | --- | --- |
| BPMN 2.0 | Activity inside the ad-hoc sub-process | |
| n8n | Tool sub-node attached to the AI Agent | |
| AWS Step Functions | No dedicated state; nested Task invoked by the agent runtime | |
| Temporal | Activity invoked from the agent's activity or child workflow | Gives each tool call its own retry policy and history entry |
| LangGraph | Tool node | |

MCP isn't in the table because it is the wire protocol a `ToolCall` often uses,
not an orchestration construct. None of these runtimes keeps an effect-class
registry. That is always the implementation's job.

## Relationship to other primitives

- [P3 AgentTask](p03-agent-task.md): its tool-scope allowlist (contract
  element 4) decides which calls the agent may make.
- [P2 DeterministicTask](p02-deterministic-task.md): performs protected effects
  instead.
- [P7 ErrorBoundary](p07-error-boundary.md): owns retries.
- [P12 AuditRecord](p12-audit-record.md): each call is recorded with its
  effect class.

## Open questions

- Where does the tool access layer end and the Identity & Trust WG's
  delegation work begin?
