# Organize Reference Architectures Around Practitioner Jobs

## Date

2026-07-20

## Status

Proposed for working group review. Not yet adopted.

## Context

The initial workstream scaffold starts with two generic categories:
single-agent and multi-agent workflows. Those categories describe one
structural property of a system, but not the job the workflow performs, the
guarantees it must provide, or the reusable workflow techniques it composes.

Agent count is also often a design outcome. A practitioner can usually state
the need for approval, durable execution, bounded automation, or coordinated
handoff before deciding how many agents should implement it. Starting from
agent count therefore makes it difficult for a reader to route a use case to
the right architecture.

The workstream is also considering patterns as an output alongside reference
architectures. The relationship between those two artifact types should be
explicit rather than introduced only through new directories and examples.

## Decision

Organize reference architectures around recognizable practitioner jobs.

- A reference architecture is a complete composition of reusable patterns,
  required capabilities, boundaries, guarantees, and exit states for a job a
  practitioner can recognize and name.
- A pattern is an independently adoptable solution to one recurring workflow
  problem. Architectures compose patterns; patterns retain their own
  invariants, failure modes, and implementation examples.
- Single-agent and multi-agent are structural characteristics used within
  architectures, not sufficient top-level architecture categories on their
  own.
- Use cases and scenarios validate architectures. When a scenario does not
  fit, that may indicate a missing variant, a missing pattern, or a genuinely
  different job requiring another architecture.

The first example under this model is the single-agent process with human
approval. Its job is to let an agent propose an action while ensuring that a
human authorizes the exact action before a workflow-controlled executor causes
the protected effect. A policy-authorized operation has a different risk and
attribution topology and would be a separate architecture, not a variant of
this one.

## Rationale

- Practitioners begin with an operational need, not a predetermined number of
  agents.
- Job-oriented names communicate scope and guarantees more clearly than
  topology alone.
- Separating reusable patterns from complete compositions avoids repeating
  the same invariants and failure modes in every architecture.
- Agent count remains visible without becoming the primary taxonomy.

## Consequences

- Replace the generic single-agent scaffold with the first complete,
  job-oriented architecture.
- Remove the generic multi-agent scaffold. Add a multi-agent architecture only
  after the group selects a concrete practitioner job for it.
- Review future architecture proposals for a recognizable job, explicit
  guarantees, and a clear composition of reusable patterns.
- Review future pattern proposals for independence from any one architecture,
  product, or use case.

## Alternatives considered

### Keep single-agent and multi-agent as the top-level architectures

This preserves the initial scaffold, but groups workflows by implementation
shape rather than practitioner need. Each category would contain workflows
with materially different guarantees and operational behavior.

### Keep generic architectures and place job-oriented flows beneath them

This retains agent count as navigation, but creates two overlapping levels of
architecture and leaves unclear whether guarantees belong to the generic
parent, the specialized child, or a reusable pattern.

## Follow-up

- Confirm, revise, or reject this model through working group review.
- Select a concrete practitioner job before proposing a multi-agent
  architecture.
- Record any terminology changes requested during review in this note and the
  two templates.
