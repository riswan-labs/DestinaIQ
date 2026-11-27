# Release strategy

Design specification **v3.0** is the source baseline. Product releases **V1.0 through V3.0** are independent identifiers. The FR registry carries Design V3 §21 assignments as the planning baseline. Section 22 still requires validation and owner sign-off. Launch criteria follow [launch scope](LAUNCH_SCOPE.md). The release owner records evidence and signs each gate. Each release requires assigned acceptance tests, applicable controls, no critical security findings and a verified rollback plan. All release gates are pending. The [release reconciliation](RELEASE_RECONCILIATION.md) identifies cross-phase slices and open scheduling decisions. V1.0 gates exclude public Q&A and optional preferences. V1.1 requires the narrow Q&A, offline summary, printable report and locale/currency slices before release.

## Gate V1.0

Core Destination Intelligence. Launch web and mandatory security, administration, operations, privacy and provenance controls.

Approve launch markets and publish coverage and limitations. Audit 100% critical claim attribution. Verify correction and deduplication, accessibility, accepted SLO loads, timed restore and rollback. Measure search success and research time in usability trials.

Exit checkpoints [CP-6.14](../engineering/ROADMAP.md#cp-614).

Requirements [FR-001](../product/REQUIREMENTS.md#fr-001), [FR-002](../product/REQUIREMENTS.md#fr-002), [FR-003](../product/REQUIREMENTS.md#fr-003), [FR-004](../product/REQUIREMENTS.md#fr-004), [FR-005](../product/REQUIREMENTS.md#fr-005), [FR-006](../product/REQUIREMENTS.md#fr-006), [FR-007](../product/REQUIREMENTS.md#fr-007), [FR-008](../product/REQUIREMENTS.md#fr-008), [FR-011](../product/REQUIREMENTS.md#fr-011), [FR-012](../product/REQUIREMENTS.md#fr-012), [FR-013](../product/REQUIREMENTS.md#fr-013), [FR-014](../product/REQUIREMENTS.md#fr-014), [FR-015](../product/REQUIREMENTS.md#fr-015), [FR-016](../product/REQUIREMENTS.md#fr-016), [FR-020](../product/REQUIREMENTS.md#fr-020), [FR-021](../product/REQUIREMENTS.md#fr-021), [FR-023](../product/REQUIREMENTS.md#fr-023), [FR-024](../product/REQUIREMENTS.md#fr-024), [FR-026](../product/REQUIREMENTS.md#fr-026), [FR-028](../product/REQUIREMENTS.md#fr-028), [FR-029](../product/REQUIREMENTS.md#fr-029), [FR-040](../product/REQUIREMENTS.md#fr-040), [FR-041](../product/REQUIREMENTS.md#fr-041), [FR-042](../product/REQUIREMENTS.md#fr-042).

Cross-cutting controls [NFR-01](../engineering/TRACEABILITY.md#nfr-01), [NFR-02](../engineering/TRACEABILITY.md#nfr-02), [NFR-03](../engineering/TRACEABILITY.md#nfr-03), [NFR-04](../engineering/TRACEABILITY.md#nfr-04), [NFR-05](../engineering/TRACEABILITY.md#nfr-05), [NFR-06](../engineering/TRACEABILITY.md#nfr-06), [NFR-07](../engineering/TRACEABILITY.md#nfr-07), [NFR-08](../engineering/TRACEABILITY.md#nfr-08), [NFR-09](../engineering/TRACEABILITY.md#nfr-09), [NFR-10](../engineering/TRACEABILITY.md#nfr-10), [NFR-13](../engineering/TRACEABILITY.md#nfr-13).

## Gate V1.1

Intelligent Discovery. Seasonal atlas, environment, activity windows, packing, entry, budgets, Q&A, offline, locale/currency, readiness and simulation.

Prove seasonal ranking and eligibility, documented unknowns, valid entry evidence and planning feasibility. Review incremental provider cost and geographic coverage.

Exit checkpoints [CP-7.9](../engineering/ROADMAP.md#cp-79), [CP-8.12](../engineering/ROADMAP.md#cp-812), [CP-8.13](../engineering/ROADMAP.md#cp-813), [CP-12.7](../engineering/ROADMAP.md#cp-127).

Requirements [FR-017](../product/REQUIREMENTS.md#fr-017), [FR-018](../product/REQUIREMENTS.md#fr-018), [FR-019](../product/REQUIREMENTS.md#fr-019), [FR-022](../product/REQUIREMENTS.md#fr-022), [FR-025](../product/REQUIREMENTS.md#fr-025), [FR-030](../product/REQUIREMENTS.md#fr-030), [FR-031](../product/REQUIREMENTS.md#fr-031), [FR-032](../product/REQUIREMENTS.md#fr-032), [FR-033](../product/REQUIREMENTS.md#fr-033), [FR-034](../product/REQUIREMENTS.md#fr-034), [FR-035](../product/REQUIREMENTS.md#fr-035), [FR-048](../product/REQUIREMENTS.md#fr-048), [FR-049](../product/REQUIREMENTS.md#fr-049), [FR-055](../product/REQUIREMENTS.md#fr-055), [FR-056](../product/REQUIREMENTS.md#fr-056).

Cross-cutting controls [NFR-01](../engineering/TRACEABILITY.md#nfr-01), [NFR-02](../engineering/TRACEABILITY.md#nfr-02), [NFR-03](../engineering/TRACEABILITY.md#nfr-03), [NFR-04](../engineering/TRACEABILITY.md#nfr-04), [NFR-05](../engineering/TRACEABILITY.md#nfr-05), [NFR-06](../engineering/TRACEABILITY.md#nfr-06), [NFR-07](../engineering/TRACEABILITY.md#nfr-07), [NFR-08](../engineering/TRACEABILITY.md#nfr-08), [NFR-09](../engineering/TRACEABILITY.md#nfr-09), [NFR-10](../engineering/TRACEABILITY.md#nfr-10), [NFR-13](../engineering/TRACEABILITY.md#nfr-13).

## Gate V1.2

Connected Travel Companion. Manual reservations then approved imports, flight feeds, Digital Twin, adaptive planning and dynamic briefings.

Approve reservation privacy and threat evidence, rights and vendor cost for aviation and daily briefings. Verify impact across dependencies and enforce the separate OAuth gate.

Exit checkpoints [CP-8.14](../engineering/ROADMAP.md#cp-814).

Requirements [FR-027](../product/REQUIREMENTS.md#fr-027), [FR-039](../product/REQUIREMENTS.md#fr-039), [FR-045](../product/REQUIREMENTS.md#fr-045), [FR-046](../product/REQUIREMENTS.md#fr-046), [FR-047](../product/REQUIREMENTS.md#fr-047), [FR-050](../product/REQUIREMENTS.md#fr-050).

Cross-cutting controls [NFR-01](../engineering/TRACEABILITY.md#nfr-01), [NFR-02](../engineering/TRACEABILITY.md#nfr-02), [NFR-03](../engineering/TRACEABILITY.md#nfr-03), [NFR-04](../engineering/TRACEABILITY.md#nfr-04), [NFR-05](../engineering/TRACEABILITY.md#nfr-05), [NFR-06](../engineering/TRACEABILITY.md#nfr-06), [NFR-07](../engineering/TRACEABILITY.md#nfr-07), [NFR-08](../engineering/TRACEABILITY.md#nfr-08), [NFR-09](../engineering/TRACEABILITY.md#nfr-09), [NFR-10](../engineering/TRACEABILITY.md#nfr-10), [NFR-11](../engineering/TRACEABILITY.md#nfr-11), [NFR-13](../engineering/TRACEABILITY.md#nfr-13).

## Gate V1.3

Hyperlocal Intelligence. Local assessments, incident maps, historical intelligence and parking subject to coverage.

Require bias and coverage review and documented spatial precision. Require licensed live parking availability and an explicit freshness SLA before coverage is published.

Exit checkpoints [CP-9.13](../engineering/ROADMAP.md#cp-913).

Requirements [FR-009](../product/REQUIREMENTS.md#fr-009), [FR-010](../product/REQUIREMENTS.md#fr-010), [FR-036](../product/REQUIREMENTS.md#fr-036), [FR-037](../product/REQUIREMENTS.md#fr-037), [FR-038](../product/REQUIREMENTS.md#fr-038), [FR-043](../product/REQUIREMENTS.md#fr-043), [FR-044](../product/REQUIREMENTS.md#fr-044), [FR-054](../product/REQUIREMENTS.md#fr-054), [FR-075](../product/REQUIREMENTS.md#fr-075), [FR-076](../product/REQUIREMENTS.md#fr-076), [FR-077](../product/REQUIREMENTS.md#fr-077), [FR-078](../product/REQUIREMENTS.md#fr-078), [FR-079](../product/REQUIREMENTS.md#fr-079), [FR-080](../product/REQUIREMENTS.md#fr-080).

Cross-cutting controls [NFR-01](../engineering/TRACEABILITY.md#nfr-01), [NFR-02](../engineering/TRACEABILITY.md#nfr-02), [NFR-03](../engineering/TRACEABILITY.md#nfr-03), [NFR-04](../engineering/TRACEABILITY.md#nfr-04), [NFR-05](../engineering/TRACEABILITY.md#nfr-05), [NFR-06](../engineering/TRACEABILITY.md#nfr-06), [NFR-07](../engineering/TRACEABILITY.md#nfr-07), [NFR-08](../engineering/TRACEABILITY.md#nfr-08), [NFR-09](../engineering/TRACEABILITY.md#nfr-09), [NFR-10](../engineering/TRACEABILITY.md#nfr-10), [NFR-11](../engineering/TRACEABILITY.md#nfr-11), [NFR-12](../engineering/TRACEABILITY.md#nfr-12), [NFR-13](../engineering/TRACEABILITY.md#nfr-13).

## Gate V2.0

Travel Ecosystem and Enterprise. Creator and provider networks, care, Travel Circle and licensed APIs. Native apps depend on demand.

Verify contractual authority and reviews, moderation, partner boundaries, opt-in, revocation, independent ranking, evidence-backed contribution and tenant isolation.

Exit checkpoints [CP-11.11](../engineering/ROADMAP.md#cp-1111).

Requirements [FR-051](../product/REQUIREMENTS.md#fr-051), [FR-052](../product/REQUIREMENTS.md#fr-052), [FR-053](../product/REQUIREMENTS.md#fr-053), [FR-057](../product/REQUIREMENTS.md#fr-057), [FR-058](../product/REQUIREMENTS.md#fr-058), [FR-059](../product/REQUIREMENTS.md#fr-059), [FR-060](../product/REQUIREMENTS.md#fr-060), [FR-061](../product/REQUIREMENTS.md#fr-061), [FR-062](../product/REQUIREMENTS.md#fr-062), [FR-063](../product/REQUIREMENTS.md#fr-063), [FR-064](../product/REQUIREMENTS.md#fr-064), [FR-065](../product/REQUIREMENTS.md#fr-065), [FR-066](../product/REQUIREMENTS.md#fr-066).

Cross-cutting controls [NFR-01](../engineering/TRACEABILITY.md#nfr-01), [NFR-02](../engineering/TRACEABILITY.md#nfr-02), [NFR-03](../engineering/TRACEABILITY.md#nfr-03), [NFR-04](../engineering/TRACEABILITY.md#nfr-04), [NFR-05](../engineering/TRACEABILITY.md#nfr-05), [NFR-06](../engineering/TRACEABILITY.md#nfr-06), [NFR-07](../engineering/TRACEABILITY.md#nfr-07), [NFR-08](../engineering/TRACEABILITY.md#nfr-08), [NFR-09](../engineering/TRACEABILITY.md#nfr-09), [NFR-10](../engineering/TRACEABILITY.md#nfr-10), [NFR-11](../engineering/TRACEABILITY.md#nfr-11), [NFR-12](../engineering/TRACEABILITY.md#nfr-12), [NFR-13](../engineering/TRACEABILITY.md#nfr-13), [NFR-14](../engineering/TRACEABILITY.md#nfr-14).

## Gate V3.0

Advanced Intelligence. Predictions and partner rebooking. Deferred vault and social features require separate approval.

Approve demand and risk case for deferred features. Verify calibration, drift, partner approval, encrypted deletion and community moderation before any authorized rollout.

Exit checkpoints [CP-12.13](../engineering/ROADMAP.md#cp-1213).

Requirements [FR-067](../product/REQUIREMENTS.md#fr-067), [FR-068](../product/REQUIREMENTS.md#fr-068), [FR-069](../product/REQUIREMENTS.md#fr-069), [FR-070](../product/REQUIREMENTS.md#fr-070), [FR-071](../product/REQUIREMENTS.md#fr-071), [FR-072](../product/REQUIREMENTS.md#fr-072), [FR-073](../product/REQUIREMENTS.md#fr-073), [FR-074](../product/REQUIREMENTS.md#fr-074).

Cross-cutting controls [NFR-01](../engineering/TRACEABILITY.md#nfr-01), [NFR-02](../engineering/TRACEABILITY.md#nfr-02), [NFR-03](../engineering/TRACEABILITY.md#nfr-03), [NFR-04](../engineering/TRACEABILITY.md#nfr-04), [NFR-05](../engineering/TRACEABILITY.md#nfr-05), [NFR-06](../engineering/TRACEABILITY.md#nfr-06), [NFR-07](../engineering/TRACEABILITY.md#nfr-07), [NFR-08](../engineering/TRACEABILITY.md#nfr-08), [NFR-09](../engineering/TRACEABILITY.md#nfr-09), [NFR-10](../engineering/TRACEABILITY.md#nfr-10), [NFR-11](../engineering/TRACEABILITY.md#nfr-11), [NFR-12](../engineering/TRACEABILITY.md#nfr-12), [NFR-13](../engineering/TRACEABILITY.md#nfr-13), [NFR-14](../engineering/TRACEABILITY.md#nfr-14).
