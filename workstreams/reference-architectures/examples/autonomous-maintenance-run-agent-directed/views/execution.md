# Agent-Directed Maintenance Run — Execution

| Stage | Work | Authority / guard |
|---|---|---|
| 1. Envelope | `TRG`, `INP`, `CHK` record objective digest, fixed scope, tools, budgets, terminal outcomes, and a new sandbox. | Durable envelope, not agent memory. |
| 2. Direct the run | Agent uses `PLN` / `TSL` to choose diagnostics, edits, gate runs, waits, or an escalation proposal. | Whole-run agent control-flow. |
| 3. Execute capability | `TRO` reads/runs gates; `TRW` requests scoped sandbox edit. | Gateway and `POL` enforce allow-list/effect ceiling. |
| 4. Wait and verify | `WAI` resumes CI durably; `DVL` checks gate result, scope manifest, and exact digest. | Gate is deterministic arbiter. |
| 5. Meter | `CST` checks strict independent limits after each action and effect. | First breached limit stops/escalates. |
| 6. PR or escalation | Green exact result gets independent `POL`, `IDM`, PR `TRW`, and `RCP` if uncertain. Failure/scope/budget risk gets `HRV`. | Agent never self-authorises. |
| 7. Close | `EVH` records accepted evidence and `FSK` closes once. | External state owner validates outcome. |

Unlike EP3, the agent decides whether and how to move among stages 2–6. It cannot skip gateway/policy/validation checks: they are mandatory external transition guards, and an attempted bypass is technical failure or escalation.
