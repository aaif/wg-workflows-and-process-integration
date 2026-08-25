# References

One consolidated reference list for the whole RA document set, merged from the source lists of [`single-agent.md`](../architectures/single-agent.md) and [`multi-agent.md`](../architectures/multi-agent.md). Both RAs, and the primitives, contracts, and topologies that cite external material, link here rather than restating their own copy of this list.

## A note on source quality

Not every source below carries the same weight, and this RA set has been deliberately explicit about the difference rather than flattening everything into one undifferentiated "references" list:

- **Primary standards and foundation sources**: the OMG specifications (BPMN 2.0, DMN, CMMN), the Model Context Protocol specification, the A2A Protocol specification, Linux Foundation press releases, the OWASP project page, and the NIST AI Risk Management Framework. These are normative or foundation-level statements about what a spec or a project actually says or is. Treat these as authoritative for the claims they make about themselves.
- **Vendor documentation**: Camunda's, Temporal's, LangGraph's, n8n's, AWS Step Functions', and Dapr Agents' own docs. These are accurate about that vendor's own product behaviour. It is not a standards claim, and this RA set does not treat it as one; every cross-mapping table built from vendor documentation in this RA set is marked as editorial judgment, not a conformance claim.
- **Vendor and practitioner blogs**: the Camunda blog posts, the AAIF blog post, and Anthropic's "Building Effective Agents." These reflect that vendor's or foundation's own framing or opinion at the time of writing. They are useful context for why a pattern exists or how the industry is naming it, not a settled or peer-reviewed fact.

## Standards and foundations

- OMG: [BPMN 2.0](https://www.omg.org/spec/BPMN/2.0/)
- OMG: [DMN](https://www.omg.org/spec/DMN/)
- OMG: [CMMN](https://www.omg.org/spec/CMMN/)
- [Model Context Protocol specification (2025-06-18)](https://modelcontextprotocol.io/specification/2025-06-18)
- [A2A Protocol specification](https://a2a-protocol.org/latest/)
- Linux Foundation: [Agent2Agent Protocol project launch](https://www.linuxfoundation.org/press/linux-foundation-launches-the-agent2agent-protocol-project-to-enable-secure-intelligent-communication-between-ai-agents)
- Linux Foundation: [Agentic AI Foundation formation](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation)
- AAIF: [From Workflow Orchestration to Agentic Orchestration](https://aaif.io/blog/from-workflow-orchestration-to-agentic-orchestration)
- [OWASP Agentic Applications Top 10](https://owasp.org/www-project-agentic-skills-top-10/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)

## Engines and frameworks

- Camunda: [Ad-hoc sub-processes](https://docs.camunda.io/docs/components/modeler/bpmn/ad-hoc-subprocesses/)
- Camunda: [AI Agent Sub-process connector](https://docs.camunda.io/docs/components/connectors/out-of-the-box-connectors/agentic-ai-aiagent-subprocess)
- Camunda: [Agentic orchestration overview](https://docs.camunda.io/docs/components/agentic-orchestration/agentic-orchestration-overview/)
- Camunda: [Essential agentic patterns for AI agents in BPMN](https://camunda.com/blog/2025/03/essential-agentic-patterns-ai-agents-bpmn/) (blog)
- Camunda: [AI agent or rule-based DMN?](https://camunda.com/blog/2025/07/ai-agent-or-based-rule-dmn-ai-powered-orchestration/) (blog)
- Camunda: [Guardrails and best practices for agentic orchestration](https://camunda.com/blog/2026/01/guardrails-and-best-practices-for-agentic-orchestration/) (blog)
- Anthropic: [Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)
- [Temporal documentation](https://docs.temporal.io/)
- [Dapr Agents](https://dapr.github.io/dapr-agents/)
- [LangGraph documentation](https://langchain-ai.github.io/langgraph/)
- [n8n documentation](https://docs.n8n.io/)
- [AWS Step Functions developer guide](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html)
- [CNCF Serverless Workflow](https://serverlessworkflow.io/)

## Internal

- [`single-agent.md`](../architectures/single-agent.md)
- [`multi-agent.md`](../architectures/multi-agent.md)
- [Reference Architectures workstream README](../README.md)
- [Working Group Charter](../../../charter/charter.md)
- [Reference Architecture Proposal](../../../Workflows-and-Processes-Reference-Architecture-Proposal.md)

## Related

- [Boundaries with other working groups](wg-boundaries.md)
- [Failure modes](failure-modes.md)
- [Loop tiers](loop-tiers.md)
