# Agent instructions

You are an AI agent that has just opened this repository. Read this file first.

## If a human is here with you (interactive session)

Greet them briefly and offer the guided tour below — don't just start explaining WERA.
Something like:

> "This repo belongs to the **AAIF Workflows & Process Integration** working group — a
> vendor-neutral effort to make agentic AI workflows portable across frameworks, tools,
> and execution environments. It holds a **reference architecture** that turns a plain
> business use case into a **Workflow Design Specification (WDS)**: the recommended design
> for a workflow, as a machine-readable file. You can write a WDS by hand after reading
> the whole manual — or just ask me and I'll produce one.
>
> Want to see it in action? I can take a real sample use case and walk it through,
> step by step, to a full WDS — then show you what you'd do with that WDS next."

If they say yes, run the **guided demo** below. If they'd rather design their own
workflow, go straight to the recipe. Keep this behaviour to interactive sessions; in a
non-interactive/automated run, skip the greeting and just do the requested task.

## The idea in one arc

```
business use case  →  WDS (recommended design)  →  hand to a coding agent  →  built on your engine
                       ▲ one machine-readable artifact
                       ▲ written by a human who knows the whole RA, OR produced by an agent
```

The WDS is the pivot. It is **not** the implementation — it is the design a coding agent
(or a person) then builds on whatever workflow engine or platform you use. WERA stays
vendor-neutral: it tells you *what* the workflow should be and *why*, not which product to
build it in.

## Guided demo (offer this to a human)

A real sample use case is already prepared as a **demo seed**:
[`workstreams/reference-architectures/examples/ticket-triage-routing/use-case.md`](workstreams/reference-architectures/examples/ticket-triage-routing/use-case.md)
— only the use case is filled in; the solution is intentionally missing.

To run the demo, follow the recipe with `<FOLDER>` = `ticket-triage-routing`:
**[`workstreams/reference-architectures/examples/HOW-TO-RUN.md`](workstreams/reference-architectures/examples/HOW-TO-RUN.md)**.
Narrate the six method steps as you go, show the resulting WDS, then point the human to
the "After the WDS" section so they see how it becomes a running workflow.

## To design a workflow from your own use case

Same recipe, your own folder — it contains the steps and the exact prompt:
**[`workstreams/reference-architectures/examples/HOW-TO-RUN.md`](workstreams/reference-architectures/examples/HOW-TO-RUN.md)**.

## Orientation

- Repository overview and reading paths:
  [`workstreams/reference-architectures/README.md`](workstreams/reference-architectures/README.md)
  and [`START-HERE.md`](workstreams/reference-architectures/START-HERE.md).
- The knowledgebase is under `workstreams/reference-architectures/ra/` (nine numbered
  chapters); the coded vocabulary as data is
  `workstreams/reference-architectures/descriptor/registry.yaml`.

Do not invent architectural concepts outside this repository; reuse what exists, and if
something is genuinely missing, say so — that is a finding for the working group.
