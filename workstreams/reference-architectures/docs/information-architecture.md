# Information Architecture

Status: Mature

## Purpose

Explain why the repository separates foundations, model, patterns, profiles, selection, overlays, readiness, descriptor, playbook, examples, and decisions — and how those layers depend on each other.

## Layers

| Area | Question answered |
|---|---|
| `docs/` | How should readers understand, review, and navigate the repository? |
| `foundations/` | What are the scope, shared concepts, design principles, and non-negotiable invariants? |
| `model/` | What are the reusable building blocks, how are they classified, and how may they be combined? |
| `patterns/` | What recurring architectural problems have reusable solutions (`WP##`)? |
| `profiles/` | What coherent whole-run execution styles combine the concepts (`EP#`)? |
| `selection/` | How does a designer choose patterns and a profile (wizard questions, coordinates)? |
| `overlays/` | What cross-cutting controls apply (`OV-##`), and what belongs to other WGs (`XB-##`)? |
| `readiness/` | When is a workflow production-ready (`RT#`) and conformant (`CL#`)? |
| `descriptor/` | How is a workflow captured as a machine-readable WDS, and where is the coded vocabulary as data? |
| `playbook/` | How does a human or AI actually design and review a workflow? |
| `examples/` | How do the concepts work together in realistic cases, and how do they serve as few-shot exemplars? |
| `decisions/` | Why were important repository or architecture choices made? |

## Intended dependency direction

Examples depend on patterns, profiles, and core concepts. Patterns and profiles depend on the model and foundations. The foundations and model do not depend on any particular example, product, or runtime. The descriptor and registry encode the model; they do not extend it.

```mermaid
flowchart BT
    EX[Worked examples] --> PA[Patterns]
    EX --> PR[Profiles]
    EX --> MO[Model]
    PA --> MO
    PR --> MO
    MO --> FO[Foundations]
    SEL[Selection] --> PA
    SEL --> PR
    SEL --> MO
    OV[Overlays] --> MO
    RD[Readiness] --> MO
    DESC[Descriptor and registry] --> MO
    DESC --> FO
    PB[Playbook] --> SEL
    PB --> PA
    PB --> DESC
    DOC[Repository guidance] --> PB
    DOC --> EX
```

## The two outputs

The information architecture serves two consumers who must reach the same result.

```mermaid
flowchart LR
    R[Repository] --> H[Human architect]
    R --> A[AI agent]
    H --> W[Workflow Design Specification]
    A --> W
```

The [Workflow Design Method](../playbook/workflow-design-method.md) is the shared path; the [descriptor](../descriptor/README.md) is the shared artifact.

## Intentional incompleteness

Every document should be useful even when incomplete. Proposal-level documents contain purpose, scope, candidate structure, relationships, and open questions rather than empty headings or invented normative detail. Even proposal-level documents still carry their codes, so the [registry](../descriptor/registry.yaml) stays complete.
