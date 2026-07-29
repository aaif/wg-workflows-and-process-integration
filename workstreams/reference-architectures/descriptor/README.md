# The Workflow Descriptor

Status: Mature

## What this is

The **workflow descriptor** is the machine-readable form of a **Workflow Design Specification (WDS)** — the artifact both a human architect and an AI agent produce by applying WERA to a use case. It is the shared output that makes the [dual-mode acceptance test](../docs/acceptance-test.md) possible.

One descriptor is a single `*.wera.yaml` file with three blocks:

| Block | Contains | Populated from |
|---|---|---|
| `intake` | the business use case (outcome, inputs, nondeterminism justification, requested authority, assurance, side-effects, operations) | the [wizard questions](../ra/05-selection/wizard-questions.md) |
| `design` | the resolved architecture (coordinates, five-authority allocation, primitive graph, effects, selected profile + patterns, overlays, boundaries, readiness, conformance target) | [selection logic](../ra/05-selection/selection-logic.yaml) + review |
| `recommendation` | rationale, alternatives rejected, mandatory primitives, required views, exceptions | the designer's reasoning |

## Files here

- **[workflow-descriptor.schema.json](workflow-descriptor.schema.json)** — JSON Schema (draft 2020-12) that every descriptor validates against. All codes are constrained to the registry vocabulary.
- **[workflow-descriptor.reference.md](workflow-descriptor.reference.md)** — field-by-field human documentation.
- **[registry.yaml](registry.yaml)** — the entire coded vocabulary as data, so an agent can load WERA as data rather than prose.

The WDS instances themselves (`*.wera.yaml`) live **with their worked examples**, not here — each output sits next to the use case it answers, in [`examples/`](../examples/README.md):

| WDS | Example | End of the spectrum |
|---|---|---|
| [invoice-processing.wera.yaml](../examples/invoice-processing/invoice-processing.wera.yaml) | [invoice processing](../examples/invoice-processing/README.md) | model-assisted, least-agentic (`EP2`/`WP02`) |
| [gated-delivery-pipeline.wera.yaml](../examples/gated-delivery-pipeline/gated-delivery-pipeline.wera.yaml) | [gated delivery pipeline](../examples/gated-delivery-pipeline/README.md) | human-gated, high-impact deploy (`EP2`/`WP07`) |
| [autonomous-maintenance-run.wera.yaml](../examples/autonomous-maintenance-run/autonomous-maintenance-run.wera.yaml) | [autonomous maintenance run](../examples/autonomous-maintenance-run/README.md) | bounded agentic region (`EP3`/`WP09`) |
| [autonomous-maintenance-run-agent-directed.wera.yaml](../examples/autonomous-maintenance-run-agent-directed/autonomous-maintenance-run-agent-directed.wera.yaml) | [agent-directed variant](../examples/autonomous-maintenance-run-agent-directed/README.md) | agent owns the run (`EP4`/`WP09`) |

See the [examples index](../examples/README.md) for how these span the autonomy spectrum, and [HOW-TO-RUN](../examples/HOW-TO-RUN.md) to generate one yourself.

## Why it matters

```mermaid
flowchart LR
    subgraph inputs [Given to a human or AI]
      REG[registry.yaml]
      SCH[schema + reference]
      SEL[selection-logic.yaml]
      PB[playbook / WDM]
      UC[business use case]
    end
    inputs --> WDS[Valid *.wera.yaml WDS]
    WDS --> CHK[Conformance check CL0-CL3]
    WDS --> IMPL[Implementation]
```

Because the design is data, three things become mechanical: **authoring** (fill the schema), **checking** ([conformance](../ra/07-readiness/conformance.md) `CL0`–`CL1` can be validated automatically), and **comparing** (two WDS artifacts for the same use case can be diffed — the heart of the acceptance test).

## Validating a descriptor

Any JSON-Schema validator works. For example, with a YAML-aware validator:

```bash
# from this descriptor/ directory; using ajv-cli (npm) with a YAML loader, or convert YAML->JSON first
npx ajv-cli validate -s workflow-descriptor.schema.json -d ../examples/invoice-processing/invoice-processing.wera.yaml
```

or in Python:

```python
import json, yaml, jsonschema
schema = json.load(open("workflow-descriptor.schema.json"))
doc = yaml.safe_load(open("../examples/invoice-processing/invoice-processing.wera.yaml"))
jsonschema.validate(doc, schema)
```
