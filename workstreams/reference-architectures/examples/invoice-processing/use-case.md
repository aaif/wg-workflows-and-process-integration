# Invoice Processing — Use Case

Status: Mature worked example

*This is the **Input** to the design: the business problem, exactly as a stakeholder might hand it over.*

## Business problem

The Accounts Payable team receives supplier invoices through an inbox and a submission portal. Each invoice must be read, matched against purchase orders and receipts, coded to the correct GL accounts and accounting dimensions, and turned into an AP entry — today this is slow and inconsistent, and errors are expensive to unwind after payment.

We want to automate the preparation of a **validated, unposted AP draft** and route it to a human reviewer for a final decision. We are **not** automating payment.

## Requirements

- Accept invoices as email attachments or portal uploads (PDF, images).
- Extract header and line-item data reliably, keeping evidence of where each value came from.
- Match to the correct purchase order, verify vendor and legal entity, apply price/quantity tolerances, match receipts, and inherit PO coding where valid.
- For lines that cannot be resolved by rules, propose the most likely GL account / PO line from the **allowed** candidates — or abstain.
- Create an **unposted** draft in the ERP; never post or pay automatically.
- A human reviewer must approve the **exact** draft before it moves to the standard AP process.
- Keep a record of what happened and why, sufficient for audit.

## Constraints and context

- Invoice attachments are **untrusted** content.
- The ERP is the authoritative record for the posted document; the workflow must not become a shadow ledger.
- A wrong coding is **material but correctable** before payment.
- The workflow may need to wait hours or days for a reviewer and must survive restarts in the meantime.
- Must be vendor-neutral: no dependency on a specific ERP, model provider, or workflow engine.

## Out of scope

- Vendor-master or banking changes; PO creation/modification.
- Payment scheduling or release.
- Autonomous posting; agent self-approval.
- Unrestricted ERP access.

## Success criteria

Given an accepted invoice, the workflow produces either a reviewable, evidence-backed unposted draft for approval, or a clear rejected / held / manual-disposition outcome — with authoritative state and an audit trail throughout.
