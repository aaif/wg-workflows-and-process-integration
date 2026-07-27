# Core Concepts

Status: Mature

Shared vocabulary used throughout WERA. These concepts are intended to remain valid across deterministic, model-assisted, agentic, human-driven, and cross-runtime workflows.

## Workflow run

A **workflow run** is one coordinated execution toward an intended outcome under a declared set of constraints and authority boundaries. It is the central unit of the architecture.

A run may include deterministic steps, rules, model calls, bounded agentic regions, delegated agents, human tasks, waits, external events, tool calls, and effects. None of these alone defines the run.

### Minimum conceptual record

A workflow run should make the following addressable:

| Element | Meaning |
|---|---|
| Run identity | Stable correlation for this execution |
| Intended outcome | The business or operational result being pursued |
| Governing definition or plan | The versioned structure currently accepted for execution |
| Accepted input | Canonical starting data and provenance |
| Current authoritative state | What has been accepted as completed, pending, blocked, or terminal |
| Pending work | Tasks, waits, approvals, delegated goals, or expected events |
| Authority allocation | Who may decide, authorise, execute, and record each class of action |
| Capability boundary | Tools, actors, data, effects, and budgets available to the run |
| Effect record | Requested, authorised, attempted, confirmed, and reconciled effects |
| Execution history | Accepted transitions and their evidence |
| Terminal outcome | The final technical and business disposition |

### Run boundary

The run boundary should be chosen around an outcome that needs coordinated state and recovery. It should not be defined merely by an HTTP request, one model invocation, one agent conversation, or one queue message.

## Workflow definition vs run

A reusable **workflow definition** describes allowed behaviour. A **workflow run** is one execution of a version of that definition. Dynamic planning may extend or revise work within a run, but accepted plan versions, constraints, and completed effects remain part of the run record.

## Step

A **step** is an addressable unit of work with a declared contract (input, output, actor/runtime, authority, allowed capabilities and effects, outcomes, timeout/retry class, evidence). A step may be implemented by code, a model, an agent, a human, a tool, or another runtime.

## Proposal vs accepted transition

A step result may be a **proposal** rather than an **accepted transition**. Probabilistic output (from a model or agent) is always a proposal until it satisfies the relevant schema, policy, evidence, and authority boundary and is committed as an accepted transition. This distinction is the backbone of [effect protection](../overlays/workflow-overlays.md).

## The five authorities

"Who is in control" is too coarse. WERA separates control into five authorities that may be held by different actors for the same step:

| Authority | Question |
|---|---|
| Control-flow authority | Who determines the next valid step or transition? |
| Decision authority | Who makes or accepts the authoritative business decision? |
| Action-authorisation authority | Who permits an externally visible action? |
| Execution authority | Which component technically performs the action? |
| State authority | Which system records accepted workflow state? |

Full treatment: [reference model](../model/reference-model.md).

## Execution state and system of record

**Execution state** records what the workflow has accepted as true about progress. The workflow **system of record** owns accepted progress and recovery state. It is distinct from **model context** (selected information supplied for reasoning, which may be incomplete or transient) and from external business records (ERP, document stores) which it may reference.

## Effect

An **effect** is an externally visible action. Effects are classified by level ([`EF0`–`EF4`](../model/classification.md)) and are protected: authorisation, execution, idempotency, and confirmation are explicit and separated from reasoning.

## Actor topology

The arrangement of actors in a run — `none`, `single_agent`, `bounded_agentic_region`, `multi_agent`, `cross_runtime` — is **one classification axis**, not the organising principle of the architecture. See [classification](../model/classification.md).

## Bounded agentic region

A **bounded agentic region** delegates a goal and limited action-selection authority to an agent, under an explicit contract (goal, accepted context, allowed tools/data, maximum effect level, budgets, expected outcomes, exit states, state owner, return conditions). The surrounding workflow remains responsible for accepting the region's outcome.

## Control transfer / handoff

A **control transfer** is an explicit transition of work between actors or runtimes, carrying run/task identity, delegated goal, accepted context, allowed capabilities, effect permissions, budget/deadline, expected result and exit states, and state-ownership. An event may trigger reconsideration of a pending transition without automatically acquiring control-flow authority.

## Workflow Design Specification (WDS)

The **WDS** is the artifact produced by applying WERA to a use case: a machine-readable [descriptor](../descriptor/README.md) (`*.wera.yaml`) plus its human-readable rendering. It is the shared output of both human mode and AI mode.

## Terminal outcome

Technical completion and business acceptance are distinguishable. A run may finish technically while producing a business outcome such as rejected, abstained, escalated, or manually disposed. The closed set of terminal outcomes is defined in [classification](../model/classification.md).
