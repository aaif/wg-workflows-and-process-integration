# Primitive Catalog

Status: Mature

## Why this document exists

Primitives are the reusable logical building blocks a workflow is assembled from. Each has a stable three-letter mnemonic. The mnemonics describe **capabilities**, not agent count, so they apply unchanged across the whole determinism spectrum.

Each primitive lists: **purpose**, **determinism** (deterministic / nondeterministic / either), and **key controls**. Two primitives — `DLG` and `HND` — are added for agentic and cross-runtime execution.

The machine-readable list is in [registry.yaml](../descriptor/registry.yaml). Adding a new primitive requires justification per [DP-10](../foundations/design-principles.md).

## Entry and exit

- **TRG — Trigger.** Create a run from an API call, event, schedule, or message. *Deterministic.* Controls: authentication, replay protection, correlation ID, input-size limit, source identity, accepted schema, rate limits.
- **INP — Input intake.** Accept and canonicalise starting data and provenance. *Deterministic.* Controls: schema, classification tagging, untrusted-content handling ([INV-018](../foundations/architecture-invariants.md)).
- **OUT — Output emission.** Emit the accepted result to a caller or downstream. *Deterministic.* Controls: output schema, redaction, audit.
- **FSK — Finalize / sink.** Reach and record a terminal outcome. *Deterministic.* Controls: closed terminal-outcome set, evidence.

## Deterministic processing

- **DFN — Deterministic function.** Pure computation from inputs. *Deterministic.*
- **BRL — Business rule.** Apply explicit rules/policy. *Deterministic.* Controls: versioned rule set.
- **XFM — Transform.** Map/normalise/format data. *Deterministic.*
- **SCH — Schema / arithmetic validation.** Check structure, totals, types. *Deterministic.*

## Semantic (nondeterministic)

- **AIN — Analyze / interpret.** Extract structure or meaning from content. *Nondeterministic.* Controls: output contract, evidence locations, confidence.
- **CLS — Classify.** Assign a closed-set label. *Nondeterministic.* Controls: fixed label set, abstention.
- **GEN — Generate.** Produce an artifact not fully specifiable by rules. *Nondeterministic.* Controls: format, content constraints, provenance, downstream validation.
- **REC — Recommend.** Propose a decision or action for adjudication. *Nondeterministic.* Controls: candidate set, explanation, confidence, abstention.
- **PLN — Plan.** Produce a bounded sequence of steps to attempt. *Nondeterministic.* Controls: allowed step vocabulary, budget, exit states.
- **TSL — Tool selection.** Choose a tool/capability to invoke. *Nondeterministic.* Controls: allowed-tool set, effect ceiling.

## Context

- **CAS — Context assembly.** Select and package context for a step. *Deterministic.* Controls: provenance, size/classification limits.
- **RET — Retrieval.** Read reference data / documents. *Deterministic.* Controls: least privilege, query bounds.
- **SME — Session memory.** Hold within-run working memory. *Either.* Controls: not a system of record ([INV-002](../foundations/architecture-invariants.md)).
- **DME — Durable memory.** Persist cross-run learned/reference memory. *Either.* Controls: provenance, staleness.
- **INS — Instruction / prompt context.** Supply governing instructions to a model. *Deterministic.* Controls: versioning.

## Action

- **TRO — Tool read-only.** Invoke a read-only external capability (`EF1`). Controls: least privilege, output sanitisation.
- **TRW — Tool reversible write.** Invoke a reversible external write (`EF2`). Controls: policy, idempotency, compensation, postcondition check.
- **THI — Tool high-impact.** Invoke a high-impact/irreversible action (`EF4`). Controls: deterministic validation, approval, segregation, strong evidence.
- **TXN — Transactional write.** Perform a transactional write (`EF3`). Controls: transaction semantics, concurrency, commit evidence, reconciliation.

## Control flow

- **SEQ — Sequence.** Ordered steps. *Deterministic.*
- **DBR — Deterministic branch.** Rule-selected branch. *Deterministic.*
- **ABR — Agent-selected branch.** Model-selected among allowed branches. *Nondeterministic.* Controls: closed branch set.
- **PAR — Parallel.** Fan-out with declared join. *Deterministic.* Controls: join semantics (all/quorum/first/deadline), late-result treatment.
- **LOP — Loop.** Bounded iteration/refinement. *Either.* Controls: max iterations, progress/exit.
- **RTY — Retry.** Re-attempt on a retry class. *Deterministic.* Controls: retry class, idempotency ([INV-011](../foundations/architecture-invariants.md)).
- **WAI — Wait.** Pause for time, human, or event. *Deterministic.* Controls: durable state, correlation, expiry.
- **TMO — Timeout.** Bound elapsed time. *Deterministic.* Controls: explicit outcome on expiry.
- **CAN — Cancel.** Cancel work / a run. *Deterministic.* Controls: cleanup, terminal outcome.

## Assurance

- **DVL — Deterministic validation.** Postcondition/rule check on a proposal. *Deterministic.*
- **MVL — Model-assisted validation.** Second-model or evaluator check under a fixed contract. *Nondeterministic.*
- **POL — Policy check.** Authorisation / permitted-effect decision. *Deterministic.*
- **HRV — Human review.** Human inspects and comments; not a final gate. *Human.*
- **APR — Human approval.** Human authorises an exact version/action. *Human.* Controls: identity, exact-version binding ([INV-013](../foundations/architecture-invariants.md)).
- **UNC — Uncertainty handling.** Abstain / escalate when confidence is insufficient. *Either.*

## Reliability

- **CHK — Checkpoint.** Persist accepted state for recovery. *Deterministic.*
- **IDM — Idempotency.** Enforce duplicate protection for effects. *Deterministic.*
- **CBR — Circuit breaker.** Stop calling a failing dependency. *Deterministic.*
- **DLQ — Dead-letter.** Divert unprocessable work. *Deterministic.*
- **CMP — Compensation.** Apply a compensating action after a partial effect. *Deterministic.*
- **RCP — Reconciliation.** Resolve ambiguous effect outcomes against the target system. *Deterministic.*

## Observability and evaluation

- **TRC — Trace.** Emit execution trace signals. *Deterministic.* (Signal consumption is `XB-03`, Observability WG.)
- **AUD — Audit.** Record an auditable decision/effect entry. *Deterministic.*
- **EVH — Execution history.** Record accepted transitions as the workflow system of record. *Deterministic.* (Charter Scope B; distinct from observability.)
- **CST — Cost accounting.** Track cost/budget consumption. *Deterministic.*
- **FDB — Feedback capture.** Capture outcome feedback for later improvement. *Deterministic.*

## Delegation (agentic / multi-agent / cross-runtime)

- **DLG — Delegate goal.** Hand a bounded sub-goal to an agent or sub-run under an explicit contract. *Either.* Controls: goal, allowed tools/data, max effect level, budgets, exit states, state owner ([INV-008](../foundations/architecture-invariants.md)).
- **HND — Handoff / control transfer.** Transfer control between actors or runtimes with a portable envelope. *Deterministic.* Controls: run/task identity, accepted context, capability + effect permissions, budget/deadline, expected result, state-ownership.
