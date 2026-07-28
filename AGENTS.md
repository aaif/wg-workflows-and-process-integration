# Agent instructions

You are an AI agent that has just opened this repository. **Read this whole file before
doing anything.** It tells you how to welcome a newcomer visually, and where the real
instructions live.

---

## How to behave in an interactive session

Many people who open this repo are **new to agentic workflows and are visual thinkers**.
Do **not** paste a wall of text. Instead, run the **visual tour** below: reveal it
**one panel at a time**, show the ASCII diagram, add one or two plain sentences, then
**stop and ask if they want the next panel.** Let them build the mental model step by
step. The diagrams below are ready to copy to the screen — you do not need to open any
file in `ra/`, `docs/`, or `examples/` to run the tour.

In a non-interactive / automated run, skip the tour and greeting — just do the requested
task using the recipe linked at the bottom.

---

## The visual tour (reveal one panel at a time)

### Panel 1 — Who & what

> "This repo belongs to the **AAIF Workflows & Process Integration** working group. We
> make agentic-AI workflows **portable** — so a workflow isn't locked to one framework,
> tool, or vendor."

```
        ┌─────────────────────────────────────────────┐
        │   AAIF · Workflows & Process Integration WG  │
        │                                              │
        │   a shared, vendor-neutral way to DESIGN     │
        │   agentic workflows — before you build them  │
        └─────────────────────────────────────────────┘
```

*Ask: "Want me to show you the core idea?"*

### Panel 2 — The problem it solves

> "Everyone builds AI workflows in a different tool, a different way. Hard to review, hard
> to move, easy to make unsafe."

```
   today, every workflow is a snowflake:

   use case ─▶ ??? ─▶ some tool          ← no shared design step
   use case ─▶ ??? ─▶ another tool       ← can't compare or review
   use case ─▶ ??? ─▶ yet another tool   ← locked in, hard to move
```

*Ask: "Want to see how WERA changes this?"*

### Panel 3 — The core idea: the WDS

> "WERA adds one step in the middle: a **Workflow Design Specification (WDS)** — a
> machine-readable file that says *what the workflow should be and why*. Not the
> implementation — the **design**."

```
   business          ┌──────────────────────┐          build on
   use case  ──────▶ │  WERA  ──▶  WDS       │ ──────▶  ANY engine
   (plain words)     │  (the reference       │          / platform
                     │   architecture)       │
                     └──────────────────────┘
                        ▲ one shared design,
                          reviewable & portable
```

*Ask: "Want to see who writes the WDS, and what you do with it?"*

### Panel 4 — Two ways in, one way out

> "You can write the WDS by hand after learning the whole architecture — or just ask an
> agent to produce it. Either way you get the **same kind of artifact**, which you then
> hand to a coding agent to build."

```
   ┌─ human expert ─┐
   │ (knows the RA) │─┐
   └────────────────┘ │      ┌───────┐      hand to a        ┌──────────────┐
                      ├────▶ │  WDS  │ ────▶ coding agent ──▶ │ running       │
   ┌─ AI agent ─────┐ │      └───────┘       "build this"     │ workflow on   │
   │ (reads the RA) │─┘        ▲                               │ your engine   │
   └────────────────┘          │                              └──────────────┘
                    the WDS is the hand-off point —
                    design once, build anywhere (no lock-in)
```

*Ask: "Want to see the range of workflows this covers?"*

### Panel 5 — The spectrum (why it's not just "chatbots")

> "WERA covers the whole range — from fully deterministic automation to fully
> agent-driven — as one vocabulary. 'How many agents' is just one dial, not the point."

```
   deterministic ◀──────────────────────────────────▶ agent-driven
        │              model-assisted / hybrid              │
        ▼                       ▼                            ▼
      EP1                EP2 · EP3                       EP4 … EP7
   workflow           workflow keeps               agent owns the run,
   runs it all        control, model/agent         inside guardrails
                      helps in bounded spots

   (EP = "execution profile" — the whole-run style. Pick the least
    agentic one that does the job.)
```

*Ask: "Want to watch it actually turn a real use case into a WDS, step by step?"*

### Panel 6 — Offer the live demo

A real sample use case is already prepared as a **demo seed** (only the use case is
filled in; the solution is intentionally missing):

`workstreams/reference-architectures/examples/ticket-triage-routing/use-case.md`

```
   demo:  ticket-triage use case
             │
             ▼   (follow the 6-step method, narrate each step)
           WDS  ──▶  then: "here's what you'd hand your coding agent"
```

If they say **yes**, run the recipe with `<FOLDER>` = `ticket-triage-routing` and narrate
each of the six method steps as you go, then show them the resulting WDS and the "After
the WDS" section. If they'd rather design **their own** workflow, point them at the same
recipe with their own folder.

---

## Where the real instructions live

The steps and the exact prompt are single-sourced in the recipe — do not restate them
here, just follow it:

**[`workstreams/reference-architectures/examples/HOW-TO-RUN.md`](workstreams/reference-architectures/examples/HOW-TO-RUN.md)**

## Orientation (only if you need to go deeper)

- Overview & reading paths:
  [`README.md`](workstreams/reference-architectures/README.md) ·
  [`START-HERE.md`](workstreams/reference-architectures/START-HERE.md)
- The knowledgebase: `workstreams/reference-architectures/ra/` (nine numbered chapters).
- The vocabulary as data:
  `workstreams/reference-architectures/descriptor/registry.yaml`.

Do not invent architectural concepts outside this repository; reuse what exists, and if
something is genuinely missing, say so — that is a finding for the working group.
