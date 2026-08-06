# Reference Architectures Workstream

Workflows & Process Integration WG · Agentic AI Foundation

## What this workstream is for

Produce a catalog of reference architectures and reusable patterns for agent
workflow execution.

This contribution proposes organizing reference architectures around the
**job a practitioner needs the system to perform**, rather than treating agent
count as the top-level architecture. "Single-agent" and "multi-agent" remain
useful structural characteristics, but they do not by themselves say what the
workflow is built to accomplish or which guarantees it provides.

The proposed model is recorded explicitly in
[the job-oriented architecture decision note](decisions/job-oriented-architecture-model.md)
for working group review.

### Architectures and patterns

- A **reference architecture** is a complete composition: the reusable
  patterns, required capabilities, boundaries, relationships, guarantees, and
  exit states for a recognizable practitioner job. Its name should complete
  the sentence, "we're building a ___."
- A **pattern** solves one recurring sub-problem and can be adopted
  independently or composed into multiple architectures. It owns its own
  invariants and failure modes.
- A **scenario** tests whether an architecture fits a real use case and makes
  its behavior concrete. A scenario is validation material, not a separate
  architecture.

The first worked architecture is a
[single-agent process with human approval](architectures/single-agent-human-approval.md).
It composes the
[proposal/execution split](patterns/proposal-execution-split.md),
[human approval gate](patterns/human-approval-gate.md), and
[durable wait](patterns/durable-wait.md) patterns.

## Guidelines

A reference architecture should act as a routing checklist: a practitioner
brings a use case and determines whether the architecture fits, whether a
nearby variant fits, or whether an individual pattern is sufficient.

Include guidance for choosing deterministic and model-driven steps: identify
where conventional workflow logic provides predictable, testable behavior and
where open-ended reasoning benefits from an LLM.

Start with the smallest job-oriented architecture that exercises the
workstream's core concerns. Treat deterministic and ReAct-style internals as
equal implementation choices inside the agent boundary.

Keep the architecture at the component and relationship level.

Use `docs/` for supporting material that informs the reference architectures.
Use cases and scenarios validate the architectures; they are not separate reference architecture documents.

## Structure

```text
workstreams/reference-architectures/
├── README.md
├── architectures/           # complete architectures: what you'd say you're building
│   ├── TEMPLATE.md
│   └── single-agent-human-approval.md
├── patterns/                # independently adoptable pattern entries
│   ├── TEMPLATE.md
│   ├── durable-wait.md
│   ├── human-approval-gate.md
│   └── proposal-execution-split.md
├── decisions/
│   ├── TEMPLATE.md
│   └── job-oriented-architecture-model.md
└── docs/
    └── *.md
```

## How to read the architectures

A reference architecture should describe:

- the surrounding workflow pieces
- how they connect
- what the agent is allowed to do
- what must be handled outside the agent

It should not get into the agent’s internal reasoning loop.

## Side docs

Use `docs/` for supporting material that helps the workstream but is not itself a reference architecture.

Examples:

- meeting notes and takeaways
- comparison tables
- source summaries and reading notes
- exploratory drafts and hypotheses
- background research that may later feed a deliverable

If a document is meant to inform the workstream but not define the architecture, put it in `docs/`.

## Working style

- Async first: use PR comments to discuss and converge.
- Fork-first: contributors work in their own fork or branch and open PRs directly to the workstream destination branch.
- Keep drafts concise and easy to review.
- Use decision notes when a choice needs to be recorded.
- Use TODOs instead of blank sections when something is intentionally unresolved.

## Contribution flow

1. Create or update work in your fork
2. Open a PR against the workstream destination branch
3. Discuss and iterate in PR comments
4. Merge only after the review outcome is clear

## Links

- WG repo: https://github.com/aaif/wg-workflows-and-process-integration
- Charter: [charter.md](../../charter/charter.md)
- Meeting notes: https://docs.google.com/document/d/1g8637JPZZ4Y-V-KXTcGU0de1HmTEc2iI6-PCTHv7zuI/edit?usp=sharing
- Discord: https://discord.com/channels/1461090924791595243/1504501906251452478
