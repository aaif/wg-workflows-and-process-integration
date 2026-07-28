# Agent instructions

This repository is a **workflow execution reference architecture** (WERA). Its main use
for an AI agent is to turn a business use case into a **Workflow Design Specification** —
a full, machine-readable design a human can review and implement.

## To design a workflow from a use case

Follow the recipe in
**[`workstreams/reference-architectures/examples/HOW-TO-RUN.md`](workstreams/reference-architectures/examples/HOW-TO-RUN.md)**.
In short:

1. Copy `workstreams/reference-architectures/examples/_template/` to
   `workstreams/reference-architectures/examples/<your-usecase>/`.
2. Write the business problem into that folder's `use-case.md` (the only file a human
   fills in).
3. Run the prompt below, with `<FOLDER>` set to `<your-usecase>`.

All paths in the prompt are relative to `workstreams/reference-architectures/`.

```text
You are a workflow architect. Read this repository — start at ra/README.md and load
descriptor/registry.yaml as data. Follow the Workflow Design Method
(ra/08-lifecycle/workflow-design-method.md) for the use case in:

    examples/<FOLDER>/use-case.md

Produce the FULL solution set in examples/<FOLDER>/, matching the shape of
examples/invoice-processing/ (see examples/_template/SOLUTION-FILES.md):

    rationale.md
    solution.md
    <FOLDER>.wera.yaml
    views/architecture.md
    views/execution.md
    views/sequence.md
    views/contracts-and-state.md
    README.md

Rules:
- Do not invent architectural concepts outside this repository.
- Use only codes present in descriptor/registry.yaml.
- Reuse existing patterns and profiles whenever possible.
- Prefer the least-agentic composition that satisfies the requirements (DP-01).
- If you must introduce a new concept, explain why existing concepts were insufficient.
- Reference cross-cutting concerns owned by other WGs as external boundaries (XB-##);
  do not redefine them.

Before returning, self-check against the repository:
- the *.wera.yaml validates against descriptor/workflow-descriptor.schema.json;
- every code used (in the WDS and the prose) exists in descriptor/registry.yaml (INV-017);
- applicable invariants and composition rules hold (target at least CL1);
- no cross-WG concern was redefined locally (INV-015);
- the least-agentic viable composition was chosen (DP-01);
- relative links resolve (../../ra/… from the folder, ../../../ra/… from views/).
```

## Orientation

- Repository overview and reading paths:
  [`workstreams/reference-architectures/README.md`](workstreams/reference-architectures/README.md)
  and [`START-HERE.md`](workstreams/reference-architectures/START-HERE.md).
- The knowledgebase itself is under `workstreams/reference-architectures/ra/` (nine
  numbered chapters); the coded vocabulary as data is
  `workstreams/reference-architectures/descriptor/registry.yaml`.
- The method both humans and agents follow:
  [`ra/08-lifecycle/workflow-design-method.md`](workstreams/reference-architectures/ra/08-lifecycle/workflow-design-method.md).

Do not invent architectural concepts outside this repository; reuse what exists, and if
something is genuinely missing, say so — that is a finding for the working group, per the
[acceptance test](workstreams/reference-architectures/docs/acceptance-test.md).
