# Pattern Coordinates

Status: Mature

## Idea

A workflow run is located at a **coordinate** across the eight [classification axes](../02-architecture-model/classification.md). The [wizard answers](wizard-questions.md) assemble that coordinate; the coordinate then suggests candidate [patterns](../03-patterns/README.md) and a [profile](../04-profiles/README.md). Coordinates support selection and comparison — they do not replace review.

## The coordinate

```yaml
coordinates:
  nondeterminism: ND0..ND8
  control_flow_authority: workflow | agent | human | event | external_runtime
  actor_topology: none | single_agent | bounded_agentic_region | multi_agent | cross_runtime
  flow_shape: FS1..FS9
  durability: DUR0..DUR4
  effect_level: EF0..EF4
  assurance: AS0..AS5
  impact: IM0..IM4
```

## Coordinate → candidate pattern (dominant axis)

The primary pattern usually follows the dominant characteristic; the full precedence is encoded in [selection-logic.yaml](selection-logic.yaml).

| Dominant characteristic | Primary pattern | Typical profile |
|---|---|---|
| `nondeterminism: ND0` | WP00 | EP1 |
| Content/label (`ND1`–`ND2`) | WP01 | EP2 |
| Selection over closed set (`ND3`) | WP02 | EP2 |
| Branch selection (`ND4`) | WP03 | EP2 |
| Open generation | WP04 | EP2 |
| Planning (`ND6`) | WP05 | EP4 |
| Exception-only (`FS6`) | WP06 | EP2 |
| `actor_topology: bounded_agentic_region` | WP09 | EP3 |
| `actor_topology: multi_agent` (`ND7`) | WP10 | EP4 |
| `actor_topology: cross_runtime` | WP11 | EP7 |

## Modifiers attach on top

Independent of the primary pattern:

- `durability ≥ DUR2` → wrap in **WP08** (durable envelope), overlay `OV-04`.
- `assurance ≥ AS4` → gate with **WP07** (human-supervised action), overlay `OV-01`.
- `effect_level ≥ EF2` → apply overlay `OV-02` (protected effect).
- `durability = DUR4` → overlay `OV-07` (execution history).

## Worked coordinate — invoice processing

```yaml
coordinates:
  nondeterminism: ND3            # selection among validated GL/PO candidates
  control_flow_authority: workflow
  actor_topology: single_agent
  flow_shape: FS7                # long-running with a human-review wait
  durability: DUR3
  effect_level: EF2              # unposted ERP draft = reversible write
  assurance: AS4                 # human approval before handoff
  impact: IM2
# =>
primary_pattern: WP02
embedded_patterns: [WP00, WP01, WP07]
lifecycle_envelope: WP08
profile: EP2
overlays: [OV-01, OV-02, OV-07]
```

This is exactly the design captured in [descriptor/examples/invoice-processing.wera.yaml](../../examples/invoice-processing/invoice-processing.wera.yaml).
