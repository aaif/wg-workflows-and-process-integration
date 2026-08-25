# Guidance

This directory holds the guidance that [`single-agent.md`](../architectures/single-agent.md) and [`multi-agent.md`](../architectures/multi-agent.md) both draw on. Most of these documents started as sections inline in one or both RA files; several were near-duplicated across the two. Extracting each argument into its own file here gives it one canonical home, and the two RAs link to that home instead of restating it, the same pattern already used for the primitive definitions in [`../../taxonomy/primitives/`](../../taxonomy/primitives/) and the two contracts in [`../contracts/`](../contracts/).

## Contents

- [Loop tiers](loop-tiers.md): the four nested cadences of continue-or-stop decision-making around an `AgentStep`, from the model's own reasoning loop up to a product-ownership decision, and why they must not share a budget or a termination condition.
- [Determinism hints](determinism-hints.md): a decision table for where to spend on an `AgentStep` and where a deterministic mechanism is strictly better, plus the one-line heuristic behind it.
- [Single-agent checklist](checklist-single-agent.md): the walkthrough for deciding whether a use case needs an `AgentStep` at all, and how many.
- [Multi-agent checklist](checklist-multi-agent.md): the walkthrough for deciding whether a workflow needs more than one `AgentStep`, and if so, which topology.
- [Anti-patterns](anti-patterns.md): the named failure patterns for single-agent and multi-agent workflows, in one place.
- [Global invariants](global-invariants.md): the seven properties every multi-agent topology MUST satisfy regardless of which one is chosen.
- [Failure modes](failure-modes.md): the multi-agent failure-mode table and the state of the empirical evidence for and against multi-agent architectures generally.
- [Boundaries with other working groups](wg-boundaries.md): the canonical statement of what this RA set emits to, and consumes from, each of the other AAIF working groups.
- [References](references.md): the consolidated reference list for the whole RA set, with a note on source quality.

## Related

- [`../architectures/single-agent.md`](../architectures/single-agent.md)
- [`../architectures/multi-agent.md`](../architectures/multi-agent.md)
- [`../README.md`](../README.md)
