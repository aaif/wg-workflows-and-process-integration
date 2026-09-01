*DRAFT STATUS: THIS HAS NOT YET BEEN ALIGNED WITH REF ARCH WORKSTREAM*

# Agentic Use Cases Landscape: Proposed Classification Schema

**Agentic AI Foundation · Workflows & Process Integration Working Group · Critical Use Cases Workstream**

This documents a proposed way to describe agentic workflows consistently, so use cases across industries can be compared and built against. Applied to the workflows in the companion [Use Case Inventory](./use-case-inventory.md) file, which links back here for every definition it uses.

This is a starting point, not a closed spec. If a real workflow doesn't fit (a missing dimension, a missing value, a different way to draw a line), propose the change. See [Open questions](#open-questions) for what's already on the table. 

**This work needs to be aligned with the Working Group output from the Reference Architecture Workstream.**

---

## Contents

- [How to Use This Document](#how-to-use-this-file)
- [Classification](#classification): the dimensions and how they relate
- [Schema summary](#schema-summary): all fields and allowed values, one table each
- [Open questions](#open-questions)
- [Classifying a row](#classifying-a-row)

---

## How to Use This Document

**Classifying a use case:** read [Classification](#classification), then [Classifying a row](#classifying-a-row) for what to do when the source material doesn't say enough.

**Browsing classified use cases:** go to the [Use Case Inventory](./use-case-inventory.md) and jump to a category. Every row is tagged with the dimensions defined here.

**Lower-level detail** (tool invocation, state/context handoff, guardrail enforcement, and similar building blocks) is out of scope here. See the [Workflow Reference Architecture](#).

---

## Classification

**Twelve columns total. Five are proposed as classification dimensions; the rest describe or support a row.**

A classification dimension marks a structural choice: something a workflow's design settles one way or another, not just a fact true of one implementation. Proposed dimensions:

- **Trigger.** What starts execution: something happening in an external system, a recurring schedule, or a person directly asking.
- **HITL Pattern.** Where, if anywhere, a person has to act before the workflow can proceed.
- **Agent Count.** How many separate reasoning agents the workflow uses, and why: task complexity is one reason to split, but so is using a different model per agent, giving agents different or narrower tool access, or other deliberate separation.
- **Coordination.** Once there's more than one activity or more than one agent, who decides what happens next: fixed code following a script, or an LLM reasoning about it at runtime.
- **Workflow Pattern.** The shape execution actually takes once it's running: a straight line, concurrent branches that merge back together, or a loop that keeps retrying against a gate until it passes.

Each should describe something the others don't. If two seem to overlap, or a workflow needs a sixth, that's an [open question](#open-questions) to raise, not a reason to force a fit.

The other seven columns are supporting fields, not dimensions. A dimension has a small, fixed set of values because it names a real fork in how the workflow is built. These seven don't have that property:

- **Duration** is measured, not chosen: how long one implementation happened to take, observed after the fact rather than decided in the design. Two systems with identical dimension values can land at very different durations.
- **Use Case, Description, Tools & Systems** identify and describe the row. Free text.
- **Key Failure Mode, Preconditions, Notes** carry rationale and evidence. Free text.

**Each row is classified against its own cited implementation, not its use case name.** Two rows can share a name and still get different values. Check a row's own Notes before assuming consistency across rows.

### Duration

Agent execution time only, not time spent waiting in a human queue or on downstream processing.

### Trigger

- **`Event`.** Something happens in an external system: a record is created, a threshold is crossed, a file arrives.
- **`Scheduled`.** A recurring cadence, whether or not there's something to act on that cycle.
- **`User`.** A person asks directly.

### HITL Pattern

The primary gate in the critical path: the one that blocks progress, not an optional review someone could choose to do.

- **`None`.** No mandatory checkpoint.
- **`Exception escalation`.** Runs autonomously by default; a person is pulled in only when confidence runs out, or before one specific irreversible activity.
- **`Approval gate`.** A person acts before a point every run reaches. Covers three sub-cases (transactional, content review, formal sign-off); note which one applies in the row's Notes.

### Agent Count and Coordination

Two separate questions. Default to the simpler answer when in doubt.

**Agent Count:** does the task need more than one agent?

- **`Single-agent sufficient`.** One agent handles it well.
- **`Better as multi-agent`.** Not required, but a split demonstrably helps: a writer/critic pair, independent verification, a different model per agent, or giving each agent a different or narrower set of tools than the others.
- **`Inherently multi-agent`.** Either a single agent's context/tools/execution would degrade the result, or correctness requires certain roles to stay structurally separate (an independent fact-checker, an isolated policy gate).

**Coordination:** is the next activity predetermined, or decided by an LLM at runtime?

- **`Fixed/scripted`.** Deterministic code decides.
- **`Single-agent, orchestrated`.** One agent running a dynamic, ReAct-style loop. Only applies with `Single-agent sufficient`.
- **`AI-coordinated, routing`.** A supervisor delegates at runtime, no multi-activity plan.
- **`AI-coordinated, planning`.** A supervisor builds and revises a plan.
- **`Swarm/peer-to-peer`.** Decentralized, all-to-all. Not seen in the inventory yet.
- **`n/a`.** Single agent, no dynamic loop.

A single agent can be fixed or dynamic; a multi-agent system can be scripted or AI-coordinated. Neither field determines the other.

### Workflow Pattern

Four shapes proposed so far, checked in order, first match wins. Likely not a complete list, so flag anything that doesn't fit.

1. **`Convergence loop`.** Iterates against a deterministic gate until it passes or escalates.
2. **`Parallel fan-out`.** Concurrent sub-tasks, merged into one result.
3. **`Sequential pipeline`.** Dependent activities, each feeding the next.
4. **`Atomic action`.** None of the above; one indivisible activity.

`Atomic action` is the one value that implies anything else: an indivisible activity can't be multi-agent or dynamically coordinated, so `Agent Count = Single-agent sufficient` and `Coordination = n/a` follow automatically. No other Workflow Pattern value implies anything about Agent Count or Coordination. `Sequential pipeline` and `Parallel fan-out` are both silent on fixed vs. dynamic; that's Coordination's job.

### Scope and limits of the dimensions

**Use.** Read a row's five values and you know its trigger, HITL gate, agent count, coordination, and processing shape, without reading the whole row. That's what these dimensions are for: comparing use cases within this inventory.

**Limits**. They don't define a workflow's full architecture. That also includes boundaries, guarantees, exit states, tool integrations, and task logic, none of which any of the five dimensions capture. Whether any of these or other items should become their own dimension is an open question. Not every combination of the five values is even valid (see the `Atomic action` and `Single-agent, orchestrated` constraints above).

**Goal.** Treat these five as descriptive inventory metadata today. That's where things stand, not the goal. These were derived bottom-up from real deployments specifically so they could inform, and eventually converge with, whatever primitives the Reference Architecture selects top-down, whether that means adopting theirs, contributing pieces to theirs, both changing, or this list shrinking once checked against real definitions. Five isn't guaranteed to be the final number either way. 

See [open question](#open-questions).

---

## Schema summary

### Classification dimensions

| Dimension | Description | Allowed values |
|---|---|---|
| **Trigger** | What starts execution | • `Event`<br>• `Scheduled`<br>• `User` |
| **HITL Pattern** | Where a person has to act | • `None`<br>• `Exception escalation`<br>• `Approval gate` |
| **Agent Count** | How many agents the workflow uses, and why | • `Single-agent sufficient`<br>• `Better as multi-agent`<br>• `Inherently multi-agent` |
| **Coordination** | Scripted vs. decided at runtime | • `Fixed/scripted`<br>• `Single-agent, orchestrated`<br>• `AI-coordinated, routing`<br>• `AI-coordinated, planning`<br>• `Swarm/peer-to-peer`<br>• `n/a` |
| **Workflow Pattern** | The processing shape, checked in priority order | • `Convergence loop`<br>• `Parallel fan-out`<br>• `Sequential pipeline`<br>• `Atomic action` |

### Supporting fields

Filled in per-row in the [Use Case Inventory](./use-case-inventory.md).

| Field | Description | Allowed values |
|---|---|---|
| **Use Case** | Short name | Free text |
| **Description** | What triggers it, what it does, what it produces | Free text |
| **Tools & Systems** | External systems read from or written to | Free text; separate with `;` |
| **Duration** | Agent execution time only | • `Instant` (< 1 min)<br>• `Short` (1–30 min)<br>• `Long` (hours–days) |
| **Key Failure Mode** | Most likely way this fails or causes harm | Free text; be specific |
| **Preconditions** | What has to be true beforehand for the HITL pattern to be safe | Free text |
| **Notes** | Sources, rationale, caveats | Free text |

---

## Open questions

Add to this list as new questions surface. Record the resolution here rather than deleting the entry once one's settled; the reasoning is worth keeping.

### Should `Tools & Systems` be a dimension?

Integration count and read/write access shape what gets built (credential scoping, write-path safeguards) arguably as much as the other five do, but currently sit in Supporting fields as free text. Not resolved; worth reviewing alongside the Workflow Reference Architecture.

### `Decentralized handoff`: possible Coordination value

For agents that hand off control to each other with no central coordinator and no all-to-all structure (Azure's Handoff / Group-chat patterns). Checked against three candidate rows in the inventory (Runbook-guided remediation, Ticket triage & routing, Bug triage from logs); none clearly needed it, but the case for adding it isn't closed.

### Where does model selection happen?

Not captured by any dimension today. Which model runs a given activity, and who chooses it, is a separate question from Coordination (which is about what runs next, not which model does it): a fully `Fixed/scripted` pipeline can still use different models per phase if that's set by config rather than decided by a reasoning activity. Using multiple models isn't on its own grounds for `AI-coordinated`.

This matters because model choice per phase is now a real, cost-driven design decision in production pipelines (cheap model for triage, escalate to a stronger one on failure or risk), and two rows can look identical on every other dimension while behaving very differently on cost and quality depending on how the model is chosen. Broader model infrastructure stays with the Reference Architecture; this is narrower.

Three candidate cases proposed:

* **Pinned.** One model, fixed by the workflow's author.
* **Gateway-routed.** An upstream broker picks the model per call, possibly across vendors.
* **Model-native.** A single vendor's endpoint routes within its own model family. Not broadly available yet.

Not resolved. Leaning toward a Notes convention (e.g. `routing: gateway (cross-brand)`) rather than a new column, promoting to a column only if enough rows end up using it.

---

## Classifying a row

### Documenting rationale

Every value should have a reason in Notes (e.g., why `Better as multi-agent` helps here specifically). If the value seems right but the rationale isn't written down yet, keep the value and footnote it rather than downgrading to Unspecified: ¹ Needs confirmation. Rationale not yet documented.

Reuse the same footnote number for every cell in a table with the same kind of gap.

### When source material doesn't say enough

If a cited source describes what a workflow does but not enough to choose a value confidently (e.g., whether three reads happen concurrently or in sequence), write **Unspecified: insufficient source detail** rather than guessing, and add a line in Notes naming the gap.

---

*Schema only. For the use cases classified against it, see the [Use Case Inventory](./use-case-inventory.md).*
