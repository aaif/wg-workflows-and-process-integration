# Agentic AI Workflow Orchestration Patterns - Comparison

This document compares agentic AI workflow patterns from AWS, Azure, Google Cloud, and Anthropic documentation.

## Pattern Overview

| Pattern | Aliases | Description | Complexity | Agency Level |
|---------|---------|-------------|------------|--------------|
| **[LLM-Augmented Workflow](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/agentic-ai.html#llm-augmented-workflows)** | - | Code paths are largely deterministic, with certain steps augmented with LLMs to make decisions (e.g., document classification and routing) | ⭐ Low | Minimal |
| **[Single-Agent (ReAct)](https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system#react-pattern)** | Augmented LLM | LLM augmented with retrieval, tools, and memory. Adapts to dynamic conditions through reasoning and action cycles | ⭐⭐ Low-Medium | Low-Medium |
| **[Routing](https://www.anthropic.com/engineering/building-effective-agents)** | Triage, Classification | Classifies inputs and directs them to specialized handlers based on content analysis | ⭐⭐ Low-Medium | Low |
| **[Prompt Chaining](https://www.anthropic.com/engineering/building-effective-agents)** | Sequential Prompting | Decomposes tasks into sequential steps where each LLM call processes previous output | ⭐⭐ Low-Medium | Low |
| **[Sequential Multi-Agent](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns)** | Pipeline, Linear Delegation | Chains agents in predefined linear order. Each agent processes output from previous agent | ⭐⭐ Medium | Low |
| **[Parallel Multi-Agent](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns)** | Concurrent, Fan-out/Fan-in, Parallelization | Multiple agents work simultaneously on the same task from different perspectives or specializations | ⭐⭐⭐ Medium | Medium |
| **[Loop Pattern](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns)** | Iterative Loop | Agent iteratively refines output until quality criteria met or maximum iterations reached | ⭐⭐⭐ Medium | Medium |
| **[Review & Critique](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns)** | Evaluator-Optimizer, Maker-Checker | One agent generates, another evaluates and provides feedback in a loop until criteria met | ⭐⭐⭐ Medium | Medium |
| **[Coordinator Pattern](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns)** | Orchestrator-Workers, Handoff | Central LLM dynamically breaks down and delegates tasks to workers, then synthesizes results | ⭐⭐⭐⭐ Medium-High | Medium-High |
| **[Iterative Refinement](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns)** | Multi-cycle Refinement | Systematic improvement through multiple planning and revision cycles | ⭐⭐⭐⭐ Medium-High | Medium-High |
| **[Autonomous Agent (ReAct Loop)](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/agentic-ai.html#autonomous-agents)** | Computer Use | LLM with tools, memory, and retrieval orchestrated in autonomous loop with environmental feedback | ⭐⭐⭐⭐ Medium-High | High |
| **[Hierarchical Task Decomposition](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns)** | Multi-level Planning | Breaks complex problems into multiple levels of subtasks with delegation framework | ⭐⭐⭐⭐⭐ High | High |
| **[Swarm Pattern](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns)** | Group Chat, Roundtable, Council | Multiple agents collaborate through structured conversation to solve problems or make decisions | ⭐⭐⭐⭐⭐ Very High | Very High |
| **[Hybrid (Plan & Solve)](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/agentic-ai.html#hybrids)** | Magentic | LLM creates plan and task breakdown, uses ReAct agents to resolve tasks, then evaluates completion | ⭐⭐⭐⭐⭐ High | High |
| **[Human-in-the-Loop](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns)** | HITL | Incorporates human judgment at critical decision points or approval gates | ⭐⭐⭐⭐ Medium-High | Medium |
| **[Custom Logic](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns)** | - | Mix of predefined rules and model reasoning for workflows not fitting standard patterns | ⭐⭐⭐⭐⭐ Very High | Variable |

---

## Example Use Cases

| Pattern | Concrete Examples |
|---------|-------------------|
| **LLM-Augmented Workflow** | • Simple document classification (invoice vs receipt)<br>• Binary routing decisions (escalate to human or handle automatically)<br>• Document type detection with routing to appropriate processor |
| **Single-Agent (ReAct)** | • Customer support queries with data lookup<br>• Research assistance gathering information from multiple sources<br>• Multi-step tasks requiring external data access<br>• Computer use implementations (UI automation, file operations) |
| **Routing** | • Customer service triage: route to general/refund/technical support<br>• Model selection based on query complexity (simple→Haiku, complex→Opus)<br>• Query classification to appropriate knowledge bases |
| **Prompt Chaining** | • Marketing copy generation → translation to multiple languages<br>• Document outline creation → detailed section writing → validation<br>• Research → synthesis → summary generation |
| **Sequential Multi-Agent** | • **Law firm contract generation**: Template selection → Clause customization → Regulatory compliance → Risk assessment<br>• **Data pipelines**: Extraction agent → Cleaning agent → Loading agent<br>• Structured repeatable workflows with clear stage dependencies |
| **Parallel Multi-Agent** | • **Financial stock analysis**: Fundamental, Technical, Sentiment, ESG agents analyze simultaneously<br>• Multi-perspective code review (security, performance, maintainability)<br>• Parallel guardrails implementation (safety, bias, accuracy checks)<br>• Evaluation automation across multiple aspects |
| **Loop Pattern** | • Iterative code refinement until tests pass<br>• Self-correction workflows (generate → validate → fix → repeat)<br>• Automated polling/status checks until condition met |
| **Review & Critique** | • Code generation with security auditing and revision<br>• Document summarization with accuracy validation<br>• Content creation with editorial review<br>• Literary translation refinement through critique cycles |
| **Coordinator Pattern** | • Complex adaptive business processes requiring dynamic routing<br>• Multi-file coding modifications (identify files → modify → integrate)<br>• Variable workflow coordination based on emerging requirements |
| **Iterative Refinement** | • Code writing with debugging cycles<br>• Multi-part project planning with revision<br>• Long-form document drafting with structural improvements |
| **Autonomous Agent (ReAct Loop)** | • **[SWE-bench task resolution](https://www.anthropic.com/engineering/building-effective-agents)**: Understand codebase → locate bugs → implement fixes → test<br>• Open-ended problem solving with unpredictable steps<br>• Computer use tasks (UI testing, system administration) |
| **Hierarchical Task Decomposition** | • Research projects with multiple investigation threads<br>• Complex planning requiring multi-level decomposition<br>• Ambiguous open-ended problems needing systematic breakdown |
| **Swarm Pattern** | • **City park planning**: Community engagement, environmental, budget agents debate proposal<br>• Product design requiring expert debate and consensus<br>• Creative problem-solving through collaborative discussion |
| **Hybrid (Plan & Solve)** | • **SRE automation**: Create remediation plan → delegate to diagnostic/infrastructure/rollback agents → evaluate resolution<br>• Complex goal decomposition with queue-based task processing<br>• Scalable autonomous execution with planning overhead |
| **Human-in-the-Loop** | • Large financial transactions requiring approval<br>• Sensitive document validation with human review<br>• Subjective creative feedback on AI-generated content<br>• High-stakes compliance decisions |
| **Custom Logic** | • Workflows not fitting standard patterns<br>• Complex branching logic with multiple conditions<br>• Mixed pattern requirements in single workflow<br>• Fine-grained process control needs |

---

## When to Use Each Pattern

### Use This Pattern When...

| Pattern | Ideal Scenarios |
|---------|-----------------|
| **LLM-Augmented Workflow** | ✅ Task requires only simple classification or binary decisions<br>✅ Workflow is mostly deterministic with few decision points<br>✅ Predictability and low cost are priorities<br>✅ Minimal agency is acceptable |
| **Single-Agent (ReAct)** | ✅ [Good starting point](https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system) for agentic systems<br>✅ Task requires dynamic tool selection but manageable tool count<br>✅ Need balance between simplicity and capability<br>✅ Transparent reasoning is important for debugging |
| **Routing** | ✅ Multiple distinct input categories require different handling<br>✅ Specialized optimization per input type needed<br>✅ Classification accuracy is high<br>✅ Categories are well-defined and stable |
| **Prompt Chaining** | ✅ Task has clear, fixed subtask boundaries<br>✅ Each step naturally builds on previous output<br>✅ [Programmatic validation gates](https://www.anthropic.com/engineering/building-effective-agents) needed between steps<br>✅ Debugging individual steps is important |
| **Sequential Multi-Agent** | ✅ Multistage process has clear linear dependencies<br>✅ Data transformation pipeline where each stage adds specific value<br>✅ Stages cannot be parallelized<br>✅ Progressive refinement through predefined stages |
| **Parallel Multi-Agent** | ✅ Tasks are [embarrassingly parallel](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns)<br>✅ Multiple independent perspectives needed<br>✅ Time-sensitive scenarios where latency matters<br>✅ [Voting/consensus mechanisms](https://www.anthropic.com/engineering/building-effective-agents) improve confidence |
| **Loop Pattern** | ✅ Quality refinement through iteration is beneficial<br>✅ Clear exit conditions can be defined<br>✅ Self-correction capability valuable<br>✅ Acceptable to trade latency for quality |
| **Review & Critique** | ✅ Quality assurance is critical<br>✅ [Dedicated verification step](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns) improves outcomes<br>✅ Clear evaluation criteria exist<br>✅ Polished, validated results worth additional cost |
| **Coordinator Pattern** | ✅ Task requirements unclear upfront<br>✅ [Unpredictable subtask requirements](https://www.anthropic.com/engineering/building-effective-agents) emerge during processing<br>✅ Dynamic workflow adjustment needed<br>✅ Flexible, adaptive routing is essential |
| **Iterative Refinement** | ✅ [Complex, polished outputs](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns) required<br>✅ Multi-cycle refinement improves quality<br>✅ Systematic improvement process beneficial<br>✅ Clear quality metrics guide iteration |
| **Autonomous Agent (ReAct Loop)** | ✅ Problem requires [environmental feedback](https://www.anthropic.com/engineering/building-effective-agents) at each step<br>✅ Steps are unpredictable or open-ended<br>✅ Task benefits from real-time adaptation<br>✅ Sophisticated problem-solving capability needed |
| **Hierarchical Task Decomposition** | ✅ Highly complex, ambiguous problems<br>✅ Single-level decomposition insufficient<br>✅ [Systematic breakdown](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns) into multiple tiers needed<br>✅ Comprehensive results worth high complexity |
| **Swarm Pattern** | ✅ [Collaborative ideation or debate](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns) improves outcomes<br>✅ Problem requires multiple expert perspectives<br>✅ Consensus-building or structured validation needed<br>✅ Exceptionally high-quality creative solutions justify cost |
| **Hybrid (Plan & Solve)** | ✅ Complex goals require both planning and execution<br>✅ [Queue-based task processing](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/agentic-ai.html#hybrids) beneficial<br>✅ High degree of agency needed<br>✅ Scalability with auto-scaling important |
| **Human-in-the-Loop** | ✅ [Safety and reliability](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns) require human judgment<br>✅ High-stakes decisions need approval<br>✅ Compliance-essential operations<br>✅ Subjective evaluation needed |
| **Custom Logic** | ✅ [Standard patterns insufficient](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns)<br>✅ Need maximum flexibility<br>✅ Mix of deterministic rules and AI reasoning required<br>✅ Complete orchestration control needed |

### Avoid This Pattern When...

| Pattern | Anti-patterns |
|---------|---------------|
| **LLM-Augmented Workflow** | ❌ Complex decisions or reasoning required<br>❌ Task requires adaptation or learning<br>❌ Higher agency needed |
| **Single-Agent (ReAct)** | ❌ [Too many tools](https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system) (causes performance degradation)<br>❌ Tool count exceeds model's ability to select correctly<br>❌ [Unpredictable termination](https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system) is problematic |
| **Routing** | ❌ Input categories are unclear or overlapping<br>❌ [Misclassification has serious consequences](https://www.anthropic.com/engineering/building-effective-agents)<br>❌ Categories change frequently |
| **Prompt Chaining** | ❌ [Tasks require flexibility or adaptation](https://www.anthropic.com/engineering/building-effective-agents)<br>❌ Cannot define fixed structure upfront<br>❌ Steps might need to be skipped or reordered |
| **Sequential Multi-Agent** | ❌ [Stages are embarrassingly parallel](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns)<br>❌ Single agent can handle all stages<br>❌ Workflow needs dynamic adaptation<br>❌ Early stage failures propagate unacceptably |
| **Parallel Multi-Agent** | ❌ Tasks are dependent or sequential<br>❌ [Resource constraints](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns) make parallel processing infeasible<br>❌ [Result aggregation too complex](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns)<br>❌ Contradictory results have no resolution strategy |
| **Loop Pattern** | ❌ [Exit conditions unclear](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns)<br>❌ [Risk of infinite loop](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns) too high<br>❌ Unpredictable latency unacceptable<br>❌ Cost control difficult |
| **Review & Critique** | ❌ Evaluation criteria ambiguous<br>❌ [Additional latency and cost](https://www.anthropic.com/engineering/building-effective-agents) not justified<br>❌ First-pass output usually sufficient |
| **Coordinator Pattern** | ❌ Simple linear tasks sufficient<br>❌ [Orchestrator failure](https://www.anthropic.com/engineering/building-effective-agents) has unacceptable impact<br>❌ Workflow is predictable and deterministic |
| **Iterative Refinement** | ❌ Simple tasks (over-engineering)<br>❌ [Accumulated latency per cycle](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns) too high<br>❌ Exit condition design too complex |
| **Autonomous Agent (ReAct Loop)** | ❌ Task steps are predictable and structured<br>❌ [Requires extensive oversight](https://www.anthropic.com/engineering/building-effective-agents) but resources unavailable<br>❌ [Compounding errors](https://www.anthropic.com/engineering/building-effective-agents) too risky<br>❌ Cost control critical |
| **Hierarchical Task Decomposition** | ❌ Simple tasks (significant over-engineering)<br>❌ [Architectural complexity](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns) not justified<br>❌ Simpler patterns sufficient |
| **Swarm Pattern** | ❌ Deterministic solution exists<br>❌ [Most complex and costly](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns) pattern unjustified<br>❌ [Risk of unproductive loops](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns)<br>❌ Basic task delegation sufficient |
| **Hybrid (Plan & Solve)** | ❌ Simple patterns suffice<br>❌ Planning overhead not beneficial<br>❌ Queue management complexity unwanted |
| **Human-in-the-Loop** | ❌ Real-time responses required<br>❌ Human latency unacceptable<br>❌ UI infrastructure not available<br>❌ Full automation feasible |
| **Custom Logic** | ❌ Standard patterns fit requirements<br>❌ [Development/maintenance complexity](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns) too high<br>❌ Team lacks expertise to design/debug custom flows |

---

## Cost and Performance Characteristics

| Pattern | Cost Profile | Latency Profile | Key Tradeoffs |
|---------|--------------|-----------------|---------------|
| **LLM-Augmented Workflow** | 💰 Minimal | ⚡ Very Low | Best cost/performance but limited capability |
| **Single-Agent (ReAct)** | 💰 Low | ⚡⚡ Low | Good balance for starting point |
| **Routing** | 💰 Low | ⚡ Very Low | Efficient but depends on classification accuracy |
| **Prompt Chaining** | 💰💰 Low-Medium | ⚡⚡⚡ Medium | Fixed latency overhead from sequential calls |
| **Sequential Multi-Agent** | 💰💰 Low-Medium | ⚡⚡ Low-Medium | [Lower cost than AI orchestration](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns), predictable execution |
| **Parallel Multi-Agent** | 💰💰💰 Medium-High | ⚡⚡ Low (parallel gains) | [Higher token consumption](https://www.anthropic.com/engineering/building-effective-agents) but faster execution |
| **Loop Pattern** | 💰💰💰 Medium (unpredictable) | ⚡⚡⚡⚡ High (unpredictable) | Unpredictable cost and latency |
| **Review & Critique** | 💰💰💰 Medium-High | ⚡⚡⚡⚡ High | [Additional calls per critique](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns) |
| **Coordinator Pattern** | 💰💰💰💰 High | ⚡⚡⚡⚡ High | [More calls than single-agent](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns) |
| **Iterative Refinement** | 💰💰💰💰 High | ⚡⚡⚡⚡⚡ Very High | [Latency increases per cycle](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns) |
| **Autonomous Agent (ReAct Loop)** | 💰💰💰💰 High | ⚡⚡⚡⚡ High | [Costs from iterations](https://www.anthropic.com/engineering/building-effective-agents) |
| **Hierarchical Task Decomposition** | 💰💰💰💰💰 Very High | ⚡⚡⚡⚡⚡ Very High | [Very high number of calls](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns) |
| **Swarm Pattern** | 💰💰💰💰💰 Very High | ⚡⚡⚡⚡⚡ Very High | Highest cost and complexity |
| **Hybrid (Plan & Solve)** | 💰💰💰💰💰 Very High | ⚡⚡⚡⚡⚡ Very High | [Multiple agents in queues](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/agentic-ai.html#hybrids) |
| **Human-in-the-Loop** | 💰💰💰 Medium-High | ⚡⚡⚡⚡⚡ Very High (human wait) | Human latency dominates |
| **Custom Logic** | 💰💰💰💰 Variable (High) | ⚡⚡⚡⚡ Variable | Depends on implementation |

---

## Implementation & Operational Considerations

| Pattern | Key Implementation Considerations | Testing Strategy | Debugging Difficulty |
|---------|----------------------------------|------------------|---------------------|
| **LLM-Augmented Workflow** | • Use tool calls for routing<br>• Keep decision logic deterministic<br>• Minimal prompt engineering | Simple validation | ⚙️ Easy |
| **Single-Agent (ReAct)** | • [Refine prompts & tool definitions first](https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system)<br>• [Give model enough tokens to 'think'](https://www.anthropic.com/engineering/building-effective-agents)<br>• [Clear stopping conditions](https://www.anthropic.com/engineering/building-effective-agents) | [Sandboxed testing](https://www.anthropic.com/engineering/building-effective-agents) | ⚙️⚙️ Medium |
| **Routing** | • Ensure accurate classification<br>• Define clear routing criteria<br>• Handle edge cases | Classification accuracy | ⚙️ Easy |
| **Prompt Chaining** | • Define clear subtask boundaries<br>• [Validation gates between steps](https://www.anthropic.com/engineering/building-effective-agents)<br>• Balance latency vs accuracy | Step-by-step validation | ⚙️⚙️ Medium |
| **Sequential Multi-Agent** | • Use workflow agents<br>• No AI orchestration needed<br>• Predefined logic execution | Pipeline testing | ⚙️ Easy |
| **Parallel Multi-Agent** | • [Result consolidation logic](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns)<br>• [Voting thresholds if applicable](https://www.anthropic.com/engineering/building-effective-agents)<br>• Parallel execution framework | Parallel execution validation | ⚙️⚙️⚙️ Medium |
| **Loop Pattern** | • [Design termination conditions carefully](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns)<br>• Maximum iteration safeguards<br>• Exit logic critical | Exit condition testing | ⚙️⚙️⚙️⚙️ Hard |
| **Review & Critique** | • [Quality evaluation criteria](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns)<br>• [Effective feedback mechanisms](https://www.anthropic.com/engineering/building-effective-agents)<br>• Manage revision loops | Critique effectiveness | ⚙️⚙️⚙️ Medium |
| **Coordinator Pattern** | • [Task decomposition logic](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns)<br>• [Complex error handling](https://www.anthropic.com/engineering/building-effective-agents)<br>• Dynamic routing decisions | Routing decision testing | ⚙️⚙️⚙️⚙️ Hard |
| **Iterative Refinement** | • Quality evaluation metrics<br>• [Maximum iteration safeguards](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns)<br>• Session state management | Refinement quality metrics | ⚙️⚙️⚙️⚙️ Hard |
| **Autonomous Agent (ReAct Loop)** | • [Sandboxed testing environments](https://www.anthropic.com/engineering/building-effective-agents)<br>• ['Ground truth' from environment](https://www.anthropic.com/engineering/building-effective-agents)<br>• [Explicit stopping conditions](https://www.anthropic.com/engineering/building-effective-agents) | [Extensive sandboxed testing](https://www.anthropic.com/engineering/building-effective-agents) | ⚙️⚙️⚙️⚙️⚙️ Very Hard |
| **Hierarchical Task Decomposition** | • Multi-level delegation framework<br>• [Sophisticated decomposition logic](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns)<br>• Hierarchical task management | Multi-level validation | ⚙️⚙️⚙️⚙️⚙️ Very Hard |
| **Swarm Pattern** | • [Dispatcher agent required](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns)<br>• [All-to-all communication control](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns)<br>• Explicit exit conditions | Communication pattern testing | ⚙️⚙️⚙️⚙️⚙️ Very Hard |
| **Hybrid (Plan & Solve)** | • [Queue-based task processing](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/agentic-ai.html#hybrids)<br>• Auto-scaling capability<br>• Async execution support | End-to-end integration | ⚙️⚙️⚙️⚙️⚙️ Very Hard |
| **Human-in-the-Loop** | • [External user interaction system](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns)<br>• Checkpoint management<br>• UI for review/approval | Human interaction flows | ⚙️⚙️⚙️⚙️ Hard |
| **Custom Logic** | • [Custom orchestration code](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns)<br>• [Consider Agent Development Kit](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns)<br>• Extensive testing required | Comprehensive edge cases | ⚙️⚙️⚙️⚙️⚙️ Very Hard |

---

## Pattern Selection Guide

| Current State | When to Upgrade To |
|---------------|-------------------|
| **LLM-Augmented Workflow** | → **Routing** when routing becomes complex<br>→ **Single-Agent** when more dynamic decisions needed |
| **Single-Agent (ReAct)** | → **Routing** when tool selection too complex<br>→ **Sequential** when workflow becomes structured<br>→ **Coordinator** when dynamic decomposition needed |
| **Routing** | → **Single-Agent** when categories need reasoning<br>→ **Coordinator** when routing becomes adaptive |
| **Prompt Chaining** | → **Sequential Multi-Agent** when steps need specialization<br>→ **Coordinator** when tasks become dynamic |
| **Sequential Multi-Agent** | → **Parallel** when speed critical<br>→ **Coordinator** when adaptation needed |
| **Parallel Multi-Agent** | → **Review & Critique** when validation required<br>→ **Swarm** when collaboration essential |
| **Loop Pattern** | → **Review & Critique** when structured feedback needed<br>→ **Iterative Refinement** when polish required |
| **Review & Critique** | → **Iterative Refinement** for multi-aspect refinement<br>→ **Swarm** for collaborative critique |
| **Coordinator Pattern** | → **Hybrid** when planning + execution needed separately<br>→ **Hierarchical** when single-level insufficient |
| **Iterative Refinement** | → **Review & Critique** for structured validation<br>→ **Autonomous Agent** when environmental feedback needed |
| **Autonomous Agent (ReAct Loop)** | → Simpler patterns when predictable patterns emerge |
| **Hierarchical Task Decomposition** | → **Hybrid** when queue-based execution beneficial |
| **Swarm Pattern** | → **Hierarchical** for more structure |
| **Hybrid (Plan & Solve)** | → **Swarm** when planning needs collaboration |
| **Human-in-the-Loop** | → Automated patterns when automation risks acceptable |

---

## Key Takeaways

1. **[Start Simple](https://www.anthropic.com/engineering/building-effective-agents)**: Anthropic recommends beginning with simple prompts and direct API calls before adding complexity.

2. **[Measure Before Complexity](https://www.anthropic.com/engineering/building-effective-agents)**: Only increase complexity when demonstrably improving outcomes through rigorous measurement.

3. **[Agency Spectrum](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/agentic-ai.html)**: Align level of autonomy with problem complexity—don't over-engineer.

4. **[Cost-Complexity Tradeoff](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns)**: More sophisticated patterns dramatically increase operational costs and latency.

5. **[Environmental Feedback](https://www.anthropic.com/engineering/building-effective-agents)**: Autonomous agents require 'ground truth' from environment at each step for effectiveness.

6. **[Transparency](https://www.anthropic.com/engineering/building-effective-agents)**: Explicitly show planning steps for debugging and trust.

---

## Further Reading

- [AWS Well-Architected GenAI Lens - Agentic AI](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/agentic-ai.html)
- [Azure AI Agent Design Patterns](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns)
- [Google Cloud Agentic AI Patterns](https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system)
- [Anthropic: Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)
