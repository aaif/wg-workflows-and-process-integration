# Gated Multi-Stage Delivery Pipeline — Use Case

## Business problem

This is the deliberate opposite of the autonomous "night shift" run: the same kind of work
— software delivery done by agents — but with a lot more human-in-the-loop. It's the
orchestrated bookend to that fully autonomous case.

On a delivery request, we want to run the whole thing as ordered stages — requirements →
design → build → review → QA → sign-off → deploy → retro. Agents do the work inside each
stage and build/review can fan out in parallel, but the pipeline **runs itself between
gates and stops dead at the authority boundaries we set**. Small changes get a shorter
track. Every stage drops an artifact plus a gate record, so there's a paper trail. It ends
in a real production deploy, so control and accountability matter more than speed.

## Requirements

- Start on a delivery request; run ordered stages, each producing an artifact and a gate
  record.
- Let specialist work happen inside a stage (produce a design, write code, review a diff)
  and let build/review fan out in parallel — but keep the **stage order and gate positions
  fixed**.
- Choose a shorter or fuller track by change size.
- Run per-language verification / QA at each stage.
- At each **authority boundary**, stop and wait for a named human to sign off the exact
  version before continuing.
- Deploy only the signed-off version, and only after sign-off authorises it; merge
  conservatively.
- Keep a replayable record of stages, gate decisions, and the deploy, plus a retro.

## Constraints and context

**Preconditions — what must be in place for this to run safely:**

- A stage / role / gate setup that doesn't care which model host runs each stage.
- Per-language verification.
- Somewhere to keep artifacts and gate history.
- Authority boundaries defined up front.
- Access scoped per role.

Other context:

- The **workflow owns sequencing** — agents produce content but never decide what runs next
  and never authorise the deploy.
- Deploy is a **transactional** effect on a real environment, reversible only via rollback;
  a bad change shipping is serious.
- Approval binds to the **exact version** reviewed; a later change invalidates a prior
  sign-off.
- The run spans hours to days across stages and human gates, and must be durable and
  replayable throughout.
- Vendor-neutral: no dependency on a specific CI/CD product, deploy target, model host, or
  orchestrator.

## Out of scope

- Letting an agent own the stage sequence or the gate decisions.
- Deploying without a human sign-off, or on a version a human did not approve.
- Defining the org's approval policy or who the approvers are — the workflow consumes that,
  it doesn't set it.

## Key failure mode to design against

A gate **waves something through on thin evidence** and it rots downstream — or the
authority boundaries are **too loose** and unreviewed work ships. The design has to make
the gates real and bind approval to what was actually reviewed.

## Success criteria

A good run deploys a change that passed every stage gate and carries a recorded human
sign-off at each authority boundary, with a replayable history and a rollback path if the
deploy's postcondition fails. Clear non-success endings exist too: rejected at a sign-off
gate, escalated when a stage hits something beyond its authority, cancelled if the request
is withdrawn, or a technical build/deploy failure. Every run ends in one recorded outcome.
