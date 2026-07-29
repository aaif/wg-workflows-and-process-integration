# Gated Multi-Stage Delivery Pipeline — Rationale

Status: Designed solution

*This is the reasoning from the six-step [Workflow Design Method](../../ra/08-lifecycle/workflow-design-method.md).* The workflow is deliberately more governed than the autonomous maintenance seed: agents may produce stage artifacts, but the workflow owns sequencing and people own authority at each gate.

## Step 1 — Understand the business outcome

**Outcome:** deploy exactly the version that passed the selected delivery track, every required stage gate, and named human approvals; record the complete run and a retrospective.

**Run boundary:** starts when a delivery request is accepted; ends in `COMPLETED`, `REJECTED`, `ESCALATED`, `CANCELLED`, `FAILED_TECHNICAL`, or `COMPENSATED` ([INV-004][invariants], [INV-005][invariants]). The workflow system of record owns run state and links to immutable artifacts, gate decisions, and deployment identity.

The authoritative decision owner is the named human approver supplied by the organisation's policy at each authority boundary. The workflow consumes that policy; it does not define approver membership.

## Step 2 — Identify the deterministic baseline

The workflow can deterministically accept and classify the request, select the short/full track from change-size policy, order stages, create stage records, fan out build and review, join their results, run per-language verification, compare digests, enforce gate positions, invalidate approvals after any version change, and decide terminal outcomes. These are the plain-rules floor (`WP00`, the Deterministic Baseline).

## Step 3 — Identify semantic gaps

Specialists need bounded model assistance for the content of requirements clarification, design alternatives, implementation suggestions, review explanations, and retrospective synthesis. The smallest semantic task is to produce a stage artifact or recommendation against a supplied scope and contract; models do not choose the next stage, select tools, approve gates, or deploy.

The resulting coordinate is:

```yaml
nondeterminism: ND1
control_flow_authority: workflow
actor_topology: single_agent
flow_shape: FS7
durability: DUR3
effect_level: EF4
assurance: AS4
impact: IM4
```

Production deployment is an irreversible/high-impact effect in this design (`EF4`/`IM4`), even though rollback is available as a compensating operation. The run spans days and waits for humans, so durable state and replay are mandatory.

## Step 4 — Choose the execution profile

The least-agentic viable whole-run profile is `EP2` (workflow-directed + model-assisted): the workflow engine owns all control-flow and stage transitions; bounded model calls assist content production. The five authorities are explicit:

| Authority | Holder |
|---|---|
| Control-flow | Durable workflow runtime and fixed stage policy |
| Decision | Workflow rules plus named human approvers at gates |
| Action-authorisation | Named human approver for each exact artifact/version |
| Execution | Constrained build, merge, and deployment adapters after approval |
| State | Workflow state store and execution history |

No agent may decide what runs next, authorise deployment, or mutate the authoritative state.

## Step 5 — Apply patterns and overlays

- Primary: `WP07` (Human-Supervised Action), because every authority boundary must bind approval to the exact artifact version.
- Embedded: `WP00` (Deterministic Baseline) for routing and gates; `WP01` (Bounded Model Step) for specialist artifact production; `WP08` (Durable Workflow Envelope) for the long-running run.
- Composition: `SEQ` fixed stage order; `PAR` for build/review fan-out with a deterministic join; `CHK` at every stage and gate; `WAI`/`TMO` for resumable human waits; `DVL` and `POL` before each gate; `IDM` and `RCP` for deploy ambiguity; `TXN` for the protected deploy; `CMP` for rollback/compensation; `EVH`/`AUD` for history.
- Overlays: `OV-01` human approval, `OV-02` protected effect, `OV-03` idempotency and reconciliation, `OV-04` durable wait, `OV-05` compensation, `OV-07` execution history.
- External boundaries: `XB-01` security/privacy, `XB-02` identity/delegation, `XB-03` observability, `XB-04` governance/risk, and `XB-05` accuracy/evaluation.

The workflow uses no autonomous planning or delegation; `WP05`, `WP09`, and `EP4` would give agents authority the use case explicitly excludes.

## Step 6 — Produce and check the WDS

The descriptor captures the fixed stage graph, the short/full branch, the build/review join, version-bound approval, protected deployment, rollback path, and terminal outcomes. Target readiness is `RT3` (business-critical production delivery); target conformance is `CL3` because the design declares overlays, boundaries, and readiness controls.

## Alternatives rejected

- `EP4` / `WP09`: rejected because agents must not own sequencing or gate decisions.
- `WP05` bounded plan + deterministic execute: rejected because the workflow already has a fixed stage plan; allowing an agent to plan would weaken the stated control model.
- `WP10` multi-agent delegation: rejected; specialist workers are bounded model steps, not goal-delegating agents.
- `EP1` alone: insufficient for requirements/design/review prose where bounded semantic assistance is useful.
- Treating deployment as `EF2` or `EF3`: rejected; production deployment is high-impact and needs human approval, constrained execution, idempotency, and compensation.

<!-- link definitions -->
[invariants]: ../../ra/01-foundations/architecture-invariants.md
