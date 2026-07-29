# Worked Examples

Status: Index

Examples serve two purposes at once:

1. they **validate** the architecture by exercising it on a realistic case; and
2. they are **few-shot exemplars** — a human or AI agent can read them as `Input → Reasoning → Architecture → Result` before designing something new.

## Run your own

To turn a new use case into a full solution — or to reproduce an existing one — follow
[HOW-TO-RUN.md](HOW-TO-RUN.md): copy [`_template/`](_template/README.md) to
`examples/<your-usecase>/`, fill in `use-case.md`, and paste the generic prompt into your
coding agent. `_template/` is scaffolding, not an exemplar.

The [`ticket-triage-routing/`](ticket-triage-routing/use-case.md) folder is a **prepared
demo seed**: a real use case from the WG landscape with only `use-case.md` filled in, so
anyone can watch the recipe produce a full solution from scratch. Run the recipe with
`<FOLDER>` = `ticket-triage-routing` to complete it.

## Exemplar shape

Every example follows the same triad, so it reads the same way for both audiences:

| File | Role | Corresponds to |
|---|---|---|
| `use-case.md` | Input — the business problem and requirements | what you are given |
| `rationale.md` | Reasoning — applying the six-step method | the [WDM](../ra/08-lifecycle/workflow-design-method.md) |
| `solution.md` | Architecture + Result — the design and the WDS | the [descriptor](../descriptor/README.md) |
| `<name>.wera.yaml` | Result — the machine-readable WDS **output**, co-located | the [schema](../descriptor/workflow-descriptor.schema.json) |

The WDS output sits **in the example folder**, next to the triad, so the deliverable is obvious. Detailed views (architecture, execution, sequence, contracts) sit under `views/` for readers who want depth.

## Examples

Each is a complete worked example — full triad, co-located WDS, and detailed views. They sit at different points on the determinism → agency spectrum, so together they show one vocabulary stretched across very different control models.

| Example | Profile · pattern | What makes it distinct |
|---|---|---|
| [invoice-processing](invoice-processing/README.md) | `EP2` · `WP02` | Model-assisted, **least-agentic**: the model only recommends a coding from a validated set; a reversible ERP draft (`EF2`) behind a human approval. |
| [gated-delivery-pipeline](gated-delivery-pipeline/README.md) | `EP2` · `WP07` | Workflow owns the stage sequence; a human **signs off at each authority boundary** before a high-impact deploy (`EF4`). Most governed. |
| [autonomous-maintenance-run](autonomous-maintenance-run/README.md) | `EP3` · `WP09` | A "night shift": the workflow admits one task, then **delegates a fenced agentic region** that loops against a deterministic gate and opens a PR — no human on the success path. |
| [autonomous-maintenance-run-agent-directed](autonomous-maintenance-run-agent-directed/README.md) | `EP4` · `WP09` | **Variant** of the run above: the same use case, but the architect asked for **more agency** — the agent owns the whole run, not just a region. See the comparison below. |

## The autonomy spectrum, one use case

The last two examples are the **same night-shift use case** at two points on the agency axis. The `EP3` version is what the method recommends by default (least-agentic, `DP-01`). The `EP4` version exists because, as the architect, **I asked for a more agent-directed design** — and the RA supported that by shifting a few coordinates and making the trade-off explicit, not by changing frameworks:

| Coordinate | `EP3` (default) | `EP4` (architect asked for more agency) |
|---|---|---|
| `control_flow_authority` | `workflow` | **`agent`** — the agent owns the whole run |
| `assurance` | `AS2` | **`AS3`** — raised to offset less deterministic sequencing |
| overlays / patterns | — | **`OV-01` + `WP07`** added: mandatory escalation and post-run human review |

Everything else — the reversible PR-only effect (`EF2`), impact (`IM2`), durability (`DUR4`) — stays the same. The extra agency is a **priced choice**: the `EP4` WDS records an explicit `DP-01` override and *tightens* the envelope, budgets, and effect ceiling rather than loosening them. That is the point of the spectrum — how much agency to use is a design decision, and its cost is visible in the coordinate.

## Try it yourself

The [`ticket-triage-routing/`](ticket-triage-routing/use-case.md) folder is a **prepared seed**: a real use case with only `use-case.md` filled in, so you can watch the [recipe](HOW-TO-RUN.md) produce a full solution from scratch. Run it with `<FOLDER>` = `ticket-triage-routing`.

## Choosing future examples

Future examples should **stress architecture areas not yet covered**, not repeat a control model in a new domain. Covered now: model-assisted (`EP2`), human-gated (`WP07`), bounded-agentic (`EP3`), and agent-directed (`EP4`). Still open: **fan-out/aggregation** and **cross-runtime handoff** (`WP11`/`EP7`). See the [roadmap](../ra/09-evolution/roadmap.md).
