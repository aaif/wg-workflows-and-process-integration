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

**Note:** this definition holds without modification for agentic Workflows, including where a Plan is created or revised mid-execution (see Plan) or an Activity is retried. In the common case, replanning and retry are treated as transitions within a single Workflow Execution's Lifecycle (see Lifecycle) rather than the start of a new one, so the Workflow Execution's identity persists across them. This depends on how a given system defines execution identity, and is not asserted here as the only valid model.

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

**Note:** Determinism can apply at the level of the overall Workflow Execution or at the level of a specific layer or component within it, such as its Control Flow or an individual Activity — a Workflow may be deterministic in its Control Flow (the same branch taken, the same next Activity selected, the same synchronization point reached) while containing Activities, particularly LLM-driven ones, whose individual outputs vary across otherwise identical executions. This definition deliberately says nothing about how Determinism is measured, scored, or evaluated; that is a separate question for whichever group or specification takes it up.

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

### Plan

A structured representation of intended actions, dependencies, constraints, or objectives that guides Workflow Execution. A Plan may be created before execution begins or modified during execution.

### Dry Run

A mode of Workflow Execution that validates or simulates execution behavior without committing external side effects or permanently modifying managed resources.
