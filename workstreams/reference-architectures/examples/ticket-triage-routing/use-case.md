# Ticket triage & routing — Use Case

Status: Demo seed (input only)

*This is a **prepared demo input** — a real use case from the WG use-case landscape, with
only `use-case.md` filled in. It exists so anyone can watch WERA turn a use case into a
full solution: follow [../HOW-TO-RUN.md](../HOW-TO-RUN.md) with `<FOLDER>` =
`ticket-triage-routing`. The rest of the solution set is intentionally absent until you
run the recipe.*

## Business problem

On support-ticket creation, we want an agent to classify the ticket's intent and
sentiment, assign a priority label, and route it to the correct queue before a human agent
is paged. Today this triage is manual, slow, and inconsistent, and a mis-routed critical
ticket can sit unseen.

## Requirements

- Trigger on a new ticket event from the helpdesk.
- Classify intent and sentiment, and assign a priority label.
- Route the ticket to the correct queue.
- Read CRM context for the requester where useful.
- Routing must follow an explicit routing-rules configuration, not free choice.
- Keep an auditable record of the classification and the routing decision.

## Constraints and context

- Ticket content is untrusted user input.
- The helpdesk is the authoritative record for the ticket; the workflow must not become a
  shadow copy of it.
- A mis-route is correctable, but a silent drop on integration failure is the real harm to
  avoid.
- Runs must be effectively instant; no long human wait in the default path.
- Vendor-neutral: no dependency on a specific helpdesk product, model provider, or workflow
  engine.

## Out of scope

- Resolving or replying to the ticket.
- Any destructive or customer-visible action beyond setting labels and queue.
- Autonomous escalation/paging decisions that bypass the routing rules.

## Success criteria

Given a new ticket, the workflow produces a classified, priority-labelled ticket routed to
the correct queue with an audit record — or a clear escalated / failed-technical outcome if
classification is low-confidence or the integration fails. No ticket is silently dropped.
