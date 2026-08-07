# Contributing Reference Architecture Content

This guide explains how to add or change content in this workstream so that patterns, reference architectures, and validation scenarios remain consistent and reusable.

## Before you write

Read these in order:

1. [README.md](README.md) — the workstream model and current content.
2. [Job-oriented architecture decision](decisions/job-oriented-architecture-model.md) — the relationship between patterns, architectures, and scenarios.
3. The applicable template:
   - [Pattern template](patterns/TEMPLATE.md)
   - [Architecture template](architectures/TEMPLATE.md)

Reuse existing guidance before proposing a new concept. This workstream is a draft: record genuine gaps as open questions rather than silently inventing new terminology or rules.

## Choose the right contribution type

| If you have… | Add or update… | It is for… |
|---|---|---|
| One recurring workflow problem with an independently reusable solution | A **pattern** in `patterns/` | Explaining how to solve that one problem reliably. |
| A recognizable practitioner job requiring several patterns and capability roles together | A **reference architecture** in `architectures/` | Defining the complete composition, boundaries, guarantees, and exit states for that job. |
| A real or illustrative workflow example | A **scenario** in an architecture’s `Worked scenario` and `Validation record` sections | Testing whether an architecture fits; it is not an architecture by itself. |
| Rationale for a structural choice | A **decision note** in `decisions/` | Recording the choice, alternatives, and consequences. |
| Background research, comparison, or exploratory idea | A document in `docs/` | Informing the workstream without defining the architecture. |

### Pattern or architecture?

A **pattern** solves one sub-problem and can be adopted independently. Examples: a durable wait, a human approval gate, or an independent acceptance check.

A **reference architecture** is the reusable whole for a practitioner job. It composes patterns, capability roles, boundaries, guarantees, and exit states. Its name should complete the sentence:

```text
“We are building a ___.”
```

Do not use a domain example as an architecture name unless the job itself is inherently domain-specific. For example, an autonomous maintenance run can validate a broader bounded-autonomous-remediation architecture; it is not automatically the architecture’s name.

## Authoring rules

### For every contribution

- Keep it vendor-neutral. Describe logical capabilities and required behaviour before naming products.
- State what is known from evidence and what is a proposed WG interpretation. Do not present an unverified implementation claim as fact.
- Reuse existing patterns and guarantees instead of copying or weakening them.
- Name cross-cutting concerns owned by another WG as out of scope; do not redefine their standards here.
- Use plain language first. Define specialized terms where a new reader needs them.
- Add real open questions rather than filling gaps with invented certainty.

### For a pattern

- Use [`patterns/TEMPLATE.md`](patterns/TEMPLATE.md) in its stated order.
- Keep the solution small and context-free. If it needs many components or only makes sense as part of one job, it is probably an architecture.
- State invariants as guarantees that every implementation must preserve.
- Give concrete failure modes for violated invariants.
- Distinguish what a runtime mechanism provides from what an implementation must still add.

### For a reference architecture

- Use [`architectures/TEMPLATE.md`](architectures/TEMPLATE.md) in its stated order.
- Name a reusable practitioner job, not an agent count, vendor, or single example.
- Compose patterns; do not restate each pattern’s full invariant and failure-mode content.
- Make the agent/workflow-control boundary explicit: who may propose, decide, authorize, execute, and own state.
- Describe deterministic versus model-driven work.
- Define all terminal/exit states and what is recorded for each.
- Include at least one worked scenario and a validation record. A no-fit or partial-fit result is useful evidence.

### Extra material

Keep the template sections in their stated order. If additional material is genuinely useful, place it after `Open questions` under an explicitly named:

```md
## Appendix: <topic>
```

Do not insert new core sections ad hoc.

## Suggested authoring flow

```text
1. Start with a real problem or scenario.
2. Check whether an existing pattern or architecture already fits.
3. Identify the reusable problem or practitioner job—not the domain example.
4. Draft from the applicable template.
5. Reuse patterns and state only the new composition-level guarantees.
6. Add a worked scenario and validation record.
7. Record uncertainties as open questions.
8. Run the self-review before opening a PR.
```

## Self-review checklist

Before opening a PR, confirm:

- [ ] I chose the correct contribution type.
- [ ] I read the relevant template and retained its core section order.
- [ ] The name describes a reusable problem or practitioner job, not merely one scenario.
- [ ] Existing patterns were reused where they fit.
- [ ] Capability roles are logical and vendor-neutral.
- [ ] Authority boundaries, external effects, and failure/recovery behaviour are explicit where relevant.
- [ ] The contribution distinguishes evidence from WG interpretation.
- [ ] A reference architecture has a scenario-based validation record.
- [ ] Extra content, if any, is in an explicit appendix.
- [ ] Internal links resolve and the Markdown has no whitespace errors.

## AI-assisted contributions

AI tools may help draft or review content, but the same rules apply. An AI-generated contribution must identify its evidence, open questions, and assumptions. A human contributor remains responsible for deciding whether the proposed pattern or architecture is correct and reusable.
