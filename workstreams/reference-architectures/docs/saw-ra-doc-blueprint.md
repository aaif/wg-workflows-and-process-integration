# SAW-RA Documentation Blueprint
## Discussion Draft


> **Status:** Draft for RA WS Team Review
>
> This document is **not** the Single-Agent Workflow Reference Architecture (SAW-RA).
>
> It is a proposal for **how the future reference architecture should be organized**.

## Contents

- [1. Purpose of this Blueprint](#1-purpose-of-this-blueprint)
- [2. How to Use this Blueprint](#2-how-to-use-this-blueprint)
- [3. Expected Review Outcome](#3-expected-review-outcome)
- [4. Guiding Questions](#4-guiding-questions)
- [5. Proposed SAW-RA Documentation Structure](#5-proposed-saw-ra-documentation-structure)
  - [5.1 Foundations](#51-foundations)
    - [0. Start Here](#0-start-here)
    - [1. Scope and Boundaries](#1-scope-and-boundaries)
    - [2. Core Concepts](#2-core-concepts)
    - [3. Design Principles](#3-design-principles)
    - [4. Architecture Invariants](#4-architecture-invariants)
  - [5.2 Architecture Model](#52-architecture-model)
    - [5. Reference Model](#5-reference-model)
    - [6. Primitive Catalog](#6-primitive-catalog)
    - [7. Runtime Components](#7-runtime-components)
    - [8. Composition Rules](#8-composition-rules)
  - [5.3 Patterns and Selection](#53-patterns-and-selection)
    - [9. Pattern Classification](#9-pattern-classification)
    - [10. Pattern Selection](#10-pattern-selection)
    - [11. Pattern Catalog](#11-pattern-catalog)
  - [5.4 Enterprise Readiness](#54-enterprise-readiness)
    - [12. Enterprise Control Overlays](#12-enterprise-control-overlays)
    - [13. Enterprise Readiness](#13-enterprise-readiness)
  - [5.5 Workflow Lifecycle](#55-workflow-lifecycle)
    - [14. Designing a New Workflow](#14-designing-a-new-workflow)
    - [15. Assessing an Existing Workflow](#15-assessing-an-existing-workflow)
    - [16. Required Workflow Architecture Documentation](#16-required-workflow-architecture-documentation)
    - [17. Testing and Evaluation](#17-testing-and-evaluation)
    - [18. Operations and Lifecycle](#18-operations-and-lifecycle)
    - [19. Governance and Conformance](#19-governance-and-conformance)
  - [5.6 Evolution and Supporting Material](#56-evolution-and-supporting-material)
    - [20. Evolution Roadmap](#20-evolution-roadmap)
    - [Appendices](#appendices)

---

# 1. Purpose of this Blueprint

Before creating a reference architecture, the team should first agree on **how the architecture will be documented**.

This blueprint proposes a structure that is intended to:

- be understandable to both technical and non-technical audiences
- support designing new workflows
- support assessing existing workflows
- encourage reusable workflow patterns rather than use-case-specific designs
- evolve over time without restructuring the entire document

The outcome of reviewing this blueprint should be agreement on the overall documentation structure rather than detailed technical decisions.

---

# 2. How to Use this Blueprint

For this review, focus on the proposed documentation structure; detailed implementation choices can be addressed later.

Use the following questions to guide your feedback:

- Does each proposed section belong?
- Are any important topics missing, unnecessary, or better moved elsewhere?
- Is the purpose of each section clear?
- Is the document organized and named intuitively, so future readers can find the information they need?
- Should any topic become its own document or companion guidance?
- Which sections are essential for the first release, and which can wait until later?
- Is the document understandable for both technical and non-technical audiences?

---

# 3. Expected Review Outcome

The review should result in agreement on:

- The overall structure of SAW-RA.
- Any missing or unnecessary sections.
- The terminology used throughout the document.
- Which topics belong in the core reference architecture.
- Which topics belong in companion guidance documents.
- Priorities for developing the first complete version of SAW-RA.

Once we reach this agreement, we can start writing the detailed reference architecture itself.

---

# 4. Guiding Questions

The following questions shaped the proposed structure. They represent the problems the architecture should help answer.

| ID | Question | Why this question exists | Comment |
|---|---|---|---|
| Q1 | What is this architecture trying to achieve? | Every reference architecture should have a clearly defined purpose. Readers should understand why the architecture exists before learning how it works. | |
| Q2 | What concepts must every reader understand first? | People from different backgrounds use different terminology. The architecture should establish a shared vocabulary before discussing patterns or implementation. | |
| Q3 | What reusable building blocks exist? | Reusable building blocks encourage consistency and reduce duplication. Different workflows should be assembled from the same set of primitives. | |
| Q4 | How are those building blocks combined? | The architecture should define approved ways of composing primitives rather than allowing every workflow to invent its own structure. | |
| Q5 | How should the responsible architect or review team choose the right combination? | Pattern selection needs a clear decision owner and a repeatable method. Machine-readable guidance could help both people and AI assistants apply the same questions while keeping human accountability clear. | |
| Q6 | How do we know a workflow is enterprise ready? | Enterprise readiness should be measurable. The architecture should define the controls and evidence expected before a workflow reaches production. | |
| Q7 | How should this architecture evolve over time? | The architecture should support future workflow patterns, machine-readable guidance, and eventually multi-agent workflows without requiring a complete redesign. | |

---

# 5. Proposed SAW-RA Documentation Structure

Every proposed SAW-RA section should exist because it helps answer one or more of the Guiding Questions above.

If a section cannot be linked to at least one Guiding Question, we should question whether it belongs in the reference architecture.

The sections are grouped into six themes to make the overall structure easier to scan. The **Comments** column is reserved for review feedback.

## 5.1 Foundations

These sections explain the purpose, scope, language, and non-negotiable rules of SAW-RA.

| Section | Purpose | Why this section exists | Future Contents | Helps Answer | Comments |
|---|---|---|---|---|---|
| **0. Start Here** | Introduce the reference architecture and help readers quickly understand what it is, who it is for, and how to use it. | Readers need a quick way to judge whether the document is relevant and where to begin. The table of contents supports quick browsing, while reading paths guide different audiences to the sections most useful to them. | Table of contents<br>Purpose<br>Audience<br>Role-based reading paths<br>Pattern selector overview<br>Document conventions | Q1<br>Q2 | |
| **1. Scope and Boundaries** | Clearly define what SAW-RA covers and what it intentionally leaves outside its scope. | Readers should understand the difference between architectural guidance and implementation guidance. | Scope<br>Non-goals<br>Level of abstraction<br>Relationship to implementation guidance<br>Relationship to future multi-agent architecture | Q1 | |
| **2. Core Concepts** | Introduce the common terminology used throughout the document. | Using consistent language reduces misunderstandings between architects, developers, and business stakeholders. | Definitions<br>Terminology<br>Core concepts<br>Key relationships | Q2 | |
| **3. Design Principles** | Describe the high-level principles that influence every architectural decision. | Readers should understand the thinking behind the architecture before learning detailed rules. | Design principles<br>Architectural philosophy<br>Guiding ideas | Q1 | |
| **4. Architecture Invariants** | Define the rules that should never be violated. | These rules create consistency across every workflow regardless of technology or business domain. | Mandatory rules<br>Architectural constraints<br>Trust boundaries<br>Consistency requirements | Q4<br>Q6 | |

## 5.2 Architecture Model

These sections define the overall workflow model, its reusable building blocks, and how those blocks can be combined.

| Section | Purpose | Why this section exists | Future Contents | Helps Answer | Comments |
|---|---|---|---|---|---|
| **5. Reference Model** | Provide the "big picture" of a single-agent workflow. | Readers should understand the overall architecture before learning individual building blocks. | Logical architecture<br>Major architectural areas<br>Trust boundaries<br>High-level workflow | Q2 | |
| **6. Primitive Catalog** | Describe the reusable workflow building blocks. | Every workflow should be assembled from a common set of approved primitives. | Primitive definitions<br>Responsibilities<br>Inputs and outputs<br>Relationships | Q3 | |
| **7. Runtime Components** | Describe the logical runtime capabilities required to implement the primitives. | Logical building blocks should remain independent from specific products or technologies. | Runtime capabilities<br>Logical services<br>Component responsibilities | Q3 | |
| **8. Composition Rules** | Describe how primitives can be safely combined into complete workflows. | Without composition rules, different teams may build inconsistent solutions using the same primitives. | Composition rules<br>Invalid combinations<br>Workflow grammar<br>Control-flow guidance | Q4 | |

## 5.3 Patterns and Selection

These sections explain how patterns are grouped, how a pattern is selected, and where each approved pattern is defined.

| Section | Purpose | Why this section exists | Future Contents | Helps Answer | Comments |
|---|---|---|---|---|---|
| **9. Pattern Classification** | Explain how workflow patterns are grouped into clear families. | A consistent classification helps readers understand the landscape of available patterns before choosing one. Patterns should be grouped by architectural characteristics rather than business use cases. | Pattern families<br>Classification criteria<br>Relationships between pattern families | Q4 | |
| **10. Pattern Selection** | Help the responsible architect or review team choose the most appropriate workflow pattern. | Pattern selection should follow a repeatable decision process rather than personal preference. Machine-readable guidance may guide users through the same questions and explain its recommendation, while the accountable person or team retains the decision. | Decision owner<br>Selection questions<br>Decision flow<br>Recommendation and rationale<br>Human-readable guidance<br>Machine-readable decision logic<br>Future machine-readable guidance interface | Q5 | |
| **11. Pattern Catalog** | Define each approved workflow pattern in a consistent format. | The catalog is where readers find the detailed description of a selected pattern, including how it is composed and when it should be used. | Pattern intent<br>When to use<br>Primitive composition<br>Required controls<br>Variations<br>Related patterns | Q4<br>Q5 | |

## 5.4 Enterprise Readiness

These sections define reusable enterprise requirements and explain how readiness is measured.

| Section | Purpose | Why this section exists | Future Contents | Helps Answer | Comments |
|---|---|---|---|---|---|
| **12. Enterprise Control Overlays** | Describe reusable governance, security, reliability, and operational requirements that can apply across multiple workflow patterns. | Common requirements should be defined once and reused instead of being repeated inside every pattern. | Security overlays<br>Governance overlays<br>Reliability overlays<br>Operational overlays | Q6 | **Open terminology question:** Is "Enterprise Control Overlays" the most intuitive name for this concept?<br><br>Alternative names to discuss:<br>- Architecture Traits<br>- Cross-Cutting Concerns<br>- Enterprise Profiles |
| **13. Enterprise Readiness** | Define what "enterprise ready" means and how it is measured. | Production readiness should be based on consistent criteria and evidence rather than opinion. | Readiness tiers<br>Measurable criteria<br>Required evidence<br>Production checklist<br>Assessment approach | Q6 | |

## 5.5 Workflow Lifecycle

These sections explain how SAW-RA is used to design, document, assess, test, operate, and govern workflows.

| Section | Purpose | Why this section exists | Future Contents | Helps Answer | Comments |
|---|---|---|---|---|---|
| **14. Designing a New Workflow** | Provide a repeatable process for designing a new workflow using SAW-RA. | The architecture should be usable as a practical design guide rather than only as documentation. | Design process<br>Decision points<br>Pattern selection<br>Validation steps | Q5 | |
| **15. Assessing an Existing Workflow** | Provide a structured approach for analysing and improving an existing workflow. | Many organizations already have AI workflows and need guidance on making them enterprise ready. | Assessment process<br>Gap analysis<br>Pattern mapping<br>Improvement recommendations | Q5<br>Q6 | |
| **16. Required Workflow Architecture Documentation** | Define the diagrams, views, and supporting documentation expected for every workflow, including the documentation required as evidence for enterprise readiness and conformance. | Clear naming makes it explicit that this section defines documentation requirements. Consistent documentation makes reviews, handovers, and maintenance easier. | Required diagrams<br>Required architecture views<br>Supporting descriptions<br>Documentation standards<br>Templates | Q2<br>Q6 | |
| **17. Testing and Evaluation** | Describe how workflow quality should be verified. | Enterprise workflows require more than functional testing. Quality, safety, and reliability should also be evaluated. | Testing strategy<br>Evaluation approach<br>Acceptance criteria | Q6 | |
| **18. Operations and Lifecycle** | Describe how workflows are deployed, monitored, maintained, and improved. | The architecture should remain useful after deployment, not only during design. | Monitoring<br>Operations<br>Versioning<br>Change management<br>Continuous improvement | Q6<br>Q7 | |
| **19. Governance and Conformance** | Define how compliance with SAW-RA is assessed. | A reference architecture is most useful when there is a consistent way to determine whether a workflow follows it and how exceptions are handled. | Conformance process<br>Exceptions<br>Architecture reviews<br>Required evidence | Q6 | |

## 5.6 Evolution and Supporting Material

These sections explain how SAW-RA can grow and where supporting material will live.

| Section | Purpose | Why this section exists | Future Contents | Helps Answer | Comments |
|---|---|---|---|---|---|
| **20. Evolution Roadmap** | Describe how SAW-RA can evolve over time. | The architecture should support new patterns, machine-readable guidance, and future multi-agent extensions without requiring major restructuring. | Future roadmap<br>Planned extensions<br>Machine-readable formats<br>Machine-readable guidance evolution<br>Multi-agent direction | Q7 | |
| **Appendices** | Keep supporting material separate from the main document so the reference architecture remains focused and easy to read. | Templates, checklists, glossaries, and structured metadata are useful but should not interrupt the main narrative. | Glossary<br>Templates<br>Checklists<br>Questionnaires<br>Machine-readable metadata<br>References | All Guiding Questions | |

---
