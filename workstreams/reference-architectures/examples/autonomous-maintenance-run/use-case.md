# Autonomous Maintenance Run ("night shift") — Use Case

## Business problem

Most of our workflows have a human gate and run once — which is fine, but it leaves the
"fully autonomous" end that the charter points at empty. This is an attempt to fill that
end.

On a schedule, or from a backlog of triage-labelled issues, we want an agent that loops
over the boring maintenance stuff — dependency bumps, lint/type fixes, spec & doc drift.
For each task it makes the change in an isolated sandbox, opens a pull request behind
deterministic gate checks, and keeps iterating against CI until the gate goes green. It
only pings a human on repeated failure, or when a change is bigger than it's allowed to
make on its own. It is the "you stop prompting and start writing the loop" idea: good for
small, bounded work, not big features.

## Requirements

- Start on a schedule or from a triage-labelled backlog item; take one bounded task at a
  time.
- Do each change in a **fresh, isolated sandbox** per task — never touch real repo state
  directly.
- Iterate: make edits, run the deterministic gate (CI + contract/eval checks), read the
  feedback, try again, until the gate is green.
- On green, open a pull request for that exact change. It does not merge.
- Escalate to a human on repeated failure, or when the change exceeds the allowed scope.
- Stop cleanly if it exhausts its budget rather than looping forever.
- Leave enough of a trail (what it tried, the gate results) to review the PR and audit the
  run.

## Constraints and context

**Preconditions — what must be true for this to be safe to run autonomously:**

- Decent CI with tests that actually mean something (plus feature flags), so the gate is a
  real arbiter of "done".
- A fresh isolated environment per task.
- A gate the loop can genuinely stop on — a deterministic pass/fail.
- Scoped write credentials (issue + PR write only).
- A token / iteration / wall-clock budget per task.

Other context:

- Issue text and dependency changelogs are **untrusted** input.
- Opening a PR is reversible (close it, discard the sandbox); merging and deploying are a
  separate human decision.
- Runs are long — minutes to hours per task, unattended — and must survive restarts and CI
  waits.
- Vendor-neutral: no dependency on a specific Git host, CI system, sandbox tech, model
  provider, or orchestrator.

## Out of scope

- Merging pull requests or deploying anything.
- Touching production or any authoritative system directly.
- Large features or changes beyond the task's declared, allowed scope.

## Key failure mode to design against

The loop lands on a fix that is **green but wrong** — the tests pass but the behaviour is
still off — or it just **burns budget going in circles** without converging. The design has
to make the gate trustworthy and bound the loop.

## Success criteria

For one assigned task, a good run produces a change that makes the deterministic gate pass
in a sandbox plus an open PR for exactly that change — or a clear non-success ending:
nothing attempted because the task was out of scope, handed to a human after repeated
failure or over-scope, or stopped because the budget ran out. Every run ends in one of
those recorded outcomes, and never merges or deploys.
