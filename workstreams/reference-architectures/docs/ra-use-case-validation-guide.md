# Validate a Reference Architecture with a Use Case

Use this guide to check whether one Reference Architecture (RA) fits one real use case. 
It is written for both people and coding agents. 
You do not need to be a technical contributor. 
Your result can be a small GitHub Issue or a focused pull request (PR).

For repository contribution rules, follow [CONTRIBUTING.md](../CONTRIBUTING.md).
If this guide and the contribution guide differ, the contribution guide takes precedence.

## What validation shows

Validation asks whether a real use case has the job and key boundary that this RA is designed to solve.

A `Validated` result means the RA is a good architectural fit for the use case.
It does not prove that an existing implementation already follows every RA requirement, 
such as a specific retry mechanism, storage design, or credential setup.

The RA provides the controls needed to implement the use case safely. 
A future implementation or conformance review can check whether those controls are actually in place.

When the use-case source clearly shows the RA's main job and defining boundary, mark it `Validated` even 
if it does not describe technical controls such as version hashes, credentials, retry settings, storage, or idempotency.
Those are controls the RA provides for a safe implementation, not facts required to prove architectural fit. 
Do not use a validation check to ask whether the current implementation already has a control that the RA itself provides.

## What you need

- One RA document.
- One use case from the [Use Case Inventory](../../critical-use-cases/use-case-inventory.md).
- Any source links or facts that support the use case.

**Evidence** means facts stated in the Use Case Inventory or its cited sources. 
Do not treat an illustrative example inside an RA as independent validation.

## How to validate any RA

1. Read the selected RA's purpose, `Is this your architecture?` checklist, boundaries, guarantees, exit states, and Validation record.
2. Compare those with one use case:
   - Does the RA solve the use case's main job?
   - Who does what: agent, workflow, person, and external system?
   - Does the use case have the boundary this RA requires?
   - Does the RA cover the important failure, wait, retry, recovery, or handoff path?
   - What does not fit, or what facts are still unknown?
3. Choose one result and produce the short validation output below.

Start with a short, plain-language answer. 
Technical detail is optional and should be added only when it changes the result or when a reviewer asks for it.
Keep `What matches` and `What is unknown` to no more than two bullets each.

## Validation checks and result

Use the selected RA's purpose, checklist, boundaries, and guarantees to create two or three simple checks by default. 
Do not add more than three checks. Check the use case's main job and defining boundary; do not require public evidence 
for every implementation detail unless that detail changes whether the RA fits. 
For each check, record what a `Yes`, `No`, or `Unknown` answer means.

The Use Case Inventory classification fields are evidence. Do not ignore an `Approval gate`, `Exception escalation`, 
or workflow-pattern value only because the prose does not describe every implementation detail. 
If a classification has an undocumented-rationale marker, treat the reason behind that classification as `Unknown` 
unless the use-case description or cited source explains it.

Use `No` only when the evidence clearly says that the RA has a different main job or incompatible boundary. 
Use `Unknown` when a key workflow fact is not stated, or when the description and classification fields conflict. 
Do not treat a missing implementation detail as `Unknown` when the use case already shows the RA's main job and key boundary.

| Result | Meaning | Next step |
|---|---|---|
| **Validated** | The use case clearly shows the RA's main job and key boundary. Missing implementation details do not block this result. | Open a small PR to add a Validation record row. |
| **Partial** | The main job fits, but available evidence clearly shows that a required RA boundary is missing. | Open a small PR to add a Partial row and describe the gap. |
| **No fit** | Available evidence clearly shows a different main job or incompatible boundary. | Open a small PR to add a No-fit row. This is useful evidence for a future RA. |
| **Candidate** | A key workflow fact is unknown, or the available sources conflict. | Open a GitHub Issue using the template below. |

## Choose an output

### Open a PR when the evidence is clear

A validation PR should normally update only the RA's `Validation record` table.
It may also add a source link or clarification to the use case when directly supported by evidence.

Do not change RA diagrams, patterns, taxonomy, or guarantees unless the PR is explicitly about that larger change.

### Open an Issue when you need help

Open an Issue when the result is `Candidate`, when source evidence is missing, or when you are unsure how to interpret a gap. 
A maintainer or coding agent can turn the Issue into a focused PR later.

## Copy/paste template for an Issue or PR

```md
## RA use-case validation

**Reference Architecture:** <RA link and name>
**Use case:** <Use Case Inventory link and name>
**Evidence:** <source links or facts>

### Validation checks

| Check | If yes | If no | Current evidence |
|---|---|---|---|
| <plain-language check based on this RA> | <what this supports> | <what this means for the fit> | Yes / No / Unknown |
| <second check> | ... | ... | ... |
| <optional third check> | ... | ... | ... |

### Result

`Validated` / `Partial` / `No fit` / `Candidate`

If the use-case description and its classification fields appear to conflict,
record the conflict as `Unknown` and use `Candidate` until the use-case owner
clarifies it.

**Why:** <one plain-language sentence explaining the result. Name the check or
fact that leads to this result.>

### Next step

<if any checks are Unknown, name who can answer them and ask only those
questions in plain language. If all checks are answered, state the proposed
repository update.>
```

Use the selected RA to create the checks. Do not reuse approval checks for an
RA that has a different job or boundary.

Examples:

| Selected RA | Plain-language checks may include |
|---|---|
| Human-approved operation | Does a person approve the proposed action? Can the agent perform that action directly? Is the approved version the version that is used? |
| Bounded autonomous remediation | Is the repair task small and clearly limited? What check decides that it worked? What happens after repeated failure? |
| Exception detection and escalation | Which team receives the escalation? What information is included? What happens if nobody responds? |
| Evidence-grounded briefing and delivery | Which sources are authoritative? Where is the briefing delivered? What happens if one source is unavailable? |

For a PR, include the proposed row:

```md
| Scenario | Source | Result | Notes |
|---|---|---|---|
| <use case> | <source> | Validated / Partial / No fit | <short reason> |
```

A new RA is stronger when several contrasting real use cases receive a `Validated` result.
