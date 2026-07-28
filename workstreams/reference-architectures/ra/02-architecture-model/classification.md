# Classification — the Workflow-Run Coordinate

Status: Mature

## Why this document exists

WERA does not classify workflows by "single-agent vs multi-agent." Instead it places each workflow run at a **coordinate** across eight orthogonal axes. This lets one architecture describe the whole spectrum from deterministic automation to multi-agent execution, and it gives the [descriptor](../../descriptor/README.md) a precise, machine-readable way to say what a workflow *is*.

A **coordinate** is one value per axis. Agent count appears only as the `actor_topology` axis — one dimension among eight, never the organising principle.

## The eight axes

### 1. Locus of nondeterminism — `nondeterminism` (`ND0`–`ND8`)

Where, and how much, model/agent judgement drives the run.

| Code | Locus | The model/agent determines |
|---|---|---|
| ND0 | None | Nothing; explicit rules suffice |
| ND1 | Content | What artifact or text to produce |
| ND2 | Classification | Which closed-set label applies |
| ND3 | Selection | Which candidate from a validated set |
| ND4 | Branch | Which deterministic branch to take |
| ND5 | Tool | Which tool/capability to invoke |
| ND6 | Plan | What sequence of steps to attempt |
| ND7 | Delegation | Which sub-goal to delegate to whom |
| ND8 | Open goal | How to pursue an open-ended objective |

### 2. Control-flow authority — `control_flow_authority` (enum)

Who determines the next valid transition: `workflow` | `agent` | `human` | `event` | `external_runtime`.

### 3. Actor topology — `actor_topology` (enum)

How execution actors are arranged: `none` (deterministic) | `single_agent` | `bounded_agentic_region` | `multi_agent` | `cross_runtime`.

### 4. Flow shape — `flow_shape` (`FS1`–`FS9`)

| Code | Shape |
|---|---|
| FS1 | Single step |
| FS2 | Linear sequence |
| FS3 | Conditional branch |
| FS4 | Iterative refinement / loop |
| FS5 | Parallel fan-out and join |
| FS6 | Exception-only nondeterminism |
| FS7 | Long-running with waits |
| FS8 | Event-driven continuation |
| FS9 | Child / remote sub-runs |

### 5. State and durability — `durability` (`DUR0`–`DUR4`)

| Code | State model |
|---|---|
| DUR0 | Ephemeral; single call |
| DUR1 | Session state within one process lifetime |
| DUR2 | Durable state; survives restart |
| DUR3 | Durable + resumable after waits/events |
| DUR4 | Durable + replayable execution history |

### 6. Effect level — `effect_level` (`EF0`–`EF4`)

The single scale every `EFn` reference in the repository resolves to.

| Code | Side effect | Minimum controls |
|---|---|---|
| EF0 | None | Output validation and audit appropriate to use |
| EF1 | Read-only | Least privilege, query bounds, output sanitisation, audit |
| EF2 | Reversible write | Policy, idempotency, compensation, postcondition check |
| EF3 | Transactional write | Transaction semantics, concurrency control, commit evidence, reconciliation |
| EF4 | High-impact / irreversible | Deterministic validation, human approval, segregation of duties, strong evidence |

### 7. Assurance model — `assurance` (`AS0`–`AS5`)

| Code | Assurance model | Suitable when |
|---|---|---|
| AS0 | None beyond basic logging | Experiments only |
| AS1 | Output schema validation | Structured output, low impact |
| AS2 | Deterministic postcondition checks | Verifiable results |
| AS3 | Human review | Judgement needed, reversible |
| AS4 | Human approval before effect | Consequential effects |
| AS5 | Multi-party / segregated approval | High-impact or regulated |

### 8. Impact — `impact` (`IM0`–`IM4`)

| Code | Impact of a wrong result/action | Typical readiness floor |
|---|---|---|
| IM0 | Negligible | RT0 |
| IM1 | Minor, easily corrected | RT1 |
| IM2 | Material, business-visible | RT2 |
| IM3 | Serious, hard to reverse | RT3 |
| IM4 | Severe, regulated or safety | RT4 |

## Example coordinate (invoice processing)

```yaml
coordinates:
  nondeterminism: ND3          # selection among validated candidates
  control_flow_authority: workflow
  actor_topology: single_agent # one bounded recommendation agent
  flow_shape: FS7              # long-running with a human-review wait
  durability: DUR3             # resumable across the approval wait
  effect_level: EF2            # unposted ERP draft is a reversible write
  assurance: AS4               # human approval before handoff
  impact: IM2                  # material AP error, correctable pre-payment
```

Coordinates support [pattern selection](../05-selection/README.md) and comparison; they do not replace architecture review.

## Terminal outcomes (closed set)

Every run ends in exactly one terminal outcome:

`COMPLETED`, `COMPLETED_WITH_LIMITATION`, `REJECTED`, `ABSTAINED`, `ESCALATED`, `FAILED_TECHNICAL`, `FAILED_SEMANTIC`, `FAILED_BUDGET`, `CANCELLED`, `COMPENSATED`, `MANUAL_DISPOSITION`.

## Relationship to profiles and patterns

A [profile](../04-profiles/README.md) (`EP#`) names a region of this coordinate space (a typical whole-run arrangement). A [pattern](../03-patterns/README.md) (`WP##`) is a reusable sub-solution that occupies characteristic values on a few axes. The descriptor records a run's exact coordinate; the profile and patterns explain and justify it.
