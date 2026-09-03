# Core Workflow Terms

> **Status:** In Review — terms, definitions, and scope are subject to change as WG discussions progress.

This document defines the core vocabulary for agentic AI workflow concepts used across the Workflows and Process Integration Working Group. These terms provide a shared foundation for reference architectures, use cases, and interoperability specifications. The definitions are for reference only and would change in the near future.

---

## Foundational Concepts

### Activity

A single, bounded task with defined inputs and outputs that can be tracked to completion.

### Workflow

The primary unit of structured, multi-activity work with a defined goal and outcome. A Workflow is composed of one or more Activities, their relationships, and the logic required to achieve that goal or outcome.

### Workflow Execution

A runtime instance of a Workflow definition. A single Workflow definition may have multiple concurrent Workflow Executions, each maintaining its own execution state and lifecycle.

**Note:** this definition holds without modification for agentic Workflows, including where a Plan is created or revised mid-execution (see Plan) or an Activity is retried. Replanning and retry are transitions within a single Workflow Execution's Lifecycle (see Lifecycle), not the start of a new Workflow Execution — the Workflow Execution's identity persists across them. No change to the definition itself is proposed.

### Workflow State

The information representing the current condition of a Workflow Execution at a specific point in time, including execution progress and data required to continue execution.

### Workflow Context

The shared information available to Workflow participants during execution that informs decision-making and execution across Activities and Workflow boundaries. Workflow Context may include inputs, metadata, shared data, execution history, configuration, and references to external resources.

---

## Execution & Control

### Control Flow

The logic that determines the order, conditions, branching, iteration, parallelism, and synchronization of Activity execution within a Workflow.

**Note:** this definition is agnostic to when or how that logic is evaluated — it may be fixed at design time, or determined dynamically at runtime, for example by an agent's own reasoning about which Activity to perform next. The latter case is still Control Flow in the sense defined here; which participant or mechanism is doing the determining is Orchestration's concern, not Control Flow's — Orchestration already covers an orchestrator "determining subsequent actions based on execution State and results." No change to either definition is proposed; this note exists only to make an ambiguity explicit before "logic that determines" gets read as implying a static, pre-authored structure.

### Trigger

An event, condition, signal, schedule, or request that initiates a Workflow Execution or causes a Workflow Execution to advance.

### Lifecycle

The sequence of execution states and transitions through which a Workflow Execution progresses from initiation to completion or termination.

### Durability

The capability of a Workflow Execution to preserve its execution state across failures or interruptions so that execution can continue without loss of progress.

### Determinism

The degree to which a Workflow Execution, or a specific layer of a Workflow Execution such as its Control Flow or an individual Activity, produces the same execution behavior given the same inputs, execution state, and execution history.

**Note:** Determinism is a property of a specific layer of a Workflow, not necessarily of the Workflow as a whole — a Workflow may be deterministic in its Control Flow (the same branch taken, the same next Activity selected, the same synchronization point reached) while containing Activities, particularly LLM-driven ones, whose individual outputs vary across otherwise identical executions. This definition deliberately says nothing about how Determinism is measured, scored, or evaluated; that is a separate question for whichever group or specification takes it up. For grounding only, not as an endorsement of any particular approach: AVE, an external behavioral-vulnerability taxonomy for agentic components, already scores `non_determinism` as one of ten factors contributing to its severity scoring, defined there simply as "behavioral variability across runs" — evidence that treating Determinism as graded and layer-specific, rather than binary and Workflow-wide, is already load-bearing in at least one adjacent specification.

---

## Coordination Models

### Orchestration

A coordination model in which a Workflow acts as the orchestrator — invoking Activities and participants, managing sequencing, and determining subsequent actions based on execution State and results.

### Choreography

A coordination model in which participants coordinate by reacting to Triggers based on their own logic, with sequencing and outcomes emerging from the event flow rather than being directed by an orchestrator.

### Composition

The construction of a Workflow from reusable components, including Activities, sub-workflows, and other composable units. Composition defines how Workflows are organized while preserving the execution boundaries of each composed unit.

---

## Actors & Roles

### Role

A defined set of responsibilities, capabilities, or permissions assigned to a participant within a Workflow, independent of the participant's identity.

### Agent Card

Representation of an agent's self-declared capabilities intended for discovery and interaction with other agents. Does not contain governance-focused internals like models, tools, and sub-agents.

### Human-in-the-Loop

The pattern where a human holds a Role at a defined Activity — as approver, reviewer, or decision-maker — before the Workflow continues. Structurally it is a Handoff subtype (agent → human → agent).

---

## Cross-cutting

### Discovery

The process by which an agent, user, or system finds available agents, services, capabilities, identities, or trust information.

### Handoff

The explicit transfer of responsibility, execution context, state, or authority from one participant, Workflow, or execution unit to another.

**Note (2026-09-03):** Handoff is jointly listed under Workflows & Process Integration, Observability & Traceability, and Governance, Risk & Regulatory Alignment in the central taxonomy landscape, with its definition marked "pending — term accepted; definition under working group discussion" as of this note. A candidate definition has been proposed from this group via `aaif/ws-taxonomy-landscape#55` (open, not yet merged): "The transfer of responsibility for continuing an Activity, Workflow segment, or Workflow from one participant to another, together with the relevant State, Context, or information needed to continue execution. A Handoff concerns continuation of work. It does not by itself imply transfer of authorization, accountability, or broader authority." That wording is not reflected above, deliberately: it has not yet been reviewed by Observability & Traceability or Governance, and this document should not get ahead of that agreement.

A definition informally attributed to Observability & Traceability — "the observable boundary at which work, context, or results move between actors" — was checked directly against that group's own repository and does not exist there as a committed definition; only passing charter-level mentions of "hand-offs" as an in-scope tracing concern were found, with no standalone term entry. There is therefore no real, citable collision between two written definitions to reconcile right now. The underlying concern is still worth raising proactively, since it describes a real difference in vantage — this group's framing names the transfer itself (who now holds responsibility), while the informally-reported Observability framing would name the point at which that transfer becomes visible in a trace. The two seem complementary rather than competing, once Observability puts something in writing. Recommend Observability & Traceability review `#55` directly rather than defining Handoff independently, given the term is already jointly claimed by three groups.

### Plan

A structured representation of intended actions, dependencies, constraints, or objectives that guides Workflow Execution. A Plan may be created before execution begins or modified during execution.

### Dry Run

A mode of Workflow Execution that validates or simulates execution behavior without committing external side effects or permanently modifying managed resources.
