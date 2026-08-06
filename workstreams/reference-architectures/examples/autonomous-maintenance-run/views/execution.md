# Autonomous Maintenance Run — Execution

Status: Design example

## Stage walkthrough

| Stage | Work | Accepted transition / authority |
|---|---|---|
| 1. Trigger and bind | `TRG` / `INP` accepts one scheduled or directly submitted task and fixes its task contract. | Workflow opens one run. |
| 2. Deterministic admission | `BRL` verifies label, declared scope, repository, duplicate exclusion, and policy; `POL` selects admit, reject, or escalate. | Rules decide; agent has not yet run. |
| 3. Fresh sandbox checkpoint | `CHK` records admitted task and sandbox generation; fresh isolated sandbox is provisioned. | Workflow state authority. |
| 4. Delegate fence | `DLG` gives the agent one goal, result schema, allow-listed tools, effect ceiling, and multidimensional budget. | Workflow lends local control only. |
| 5. Repair attempt | Agent uses `PLN` and `TSL` to choose allowed diagnostics/edits. `TRW` changes only the sandbox; `TRO` runs allowed checks. | Agent is locally dynamic; tool gateway enforces contract. |
| 6. Durable gate wait | If CI is asynchronous, `WAI` holds a durable correlation and resumes from a checkpoint. | Workflow controls wait/resume. |
| 7. Validate gate and manifest | `DVL` checks deterministic green result, task scope, changed-file manifest, and final change digest. | Gate/policy decide success; green but over-scope does not pass. |
| 8. Repair loop or safe exit | On permitted red feedback, `LOP` re-enters repair only after `CST` confirms all budgets remain. Repeated failure or over-scope escalates; an exhausted ceiling yields `FAILED_BUDGET`. | Deterministic budget and disposition rules. |
| 9. Return and open PR | `HND` returns the valid result. `IDM` binds exact task/change digest; policy authorises a `TRW` PR creation. Ambiguous response goes to `RCP`. | Separate PR adapter, constrained credentials. |
| 10. Record and close | `EVH` records attempts, gate evidence, PR identity or non-success disposition; `FSK` closes the run. | Workflow closes exactly once. |

## Least-agentic path

No agent is needed to reject an ineligible/duplicate/out-of-scope task, provision/discard a sandbox, run the gate, wait for CI, meter costs, check the manifest, create the exact PR intent, reconcile an uncertain PR response, or close the run. The agent is used only for the residual dynamic repair sequence. This satisfies least-agentic composition (`DP-01`) while retaining the autonomous repair capability actually required.

## Stop rules

The first exhausted ceiling among task count, iterations, tokens, tool calls, wall-clock time, effect count, or allowed scope stops the region. A red gate is feedback, not permission to continue forever. A green gate with a manifest outside contract is an escalation, not success. Every stop is checkpointed with the evidence needed for a human to review what was attempted.
