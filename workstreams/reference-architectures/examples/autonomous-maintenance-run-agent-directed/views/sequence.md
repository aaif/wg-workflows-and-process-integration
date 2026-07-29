# Agent-Directed Maintenance Run — Sequence

```mermaid
sequenceDiagram
 participant T as Trigger
 participant E as Durable envelope
 participant A as Agent
 participant G as Capability / CI gateway
 participant P as Independent policy
 participant R as PR adapter
 participant H as Human service
 T->>E: Objective and fixed envelope
 E->>A: Resume agent-directed run
 loop agent-selected actions; envelope limits apply
   A->>G: Allowed diagnostic/edit/gate request
   G-->>A: Result or CI correlation
   A->>E: Checkpoint proposal/evidence
   E->>P: Validate budget, scope, effect request
   P-->>A: Permit, deny, or escalation required
 end
 alt exact green gate + scope valid
   A->>P: Propose PR for exact digest
   P->>R: Authorise idempotent PR intent
   R-->>E: Confirm / uncertain result
   E->>E: Reconcile and record
 else repeated failure / scope risk / budget risk
   E->>H: Escalation evidence
 end
 E->>E: Terminal outcome
```

The key boundary is agent → independent policy. Agent-directed control-flow never implies self-authorisation or direct PR credentials.
