# Invoice Processing — Sequence

Status: Mature worked example

*This is a **detailed view** of the [solution](../solution.md). It shows the interaction sequence across participants, including the ambiguous-line and reviewable-draft branches.*

## Interaction sequence

```mermaid
sequenceDiagram
    participant SC as Submission channel
    participant WR as Workflow runtime
    participant DS as Document service
    participant EM as Extraction model
    participant RD as Reference-data adapters
    participant RM as Recommendation model
    participant VP as Validation and policy
    participant EE as ERP effect executor
    participant AR as AP reviewer

    SC->>WR: Submit invoice (TRG INP)
    WR->>DS: Secure and fix source (XB-01 DFN)
    WR->>EM: Request extraction (AIN)
    EM-->>WR: Proposed fields
    WR->>VP: Validate schema and arithmetic (SCH)
    VP-->>WR: Valid extraction
    WR->>RD: Read vendor PO receipt GL (RET)
    RD-->>WR: Reference context
    WR->>VP: Deterministic match and inherit (BRL)
    VP-->>WR: Resolved and residual lines

    alt Residual line ambiguous
        WR->>RM: Recommend from bounded set (REC)
        RM-->>WR: Coding proposal or abstain (UNC)
        WR->>VP: Adjudicate candidate and policy (DVL)
        VP-->>WR: Accepted coding or abstain
    end

    WR->>VP: Determine disposition (POL)
    VP-->>WR: Disposition

    alt Reviewable draft
        WR->>EE: Create unposted draft (TRW IDM)
        EE-->>WR: Draft identity and version
        WR->>WR: Checkpoint and package (CHK WAI)
        WR->>AR: Request approval of exact version
        AR-->>WR: Approve exact version and digest (APR)
        WR->>WR: Record and finish (EVH FSK)
    else Rejected held or manual
        WR->>WR: Record disposition (EVH FSK)
    end
```

## Important boundary

The recommendation model never talks to the ERP effect executor directly. Every proposal returns to the workflow runtime, is adjudicated by validation and policy (`DVL`, `POL`), and only then does the workflow — under authorisation — instruct the ERP effect executor to create the unposted draft. This preserves the `OV-02` propose→validate→authorise→execute→confirm→reconcile separation and keeps all five authorities away from the model ([INV-009](../../../ra/01-foundations/architecture-invariants.md), [INV-010](../../../ra/01-foundations/architecture-invariants.md)). The draft creation is a reversible `EF2` write of an unposted draft; posting and payment are out of scope. Approval binds the exact draft version and does **not** authorise payment.

## Related views

- [architecture.md](architecture.md) — logical architecture and actors.
- [execution.md](execution.md) — stage-by-stage walkthrough.
- [contracts-and-state.md](contracts-and-state.md) — contracts and state checkpoints.
