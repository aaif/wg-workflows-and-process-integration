# Architecture Name — so a practitioner can say "we're building a ___"

**The job it serves:** The recurring need this architecture answers, stated plainly \
**Built from patterns:** Links into `patterns/` \
**Requires capabilities:** Capability roles required to realize the architecture \
**Audience:** Who benefits from reading this architecture — builders, reviewers, and the stakeholders it serves

*(Header convention: every field line ends with a trailing backslash except
the last; field values start capitalized.)*

## Status

Draft / proposed / approved (decision note link). What's locked, what isn't.

## Purpose

The job, in two or three sentences, and why this RA exists — including,
for early RAs, why it comes in this order (which charter motivations it
answers, which components it exercises).

The intended audience lives in the header; here, give reading paths. Route
readers by providing clear direction about what content they will find 
in different sections, not by assuming who a reader might be. Name sections that
carry the *what* and the *why*, and the sections that are implementation
guidance, and let readers opt into the depth they need. Readers decide whether 
a document is for them. Tell them what content to expect.

## Is this your architecture? (checklist)

Routing questions a practitioner walks with their use case in hand. Every
question must be answerable from the use case alone — before any design
exists, and without reference to model capability, which shifts every
generation. Every answer routes somewhere explicit — including "yes":
confirm the fit and say keep going, or name the nearby flow this
architecture does not cover. A "no" routes to another architecture, a
variant below, or a single pattern that suffices without the full
composition.

The same checklist should work in reverse — assessing an existing workflow
by checking each invariant, exit state, and boundary; the gaps are the
findings.

## Variants

Same composition, plus or minus roughly one component, serving an adjacent
job. The deeper test: a variant may add or remove invariants, but never
rewrite one — the guarantees are promises, and a variant cannot quietly
weaken a promise the architecture's name still implies. If an invariant or
an arrow contract changes meaning, it is a separate architecture, no matter
how small the diagram delta looks.

## Structure

The architecture diagram, at capability-and-relationship level only. The
agent's internal reasoning loop stays unspecified. Where useful, label what
crosses an arrow (the data, not the control flow) — the contracts on the
arrows are what implementations actually disagree about.

Follow with the required-capabilities table: capability, responsibility in
*this* architecture, charter basis. An implementation may realize a capability
as its own technical component or combine several capabilities in one
platform.

## Pattern composition

| Pattern | Where it sits | Why it is required here |
|---|---|---|

Per-pattern invariants, failure modes, and runtime examples live in the
pattern entries — this table records only the composition.

Follow with any **invalid compositions**: combinations or shortcuts that
break the architecture's guarantees. Naming what is *not* this architecture
is as load-bearing as naming what is.

## The agent and workflow-control boundary

What the agent is allowed to do; what capabilities and guarantees must remain
under workflow control. Name any protected effects the agent must be unable to
cause directly.

## Choosing deterministic and model-driven steps

Identify where deterministic or rule-based implementation provides required
guarantees, and where the input is open-ended enough to warrant model
reasoning. Explain the relevant criteria — such as predictability,
testability, enforceability, and latency — rather than treating cost alone as
the deciding factor.

## Exit states

Every way a run can end — success is one row, not the table. Each exit
lands in the system of record. A run that can end in a state not listed
here falsifies the architecture just as surely as a missing component.

| Exit state | Reached when | Recorded as |
|---|---|---|

## Worked scenario

Sourced from (or sharpened from, with a pointer to) the Use Cases WS. A
story with real systems and stakes, not an abstract flow. Include:

- the numbered steps, each naming the components it touches
- the run-over-time lifecycle view (where durability lives)
- the "if the process dies during step N" table

## Composition considerations

Only concerns that appear when the patterns combine — anything attributable
to a single pattern belongs in that pattern's entry.

## Out of scope (handled elsewhere)

The concerns this architecture deliberately does not own, with pointers —
other WGs, other workstreams, other shelves. Carrying the fence in-document
keeps every review thread from relitigating it.

## Validation record

Scenarios come from the Use Cases workstream. Every scenario walked through
this architecture gets a row, whatever the outcome — no-fit rows are the
most valuable ones.

| Scenario | Source | Result | Notes |
|---|---|---|---|

## Open questions

Genuinely unresolved items, each phrased so a PR comment could close it.
