# Workflow Execution Reference Architecture (WERA)

Workflows & Process Integration WG · Agentic AI Foundation

Status: Proposal snapshot (`v2-descriptor-driven`)

## What this is

A vendor-neutral reference architecture for **workflow execution**, organised around one central unit — the **workflow run** — spanning the full spectrum from fully deterministic automation, through model-assisted and hybrid workflows, to bounded-agentic and multi-agent execution.

It is **not** organised around "single-agent vs multi-agent." Agent count is one classification axis, not the organising principle.

## The one idea that makes this different

The whole repository is designed to have **two outputs that converge on the same result**:

```mermaid
flowchart TD
    BP[Business problem] --> RA[This reference architecture]
    RA --> HA[Human architect]
    RA --> AI[AI agent]
    HA --> WDS1[Workflow Design Specification]
    AI --> WDS2[Workflow Design Specification]
    WDS1 --> IMPL[Implementation]
    WDS2 --> IMPL
```

A **Workflow Design Specification (WDS)** is the artifact both a human and an AI agent produce by following the same method. In this repository the WDS is a machine-readable **workflow descriptor** (`*.wera.yaml`) plus its human-readable rendering.

### The acceptance test

The primary success criterion for this repository is **not** "is the document nice." It is:

> Can someone — human or AI — take a **new** use case and, using **only this repository**, produce a quality Workflow Design Specification?

If yes, the reference architecture works. If no, the problem is not "20 more pages of prose"; it is that the repository did not guide the user through the process. See [docs/acceptance-test.md](docs/acceptance-test.md).

## Two ways to use this repository

**Human mode** — read in this order:
[START-HERE](START-HERE.md) → [architecture principles](docs/architecture-principles.md) → [workflow design method](ra/08-lifecycle/workflow-design-method.md) → [patterns](ra/03-patterns/README.md) → [examples](examples/README.md) → design your workflow.

**AI mode** — point a coding agent at [`AGENTS.md`](../../AGENTS.md); it's the entry point. Run the agent in the repo, then either ask for a guided tour, or hand it your use case directly — described inline or as a file you already have:

```
Read AGENTS.md and give me a guided tour.
```
```
Read AGENTS.md. Here's my use case: <a few sentences>. Design me a solution.
```
```
Read AGENTS.md. My use case is in @path/to/use-case.md. Design me a solution.
```

The agent produces a full solution (a machine-readable WDS plus its human-readable design). The mechanics live in [examples/HOW-TO-RUN.md](examples/HOW-TO-RUN.md), but you don't need to reference it — `AGENTS.md` routes there for you.

## Repository map

| Area | Question it answers |
|---|---|
| [`docs/`](docs/README.md) | How do I read and review this repository? |
| [`ra/`](ra/README.md) | **The knowledgebase** — the reference architecture itself, in nine numbered chapters. |
| [`descriptor/`](descriptor/README.md) | How is a workflow captured as a machine-readable WDS? |
| [`examples/`](examples/README.md) | Worked examples (with their WDS outputs) that double as few-shot exemplars. |

Inside [`ra/`](ra/README.md), the nine chapters are:

| Chapter | Question it answers |
|---|---|
| [`01-foundations/`](ra/01-foundations/scope-and-boundaries.md) | What are the scope, concepts, principles, and non-negotiable rules? |
| [`02-architecture-model/`](ra/02-architecture-model/README.md) | What are the building blocks and how are they classified and combined? |
| [`03-patterns/`](ra/03-patterns/README.md) | What recurring problems have reusable solutions? |
| [`04-profiles/`](ra/04-profiles/README.md) | What coherent whole-run execution styles exist? |
| [`05-selection/`](ra/05-selection/README.md) | How do I choose the right patterns and profile? |
| [`06-overlays/`](ra/06-overlays/README.md) | What cross-cutting controls apply, and what belongs to other WGs? |
| [`07-readiness/`](ra/07-readiness/readiness-tiers.md) | When is a workflow production-ready and conformant? |
| [`08-lifecycle/`](ra/08-lifecycle/workflow-design-method.md) | How does a human or AI actually design a workflow? |
| [`09-evolution/`](ra/09-evolution/roadmap.md) | What is unfinished, and why were the important choices made? |

## Coded vocabulary

Every concept carries a stable code (design principles `DP-##`, invariants `INV-###`, primitives 3-letter mnemonics, patterns `WP##`, profiles `EP#`, overlays `OV-##` / external boundaries `XB-##`, readiness `RT#`, conformance `CL#`, and eight classification axes). The complete vocabulary is also published as machine-readable data in [`descriptor/registry.yaml`](descriptor/registry.yaml), so an AI agent can load the reference architecture as data rather than prose.

## Status & maturity

This is a proposal snapshot that uses **example-driven maturation**: the full structure exists, but only the concepts and patterns required by the current worked example ([invoice processing](examples/invoice-processing/README.md)) are marked **Mature**. Everything else is an explicit **Proposal** with open questions. See [ROADMAP.md](ra/09-evolution/roadmap.md).

## Working style

- Async first: use PR comments to discuss and converge.
- Fork-first: contributors work in a fork or branch and open PRs to the workstream branch.
- Keep drafts concise; use decision notes ([decisions/](ra/09-evolution/decisions/README.md)) when a choice needs recording.
- Use explicit "open questions" instead of blank sections.

## Links

- Charter (source of truth): [charter.md](../../charter/charter.md)
- WG repo: https://github.com/aaif/wg-workflows-and-process-integration
