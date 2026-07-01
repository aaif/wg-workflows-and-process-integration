# Reference Architectures Workstream

Workflows & Process Integration WG · Agentic AI Foundation

## What

A composable catalog of independently adoptable components for agentic workflows, plus one reference architecture per use case. Components first; architectures derived from use cases. Not a monolithic RA. Charter deliverable target: 08.01.2026.

## Structure

```
./catalog/component-catalog.md   Component blocks, defined once
./ra/ra-<use-case>.md            One RA per use case
./templates/ra-template.md       Copy to start a new RA
./decisions/decision-log.md      Decisions + dates
```

RA files reference catalog blocks — they don't redefine them.

## How we work

- Async first. Discord = ideas; Google Doc = proposals; GitHub = artifacts.
- Contributions happen through PRs: fork the repo, propose changes, discuss on the PR, and merge when ready.
- Keep artifacts easy to maintain by making ownership clear where useful.
- Abstraction = components + relationships, not implementation. Properties, not mechanisms.

## Contribute

Request repo access in the WG Discord. Copy the template → open a PR → discuss on the PR. Decisions logged in `./decisions/`.

## Links

- WG repo: https://github.com/aaif/wg-workflows-and-process-integration
- Google Doc: https://docs.google.com/document/d/1g8637JPZZ4Y-V-KXTcGU0de1HmTEc2iI6-PCTHv7zuI/edit?tab=t.s4e90o73aqx5#heading=h.71q4tygpnbxa
- Discord: https://discord.com/channels/1461090924791595243/1504501906251452478
