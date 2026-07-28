# Start Here

Status: Index

## What this repository is

A proposal for how the Workflows and Process Integration workstream can organise and evolve a **workflow execution reference architecture**.

The central unit is the **workflow run**: one coordinated execution toward an intended outcome. A run may combine deterministic logic, model-assisted decisions, bounded agentic regions, multi-agent delegation, human tasks, waits, events, tools, and externally visible effects. None of these alone defines the run.

## What this repository is not

- a finished standard;
- a prescription for a particular workflow engine or agent framework;
- a claim that every section already has Working Group agreement;
- a complete catalogue of workflow patterns.

## Who it is for

| Audience | Enters through | Wants |
|---|---|---|
| Solution / platform architect | [Architecture principles](docs/architecture-principles.md) → [WDM][workflow-design-method] | Design a specific workflow |
| Workflow reviewer | [Architecture invariants](ra/01-foundations/architecture-invariants.md) → [Conformance](ra/07-readiness/conformance.md) | Assess an existing workflow |
| AI engineer building an assistant | [AI agent instructions](ra/08-lifecycle/ai-agent-instructions.md) → [registry.yaml](descriptor/registry.yaml) | Point an agent at the repo |
| WG contributor | [ROADMAP](ra/09-evolution/roadmap.md) → [decisions](ra/09-evolution/decisions/README.md) | See what is unfinished and why |

## The two modes

This repository is meant to be driven two ways, converging on the same **Workflow Design Specification (WDS)**.

### Human mode

```text
START-HERE
   ↓
Architecture principles
   ↓
Workflow Design Method
   ↓
Patterns
   ↓
Examples
   ↓
Design your workflow (produce a WDS)
```

### AI mode

Give an agent the repository plus a use case:

```text
Design workflow for: <use case>
Requirements: ...
```

and expect a quality WDS in return. The agent follows the same [Workflow Design Method][workflow-design-method] a human would.

## How to review this proposal

1. **Vision and structure** — is the information architecture useful? ([information architecture](docs/information-architecture.md))
2. **Foundational concepts** — are workflow run, authority, state, and effects the right centre? ([core concepts](ra/01-foundations/core-concepts.md))
3. **The method** — can a new use case be turned into a WDS using only this repository? ([WDM][workflow-design-method])
4. **Worked example** — does [invoice processing](examples/invoice-processing/README.md) demonstrate it end to end?

## Document status labels

- **Mature** — developed enough to support the current worked example; still open to WG change.
- **Proposal** — establishes purpose, scope, candidate structure, and open questions without a complete definition.
- **Index** — navigation only.

<!-- link definitions -->
[workflow-design-method]: ra/08-lifecycle/workflow-design-method.md
