# Reference Architectures Workstream

Workflows & Process Integration WG · Agentic AI Foundation

## What this workstream is for

Produce the workflow reference architecture for agent workflow execution.

Start with two generic reference architectures:

- **single-agent workflow**
- **multi-agent workflow**

Scenarios validate and illustrate the reference architectures. If a scenario does not fit either generic architecture, that is a signal that a new reference architecture may be needed.

## Guidelines

The RA should act as a checklist: a user brings a use case, walks through the right questions, and lands on a pattern.

Include determinism hints: where to use cheap deterministic steps, and where LLM reasoning is worth the cost.

Start with single-agent workflow first. Treat deterministic and ReAct-style internals as equal implementation choices inside the boundary.

Keep the architecture at the component and relationship level.

Use `docs/` for supporting material that informs the reference architectures.
Use cases and scenarios validate the architectures; they are not separate reference architecture documents.

## Structure

```text
workstreams/reference-architectures/
├── README.md
├── ra/
│   ├── ra-single-agent.md
│   └── ra-multi-agent.md
├── decisions/
│   └── TEMPLATE.md
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
