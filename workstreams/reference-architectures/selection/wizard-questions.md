# Wizard Questions

Status: Mature

An ordered question set that drives pattern and profile selection. Each question maps answers to codes in the [classification coordinate](../model/classification.md) or directly to [patterns](../patterns/README.md), [profiles](../profiles/README.md), and [overlays](../overlays/workflow-overlays.md). The machine-readable form is [selection-logic.yaml](selection-logic.yaml).

Answer them in order. Early answers can short-circuit (e.g. a fully deterministic workflow lands on `WP00`/`EP1` immediately).

## Foundational

### Q01 — Is nondeterminism necessary?
Can explicit rules, code, templates, search, or conventional workflow logic meet the requirement with acceptable quality and maintenance?
- `yes` → recommend `WP00`, profile `EP1`, `nondeterminism: ND0`, stop unless another requirement re-opens it.
- `partially` → identify the exact residual semantic task; continue.
- `no` → continue.

### Q02 — What is the smallest semantic task?
Name the single narrowest task that genuinely needs a model. Sets `nondeterminism`: content→`ND1`, classification→`ND2`, selection→`ND3`, branch→`ND4`, tool→`ND5`, plan→`ND6`, delegation→`ND7`, open goal→`ND8`.

## Authority and topology

### Q03 — Who owns control flow?
`workflow` | `agent` | `human` | `event` | `external_runtime` → sets `control_flow_authority` and steers the profile (`EP1`/`EP2` workflow, `EP4` agent, `EP5` human, `EP6` event, `EP7` external_runtime).

### Q04 — What is the actor topology?
`none` | `single_agent` | `bounded_agentic_region` | `multi_agent` | `cross_runtime` → sets `actor_topology`; `bounded_agentic_region`→`WP09`/`EP3`, `multi_agent`→`WP10`, `cross_runtime`→`WP11`/`EP7`.

### Q05 — Is the decision/branch space closed?
- `closed` → prefer selection/branch patterns (`WP02`/`WP03`, `DP-07`).
- `open` → generation (`WP04`) or planning (`WP05`) with stronger validation.

### Q06 — Does the model select tools or actions?
- `no` → no tool-selection authority.
- `workflow-selected` → workflow picks tools.
- `agent-selected` → `TSL` with an allowed-tool set and effect ceiling; pushes toward `WP09`.

## Assurance

### Q07 — Can output be verified deterministically?
`full`/`partial`/`none` → sets `assurance` floor (`AS2` if full postconditions exist).

### Q08 — Is abstention acceptable?
- `yes` → require `UNC` on semantic steps.
- `no` → a fallback path (human or deterministic default) MUST exist.

### Q09 — Is human review or approval required?
`none` | `review` | `approval` | `multi-party` → `AS3`/`AS4`/`AS5`; `approval`+ triggers `OV-01` and `WP07`.

## Flow, state, duration

### Q10 — What is the flow shape?
single→`FS1`, linear→`FS2`, branch→`FS3`, loop→`FS4`, parallel→`FS5`, exception-only→`FS6`, long-running→`FS7`, event-driven→`FS8`, sub-runs→`FS9`.

### Q11 — Must the workflow wait or resume?
- completes in one process lifetime → `DUR0`/`DUR1`.
- waits for event/human, or may outlive a restart → `DUR2`+, triggers `OV-04` and `WP08`.

### Q12 — Is replayable execution history required?
- `yes` → `DUR4`, `OV-07`, component `RC-10`.

### Q13 — What state is authoritative?
Name the single system of record ([INV-002](../foundations/architecture-invariants.md)). Confirms `EVH`/`CHK` target.

## Effects

### Q14 — What is the highest effect level?
none→`EF0`, read→`EF1`, reversible write→`EF2`, transactional→`EF3`, high-impact/irreversible→`EF4`. `EF2`+ triggers `OV-02`.

### Q15 — Is the effect idempotent or compensable?
- idempotent → `IDM`.
- compensable → `OV-05`.
- neither → escalate controls; likely `AS4`+ and `EF4` handling.

## Untrusted input and boundaries

### Q16 — Does the workflow process untrusted content?
- `yes` → input controls before any semantic step ([INV-018](../foundations/architecture-invariants.md)); declare `XB-01`.

### Q17 — Which external boundaries are touched?
Any of `XB-01` security, `XB-02` identity, `XB-03` observability, `XB-04` governance, `XB-05` accuracy → list them in the descriptor.

## Impact and readiness

### Q18 — What is the impact of a wrong result or action?
`IM0`…`IM4` → sets the [readiness](../readiness/readiness-tiers.md) floor.

### Q19 — What readiness tier is required?
`RT0`…`RT4` (≥ the impact floor from Q18).

### Q20 — Is source and decision lineage required?
- `yes` → `AUD` + `EVH` on decisions and effects; relevant to `XB-04`.

## Delegation and handoff

### Q21 — Is any goal delegated to an agent or sub-run?
- `yes` → `DLG` with a bounded contract ([INV-008](../foundations/architecture-invariants.md)), `OV-06` budgets; `WP09`/`WP10`.

### Q22 — Does control cross an agent or runtime boundary?
- `yes` → `HND` portable envelope, `WP11`, profile `EP7`.

## From answers to a recommendation

The answers assemble into a coordinate (see [pattern-coordinates.md](pattern-coordinates.md)); the primary pattern and profile follow from the dominant characteristics, and triggered overlays/boundaries attach. The [selection-logic.yaml](selection-logic.yaml) encodes the exact algorithm.
