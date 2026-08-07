# Instructions for AI Contributors

Before adding or changing a pattern, reference architecture, scenario, decision, or supporting document in this workstream:

1. Read [README.md](README.md).
2. Read [CONTRIBUTING.md](CONTRIBUTING.md) completely.
3. Read the applicable template before drafting:
   - [patterns/TEMPLATE.md](patterns/TEMPLATE.md)
   - [architectures/TEMPLATE.md](architectures/TEMPLATE.md)

## Required rules

- A **pattern** solves one independently reusable workflow problem.
- A **reference architecture** serves a recognizable practitioner job and composes patterns, capability roles, boundaries, guarantees, and exit states.
- A **scenario** validates an architecture; do not mistake a domain example for the generic architecture name.
- Reuse existing patterns before proposing a new one.
- Keep capability descriptions vendor-neutral and at the logical role level.
- Make the boundary between agent and workflow-controlled work explicit.
- Do not invent unagreed terminology, standards, or cross-WG controls. Record genuine gaps as open questions.
- Follow the template’s core section order. Put allowed additional material only after `Open questions` in an explicit `## Appendix: ...` section.
- State evidence separately from proposed WG interpretation.

Before finishing, complete the self-review checklist in [CONTRIBUTING.md](CONTRIBUTING.md), check internal links, and run:

```bash
git diff --check
```
