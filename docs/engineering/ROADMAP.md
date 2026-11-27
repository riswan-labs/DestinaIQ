# Engineering roadmap

Checkpoints are gated by evidence and project-owner approval. Status is maintained in [progress](PROGRESS.md). Acceptance criteria below are planned except where progress records evidence. Phases 0–6 lead to Core Destination Intelligence. Phases 7–12 stage later releases. Each phase depends on acceptance of its preceding phase, and its exit requires every checkpoint below to meet its exit gate. Release phases also require the linked release gate.

## Design V3 checkpoint crosswalk

| Original | Intent and slice | Engineering checkpoints |
| --- | --- | --- |
| A | Discovery | [CP-0.1](#cp-01), [CP-0.2](#cp-02) |
| B | Platform and release recovery | [CP-1.1](#cp-11), [CP-6.1](#cp-61) |
| C | Geography and temporal evidence | [CP-2.1](#cp-21), [CP-3.3](#cp-33) |
| D | Launch climate/forecasts, then advanced environment | [CP-3.1](#cp-31), [CP-6.1](#cp-61), [CP-7.1](#cp-71) |
| E | Launch events and safety, then comparisons and map | [CP-3.2](#cp-32), [CP-6.1](#cp-61), [CP-9.1](#cp-91) |
| F | Launch comparisons and ranking, then atlas | [CP-3.3](#cp-33), [CP-4.1](#cp-41), [CP-6.1](#cp-61), [CP-7.1](#cp-71) |
| G | Grounded planning, then simulator, readiness and optimization | [CP-5.1](#cp-51), [CP-6.1](#cp-61), [CP-7.2](#cp-72), [CP-8.2](#cp-82) |
| H | Launch monitor, then reservation, aviation and graph | [CP-4.2](#cp-42), [CP-5.2](#cp-52), [CP-6.1](#cp-61), [CP-8.1](#cp-81), [CP-8.2](#cp-82) |
| I | Hyperlocal and parking | [CP-9.1](#cp-91), [CP-9.2](#cp-92) |
| J | Creator experiences | [CP-10.1](#cp-101) |
| K | Provider trust | [CP-10.2](#cp-102) |
| L | Care and Circle | [CP-10.3](#cp-103) |
| M | Commercial and enterprise | [CP-11.1](#cp-111), [CP-11.2](#cp-112) |
| N | Expansion | [CP-12.1](#cp-121), [CP-12.2](#cp-122) |

## Phase 0 — Product & Engineering Readiness

### CP-0.1

**Design baseline and requirements traceability**

- Dependencies — Design V3 and checkpoint authorization
- Design V3 — A
- Deliverables — Versioned design, requirements, governance and draft PR.
- Acceptance and exit gate — 80 source IDs and 15 launch mappings reconcile, original file hash matches and owner reviews draft evidence.

### CP-0.2

**Discovery and readiness validation**

- Dependencies — [CP-0.1](#cp-01)
- Design V3 — A
- Deliverables — Benchmark evidence, interviews, source feasibility, quotes, threat/privacy assessments and name clearance.
- Acceptance and exit gate — All A.1–A.6 findings recorded with owner decisions and blockers. Owner approves launch scope and Phase 1 entry.

## Phase 1 — Platform Foundation

### CP-1.1

**Platform foundation**

- Dependencies — [CP-0.2](#cp-02)
- Design V3 — B
- Deliverables — Reproducible app environment, identity, secure CI/CD, migration pipeline and telemetry.
- Acceptance and exit gate — Clean setup and pipeline runs succeed, identity and migration rollback tested, defensive security and baseline recovery demonstrated.
- Requirements — [NFR-02](TRACEABILITY.md#nfr-02).

## Phase 2 — Global Destination Knowledge Platform

### CP-2.1

**Canonical geography and temporal evidence**

- Dependencies — [CP-1.1](#cp-11)
- Design V3 — C
- Deliverables — PostgreSQL schema, PostGIS geometry, evidence and temporal facts, rebuildable retrieval projections.
- Acceptance and exit gate — Canonical IDs, time-as-of queries, geography fixtures, critical evidence validity and projection rebuilds pass.
- Requirements — [FR-023](../product/REQUIREMENTS.md#fr-023), [FR-024](../product/REQUIREMENTS.md#fr-024), [NFR-03](TRACEABILITY.md#nfr-03).

## Phase 3 — Data Ingestion & Destination Intelligence

### CP-3.1

**Climate, weather and tourism ingestion**

- Dependencies — [CP-2.1](#cp-21)
- Design V3 — D
- Deliverables — Climate normals, forecast and season data with rights and expiry rules.
- Acceptance and exit gate — Verify monthly coverage, forecast staleness and licensed source freshness; prove replay, retry and quarantine controls.
- Requirements — [FR-004](../product/REQUIREMENTS.md#fr-004), [FR-005](../product/REQUIREMENTS.md#fr-005), [NFR-04](TRACEABILITY.md#nfr-04).

### CP-3.2

**Advisories, news and review**

- Dependencies — [CP-2.1](#cp-21)
- Design V3 — E
- Deliverables — Official advisories, clustered news and administrative quarantine workflow.
- Acceptance and exit gate — Test conflicting issuers, deduplication, irrelevant events, corrections and reviewed publication.
- Requirements — [FR-007](../product/REQUIREMENTS.md#fr-007), [FR-008](../product/REQUIREMENTS.md#fr-008), [FR-028](../product/REQUIREMENTS.md#fr-028).

### CP-3.3

**Attractions, transit and practical data**

- Dependencies — [CP-2.1](#cp-21)
- Design V3 — C, F
- Deliverables — Sourced attractions, airport gateways, route data and travel essentials.
- Acceptance and exit gate — Verify airport service relationships, canonical POIs, dated fields and explicit unknowns.
- Requirements — [FR-011](../product/REQUIREMENTS.md#fr-011), [FR-012](../product/REQUIREMENTS.md#fr-012), [FR-013](../product/REQUIREMENTS.md#fr-013), [FR-042](../product/REQUIREMENTS.md#fr-042).

## Phase 4 — Core Consumer Application

### CP-4.1

**Discover and compare**

- Dependencies — [CP-3.1](#cp-31), [CP-3.2](#cp-32), [CP-3.3](#cp-33)
- Design V3 — F
- Deliverables — Responsive profiles, alias search, comparisons and deterministic best-time ranking.
- Acceptance and exit gate — Verify curated search, disambiguation, rationale and missing values. Reject comparisons beyond four.
- Requirements — [FR-001](../product/REQUIREMENTS.md#fr-001), [FR-002](../product/REQUIREMENTS.md#fr-002), [FR-003](../product/REQUIREMENTS.md#fr-003), [FR-006](../product/REQUIREMENTS.md#fr-006), [FR-014](../product/REQUIREMENTS.md#fr-014).

### CP-4.2

**Saved trips and account controls**

- Dependencies — [CP-1.1](#cp-11), [CP-4.1](#cp-41)
- Design V3 — H
- Deliverables — Saved trips, accuracy reports, privacy controls and user data lifecycle.
- Acceptance and exit gate — Verify report reference, cross-user isolation, date edits, deletion and export.
- Requirements — [FR-015](../product/REQUIREMENTS.md#fr-015), [FR-026](../product/REQUIREMENTS.md#fr-026), [FR-029](../product/REQUIREMENTS.md#fr-029), [NFR-01](TRACEABILITY.md#nfr-01).

## Phase 5 — AI & Proactive Intelligence

### CP-5.1

**Grounded itinerary planning**

- Dependencies — [CP-4.2](#cp-42)
- Design V3 — G
- Deliverables — Editable itineraries validated against hours, transfers and other constraints.
- Acceptance and exit gate — Golden set proves grounded and feasible itineraries, unknowns shown and unauthorized tools denied.
- Requirements — [FR-016](../product/REQUIREMENTS.md#fr-016), [NFR-05](TRACEABILITY.md#nfr-05).

### CP-5.2

**Launch briefings and urgent alerts**

- Dependencies — [CP-3.2](#cp-32), [CP-4.2](#cp-42)
- Design V3 — H
- Deliverables — Trip correlation, consent, weekly digest and urgent event worker.
- Acceptance and exit gate — Verify exact-once delivery on replay, corrections, consent, quiet hours and end-of-trip cutoff.
- Requirements — [FR-020](../product/REQUIREMENTS.md#fr-020), [FR-021](../product/REQUIREMENTS.md#fr-021), [FR-040](../product/REQUIREMENTS.md#fr-040), [FR-041](../product/REQUIREMENTS.md#fr-041), [NFR-10](TRACEABILITY.md#nfr-10).

## Phase 6 — Production Readiness & V1.0 Launch

Phase exit also requires [Gate V1.0](../product/RELEASE_STRATEGY.md#gate-v10).

### CP-6.1

**Launch certification**

- Dependencies — [CP-5.1](#cp-51), [CP-5.2](#cp-52)
- Design V3 — B, D–H
- Deliverables — Coverage evidence, load and restore tests, accessibility, security review and rollback plan.
- Acceptance and exit gate — All V1.0 gates signed with agreed load, market coverage, test evidence and release owner approval.
- Requirements — [NFR-06](TRACEABILITY.md#nfr-06), [NFR-07](TRACEABILITY.md#nfr-07), [NFR-08](TRACEABILITY.md#nfr-08), [NFR-09](TRACEABILITY.md#nfr-09).

## Phase 7 — Intelligent Discovery

Phase exit also requires [Gate V1.1](../product/RELEASE_STRATEGY.md#gate-v11).

### CP-7.1

**Environmental discovery**

- Dependencies — [CP-6.1](#cp-61)
- Design V3 — D, F
- Deliverables — Atlas, AQI, filters, activity windows and suitability explanations.
- Acceptance and exit gate — Verify missing coverage, validated AQI standard/expiry, activity windows and safety constraints.
- Requirements — [FR-031](../product/REQUIREMENTS.md#fr-031), [FR-032](../product/REQUIREMENTS.md#fr-032), [FR-033](../product/REQUIREMENTS.md#fr-033), [FR-034](../product/REQUIREMENTS.md#fr-034), [FR-035](../product/REQUIREMENTS.md#fr-035).

### CP-7.2

**Expanded planning and readiness**

- Dependencies — [CP-7.1](#cp-71)
- Design V3 — G
- Deliverables — Packing, entry, budget, Q&A, offline and printable reports, localization, profiles, simulator and readiness.
- Acceptance and exit gate — Pass V1.1 fixture suite with cited unknown handling, offline date, currency and reproducible scenarios.
- Requirements — [FR-017](../product/REQUIREMENTS.md#fr-017), [FR-018](../product/REQUIREMENTS.md#fr-018), [FR-019](../product/REQUIREMENTS.md#fr-019), [FR-022](../product/REQUIREMENTS.md#fr-022), [FR-025](../product/REQUIREMENTS.md#fr-025), [FR-030](../product/REQUIREMENTS.md#fr-030), [FR-048](../product/REQUIREMENTS.md#fr-048), [FR-049](../product/REQUIREMENTS.md#fr-049), [FR-055](../product/REQUIREMENTS.md#fr-055), [FR-056](../product/REQUIREMENTS.md#fr-056).

## Phase 8 — Connected Travel Companion

Phase exit also requires [Gate V1.2](../product/RELEASE_STRATEGY.md#gate-v12).

### CP-8.1

**Reservations and aviation**

- Dependencies — [CP-7.2](#cp-72)
- Design V3 — H
- Deliverables — Manual reservations, consented imports and flight feed.
- Acceptance and exit gate — Owner validates provider costs, data rights, retention and isolation. OAuth requires separate approval.
- Requirements — [FR-045](../product/REQUIREMENTS.md#fr-045), [FR-046](../product/REQUIREMENTS.md#fr-046), [NFR-11](TRACEABILITY.md#nfr-11).

### CP-8.2

**Connected trip intelligence**

- Dependencies — [CP-8.1](#cp-81)
- Design V3 — G, H
- Deliverables — Trip dependencies, dynamic briefings and adaptive optimization.
- Acceptance and exit gate — Verify V1.2 trip impact, graph cycles, cadence boundaries and confirmed booking protections.
- Requirements — [FR-027](../product/REQUIREMENTS.md#fr-027), [FR-039](../product/REQUIREMENTS.md#fr-039), [FR-047](../product/REQUIREMENTS.md#fr-047), [FR-050](../product/REQUIREMENTS.md#fr-050).

## Phase 9 — Hyperlocal Intelligence

Phase exit also requires [Gate V1.3](../product/RELEASE_STRATEGY.md#gate-v13).

### CP-9.1

**Hyperlocal and local safety**

- Dependencies — [CP-8.2](#cp-82)
- Design V3 — E, I
- Deliverables — Incident maps, advisory and history views, crime/scam evidence and hotel-area assessments.
- Acceptance and exit gate — Confirm geographic precision, bias and coverage thresholds, moderation, conflicting source treatment and as-of correctness.
- Requirements — [FR-009](../product/REQUIREMENTS.md#fr-009), [FR-010](../product/REQUIREMENTS.md#fr-010), [FR-036](../product/REQUIREMENTS.md#fr-036), [FR-037](../product/REQUIREMENTS.md#fr-037), [FR-038](../product/REQUIREMENTS.md#fr-038), [FR-043](../product/REQUIREMENTS.md#fr-043), [FR-044](../product/REQUIREMENTS.md#fr-044), [FR-054](../product/REQUIREMENTS.md#fr-054), [NFR-12](TRACEABILITY.md#nfr-12).

### CP-9.2

**Parking intelligence**

- Dependencies — [CP-9.1](#cp-91)
- Design V3 — I
- Deliverables — Parking discovery, airport transfers, accessible and EV data, driving plans and licensed availability.
- Acceptance and exit gate — Pass V1.3 expiry and geospatial fixtures with category-level coverage approval.
- Requirements — [FR-075](../product/REQUIREMENTS.md#fr-075), [FR-076](../product/REQUIREMENTS.md#fr-076), [FR-077](../product/REQUIREMENTS.md#fr-077), [FR-078](../product/REQUIREMENTS.md#fr-078), [FR-079](../product/REQUIREMENTS.md#fr-079), [FR-080](../product/REQUIREMENTS.md#fr-080).

## Phase 10 — Travel Ecosystem

### CP-10.1

**Creator and experience networks**

- Dependencies — [CP-9.2](#cp-92)
- Design V3 — J
- Deliverables — Moderated rights and verified expenses.
- Acceptance and exit gate — Verify permission revocation, location linkage, expense provenance, moderation and dispute handling.
- Requirements — [FR-051](../product/REQUIREMENTS.md#fr-051), [FR-052](../product/REQUIREMENTS.md#fr-052), [FR-053](../product/REQUIREMENTS.md#fr-053).

### CP-10.2

**Provider trust**

- Dependencies — [CP-10.1](#cp-101)
- Design V3 — K
- Deliverables — Credential registry, verified reviews and transparent offers.
- Acceptance and exit gate — Demonstrate eligibility, expiry, transaction verification and pricing disclosures.
- Requirements — [FR-057](../product/REQUIREMENTS.md#fr-057), [FR-058](../product/REQUIREMENTS.md#fr-058), [FR-059](../product/REQUIREMENTS.md#fr-059), [FR-060](../product/REQUIREMENTS.md#fr-060).

### CP-10.3

**Travel Circle and qualified care**

- Dependencies — [CP-10.2](#cp-102)
- Design V3 — L
- Deliverables — Privacy-scoped sharing and approved referral partners.
- Acceptance and exit gate — Verify consent, audience restriction, expiry, revocation and evidence of qualified partner contracts.
- Requirements — [FR-061](../product/REQUIREMENTS.md#fr-061), [FR-062](../product/REQUIREMENTS.md#fr-062), [FR-063](../product/REQUIREMENTS.md#fr-063), [FR-064](../product/REQUIREMENTS.md#fr-064), [NFR-14](TRACEABILITY.md#nfr-14).

## Phase 11 — Commercialization & Enterprise

Phase exit also requires [Gate V2.0](../product/RELEASE_STRATEGY.md#gate-v20).

### CP-11.1

**Commercial validation**

- Dependencies — [CP-10.3](#cp-103)
- Design V3 — M
- Deliverables — Pricing experiments, contribution model, creator ledger and payment controls.
- Acceptance and exit gate — Reconcile ledger, test material usage scenarios and agree margins and support cost thresholds.
- Requirements — [FR-065](../product/REQUIREMENTS.md#fr-065), [NFR-13](TRACEABILITY.md#nfr-13).

### CP-11.2

**Enterprise and distribution**

- Dependencies — [CP-11.1](#cp-111)
- Design V3 — M
- Deliverables — Licensed APIs and conditional demand-based native distribution decision.
- Acceptance and exit gate — Verify tenant isolation, licensing and rate limits. Record V2.0 economics and distribution go/no-go.
- Requirements — [FR-066](../product/REQUIREMENTS.md#fr-066).

## Phase 12 — Advanced Intelligence & Global Scale

Phase exit also requires [Gate V3.0](../product/RELEASE_STRATEGY.md#gate-v30).

### CP-12.1

**Predictive analytics and partner rebooking**

- Dependencies — [CP-11.2](#cp-112)
- Design V3 — N
- Deliverables — Calibrated prediction workflows and confirmation-driven partner handoff.
- Acceptance and exit gate — Verify holdout performance, drift, approval boundaries and operational value.
- Requirements — [FR-073](../product/REQUIREMENTS.md#fr-073), [FR-074](../product/REQUIREMENTS.md#fr-074).

### CP-12.2

**Deferred strategic scope and scale gate**

- Dependencies — [CP-12.1](#cp-121)
- Design V3 — N
- Deliverables — Demand/risk decision for vault, sharing, audits and social features, plus scale readiness.
- Acceptance and exit gate — Obtain separate authorization before sensitive implementation. Pass privacy and moderation gates and V3.0 evidence review.
- Requirements — [FR-067](../product/REQUIREMENTS.md#fr-067), [FR-068](../product/REQUIREMENTS.md#fr-068), [FR-069](../product/REQUIREMENTS.md#fr-069), [FR-070](../product/REQUIREMENTS.md#fr-070), [FR-071](../product/REQUIREMENTS.md#fr-071), [FR-072](../product/REQUIREMENTS.md#fr-072).
