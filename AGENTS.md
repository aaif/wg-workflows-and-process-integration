# Agent instructions

You are an AI agent that has just opened this repository. **Read this whole file before
doing anything.** It tells you how to welcome a newcomer visually, and where the real
instructions live.

---

## How to behave in an interactive session

**First, offer a choice** — don't assume everyone is new. Greet in one line and present
three paths:

```
   How would you like to start?

   1) Give me the quick tour   — what this is & why (visual, ~2 min)
   2) Run the live demo        — watch a real use case become a
                                 Workflow Design Specification (WDS)
   3) Design my own workflow   — I already have a use case in mind
```

- **Choice 1** → run the **visual tour** below.
- **Choice 2** → skip to [Panel 6](#panel-6--offer-the-live-demo) and run the demo on the
  prepared seed.
- **Choice 3** → go straight to the recipe (the "real instructions" link at the bottom)
  with the person's own use case.

Returning users will usually pick 2 or 3 — let them skip the tour entirely.

### Running the tour (choice 1)

Many first-time visitors are **new to agentic workflows and are visual thinkers**.
Do **not** paste a wall of text. Reveal the tour **one panel at a time**: show the ASCII
diagram, add one or two plain sentences, then **stop and tease what's next** (each panel
ends with a "Next, I can show you…" line) and wait for the person to continue. Let them
build the mental model step by step. The diagrams below are ready to copy to the screen —
you do not need to open any file in `ra/`, `docs/`, or `examples/` to run the tour.

In a non-interactive / automated run, skip the greeting and choice — just do the requested
task using the recipe linked at the bottom.

---

## The visual tour (reveal one panel at a time)

### Panel 1 — Who & what

> "This repo belongs to the **AAIF Workflows & Process Integration** working group. We
> define a **shared model and common terminology** for agentic-AI workflows — the
> primitives, patterns, and design rules for multi-step work. We standardize how agents
> **coordinate** with each other, with external systems and tools, and with human
> reviewers. We keep workflow definitions **portable** across frameworks and runtimes, so
> nothing is locked to one vendor. And we cover what production needs — **stateful
> replay, failure recovery, and human-in-the-loop** — so these workflows are safe to run
> at scale."

```
   ┌──────────────────────────────────────────────────────┐
   │        AAIF · Workflows & Process Integration WG       │
   │        vendor-neutral standards for agentic workflows  │
   ├──────────────────────────────────────────────────────┤
   │  shared model  │ coordinate  │ portable │ production   │
   │  & terminology │ agents +    │ across   │ replay,      │
   │  (primitives,  │ systems +   │ frame-   │ recovery,    │
   │   patterns)    │ humans      │ works    │ human-in-loop│
   └──────────────────────────────────────────────────────┘
```

*Then pause — offer: "Next, I can show you the core idea. Ready?"*

### Panel 2 — The problem it solves

> "Everyone builds AI workflows in a different tool, a different way. Hard to review, hard
> to move, easy to make unsafe."

```
   today, every workflow is a snowflake:

   use case ─▶ ??? ─▶ some tool          ← no shared design step
   use case ─▶ ??? ─▶ another tool       ← can't compare or review
   use case ─▶ ??? ─▶ yet another tool   ← locked in, hard to move
```

*Then pause — offer: "Next, I can show you how this group's reference architecture changes that."*

### Panel 3 — The core idea: the WDS

> "The group's reference architecture — **WERA**, the Workflow Execution Reference
> Architecture — adds one step in the middle: a **Workflow Design Specification (WDS)**,
> a machine-readable file that says *what the workflow should be and why*. Not the
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

*Then pause — offer: "Next, I can show you who writes the WDS and what you do with it."*

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

*Then pause — offer: "Next, I can show you the range of workflows this covers."*

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

*Then pause — offer: "Finally, I can run a live demo — watch it turn a real use case into a WDS, step by step. Want to see it?"*

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
