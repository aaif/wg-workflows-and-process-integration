# How to run a use case → full solution

Status: Mature

This is the repeatable recipe for turning a business use case into a **full solution** —
the same file set as [invoice-processing](invoice-processing/README.md) — using a coding
agent and this repository. It is the practical wrapper around the
[Workflow Design Method](../ra/08-lifecycle/workflow-design-method.md): the method is
*what to think*; this page is *how to run it*.

## Quickstart

1. **Copy the template.** `examples/_template/` → `examples/<your-usecase>/`
   (short, kebab-case name). Delete the template's `README.md` from the copy.
2. **Describe the problem.** Fill in `examples/<your-usecase>/use-case.md`. This is the
   only file you write by hand.
3. **Run the agent.** Paste the prompt below into your coding agent, with `<FOLDER>`
   replaced by `<your-usecase>`.
4. **Check it.** Confirm the [done criteria](#what-done-looks-like) below.

## The prompt

The prompt is **generic** — the only thing that changes between runs is `<FOLDER>`. Point
it at a folder that already contains a filled `use-case.md`.

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

This is the [AI agent instructions](../ra/08-lifecycle/ai-agent-instructions.md) prompt,
extended to point at a folder and ask for the full solution set instead of only the WDS.

## Reproduce or complete an existing example

Point `<FOLDER>` at an example that already exists:

- **Complete a trial to full parity** — the SDLC trials
  [`autonomous-maintenance-run`](autonomous-maintenance-run/README.md) and
  [`gated-delivery-pipeline`](gated-delivery-pipeline/README.md) currently have only a WDS
  and a README. Running the prompt with that folder fills in the missing triad and
  `views/`.
- **Regenerate / audit** — run the prompt against any folder and diff the result against
  the committed files. A clean reproduction is exactly the
  [acceptance test](../docs/acceptance-test.md): the same repository, the same use case,
  the same solution.

## What "done" looks like

- Every file in [`_template/SOLUTION-FILES.md`](_template/SOLUTION-FILES.md) exists in the
  folder (a lighter WDS-only deliverable is fine for a quick trial).
- The `*.wera.yaml` validates against the
  [schema](../descriptor/workflow-descriptor.schema.json).
- Every code resolves in [registry.yaml](../descriptor/registry.yaml); relative links
  resolve.

### Verifying

```python
# from workstreams/reference-architectures/ — schema-validate the WDS
import json, yaml, jsonschema
schema = json.load(open("descriptor/workflow-descriptor.schema.json"))
doc = yaml.safe_load(open("examples/<FOLDER>/<FOLDER>.wera.yaml"))
jsonschema.validate(doc, schema)
```

Reviewers apply the [review checklist](../ra/08-lifecycle/review-checklist.md) and the
[conformance levels](../ra/07-readiness/conformance.md) to judge quality beyond schema
validity.

## After the WDS

A WDS is a **design, not an implementation**. It is the recommended way to build the
workflow — profile, patterns, authorities, effects, overlays — captured once, so the build
step is a hand-off rather than a fresh interpretation.

With the WDS in hand you (or a coding agent) build the actual workflow on whatever engine
or platform you use:

```text
Here is the Workflow Design Specification for my workflow:
examples/<FOLDER>/<FOLDER>.wera.yaml (with its solution.md and views/).
Implement it on <the workflow engine / automation platform we use>, preserving the
authority allocation, the protected effects, and the human-in-the-loop gates exactly as
the WDS specifies.
```

WERA stays **vendor-neutral** on purpose: it says *what* the workflow should be and *why*,
never which product to build it in. The same WDS can target different engines without
being redesigned — that portability is the point ([the WG exists to avoid workflow
lock-in](../../../charter/charter.md)). The WDS is also the review and conformance artifact,
so what gets built can be checked back against what was designed.

## Later: one command

This page is written so a future `run-my-usecase.py` is a thin wrapper: ask for the
use-case name, copy `_template/` into place, open `use-case.md` for editing, then print
the prompt above with `<FOLDER>` filled in. The manual recipe and the script produce the
same result, so starting by hand costs nothing.
