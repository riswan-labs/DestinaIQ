# Functional requirements

Design V3 [section 21](DESIGN.md#21-requirement-acceptance-register) supplies the 80 stable IDs, release assignments and minimum acceptance tests. Descriptions specify intended behavior. Checkpoints, primary domain ownership, prerequisite mappings, verification fixtures and priorities labeled proposed are Checkpoint 0.1 planning assignments. All planned tests are pending. Status is **Not Started** for every implementation item.

Dependencies identify upstream interfaces or coordinated prerequisites. Within a checkpoint, implementation can proceed in dependency order. The release gate requires positive, negative and failure-path coverage and applicable security, documentation and telemetry evidence.

## FR-001

**Search destinations**

Return ranked canonical geographic matches for exact names and aliases.

- Domain and priority — Destination IQ, P0 (proposed)
- Target release and gate — [Gate V1.0](../product/RELEASE_STRATEGY.md#gate-v10)
- Implementation phase and checkpoint — Phase 4, [CP-4.1](../engineering/ROADMAP.md#cp-41)
- Dependencies — [CP-2.1](../engineering/ROADMAP.md#cp-21)
- Acceptance criterion — Search exact and alias fixtures; ≥95% top-5 recall on curated set.
- Verification — Pending automated verification with curated exact names and aliases. Test reference TEST-FR-001.
- Traceability — [L01](../product/LAUNCH_SCOPE.md#l01). Controls [NFR-06](../engineering/TRACEABILITY.md#nfr-06), [NFR-08](../engineering/TRACEABILITY.md#nfr-08), [NFR-09](../engineering/TRACEABILITY.md#nfr-09).
- Status — Not Started

## FR-002

**Resolve aliases and ambiguous names**

Disambiguate shared place names using regional context.

- Domain and priority — Destination IQ, P0 (proposed)
- Target release and gate — [Gate V1.0](../product/RELEASE_STRATEGY.md#gate-v10)
- Implementation phase and checkpoint — Phase 4, [CP-4.1](../engineering/ROADMAP.md#cp-41)
- Dependencies — [FR-001](#fr-001)
- Acceptance criterion — Ambiguous names return distinct candidates with region labels; no silent selection.
- Verification — Pending automated verification with ambiguous name fixtures. Test reference TEST-FR-002.
- Traceability — [L01](../product/LAUNCH_SCOPE.md#l01). Controls [NFR-08](../engineering/TRACEABILITY.md#nfr-08), [NFR-09](../engineering/TRACEABILITY.md#nfr-09).
- Status — Not Started

## FR-003

**Structured destination profiles**

Publish a structured source-backed profile including weather forecast, freshness and supported fields.

- Domain and priority — Destination IQ, P0 (proposed)
- Target release and gate — [Gate V1.0](../product/RELEASE_STRATEGY.md#gate-v10)
- Implementation phase and checkpoint — Phase 4, [CP-4.1](../engineering/ROADMAP.md#cp-41)
- Dependencies — [CP-3.1](../engineering/ROADMAP.md#cp-31), [CP-3.2](../engineering/ROADMAP.md#cp-32), [CP-3.3](../engineering/ROADMAP.md#cp-33), [FR-023](#fr-023), [FR-024](#fr-024)
- Acceptance criterion — Profile displays source-backed required fields and forecast timestamp; expired forecast marked stale or withheld.
- Verification — Pending automated verification with required-field and forecast expiry fixtures. Test reference TEST-FR-003.
- Traceability — [L02](../product/LAUNCH_SCOPE.md#l02), [L04](../product/LAUNCH_SCOPE.md#l04). Controls [NFR-03](../engineering/TRACEABILITY.md#nfr-03), [NFR-04](../engineering/TRACEABILITY.md#nfr-04), [NFR-06](../engineering/TRACEABILITY.md#nfr-06), [NFR-07](../engineering/TRACEABILITY.md#nfr-07), [NFR-08](../engineering/TRACEABILITY.md#nfr-08), [NFR-09](../engineering/TRACEABILITY.md#nfr-09).
- Status — Not Started

## FR-004

**Monthly climate statistics**

Expose monthly historical climate normals with units and reference periods.

- Domain and priority — Season IQ, P0 (proposed)
- Target release and gate — [Gate V1.0](../product/RELEASE_STRATEGY.md#gate-v10)
- Implementation phase and checkpoint — Phase 3, [CP-3.1](../engineering/ROADMAP.md#cp-31)
- Dependencies — [CP-2.1](../engineering/ROADMAP.md#cp-21), [FR-023](#fr-023)
- Acceptance criterion — All 12 months show units and reference period or explicit missing status.
- Verification — Pending automated verification with monthly normals and missing month fixtures. Test reference TEST-FR-004.
- Traceability — [L03](../product/LAUNCH_SCOPE.md#l03). Controls [NFR-03](../engineering/TRACEABILITY.md#nfr-03), [NFR-04](../engineering/TRACEABILITY.md#nfr-04), [NFR-09](../engineering/TRACEABILITY.md#nfr-09).
- Status — Not Started

## FR-005

**Peak, shoulder and low seasons**

Classify tourism periods using documented demand evidence.

- Domain and priority — Season IQ, P0 (proposed)
- Target release and gate — [Gate V1.0](../product/RELEASE_STRATEGY.md#gate-v10)
- Implementation phase and checkpoint — Phase 3, [CP-3.1](../engineering/ROADMAP.md#cp-31)
- Dependencies — [FR-004](#fr-004), [FR-023](#fr-023)
- Acceptance criterion — Season labels include evidence and rationale; unsupported months unknown.
- Verification — Pending automated verification with tourism demand and season evidence fixtures. Test reference TEST-FR-005.
- Traceability — [L05](../product/LAUNCH_SCOPE.md#l05). Controls [NFR-03](../engineering/TRACEABILITY.md#nfr-03), [NFR-09](../engineering/TRACEABILITY.md#nfr-09).
- Status — Not Started

## FR-006

**Personalized travel windows**

Rank travel windows using the traveler’s month and preferences and explain trade-offs.

- Domain and priority — Season IQ, P0 (proposed)
- Target release and gate — [Gate V1.0](../product/RELEASE_STRATEGY.md#gate-v10)
- Implementation phase and checkpoint — Phase 4, [CP-4.1](../engineering/ROADMAP.md#cp-41)
- Dependencies — [FR-004](#fr-004), [FR-005](#fr-005), [FR-008](#fr-008)
- Acceptance criterion — Changing month or preference changes ranking on deterministic fixture; explain trade-offs.
- Verification — Pending automated verification with deterministic preference and month perturbation. Test reference TEST-FR-006.
- Traceability — [L06](../product/LAUNCH_SCOPE.md#l06). Controls [NFR-03](../engineering/TRACEABILITY.md#nfr-03), [NFR-05](../engineering/TRACEABILITY.md#nfr-05), [NFR-09](../engineering/TRACEABILITY.md#nfr-09), [NFR-13](../engineering/TRACEABILITY.md#nfr-13).
- Status — Not Started

## FR-007

**Relevant news and events**

Show verified geographically relevant news and deduplicated travel events.

- Domain and priority — Pulse IQ, P0 (proposed)
- Target release and gate — [Gate V1.0](../product/RELEASE_STRATEGY.md#gate-v10)
- Implementation phase and checkpoint — Phase 3, [CP-3.2](../engineering/ROADMAP.md#cp-32)
- Dependencies — [CP-2.1](../engineering/ROADMAP.md#cp-21), [FR-023](#fr-023), [FR-024](#fr-024)
- Acceptance criterion — Duplicate articles cluster into one event; unrelated geography excluded.
- Verification — Pending automated verification with duplicate articles and disjoint geographic fixtures. Test reference TEST-FR-007.
- Traceability — [L09](../product/LAUNCH_SCOPE.md#l09). Controls [NFR-03](../engineering/TRACEABILITY.md#nfr-03), [NFR-04](../engineering/TRACEABILITY.md#nfr-04), [NFR-07](../engineering/TRACEABILITY.md#nfr-07), [NFR-09](../engineering/TRACEABILITY.md#nfr-09).
- Status — Not Started

## FR-008

**Multi-government advisories**

Publish authoritative advisories by issuing government and validity period.

- Domain and priority — Safety IQ, P0 (proposed)
- Target release and gate — [Gate V1.0](../product/RELEASE_STRATEGY.md#gate-v10)
- Implementation phase and checkpoint — Phase 3, [CP-3.2](../engineering/ROADMAP.md#cp-32)
- Dependencies — [CP-2.1](../engineering/ROADMAP.md#cp-21), [FR-023](#fr-023), [FR-024](#fr-024)
- Acceptance criterion — Show issuer, source and dates; conflicting advisories separate; expired critical claims withheld.
- Verification — Pending automated verification with conflicting issuer and expired advisory fixtures. Test reference TEST-FR-008.
- Traceability — [L08](../product/LAUNCH_SCOPE.md#l08). Controls [NFR-03](../engineering/TRACEABILITY.md#nfr-03), [NFR-04](../engineering/TRACEABILITY.md#nfr-04), [NFR-07](../engineering/TRACEABILITY.md#nfr-07), [NFR-09](../engineering/TRACEABILITY.md#nfr-09), [NFR-13](../engineering/TRACEABILITY.md#nfr-13).
- Status — Not Started

## FR-009

**Contextual crime statistics**

Provide contextual local crime statistics with comparable methodology only.

- Domain and priority — Safety IQ, P1 (proposed)
- Target release and gate — [Gate V1.3](../product/RELEASE_STRATEGY.md#gate-v13)
- Implementation phase and checkpoint — Phase 9, [CP-9.1](../engineering/ROADMAP.md#cp-91)
- Dependencies — [CP-2.1](../engineering/ROADMAP.md#cp-21), [FR-023](#fr-023)
- Acceptance criterion — Crime figures retain period, denominator and methodology; incomparable data not ranked.
- Verification — Pending automated verification with incomparable crime methodologies. Test reference TEST-FR-009.
- Traceability — Post-launch. Controls [NFR-03](../engineering/TRACEABILITY.md#nfr-03), [NFR-09](../engineering/TRACEABILITY.md#nfr-09), [NFR-12](../engineering/TRACEABILITY.md#nfr-12).
- Status — Not Started

## FR-010

**Safety and scam guidance**

Publish sourced local scam and safety guidance.

- Domain and priority — Safety IQ, P1 (proposed)
- Target release and gate — [Gate V1.3](../product/RELEASE_STRATEGY.md#gate-v13)
- Implementation phase and checkpoint — Phase 9, [CP-9.1](../engineering/ROADMAP.md#cp-91)
- Dependencies — [FR-009](#fr-009), [FR-023](#fr-023)
- Acceptance criterion — Scam guidance cites local evidence; unsupported claims return unknown.
- Verification — Pending automated verification with local scam evidence and unknown coverage. Test reference TEST-FR-010.
- Traceability — Post-launch. Controls [NFR-03](../engineering/TRACEABILITY.md#nfr-03), [NFR-09](../engineering/TRACEABILITY.md#nfr-09), [NFR-12](../engineering/TRACEABILITY.md#nfr-12).
- Status — Not Started

## FR-011

**Attractions and experiences**

List canonically located attractions and experiences with sourced visiting information.

- Domain and priority — Experience IQ, P0 (proposed)
- Target release and gate — [Gate V1.0](../product/RELEASE_STRATEGY.md#gate-v10)
- Implementation phase and checkpoint — Phase 3, [CP-3.3](../engineering/ROADMAP.md#cp-33)
- Dependencies — [CP-2.1](../engineering/ROADMAP.md#cp-21), [FR-023](#fr-023)
- Acceptance criterion — Attractions show canonical location and source; unknown hours labeled.
- Verification — Pending automated verification with canonical POI and unknown hours fixtures. Test reference TEST-FR-011.
- Traceability — [L10](../product/LAUNCH_SCOPE.md#l10). Controls [NFR-03](../engineering/TRACEABILITY.md#nfr-03), [NFR-04](../engineering/TRACEABILITY.md#nfr-04), [NFR-09](../engineering/TRACEABILITY.md#nfr-09).
- Status — Not Started

## FR-012

**Airport gateways**

Identify airport gateways serving a destination and their codes.

- Domain and priority — Transit IQ, P0 (proposed)
- Target release and gate — [Gate V1.0](../product/RELEASE_STRATEGY.md#gate-v10)
- Implementation phase and checkpoint — Phase 3, [CP-3.3](../engineering/ROADMAP.md#cp-33)
- Dependencies — [CP-2.1](../engineering/ROADMAP.md#cp-21), [FR-023](#fr-023)
- Acceptance criterion — Airport codes resolve to correct gateways on fixture; distinguish serving vs located in.
- Verification — Pending automated verification with airport location versus service area fixtures. Test reference TEST-FR-012.
- Traceability — [L11](../product/LAUNCH_SCOPE.md#l11). Controls [NFR-03](../engineering/TRACEABILITY.md#nfr-03), [NFR-04](../engineering/TRACEABILITY.md#nfr-04), [NFR-09](../engineering/TRACEABILITY.md#nfr-09).
- Status — Not Started

## FR-013

**Transport connections**

Present sourced connections and basic parking guidance where available.

- Domain and priority — Transit IQ, P0 (proposed)
- Target release and gate — [Gate V1.0](../product/RELEASE_STRATEGY.md#gate-v10)
- Implementation phase and checkpoint — Phase 3, [CP-3.3](../engineering/ROADMAP.md#cp-33)
- Dependencies — [FR-012](#fr-012), [FR-023](#fr-023)
- Acceptance criterion — Transport modes and sourced parking notes shown; unknown fares/times labeled.
- Verification — Pending automated verification with route modes, parking notes and absent fares. Test reference TEST-FR-013.
- Traceability — [L11](../product/LAUNCH_SCOPE.md#l11). Controls [NFR-03](../engineering/TRACEABILITY.md#nfr-03), [NFR-04](../engineering/TRACEABILITY.md#nfr-04), [NFR-09](../engineering/TRACEABILITY.md#nfr-09).
- Status — Not Started

## FR-014

**Destination comparisons**

Compare destinations across shared dates, weather, crowds, cost evidence and traveler preferences.

- Domain and priority — Budget IQ, P0 (proposed)
- Target release and gate — [Gate V1.0](../product/RELEASE_STRATEGY.md#gate-v10)
- Implementation phase and checkpoint — Phase 4, [CP-4.1](../engineering/ROADMAP.md#cp-41)
- Dependencies — [FR-003](#fr-003), [FR-004](#fr-004), [FR-005](#fr-005), [FR-008](#fr-008)
- Acceptance criterion — Compare 2–4 destinations with common units and missing values; reject fifth.
- Verification — Pending automated verification with two through five comparison inputs. Test reference TEST-FR-014.
- Traceability — [L07](../product/LAUNCH_SCOPE.md#l07). Controls [NFR-03](../engineering/TRACEABILITY.md#nfr-03), [NFR-08](../engineering/TRACEABILITY.md#nfr-08), [NFR-09](../engineering/TRACEABILITY.md#nfr-09).
- Status — Not Started

## FR-015

**Saved destinations and dates**

Save, edit and delete destination and trip dates for the authenticated owner.

- Domain and priority — Plan IQ, P0 (proposed)
- Target release and gate — [Gate V1.0](../product/RELEASE_STRATEGY.md#gate-v10)
- Implementation phase and checkpoint — Phase 4, [CP-4.2](../engineering/ROADMAP.md#cp-42)
- Dependencies — [FR-001](#fr-001), [CP-1.1](../engineering/ROADMAP.md#cp-11)
- Acceptance criterion — Save/edit/delete dates; cross-user access denied.
- Verification — Pending automated verification with two identities and trip lifecycle. Test reference TEST-FR-015.
- Traceability — [L13](../product/LAUNCH_SCOPE.md#l13). Controls [NFR-01](../engineering/TRACEABILITY.md#nfr-01), [NFR-02](../engineering/TRACEABILITY.md#nfr-02), [NFR-08](../engineering/TRACEABILITY.md#nfr-08), [NFR-09](../engineering/TRACEABILITY.md#nfr-09).
- Status — Not Started

## FR-016

**Personalized itineraries**

Generate editable grounded itineraries validated against known travel constraints.

- Domain and priority — Plan IQ, P0 (proposed)
- Target release and gate — [Gate V1.0](../product/RELEASE_STRATEGY.md#gate-v10)
- Implementation phase and checkpoint — Phase 5, [CP-5.1](../engineering/ROADMAP.md#cp-51)
- Dependencies — [FR-011](#fr-011), [FR-013](#fr-013), [FR-015](#fr-015), [FR-023](#fr-023)
- Acceptance criterion — Generate editable itinerary; reject known closed hours and impossible transfers; unknowns flagged.
- Verification — Pending automated verification with closed venues, transfer time and unknowns. Test reference TEST-FR-016.
- Traceability — [L15](../product/LAUNCH_SCOPE.md#l15). Controls [NFR-02](../engineering/TRACEABILITY.md#nfr-02), [NFR-03](../engineering/TRACEABILITY.md#nfr-03), [NFR-05](../engineering/TRACEABILITY.md#nfr-05), [NFR-06](../engineering/TRACEABILITY.md#nfr-06), [NFR-08](../engineering/TRACEABILITY.md#nfr-08), [NFR-09](../engineering/TRACEABILITY.md#nfr-09).
- Status — Not Started

## FR-017

**Packing checklists**

Generate an editable packing checklist from trip conditions.

- Domain and priority — Ready IQ, P1 (proposed)
- Target release and gate — [Gate V1.1](../product/RELEASE_STRATEGY.md#gate-v11)
- Implementation phase and checkpoint — Phase 7, [CP-7.2](../engineering/ROADMAP.md#cp-72)
- Dependencies — [FR-015](#fr-015), [FR-004](#fr-004)
- Acceptance criterion — Packing changes with trip conditions; user can edit and check items.
- Verification — Pending automated verification with condition-driven checklist edit flow. Test reference TEST-FR-017.
- Traceability — Post-launch. Controls [NFR-09](../engineering/TRACEABILITY.md#nfr-09).
- Status — Not Started

## FR-018

**Nationality-specific entry guidance**

Present official entry guidance appropriate to traveler nationality, transit and dates.

- Domain and priority — Ready IQ, P1 (proposed)
- Target release and gate — [Gate V1.1](../product/RELEASE_STRATEGY.md#gate-v11)
- Implementation phase and checkpoint — Phase 7, [CP-7.2](../engineering/ROADMAP.md#cp-72)
- Dependencies — [CP-2.1](../engineering/ROADMAP.md#cp-21), [FR-023](#fr-023), [FR-024](#fr-024)
- Acceptance criterion — Entry result uses nationality, transit and dates; source and validity shown; unknown if unsupported.
- Verification — Pending automated verification with nationality, transit and validity matrix. Test reference TEST-FR-018.
- Traceability — Post-launch. Controls [NFR-03](../engineering/TRACEABILITY.md#nfr-03), [NFR-05](../engineering/TRACEABILITY.md#nfr-05), [NFR-09](../engineering/TRACEABILITY.md#nfr-09).
- Status — Not Started

## FR-019

**Budget estimates**

Estimate a trip budget range using trip and occupancy assumptions.

- Domain and priority — Budget IQ, P1 (proposed)
- Target release and gate — [Gate V1.1](../product/RELEASE_STRATEGY.md#gate-v11)
- Implementation phase and checkpoint — Phase 7, [CP-7.2](../engineering/ROADMAP.md#cp-72)
- Dependencies — [FR-015](#fr-015), [FR-023](#fr-023)
- Acceptance criterion — Budget shows currency, dates, occupancy and range; no quote implied.
- Verification — Pending automated verification with currency, occupancy and date ranges. Test reference TEST-FR-019.
- Traceability — Post-launch. Controls [NFR-09](../engineering/TRACEABILITY.md#nfr-09), [NFR-13](../engineering/TRACEABILITY.md#nfr-13).
- Status — Not Started

## FR-020

**Relevant notifications**

Notify travelers of verified urgent events relevant to opted-in trips.

- Domain and priority — Pulse IQ, P0 (proposed)
- Target release and gate — [Gate V1.0](../product/RELEASE_STRATEGY.md#gate-v10)
- Implementation phase and checkpoint — Phase 5, [CP-5.2](../engineering/ROADMAP.md#cp-52)
- Dependencies — [FR-015](#fr-015), [FR-040](#fr-040), [FR-041](#fr-041)
- Acceptance criterion — Verified relevant urgent event triggers one alert per trip/version; irrelevant event suppressed.
- Verification — Pending automated verification with verified event replay and irrelevant control. Test reference TEST-FR-020.
- Traceability — [L14](../product/LAUNCH_SCOPE.md#l14). Controls [NFR-06](../engineering/TRACEABILITY.md#nfr-06), [NFR-07](../engineering/TRACEABILITY.md#nfr-07), [NFR-09](../engineering/TRACEABILITY.md#nfr-09), [NFR-10](../engineering/TRACEABILITY.md#nfr-10), [NFR-13](../engineering/TRACEABILITY.md#nfr-13).
- Status — Not Started

## FR-021

**Weekly briefings**

Send opted-in weekly intelligence summaries during the monitoring window.

- Domain and priority — Pulse IQ, P0 (proposed)
- Target release and gate — [Gate V1.0](../product/RELEASE_STRATEGY.md#gate-v10)
- Implementation phase and checkpoint — Phase 5, [CP-5.2](../engineering/ROADMAP.md#cp-52)
- Dependencies — [FR-015](#fr-015), [FR-040](#fr-040), [FR-041](#fr-041)
- Acceptance criterion — Weekly digest sent once per opted-in trip/week; stops after return.
- Verification — Pending automated verification with opt-in schedule and returned trip clock. Test reference TEST-FR-021.
- Traceability — [L14](../product/LAUNCH_SCOPE.md#l14). Controls [NFR-06](../engineering/TRACEABILITY.md#nfr-06), [NFR-07](../engineering/TRACEABILITY.md#nfr-07), [NFR-09](../engineering/TRACEABILITY.md#nfr-09), [NFR-10](../engineering/TRACEABILITY.md#nfr-10), [NFR-13](../engineering/TRACEABILITY.md#nfr-13).
- Status — Not Started

## FR-022

**Natural-language questions**

Answer destination questions using trusted evidence and abstain when necessary.

- Domain and priority — Plan IQ, P1 (proposed)
- Target release and gate — [Gate V1.1](../product/RELEASE_STRATEGY.md#gate-v11)
- Implementation phase and checkpoint — Phase 7, [CP-7.2](../engineering/ROADMAP.md#cp-72)
- Dependencies — [FR-023](#fr-023), [FR-024](#fr-024), [CP-5.1](../engineering/ROADMAP.md#cp-51)
- Acceptance criterion — Answers cite retrieved evidence; unsupported critical query abstains.
- Verification — Pending automated verification with grounded responses and abstention. Test reference TEST-FR-022.
- Traceability — Post-launch. Controls [NFR-02](../engineering/TRACEABILITY.md#nfr-02), [NFR-03](../engineering/TRACEABILITY.md#nfr-03), [NFR-05](../engineering/TRACEABILITY.md#nfr-05), [NFR-06](../engineering/TRACEABILITY.md#nfr-06), [NFR-09](../engineering/TRACEABILITY.md#nfr-09).
- Status — Not Started

## FR-023

**Sources and timestamps**

Attach provenance and timestamps to published destination assertions.

- Domain and priority — Trust IQ, P0 (proposed)
- Target release and gate — [Gate V1.0](../product/RELEASE_STRATEGY.md#gate-v10)
- Implementation phase and checkpoint — Phase 2, [CP-2.1](../engineering/ROADMAP.md#cp-21)
- Dependencies — [CP-1.1](../engineering/ROADMAP.md#cp-11)
- Acceptance criterion — Every critical claim has source ID and timestamp; missing evidence blocks publication.
- Verification — Pending automated verification with fact publication with and without evidence. Test reference TEST-FR-023.
- Traceability — [L02](../product/LAUNCH_SCOPE.md#l02). Controls [NFR-03](../engineering/TRACEABILITY.md#nfr-03), [NFR-04](../engineering/TRACEABILITY.md#nfr-04), [NFR-07](../engineering/TRACEABILITY.md#nfr-07), [NFR-09](../engineering/TRACEABILITY.md#nfr-09).
- Status — Not Started

## FR-024

**Stale/conflicting information detection**

Detect conflicting or stale facts and govern serving based on evidence validity.

- Domain and priority — Trust IQ, P0 (proposed)
- Target release and gate — [Gate V1.0](../product/RELEASE_STRATEGY.md#gate-v10)
- Implementation phase and checkpoint — Phase 2, [CP-2.1](../engineering/ROADMAP.md#cp-21)
- Dependencies — [FR-023](#fr-023)
- Acceptance criterion — Stale/conflicting fixtures visibly labeled; critical expired facts suppressed.
- Verification — Pending automated verification with stale, expired and conflicting version fixtures. Test reference TEST-FR-024.
- Traceability — [L02](../product/LAUNCH_SCOPE.md#l02). Controls [NFR-03](../engineering/TRACEABILITY.md#nfr-03), [NFR-04](../engineering/TRACEABILITY.md#nfr-04), [NFR-07](../engineering/TRACEABILITY.md#nfr-07), [NFR-09](../engineering/TRACEABILITY.md#nfr-09).
- Status — Not Started

## FR-025

**Offline trip summaries**

Make a trip summary available offline with its freshness visible.

- Domain and priority — Plan IQ, P1 (proposed)
- Target release and gate — [Gate V1.1](../product/RELEASE_STRATEGY.md#gate-v11)
- Implementation phase and checkpoint — Phase 7, [CP-7.2](../engineering/ROADMAP.md#cp-72)
- Dependencies — [FR-015](#fr-015), [FR-023](#fr-023)
- Acceptance criterion — Offline summary opens without network and shows last sync date.
- Verification — Pending automated verification with network-disabled trip view. Test reference TEST-FR-025.
- Traceability — Post-launch. Controls [NFR-08](../engineering/TRACEABILITY.md#nfr-08), [NFR-09](../engineering/TRACEABILITY.md#nfr-09).
- Status — Not Started

## FR-026

**Accuracy reporting**

Accept accuracy reports and route them into an auditable review process.

- Domain and priority — Trust IQ, P0 (proposed)
- Target release and gate — [Gate V1.0](../product/RELEASE_STRATEGY.md#gate-v10)
- Implementation phase and checkpoint — Phase 4, [CP-4.2](../engineering/ROADMAP.md#cp-42)
- Dependencies — [FR-003](#fr-003), [FR-028](#fr-028)
- Acceptance criterion — Report creates tracked review item; reporter receives reference.
- Verification — Pending automated verification with accuracy report reference and review queue. Test reference TEST-FR-026.
- Traceability — [Launch controls](LAUNCH_SCOPE.md#launch-controls). Controls [NFR-01](../engineering/TRACEABILITY.md#nfr-01), [NFR-02](../engineering/TRACEABILITY.md#nfr-02), [NFR-09](../engineering/TRACEABILITY.md#nfr-09).
- Status — Not Started

## FR-027

**Adaptive itineraries**

Propose itinerary changes in response to disruptions while preserving confirmed bookings.

- Domain and priority — Plan IQ, P1 (proposed)
- Target release and gate — [Gate V1.2](../product/RELEASE_STRATEGY.md#gate-v12)
- Implementation phase and checkpoint — Phase 8, [CP-8.2](../engineering/ROADMAP.md#cp-82)
- Dependencies — [FR-016](#fr-016), [FR-047](#fr-047)
- Acceptance criterion — Disruption proposes alternatives without modifying bookings.
- Verification — Pending automated verification with disruption replay and booking mutation guard. Test reference TEST-FR-027.
- Traceability — Post-launch. Controls [NFR-05](../engineering/TRACEABILITY.md#nfr-05), [NFR-09](../engineering/TRACEABILITY.md#nfr-09), [NFR-14](../engineering/TRACEABILITY.md#nfr-14).
- Status — Not Started

## FR-028

**Administrative review**

Allow authorized reviewers to make recorded decisions on quarantined information.

- Domain and priority — Trust IQ, P0 (proposed)
- Target release and gate — [Gate V1.0](../product/RELEASE_STRATEGY.md#gate-v10)
- Implementation phase and checkpoint — Phase 3, [CP-3.2](../engineering/ROADMAP.md#cp-32)
- Dependencies — [FR-023](#fr-023), [FR-024](#fr-024)
- Acceptance criterion — Reviewer can approve/reject quarantined fact; decision audit recorded.
- Verification — Pending automated verification with reviewer role and quarantine decision audit. Test reference TEST-FR-028.
- Traceability — [Launch controls](LAUNCH_SCOPE.md#launch-controls). Controls [NFR-01](../engineering/TRACEABILITY.md#nfr-01), [NFR-02](../engineering/TRACEABILITY.md#nfr-02), [NFR-04](../engineering/TRACEABILITY.md#nfr-04), [NFR-07](../engineering/TRACEABILITY.md#nfr-07), [NFR-09](../engineering/TRACEABILITY.md#nfr-09).
- Status — Not Started

## FR-029

**Data export and deletion**

Support user data export, deletion and backup expiry tracking.

- Domain and priority — Trust IQ, P0 (proposed)
- Target release and gate — [Gate V1.0](../product/RELEASE_STRATEGY.md#gate-v10)
- Implementation phase and checkpoint — Phase 4, [CP-4.2](../engineering/ROADMAP.md#cp-42)
- Dependencies — [FR-015](#fr-015), [CP-1.1](../engineering/ROADMAP.md#cp-11)
- Acceptance criterion — Export includes user records; deletion removes active copies and queues backup expiry.
- Verification — Pending automated verification with export, deletion and queue inspection. Test reference TEST-FR-029.
- Traceability — [Launch controls](LAUNCH_SCOPE.md#launch-controls). Controls [NFR-01](../engineering/TRACEABILITY.md#nfr-01), [NFR-02](../engineering/TRACEABILITY.md#nfr-02), [NFR-07](../engineering/TRACEABILITY.md#nfr-07), [NFR-09](../engineering/TRACEABILITY.md#nfr-09), [NFR-11](../engineering/TRACEABILITY.md#nfr-11).
- Status — Not Started

## FR-030

**Multilingual and multicurrency support**

Localize applicable content and present currency conversions with timestamped rates.

- Domain and priority — Destination IQ, P1 (proposed)
- Target release and gate — [Gate V1.1](../product/RELEASE_STRATEGY.md#gate-v11)
- Implementation phase and checkpoint — Phase 7, [CP-7.2](../engineering/ROADMAP.md#cp-72)
- Dependencies — [CP-2.1](../engineering/ROADMAP.md#cp-21), [FR-023](#fr-023)
- Acceptance criterion — Locale and currency fixtures preserve units, original value and rate timestamp.
- Verification — Pending automated verification with locales, original monetary units and rates. Test reference TEST-FR-030.
- Traceability — Post-launch. Controls [NFR-08](../engineering/TRACEABILITY.md#nfr-08), [NFR-09](../engineering/TRACEABILITY.md#nfr-09).
- Status — Not Started

## FR-031

**Interactive seasonal atlas**

Explore destinations through a map filtered by travel month and climate.

- Domain and priority — Season IQ, P0
- Target release and gate — [Gate V1.1](../product/RELEASE_STRATEGY.md#gate-v11)
- Implementation phase and checkpoint — Phase 7, [CP-7.1](../engineering/ROADMAP.md#cp-71)
- Dependencies — [FR-004](#fr-004), [FR-005](#fr-005), [FR-033](#fr-033), [FR-034](#fr-034)
- Acceptance criterion — Atlas filters month and climate; unsupported regions visibly marked.
- Verification — Pending automated verification with map filters and unsupported-region fixtures. Test reference TEST-FR-031.
- Traceability — Post-launch. Controls [NFR-08](../engineering/TRACEABILITY.md#nfr-08), [NFR-09](../engineering/TRACEABILITY.md#nfr-09).
- Status — Not Started

## FR-032

**Month-based discovery**

Discover eligible destinations for a specified month with supporting rationale.

- Domain and priority — Season IQ, P0
- Target release and gate — [Gate V1.1](../product/RELEASE_STRATEGY.md#gate-v11)
- Implementation phase and checkpoint — Phase 7, [CP-7.1](../engineering/ROADMAP.md#cp-71)
- Dependencies — [FR-031](#fr-031), [FR-034](#fr-034)
- Acceptance criterion — Month filter returns only eligible supported destinations; rationale shown.
- Verification — Pending automated verification with eligible candidates and rationale. Test reference TEST-FR-032.
- Traceability — Post-launch. Controls [NFR-08](../engineering/TRACEABILITY.md#nfr-08), [NFR-09](../engineering/TRACEABILITY.md#nfr-09).
- Status — Not Started

## FR-033

**AQI and environmental intelligence**

Present sourced AQI and environmental observations with freshness and standard.

- Domain and priority — Season IQ, P0
- Target release and gate — [Gate V1.1](../product/RELEASE_STRATEGY.md#gate-v11)
- Implementation phase and checkpoint — Phase 7, [CP-7.1](../engineering/ROADMAP.md#cp-71)
- Dependencies — [FR-023](#fr-023), [FR-024](#fr-024)
- Acceptance criterion — AQI shows standard, observation time and source; stale readings labeled.
- Verification — Pending automated verification with AQI standard and expired observation. Test reference TEST-FR-033.
- Traceability — Post-launch. Controls [NFR-03](../engineering/TRACEABILITY.md#nfr-03), [NFR-04](../engineering/TRACEABILITY.md#nfr-04), [NFR-09](../engineering/TRACEABILITY.md#nfr-09).
- Status — Not Started

## FR-034

**Explainable suitability ranking**

Rank suitability with visible evidence and weights while honoring safety constraints.

- Domain and priority — Season IQ, P0
- Target release and gate — [Gate V1.1](../product/RELEASE_STRATEGY.md#gate-v11)
- Implementation phase and checkpoint — Phase 7, [CP-7.1](../engineering/ROADMAP.md#cp-71)
- Dependencies — [FR-004](#fr-004), [FR-005](#fr-005), [FR-008](#fr-008), [FR-033](#fr-033)
- Acceptance criterion — Ranking exposes inputs and weights; serious advisory cannot be averaged away.
- Verification — Pending automated verification with ranking weights and serious advisory override. Test reference TEST-FR-034.
- Traceability — Post-launch. Controls [NFR-05](../engineering/TRACEABILITY.md#nfr-05), [NFR-09](../engineering/TRACEABILITY.md#nfr-09), [NFR-13](../engineering/TRACEABILITY.md#nfr-13).
- Status — Not Started

## FR-035

**Activity-specific seasonal intelligence**

Describe seasonal activity windows and their evidence and uncertainty.

- Domain and priority — Season IQ, P0
- Target release and gate — [Gate V1.1](../product/RELEASE_STRATEGY.md#gate-v11)
- Implementation phase and checkpoint — Phase 7, [CP-7.1](../engineering/ROADMAP.md#cp-71)
- Dependencies — [FR-004](#fr-004), [FR-011](#fr-011), [FR-023](#fr-023)
- Acceptance criterion — Activity window includes evidence and uncertainty; missing season unknown.
- Verification — Pending automated verification with activity evidence and missing season. Test reference TEST-FR-035.
- Traceability — Post-launch. Controls [NFR-03](../engineering/TRACEABILITY.md#nfr-03), [NFR-09](../engineering/TRACEABILITY.md#nfr-09).
- Status — Not Started

## FR-036

**Geospatial incident mapping**

Map geospatial incidents with verified time and geographic precision.

- Domain and priority — Safety IQ, P0
- Target release and gate — [Gate V1.3](../product/RELEASE_STRATEGY.md#gate-v13)
- Implementation phase and checkpoint — Phase 9, [CP-9.1](../engineering/ROADMAP.md#cp-91)
- Dependencies — [FR-008](#fr-008), [CP-2.1](../engineering/ROADMAP.md#cp-21)
- Acceptance criterion — Incident map uses verified geometry and time; uncertain location not shown as precise pin.
- Verification — Pending automated verification with precise versus uncertain event geometry. Test reference TEST-FR-036.
- Traceability — Post-launch. Controls [NFR-03](../engineering/TRACEABILITY.md#nfr-03), [NFR-09](../engineering/TRACEABILITY.md#nfr-09), [NFR-12](../engineering/TRACEABILITY.md#nfr-12).
- Status — Not Started

## FR-037

**Government advisory comparisons**

Compare official advisories across available authorities.

- Domain and priority — Safety IQ, P0
- Target release and gate — [Gate V1.3](../product/RELEASE_STRATEGY.md#gate-v13)
- Implementation phase and checkpoint — Phase 9, [CP-9.1](../engineering/ROADMAP.md#cp-91)
- Dependencies — [FR-008](#fr-008), [FR-024](#fr-024)
- Acceptance criterion — Compare at least two available authorities without merging conflicting advice.
- Verification — Pending automated verification with two authorities and conflicting guidance. Test reference TEST-FR-037.
- Traceability — Post-launch. Controls [NFR-03](../engineering/TRACEABILITY.md#nfr-03), [NFR-09](../engineering/TRACEABILITY.md#nfr-09), [NFR-12](../engineering/TRACEABILITY.md#nfr-12).
- Status — Not Started

## FR-038

**Historical intelligence**

Query historical facts by effective time while retaining source caveats.

- Domain and priority — Pulse IQ, P0
- Target release and gate — [Gate V1.3](../product/RELEASE_STRATEGY.md#gate-v13)
- Implementation phase and checkpoint — Phase 9, [CP-9.1](../engineering/ROADMAP.md#cp-91)
- Dependencies — [FR-007](#fr-007), [FR-024](#fr-024)
- Acceptance criterion — Historical query returns correct as-of versions and reporting caveats.
- Verification — Pending automated verification with as-of history and caveats. Test reference TEST-FR-038.
- Traceability — Post-launch. Controls [NFR-03](../engineering/TRACEABILITY.md#nfr-03), [NFR-04](../engineering/TRACEABILITY.md#nfr-04), [NFR-09](../engineering/TRACEABILITY.md#nfr-09), [NFR-12](../engineering/TRACEABILITY.md#nfr-12).
- Status — Not Started

## FR-039

**Dynamic briefing cadence**

Increase briefing frequency as departure approaches and during travel.

- Domain and priority — Pulse IQ, P0
- Target release and gate — [Gate V1.2](../product/RELEASE_STRATEGY.md#gate-v12)
- Implementation phase and checkpoint — Phase 8, [CP-8.2](../engineering/ROADMAP.md#cp-82)
- Dependencies — [FR-021](#fr-021), [FR-041](#fr-041)
- Acceptance criterion — Boundary tests: >30 weekly, 8–30 twice weekly, ≤7 daily; stop after return.
- Verification — Pending automated verification with clock at 31, 30, 8 and 7 days and trip end. Test reference TEST-FR-039.
- Traceability — Post-launch. Controls [NFR-09](../engineering/TRACEABILITY.md#nfr-09), [NFR-10](../engineering/TRACEABILITY.md#nfr-10), [NFR-13](../engineering/TRACEABILITY.md#nfr-13).
- Status — Not Started

## FR-040

**Trip-relevant event correlation**

Associate events with saved trips by overlapping geography and effective dates.

- Domain and priority — Pulse IQ, P0
- Target release and gate — [Gate V1.0](../product/RELEASE_STRATEGY.md#gate-v10)
- Implementation phase and checkpoint — Phase 5, [CP-5.2](../engineering/ROADMAP.md#cp-52)
- Dependencies — [FR-007](#fr-007), [FR-008](#fr-008), [FR-015](#fr-015)
- Acceptance criterion — Spatial and temporal overlap matches relevant trip; unrelated event suppressed.
- Verification — Pending automated verification with intersecting and disjoint geometry/time. Test reference TEST-FR-040.
- Traceability — [L14](../product/LAUNCH_SCOPE.md#l14). Controls [NFR-07](../engineering/TRACEABILITY.md#nfr-07), [NFR-09](../engineering/TRACEABILITY.md#nfr-09), [NFR-10](../engineering/TRACEABILITY.md#nfr-10).
- Status — Not Started

## FR-041

**Quiet hours and notification controls**

Let travelers manage quiet hours and consent for urgent overrides.

- Domain and priority — Pulse IQ, P0
- Target release and gate — [Gate V1.0](../product/RELEASE_STRATEGY.md#gate-v10)
- Implementation phase and checkpoint — Phase 5, [CP-5.2](../engineering/ROADMAP.md#cp-52)
- Dependencies — [FR-015](#fr-015)
- Acceptance criterion — Quiet hours respected for nonurgent alerts; urgent override requires consent.
- Verification — Pending automated verification with quiet hours and urgent override consent. Test reference TEST-FR-041.
- Traceability — [L14](../product/LAUNCH_SCOPE.md#l14). Controls [NFR-09](../engineering/TRACEABILITY.md#nfr-09), [NFR-10](../engineering/TRACEABILITY.md#nfr-10).
- Status — Not Started

## FR-042

**Practical local living intelligence**

Publish sourced practical travel essentials and mark unknown fields.

- Domain and priority — Destination IQ, P0
- Target release and gate — [Gate V1.0](../product/RELEASE_STRATEGY.md#gate-v10)
- Implementation phase and checkpoint — Phase 3, [CP-3.3](../engineering/ROADMAP.md#cp-33)
- Dependencies — [CP-2.1](../engineering/ROADMAP.md#cp-21), [FR-023](#fr-023)
- Acceptance criterion — Practical facts include local source and date; missing values explicit.
- Verification — Pending automated verification with practical fields and missing values. Test reference TEST-FR-042.
- Traceability — [L12](../product/LAUNCH_SCOPE.md#l12). Controls [NFR-03](../engineering/TRACEABILITY.md#nfr-03), [NFR-04](../engineering/TRACEABILITY.md#nfr-04), [NFR-09](../engineering/TRACEABILITY.md#nfr-09).
- Status — Not Started

## FR-043

**Neighborhood intelligence**

Assess neighborhoods using geographic evidence and supported coverage.

- Domain and priority — Safety IQ, P1
- Target release and gate — [Gate V1.3](../product/RELEASE_STRATEGY.md#gate-v13)
- Implementation phase and checkpoint — Phase 9, [CP-9.1](../engineering/ROADMAP.md#cp-91)
- Dependencies — [FR-009](#fr-009), [FR-036](#fr-036), [FR-042](#fr-042)
- Acceptance criterion — Neighborhood assessment returns unknown below coverage threshold; no demographic proxy.
- Verification — Pending automated verification with low coverage and demographic proxy checks. Test reference TEST-FR-043.
- Traceability — Post-launch. Controls [NFR-09](../engineering/TRACEABILITY.md#nfr-09), [NFR-12](../engineering/TRACEABILITY.md#nfr-12).
- Status — Not Started

## FR-044

**Know Your Stay accommodation assessment**

Describe hotel-area access, distances and evidenced local conditions.

- Domain and priority — Safety IQ, P1
- Target release and gate — [Gate V1.3](../product/RELEASE_STRATEGY.md#gate-v13)
- Implementation phase and checkpoint — Phase 9, [CP-9.1](../engineering/ROADMAP.md#cp-91)
- Dependencies — [FR-013](#fr-013), [FR-043](#fr-043)
- Acceptance criterion — Hotel-area report distinguishes distance, access and evidenced risk; unknowns visible.
- Verification — Pending automated verification with hotel distance, accessibility and risk data. Test reference TEST-FR-044.
- Traceability — Post-launch. Controls [NFR-03](../engineering/TRACEABILITY.md#nfr-03), [NFR-09](../engineering/TRACEABILITY.md#nfr-09), [NFR-12](../engineering/TRACEABILITY.md#nfr-12).
- Status — Not Started

## FR-045

**Reservation confirmation import**

Extract approved reservation fields from consented input and require confirmation.

- Domain and priority — Plan IQ, P1
- Target release and gate — [Gate V1.2](../product/RELEASE_STRATEGY.md#gate-v12)
- Implementation phase and checkpoint — Phase 8, [CP-8.1](../engineering/ROADMAP.md#cp-81)
- Dependencies — [FR-015](#fr-015), [CP-1.1](../engineering/ROADMAP.md#cp-11)
- Acceptance criterion — Extract selected confirmation fields; user confirms; raw deletion and isolation tested.
- Verification — Pending automated verification with confirmed extraction, cross-user access and retention clock. Test reference TEST-FR-045.
- Traceability — Post-launch. Controls [NFR-01](../engineering/TRACEABILITY.md#nfr-01), [NFR-02](../engineering/TRACEABILITY.md#nfr-02), [NFR-05](../engineering/TRACEABILITY.md#nfr-05), [NFR-09](../engineering/TRACEABILITY.md#nfr-09), [NFR-11](../engineering/TRACEABILITY.md#nfr-11).
- Status — Not Started

## FR-046

**Flight status and gate tracking**

Track date-specific flight status and gate changes with freshness shown.

- Domain and priority — Transit IQ, P1
- Target release and gate — [Gate V1.2](../product/RELEASE_STRATEGY.md#gate-v12)
- Implementation phase and checkpoint — Phase 8, [CP-8.1](../engineering/ROADMAP.md#cp-81)
- Dependencies — [FR-045](#fr-045), [FR-024](#fr-024)
- Acceptance criterion — Flight update matches flight/date; stale feed labeled; duplicates suppressed.
- Verification — Pending automated verification with flight identity, expiry and duplicate replay. Test reference TEST-FR-046.
- Traceability — Post-launch. Controls [NFR-03](../engineering/TRACEABILITY.md#nfr-03), [NFR-04](../engineering/TRACEABILITY.md#nfr-04), [NFR-07](../engineering/TRACEABILITY.md#nfr-07), [NFR-09](../engineering/TRACEABILITY.md#nfr-09), [NFR-10](../engineering/TRACEABILITY.md#nfr-10), [NFR-11](../engineering/TRACEABILITY.md#nfr-11), [NFR-13](../engineering/TRACEABILITY.md#nfr-13).
- Status — Not Started

## FR-047

**Travel Digital Twin**

Model dependency impacts between reservations, activities and trip segments.

- Domain and priority — Plan IQ, P1
- Target release and gate — [Gate V1.2](../product/RELEASE_STRATEGY.md#gate-v12)
- Implementation phase and checkpoint — Phase 8, [CP-8.2](../engineering/ROADMAP.md#cp-82)
- Dependencies — [FR-045](#fr-045), [FR-046](#fr-046)
- Acceptance criterion — Delayed-flight fixture identifies downstream dependencies; cycles handled; no booking changes.
- Verification — Pending automated verification with delayed flight and cycle fixtures. Test reference TEST-FR-047.
- Traceability — Post-launch. Controls [NFR-05](../engineering/TRACEABILITY.md#nfr-05), [NFR-09](../engineering/TRACEABILITY.md#nfr-09), [NFR-11](../engineering/TRACEABILITY.md#nfr-11), [NFR-14](../engineering/TRACEABILITY.md#nfr-14).
- Status — Not Started

## FR-048

**Destination What-If Simulator**

Recalculate a proposed trip scenario under alternative dates or occupancy.

- Domain and priority — Budget IQ, P1
- Target release and gate — [Gate V1.1](../product/RELEASE_STRATEGY.md#gate-v11)
- Implementation phase and checkpoint — Phase 7, [CP-7.2](../engineering/ROADMAP.md#cp-72)
- Dependencies — [FR-019](#fr-019)
- Acceptance criterion — Scenario changes dates/occupancy and recalculates ranges with assumptions.
- Verification — Pending automated verification with date and occupancy sensitivity. Test reference TEST-FR-048.
- Traceability — Post-launch. Controls [NFR-05](../engineering/TRACEABILITY.md#nfr-05), [NFR-09](../engineering/TRACEABILITY.md#nfr-09), [NFR-13](../engineering/TRACEABILITY.md#nfr-13).
- Status — Not Started

## FR-049

**Travel Readiness Center**

Build a trip preparation checklist from trip facts and traveler inputs.

- Domain and priority — Ready IQ, P1
- Target release and gate — [Gate V1.1](../product/RELEASE_STRATEGY.md#gate-v11)
- Implementation phase and checkpoint — Phase 7, [CP-7.2](../engineering/ROADMAP.md#cp-72)
- Dependencies — [FR-015](#fr-015), [FR-018](#fr-018)
- Acceptance criterion — Checklist generated from trip facts; completion not presented as safety or entry guarantee.
- Verification — Pending automated verification with checklist completion and eligibility distinction. Test reference TEST-FR-049.
- Traceability — Post-launch. Controls [NFR-05](../engineering/TRACEABILITY.md#nfr-05), [NFR-09](../engineering/TRACEABILITY.md#nfr-09).
- Status — Not Started

## FR-050

**Constraint-based itinerary optimization**

Optimize itineraries subject to hard constraints and explain infeasibility.

- Domain and priority — Plan IQ, P1
- Target release and gate — [Gate V1.2](../product/RELEASE_STRATEGY.md#gate-v12)
- Implementation phase and checkpoint — Phase 8, [CP-8.2](../engineering/ROADMAP.md#cp-82)
- Dependencies — [FR-016](#fr-016), [FR-047](#fr-047)
- Acceptance criterion — Optimizer respects hard constraints; infeasible case returns explanation.
- Verification — Pending automated verification with feasible and infeasible constraint sets. Test reference TEST-FR-050.
- Traceability — Post-launch. Controls [NFR-05](../engineering/TRACEABILITY.md#nfr-05), [NFR-09](../engineering/TRACEABILITY.md#nfr-09).
- Status — Not Started

## FR-051

**Verified creator contributions**

Collect creator contributions with documented rights and moderation.

- Domain and priority — Experience IQ, P1
- Target release and gate — [Gate V2.0](../product/RELEASE_STRATEGY.md#gate-v20)
- Implementation phase and checkpoint — Phase 10, [CP-10.1](../engineering/ROADMAP.md#cp-101)
- Dependencies — [FR-011](#fr-011), [FR-028](#fr-028)
- Acceptance criterion — Creator contribution records rights, visit date and moderation status before publication.
- Verification — Pending automated verification with submission rights and moderation review. Test reference TEST-FR-051.
- Traceability — Post-launch. Controls [NFR-09](../engineering/TRACEABILITY.md#nfr-09), [NFR-14](../engineering/TRACEABILITY.md#nfr-14).
- Status — Not Started

## FR-052

**Location-linked videos**

Attach licensed video to canonical locations and honor revoked rights.

- Domain and priority — Experience IQ, P1
- Target release and gate — [Gate V2.0](../product/RELEASE_STRATEGY.md#gate-v20)
- Implementation phase and checkpoint — Phase 10, [CP-10.1](../engineering/ROADMAP.md#cp-101)
- Dependencies — [FR-051](#fr-051), [CP-2.1](../engineering/ROADMAP.md#cp-21)
- Acceptance criterion — Video links to canonical location; rights revocation removes access.
- Verification — Pending automated verification with location linkage and revoked media rights. Test reference TEST-FR-052.
- Traceability — Post-launch. Controls [NFR-09](../engineering/TRACEABILITY.md#nfr-09), [NFR-14](../engineering/TRACEABILITY.md#nfr-14).
- Status — Not Started

## FR-053

**Traveler-reported expenses**

Collect and aggregate validated expense reports with source context.

- Domain and priority — Experience IQ, P1
- Target release and gate — [Gate V2.0](../product/RELEASE_STRATEGY.md#gate-v20)
- Implementation phase and checkpoint — Phase 10, [CP-10.1](../engineering/ROADMAP.md#cp-101)
- Dependencies — [FR-051](#fr-051), [FR-030](#fr-030)
- Acceptance criterion — Expense records include currency, date and category; aggregation excludes invalid records.
- Verification — Pending automated verification with expense validation and aggregation. Test reference TEST-FR-053.
- Traceability — Post-launch. Controls [NFR-09](../engineering/TRACEABILITY.md#nfr-09), [NFR-13](../engineering/TRACEABILITY.md#nfr-13), [NFR-14](../engineering/TRACEABILITY.md#nfr-14).
- Status — Not Started

## FR-054

**Community scam/disruption reports**

Accept traveler scam and disruption reports for moderation.

- Domain and priority — Safety IQ, P1
- Target release and gate — [Gate V1.3](../product/RELEASE_STRATEGY.md#gate-v13)
- Implementation phase and checkpoint — Phase 9, [CP-9.1](../engineering/ROADMAP.md#cp-91)
- Dependencies — [FR-010](#fr-010), [FR-028](#fr-028)
- Acceptance criterion — Report enters moderation; unverified report not promoted to critical alert.
- Verification — Pending automated verification with moderation and unverified alert suppression. Test reference TEST-FR-054.
- Traceability — Post-launch. Controls [NFR-09](../engineering/TRACEABILITY.md#nfr-09), [NFR-12](../engineering/TRACEABILITY.md#nfr-12), [NFR-14](../engineering/TRACEABILITY.md#nfr-14).
- Status — Not Started

## FR-055

**Personal traveler profiles**

Store optional editable and deletable traveler preferences.

- Domain and priority — Plan IQ, P1
- Target release and gate — [Gate V1.1](../product/RELEASE_STRATEGY.md#gate-v11)
- Implementation phase and checkpoint — Phase 7, [CP-7.2](../engineering/ROADMAP.md#cp-72)
- Dependencies — [FR-015](#fr-015), [FR-029](#fr-029)
- Acceptance criterion — Optional preferences editable/deletable; sensitive defaults absent.
- Verification — Pending automated verification with preference editing, deletion and defaults. Test reference TEST-FR-055.
- Traceability — Post-launch. Controls [NFR-01](../engineering/TRACEABILITY.md#nfr-01), [NFR-09](../engineering/TRACEABILITY.md#nfr-09).
- Status — Not Started

## FR-056

**Printable intelligence reports**

Produce printable destination or trip reports with evidence and generation date.

- Domain and priority — Destination IQ, P1
- Target release and gate — [Gate V1.1](../product/RELEASE_STRATEGY.md#gate-v11)
- Implementation phase and checkpoint — Phase 7, [CP-7.2](../engineering/ROADMAP.md#cp-72)
- Dependencies — [FR-003](#fr-003), [FR-023](#fr-023), [FR-024](#fr-024)
- Acceptance criterion — Export report includes sources, generation time and uncertainty.
- Verification — Pending automated verification with rendered report content snapshot. Test reference TEST-FR-056.
- Traceability — Post-launch. Controls [NFR-03](../engineering/TRACEABILITY.md#nfr-03), [NFR-08](../engineering/TRACEABILITY.md#nfr-08), [NFR-09](../engineering/TRACEABILITY.md#nfr-09).
- Status — Not Started

## FR-057

**Verified provider marketplace**

List eligible verified providers and enforce expired credential removal.

- Domain and priority — Trust IQ, P2
- Target release and gate — [Gate V2.0](../product/RELEASE_STRATEGY.md#gate-v20)
- Implementation phase and checkpoint — Phase 10, [CP-10.2](../engineering/ROADMAP.md#cp-102)
- Dependencies — [FR-058](#fr-058), [FR-060](#fr-060)
- Acceptance criterion — Marketplace lists only eligible providers; expired verification removed.
- Verification — Pending automated verification with eligible and expired provider fixtures. Test reference TEST-FR-057.
- Traceability — Post-launch. Controls [NFR-09](../engineering/TRACEABILITY.md#nfr-09), [NFR-13](../engineering/TRACEABILITY.md#nfr-13), [NFR-14](../engineering/TRACEABILITY.md#nfr-14).
- Status — Not Started

## FR-058

**Credential verification**

Verify provider credentials within issuer, scope and expiry boundaries.

- Domain and priority — Trust IQ, P2
- Target release and gate — [Gate V2.0](../product/RELEASE_STRATEGY.md#gate-v20)
- Implementation phase and checkpoint — Phase 10, [CP-10.2](../engineering/ROADMAP.md#cp-102)
- Dependencies — [FR-028](#fr-028)
- Acceptance criterion — Credential check records issuer, scope and expiry; failed check not verified.
- Verification — Pending automated verification with issuer, scope, expiry and failed checks. Test reference TEST-FR-058.
- Traceability — Post-launch. Controls [NFR-02](../engineering/TRACEABILITY.md#nfr-02), [NFR-03](../engineering/TRACEABILITY.md#nfr-03), [NFR-09](../engineering/TRACEABILITY.md#nfr-09), [NFR-14](../engineering/TRACEABILITY.md#nfr-14).
- Status — Not Started

## FR-059

**Confirmed-trip reviews**

Accept one eligible review per qualifying confirmed transaction.

- Domain and priority — Trust IQ, P2
- Target release and gate — [Gate V2.0](../product/RELEASE_STRATEGY.md#gate-v20)
- Implementation phase and checkpoint — Phase 10, [CP-10.2](../engineering/ROADMAP.md#cp-102)
- Dependencies — [FR-057](#fr-057)
- Acceptance criterion — Review requires transaction evidence; duplicate review rejected.
- Verification — Pending automated verification with transaction evidence and duplicate reviews. Test reference TEST-FR-059.
- Traceability — Post-launch. Controls [NFR-09](../engineering/TRACEABILITY.md#nfr-09), [NFR-14](../engineering/TRACEABILITY.md#nfr-14).
- Status — Not Started

## FR-060

**Transparent total pricing**

Disclose total known mandatory pricing and unresolved charges.

- Domain and priority — Trust IQ, P2
- Target release and gate — [Gate V2.0](../product/RELEASE_STRATEGY.md#gate-v20)
- Implementation phase and checkpoint — Phase 10, [CP-10.2](../engineering/ROADMAP.md#cp-102)
- Dependencies — [FR-023](#fr-023)
- Acceptance criterion — Total price includes known mandatory charges; unknown charges disclosed.
- Verification — Pending automated verification with mandatory and unknown charge fixtures. Test reference TEST-FR-060.
- Traceability — Post-launch. Controls [NFR-09](../engineering/TRACEABILITY.md#nfr-09), [NFR-13](../engineering/TRACEABILITY.md#nfr-13), [NFR-14](../engineering/TRACEABILITY.md#nfr-14).
- Status — Not Started

## FR-061

**Travel Circle and shared itineraries**

Share explicitly selected trip information with revocable access.

- Domain and priority — Circle IQ, P2
- Target release and gate — [Gate V2.0](../product/RELEASE_STRATEGY.md#gate-v20)
- Implementation phase and checkpoint — Phase 10, [CP-10.3](../engineering/ROADMAP.md#cp-103)
- Dependencies — [FR-015](#fr-015), [FR-029](#fr-029)
- Acceptance criterion — Share only selected trip fields; revoked or expired link denied.
- Verification — Pending automated verification with selective share, revocation and expiry. Test reference TEST-FR-061.
- Traceability — Post-launch. Controls [NFR-01](../engineering/TRACEABILITY.md#nfr-01), [NFR-02](../engineering/TRACEABILITY.md#nfr-02), [NFR-09](../engineering/TRACEABILITY.md#nfr-09), [NFR-14](../engineering/TRACEABILITY.md#nfr-14).
- Status — Not Started

## FR-062

**Voluntary safety check-ins**

Provide consent-based safety check-ins with recipient visibility.

- Domain and priority — Circle IQ, P2
- Target release and gate — [Gate V2.0](../product/RELEASE_STRATEGY.md#gate-v20)
- Implementation phase and checkpoint — Phase 10, [CP-10.3](../engineering/ROADMAP.md#cp-103)
- Dependencies — [FR-061](#fr-061)
- Acceptance criterion — Check-in requires opt-in; recipients and timestamp visible; stop on revocation.
- Verification — Pending automated verification with opt-in, recipients and revocation. Test reference TEST-FR-062.
- Traceability — Post-launch. Controls [NFR-01](../engineering/TRACEABILITY.md#nfr-01), [NFR-09](../engineering/TRACEABILITY.md#nfr-09), [NFR-14](../engineering/TRACEABILITY.md#nfr-14).
- Status — Not Started

## FR-063

**Insurance partner integration**

Refer travelers to approved insurance partners with disclosed terms.

- Domain and priority — Care IQ, P2
- Target release and gate — [Gate V2.0](../product/RELEASE_STRATEGY.md#gate-v20)
- Implementation phase and checkpoint — Phase 10, [CP-10.3](../engineering/ROADMAP.md#cp-103)
- Dependencies — [FR-058](#fr-058)
- Acceptance criterion — Insurance referral discloses partner and terms; no underwriting by platform.
- Verification — Pending automated verification with partner referral and underwriting boundary. Test reference TEST-FR-063.
- Traceability — Post-launch. Controls [NFR-09](../engineering/TRACEABILITY.md#nfr-09), [NFR-13](../engineering/TRACEABILITY.md#nfr-13), [NFR-14](../engineering/TRACEABILITY.md#nfr-14).
- Status — Not Started

## FR-064

**Telemedicine and assistance partners**

Refer travelers to qualified assistance partners using verified contacts.

- Domain and priority — Care IQ, P2
- Target release and gate — [Gate V2.0](../product/RELEASE_STRATEGY.md#gate-v20)
- Implementation phase and checkpoint — Phase 10, [CP-10.3](../engineering/ROADMAP.md#cp-103)
- Dependencies — [FR-058](#fr-058), [FR-023](#fr-023)
- Acceptance criterion — Assistance handoff uses approved partner and verified contact; no medical claims.
- Verification — Pending automated verification with approved contacts and medical claim policy. Test reference TEST-FR-064.
- Traceability — Post-launch. Controls [NFR-09](../engineering/TRACEABILITY.md#nfr-09), [NFR-14](../engineering/TRACEABILITY.md#nfr-14).
- Status — Not Started

## FR-065

**Creator monetization**

Account for creator earnings and disclose commercial relationships.

- Domain and priority — Experience IQ, P2
- Target release and gate — [Gate V2.0](../product/RELEASE_STRATEGY.md#gate-v20)
- Implementation phase and checkpoint — Phase 11, [CP-11.1](../engineering/ROADMAP.md#cp-111)
- Dependencies — [FR-051](#fr-051), [FR-057](#fr-057)
- Acceptance criterion — Creator earnings ledger reconciles transactions; disclosures visible.
- Verification — Pending automated verification with settlement reconciliation and disclosure. Test reference TEST-FR-065.
- Traceability — Post-launch. Controls [NFR-09](../engineering/TRACEABILITY.md#nfr-09), [NFR-13](../engineering/TRACEABILITY.md#nfr-13), [NFR-14](../engineering/TRACEABILITY.md#nfr-14).
- Status — Not Started

## FR-066

**Enterprise intelligence APIs**

Expose licensed destination intelligence APIs to isolated enterprise tenants.

- Domain and priority — Trust IQ, P2
- Target release and gate — [Gate V2.0](../product/RELEASE_STRATEGY.md#gate-v20)
- Implementation phase and checkpoint — Phase 11, [CP-11.2](../engineering/ROADMAP.md#cp-112)
- Dependencies — [FR-023](#fr-023), [FR-029](#fr-029), [CP-1.1](../engineering/ROADMAP.md#cp-11)
- Acceptance criterion — API tenant isolation, rate limits and licensing restrictions tested.
- Verification — Pending automated verification with tenant boundaries, rate limits and license constraints. Test reference TEST-FR-066.
- Traceability — Post-launch. Controls [NFR-01](../engineering/TRACEABILITY.md#nfr-01), [NFR-02](../engineering/TRACEABILITY.md#nfr-02), [NFR-06](../engineering/TRACEABILITY.md#nfr-06), [NFR-07](../engineering/TRACEABILITY.md#nfr-07), [NFR-09](../engineering/TRACEABILITY.md#nfr-09), [NFR-13](../engineering/TRACEABILITY.md#nfr-13).
- Status — Not Started

## FR-067

**Encrypted document vault**

Provide gated encrypted storage for sensitive documents.

- Domain and priority — Trust IQ, P3
- Target release and gate — [Gate V3.0](../product/RELEASE_STRATEGY.md#gate-v30)
- Implementation phase and checkpoint — Phase 12, [CP-12.2](../engineering/ROADMAP.md#cp-122)
- Dependencies — [FR-029](#fr-029), [CP-1.1](../engineering/ROADMAP.md#cp-11)
- Acceptance criterion — Vault encrypted with access controls; threat model and deletion gate passed.
- Verification — Pending automated verification with vault authorization, encryption and deletion. Test reference TEST-FR-067.
- Traceability — Post-launch. Controls [NFR-01](../engineering/TRACEABILITY.md#nfr-01), [NFR-02](../engineering/TRACEABILITY.md#nfr-02), [NFR-09](../engineering/TRACEABILITY.md#nfr-09), [NFR-14](../engineering/TRACEABILITY.md#nfr-14).
- Status — Not Started

## FR-068

**Revocable identity document sharing**

Allow narrowly scoped time-bounded identity document sharing and revocation.

- Domain and priority — Trust IQ, P3
- Target release and gate — [Gate V3.0](../product/RELEASE_STRATEGY.md#gate-v30)
- Implementation phase and checkpoint — Phase 12, [CP-12.2](../engineering/ROADMAP.md#cp-122)
- Dependencies — [FR-067](#fr-067), [FR-069](#fr-069)
- Acceptance criterion — Document share scoped and expiring; revoked access fails.
- Verification — Pending automated verification with share scope, expiry and revocation. Test reference TEST-FR-068.
- Traceability — Post-launch. Controls [NFR-01](../engineering/TRACEABILITY.md#nfr-01), [NFR-02](../engineering/TRACEABILITY.md#nfr-02), [NFR-09](../engineering/TRACEABILITY.md#nfr-09), [NFR-14](../engineering/TRACEABILITY.md#nfr-14).
- Status — Not Started

## FR-069

**Document access audit**

Record auditable authorized access to sensitive documents.

- Domain and priority — Trust IQ, P3
- Target release and gate — [Gate V3.0](../product/RELEASE_STRATEGY.md#gate-v30)
- Implementation phase and checkpoint — Phase 12, [CP-12.2](../engineering/ROADMAP.md#cp-122)
- Dependencies — [FR-067](#fr-067)
- Acceptance criterion — Document access events record actor/time/action; unauthorized log access denied.
- Verification — Pending automated verification with actor/time/action audit and access controls. Test reference TEST-FR-069.
- Traceability — Post-launch. Controls [NFR-01](../engineering/TRACEABILITY.md#nfr-01), [NFR-02](../engineering/TRACEABILITY.md#nfr-02), [NFR-09](../engineering/TRACEABILITY.md#nfr-09), [NFR-14](../engineering/TRACEABILITY.md#nfr-14).
- Status — Not Started

## FR-070

**Community groups**

Support moderated membership-based community groups.

- Domain and priority — Circle IQ, P3
- Target release and gate — [Gate V3.0](../product/RELEASE_STRATEGY.md#gate-v30)
- Implementation phase and checkpoint — Phase 12, [CP-12.2](../engineering/ROADMAP.md#cp-122)
- Dependencies — [FR-061](#fr-061), [FR-028](#fr-028)
- Acceptance criterion — Group membership controls and moderation tested; reporting available.
- Verification — Pending automated verification with membership and moderation abuse cases. Test reference TEST-FR-070.
- Traceability — Post-launch. Controls [NFR-01](../engineering/TRACEABILITY.md#nfr-01), [NFR-09](../engineering/TRACEABILITY.md#nfr-09), [NFR-14](../engineering/TRACEABILITY.md#nfr-14).
- Status — Not Started

## FR-071

**Private messaging**

Provide private messaging with authorization, block and report controls.

- Domain and priority — Circle IQ, P3
- Target release and gate — [Gate V3.0](../product/RELEASE_STRATEGY.md#gate-v30)
- Implementation phase and checkpoint — Phase 12, [CP-12.2](../engineering/ROADMAP.md#cp-122)
- Dependencies — [FR-070](#fr-070)
- Acceptance criterion — Messaging blocks unauthorized access; block/report controls tested.
- Verification — Pending automated verification with unauthorized access, blocking and reporting. Test reference TEST-FR-071.
- Traceability — Post-launch. Controls [NFR-01](../engineering/TRACEABILITY.md#nfr-01), [NFR-02](../engineering/TRACEABILITY.md#nfr-02), [NFR-09](../engineering/TRACEABILITY.md#nfr-09), [NFR-14](../engineering/TRACEABILITY.md#nfr-14).
- Status — Not Started

## FR-072

**Traveler meetups**

Support opt-in meetups with location privacy and reporting.

- Domain and priority — Circle IQ, P3
- Target release and gate — [Gate V3.0](../product/RELEASE_STRATEGY.md#gate-v30)
- Implementation phase and checkpoint — Phase 12, [CP-12.2](../engineering/ROADMAP.md#cp-122)
- Dependencies — [FR-070](#fr-070)
- Acceptance criterion — Meetup visibility opt-in; reporting and location privacy tested.
- Verification — Pending automated verification with opt-in location and reporting. Test reference TEST-FR-072.
- Traceability — Post-launch. Controls [NFR-01](../engineering/TRACEABILITY.md#nfr-01), [NFR-09](../engineering/TRACEABILITY.md#nfr-09), [NFR-14](../engineering/TRACEABILITY.md#nfr-14).
- Status — Not Started

## FR-073

**Predictive travel analytics**

Evaluate predictive travel signals and monitor uncertainty and model drift.

- Domain and priority — Pulse IQ, P3
- Target release and gate — [Gate V3.0](../product/RELEASE_STRATEGY.md#gate-v30)
- Implementation phase and checkpoint — Phase 12, [CP-12.1](../engineering/ROADMAP.md#cp-121)
- Dependencies — [FR-038](#fr-038), [FR-047](#fr-047)
- Acceptance criterion — Predictive model evaluated against holdout baseline; uncertainty and drift monitored.
- Verification — Pending automated verification with holdout baseline, calibration and drift. Test reference TEST-FR-073.
- Traceability — Post-launch. Controls [NFR-05](../engineering/TRACEABILITY.md#nfr-05), [NFR-09](../engineering/TRACEABILITY.md#nfr-09).
- Status — Not Started

## FR-074

**Partner-operated rebooking assistance**

Offer partner-operated rebooking suggestions requiring traveler approval and partner confirmation.

- Domain and priority — Care IQ, P3
- Target release and gate — [Gate V3.0](../product/RELEASE_STRATEGY.md#gate-v30)
- Implementation phase and checkpoint — Phase 12, [CP-12.1](../engineering/ROADMAP.md#cp-121)
- Dependencies — [FR-027](#fr-027), [FR-047](#fr-047), [FR-064](#fr-064)
- Acceptance criterion — Rebooking suggestion requires explicit approval and partner confirmation; no autonomous purchase.
- Verification — Pending automated verification with unapproved, approved and partner-confirmed flows. Test reference TEST-FR-074.
- Traceability — Post-launch. Controls [NFR-05](../engineering/TRACEABILITY.md#nfr-05), [NFR-09](../engineering/TRACEABILITY.md#nfr-09), [NFR-14](../engineering/TRACEABILITY.md#nfr-14).
- Status — Not Started

## FR-075

**Parking discovery**

Find nearby parking facilities with geospatial search.

- Domain and priority — Transit IQ, P1 (proposed)
- Target release and gate — [Gate V1.3](../product/RELEASE_STRATEGY.md#gate-v13)
- Implementation phase and checkpoint — Phase 9, [CP-9.2](../engineering/ROADMAP.md#cp-92)
- Dependencies — [FR-013](#fr-013), [CP-2.1](../engineering/ROADMAP.md#cp-21)
- Acceptance criterion — Search radius returns correct facilities by distance; missing coordinates excluded.
- Verification — Pending automated verification with radius and missing coordinates. Test reference TEST-FR-075.
- Traceability — Post-launch. Controls [NFR-09](../engineering/TRACEABILITY.md#nfr-09), [NFR-12](../engineering/TRACEABILITY.md#nfr-12).
- Status — Not Started

## FR-076

**Prices, hours and restrictions**

Show sourced facility costs, opening hours and access restrictions.

- Domain and priority — Transit IQ, P1 (proposed)
- Target release and gate — [Gate V1.3](../product/RELEASE_STRATEGY.md#gate-v13)
- Implementation phase and checkpoint — Phase 9, [CP-9.2](../engineering/ROADMAP.md#cp-92)
- Dependencies — [FR-075](#fr-075), [FR-023](#fr-023)
- Acceptance criterion — Display sourced price, hours and restrictions; unknown values labeled.
- Verification — Pending automated verification with price, hours and restrictions with unknowns. Test reference TEST-FR-076.
- Traceability — Post-launch. Controls [NFR-03](../engineering/TRACEABILITY.md#nfr-03), [NFR-09](../engineering/TRACEABILITY.md#nfr-09).
- Status — Not Started

## FR-077

**Airport parking and transfers**

Associate airport parking with terminals and transfer options.

- Domain and priority — Transit IQ, P1 (proposed)
- Target release and gate — [Gate V1.3](../product/RELEASE_STRATEGY.md#gate-v13)
- Implementation phase and checkpoint — Phase 9, [CP-9.2](../engineering/ROADMAP.md#cp-92)
- Dependencies — [FR-012](#fr-012), [FR-075](#fr-075)
- Acceptance criterion — Airport parking links to correct terminal/transfer; source shown.
- Verification — Pending automated verification with terminal linkage and transfer evidence. Test reference TEST-FR-077.
- Traceability — Post-launch. Controls [NFR-03](../engineering/TRACEABILITY.md#nfr-03), [NFR-09](../engineering/TRACEABILITY.md#nfr-09).
- Status — Not Started

## FR-078

**Accessible parking and EV charging**

Present documented accessible spaces and EV charging information.

- Domain and priority — Transit IQ, P1 (proposed)
- Target release and gate — [Gate V1.3](../product/RELEASE_STRATEGY.md#gate-v13)
- Implementation phase and checkpoint — Phase 9, [CP-9.2](../engineering/ROADMAP.md#cp-92)
- Dependencies — [FR-075](#fr-075)
- Acceptance criterion — Accessible/EV attributes only displayed when documented; unknown explicit.
- Verification — Pending automated verification with documented accessibility and charging. Test reference TEST-FR-078.
- Traceability — Post-launch. Controls [NFR-03](../engineering/TRACEABILITY.md#nfr-03), [NFR-09](../engineering/TRACEABILITY.md#nfr-09).
- Status — Not Started

## FR-079

**Parking-aware driving itineraries**

Incorporate parking and walking time into driving itineraries.

- Domain and priority — Transit IQ, P1 (proposed)
- Target release and gate — [Gate V1.3](../product/RELEASE_STRATEGY.md#gate-v13)
- Implementation phase and checkpoint — Phase 9, [CP-9.2](../engineering/ROADMAP.md#cp-92)
- Dependencies — [FR-016](#fr-016), [FR-075](#fr-075), [FR-077](#fr-077)
- Acceptance criterion — Driving itinerary includes parking and walk time where known; unknowns flagged.
- Verification — Pending automated verification with parking-aware route and walking-time gaps. Test reference TEST-FR-079.
- Traceability — Post-launch. Controls [NFR-09](../engineering/TRACEABILITY.md#nfr-09).
- Status — Not Started

## FR-080

**Live parking availability**

Present licensed live parking availability with observation time and expiry.

- Domain and priority — Transit IQ, P1 (proposed)
- Target release and gate — [Gate V1.3](../product/RELEASE_STRATEGY.md#gate-v13)
- Implementation phase and checkpoint — Phase 9, [CP-9.2](../engineering/ROADMAP.md#cp-92)
- Dependencies — [FR-075](#fr-075), [FR-024](#fr-024)
- Acceptance criterion — Live availability shows observation time; expired feed returns unknown, never available.
- Verification — Pending automated verification with licensed sample feed and expired observation. Test reference TEST-FR-080.
- Traceability — Post-launch. Controls [NFR-03](../engineering/TRACEABILITY.md#nfr-03), [NFR-04](../engineering/TRACEABILITY.md#nfr-04), [NFR-07](../engineering/TRACEABILITY.md#nfr-07), [NFR-09](../engineering/TRACEABILITY.md#nfr-09), [NFR-12](../engineering/TRACEABILITY.md#nfr-12), [NFR-13](../engineering/TRACEABILITY.md#nfr-13).
- Status — Not Started
