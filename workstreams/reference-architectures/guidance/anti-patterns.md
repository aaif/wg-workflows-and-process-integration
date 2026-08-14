# Anti-patterns

The named failure patterns for single-agent and multi-agent workflows, merged into one document. None of the bullets below are literal duplicates across the two RAs, but several are the same failure showing up at a different scope: a single-agent problem that reappears, compounded, once a workflow crosses into multiple agents. Where that's true, the entries are cross-referenced rather than merged into one bullet, because the corrective action differs at each scope: "no budget" on one `AgentStep` and "no global ceiling" across several are both real, and both need naming.

## Single-agent

- **Agent as the top-level orchestrator, with the workflow inside it.** Inverts the ownership model in the [single-agent RA's Purpose](../architectures/single-agent.md); the workflow can no longer enforce budgets, gates, or audit from outside the model's own control flow, so every guarantee this RA specifies is lost.
- **Unbounded tool scope.** A denylist, or "grant access and see," means the workflow never classifies effect, so it never knows where to put a gate. Irreversible actions become reachable with no `HumanCheckpoint` in front of them.
- **No budget.** The characteristic agentic failure mode: iteration loops that terminate only when cost or time is exhausted in production, not by design. See also *Per-agent budgets with no global ceiling*, below: the multi-agent form of the same absence.
- **Confidence-free output.** Forces every downstream consumer to trust all `AgentStep` output equally, so the `Decision` primitive has nothing to route on. Outputs end up either always auto-completed or always escalated.
- **Retry logic inside the agent.** Agents retry non-idempotently and without the orchestrator's visibility; a failed tool call retried by the model can double-execute a `reversible_write`, or worse.
- **Irreversible tool with no gate.** The most consequential violation of the tool-scope contract ([element 4](../contracts/agent-step-boundary.md)). See also *A handoff that widens authority*, below: the same gap reappearing at a handoff boundary instead of at initial grant.
- **"The prompt is the guardrail."** The MCP specification itself states it "cannot enforce these security principles at the protocol level." A prompt is not enforcement either. It is a request the model MAY ignore, misread, or be steered around.

## Multi-agent

- **Agents negotiating instead of a declared `P18 ArbitrationPolicy`.** Consequence: disagreement is unbounded and the workflow has no guaranteed path to termination.
- **Per-agent budgets with no global ceiling.** Consequence: budgets compose multiplicatively across fan-out and handoffs; the actual total cost or risk exposure is unbounded even though every individual allocation looked reasonable. The single-agent scope of this same absence is *No budget*, above.
- **A handoff that widens authority.** Consequence: privilege escalation across exactly the boundary that was supposed to constrain it, and the escalation is invisible unless every handoff is individually audited. The single-agent scope of this same gap is *Irreversible tool with no gate*, above.
- **Recursive agent spawning without a depth limit.** Consequence: unbounded fan-out, budget exhaustion, and a workflow that cannot state in advance how many `AgentStep`s it might run.
- **A critic that is also the arbiter.** Consequence: the generator-critic loop has no independent check left in it, and its termination depends entirely on one agent's judgement rather than a declared rule.
- **Multi-agent chosen for organisational reasons inside a single trust boundary.** Consequence: the architecture mirrors the org chart rather than the actual coordination need, paying the full cost of multi-agent coordination for none of the four legitimate reasons.
- **Shared mutable context with no declared consistency model.** Consequence: write conflicts and stale reads silently corrupt shared state, and no one can say afterward which agent's write should have won.

## Related

- [Global invariants](global-invariants.md)
- [Failure modes](failure-modes.md)
- [Single-agent checklist](checklist-single-agent.md)
- [Multi-agent checklist](checklist-multi-agent.md)
- [`../contracts/agent-step-boundary.md`](../contracts/agent-step-boundary.md)
- [`../contracts/handoff.md`](../contracts/handoff.md)
