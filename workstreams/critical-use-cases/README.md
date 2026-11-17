# Critical Use Cases

**Workflows & Process Integration WG · Agentic AI Foundation**

## What this workstream is for

Our workstream is responsible for identifying reusable workflow patterns (“use cases”) that emerge from real deployed agentic applications, evidenced by sourced examples. 

This workstream produced an inventory of explicit use cases — specific, named, real-world workflows drawn from production deployments. Each entry is evidence of a real implementation choice. From that inventory, readers can identify workflow shapes: recurring combinations of classification dimensions that appear across multiple industries and contexts. The inventory supports creating a prioritized set of workflow shapes, potentially based on pattern frequency and industry breadth. This prioritization can be readily derived just from the inventory.

## Contents

- [`schema-agentic-use-cases.md`](./schema-agentic-use-cases.md) — Column definitions, classification values, and open questions
- [`use-case-inventory.md`](./use-case-inventory.md) — The inventory table


## Evidentiary standard

Each Notes cell in the [`use-case-inventory.md`](./use-case-inventory.md) cites vendor product pages or primary announcements with confirmed production deployment, dated either by publication or by when the source was retrieved. Citations must be publicly accessible and independently verifiable — personal knowledge of a deployment, however well-founded, is not sufficient.

At least one verified citation is required per use case. Three is the target.

**Preferred:** vendor product page or announcement with a named customer deployment — e.g. Cohere Health + BSIM, Abridge + Northwell, PagerDuty + Chicago Trading Company.

**Acceptable:** vendor product page with strong feature evidence even without a named customer, when the feature is clearly in production at scale.

**Not acceptable:** secondary blogs, analyst commentary, academic papers, market projection statistics, individual implementer write-ups, or personal knowledge of a deployment without a publicly accessible source.

Additional sources — such as blog posts, architecture whitepapers, or technical guides — may be cited within classification rationale sentences to explain how a referenced deployment works, provided they refer specifically to a vendor or deployment already in the citation list. They do not count toward the citation target and do not substitute for production deployment evidence.

## Status

The category groupings, schema, and evidentiary standard are ready for WG vote. Individual row content — source citations, classification values, and Notes cells — is under active verification.

## Structure

``` 
workstreams/critical-use-cases/
├── README.md
├── schema-agentic-use-cases.md   # column definitions and classification values for the inventory table
└── use-case-inventory.md         # the inventory table
```

## Contributing

Fork the repo, make your changes, and open a PR against the upstream WG repo.

### Link checks

Links in this folder are checked automatically ([workflow](../../.github/workflows/use-cases-link-check.yml)):

- **On every PR** that touches this folder: links between files and section anchors are checked, plus any external links the PR adds or changes. The check fails only on links that are clearly dead (404/410, a missing file or anchor, or a domain that no longer exists). Sites that block automated requests are listed in the job summary as "could not verify" but never fail the check.
- **Weekly**: every link is checked and the results are posted to a single open issue labelled `link-health`.

To run the same check locally, install [lychee](https://lychee.cli.rs/) and run `lychee 'workstreams/critical-use-cases/**/*.md'` from the repo root. It picks up `lychee.toml` and `.lycheeignore` automatically.

## Links
Upcoming workstream meetings: 
Meeting notes: https://docs.google.com/document/d/1g8637JPZZ4Y-V-KXTcGU0de1HmTEc2iI6-PCTHv7zuI/edit?usp=sharing 
Discord: https://discord.com/channels/1461090924791595243/1504501824118460547 

