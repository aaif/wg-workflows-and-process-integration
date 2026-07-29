# Autonomous Maintenance Run — Sequence

Status: Design example

```mermaid
sequenceDiagram
    participant S as Scheduler / backlog
    participant W as Workflow runtime
    participant P as Scope and budget policy
    participant X as Fresh sandbox
    participant A as Repair agent
    participant G as Tool gateway / CI
    participant R as PR adapter
    participant H as Human escalation

    S->>W: Eligible task trigger
    W->>P: Check label, scope, duplicate, task contract
    alt rejected or over-scope before entry
        P-->>W: Reject or escalate disposition
        W->>W: Record terminal outcome
    else admitted
        W->>X: Provision fresh isolated sandbox
        W->>A: Delegate bounded goal + tools + budget
        loop only while budget remains
            A->>G: Select allowed diagnostic/edit/gate action
            G-->>A: Sandbox result / gate feedback
            A-->>W: Checkpoint attempt and gate correlation
            opt asynchronous CI
                W->>W: Durable wait for gate result
            end
            W->>P: Validate gate + scope manifest
        end
        alt green and scope-valid
            P-->>W: PR permitted for exact change digest
            W->>R: Create idempotent PR intent
            R-->>W: PR identity or ambiguous result
            W->>W: Confirm/reconcile, record completed
        else repeated failure, over-scope, or budget exhausted
            W->>H: Send task, attempts, gate evidence, and reason
            W->>W: Record escalated / budget outcome
        end
        W->>X: Discard sandbox
    end
```

## Authority boundary

The repair agent never calls the PR adapter. Its only write capability is a sandbox-local edit under the predeclared fence. A green deterministic gate and a scope-valid manifest return to the workflow, which performs policy authorisation and invokes the separately credentialed PR adapter. This prevents a proposal or a model-generated instruction from becoming an externally visible effect without validation, authorisation, and confirmation.
