# Core Workflow Terms

> **Status:** In Review — terms, definitions, and scope are subject to change as WG discussions progress.

This document defines the core vocabulary for agentic AI workflow concepts used across the Workflows and Process Integration Working Group. These terms provide a shared foundation for reference architectures, use cases, and interoperability specifications. The definitions are for reference only and would change in the near future.

---

## Foundational Concepts

### Workflow

A structured definition of work composed of one or more Steps, their relationships, and the logic required to achieve a defined goal or outcome.

### Workflow Step / Workflow Task

The atomic unit of work within a Workflow — a single, bounded task with defined inputs and outputs that the Workflow orchestrates and tracks to completion.

### Workflow Execution

A runtime instance of a Workflow definition. A single Workflow definition may have multiple concurrent Workflow Executions, each maintaining its own execution state and lifecycle.

### Workflow State

The information representing the current condition of a Workflow Execution at a specific point in time, including execution progress and data required to continue execution.

### Workflow Context

The shared information available to Workflow participants during execution that informs decision-making and execution across Steps and Workflow boundaries. Workflow Context may include inputs, metadata, shared data, execution history, configuration, and references to external resources.

---

## Execution & Control

### Control Flow

The logic that determines the order, conditions, branching, iteration, parallelism, and synchronization of Step execution within a Workflow.

### Trigger

An event, condition, signal, schedule, or request that initiates a Workflow Execution or causes a Workflow Execution to advance.

### Lifecycle

The sequence of execution states and transitions through which a Workflow Execution progresses from initiation to completion or termination.

### Durability

The capability of a Workflow Execution to preserve its execution state across failures or interruptions so that execution can continue without loss of progress.

### Determinism

The property by which a Workflow produces consistent execution behavior when provided the same inputs, execution state, and execution history.

---

## Coordination Models

### Orchestration

A coordination model in which a Workflow acts as the orchestrator — invoking Steps and participants, managing sequencing, and determining subsequent actions based on execution State and results.

### Choreography

A coordination model in which participants coordinate by reacting to Triggers based on their own logic, with sequencing and outcomes emerging from the event flow rather than being directed by an orchestrator.

### Composition

The construction of a Workflow from reusable components, including Workflow Steps/Tasks, sub-workflows, and other composable units. Composition defines how Workflows are organized while preserving the execution boundaries of each composed unit.

---

## Actors & Roles

### Role

A defined set of responsibilities, capabilities, or permissions assigned to a participant within a Workflow, independent of the participant's identity.

### Agent Card

Representation of an agent's self-declared capabilities intended for discovery and interaction with other agents. Does not contain governance-focused internals like models, tools, and sub-agents.

### Human-in-the-Loop

The pattern where a human holds a Role at a defined Step — as approver, reviewer, or decision-maker — before the Workflow continues. Structurally it is a Handoff subtype (agent → human → agent).

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
