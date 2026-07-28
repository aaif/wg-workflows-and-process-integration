# <Use-case name> — Use Case

Status: Draft input

*This is the **Input** to the design: the business problem, exactly as a stakeholder might
hand it over. Fill in every section below — this file is the only thing you must write by
hand. Everything else in the full solution is produced from it by following
[HOW-TO-RUN.md](../HOW-TO-RUN.md). Delete these italic hints as you go.*

## Business problem

*What is the outcome someone wants, in plain business language? Who receives the result,
and what is painful about doing it today? Two or three sentences. State clearly what you
are **not** trying to automate if that is a live question (e.g. "we prepare the draft; we
do not pay").*

## Requirements

*A bullet list of what the workflow must do. Include, where relevant:*

- *how work enters (inputs, formats, channels);*
- *what must be produced (the deliverable and its acceptance form);*
- *any decisions that must be made, and by whom;*
- *any externally visible action (a write, a send, a deploy) and whether a human must
  approve it first;*
- *what evidence / audit trail must survive.*

## Constraints and context

*The things that shape the architecture. Consider:*

- *which inputs are **untrusted**;*
- *which system is the **authoritative record** (the workflow must not become a shadow
  copy of it);*
- *how reversible a wrong result is, and how costly to unwind;*
- *whether the run may need to **wait** (for a human, an event, a delay) and survive
  restarts;*
- *vendor-neutrality or platform constraints.*

## Out of scope

*What this workflow explicitly does **not** cover, so the design stays bounded. Name the
tempting-but-excluded actions (e.g. autonomous posting, self-approval, unrestricted
access).*

## Success criteria

*One paragraph: given a valid input, what does a good run produce, and what is the closed
set of ways a run can end (completed / rejected / abstained / escalated / failed / …)?
This becomes the run boundary in Step 1 of the method.*
