# What a full solution contains

Status: Index

A **full solution** for a use case is the same set of files as
[invoice-processing](../invoice-processing/README.md) — the complete worked example. You
write only `use-case.md`; the rest is produced by following [HOW-TO-RUN.md](../HOW-TO-RUN.md).

| File | Author | Role |
|---|---|---|
| `use-case.md` | **you** (input) | Business problem, requirements, constraints, out-of-scope, success criteria. |
| `rationale.md` | agent | The six [WDM](../../ra/08-lifecycle/workflow-design-method.md) steps applied — the reasoning from use case to design. |
| `solution.md` | agent | The design in one picture, the result table, how the effect is protected, and why it passes conformance; links to the WDS. |
| `<name>.wera.yaml` | agent | The machine-readable [WDS](../../descriptor/README.md); validates against the [schema](../../descriptor/workflow-descriptor.schema.json). |
| `views/architecture.md` | agent | Architectural position, scope (in/out), logical architecture, actor responsibilities. |
| `views/execution.md` | agent | Stage-by-stage walkthrough and the least-agentic path. |
| `views/sequence.md` | agent | Interaction sequence diagram and the key authority boundary. |
| `views/contracts-and-state.md` | agent | Key contracts, authoritative state checkpoints, and the version/consistency rule. |
| `README.md` | agent | At-a-glance index: profile, primary + embedded patterns, overlays, highest effect, readiness / conformance. |

## Done means

- All files above exist in the example folder.
- The `*.wera.yaml` validates against the schema, and every code in it (and in the prose)
  exists in [registry.yaml](../../descriptor/registry.yaml).
- Relative links resolve (the depth matches invoice-processing: `../../ra/…` from the
  folder, `../../../ra/…` from `views/`).

A **lighter** deliverable is legitimate for a quick trial: `use-case.md` +
`<name>.wera.yaml` + `README.md`, with the triad and `views/` deferred — this is what the
two SDLC trial folders currently are. Prefer the full set for anything meant as a
reference exemplar.
