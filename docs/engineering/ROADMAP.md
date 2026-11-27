# Engineering roadmap

The owner-supplied inventory enumerates **166 checkpoints** across **13 phases**, with **90 in Phases 0–6** and **76 in Phases 7–12**. The assignment states 162 total. [D20](../governance/DECISION_REGISTER.md#d20) records the discrepancy and preserves all listed IDs. Implementation stays within the separately authorized checkpoint. Future checkpoints are Not Started.

Phases group engineering work by domain. Explicit dependencies determine execution order. Release gates determine customer availability, including bounded slices of later-phase checkpoints. A phase label alone never changes a Design V3 release assignment. Review the [release reconciliation](../product/RELEASE_RECONCILIATION.md) before scheduling a slice.

## Design V3 checkpoint crosswalk

| Original | Intent and delivery slices | Engineering checkpoints |
| --- | --- | --- |
| A | Discovery, validation and authorization | [CP-0.1](#cp-01), [CP-0.2](#cp-02), [CP-0.3](#cp-03), [CP-0.4](#cp-04), [CP-0.8](#cp-08), [CP-0.9](#cp-09) |
| B | Secure platform, operations and recovery | [CP-0.5](#cp-05), [CP-0.6](#cp-06), [CP-0.7](#cp-07), [CP-1.1](#cp-11), [CP-1.10](#cp-110), [CP-1.11](#cp-111), [CP-6.3](#cp-63), [CP-6.4](#cp-64), [CP-6.6](#cp-66), [CP-6.11](#cp-611) |
| C | Canonical geography, temporal evidence and search | [CP-2.1](#cp-21), [CP-2.6](#cp-26), [CP-2.7](#cp-27), [CP-2.9](#cp-29), [CP-2.12](#cp-212) |
| D | Climate and forecast launch slices, later environmental and activity conditions | [CP-3.5](#cp-35), [CP-3.6](#cp-36), [CP-3.7](#cp-37), [CP-3.15](#cp-315), [CP-7.3](#cp-73), [CP-7.4](#cp-74) |
| E | Launch advisories, news and corrections, later comparisons and incident maps | [CP-3.8](#cp-38), [CP-3.9](#cp-39), [CP-3.13](#cp-313), [CP-6.8](#cp-68), [CP-9.3](#cp-93), [CP-9.4](#cp-94) |
| F | Search, comparisons, rankings and later atlas | [CP-4.3](#cp-43), [CP-4.6](#cp-46), [CP-4.10](#cp-410), [CP-5.5](#cp-55), [CP-7.1](#cp-71), [CP-7.2](#cp-72), [CP-7.5](#cp-75) |
| G | Grounded launch itineraries, later simulation, readiness and optimization | [CP-5.6](#cp-56), [CP-5.7](#cp-57), [CP-5.15](#cp-515), [CP-7.7](#cp-77), [CP-7.9](#cp-79), [CP-7.11](#cp-711), [CP-8.10](#cp-810) |
| H | Launch monitoring, later reservation, flight, trip graphs and cadence | [CP-4.12](#cp-412), [CP-5.8](#cp-58), [CP-5.9](#cp-59), [CP-5.10](#cp-510), [CP-5.11](#cp-511), [CP-5.12](#cp-512), [CP-8.1](#cp-81), [CP-8.6](#cp-86), [CP-8.8](#cp-88), [CP-8.11](#cp-811), [CP-8.14](#cp-814) |
| I | Hyperlocal coverage, accommodation and parking | [CP-9.1](#cp-91), [CP-9.2](#cp-92), [CP-9.5](#cp-95), [CP-9.6](#cp-96), [CP-9.8](#cp-98), [CP-9.12](#cp-912), [CP-9.13](#cp-913) |
| J | Creator ownership, verified experiences and moderation | [CP-10.1](#cp-101), [CP-10.2](#cp-102), [CP-10.3](#cp-103), [CP-10.4](#cp-104), [CP-10.5](#cp-105) |
| K | Provider credentials, verified reviews and transparent prices | [CP-10.6](#cp-106), [CP-10.7](#cp-107), [CP-10.8](#cp-108), [CP-10.9](#cp-109) |
| L | Consent, sharing and qualified assistance | [CP-10.10](#cp-1010), [CP-10.11](#cp-1011), [CP-10.12](#cp-1012), [CP-10.13](#cp-1013) |
| M | Commercial validation, payments and enterprise API economics | [CP-10.14](#cp-1014), [CP-11.1](#cp-111), [CP-11.2](#cp-112), [CP-11.3](#cp-113), [CP-11.4](#cp-114), [CP-11.7](#cp-117), [CP-11.11](#cp-1111) |
| N | Predictive evaluation, demand/risk-gated expansion | [CP-12.1](#cp-121), [CP-12.2](#cp-122), [CP-12.6](#cp-126), [CP-12.8](#cp-128), [CP-12.12](#cp-1212), [CP-12.13](#cp-1213) |

## Phase 0 — Product & Engineering Readiness

### CP-0.1

**Design baseline and requirements traceability**

- Objective — Design baseline and requirements traceability.
- Dependencies — Design V3 baseline and project-owner authorization.
- Scope — Preserve the source, restore the supplied checkpoint inventory, reconcile releases and verify documentation.
- Exclusions — Competitive benchmarking, application implementation and checkpoint acceptance.
- Deliverables — Design archive and remediation evidence.
- Acceptance criteria — Verify byte identity, 80 FRs, 14 NFRs, 15 launch mappings and the checkpoint graph; publish the existing draft.
- Target product release — V1.0.
- Exit gate — Publish verified documentation in Draft PR #1 and obtain owner acceptance.
- Implementation status — Under Review.
- FR primary — None directly assigned.
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-0.2

**Hands-on competitive benchmarking**

- Objective — Hands-on competitive benchmarking.
- Dependencies — [CP-0.1](#cp-01)
- Scope — Deliver benchmark notebook and gap matrix for this checkpoint.
- Exclusions — Application delivery, procurement and later discovery tasks outside this checkpoint.
- Deliverables — Benchmark notebook and gap matrix.
- Acceptance criteria — Record six comparable competitor attempts with dates, weighted evidence and access limitations.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-0.3

**Customer discovery and launch-market validation**

- Objective — Customer discovery and launch-market validation.
- Dependencies — [CP-0.1](#cp-01)
- Scope — Deliver interview and market shortlist evidence for this checkpoint.
- Exclusions — Application delivery, procurement and later discovery tasks outside this checkpoint.
- Deliverables — Interview and market shortlist evidence.
- Acceptance criteria — Complete 20–30 traveler interviews and score all 20 candidate markets against coverage criteria.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-0.4

**Data provider feasibility, licensing and cost analysis**

- Objective — Data provider feasibility, licensing and cost analysis.
- Dependencies — [CP-0.3](#cp-03)
- Scope — Deliver provider rights registry and cost model for this checkpoint.
- Exclusions — Application delivery, procurement and later discovery tasks outside this checkpoint.
- Deliverables — Provider rights registry and cost model.
- Acceptance criteria — Record each shortlisted source's license, freshness, redistribution rights, rate limits and 1k/10k/100k usage costs.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — [NFR-04](../engineering/TRACEABILITY.md#nfr-04), [NFR-13](../engineering/TRACEABILITY.md#nfr-13).
- NFR verification — None directly assigned.

### CP-0.5

**Technology stack and cloud provider selection**

- Objective — Technology stack and cloud provider selection.
- Dependencies — [CP-0.4](#cp-04)
- Scope — Deliver stack and cloud comparison for this checkpoint.
- Exclusions — Application delivery, procurement and later discovery tasks outside this checkpoint.
- Deliverables — Stack and cloud comparison.
- Acceptance criteria — Compare AWS and Azure against cost, operations, recovery and compatibility criteria; obtain an owner decision.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-0.6

**Repository structure and engineering governance**

- Objective — Repository structure and engineering governance.
- Dependencies — [CP-0.5](#cp-05)
- Scope — Deliver repository boundaries and governance plan for this checkpoint.
- Exclusions — Application delivery, procurement and later discovery tasks outside this checkpoint.
- Deliverables — Repository boundaries and governance plan.
- Acceptance criteria — Demonstrate one independently reviewable example for each branch, PR and checkpoint workflow.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-0.7

**Architecture Decision Records**

- Objective — Architecture Decision Records.
- Dependencies — [CP-0.5](#cp-05), [CP-0.6](#cp-06)
- Scope — Deliver baseline ADR set for this checkpoint.
- Exclusions — Application delivery, procurement and later discovery tasks outside this checkpoint.
- Deliverables — Baseline ADR set.
- Acceptance criteria — Record alternatives, consequences and approval status for each significant architecture commitment.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-0.8

**Threat model and privacy impact assessment**

- Objective — Threat model and privacy impact assessment.
- Dependencies — [CP-0.4](#cp-04), [CP-0.7](#cp-07)
- Scope — Deliver threat model and privacy impact assessment for this checkpoint.
- Exclusions — Application delivery, procurement and later discovery tasks outside this checkpoint.
- Deliverables — Threat model and privacy impact assessment.
- Acceptance criteria — Identify all trust boundaries, personal-data flows, owners and mitigations; record unresolved findings.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — [NFR-02](../engineering/TRACEABILITY.md#nfr-02), [NFR-11](../engineering/TRACEABILITY.md#nfr-11).
- NFR verification — None directly assigned.

### CP-0.9

**Launch backlog and implementation readiness review**

- Objective — Launch backlog and implementation readiness review.
- Dependencies — [CP-0.2](#cp-02), [CP-0.3](#cp-03), [CP-0.4](#cp-04), [CP-0.6](#cp-06), [CP-0.7](#cp-07), [CP-0.8](#cp-08), [CP-0.5](#cp-05)
- Scope — Deliver prioritized launch backlog and readiness packet for this checkpoint.
- Exclusions — Application delivery, procurement and later discovery tasks outside this checkpoint.
- Deliverables — Prioritized launch backlog and readiness packet.
- Acceptance criteria — Trace every launch FR to a delivery and verification checkpoint; record owner readiness approval.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

## Phase 1 — Platform Foundation

### CP-1.1

**Monorepo initialization and development environment**

- Objective — Monorepo initialization and development environment.
- Dependencies — [CP-0.9](#cp-09)
- Scope — Deliver workspace and reproducible development instructions for this checkpoint.
- Exclusions — Consumer features, destination datasets and production launch approval.
- Deliverables — Workspace and reproducible development instructions.
- Acceptance criteria — Run a clean setup twice with pinned tooling and a working local smoke command.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-1.2

**Backend application framework and configuration**

- Objective — Backend application framework and configuration.
- Dependencies — [CP-1.1](#cp-11)
- Scope — Deliver backend shell and typed settings for this checkpoint.
- Exclusions — Consumer features, destination datasets and production launch approval.
- Deliverables — Backend shell and typed settings.
- Acceptance criteria — Start with valid configuration and fail safely on each required missing or malformed setting.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-1.3

**PostgreSQL, PostGIS and pgvector integration**

- Objective — PostgreSQL, PostGIS and pgvector integration.
- Dependencies — [CP-1.2](#cp-12)
- Scope — Deliver database integration and extension configuration for this checkpoint.
- Exclusions — Consumer features, destination datasets and production launch approval.
- Deliverables — Database integration and extension configuration.
- Acceptance criteria — Connect with least privilege and exercise spatial and vector queries against pinned extensions.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-1.4

**Database migrations and transaction management**

- Objective — Database migrations and transaction management.
- Dependencies — [CP-1.3](#cp-13)
- Scope — Deliver migration and transaction policy for this checkpoint.
- Exclusions — Consumer features, destination datasets and production launch approval.
- Deliverables — Migration and transaction policy.
- Acceptance criteria — Pass clean install, supported upgrade and failure recovery while preserving data integrity.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — [NFR-09](../engineering/TRACEABILITY.md#nfr-09).
- NFR verification — None directly assigned.

### CP-1.5

**API contracts, versioning and error handling**

- Objective — API contracts, versioning and error handling.
- Dependencies — [CP-1.2](#cp-12)
- Scope — Deliver versioned API and error schema for this checkpoint.
- Exclusions — Consumer features, destination datasets and production launch approval.
- Deliverables — Versioned API and error schema.
- Acceptance criteria — Validate responses against the published contract and exercise invalid input and consistent error cases.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — [NFR-09](../engineering/TRACEABILITY.md#nfr-09).
- NFR verification — None directly assigned.

### CP-1.6

**Authentication, authorization and user isolation**

- Objective — Authentication, authorization and user isolation.
- Dependencies — [CP-1.4](#cp-14), [CP-1.5](#cp-15)
- Scope — Deliver identity and object authorization baseline for this checkpoint.
- Exclusions — Consumer features, destination datasets and production launch approval.
- Deliverables — Identity and object authorization baseline.
- Acceptance criteria — Permit the entitled user and deny unauthenticated and cross-user requests on protected resources.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — [FR-015](../product/REQUIREMENTS.md#fr-015), [FR-026](../product/REQUIREMENTS.md#fr-026), [FR-028](../product/REQUIREMENTS.md#fr-028), [FR-029](../product/REQUIREMENTS.md#fr-029), [FR-041](../product/REQUIREMENTS.md#fr-041), [FR-055](../product/REQUIREMENTS.md#fr-055), [FR-061](../product/REQUIREMENTS.md#fr-061), [FR-067](../product/REQUIREMENTS.md#fr-067), [FR-068](../product/REQUIREMENTS.md#fr-068), [FR-069](../product/REQUIREMENTS.md#fr-069), [FR-071](../product/REQUIREMENTS.md#fr-071).
- FR verification — None directly assigned.
- NFR implementation — [NFR-01](../engineering/TRACEABILITY.md#nfr-01), [NFR-02](../engineering/TRACEABILITY.md#nfr-02).
- NFR verification — None directly assigned.

### CP-1.7

**Background workers and asynchronous job processing**

- Objective — Background workers and asynchronous job processing.
- Dependencies — [CP-1.4](#cp-14)
- Scope — Deliver job scheduler and worker baseline for this checkpoint.
- Exclusions — Consumer features, destination datasets and production launch approval.
- Deliverables — Job scheduler and worker baseline.
- Acceptance criteria — Retry a transient error, suppress replay duplicates and expose terminal failure.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — [FR-029](../product/REQUIREMENTS.md#fr-029).
- FR verification — None directly assigned.
- NFR implementation — [NFR-07](../engineering/TRACEABILITY.md#nfr-07).
- NFR verification — None directly assigned.

### CP-1.8

**Object storage, caching and secrets management**

- Objective — Object storage, caching and secrets management.
- Dependencies — [CP-1.2](#cp-12), [CP-1.6](#cp-16)
- Scope — Deliver storage, cache and secret adapters for this checkpoint.
- Exclusions — Consumer features, destination datasets and production launch approval.
- Deliverables — Storage, cache and secret adapters.
- Acceptance criteria — Prove storage isolation, cache invalidation and rotation without secret disclosure.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — [FR-029](../product/REQUIREMENTS.md#fr-029), [FR-067](../product/REQUIREMENTS.md#fr-067).
- FR verification — None directly assigned.
- NFR implementation — [NFR-02](../engineering/TRACEABILITY.md#nfr-02).
- NFR verification — None directly assigned.

### CP-1.9

**Logging, metrics, tracing and health checks**

- Objective — Logging, metrics, tracing and health checks.
- Dependencies — [CP-1.7](#cp-17), [CP-1.8](#cp-18)
- Scope — Deliver telemetry conventions and health endpoints for this checkpoint.
- Exclusions — Consumer features, destination datasets and production launch approval.
- Deliverables — Telemetry conventions and health endpoints.
- Acceptance criteria — Correlate a request and job trace; demonstrate readiness failure with redacted logs.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — [FR-069](../product/REQUIREMENTS.md#fr-069).
- FR verification — None directly assigned.
- NFR implementation — [NFR-06](../engineering/TRACEABILITY.md#nfr-06), [NFR-07](../engineering/TRACEABILITY.md#nfr-07).
- NFR verification — None directly assigned.

### CP-1.10

**CI/CD, dependency scanning and infrastructure as code**

- Objective — CI/CD, dependency scanning and infrastructure as code.
- Dependencies — [CP-1.1](#cp-11), [CP-1.4](#cp-14), [CP-1.8](#cp-18), [CP-1.9](#cp-19)
- Scope — Deliver cI/CD and infrastructure definitions for this checkpoint.
- Exclusions — Consumer features, destination datasets and production launch approval.
- Deliverables — CI/CD and infrastructure definitions.
- Acceptance criteria — Run reproducible checks, migration validation, secret and dependency scans and an infrastructure plan.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — [NFR-02](../engineering/TRACEABILITY.md#nfr-02), [NFR-09](../engineering/TRACEABILITY.md#nfr-09).
- NFR verification — None directly assigned.

### CP-1.11

**Integration testing and foundation acceptance review**

- Objective — Integration testing and foundation acceptance review.
- Dependencies — [CP-1.5](#cp-15), [CP-1.6](#cp-16), [CP-1.7](#cp-17), [CP-1.9](#cp-19), [CP-1.10](#cp-110)
- Scope — Deliver foundation acceptance evidence for this checkpoint.
- Exclusions — Consumer features, destination datasets and production launch approval.
- Deliverables — Foundation acceptance evidence.
- Acceptance criteria — Pass cross-component smoke, isolation, worker replay and migration checks from a clean environment.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — [NFR-09](../engineering/TRACEABILITY.md#nfr-09).
- NFR verification — None directly assigned.

## Phase 2 — Global Destination Knowledge Platform

### CP-2.1

**Canonical destination ontology**

- Objective — Canonical destination ontology.
- Dependencies — [CP-1.11](#cp-111)
- Scope — Deliver ontology and schema contract for this checkpoint.
- Exclusions — Consumer presentation, downstream domain feeds and trip monitoring.
- Deliverables — Ontology and schema contract.
- Acceptance criteria — Validate one fixture for each supported entity type and reject an invalid relationship.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-2.2

**Geographic entities and administrative relationships**

- Objective — Geographic entities and administrative relationships.
- Dependencies — [CP-2.1](#cp-21)
- Scope — Deliver geographic entities and relationship rules for this checkpoint.
- Exclusions — Consumer presentation, downstream domain feeds and trip monitoring.
- Deliverables — Geographic entities and relationship rules.
- Acceptance criteria — Resolve overlapping and nested regions and prevent invalid hierarchy cycles.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-2.3

**Coordinates, boundaries and spatial queries**

- Objective — Coordinates, boundaries and spatial queries.
- Dependencies — [CP-2.2](#cp-22), [CP-1.3](#cp-13)
- Scope — Deliver spatial storage and queries for this checkpoint.
- Exclusions — Consumer presentation, downstream domain feeds and trip monitoring.
- Deliverables — Spatial storage and queries.
- Acceptance criteria — Pass boundary, nearest-neighbor and containment fixtures including invalid geometry.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — [FR-012](../product/REQUIREMENTS.md#fr-012), [FR-031](../product/REQUIREMENTS.md#fr-031), [FR-036](../product/REQUIREMENTS.md#fr-036), [FR-040](../product/REQUIREMENTS.md#fr-040), [FR-075](../product/REQUIREMENTS.md#fr-075).
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-2.4

**Destination aliases and multilingual names**

- Objective — Destination aliases and multilingual names.
- Dependencies — [CP-2.2](#cp-22)
- Scope — Deliver alias and multilingual name registry for this checkpoint.
- Exclusions — Consumer presentation, downstream domain feeds and trip monitoring.
- Deliverables — Alias and multilingual name registry.
- Acceptance criteria — Resolve accented and localized aliases and keep ambiguous candidates distinct.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-002](../product/REQUIREMENTS.md#fr-002).
- FR support — [FR-001](../product/REQUIREMENTS.md#fr-001), [FR-030](../product/REQUIREMENTS.md#fr-030).
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-2.5

**Entity resolution and duplicate prevention**

- Objective — Entity resolution and duplicate prevention.
- Dependencies — [CP-2.3](#cp-23), [CP-2.4](#cp-24)
- Scope — Deliver entity-resolution pipeline for this checkpoint.
- Exclusions — Consumer presentation, downstream domain feeds and trip monitoring.
- Deliverables — Entity-resolution pipeline.
- Acceptance criteria — Replay duplicate fixtures without creating extra canonical entities; queue conflicts for review.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — [FR-002](../product/REQUIREMENTS.md#fr-002).
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-2.6

**Source registry and evidence provenance**

- Objective — Source registry and evidence provenance.
- Dependencies — [CP-2.1](#cp-21), [CP-1.4](#cp-14)
- Scope — Deliver source and evidence registry for this checkpoint.
- Exclusions — Consumer presentation, downstream domain feeds and trip monitoring.
- Deliverables — Source and evidence registry.
- Acceptance criteria — Require issuer, timestamp and source identifiers for any critical claim published.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-023](../product/REQUIREMENTS.md#fr-023).
- FR support — [FR-004](../product/REQUIREMENTS.md#fr-004), [FR-005](../product/REQUIREMENTS.md#fr-005), [FR-011](../product/REQUIREMENTS.md#fr-011), [FR-018](../product/REQUIREMENTS.md#fr-018), [FR-025](../product/REQUIREMENTS.md#fr-025), [FR-042](../product/REQUIREMENTS.md#fr-042), [FR-056](../product/REQUIREMENTS.md#fr-056), [FR-060](../product/REQUIREMENTS.md#fr-060), [FR-064](../product/REQUIREMENTS.md#fr-064), [FR-066](../product/REQUIREMENTS.md#fr-066), [FR-076](../product/REQUIREMENTS.md#fr-076).
- FR verification — None directly assigned.
- NFR implementation — [NFR-03](../engineering/TRACEABILITY.md#nfr-03).
- NFR verification — None directly assigned.

### CP-2.7

**Temporal facts and historical versioning**

- Objective — Temporal facts and historical versioning.
- Dependencies — [CP-2.6](#cp-26)
- Scope — Deliver versioned fact model for this checkpoint.
- Exclusions — Consumer presentation, downstream domain feeds and trip monitoring.
- Deliverables — Versioned fact model.
- Acceptance criteria — Return correct as-of fixtures and retain conflicting claims and corrections.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — [FR-023](../product/REQUIREMENTS.md#fr-023), [FR-024](../product/REQUIREMENTS.md#fr-024), [FR-038](../product/REQUIREMENTS.md#fr-038).
- FR verification — None directly assigned.
- NFR implementation — [NFR-03](../engineering/TRACEABILITY.md#nfr-03).
- NFR verification — None directly assigned.

### CP-2.8

**Geographic data ingestion connectors**

- Objective — Geographic data ingestion connectors.
- Dependencies — [CP-2.5](#cp-25), [CP-2.7](#cp-27), [CP-1.7](#cp-17)
- Scope — Deliver geospatial connector baseline for this checkpoint.
- Exclusions — Consumer presentation, downstream domain feeds and trip monitoring.
- Deliverables — Geospatial connector baseline.
- Acceptance criteria — Replay a provider import without duplicating records and reject unlicensed inputs.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-2.9

**Destination search and relevance ranking**

- Objective — Destination search and relevance ranking.
- Dependencies — [CP-2.8](#cp-28)
- Scope — Deliver search and ranking index for this checkpoint.
- Exclusions — Consumer presentation, downstream domain feeds and trip monitoring.
- Deliverables — Search and ranking index.
- Acceptance criteria — Reach at least 95% top-five recall in the curated exact-and-alias set.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-001](../product/REQUIREMENTS.md#fr-001).
- FR support — [FR-032](../product/REQUIREMENTS.md#fr-032).
- FR verification — None directly assigned.
- NFR implementation — [NFR-06](../engineering/TRACEABILITY.md#nfr-06).
- NFR verification — None directly assigned.

### CP-2.10

**Destination knowledge APIs**

- Objective — Destination knowledge APIs.
- Dependencies — [CP-2.9](#cp-29), [CP-1.5](#cp-15)
- Scope — Deliver destination API contract for this checkpoint.
- Exclusions — Consumer presentation, downstream domain feeds and trip monitoring.
- Deliverables — Destination API contract.
- Acceptance criteria — Return stable IDs, coverage and dated provenance; reject invalid or unknown IDs.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — [FR-003](../product/REQUIREMENTS.md#fr-003).
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-2.11

**Geographic coverage and data quality framework**

- Objective — Geographic coverage and data quality framework.
- Dependencies — [CP-2.6](#cp-26), [CP-2.8](#cp-28)
- Scope — Deliver coverage and quality rules for this checkpoint.
- Exclusions — Consumer presentation, downstream domain feeds and trip monitoring.
- Deliverables — Coverage and quality rules.
- Acceptance criteria — Report per-market missingness, provenance validity and candidate eligibility.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-2.12

**Knowledge platform acceptance review**

- Objective — Knowledge platform acceptance review.
- Dependencies — [CP-2.10](#cp-210), [CP-2.11](#cp-211)
- Scope — Deliver knowledge platform acceptance evidence for this checkpoint.
- Exclusions — Consumer presentation, downstream domain feeds and trip monitoring.
- Deliverables — Knowledge platform acceptance evidence.
- Acceptance criteria — Pass identity, temporal, spatial, API and coverage regression suites.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

## Phase 3 — Data Ingestion & Destination Intelligence

### CP-3.1

**Connector framework and ingestion contracts**

- Objective — Connector framework and ingestion contracts.
- Dependencies — [CP-2.12](#cp-212)
- Scope — Deliver provider connector contract for this checkpoint.
- Exclusions — Consumer interface work, unsupported providers and post-launch intelligence.
- Deliverables — Provider connector contract.
- Acceptance criteria — Reject malformed connector emissions and record source identifiers, licensing and content hashes.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — [FR-033](../product/REQUIREMENTS.md#fr-033).
- FR verification — None directly assigned.
- NFR implementation — [NFR-04](../engineering/TRACEABILITY.md#nfr-04).
- NFR verification — None directly assigned.

### CP-3.2

**Raw data storage and ingestion auditing**

- Objective — Raw data storage and ingestion auditing.
- Dependencies — [CP-3.1](#cp-31), [CP-1.8](#cp-18)
- Scope — Deliver raw archive and ingestion audit for this checkpoint.
- Exclusions — Consumer interface work, unsupported providers and post-launch intelligence.
- Deliverables — Raw archive and ingestion audit.
- Acceptance criteria — Trace a normalized record to its permitted input and enforce archive access and expiry.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — [FR-028](../product/REQUIREMENTS.md#fr-028).
- FR verification — None directly assigned.
- NFR implementation — [NFR-04](../engineering/TRACEABILITY.md#nfr-04).
- NFR verification — None directly assigned.

### CP-3.3

**Scheduling, retries and dead-letter processing**

- Objective — Scheduling, retries and dead-letter processing.
- Dependencies — [CP-3.2](#cp-32), [CP-1.7](#cp-17)
- Scope — Deliver scheduling and failure routing for this checkpoint.
- Exclusions — Consumer interface work, unsupported providers and post-launch intelligence.
- Deliverables — Scheduling and failure routing.
- Acceptance criteria — Bound transient retries and move a permanent failure to quarantine without losing audit context.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — [NFR-04](../engineering/TRACEABILITY.md#nfr-04).
- NFR verification — None directly assigned.

### CP-3.4

**Normalization and data quality validation**

- Objective — Normalization and data quality validation.
- Dependencies — [CP-3.3](#cp-33), [CP-1.6](#cp-16)
- Scope — Deliver normalization, quarantine and review for this checkpoint.
- Exclusions — Consumer interface work, unsupported providers and post-launch intelligence.
- Deliverables — Normalization, quarantine and review.
- Acceptance criteria — Reject bad units or timestamps and record reviewer approval or rejection with audit identity.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-028](../product/REQUIREMENTS.md#fr-028).
- FR support — [FR-007](../product/REQUIREMENTS.md#fr-007), [FR-023](../product/REQUIREMENTS.md#fr-023), [FR-024](../product/REQUIREMENTS.md#fr-024), [FR-026](../product/REQUIREMENTS.md#fr-026), [FR-054](../product/REQUIREMENTS.md#fr-054), [FR-058](../product/REQUIREMENTS.md#fr-058).
- FR verification — None directly assigned.
- NFR implementation — [NFR-04](../engineering/TRACEABILITY.md#nfr-04).
- NFR verification — None directly assigned.

### CP-3.5

**Historical climate intelligence**

- Objective — Historical climate intelligence.
- Dependencies — [CP-3.4](#cp-34)
- Scope — Deliver monthly climate records for this checkpoint.
- Exclusions — Consumer interface work, unsupported providers and post-launch intelligence.
- Deliverables — Monthly climate records.
- Acceptance criteria — Return each of 12 months with units and reference period or an explicit unknown.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-004](../product/REQUIREMENTS.md#fr-004).
- FR support — [FR-014](../product/REQUIREMENTS.md#fr-014), [FR-017](../product/REQUIREMENTS.md#fr-017), [FR-035](../product/REQUIREMENTS.md#fr-035).
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-3.6

**Weather forecast intelligence**

- Objective — Weather forecast intelligence.
- Dependencies — [CP-3.4](#cp-34)
- Scope — Deliver forecast ingestion and timestamp policy for this checkpoint.
- Exclusions — Consumer interface work, unsupported providers and post-launch intelligence.
- Deliverables — Forecast ingestion and timestamp policy.
- Acceptance criteria — Demonstrate fresh, stale and expired fixtures and enforce freshness policy.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — [FR-003](../product/REQUIREMENTS.md#fr-003).
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-3.7

**Tourism seasonality and travel-window recommendations**

- Objective — Tourism seasonality and travel-window recommendations.
- Dependencies — [CP-3.5](#cp-35)
- Scope — Deliver tourism seasonality and baseline ranking for this checkpoint.
- Exclusions — Consumer interface work, unsupported providers and post-launch intelligence.
- Deliverables — Tourism seasonality and baseline ranking.
- Acceptance criteria — Verify evidence-backed season labels and deterministic date-window fixtures.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-005](../product/REQUIREMENTS.md#fr-005).
- FR support — [FR-006](../product/REQUIREMENTS.md#fr-006), [FR-014](../product/REQUIREMENTS.md#fr-014).
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-3.8

**Official travel advisory intelligence**

- Objective — Official travel advisory intelligence.
- Dependencies — [CP-3.4](#cp-34)
- Scope — Deliver official advisory aggregation for this checkpoint.
- Exclusions — Consumer interface work, unsupported providers and post-launch intelligence.
- Deliverables — Official advisory aggregation.
- Acceptance criteria — Keep conflicting issuers separate and suppress expired critical assertions.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-008](../product/REQUIREMENTS.md#fr-008).
- FR support — [FR-014](../product/REQUIREMENTS.md#fr-014), [FR-034](../product/REQUIREMENTS.md#fr-034), [FR-037](../product/REQUIREMENTS.md#fr-037), [FR-040](../product/REQUIREMENTS.md#fr-040).
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-3.9

**Destination news ingestion and deduplication**

- Objective — Destination news ingestion and deduplication.
- Dependencies — [CP-3.4](#cp-34)
- Scope — Deliver news ingestion and event clusters for this checkpoint.
- Exclusions — Consumer interface work, unsupported providers and post-launch intelligence.
- Deliverables — News ingestion and event clusters.
- Acceptance criteria — Cluster duplicates and exclude a geographically unrelated event.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-007](../product/REQUIREMENTS.md#fr-007).
- FR support — [FR-038](../product/REQUIREMENTS.md#fr-038), [FR-040](../product/REQUIREMENTS.md#fr-040).
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-3.10

**Attractions and activity intelligence**

- Objective — Attractions and activity intelligence.
- Dependencies — [CP-3.4](#cp-34)
- Scope — Deliver attraction datasets and activity facts for this checkpoint.
- Exclusions — Consumer interface work, unsupported providers and post-launch intelligence.
- Deliverables — Attraction datasets and activity facts.
- Acceptance criteria — Require canonical locations and sources and label missing hours.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-011](../product/REQUIREMENTS.md#fr-011).
- FR support — [FR-035](../product/REQUIREMENTS.md#fr-035), [FR-051](../product/REQUIREMENTS.md#fr-051).
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-3.11

**Airport, transportation and basic parking guidance**

- Objective — Airport, transportation and basic parking guidance.
- Dependencies — [CP-3.4](#cp-34), [CP-2.3](#cp-23)
- Scope — Deliver airport, transit and basic parking data for this checkpoint.
- Exclusions — Dedicated parking search, live parking and other V1.3 parking features.
- Deliverables — Airport, transit and basic parking data.
- Acceptance criteria — Distinguish serving from located-in airports and show sourced transport and parking notes.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-012](../product/REQUIREMENTS.md#fr-012), [FR-013](../product/REQUIREMENTS.md#fr-013).
- FR support — [FR-044](../product/REQUIREMENTS.md#fr-044), [FR-075](../product/REQUIREMENTS.md#fr-075), [FR-077](../product/REQUIREMENTS.md#fr-077).
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-3.12

**Practical local travel information**

- Objective — Practical local travel information.
- Dependencies — [CP-3.4](#cp-34)
- Scope — Deliver practical essentials dataset for this checkpoint.
- Exclusions — Consumer interface work, unsupported providers and post-launch intelligence.
- Deliverables — Practical essentials dataset.
- Acceptance criteria — Provide source and date per supported field and return explicit unknown for missing data.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-042](../product/REQUIREMENTS.md#fr-042).
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-3.13

**Data freshness and conflict detection**

- Objective — Data freshness and conflict detection.
- Dependencies — [CP-3.6](#cp-36), [CP-3.8](#cp-38), [CP-3.9](#cp-39)
- Scope — Deliver freshness, conflict and correction workflow for this checkpoint.
- Exclusions — Consumer interface work, unsupported providers and post-launch intelligence.
- Deliverables — Freshness, conflict and correction workflow.
- Acceptance criteria — Label stale and conflicting fixtures, withhold expired critical facts and replay corrections.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-024](../product/REQUIREMENTS.md#fr-024).
- FR support — [FR-003](../product/REQUIREMENTS.md#fr-003), [FR-008](../product/REQUIREMENTS.md#fr-008), [FR-018](../product/REQUIREMENTS.md#fr-018), [FR-033](../product/REQUIREMENTS.md#fr-033), [FR-037](../product/REQUIREMENTS.md#fr-037), [FR-046](../product/REQUIREMENTS.md#fr-046), [FR-080](../product/REQUIREMENTS.md#fr-080).
- FR verification — None directly assigned.
- NFR implementation — [NFR-03](../engineering/TRACEABILITY.md#nfr-03).
- NFR verification — None directly assigned.

### CP-3.14

**Source health monitoring and cost controls**

- Objective — Source health monitoring and cost controls.
- Dependencies — [CP-3.13](#cp-313), [CP-1.9](#cp-19)
- Scope — Deliver ingestion health and cost dashboard for this checkpoint.
- Exclusions — Consumer interface work, unsupported providers and post-launch intelligence.
- Deliverables — Ingestion health and cost dashboard.
- Acceptance criteria — Alert on simulated freshness breach and verify budget threshold telemetry.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — [FR-013](../product/REQUIREMENTS.md#fr-013), [FR-080](../product/REQUIREMENTS.md#fr-080).
- FR verification — None directly assigned.
- NFR implementation — [NFR-04](../engineering/TRACEABILITY.md#nfr-04), [NFR-07](../engineering/TRACEABILITY.md#nfr-07), [NFR-13](../engineering/TRACEABILITY.md#nfr-13).
- NFR verification — None directly assigned.

### CP-3.15

**Launch destination coverage review**

- Objective — Launch destination coverage review.
- Dependencies — [CP-3.7](#cp-37), [CP-3.10](#cp-310), [CP-3.11](#cp-311), [CP-3.12](#cp-312), [CP-3.14](#cp-314)
- Scope — Deliver launch coverage evidence for this checkpoint.
- Exclusions — Consumer interface work, unsupported providers and post-launch intelligence.
- Deliverables — Launch coverage evidence.
- Acceptance criteria — Audit every proposed launch market and exclude those with unmet mandatory category coverage.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — [NFR-04](../engineering/TRACEABILITY.md#nfr-04).

## Phase 4 — Core Consumer Application

### CP-4.1

**Design system and application shell**

- Objective — Design system and application shell.
- Dependencies — [CP-3.15](#cp-315)
- Scope — Deliver design tokens and page shell for this checkpoint.
- Exclusions — New ingestion pipelines, unauthorised data access and post-launch capabilities.
- Deliverables — Design tokens and page shell.
- Acceptance criteria — Render representative endpoints with consistent tokens and documented loading and error states.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-4.2

**Responsive navigation and accessibility**

- Objective — Responsive navigation and accessibility.
- Dependencies — [CP-4.1](#cp-41)
- Scope — Deliver responsive navigation and accessibility patterns for this checkpoint.
- Exclusions — New ingestion pipelines, unauthorised data access and post-launch capabilities.
- Deliverables — Responsive navigation and accessibility patterns.
- Acceptance criteria — Pass keyboard navigation and accessible-name checks at representative viewport widths.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — [NFR-08](../engineering/TRACEABILITY.md#nfr-08).
- NFR verification — None directly assigned.

### CP-4.3

**Destination search and discovery experience**

- Objective — Destination search and discovery experience.
- Dependencies — [CP-4.2](#cp-42), [CP-2.9](#cp-29)
- Scope — Deliver search and discovery interface for this checkpoint.
- Exclusions — New ingestion pipelines, unauthorised data access and post-launch capabilities.
- Deliverables — Search and discovery interface.
- Acceptance criteria — Load distinct results for ambiguous aliases and verify keyboard selection and empty results.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — [FR-001](../product/REQUIREMENTS.md#fr-001), [FR-002](../product/REQUIREMENTS.md#fr-002).
- FR verification — None directly assigned.
- NFR implementation — [NFR-08](../engineering/TRACEABILITY.md#nfr-08).
- NFR verification — None directly assigned.

### CP-4.4

**Destination overview pages**

- Objective — Destination overview pages.
- Dependencies — [CP-4.3](#cp-43), [CP-2.10](#cp-210), [CP-3.13](#cp-313)
- Scope — Deliver destination overview pages and reporting entry point for this checkpoint.
- Exclusions — New ingestion pipelines, unauthorised data access and post-launch capabilities.
- Deliverables — Destination overview pages and reporting entry point.
- Acceptance criteria — Render dated evidence and coverage and obtain a tracked accuracy-report reference.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-003](../product/REQUIREMENTS.md#fr-003), [FR-026](../product/REQUIREMENTS.md#fr-026).
- FR support — [FR-056](../product/REQUIREMENTS.md#fr-056).
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-4.5

**Weather and climate visualization**

- Objective — Weather and climate visualization.
- Dependencies — [CP-4.4](#cp-44), [CP-3.5](#cp-35), [CP-3.6](#cp-36)
- Scope — Deliver climate and forecast visualizations for this checkpoint.
- Exclusions — New ingestion pipelines, unauthorised data access and post-launch capabilities.
- Deliverables — Climate and forecast visualizations.
- Acceptance criteria — Distinguish all 12 climate months, forecast timestamp and missing or stale values.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — [FR-004](../product/REQUIREMENTS.md#fr-004).
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-4.6

**Seasonality and best-time-to-visit experience**

- Objective — Seasonality and best-time-to-visit experience.
- Dependencies — [CP-4.5](#cp-45), [CP-3.7](#cp-37)
- Scope — Deliver travel season and window interface for this checkpoint.
- Exclusions — New ingestion pipelines, unauthorised data access and post-launch capabilities.
- Deliverables — Travel season and window interface.
- Acceptance criteria — Expose season evidence, preference trade-offs and unsupported months in a fixture.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — [FR-005](../product/REQUIREMENTS.md#fr-005), [FR-006](../product/REQUIREMENTS.md#fr-006).
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-4.7

**Safety advisory and destination news interfaces**

- Objective — Safety advisory and destination news interfaces.
- Dependencies — [CP-4.4](#cp-44), [CP-3.8](#cp-38), [CP-3.9](#cp-39)
- Scope — Deliver advisories and news views for this checkpoint.
- Exclusions — New ingestion pipelines, unauthorised data access and post-launch capabilities.
- Deliverables — Advisories and news views.
- Acceptance criteria — Display issuer and timestamp, preserve conflicts, and show no-verified-news state.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — [FR-007](../product/REQUIREMENTS.md#fr-007), [FR-008](../product/REQUIREMENTS.md#fr-008).
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-4.8

**Attractions and activity exploration**

- Objective — Attractions and activity exploration.
- Dependencies — [CP-4.4](#cp-44), [CP-3.10](#cp-310)
- Scope — Deliver attraction browsing interface for this checkpoint.
- Exclusions — New ingestion pipelines, unauthorised data access and post-launch capabilities.
- Deliverables — Attraction browsing interface.
- Acceptance criteria — Render location, evidence and unknown hours across supported and insufficient data.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — [FR-011](../product/REQUIREMENTS.md#fr-011).
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-4.9

**Airport, transportation and practical travel information**

- Objective — Airport, transportation and practical travel information.
- Dependencies — [CP-4.4](#cp-44), [CP-3.11](#cp-311), [CP-3.12](#cp-312)
- Scope — Deliver transport and essentials views for this checkpoint.
- Exclusions — New ingestion pipelines, unauthorised data access and post-launch capabilities.
- Deliverables — Transport and essentials views.
- Acceptance criteria — Display airport relationship, practical sources and sourced basic parking notes.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — [FR-012](../product/REQUIREMENTS.md#fr-012), [FR-013](../product/REQUIREMENTS.md#fr-013), [FR-042](../product/REQUIREMENTS.md#fr-042).
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-4.10

**Destination comparison engine and interface**

- Objective — Destination comparison engine and interface.
- Dependencies — [CP-4.5](#cp-45), [CP-4.6](#cp-46), [CP-4.7](#cp-47)
- Scope — Deliver comparison engine and experience for this checkpoint.
- Exclusions — New ingestion pipelines, unauthorised data access and post-launch capabilities.
- Deliverables — Comparison engine and experience.
- Acceptance criteria — Pass comparisons for two through four destinations and reject a fifth.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-014](../product/REQUIREMENTS.md#fr-014).
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-4.11

**User profiles and preferences**

- Objective — User profiles and preferences.
- Dependencies — [CP-1.6](#cp-16), [CP-4.2](#cp-42)
- Scope — Deliver launch account plumbing in V1.0 and optional traveler preferences in V1.1.
- Exclusions — Public preferences in V1.0.
- Deliverables — Profile data foundation and later preferences.
- Acceptance criteria — Verify owner-only editing, deletion and no sensitive defaults before enabling preference UI.
- Target product release — V1.0 / V1.1.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-055](../product/REQUIREMENTS.md#fr-055).
- FR support — [FR-015](../product/REQUIREMENTS.md#fr-015), [FR-030](../product/REQUIREMENTS.md#fr-030).
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-4.12

**Saved destinations and trip workspace**

- Objective — Saved destinations and trip workspace.
- Dependencies — [CP-4.4](#cp-44), [CP-4.11](#cp-411), [CP-1.7](#cp-17)
- Scope — Deliver trip workspace and customer data controls for this checkpoint.
- Exclusions — New ingestion pipelines, unauthorised data access and post-launch capabilities.
- Deliverables — Trip workspace and customer data controls.
- Acceptance criteria — Pass save/edit/delete and cross-user denial; verify export, deletion and expiry handoff.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-015](../product/REQUIREMENTS.md#fr-015), [FR-029](../product/REQUIREMENTS.md#fr-029).
- FR support — [FR-017](../product/REQUIREMENTS.md#fr-017), [FR-019](../product/REQUIREMENTS.md#fr-019), [FR-025](../product/REQUIREMENTS.md#fr-025), [FR-055](../product/REQUIREMENTS.md#fr-055), [FR-061](../product/REQUIREMENTS.md#fr-061).
- FR verification — None directly assigned.
- NFR implementation — [NFR-01](../engineering/TRACEABILITY.md#nfr-01).
- NFR verification — None directly assigned.

### CP-4.13

**SEO and public destination pages**

- Objective — SEO and public destination pages.
- Dependencies — [CP-4.4](#cp-44), [CP-4.9](#cp-49)
- Scope — Deliver indexable destination pages for this checkpoint.
- Exclusions — New ingestion pipelines, unauthorised data access and post-launch capabilities.
- Deliverables — Indexable destination pages.
- Acceptance criteria — Verify metadata and canonical URLs for eligible pages and exclusion of unsupported pages.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-4.14

**End-to-end consumer application testing**

- Objective — End-to-end consumer application testing.
- Dependencies — [CP-4.3](#cp-43), [CP-4.6](#cp-46), [CP-4.7](#cp-47), [CP-4.8](#cp-48), [CP-4.9](#cp-49), [CP-4.10](#cp-410), [CP-4.12](#cp-412), [CP-4.13](#cp-413)
- Scope — Deliver consumer end-to-end evidence for this checkpoint.
- Exclusions — New ingestion pipelines, unauthorised data access and post-launch capabilities.
- Deliverables — Consumer end-to-end evidence.
- Acceptance criteria — Pass the planned V1.0 user journeys, isolation and accessibility regressions.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — None directly assigned.
- FR verification — [FR-001](../product/REQUIREMENTS.md#fr-001), [FR-002](../product/REQUIREMENTS.md#fr-002), [FR-005](../product/REQUIREMENTS.md#fr-005), [FR-011](../product/REQUIREMENTS.md#fr-011), [FR-012](../product/REQUIREMENTS.md#fr-012), [FR-013](../product/REQUIREMENTS.md#fr-013), [FR-014](../product/REQUIREMENTS.md#fr-014), [FR-015](../product/REQUIREMENTS.md#fr-015), [FR-026](../product/REQUIREMENTS.md#fr-026), [FR-042](../product/REQUIREMENTS.md#fr-042).
- NFR implementation — [NFR-08](../engineering/TRACEABILITY.md#nfr-08).
- NFR verification — None directly assigned.

## Phase 5 — AI & Proactive Intelligence

### CP-5.1

**LLM provider abstraction and model configuration**

- Objective — LLM provider abstraction and model configuration.
- Dependencies — [CP-4.14](#cp-414)
- Scope — Deliver model abstraction and pinned configuration for this checkpoint.
- Exclusions — Autonomous reservation changes and unapproved customer AI capabilities.
- Deliverables — Model abstraction and pinned configuration.
- Acceptance criteria — Run the same bounded contract against a test adapter and safely handle configured provider failure.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — [NFR-05](../engineering/TRACEABILITY.md#nfr-05), [NFR-06](../engineering/TRACEABILITY.md#nfr-06).
- NFR verification — None directly assigned.

### CP-5.2

**Retrieval and evidence selection**

- Objective — Retrieval and evidence selection.
- Dependencies — [CP-5.1](#cp-51), [CP-2.6](#cp-26)
- Scope — Deliver evidence retrieval pipeline for this checkpoint.
- Exclusions — Autonomous reservation changes and unapproved customer AI capabilities.
- Deliverables — Evidence retrieval pipeline.
- Acceptance criteria — Exclude expired and out-of-scope evidence and preserve provenance through a fixture.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — [FR-016](../product/REQUIREMENTS.md#fr-016), [FR-022](../product/REQUIREMENTS.md#fr-022).
- FR verification — None directly assigned.
- NFR implementation — [NFR-05](../engineering/TRACEABILITY.md#nfr-05).
- NFR verification — None directly assigned.

### CP-5.3

**Structured AI outputs and schema validation**

- Objective — Structured AI outputs and schema validation.
- Dependencies — [CP-5.2](#cp-52)
- Scope — Deliver structured answer contract for this checkpoint.
- Exclusions — Autonomous reservation changes and unapproved customer AI capabilities.
- Deliverables — Structured answer contract.
- Acceptance criteria — Reject malformed output and unsupported critical assertions with a safe fallback.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — [FR-016](../product/REQUIREMENTS.md#fr-016), [FR-022](../product/REQUIREMENTS.md#fr-022).
- FR verification — None directly assigned.
- NFR implementation — [NFR-05](../engineering/TRACEABILITY.md#nfr-05).
- NFR verification — None directly assigned.

### CP-5.4

**Destination question-answering workflow**

- Objective — Destination question-answering workflow.
- Dependencies — [CP-5.3](#cp-53), [CP-5.13](#cp-513)
- Scope — Build and verify private Q&A on evidence tools; CP-5.14 verifies the V1.1 slice separately.
- Exclusions — Public Q&A at launch; launch release dependency.
- Deliverables — Grounded answer workflow.
- Acceptance criteria — Cite retrieved evidence and abstain on unsupported critical queries before V1.1 exposure.
- Target product release — V1.1.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-022](../product/REQUIREMENTS.md#fr-022).
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-5.5

**Personalized travel-window recommendations**

- Objective — Personalized travel-window recommendations.
- Dependencies — [CP-4.6](#cp-46), [CP-3.7](#cp-37)
- Scope — Deliver deterministic personalized travel-window service for this checkpoint.
- Exclusions — Autonomous reservation changes and unapproved customer AI capabilities.
- Deliverables — Deterministic personalized travel-window service.
- Acceptance criteria — Changing a date or preference changes a controlled result and explains the trade-off.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-006](../product/REQUIREMENTS.md#fr-006).
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-5.6

**Basic itinerary generation**

- Objective — Basic itinerary generation.
- Dependencies — [CP-5.3](#cp-53), [CP-4.12](#cp-412)
- Scope — Deliver editable itinerary generation for this checkpoint.
- Exclusions — Autonomous reservation changes and unapproved customer AI capabilities.
- Deliverables — Editable itinerary generation.
- Acceptance criteria — Produce a source-backed editable itinerary and surface unknown evidence.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-016](../product/REQUIREMENTS.md#fr-016).
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-5.7

**Itinerary constraint validation**

- Objective — Itinerary constraint validation.
- Dependencies — [CP-5.6](#cp-56), [CP-3.10](#cp-310), [CP-3.11](#cp-311)
- Scope — Deliver itinerary constraint validator for this checkpoint.
- Exclusions — Autonomous reservation changes and unapproved customer AI capabilities.
- Deliverables — Itinerary constraint validator.
- Acceptance criteria — Reject closed venues and impossible transfers on deterministic fixtures.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — [FR-016](../product/REQUIREMENTS.md#fr-016), [FR-027](../product/REQUIREMENTS.md#fr-027), [FR-050](../product/REQUIREMENTS.md#fr-050), [FR-079](../product/REQUIREMENTS.md#fr-079).
- FR verification — None directly assigned.
- NFR implementation — [NFR-05](../engineering/TRACEABILITY.md#nfr-05).
- NFR verification — None directly assigned.

### CP-5.8

**Saved-trip monitoring**

- Objective — Saved-trip monitoring.
- Dependencies — [CP-4.12](#cp-412), [CP-1.7](#cp-17)
- Scope — Deliver saved-trip monitoring scheduler for this checkpoint.
- Exclusions — Autonomous reservation changes and unapproved customer AI capabilities.
- Deliverables — Saved-trip monitoring scheduler.
- Acceptance criteria — Process opted-in active trips and stop on opt-out or after return.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — [FR-020](../product/REQUIREMENTS.md#fr-020), [FR-021](../product/REQUIREMENTS.md#fr-021), [FR-040](../product/REQUIREMENTS.md#fr-040), [FR-041](../product/REQUIREMENTS.md#fr-041).
- FR verification — None directly assigned.
- NFR implementation — [NFR-10](../engineering/TRACEABILITY.md#nfr-10).
- NFR verification — None directly assigned.

### CP-5.9

**Destination event relevance engine**

- Objective — Destination event relevance engine.
- Dependencies — [CP-5.8](#cp-58), [CP-3.8](#cp-38), [CP-3.9](#cp-39)
- Scope — Deliver event relevance and impact matcher for this checkpoint.
- Exclusions — Autonomous reservation changes and unapproved customer AI capabilities.
- Deliverables — Event relevance and impact matcher.
- Acceptance criteria — Match spatial and time overlap and suppress disjoint controls.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-040](../product/REQUIREMENTS.md#fr-040).
- FR support — [FR-020](../product/REQUIREMENTS.md#fr-020).
- FR verification — None directly assigned.
- NFR implementation — [NFR-10](../engineering/TRACEABILITY.md#nfr-10).
- NFR verification — None directly assigned.

### CP-5.10

**Weekly destination briefing generation**

- Objective — Weekly destination briefing generation.
- Dependencies — [CP-5.9](#cp-59), [CP-5.12](#cp-512)
- Scope — Deliver weekly briefing workflow for this checkpoint.
- Exclusions — Dynamic daily cadence and unauthorized notifications.
- Deliverables — Weekly briefing workflow.
- Acceptance criteria — Deliver at most one opted-in digest per trip/week and stop after return.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-021](../product/REQUIREMENTS.md#fr-021).
- FR support — [FR-039](../product/REQUIREMENTS.md#fr-039).
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-5.11

**Critical event notification delivery**

- Objective — Critical event notification delivery.
- Dependencies — [CP-5.9](#cp-59), [CP-5.12](#cp-512)
- Scope — Deliver urgent notification and correction delivery for this checkpoint.
- Exclusions — Autonomous reservation changes and unapproved customer AI capabilities.
- Deliverables — Urgent notification and correction delivery.
- Acceptance criteria — Deliver one verified relevant event per trip/version and propagate a correction.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-020](../product/REQUIREMENTS.md#fr-020).
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — [NFR-10](../engineering/TRACEABILITY.md#nfr-10).
- NFR verification — None directly assigned.

### CP-5.12

**Notification preferences and deduplication**

- Objective — Notification preferences and deduplication.
- Dependencies — [CP-5.8](#cp-58)
- Scope — Deliver consent, quiet-hours and deduplication rules for this checkpoint.
- Exclusions — Autonomous reservation changes and unapproved customer AI capabilities.
- Deliverables — Consent, quiet-hours and deduplication rules.
- Acceptance criteria — Honor quiet hours, require urgent override consent and suppress replay duplicates.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-041](../product/REQUIREMENTS.md#fr-041).
- FR support — [FR-020](../product/REQUIREMENTS.md#fr-020), [FR-021](../product/REQUIREMENTS.md#fr-021), [FR-039](../product/REQUIREMENTS.md#fr-039), [FR-062](../product/REQUIREMENTS.md#fr-062).
- FR verification — None directly assigned.
- NFR implementation — [NFR-10](../engineering/TRACEABILITY.md#nfr-10).
- NFR verification — None directly assigned.

### CP-5.13

**AI security, prompt injection and hallucination defenses**

- Objective — AI security, prompt injection and hallucination defenses.
- Dependencies — [CP-5.3](#cp-53), [CP-1.6](#cp-16)
- Scope — Deliver aI security guardrails for this checkpoint.
- Exclusions — Autonomous reservation changes and unapproved customer AI capabilities.
- Deliverables — AI security guardrails.
- Acceptance criteria — Verify untrusted-input handling, tool allowlists, abstention and confirmed-booking protection.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — [FR-022](../product/REQUIREMENTS.md#fr-022).
- FR verification — None directly assigned.
- NFR implementation — [NFR-02](../engineering/TRACEABILITY.md#nfr-02), [NFR-05](../engineering/TRACEABILITY.md#nfr-05).
- NFR verification — None directly assigned.

### CP-5.14

**AI evaluation framework**

- Objective — AI evaluation framework.
- Dependencies — [CP-5.7](#cp-57), [CP-5.11](#cp-511), [CP-5.13](#cp-513)
- Scope — Verify launch AI and run a separate Q&A evaluation after CP-5.4 and before V1.1.
- Exclusions — Q&A as a V1.0 gate.
- Deliverables — AI evaluation harness.
- Acceptance criteria — Record citation, feasibility, relevance, refusal and fallback metrics on a versioned golden set.
- Target product release — V1.0 / V1.1.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — None directly assigned.
- FR verification — [FR-022](../product/REQUIREMENTS.md#fr-022).
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-5.15

**AI and proactive intelligence acceptance review**

- Objective — AI and proactive intelligence acceptance review.
- Dependencies — [CP-5.5](#cp-55), [CP-5.10](#cp-510), [CP-5.14](#cp-514)
- Scope — Deliver aI and monitoring acceptance evidence for this checkpoint.
- Exclusions — Autonomous reservation changes and unapproved customer AI capabilities.
- Deliverables — AI and monitoring acceptance evidence.
- Acceptance criteria — Pass launch itinerary, deterministic ranking, weekly/urgent delivery and safety suites.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — None directly assigned.
- FR verification — [FR-006](../product/REQUIREMENTS.md#fr-006), [FR-016](../product/REQUIREMENTS.md#fr-016), [FR-020](../product/REQUIREMENTS.md#fr-020), [FR-021](../product/REQUIREMENTS.md#fr-021), [FR-040](../product/REQUIREMENTS.md#fr-040), [FR-041](../product/REQUIREMENTS.md#fr-041).
- NFR implementation — None directly assigned.
- NFR verification — [NFR-10](../engineering/TRACEABILITY.md#nfr-10).

## Phase 6 — Production Readiness & V1.0 Launch

### CP-6.1

**Functional requirements traceability audit**

- Objective — Functional requirements traceability audit.
- Dependencies — [CP-5.15](#cp-515)
- Scope — Deliver v1.0 traceability audit for this checkpoint.
- Exclusions — New product scope and acceptance of later releases.
- Deliverables — V1.0 traceability audit.
- Acceptance criteria — Reconcile all 24 V1.0 FRs with requirements, planned tests and release evidence.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-6.2

**Cross-component integration testing**

- Objective — Cross-component integration testing.
- Dependencies — [CP-6.1](#cp-61), [CP-4.14](#cp-414)
- Scope — Deliver integrated launch verification for this checkpoint.
- Exclusions — New product scope and acceptance of later releases.
- Deliverables — Integrated launch verification.
- Acceptance criteria — Pass the required launch integration suites across web, API, storage and workers.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — None directly assigned.
- FR verification — [FR-028](../product/REQUIREMENTS.md#fr-028).
- NFR implementation — None directly assigned.
- NFR verification — [NFR-09](../engineering/TRACEABILITY.md#nfr-09).

### CP-6.3

**Performance and load testing**

- Objective — Performance and load testing.
- Dependencies — [CP-6.2](#cp-62)
- Scope — Deliver load evidence and accepted workload for this checkpoint.
- Exclusions — New product scope and acceptance of later releases.
- Deliverables — Load evidence and accepted workload.
- Acceptance criteria — Measure cached profile and search P95 against approved targets and exercise saturation recovery.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — [NFR-06](../engineering/TRACEABILITY.md#nfr-06).

### CP-6.4

**Security assessment and penetration testing**

- Objective — Security assessment and penetration testing.
- Dependencies — [CP-6.2](#cp-62), [CP-5.13](#cp-513)
- Scope — Deliver security assessment evidence for this checkpoint.
- Exclusions — New product scope and acceptance of later releases.
- Deliverables — Security assessment evidence.
- Acceptance criteria — Record assessment scope and findings; clear critical findings and obtain explicit high-risk exceptions.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — [NFR-02](../engineering/TRACEABILITY.md#nfr-02).

### CP-6.5

**Privacy compliance and data deletion verification**

- Objective — Privacy compliance and data deletion verification.
- Dependencies — [CP-6.2](#cp-62), [CP-0.8](#cp-08)
- Scope — Deliver privacy audit and deletion evidence for this checkpoint.
- Exclusions — New product scope and acceptance of later releases.
- Deliverables — Privacy audit and deletion evidence.
- Acceptance criteria — Verify owner authorization, export, active-store deletion, queue handling and backup expiry.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — [FR-067](../product/REQUIREMENTS.md#fr-067).
- FR verification — [FR-029](../product/REQUIREMENTS.md#fr-029).
- NFR implementation — None directly assigned.
- NFR verification — [NFR-01](../engineering/TRACEABILITY.md#nfr-01).

### CP-6.6

**Backup and disaster recovery exercises**

- Objective — Backup and disaster recovery exercises.
- Dependencies — [CP-6.2](#cp-62), [CP-1.8](#cp-18)
- Scope — Deliver backup and restore exercise report for this checkpoint.
- Exclusions — New product scope and acceptance of later releases.
- Deliverables — Backup and restore exercise report.
- Acceptance criteria — Demonstrate timed recovery under approved RPO and RTO with restored integrity.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — [NFR-07](../engineering/TRACEABILITY.md#nfr-07).

### CP-6.7

**Accessibility and usability assessment**

- Objective — Accessibility and usability assessment.
- Dependencies — [CP-4.14](#cp-414), [CP-6.2](#cp-62)
- Scope — Deliver accessibility audit and usability results for this checkpoint.
- Exclusions — New product scope and acceptance of later releases.
- Deliverables — Accessibility audit and usability results.
- Acceptance criteria — Audit WCAG 2.2 AA target and measure curated search success and moderated research time.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — [NFR-08](../engineering/TRACEABILITY.md#nfr-08).

### CP-6.8

**Data accuracy and geographic coverage audit**

- Objective — Data accuracy and geographic coverage audit.
- Dependencies — [CP-3.15](#cp-315), [CP-6.2](#cp-62)
- Scope — Deliver coverage and accuracy audit for this checkpoint.
- Exclusions — New product scope and acceptance of later releases.
- Deliverables — Coverage and accuracy audit.
- Acceptance criteria — Prove all supported markets meet mandatory coverage and 100% critical attribution.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — None directly assigned.
- FR verification — [FR-003](../product/REQUIREMENTS.md#fr-003), [FR-004](../product/REQUIREMENTS.md#fr-004), [FR-007](../product/REQUIREMENTS.md#fr-007), [FR-008](../product/REQUIREMENTS.md#fr-008), [FR-023](../product/REQUIREMENTS.md#fr-023), [FR-024](../product/REQUIREMENTS.md#fr-024).
- NFR implementation — None directly assigned.
- NFR verification — [NFR-03](../engineering/TRACEABILITY.md#nfr-03).

### CP-6.9

**AI evaluation and adversarial testing**

- Objective — AI evaluation and adversarial testing.
- Dependencies — [CP-5.14](#cp-514), [CP-6.4](#cp-64)
- Scope — Deliver launch AI evaluation results for this checkpoint.
- Exclusions — New product scope and acceptance of later releases.
- Deliverables — Launch AI evaluation results.
- Acceptance criteria — Pass approved golden-set and defensive test thresholds with fallback and reproducible evidence.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — [NFR-05](../engineering/TRACEABILITY.md#nfr-05).

### CP-6.10

**Infrastructure cost and unit economics validation**

- Objective — Infrastructure cost and unit economics validation.
- Dependencies — [CP-3.14](#cp-314), [CP-6.3](#cp-63)
- Scope — Deliver infrastructure and provider cost report for this checkpoint.
- Exclusions — New product scope and acceptance of later releases.
- Deliverables — Infrastructure and provider cost report.
- Acceptance criteria — Model expected and heavy usage and record spend budgets and alert thresholds.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — [NFR-13](../engineering/TRACEABILITY.md#nfr-13).
- NFR verification — [NFR-13](../engineering/TRACEABILITY.md#nfr-13).

### CP-6.11

**Production deployment and operational runbooks**

- Objective — Production deployment and operational runbooks.
- Dependencies — [CP-6.3](#cp-63), [CP-6.4](#cp-64), [CP-6.5](#cp-65), [CP-6.6](#cp-66), [CP-6.8](#cp-68), [CP-6.9](#cp-69), [CP-6.10](#cp-610), [CP-6.7](#cp-67)
- Scope — Deliver deployment and operations runbooks for this checkpoint.
- Exclusions — New product scope and acceptance of later releases.
- Deliverables — Deployment and operations runbooks.
- Acceptance criteria — Rehearse deployment, rollback and escalation and assign operating owners.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — [NFR-07](../engineering/TRACEABILITY.md#nfr-07).
- NFR verification — None directly assigned.

### CP-6.12

**Private alpha release**

- Objective — Private alpha release.
- Dependencies — [CP-6.7](#cp-67), [CP-6.11](#cp-611)
- Scope — Deliver private alpha evidence for this checkpoint.
- Exclusions — New product scope and acceptance of later releases.
- Deliverables — Private alpha evidence.
- Acceptance criteria — Complete a gated cohort and triage all findings before beta approval.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-6.13

**Controlled public beta**

- Objective — Controlled public beta.
- Dependencies — [CP-6.12](#cp-612)
- Scope — Deliver controlled beta evidence for this checkpoint.
- Exclusions — New product scope and acceptance of later releases.
- Deliverables — Controlled beta evidence.
- Acceptance criteria — Record rollout metrics, rollback exercise and issues against signed thresholds.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-6.14

**Defect remediation and release approval**

- Objective — Defect remediation and release approval.
- Dependencies — [CP-6.13](#cp-613)
- Scope — Deliver v1.0 release packet for this checkpoint.
- Exclusions — New product scope and acceptance of later releases.
- Deliverables — V1.0 release packet.
- Acceptance criteria — Close release-blocking defects and record approval, coverage, rollback and owner sign-off.
- Target product release — V1.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

## Phase 7 — Intelligent Discovery

### CP-7.1

**Interactive seasonal world atlas**

- Objective — Interactive seasonal world atlas.
- Dependencies — [CP-6.14](#cp-614), [CP-7.5](#cp-75)
- Scope — Deliver interactive atlas for this checkpoint.
- Exclusions — Flight feeds, reservation imports and unapproved customer release changes.
- Deliverables — Interactive atlas.
- Acceptance criteria — Filter by month and climate and visibly flag unsupported regions.
- Target product release — V1.1.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-031](../product/REQUIREMENTS.md#fr-031).
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-7.2

**Climate-preference destination discovery**

- Objective — Climate-preference destination discovery.
- Dependencies — [CP-7.5](#cp-75)
- Scope — Deliver month and climate discovery for this checkpoint.
- Exclusions — Flight feeds, reservation imports and unapproved customer release changes.
- Deliverables — Month and climate discovery.
- Acceptance criteria — Return only eligible candidates with rationale for each result.
- Target product release — V1.1.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-032](../product/REQUIREMENTS.md#fr-032).
- FR support — [FR-031](../product/REQUIREMENTS.md#fr-031).
- FR verification — [FR-031](../product/REQUIREMENTS.md#fr-031), [FR-032](../product/REQUIREMENTS.md#fr-032).
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-7.3

**Air quality and environmental intelligence**

- Objective — Air quality and environmental intelligence.
- Dependencies — [CP-6.14](#cp-614), [CP-3.13](#cp-313)
- Scope — Deliver environmental dataset for this checkpoint.
- Exclusions — Flight feeds, reservation imports and unapproved customer release changes.
- Deliverables — Environmental dataset.
- Acceptance criteria — Display source, AQI standard, observation time and stale status.
- Target product release — V1.1.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-033](../product/REQUIREMENTS.md#fr-033).
- FR support — [FR-034](../product/REQUIREMENTS.md#fr-034).
- FR verification — [FR-033](../product/REQUIREMENTS.md#fr-033).
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-7.4

**Activity-specific seasonal intelligence**

- Objective — Activity-specific seasonal intelligence.
- Dependencies — [CP-6.14](#cp-614), [CP-3.10](#cp-310)
- Scope — Deliver seasonal activity windows for this checkpoint.
- Exclusions — Flight feeds, reservation imports and unapproved customer release changes.
- Deliverables — Seasonal activity windows.
- Acceptance criteria — Show sourced activity windows and explicit unknown for missing seasons.
- Target product release — V1.1.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-035](../product/REQUIREMENTS.md#fr-035).
- FR support — None directly assigned.
- FR verification — [FR-035](../product/REQUIREMENTS.md#fr-035).
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-7.5

**Explainable destination suitability ranking**

- Objective — Explainable destination suitability ranking.
- Dependencies — [CP-6.14](#cp-614), [CP-7.3](#cp-73), [CP-7.4](#cp-74)
- Scope — Deliver suitability ranking and explanation for this checkpoint.
- Exclusions — Flight feeds, reservation imports and unapproved customer release changes.
- Deliverables — Suitability ranking and explanation.
- Acceptance criteria — Expose weights and prevent serious advisory from being averaged away.
- Target product release — V1.1.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-034](../product/REQUIREMENTS.md#fr-034).
- FR support — [FR-031](../product/REQUIREMENTS.md#fr-031), [FR-032](../product/REQUIREMENTS.md#fr-032).
- FR verification — [FR-034](../product/REQUIREMENTS.md#fr-034).
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-7.6

**Destination cost intelligence**

- Objective — Destination cost intelligence.
- Dependencies — [CP-6.14](#cp-614), [CP-12.7](#cp-127)
- Scope — Deliver budget and destination cost evidence for this checkpoint.
- Exclusions — Flight feeds, reservation imports and unapproved customer release changes.
- Deliverables — Budget and destination cost evidence.
- Acceptance criteria — Show currency, dates, occupancy and a range with no implied quote.
- Target product release — V1.1.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-019](../product/REQUIREMENTS.md#fr-019).
- FR support — [FR-048](../product/REQUIREMENTS.md#fr-048).
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-7.7

**What-If Simulator**

- Objective — What-If Simulator.
- Dependencies — [CP-7.6](#cp-76)
- Scope — Deliver scenario calculator for this checkpoint.
- Exclusions — Flight feeds, reservation imports and unapproved customer release changes.
- Deliverables — Scenario calculator.
- Acceptance criteria — Change dates or occupancy and reproduce recalculated ranges with assumptions.
- Target product release — V1.1.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-048](../product/REQUIREMENTS.md#fr-048).
- FR support — None directly assigned.
- FR verification — [FR-019](../product/REQUIREMENTS.md#fr-019), [FR-048](../product/REQUIREMENTS.md#fr-048).
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-7.8

**Personalized packing recommendations**

- Objective — Personalized packing recommendations.
- Dependencies — [CP-6.14](#cp-614), [CP-3.5](#cp-35)
- Scope — Deliver editable packing checklist for this checkpoint.
- Exclusions — Flight feeds, reservation imports and unapproved customer release changes.
- Deliverables — Editable packing checklist.
- Acceptance criteria — Change packing suggestions with conditions and support user edits and completion.
- Target product release — V1.1.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-017](../product/REQUIREMENTS.md#fr-017).
- FR support — [FR-049](../product/REQUIREMENTS.md#fr-049).
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-7.9

**Travel Readiness Center**

- Objective — Travel Readiness Center.
- Dependencies — [CP-7.7](#cp-77), [CP-7.8](#cp-78), [CP-7.10](#cp-710), [CP-8.12](#cp-812), [CP-8.13](#cp-813), [CP-5.4](#cp-54), [CP-4.11](#cp-411), [CP-7.1](#cp-71), [CP-7.2](#cp-72)
- Scope — Deliver readiness checklist for this checkpoint.
- Exclusions — Flight feeds, reservation imports and unapproved customer release changes.
- Deliverables — Readiness checklist.
- Acceptance criteria — Derive tasks from trip facts and keep completion distinct from eligibility or safety.
- Target product release — V1.1.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-049](../product/REQUIREMENTS.md#fr-049).
- FR support — None directly assigned.
- FR verification — [FR-017](../product/REQUIREMENTS.md#fr-017), [FR-049](../product/REQUIREMENTS.md#fr-049), [FR-055](../product/REQUIREMENTS.md#fr-055).
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-7.10

**Nationality-specific entry and visa intelligence**

- Objective — Nationality-specific entry and visa intelligence.
- Dependencies — [CP-6.14](#cp-614), [CP-3.13](#cp-313)
- Scope — Deliver entry and visa evidence for this checkpoint.
- Exclusions — Flight feeds, reservation imports and unapproved customer release changes.
- Deliverables — Entry and visa evidence.
- Acceptance criteria — Apply nationality, transit and dates and return dated official evidence or unknown.
- Target product release — V1.1.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-018](../product/REQUIREMENTS.md#fr-018).
- FR support — [FR-049](../product/REQUIREMENTS.md#fr-049).
- FR verification — [FR-018](../product/REQUIREMENTS.md#fr-018).
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-7.11

**Advanced itinerary optimization**

- Objective — Advanced itinerary optimization.
- Dependencies — [CP-8.7](#cp-87), [CP-5.7](#cp-57)
- Scope — Schedule advanced optimization after CP-8.7.
- Exclusions — Advanced optimization in V1.0 or V1.1.
- Deliverables — Constraint optimizer.
- Acceptance criteria — Honor all modeled hard constraints and explain infeasibility before V1.2 release.
- Target product release — V1.2.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-050](../product/REQUIREMENTS.md#fr-050).
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

## Phase 8 — Connected Travel Companion

### CP-8.1

**Reservation domain model**

- Objective — Reservation domain model.
- Dependencies — [CP-7.9](#cp-79)
- Scope — Deliver reservation schemas and ownership for this checkpoint.
- Exclusions — Autonomous booking changes, mailbox OAuth without approval, and unscoped expansion.
- Deliverables — Reservation schemas and ownership.
- Acceptance criteria — Validate required segments and deny cross-owner access to reservation fixtures.
- Target product release — V1.2.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — [FR-045](../product/REQUIREMENTS.md#fr-045), [FR-046](../product/REQUIREMENTS.md#fr-046).
- FR verification — None directly assigned.
- NFR implementation — [NFR-11](../engineering/TRACEABILITY.md#nfr-11).
- NFR verification — None directly assigned.

### CP-8.2

**Manual reservation management**

- Objective — Manual reservation management.
- Dependencies — [CP-8.1](#cp-81)
- Scope — Deliver manual reservation workflow for this checkpoint.
- Exclusions — Autonomous booking changes, mailbox OAuth without approval, and unscoped expansion.
- Deliverables — Manual reservation workflow.
- Acceptance criteria — Create, edit and remove a reservation within an authorized trip and audit changes.
- Target product release — V1.2.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — [FR-045](../product/REQUIREMENTS.md#fr-045).
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-8.3

**Secure booking confirmation uploads**

- Objective — Secure booking confirmation uploads.
- Dependencies — [CP-8.2](#cp-82), [CP-0.8](#cp-08)
- Scope — Deliver secure selected upload flow for this checkpoint.
- Exclusions — Autonomous booking changes, mailbox OAuth without approval, and unscoped expansion.
- Deliverables — Secure selected upload flow.
- Acceptance criteria — Quarantine attachments, limit file access and verify deletion/expiry.
- Target product release — V1.2.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — [FR-045](../product/REQUIREMENTS.md#fr-045).
- FR verification — None directly assigned.
- NFR implementation — [NFR-11](../engineering/TRACEABILITY.md#nfr-11).
- NFR verification — None directly assigned.

### CP-8.4

**Reservation extraction and validation**

- Objective — Reservation extraction and validation.
- Dependencies — [CP-8.3](#cp-83)
- Scope — Deliver reservation extraction and confirmation for this checkpoint.
- Exclusions — Autonomous booking changes, mailbox OAuth without approval, and unscoped expansion.
- Deliverables — Reservation extraction and confirmation.
- Acceptance criteria — Minimize extracted fields, require confirmation and test expiry and user isolation.
- Target product release — V1.2.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-045](../product/REQUIREMENTS.md#fr-045).
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — [NFR-11](../engineering/TRACEABILITY.md#nfr-11).
- NFR verification — None directly assigned.

### CP-8.5

**Forwarded email ingestion**

- Objective — Forwarded email ingestion.
- Dependencies — [CP-8.4](#cp-84)
- Scope — Deliver forwarded-email intake for this checkpoint.
- Exclusions — Mailbox OAuth or continuous mailbox access without separate approval.
- Deliverables — Forwarded-email intake.
- Acceptance criteria — Resolve consented forwarding aliases and reject revoked or invalid addresses.
- Target product release — V1.2.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — [FR-045](../product/REQUIREMENTS.md#fr-045).
- FR verification — None directly assigned.
- NFR implementation — [NFR-11](../engineering/TRACEABILITY.md#nfr-11).
- NFR verification — None directly assigned.

### CP-8.6

**Flight status provider integration**

- Objective — Flight status provider integration.
- Dependencies — [CP-8.1](#cp-81), [CP-3.13](#cp-313)
- Scope — Deliver licensed flight status adapter for this checkpoint.
- Exclusions — Autonomous booking changes, mailbox OAuth without approval, and unscoped expansion.
- Deliverables — Licensed flight status adapter.
- Acceptance criteria — Match flight and date, suppress duplicate events and label stale status.
- Target product release — V1.2.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-046](../product/REQUIREMENTS.md#fr-046).
- FR support — [FR-047](../product/REQUIREMENTS.md#fr-047).
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-8.7

**Temporal trip dependency graph**

- Objective — Temporal trip dependency graph.
- Dependencies — [CP-8.2](#cp-82), [CP-8.6](#cp-86)
- Scope — Deliver temporal dependency graph for this checkpoint.
- Exclusions — Autonomous booking changes, mailbox OAuth without approval, and unscoped expansion.
- Deliverables — Temporal dependency graph.
- Acceptance criteria — Validate segment time zones, dependency links and cycles.
- Target product release — V1.2.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — [FR-047](../product/REQUIREMENTS.md#fr-047), [FR-050](../product/REQUIREMENTS.md#fr-050).
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-8.8

**Travel Digital Twin**

- Objective — Travel Digital Twin.
- Dependencies — [CP-8.7](#cp-87)
- Scope — Deliver digital Twin workflow for this checkpoint.
- Exclusions — Autonomous booking changes, mailbox OAuth without approval, and unscoped expansion.
- Deliverables — Digital Twin workflow.
- Acceptance criteria — Identify downstream effects of a delayed flight without changing bookings.
- Target product release — V1.2.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-047](../product/REQUIREMENTS.md#fr-047).
- FR support — [FR-027](../product/REQUIREMENTS.md#fr-027).
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-8.9

**Cascading disruption analysis**

- Objective — Cascading disruption analysis.
- Dependencies — [CP-8.8](#cp-88), [CP-5.9](#cp-59)
- Scope — Deliver disruption impact analysis for this checkpoint.
- Exclusions — Autonomous booking changes, mailbox OAuth without approval, and unscoped expansion.
- Deliverables — Disruption impact analysis.
- Acceptance criteria — Match event geometry and time; identify affected paths and unknown links.
- Target product release — V1.2.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — [FR-027](../product/REQUIREMENTS.md#fr-027), [FR-047](../product/REQUIREMENTS.md#fr-047).
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-8.10

**Adaptive itinerary recommendations**

- Objective — Adaptive itinerary recommendations.
- Dependencies — [CP-8.9](#cp-89), [CP-5.7](#cp-57)
- Scope — Deliver adaptive itinerary recommendation for this checkpoint.
- Exclusions — Autonomous booking changes, mailbox OAuth without approval, and unscoped expansion.
- Deliverables — Adaptive itinerary recommendation.
- Acceptance criteria — Suggest alternatives after disruption while preserving confirmed reservations.
- Target product release — V1.2.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-027](../product/REQUIREMENTS.md#fr-027).
- FR support — [FR-074](../product/REQUIREMENTS.md#fr-074).
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-8.11

**Dynamic daily briefings**

- Objective — Dynamic daily briefings.
- Dependencies — [CP-8.9](#cp-89), [CP-5.10](#cp-510)
- Scope — Deliver dynamic briefing schedule for this checkpoint.
- Exclusions — Autonomous booking changes, mailbox OAuth without approval, and unscoped expansion.
- Deliverables — Dynamic briefing schedule.
- Acceptance criteria — Pass boundary-day fixtures for weekly, twice weekly and daily cadence, including stop after return.
- Target product release — V1.2.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-039](../product/REQUIREMENTS.md#fr-039).
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-8.12

**Offline destination and trip guides**

- Objective — Offline destination and trip guides.
- Dependencies — [CP-6.14](#cp-614), [CP-4.12](#cp-412)
- Scope — Deliver the offline trip summary in V1.1; assess broader offline destination guides separately.
- Exclusions — A broader offline guide commitment in V1.1.
- Deliverables — Offline trip summary and later guide expansion.
- Acceptance criteria — Open the V1.1 summary without network and show last synchronization; separately assess broader guides.
- Target product release — V1.1 / V1.2.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-025](../product/REQUIREMENTS.md#fr-025).
- FR support — None directly assigned.
- FR verification — [FR-025](../product/REQUIREMENTS.md#fr-025).
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-8.13

**Exportable intelligence reports**

- Objective — Exportable intelligence reports.
- Dependencies — [CP-6.14](#cp-614), [CP-4.4](#cp-44)
- Scope — Deliver the printable report in V1.1; evaluate any broader export interfaces separately.
- Exclusions — Delaying the printable report to V1.2.
- Deliverables — Printable intelligence report and export foundation.
- Acceptance criteria — Verify the V1.1 report includes sources, generation time and uncertainty.
- Target product release — V1.1 / V1.2.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-056](../product/REQUIREMENTS.md#fr-056).
- FR support — None directly assigned.
- FR verification — [FR-056](../product/REQUIREMENTS.md#fr-056).
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-8.14

**Reservation privacy and cost acceptance review**

- Objective — Reservation privacy and cost acceptance review.
- Dependencies — [CP-8.5](#cp-85), [CP-8.10](#cp-810), [CP-8.11](#cp-811), [CP-7.11](#cp-711)
- Scope — Deliver reservation and connected companion acceptance evidence for this checkpoint.
- Exclusions — Autonomous booking changes, mailbox OAuth without approval, and unscoped expansion.
- Deliverables — Reservation and connected companion acceptance evidence.
- Acceptance criteria — Pass the V1.2 privacy, cost, optimization, retention and connected-workflow gates.
- Target product release — V1.2.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — None directly assigned.
- FR verification — [FR-027](../product/REQUIREMENTS.md#fr-027), [FR-039](../product/REQUIREMENTS.md#fr-039), [FR-045](../product/REQUIREMENTS.md#fr-045), [FR-046](../product/REQUIREMENTS.md#fr-046), [FR-047](../product/REQUIREMENTS.md#fr-047), [FR-050](../product/REQUIREMENTS.md#fr-050).
- NFR implementation — None directly assigned.
- NFR verification — [NFR-11](../engineering/TRACEABILITY.md#nfr-11).

## Phase 9 — Hyperlocal Intelligence

### CP-9.1

**Neighborhood ontology and boundaries**

- Objective — Neighborhood ontology and boundaries.
- Dependencies — [CP-8.14](#cp-814), [CP-2.3](#cp-23)
- Scope — Deliver neighborhood schemas and boundaries for this checkpoint.
- Exclusions — Unverified safety claims, unsupported markets and creator or marketplace delivery.
- Deliverables — Neighborhood schemas and boundaries.
- Acceptance criteria — Validate geometry, hierarchy and provenance for supported neighborhoods.
- Target product release — V1.3.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — [FR-009](../product/REQUIREMENTS.md#fr-009), [FR-036](../product/REQUIREMENTS.md#fr-036), [FR-043](../product/REQUIREMENTS.md#fr-043).
- FR verification — None directly assigned.
- NFR implementation — [NFR-12](../engineering/TRACEABILITY.md#nfr-12).
- NFR verification — None directly assigned.

### CP-9.2

**Local intelligence coverage assessment**

- Objective — Local intelligence coverage assessment.
- Dependencies — [CP-9.1](#cp-91)
- Scope — Deliver hyperlocal coverage evidence for this checkpoint.
- Exclusions — Unverified safety claims, unsupported markets and creator or marketplace delivery.
- Deliverables — Hyperlocal coverage evidence.
- Acceptance criteria — Assess evidence by category and mark all below-threshold areas as unknown.
- Target product release — V1.3.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — [FR-009](../product/REQUIREMENTS.md#fr-009), [FR-010](../product/REQUIREMENTS.md#fr-010), [FR-043](../product/REQUIREMENTS.md#fr-043).
- FR verification — None directly assigned.
- NFR implementation — [NFR-12](../engineering/TRACEABILITY.md#nfr-12).
- NFR verification — None directly assigned.

### CP-9.3

**Geospatial incident mapping**

- Objective — Geospatial incident mapping.
- Dependencies — [CP-9.2](#cp-92)
- Scope — Deliver incident maps for this checkpoint.
- Exclusions — Unverified safety claims, unsupported markets and creator or marketplace delivery.
- Deliverables — Incident maps.
- Acceptance criteria — Render verified geometry and time and avoid precise pins for uncertain locations.
- Target product release — V1.3.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-036](../product/REQUIREMENTS.md#fr-036).
- FR support — [FR-043](../product/REQUIREMENTS.md#fr-043).
- FR verification — None directly assigned.
- NFR implementation — [NFR-12](../engineering/TRACEABILITY.md#nfr-12).
- NFR verification — None directly assigned.

### CP-9.4

**Historical safety and incident intelligence**

- Objective — Historical safety and incident intelligence.
- Dependencies — [CP-9.3](#cp-93), [CP-2.7](#cp-27)
- Scope — Deliver historical safety and advisory views for this checkpoint.
- Exclusions — Unverified safety claims, unsupported markets and creator or marketplace delivery.
- Deliverables — Historical safety and advisory views.
- Acceptance criteria — Verify as-of versions and comparable crime methodology; compare authority guidance without merging.
- Target product release — V1.3.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-009](../product/REQUIREMENTS.md#fr-009), [FR-037](../product/REQUIREMENTS.md#fr-037), [FR-038](../product/REQUIREMENTS.md#fr-038).
- FR support — [FR-010](../product/REQUIREMENTS.md#fr-010).
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-9.5

**Neighborhood-level assessments**

- Objective — Neighborhood-level assessments.
- Dependencies — [CP-9.4](#cp-94)
- Scope — Deliver neighborhood assessments for this checkpoint.
- Exclusions — Unverified safety claims, unsupported markets and creator or marketplace delivery.
- Deliverables — Neighborhood assessments.
- Acceptance criteria — Return unknown below coverage and confirm no demographic proxy is used.
- Target product release — V1.3.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-043](../product/REQUIREMENTS.md#fr-043).
- FR support — [FR-044](../product/REQUIREMENTS.md#fr-044).
- FR verification — None directly assigned.
- NFR implementation — [NFR-12](../engineering/TRACEABILITY.md#nfr-12).
- NFR verification — None directly assigned.

### CP-9.6

**Know Your Stay accommodation intelligence**

- Objective — Know Your Stay accommodation intelligence.
- Dependencies — [CP-9.5](#cp-95), [CP-3.11](#cp-311)
- Scope — Deliver accommodation intelligence for this checkpoint.
- Exclusions — Unverified safety claims, unsupported markets and creator or marketplace delivery.
- Deliverables — Accommodation intelligence.
- Acceptance criteria — Distinguish distance, access and evidenced risk on hotel-area fixtures.
- Target product release — V1.3.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-044](../product/REQUIREMENTS.md#fr-044).
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-9.7

**Local scam intelligence**

- Objective — Local scam intelligence.
- Dependencies — [CP-9.4](#cp-94)
- Scope — Deliver scam intelligence and report handling for this checkpoint.
- Exclusions — Unverified safety claims, unsupported markets and creator or marketplace delivery.
- Deliverables — Scam intelligence and report handling.
- Acceptance criteria — Cite local evidence or return unknown and prevent unverified reports becoming alerts.
- Target product release — V1.3.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-010](../product/REQUIREMENTS.md#fr-010).
- FR support — [FR-054](../product/REQUIREMENTS.md#fr-054).
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-9.8

**Parking facility discovery**

- Objective — Parking facility discovery.
- Dependencies — [CP-9.2](#cp-92), [CP-3.11](#cp-311)
- Scope — Deliver parking discovery for this checkpoint.
- Exclusions — Unverified safety claims, unsupported markets and creator or marketplace delivery.
- Deliverables — Parking discovery.
- Acceptance criteria — Return correct radius and distance results and exclude missing coordinates.
- Target product release — V1.3.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-075](../product/REQUIREMENTS.md#fr-075).
- FR support — [FR-076](../product/REQUIREMENTS.md#fr-076), [FR-077](../product/REQUIREMENTS.md#fr-077), [FR-078](../product/REQUIREMENTS.md#fr-078), [FR-079](../product/REQUIREMENTS.md#fr-079), [FR-080](../product/REQUIREMENTS.md#fr-080).
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-9.9

**Parking prices and regulations**

- Objective — Parking prices and regulations.
- Dependencies — [CP-9.8](#cp-98)
- Scope — Deliver parking rates and regulations for this checkpoint.
- Exclusions — Unverified safety claims, unsupported markets and creator or marketplace delivery.
- Deliverables — Parking rates and regulations.
- Acceptance criteria — Show sourced prices, hours and restrictions and label unknown values.
- Target product release — V1.3.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-076](../product/REQUIREMENTS.md#fr-076).
- FR support — [FR-078](../product/REQUIREMENTS.md#fr-078).
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-9.10

**Airport and accessible parking intelligence**

- Objective — Airport and accessible parking intelligence.
- Dependencies — [CP-9.9](#cp-99)
- Scope — Deliver terminal, accessible and EV parking information for this checkpoint.
- Exclusions — Unverified safety claims, unsupported markets and creator or marketplace delivery.
- Deliverables — Terminal, accessible and EV parking information.
- Acceptance criteria — Verify terminal transfers and show documented accessibility and EV attributes only.
- Target product release — V1.3.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-077](../product/REQUIREMENTS.md#fr-077), [FR-078](../product/REQUIREMENTS.md#fr-078).
- FR support — [FR-079](../product/REQUIREMENTS.md#fr-079).
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-9.11

**Parking-aware driving itineraries**

- Objective — Parking-aware driving itineraries.
- Dependencies — [CP-9.10](#cp-910), [CP-5.7](#cp-57)
- Scope — Deliver parking-aware itineraries for this checkpoint.
- Exclusions — Unverified safety claims, unsupported markets and creator or marketplace delivery.
- Deliverables — Parking-aware itineraries.
- Acceptance criteria — Provide parking and walking time on a known route and flag unknowns.
- Target product release — V1.3.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-079](../product/REQUIREMENTS.md#fr-079).
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-9.12

**Live parking availability where supported**

- Objective — Live parking availability where supported.
- Dependencies — [CP-9.8](#cp-98), [CP-3.14](#cp-314)
- Scope — Deliver licensed live availability for this checkpoint.
- Exclusions — Unverified safety claims, unsupported markets and creator or marketplace delivery.
- Deliverables — Licensed live availability.
- Acceptance criteria — Show observation time and return unknown on expiry or unsupported coverage.
- Target product release — V1.3.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-080](../product/REQUIREMENTS.md#fr-080).
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-9.13

**Geographic accuracy and safety evaluation**

- Objective — Geographic accuracy and safety evaluation.
- Dependencies — [CP-9.6](#cp-96), [CP-9.7](#cp-97), [CP-9.11](#cp-911), [CP-9.12](#cp-912), [CP-10.5](#cp-105)
- Scope — Deliver hyperlocal release evidence for this checkpoint.
- Exclusions — Unverified safety claims, unsupported markets and creator or marketplace delivery.
- Deliverables — Hyperlocal release evidence.
- Acceptance criteria — Pass geography, methodology, bias, safety and parking freshness audits.
- Target product release — V1.3.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — None directly assigned.
- FR verification — [FR-009](../product/REQUIREMENTS.md#fr-009), [FR-010](../product/REQUIREMENTS.md#fr-010), [FR-036](../product/REQUIREMENTS.md#fr-036), [FR-037](../product/REQUIREMENTS.md#fr-037), [FR-038](../product/REQUIREMENTS.md#fr-038), [FR-043](../product/REQUIREMENTS.md#fr-043), [FR-044](../product/REQUIREMENTS.md#fr-044), [FR-054](../product/REQUIREMENTS.md#fr-054), [FR-075](../product/REQUIREMENTS.md#fr-075), [FR-076](../product/REQUIREMENTS.md#fr-076), [FR-077](../product/REQUIREMENTS.md#fr-077), [FR-078](../product/REQUIREMENTS.md#fr-078), [FR-079](../product/REQUIREMENTS.md#fr-079), [FR-080](../product/REQUIREMENTS.md#fr-080).
- NFR implementation — None directly assigned.
- NFR verification — [NFR-12](../engineering/TRACEABILITY.md#nfr-12).

## Phase 10 — Travel Ecosystem

### CP-10.1

**Creator profiles and content ownership**

- Objective — Creator profiles and content ownership.
- Dependencies — [CP-9.13](#cp-913)
- Scope — Deliver creator rights and profiles for this checkpoint.
- Exclusions — Unapproved public distribution, confidential partner data and paid launch commitments.
- Deliverables — Creator rights and profiles.
- Acceptance criteria — Verify ownership and moderation state before a contribution is published.
- Target product release — V2.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — [FR-051](../product/REQUIREMENTS.md#fr-051), [FR-052](../product/REQUIREMENTS.md#fr-052).
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-10.2

**Location-linked travel experiences**

- Objective — Location-linked travel experiences.
- Dependencies — [CP-10.1](#cp-101)
- Scope — Deliver location-linked experiences for this checkpoint.
- Exclusions — Unapproved public distribution, confidential partner data and paid launch commitments.
- Deliverables — Location-linked experiences.
- Acceptance criteria — Resolve contributions to canonical places and reject unsupported identifiers.
- Target product release — V2.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-051](../product/REQUIREMENTS.md#fr-051).
- FR support — [FR-052](../product/REQUIREMENTS.md#fr-052), [FR-053](../product/REQUIREMENTS.md#fr-053), [FR-065](../product/REQUIREMENTS.md#fr-065).
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-10.3

**Creator video integration**

- Objective — Creator video integration.
- Dependencies — [CP-10.2](#cp-102)
- Scope — Deliver creator video pipeline for this checkpoint.
- Exclusions — Unapproved public distribution, confidential partner data and paid launch commitments.
- Deliverables — Creator video pipeline.
- Acceptance criteria — Verify rights and revoke access when consent is withdrawn.
- Target product release — V2.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-052](../product/REQUIREMENTS.md#fr-052).
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-10.4

**Traveler-reported expense intelligence**

- Objective — Traveler-reported expense intelligence.
- Dependencies — [CP-10.2](#cp-102), [CP-12.7](#cp-127)
- Scope — Deliver expense aggregation for this checkpoint.
- Exclusions — Unapproved public distribution, confidential partner data and paid launch commitments.
- Deliverables — Expense aggregation.
- Acceptance criteria — Require currency, date and category and exclude invalid expenses.
- Target product release — V2.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-053](../product/REQUIREMENTS.md#fr-053).
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-10.5

**Community reporting and moderation**

- Objective — Community reporting and moderation.
- Dependencies — [CP-9.7](#cp-97), [CP-3.4](#cp-34)
- Scope — Deliver only scam/disruption intake and review for V1.3; wider moderation follows in V2.0.
- Exclusions — Publishing unverified reports as alerts or enabling social scope.
- Deliverables — Community intake, moderation and disputes.
- Acceptance criteria — Provide a moderated V1.3 scam-report slice and verify wider V2.0 moderation separately.
- Target product release — V1.3 / V2.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-054](../product/REQUIREMENTS.md#fr-054).
- FR support — [FR-051](../product/REQUIREMENTS.md#fr-051), [FR-070](../product/REQUIREMENTS.md#fr-070), [FR-071](../product/REQUIREMENTS.md#fr-071), [FR-072](../product/REQUIREMENTS.md#fr-072).
- FR verification — None directly assigned.
- NFR implementation — [NFR-14](../engineering/TRACEABILITY.md#nfr-14).
- NFR verification — None directly assigned.

### CP-10.6

**Verified provider registry**

- Objective — Verified provider registry.
- Dependencies — [CP-9.13](#cp-913), [CP-10.7](#cp-107)
- Scope — Deliver verified marketplace registry for this checkpoint.
- Exclusions — Unapproved public distribution, confidential partner data and paid launch commitments.
- Deliverables — Verified marketplace registry.
- Acceptance criteria — List only eligible providers and remove expired verification.
- Target product release — V2.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-057](../product/REQUIREMENTS.md#fr-057).
- FR support — [FR-058](../product/REQUIREMENTS.md#fr-058), [FR-059](../product/REQUIREMENTS.md#fr-059), [FR-060](../product/REQUIREMENTS.md#fr-060).
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-10.7

**Provider credential verification**

- Objective — Provider credential verification.
- Dependencies — [CP-9.13](#cp-913), [CP-3.4](#cp-34)
- Scope — Deliver credential verification for this checkpoint.
- Exclusions — Unapproved public distribution, confidential partner data and paid launch commitments.
- Deliverables — Credential verification.
- Acceptance criteria — Record issuer, scope and expiry and reject failed verification.
- Target product release — V2.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-058](../product/REQUIREMENTS.md#fr-058).
- FR support — [FR-057](../product/REQUIREMENTS.md#fr-057), [FR-063](../product/REQUIREMENTS.md#fr-063), [FR-064](../product/REQUIREMENTS.md#fr-064).
- FR verification — None directly assigned.
- NFR implementation — [NFR-14](../engineering/TRACEABILITY.md#nfr-14).
- NFR verification — None directly assigned.

### CP-10.8

**Confirmed-trip reviews**

- Objective — Confirmed-trip reviews.
- Dependencies — [CP-10.6](#cp-106), [CP-11.6](#cp-116)
- Scope — Deliver transaction-backed reviews for this checkpoint.
- Exclusions — Unapproved public distribution, confidential partner data and paid launch commitments.
- Deliverables — Transaction-backed reviews.
- Acceptance criteria — Require confirmed-trip evidence and reject duplicate reviews.
- Target product release — V2.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-059](../product/REQUIREMENTS.md#fr-059).
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-10.9

**Transparent provider pricing**

- Objective — Transparent provider pricing.
- Dependencies — [CP-10.6](#cp-106)
- Scope — Deliver provider total-price disclosures for this checkpoint.
- Exclusions — Unapproved public distribution, confidential partner data and paid launch commitments.
- Deliverables — Provider total-price disclosures.
- Acceptance criteria — Include known mandatory charges and disclose unknown charges.
- Target product release — V2.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-060](../product/REQUIREMENTS.md#fr-060).
- FR support — [FR-057](../product/REQUIREMENTS.md#fr-057), [FR-063](../product/REQUIREMENTS.md#fr-063).
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-10.10

**Travel Circle and shared itineraries**

- Objective — Travel Circle and shared itineraries.
- Dependencies — [CP-9.13](#cp-913), [CP-4.12](#cp-412)
- Scope — Deliver selective trip sharing for this checkpoint.
- Exclusions — Unapproved public distribution, confidential partner data and paid launch commitments.
- Deliverables — Selective trip sharing.
- Acceptance criteria — Verify scoped fields, expiration and revocation.
- Target product release — V2.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-061](../product/REQUIREMENTS.md#fr-061).
- FR support — [FR-062](../product/REQUIREMENTS.md#fr-062), [FR-068](../product/REQUIREMENTS.md#fr-068), [FR-070](../product/REQUIREMENTS.md#fr-070).
- FR verification — None directly assigned.
- NFR implementation — [NFR-14](../engineering/TRACEABILITY.md#nfr-14).
- NFR verification — None directly assigned.

### CP-10.11

**Voluntary check-ins and consent controls**

- Objective — Voluntary check-ins and consent controls.
- Dependencies — [CP-10.10](#cp-1010), [CP-5.12](#cp-512)
- Scope — Deliver consent-based check-ins for this checkpoint.
- Exclusions — Unapproved public distribution, confidential partner data and paid launch commitments.
- Deliverables — Consent-based check-ins.
- Acceptance criteria — Verify opt-in, recipient and timestamp display, and revocation.
- Target product release — V2.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-062](../product/REQUIREMENTS.md#fr-062).
- FR support — [FR-072](../product/REQUIREMENTS.md#fr-072).
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-10.12

**Insurance partner integrations**

- Objective — Insurance partner integrations.
- Dependencies — [CP-10.7](#cp-107)
- Scope — Deliver insurance referrals for this checkpoint.
- Exclusions — Unapproved public distribution, confidential partner data and paid launch commitments.
- Deliverables — Insurance referrals.
- Acceptance criteria — Disclose terms and approved partner and verify no platform underwriting.
- Target product release — V2.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-063](../product/REQUIREMENTS.md#fr-063).
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — [NFR-14](../engineering/TRACEABILITY.md#nfr-14).
- NFR verification — None directly assigned.

### CP-10.13

**Medical and emergency assistance partnerships**

- Objective — Medical and emergency assistance partnerships.
- Dependencies — [CP-10.7](#cp-107)
- Scope — Deliver qualified assistance handoffs for this checkpoint.
- Exclusions — Unapproved public distribution, confidential partner data and paid launch commitments.
- Deliverables — Qualified assistance handoffs.
- Acceptance criteria — Verify approved contact and restrict platforms from making medical claims.
- Target product release — V2.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-064](../product/REQUIREMENTS.md#fr-064).
- FR support — [FR-074](../product/REQUIREMENTS.md#fr-074).
- FR verification — None directly assigned.
- NFR implementation — [NFR-14](../engineering/TRACEABILITY.md#nfr-14).
- NFR verification — None directly assigned.

### CP-10.14

**Creator monetization infrastructure**

- Objective — Creator monetization infrastructure.
- Dependencies — [CP-10.2](#cp-102), [CP-11.3](#cp-113), [CP-11.4](#cp-114)
- Scope — Deliver creator monetization ledger for this checkpoint.
- Exclusions — Unapproved public distribution, confidential partner data and paid launch commitments.
- Deliverables — Creator monetization ledger.
- Acceptance criteria — Reconcile creator earnings against transaction fixtures and show disclosures.
- Target product release — V2.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-065](../product/REQUIREMENTS.md#fr-065).
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

## Phase 11 — Commercialization & Enterprise

### CP-11.1

**Subscription and entitlement architecture**

- Objective — Subscription and entitlement architecture.
- Dependencies — [CP-9.13](#cp-913)
- Scope — Model entitlements and commercial controls while validating earlier pricing economics separately.
- Exclusions — Charging customers before explicit commercial approval.
- Deliverables — Subscription and entitlement contracts.
- Acceptance criteria — Validate entitlement transitions against approved pricing and require explicit commercialization approval.
- Target product release — V2.0 (proposed).
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-11.2

**Trip Pass lifecycle**

- Objective — Trip Pass lifecycle.
- Dependencies — [CP-11.1](#cp-111)
- Scope — Deliver trip Pass state machine for this checkpoint.
- Exclusions — Unapproved charging, undisclosed commissions and unrelated feature delivery.
- Deliverables — Trip Pass state machine.
- Acceptance criteria — Verify activation, cancellation, expiry and idempotent use.
- Target product release — V2.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-11.3

**Payment processing and billing**

- Objective — Payment processing and billing.
- Dependencies — [CP-11.2](#cp-112)
- Scope — Deliver billing integration and controls for this checkpoint.
- Exclusions — Unapproved charging, undisclosed commissions and unrelated feature delivery.
- Deliverables — Billing integration and controls.
- Acceptance criteria — Test payment webhooks, refunds and duplicate suppression using sandbox fixtures.
- Target product release — V2.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — [FR-065](../product/REQUIREMENTS.md#fr-065).
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-11.4

**Usage metering and cost attribution**

- Objective — Usage metering and cost attribution.
- Dependencies — [CP-11.3](#cp-113)
- Scope — Deliver usage and cost allocation for this checkpoint.
- Exclusions — Unapproved charging, undisclosed commissions and unrelated feature delivery.
- Deliverables — Usage and cost allocation.
- Acceptance criteria — Reconcile per-trip and tenant meters with usage fixtures.
- Target product release — V2.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — [FR-065](../product/REQUIREMENTS.md#fr-065).
- FR verification — None directly assigned.
- NFR implementation — [NFR-13](../engineering/TRACEABILITY.md#nfr-13).
- NFR verification — None directly assigned.

### CP-11.5

**Affiliate tracking and attribution**

- Objective — Affiliate tracking and attribution.
- Dependencies — [CP-11.4](#cp-114)
- Scope — Deliver affiliate attribution controls for this checkpoint.
- Exclusions — Unapproved charging, undisclosed commissions and unrelated feature delivery.
- Deliverables — Affiliate attribution controls.
- Acceptance criteria — Verify referral disclosure, consent and ranking independence.
- Target product release — V2.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — [NFR-13](../engineering/TRACEABILITY.md#nfr-13).
- NFR verification — None directly assigned.

### CP-11.6

**Marketplace commercial integrations**

- Objective — Marketplace commercial integrations.
- Dependencies — [CP-10.9](#cp-109), [CP-11.4](#cp-114)
- Scope — Deliver commercial marketplace integration for this checkpoint.
- Exclusions — Unapproved charging, undisclosed commissions and unrelated feature delivery.
- Deliverables — Commercial marketplace integration.
- Acceptance criteria — Verify catalog gating, approved terms and pricing scope.
- Target product release — V2.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — [FR-059](../product/REQUIREMENTS.md#fr-059).
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-11.7

**Enterprise API gateway**

- Objective — Enterprise API gateway.
- Dependencies — [CP-11.8](#cp-118), [CP-11.9](#cp-119)
- Scope — Deliver enterprise API gateway for this checkpoint.
- Exclusions — Unapproved charging, undisclosed commissions and unrelated feature delivery.
- Deliverables — Enterprise API gateway.
- Acceptance criteria — Verify versioned API auth, licensing and tenant boundaries.
- Target product release — V2.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-066](../product/REQUIREMENTS.md#fr-066).
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-11.8

**Organization and enterprise access management**

- Objective — Organization and enterprise access management.
- Dependencies — [CP-9.13](#cp-913), [CP-1.6](#cp-16)
- Scope — Deliver organization access management for this checkpoint.
- Exclusions — Unapproved charging, undisclosed commissions and unrelated feature delivery.
- Deliverables — Organization access management.
- Acceptance criteria — Deny cross-tenant access and verify organization roles and revocation.
- Target product release — V2.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — [FR-066](../product/REQUIREMENTS.md#fr-066).
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-11.9

**API quotas and commercial contracts**

- Objective — API quotas and commercial contracts.
- Dependencies — [CP-11.8](#cp-118)
- Scope — Deliver quota and contract controls for this checkpoint.
- Exclusions — Unapproved charging, undisclosed commissions and unrelated feature delivery.
- Deliverables — Quota and contract controls.
- Acceptance criteria — Test tenant quotas, throttling and commercial data-use restrictions.
- Target product release — V2.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — [FR-066](../product/REQUIREMENTS.md#fr-066).
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-11.10

**Revenue and product analytics**

- Objective — Revenue and product analytics.
- Dependencies — [CP-11.3](#cp-113), [CP-11.4](#cp-114)
- Scope — Deliver revenue and product analytics for this checkpoint.
- Exclusions — Unapproved charging, undisclosed commissions and unrelated feature delivery.
- Deliverables — Revenue and product analytics.
- Acceptance criteria — Reconcile revenue aggregates and redact personal data.
- Target product release — V2.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-11.11

**Commercial security and compliance review**

- Objective — Commercial security and compliance review.
- Dependencies — [CP-10.3](#cp-103), [CP-10.4](#cp-104), [CP-10.5](#cp-105), [CP-10.8](#cp-108), [CP-10.11](#cp-1011), [CP-10.12](#cp-1012), [CP-10.13](#cp-1013), [CP-10.14](#cp-1014), [CP-11.5](#cp-115), [CP-11.7](#cp-117), [CP-11.10](#cp-1110)
- Scope — Review commercialization and enterprise gates. Record native-app demand and scope decision separately.
- Exclusions — Automatic native-app commitment or unapproved monetization.
- Deliverables — Commercial acceptance and distribution decision.
- Acceptance criteria — Verify commercial and enterprise gates and record a separate demand-based native delivery decision.
- Target product release — V2.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — None directly assigned.
- FR verification — [FR-051](../product/REQUIREMENTS.md#fr-051), [FR-052](../product/REQUIREMENTS.md#fr-052), [FR-053](../product/REQUIREMENTS.md#fr-053), [FR-057](../product/REQUIREMENTS.md#fr-057), [FR-058](../product/REQUIREMENTS.md#fr-058), [FR-059](../product/REQUIREMENTS.md#fr-059), [FR-060](../product/REQUIREMENTS.md#fr-060), [FR-061](../product/REQUIREMENTS.md#fr-061), [FR-062](../product/REQUIREMENTS.md#fr-062), [FR-063](../product/REQUIREMENTS.md#fr-063), [FR-064](../product/REQUIREMENTS.md#fr-064), [FR-065](../product/REQUIREMENTS.md#fr-065), [FR-066](../product/REQUIREMENTS.md#fr-066).
- NFR implementation — None directly assigned.
- NFR verification — [NFR-13](../engineering/TRACEABILITY.md#nfr-13), [NFR-14](../engineering/TRACEABILITY.md#nfr-14).

## Phase 12 — Advanced Intelligence & Global Scale

### CP-12.1

**Advanced temporal knowledge analytics**

- Objective — Advanced temporal knowledge analytics.
- Dependencies — [CP-11.11](#cp-1111), [CP-2.7](#cp-27)
- Scope — Deliver advanced temporal analytics for this checkpoint.
- Exclusions — Unapproved sensitive data collection, autonomous bookings and unrelated product expansion.
- Deliverables — Advanced temporal analytics.
- Acceptance criteria — Reconstruct historical knowledge from as-of fixtures and document coverage gaps.
- Target product release — V3.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — [FR-073](../product/REQUIREMENTS.md#fr-073).
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-12.2

**Predictive destination intelligence**

- Objective — Predictive destination intelligence.
- Dependencies — [CP-12.1](#cp-121), [CP-12.3](#cp-123)
- Scope — Deliver predictive model evaluation for this checkpoint.
- Exclusions — Unapproved sensitive data collection, autonomous bookings and unrelated product expansion.
- Deliverables — Predictive model evaluation.
- Acceptance criteria — Compare with a holdout baseline and record uncertainty and drift.
- Target product release — V3.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-073](../product/REQUIREMENTS.md#fr-073).
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-12.3

**Historical travel disruption modeling**

- Objective — Historical travel disruption modeling.
- Dependencies — [CP-12.1](#cp-121), [CP-9.4](#cp-94)
- Scope — Deliver disruption modeling corpus for this checkpoint.
- Exclusions — Unapproved sensitive data collection, autonomous bookings and unrelated product expansion.
- Deliverables — Disruption modeling corpus.
- Acceptance criteria — Validate event chronology and outcome labels on a curated historical dataset.
- Target product release — V3.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — [FR-073](../product/REQUIREMENTS.md#fr-073).
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-12.4

**Advanced multi-objective recommendations**

- Objective — Advanced multi-objective recommendations.
- Dependencies — [CP-12.2](#cp-122), [CP-7.5](#cp-75)
- Scope — Deliver multi-objective recommendations for this checkpoint.
- Exclusions — Unapproved sensitive data collection, autonomous bookings and unrelated product expansion.
- Deliverables — Multi-objective recommendations.
- Acceptance criteria — Verify deterministic hard constraints and explain ranking trade-offs.
- Target product release — V3.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-12.5

**Multi-agent travel orchestration**

- Objective — Multi-agent travel orchestration.
- Dependencies — [CP-12.4](#cp-124), [CP-5.13](#cp-513)
- Scope — Deliver bounded workflow orchestration for this checkpoint.
- Exclusions — Unapproved sensitive data collection, autonomous bookings and unrelated product expansion.
- Deliverables — Bounded workflow orchestration.
- Acceptance criteria — Verify tool boundaries, termination and approval-only external actions.
- Target product release — V3.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — [FR-074](../product/REQUIREMENTS.md#fr-074).
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-12.6

**Partner-operated rebooking assistance**

- Objective — Partner-operated rebooking assistance.
- Dependencies — [CP-12.5](#cp-125), [CP-8.10](#cp-810), [CP-10.13](#cp-1013)
- Scope — Deliver partner rebooking handoff for this checkpoint.
- Exclusions — Unapproved sensitive data collection, autonomous bookings and unrelated product expansion.
- Deliverables — Partner rebooking handoff.
- Acceptance criteria — Require traveler approval and partner confirmation; verify zero autonomous purchases.
- Target product release — V3.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-074](../product/REQUIREMENTS.md#fr-074).
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — [NFR-14](../engineering/TRACEABILITY.md#nfr-14).
- NFR verification — None directly assigned.

### CP-12.7

**Internationalization and multilingual intelligence**

- Objective — Internationalization and multilingual intelligence.
- Dependencies — [CP-6.14](#cp-614), [CP-2.4](#cp-24)
- Scope — Deliver the narrow locale and currency slice in V1.1; expand languages and markets in V3.0 subject to approval.
- Exclusions — Delaying FR-030 or promising broad V1.1 internationalization.
- Deliverables — Localized foundation slice and global expansion.
- Acceptance criteria — Preserve original units and rate timestamps for V1.1; test advanced multilingual coverage separately.
- Target product release — V1.1 / V3.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-030](../product/REQUIREMENTS.md#fr-030).
- FR support — [FR-019](../product/REQUIREMENTS.md#fr-019), [FR-053](../product/REQUIREMENTS.md#fr-053).
- FR verification — [FR-030](../product/REQUIREMENTS.md#fr-030).
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-12.8

**Global destination coverage expansion**

- Objective — Global destination coverage expansion.
- Dependencies — [CP-11.11](#cp-1111), [CP-12.7](#cp-127)
- Scope — Deliver coverage expansion controls for this checkpoint.
- Exclusions — Unapproved sensitive data collection, autonomous bookings and unrelated product expansion.
- Deliverables — Coverage expansion controls.
- Acceptance criteria — Audit each new geography against provenance, quality and operational thresholds.
- Target product release — V3.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-12.9

**Multi-region infrastructure**

- Objective — Multi-region infrastructure.
- Dependencies — [CP-12.8](#cp-128)
- Scope — Deliver multi-region design and resilience evidence for this checkpoint.
- Exclusions — Unapproved sensitive data collection, autonomous bookings and unrelated product expansion.
- Deliverables — Multi-region design and resilience evidence.
- Acceptance criteria — Demonstrate approved recovery and routing objectives under simulated regional loss.
- Target product release — V3.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-12.10

**Large-scale data processing optimization**

- Objective — Large-scale data processing optimization.
- Dependencies — [CP-12.9](#cp-129)
- Scope — Deliver large-scale processing evaluation for this checkpoint.
- Exclusions — Unapproved sensitive data collection, autonomous bookings and unrelated product expansion.
- Deliverables — Large-scale processing evaluation.
- Acceptance criteria — Establish a benchmark and verify throughput and cost under agreed workload.
- Target product release — V3.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-12.11

**Enterprise intelligence products**

- Objective — Enterprise intelligence products.
- Dependencies — [CP-12.10](#cp-1210), [CP-11.11](#cp-1111)
- Scope — Deliver advanced enterprise products for this checkpoint.
- Exclusions — Unapproved sensitive data collection, autonomous bookings and unrelated product expansion.
- Deliverables — Advanced enterprise products.
- Acceptance criteria — Demonstrate tenant controls and signed data scope for each proposed product.
- Target product release — V3.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — None directly assigned.
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-12.12

**Advanced privacy-preserving personalization**

- Objective — Advanced privacy-preserving personalization.
- Dependencies — [CP-12.5](#cp-125), [CP-6.5](#cp-65)
- Scope — Plan protected-document work only with D17 approval alongside advanced personalization.
- Exclusions — Document storage or sharing before separate approval.
- Deliverables — Privacy-preserving personalization and protected-document decision.
- Acceptance criteria — Require separate D17 approval; if authorized, test vault encryption, sharing expiry and audit controls.
- Target product release — V3.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-067](../product/REQUIREMENTS.md#fr-067), [FR-068](../product/REQUIREMENTS.md#fr-068), [FR-069](../product/REQUIREMENTS.md#fr-069).
- FR support — None directly assigned.
- FR verification — None directly assigned.
- NFR implementation — None directly assigned.
- NFR verification — None directly assigned.

### CP-12.13

**Continuous platform maturity assessment**

- Objective — Continuous platform maturity assessment.
- Dependencies — [CP-12.6](#cp-126), [CP-12.11](#cp-1211), [CP-12.12](#cp-1212)
- Scope — Review maturity and gated community groups, messages and meetups only with D17 approval.
- Exclusions — Community rollout before separate approval.
- Deliverables — Platform maturity and deferred social decision.
- Acceptance criteria — Require separate D17 approval; if authorized, verify membership, message restrictions, reporting and meetup privacy.
- Target product release — V3.0.
- Exit gate — Record passing checkpoint evidence and obtain owner acceptance before dependent work.
- Implementation status — Not Started.
- FR primary — [FR-070](../product/REQUIREMENTS.md#fr-070), [FR-071](../product/REQUIREMENTS.md#fr-071), [FR-072](../product/REQUIREMENTS.md#fr-072).
- FR support — None directly assigned.
- FR verification — [FR-067](../product/REQUIREMENTS.md#fr-067), [FR-068](../product/REQUIREMENTS.md#fr-068), [FR-069](../product/REQUIREMENTS.md#fr-069), [FR-070](../product/REQUIREMENTS.md#fr-070), [FR-071](../product/REQUIREMENTS.md#fr-071), [FR-072](../product/REQUIREMENTS.md#fr-072), [FR-073](../product/REQUIREMENTS.md#fr-073), [FR-074](../product/REQUIREMENTS.md#fr-074).
- NFR implementation — None directly assigned.
- NFR verification — [NFR-14](../engineering/TRACEABILITY.md#nfr-14).
