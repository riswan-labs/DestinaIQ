# Requirements impact proposals

All proposals remain **Pending owner approval**. Review dispositions below record research recommendations only. Formal specification changes require separate owner approval. Priority and complexity are research estimates and carry no release authorization. No FR, NFR, launch capability or checkpoint assignment was changed. Evidence IDs resolve through the [evidence register](EVIDENCE_REGISTER.tsv).

## F01

- Evidence — TI02,TI04,TI05,TI06,TI07,TI11,TI15.
- Requirements — [FR-001](../../product/REQUIREMENTS.md#fr-001), [FR-002](../../product/REQUIREMENTS.md#fr-002), [FR-003](../../product/REQUIREMENTS.md#fr-003), [FR-004](../../product/REQUIREMENTS.md#fr-004), [FR-005](../../product/REQUIREMENTS.md#fr-005), [FR-006](../../product/REQUIREMENTS.md#fr-006), [FR-023](../../product/REQUIREMENTS.md#fr-023), [FR-024](../../product/REQUIREMENTS.md#fr-024). [NFR-03](../../engineering/TRACEABILITY.md#nfr-03), [NFR-04](../../engineering/TRACEABILITY.md#nfr-04).
- Launch capabilities — [L01](../../product/LAUNCH_SCOPE.md#l01), [L02](../../product/LAUNCH_SCOPE.md#l02), [L03](../../product/LAUNCH_SCOPE.md#l03), [L04](../../product/LAUNCH_SCOPE.md#l04), [L05](../../product/LAUNCH_SCOPE.md#l05), [L06](../../product/LAUNCH_SCOPE.md#l06).
- Recommendation — Refine existing requirement.
- Customer value hypothesis — Make canonical island and local-month claims auditable with field-level sources, units and historical periods.
- Proposed priority — P0.
- Estimated engineering complexity — Medium.
- Data and operations — Licensed climate normals, aliases and dated source samples.
- Privacy and safety — Missing or stale inputs must be explicit.
- Release implications — V1.0 criteria proposal; target unchanged.
- Decision owner — Project owner.
- Review disposition — Support refining field-level destination and climate provenance in principle.
- Approval — Pending owner approval.

## F02

- Evidence — TI02,TI12,TG01,AU05,WP05,OR01.
- Requirements — [FR-008](../../product/REQUIREMENTS.md#fr-008), [FR-023](../../product/REQUIREMENTS.md#fr-023), [FR-024](../../product/REQUIREMENTS.md#fr-024), [FR-026](../../product/REQUIREMENTS.md#fr-026), [FR-028](../../product/REQUIREMENTS.md#fr-028), [FR-037](../../product/REQUIREMENTS.md#fr-037). [NFR-02](../../engineering/TRACEABILITY.md#nfr-02), [NFR-03](../../engineering/TRACEABILITY.md#nfr-03), [NFR-07](../../engineering/TRACEABILITY.md#nfr-07).
- Launch capabilities — [L02](../../product/LAUNCH_SCOPE.md#l02), [L08](../../product/LAUNCH_SCOPE.md#l08).
- Recommendation — Retain existing requirement.
- Customer value hypothesis — Keep official issuer, timestamp, regional exceptions and correction path visible.
- Proposed priority — P0.
- Estimated engineering complexity — Medium.
- Data and operations — Issuer feeds, validity and REVIEW ownership.
- Privacy and safety — Avoid roll-up masking conflicting evidence. Keep critical claims official and scoped.
- Release implications — V1.0 FR-008 scope retained; FR-037 side-by-side remains V1.3.
- Decision owner — Project owner.
- Review disposition — Retain existing official travel advisory requirements.
- Approval — Pending owner approval.

## F03

- Evidence — TI03,TI11,WP01,WP05.
- Requirements — [FR-007](../../product/REQUIREMENTS.md#fr-007), [FR-012](../../product/REQUIREMENTS.md#fr-012), [FR-013](../../product/REQUIREMENTS.md#fr-013), [FR-042](../../product/REQUIREMENTS.md#fr-042), [FR-075](../../product/REQUIREMENTS.md#fr-075), [FR-076](../../product/REQUIREMENTS.md#fr-076), [FR-077](../../product/REQUIREMENTS.md#fr-077), [FR-078](../../product/REQUIREMENTS.md#fr-078), [FR-079](../../product/REQUIREMENTS.md#fr-079), [FR-080](../../product/REQUIREMENTS.md#fr-080). [NFR-04](../../engineering/TRACEABILITY.md#nfr-04), [NFR-12](../../engineering/TRACEABILITY.md#nfr-12).
- Launch capabilities — [L09](../../product/LAUNCH_SCOPE.md#l09), [L11](../../product/LAUNCH_SCOPE.md#l11), [L12](../../product/LAUNCH_SCOPE.md#l12).
- Recommendation — Require further validation.
- Customer value hypothesis — Check island breadth, verified access and basic dated parking notes across launch markets.
- Proposed priority — P0.
- Estimated engineering complexity — Medium.
- Data and operations — Canonical POI/airport data, parking and transport licenses, country/region source mapping.
- Privacy and safety — Stale or inaccessible parking must never look live; avoid risky diversion.
- Release implications — V1.0 basic notes only; retain V1.3 advanced gates.
- Decision owner — Project owner.
- Review disposition — Carry destination, airport, transportation and parking coverage questions into CP-0.4.
- Approval — Pending owner approval.

## F04

- Evidence — TI04,TI05,TI06,TI07,TI08,TI14,TI16.
- Requirements — [FR-014](../../product/REQUIREMENTS.md#fr-014), [FR-016](../../product/REQUIREMENTS.md#fr-016), [FR-017](../../product/REQUIREMENTS.md#fr-017), [FR-019](../../product/REQUIREMENTS.md#fr-019), [FR-030](../../product/REQUIREMENTS.md#fr-030), [FR-031](../../product/REQUIREMENTS.md#fr-031), [FR-032](../../product/REQUIREMENTS.md#fr-032), [FR-033](../../product/REQUIREMENTS.md#fr-033), [FR-034](../../product/REQUIREMENTS.md#fr-034), [FR-035](../../product/REQUIREMENTS.md#fr-035), [FR-048](../../product/REQUIREMENTS.md#fr-048), [FR-049](../../product/REQUIREMENTS.md#fr-049), [FR-050](../../product/REQUIREMENTS.md#fr-050). [NFR-05](../../engineering/TRACEABILITY.md#nfr-05), [NFR-08](../../engineering/TRACEABILITY.md#nfr-08).
- Launch capabilities — [L07](../../product/LAUNCH_SCOPE.md#l07), [L15](../../product/LAUNCH_SCOPE.md#l15).
- Recommendation — Refine existing requirement.
- Customer value hypothesis — A four-place comparison with shared units, cost ranges, and honest seasonal uncertainty may improve decisions.
- Proposed priority — P1.
- Estimated engineering complexity — Medium.
- Data and operations — Route, opening hours, blossom history, price and FX provenance.
- Privacy and safety — Historical ranges are not predictions; disclose unknowns and safe fallback.
- Release implications — Retain authoritative staged releases; only baseline comparison and basic itinerary at launch.
- Decision owner — Project owner.
- Review disposition — Support consistent comparison units, historical periods and seasonal uncertainty in principle.
- Approval — Pending owner approval.

## F05

- Evidence — TI09,SI02,SI04,WP03,OR02.
- Requirements — [FR-015](../../product/REQUIREMENTS.md#fr-015), [FR-020](../../product/REQUIREMENTS.md#fr-020), [FR-021](../../product/REQUIREMENTS.md#fr-021), [FR-025](../../product/REQUIREMENTS.md#fr-025), [FR-029](../../product/REQUIREMENTS.md#fr-029), [FR-040](../../product/REQUIREMENTS.md#fr-040), [FR-041](../../product/REQUIREMENTS.md#fr-041), [FR-045](../../product/REQUIREMENTS.md#fr-045), [FR-055](../../product/REQUIREMENTS.md#fr-055), [FR-061](../../product/REQUIREMENTS.md#fr-061), [FR-062](../../product/REQUIREMENTS.md#fr-062), [FR-067](../../product/REQUIREMENTS.md#fr-067), [FR-068](../../product/REQUIREMENTS.md#fr-068), [FR-069](../../product/REQUIREMENTS.md#fr-069). [NFR-01](../../engineering/TRACEABILITY.md#nfr-01), [NFR-02](../../engineering/TRACEABILITY.md#nfr-02), [NFR-10](../../engineering/TRACEABILITY.md#nfr-10), [NFR-11](../../engineering/TRACEABILITY.md#nfr-11), [NFR-14](../../engineering/TRACEABILITY.md#nfr-14).
- Launch capabilities — [L13](../../product/LAUNCH_SCOPE.md#l13), [L14](../../product/LAUNCH_SCOPE.md#l14).
- Recommendation — Retain existing requirement.
- Customer value hypothesis — Let travelers activate monitoring and turn it off; avoid blind collection of confirmations or location.
- Proposed priority — P0.
- Estimated engineering complexity — High.
- Data and operations — Consent ledger, offline storage, retention, notification receipts.
- Privacy and safety — No real passport or confirmation in research; minimize future data and require explicit owner gates.
- Release implications — V1.0 save/alerts, V1.1 offline/preference, V1.2 imports. Preserve V3.0 deferrals.
- Decision owner — Project owner.
- Review disposition — Retain monitoring consent and privacy requirements.
- Approval — Pending owner approval.

## F06

- Evidence — TG01,TG02,TG03,TG04,TG05.
- Requirements — [FR-001](../../product/REQUIREMENTS.md#fr-001), [FR-002](../../product/REQUIREMENTS.md#fr-002), [FR-006](../../product/REQUIREMENTS.md#fr-006), [FR-014](../../product/REQUIREMENTS.md#fr-014), [FR-018](../../product/REQUIREMENTS.md#fr-018), [FR-022](../../product/REQUIREMENTS.md#fr-022), [FR-055](../../product/REQUIREMENTS.md#fr-055), [FR-057](../../product/REQUIREMENTS.md#fr-057), [FR-058](../../product/REQUIREMENTS.md#fr-058), [FR-059](../../product/REQUIREMENTS.md#fr-059), [FR-060](../../product/REQUIREMENTS.md#fr-060). [NFR-02](../../engineering/TRACEABILITY.md#nfr-02), [NFR-05](../../engineering/TRACEABILITY.md#nfr-05), [NFR-08](../../engineering/TRACEABILITY.md#nfr-08), [NFR-14](../../engineering/TRACEABILITY.md#nfr-14).
- Launch capabilities — [L01](../../product/LAUNCH_SCOPE.md#l01), [L06](../../product/LAUNCH_SCOPE.md#l06), [L07](../../product/LAUNCH_SCOPE.md#l07).
- Recommendation — Require further validation.
- Customer value hypothesis — Validate risk-preference disclosure and provider credentials before drawing competitive conclusions.
- Proposed priority — P1.
- Estimated engineering complexity — Medium.
- Data and operations — Authorized comparable tier, provider licenses, accessibility fixtures.
- Privacy and safety — Free scan remains incomplete; do not send identity data or infer app parity.
- Release implications — No launch expansion; Q&A and entry defer as assigned.
- Decision owner — Project owner.
- Review disposition — Retain provider verification and personalization as items for further validation.
- Approval — Pending owner approval.

## F07

- Evidence — AU01,AU03,AU04.
- Requirements — [FR-011](../../product/REQUIREMENTS.md#fr-011), [FR-030](../../product/REQUIREMENTS.md#fr-030), [FR-051](../../product/REQUIREMENTS.md#fr-051), [FR-052](../../product/REQUIREMENTS.md#fr-052), [FR-053](../../product/REQUIREMENTS.md#fr-053), [FR-054](../../product/REQUIREMENTS.md#fr-054), [FR-065](../../product/REQUIREMENTS.md#fr-065), [FR-070](../../product/REQUIREMENTS.md#fr-070), [FR-071](../../product/REQUIREMENTS.md#fr-071), [FR-072](../../product/REQUIREMENTS.md#fr-072). [NFR-01](../../engineering/TRACEABILITY.md#nfr-01), [NFR-08](../../engineering/TRACEABILITY.md#nfr-08), [NFR-13](../../engineering/TRACEABILITY.md#nfr-13), [NFR-14](../../engineering/TRACEABILITY.md#nfr-14).
- Launch capabilities — [L10](../../product/LAUNCH_SCOPE.md#l10).
- Recommendation — Defer.
- Customer value hypothesis — Validate whether user-entered costs and media improve trust enough to fund moderation.
- Proposed priority — P2.
- Estimated engineering complexity — High.
- Data and operations — Community rights, provenance, moderation, pricing verification and support.
- Privacy and safety — Avoid redistributing contributor material; location and social data require consent.
- Release implications — Keep creator media and commerce post-launch; preserve separate social authorization.
- Decision owner — Project owner.
- Review disposition — Retain creator content and traveler expenses in their existing post-launch releases.
- Approval — Pending owner approval.

## F08

- Evidence — AU01,AU04,AU05,AU06,AU07.
- Requirements — [FR-003](../../product/REQUIREMENTS.md#fr-003), [FR-008](../../product/REQUIREMENTS.md#fr-008), [FR-011](../../product/REQUIREMENTS.md#fr-011), [FR-016](../../product/REQUIREMENTS.md#fr-016), [FR-017](../../product/REQUIREMENTS.md#fr-017), [FR-022](../../product/REQUIREMENTS.md#fr-022), [FR-037](../../product/REQUIREMENTS.md#fr-037), [FR-042](../../product/REQUIREMENTS.md#fr-042), [FR-064](../../product/REQUIREMENTS.md#fr-064). [NFR-03](../../engineering/TRACEABILITY.md#nfr-03), [NFR-05](../../engineering/TRACEABILITY.md#nfr-05), [NFR-08](../../engineering/TRACEABILITY.md#nfr-08), [NFR-09](../../engineering/TRACEABILITY.md#nfr-09).
- Launch capabilities — [L02](../../product/LAUNCH_SCOPE.md#l02), [L08](../../product/LAUNCH_SCOPE.md#l08), [L10](../../product/LAUNCH_SCOPE.md#l10), [L15](../../product/LAUNCH_SCOPE.md#l15).
- Recommendation — Refine existing requirement.
- Customer value hypothesis — Freshness labels and editable itinerary inputs may build more trust than illustrative fluency.
- Proposed priority — P1.
- Estimated engineering complexity — Medium.
- Data and operations — Independent advisory fixtures, place hours, transit and source retrieval.
- Privacy and safety — Treat AI output as untrusted; no diagnosis or guarantee.
- Release implications — V1.0 basic itinerary stays; fuller questions and comparisons retain existing targets.
- Decision owner — Project owner.
- Review disposition — Support dated information and editable itinerary inputs in principle.
- Approval — Pending owner approval.

## F09

- Evidence — SI01,SI03,SI04,SI05,SI06.
- Requirements — [FR-018](../../product/REQUIREMENTS.md#fr-018), [FR-045](../../product/REQUIREMENTS.md#fr-045), [FR-046](../../product/REQUIREMENTS.md#fr-046), [FR-061](../../product/REQUIREMENTS.md#fr-061), [FR-062](../../product/REQUIREMENTS.md#fr-062), [FR-063](../../product/REQUIREMENTS.md#fr-063), [FR-064](../../product/REQUIREMENTS.md#fr-064), [FR-066](../../product/REQUIREMENTS.md#fr-066), [FR-074](../../product/REQUIREMENTS.md#fr-074). [NFR-01](../../engineering/TRACEABILITY.md#nfr-01), [NFR-02](../../engineering/TRACEABILITY.md#nfr-02), [NFR-11](../../engineering/TRACEABILITY.md#nfr-11), [NFR-13](../../engineering/TRACEABILITY.md#nfr-13), [NFR-14](../../engineering/TRACEABILITY.md#nfr-14).
- Launch capabilities — [L14](../../product/LAUNCH_SCOPE.md#l14).
- Recommendation — Consider partnership.
- Customer value hypothesis — Specialist assistance and insurance may solve urgent cases without building claims operations.
- Proposed priority — P2.
- Estimated engineering complexity — High.
- Data and operations — Partner due diligence, coverage contracts, regulated services and support economics.
- Privacy and safety — Consent, eligibility, escalation and regional rules require specialist review.
- Release implications — No V1.0 insurance or assistance expansion; authorization for later partners.
- Decision owner — Project owner.
- Review disposition — Evaluate specialist insurance and assistance partnerships at their designated future checkpoints.
- Approval — Pending owner approval.

## F10

- Evidence — SI02,SI03,SI06.
- Requirements — [FR-020](../../product/REQUIREMENTS.md#fr-020), [FR-025](../../product/REQUIREMENTS.md#fr-025), [FR-027](../../product/REQUIREMENTS.md#fr-027), [FR-039](../../product/REQUIREMENTS.md#fr-039), [FR-040](../../product/REQUIREMENTS.md#fr-040), [FR-041](../../product/REQUIREMENTS.md#fr-041), [FR-045](../../product/REQUIREMENTS.md#fr-045), [FR-046](../../product/REQUIREMENTS.md#fr-046), [FR-047](../../product/REQUIREMENTS.md#fr-047), [FR-049](../../product/REQUIREMENTS.md#fr-049), [FR-050](../../product/REQUIREMENTS.md#fr-050), [FR-074](../../product/REQUIREMENTS.md#fr-074). [NFR-02](../../engineering/TRACEABILITY.md#nfr-02), [NFR-06](../../engineering/TRACEABILITY.md#nfr-06), [NFR-07](../../engineering/TRACEABILITY.md#nfr-07), [NFR-10](../../engineering/TRACEABILITY.md#nfr-10), [NFR-11](../../engineering/TRACEABILITY.md#nfr-11).
- Launch capabilities — [L13](../../product/LAUNCH_SCOPE.md#l13), [L14](../../product/LAUNCH_SCOPE.md#l14).
- Recommendation — Require further validation.
- Customer value hypothesis — Measure whether a verified multi-leg impact graph changes decisions beyond alerting.
- Proposed priority — P1.
- Estimated engineering complexity — High.
- Data and operations — Licensed flight data, event matching, lodging and activity dependencies.
- Privacy and safety — No autonomous booking actions; avoid alert fatigue and log approvals.
- Release implications — Preserve V1.2 connected planning and later assistance; no live disruption claim.
- Decision owner — Project owner.
- Review disposition — Retain Digital Twin and cascading disruption intelligence as unvalidated differentiation hypotheses.
- Approval — Pending owner approval.

## F11

- Evidence — WP01,WP02,WP03,WP04,WP05.
- Requirements — [FR-007](../../product/REQUIREMENTS.md#fr-007), [FR-020](../../product/REQUIREMENTS.md#fr-020), [FR-021](../../product/REQUIREMENTS.md#fr-021), [FR-037](../../product/REQUIREMENTS.md#fr-037), [FR-039](../../product/REQUIREMENTS.md#fr-039), [FR-040](../../product/REQUIREMENTS.md#fr-040), [FR-041](../../product/REQUIREMENTS.md#fr-041), [FR-056](../../product/REQUIREMENTS.md#fr-056), [FR-060](../../product/REQUIREMENTS.md#fr-060), [FR-066](../../product/REQUIREMENTS.md#fr-066), [FR-073](../../product/REQUIREMENTS.md#fr-073). [NFR-03](../../engineering/TRACEABILITY.md#nfr-03), [NFR-06](../../engineering/TRACEABILITY.md#nfr-06), [NFR-07](../../engineering/TRACEABILITY.md#nfr-07), [NFR-10](../../engineering/TRACEABILITY.md#nfr-10), [NFR-13](../../engineering/TRACEABILITY.md#nfr-13).
- Launch capabilities — [L09](../../product/LAUNCH_SCOPE.md#l09), [L14](../../product/LAUNCH_SCOPE.md#l14).
- Recommendation — Require further validation.
- Customer value hypothesis — Test if a bounded trip pass or weekly alerts cover customer needs before funding daily monitoring.
- Proposed priority — P1.
- Estimated engineering complexity — Medium.
- Data and operations — Licensed data, availability, cost per monitored trip, explicit permission for competitive output tests.
- Privacy and safety — Scope and cadence controls and source corrections needed; vendor price is not cost evidence.
- Release implications — No change to pricing or releases; validate at CP-0.3, CP-0.4 and CP-11.11.
- Decision owner — Project owner.
- Review disposition — Carry pricing and monitoring economics into CP-0.3 and CP-0.4.
- Approval — Pending owner approval.

## F12

- Evidence — OR01,OR02,OR04,OR05,OR06.
- Requirements — [FR-009](../../product/REQUIREMENTS.md#fr-009), [FR-010](../../product/REQUIREMENTS.md#fr-010), [FR-013](../../product/REQUIREMENTS.md#fr-013), [FR-036](../../product/REQUIREMENTS.md#fr-036), [FR-038](../../product/REQUIREMENTS.md#fr-038), [FR-042](../../product/REQUIREMENTS.md#fr-042), [FR-043](../../product/REQUIREMENTS.md#fr-043), [FR-044](../../product/REQUIREMENTS.md#fr-044), [FR-054](../../product/REQUIREMENTS.md#fr-054), [FR-075](../../product/REQUIREMENTS.md#fr-075), [FR-079](../../product/REQUIREMENTS.md#fr-079), [FR-080](../../product/REQUIREMENTS.md#fr-080). [NFR-02](../../engineering/TRACEABILITY.md#nfr-02), [NFR-03](../../engineering/TRACEABILITY.md#nfr-03), [NFR-12](../../engineering/TRACEABILITY.md#nfr-12).
- Launch capabilities — [L11](../../product/LAUNCH_SCOPE.md#l11), [L12](../../product/LAUNCH_SCOPE.md#l12).
- Recommendation — Defer.
- Customer value hypothesis — Local evidence can improve hotel and itinerary decisions if geographic precision is defensible.
- Proposed priority — P2.
- Estimated engineering complexity — High.
- Data and operations — Geocoded incidents, source timestamps, licensed boundaries, parking recency.
- Privacy and safety — Do not convert zero observed incidents or demographics into safety claims.
- Release implications — Keep hyperlocal and advanced parking in V1.3. Keep launch essentials sourced.
- Decision owner — Project owner.
- Review disposition — Retain hyperlocal safety and advanced parking within existing V1.3 scope.
- Approval — Pending owner approval.

## F13

- Evidence — TI04,TI09,AU05,SI04,WP03,OR02.
- Requirements — [FR-023](../../product/REQUIREMENTS.md#fr-023), [FR-024](../../product/REQUIREMENTS.md#fr-024), [FR-026](../../product/REQUIREMENTS.md#fr-026), [FR-028](../../product/REQUIREMENTS.md#fr-028), [FR-029](../../product/REQUIREMENTS.md#fr-029), [FR-038](../../product/REQUIREMENTS.md#fr-038), [FR-066](../../product/REQUIREMENTS.md#fr-066). [NFR-02](../../engineering/TRACEABILITY.md#nfr-02), [NFR-03](../../engineering/TRACEABILITY.md#nfr-03), [NFR-04](../../engineering/TRACEABILITY.md#nfr-04), [NFR-07](../../engineering/TRACEABILITY.md#nfr-07), [NFR-09](../../engineering/TRACEABILITY.md#nfr-09), [NFR-13](../../engineering/TRACEABILITY.md#nfr-13).
- Launch capabilities — [L02](../../product/LAUNCH_SCOPE.md#l02), [L08](../../product/LAUNCH_SCOPE.md#l08), [L09](../../product/LAUNCH_SCOPE.md#l09).
- Recommendation — Refine existing requirement.
- Customer value hypothesis — Evaluate visible correction history and links to affected evidence within the existing provenance and correction scope.
- Proposed priority — P2.
- Estimated engineering complexity — Medium.
- Data and operations — Temporal version store, audit policy, editorial workflow, operating ownership.
- Privacy and safety — Avoid leaking trip-linked context and stale or retracted safety claims.
- Release implications — No new FR created; defer release assignment until customer tests and architectural review.
- Decision owner — Project owner.
- Review disposition — Evaluate visible correction history as a possible refinement of existing provenance and correction requirements.
- Approval — Pending owner approval.

## Registry coverage

Material findings reference all 80 FRs, all 14 NFRs and all 15 launch capabilities. A reference identifies the scope considered, including recommendations to keep current requirements and defer later work.
