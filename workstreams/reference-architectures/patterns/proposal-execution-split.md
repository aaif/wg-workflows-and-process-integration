# Proposal/Execution Split

**Solves:** Enforcing authorization and attribution at the protected-effect boundary when intent comes from a probabilistic agent \
**Used in:** [Single-agent process with human approval](../architectures/single-agent-human-approval.md) \
**Requires capabilities:** Agent · authorization gate · workflow-controlled executor · audit log \
**Related patterns:** [Human approval gate](human-approval-gate.md) · [durable wait](durable-wait.md)

## Problem

An agent step is probabilistic; the enterprise needs enforceable controls at
the point of effect. That need arrives in several forms, any one of which is
sufficient:

- **Risk exposure** — the effect is costly, dangerous, or hard to reverse
  (a refund, a configuration change, an outbound message).
- **Audit exposure** — regulation or policy requires proving, after the
  fact, exactly what was authorized, by which authority, and what then ran.
- **Attribution of authority** — an accountable human or versioned policy
  must own the authorization decision; "the model decided" is not an answer
  the organization can give.

A probabilistic actor cannot carry any of these guarantees. Authorization
has to attach to *exactly* what will happen, and what happens has to be
*exactly* what was authorized — which is impossible if the agent both
decides and acts.

## Why this is hard

- Letting the agent execute directly is the shortest path and removes the
  entire safety story.
- Time can pass between proposal and authorization; the world can change
  before an authorized proposal executes.
- An absent, expired, or failed authorization decision can accidentally be
  treated as permission unless the gate fails closed.
- Retried execution after approval must not repeat the effect.
- Human and policy authorization produce different evidence; collapsing them
  into one attribution model makes at least one of them unauditable.

## Solution

One precept, three separations: **intent, authorization, and execution belong
to distinct roles, and each is separately recorded.**

```text
  proposer (agent)            authorization authority       executor (system)
        │                             │                            │
        ▼                             ▼                            ▼
   proposal ─────────► gate: authorize this exact ─ yes ─► workflow-controlled
   (immutable data,         proposal?                      execution of the
    not an action)            │                            authorized proposal
                              └─ no / invalid ──► terminal or     │
                                 recovery path                    ▼
                                                                effect
  ─────────────────────────────────────────────────────────────────────────
    system of record: proposal · authority + decision evidence · effect
```

The agent proposes data, not an action. An authorization authority — such as
a human principal or a versioned policy — decides whether that exact proposal
may proceed. A workflow-controlled executor, which the agent cannot invoke,
performs it. The system of record ties the proposal, authorization evidence,
and effect to one run. Patterns layered on this one define the authority's
specific decision and attribution model.

## Invariants (must hold in any implementation)

- The agent cannot cause the protected effect: it does not hold the capability
  or credentials that the executor uses for that effect.
- Authorization binds to an exact, immutable proposal (version or hash). What
  was authorized is what executes — nothing else.
- Only an explicit, valid authorization decision permits execution. An absent,
  expired, denied, or failed decision never defaults to allow.
- Execution is workflow-controlled and idempotent given an authorized
  proposal.
- Intent, decision, and effect share one run identity in the system of
  record — the full chain of custody is reconstructable.
- The decision evidence identifies the authorization authority: a human
  principal, or a policy identity and version together with its evaluated
  inputs. The authorizing authority is distinct from the agent that proposed
  the action.

## Failure modes when violated

- Agent can invoke the protected effect → the gate can be bypassed and
  authorization happens after the risk, if at all.
- Proposal mutable after authorization → the authority authorized something
  other than what ran (time-of-check/time-of-use).
- Missing or failed decision defaults to allow → the system executes without
  affirmative authorization.
- Non-idempotent executor → retrying an authorized action repeats the effect.
- Human and policy evidence share an underspecified "approved by" field → the
  audit trail cannot reconstruct who or what actually authorized the effect.

## Implementation approaches (illustrative, not requirements)

What varies across implementations of this pattern is **where the
separation is enforced**. The enforcement points compose — and the first
invariant (the agent cannot invoke the protected effect) is only real if the
capability or identity layer enforces it. Orchestration alone can be bypassed
by an agent that holds the executor's credentials. Each row is therefore one
contributing control, not a complete implementation of the pattern.

| Enforced at | Documented mechanism | What it provides | What the implementation must add |
|---|---|---|---|
| Proposal artifact | [Terraform saved plan](https://developer.hashicorp.com/terraform/cli/commands/plan#out-filename) | Separates planning from application and lets `apply` execute the operations in a specific saved plan | Authorization and identity controls around who may apply; protected storage for the plan; one run identity joining decision and effect |
| Orchestration layer | [LangGraph interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts) | Checkpoints state and pauses before a separately modeled continuation | A durable checkpointer, immutable proposal binding, authenticated authorization evidence, and an executor identity unavailable to agent nodes |
| Identity layer | [AWS IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) | Gives separately assumable identities distinct permission sets and temporary credentials | A trust policy that prevents the agent from assuming the executor role; workflow binding between authorization and role assumption; audit correlation |
| Protected target | [GitHub protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches#about-branch-protection-settings) | Can require approving reviews, dismiss stale approvals after changes, restrict pushes, and disallow bypass | Correct branch-rule configuration, authenticated reviewers, and correlation between the reviewed revision and downstream effects beyond the repository |

## Known uses outside agents

Terraform `plan`/`apply` · pull-request review → merge · payment
authorization/capture · ITIL change management (RFC → CAB approval →
scheduled change). Four industries independently converged on separating
intent from execution wherever the actor proposing a change is not trusted
to perform it unilaterally.

The agent delta: the agent is the newest actor in that category, and the
pattern transfers unchanged. What is new is that the proposer's output is
probabilistic and arrives at machine volume — so the gate must be
structural (enforced by permissions) rather than social (enforced by
convention).
