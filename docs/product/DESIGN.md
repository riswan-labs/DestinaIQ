# DestinaIQ

## Global Travel Intelligence Platform

Product and system design specification  |  v3.0  |  27 November 2026

Status: Proposed — V3 launch strategy and engineering readiness. Owner: RiswanLabs.

### Executive summary

DestinaIQ consolidates destination research, seasonal guidance, safety, local news, transportation and personalized trip planning into a continuously maintained intelligence platform. Its core asset is a source-backed geographic knowledge system, not a chatbot. Travelers can discover and compare places before booking, plan a trip, and receive relevant updates until they return. V2 adds environmental discovery, hyperlocal intelligence, verified experiences, trip dependency modeling and partner-led assistance.

### Vision and mission

Vision: Become a trusted intelligence layer for global travel. Mission: Transform fragmented and changing destination information into reliable, personalized and actionable guidance. Product promise: Know the world before you go.

### Design principles

Evidence before generation; destination-first discovery; explicit freshness and uncertainty; privacy by design; progressive geographic coverage; modular architecture; commercial independence of safety and ranking decisions.

### Document map

2–10. Product, architecture, data, AI, security and business foundations<br>
11. Competitive gap analysis<br>
12. Product domains and requirements<br>
13–14. Detailed subsystem design and security<br>
15. Engineering checkpoints<br>
16. Launch scope and release strategy<br>
17. Competitive validation<br>
18. Unit economics<br>
19. Reservation privacy architecture<br>
20. Parking intelligence<br>
21. Requirement acceptance register<br>
22. Release gates and decisions

## 2. Market and customer problem

Travelers must reconcile blogs, videos, maps, weather services, official advisories and booking sites. Static guides age quickly; generic itineraries ignore real-world constraints; destination-level warnings often lack local context. Research must be repeated when conditions change.

| Customer segment | Primary job to be done |
| --- | --- |
| International leisure / couples | Choose a destination and season with confidence; reduce research effort. |
| Families / solo travelers | Understand practical logistics, safety and accessibility. |
| Frequent travelers | Monitor multiple trips and reuse preferences. |
| Travel businesses (later) | Consume reliable destination intelligence through APIs. |

### Competitive landscape

Direct comparison targets: Travel Intel, TripGuard AI, Aurora Travel, Sitata, WARNPOINT and Outroad. See section 11 for the competitive gap analysis and source links. Adjacent benchmarks remain TripAdvisor, Wanderlog, Mindtrip, TripIt, Rome2Rio and Google Maps/Gemini.

The hypothesis is not that no competitor offers these features. The proposed differentiation is a unified, evidence-backed destination model, comparative seasonality, geographically relevant event monitoring and a continuous pre-trip-to-return experience.

### Validation plan

Interview 20–30 travelers; benchmark identical trips across competitors; measure research time, correctness, coverage and update relevance. Test a landing page and trip-monitoring prototype with Journey with Ris viewers. Do not infer willingness to pay from interest alone. Current competitor capabilities, market size and pricing are not independently verified in this document.

## 3. Product requirements

| Priority / module | Required behavior |
| --- | --- |
| P0 / Discover | Search countries, territories, states, cities, islands and attractions; resolve aliases and ambiguous names. |
| P0 / Destination profile | Show climate, seasons, activities, airports, local logistics, safety, news and source timestamps. |
| P0 / Compare | Compare dates, weather, crowds, cost evidence and traveler preferences; show missing data. |
| P0 / Monitor | Save trips and destinations; deliver weekly briefings and urgent relevant alerts with opt-in controls. |
| P1 / Plan | Generate editable itineraries, packing lists and budget ranges; validate opening hours and transfers. |
| P1 / Entry and health | Nationality-specific entry guidance and official health information with validity and source links. |
| P1 / Assistant | Grounded destination Q&A, adaptive planning and offline trip summaries. |
| P2 / Ecosystem | Mobile expansion, creator contributions, affiliate marketplace and partner APIs. |
| P0 / Seasonal explorer | Interactive atlas, environmental conditions, activity windows and explainable ranking. |
| P1 / Trip companion | Reservation imports, flight tracking, readiness and trip dependency graph. |
| P1 / Local intelligence | Neighborhood and accommodation assessments, mapped incidents and practical guidance. |
| P2–P3 / Trust and care | Verified providers, travel circles and qualified assistance partners; defer sensitive document vault and social network. |

### Scope and success measures

Initial release: responsive web, English, curated destinations with verified coverage. Native apps and bookings follow evidence of demand. Proposed targets: 95% search success on a curated test set; 100% source attribution for critical claims; 50% reduction in research time in usability trials; 15% destination-to-saved-trip conversion. These are hypotheses, not benchmarks.

### Non-goals

Do not operate a travel agency, guarantee safety, issue visas, predict weather independently, or autonomously purchase or cancel bookings. Do not claim worldwide completeness at launch.

## 4. High-level system architecture

Use a modular application backend with separate ingestion and background workers. Keep domain interfaces stable so workloads can later be separated without redesigning the product.

| Layer | Proposed components |
| --- | --- |
| Experience | Next.js / TypeScript web; Expo mobile later; administrative review console. |
| Edge | CDN, WAF, API gateway, OIDC identity, rate limiting. |
| Application | FastAPI modules: destinations, climate, safety, news, transport, trips, recommendations, notifications. |
| Intelligence | Deterministic ranking, retrieval, constrained LLM workflows, verification and policy checks. |
| Knowledge | PostgreSQL + PostGIS; pgvector where useful; Redis cache; object storage for permitted raw payloads. |
| Ingestion | Scheduled connectors, Dagster or managed scheduler, durable queue, normalization and quality workers. |
| Operations | Docker, Terraform, CI/CD, OpenTelemetry, secrets manager, backups and alerts. |
| V2 intelligence | Temporal facts, trip graph, geospatial event matching, constraint solver, notification orchestration. |
| V2 trust | Consent, moderation, provider verification registry and partner gateway. |

### Data and control flow

Providers → ingestion queue → raw storage → validation / entity resolution → canonical facts → transactional outbox → search/cache projections → API and AI retrieval → web/mobile. Trip subscriptions consume verified event changes through a separate relevance and delivery worker.

### Trade-offs

PostgreSQL is the system of record; search and vector indexes are rebuildable projections. Avoid Kafka, Kubernetes and a dedicated graph database until throughput, query complexity or isolation warrants them. Select AWS or Azure after cost and operational evaluation. Separate ingestion credentials from serving credentials.

## 5. Destination knowledge model

Represent geography as a typed graph over stable identifiers, not a single rigid tree. French Polynesia contains archipelagos and islands; Tahiti contains Papeete, while airports serve multiple destinations. Administrative and tourism boundaries may overlap.

| Entity | Key attributes / relationships |
| --- | --- |
| Destination | UUID, type, localized names, aliases, geometry, timezone, external IDs; contained_in, overlaps, near. |
| Airport / POI / Route | Coordinates, codes, categories, serves, connects, operator, schedule validity. |
| ClimateNormal / TourismSeason | Location, month, reference period, temperature, rainfall, demand evidence. |
| Advisory / CrimeStatistic | Issuer, scope geometry, category, methodology, denominator, effective interval. |
| NewsArticle / TravelEvent | Source, publication time, event time, affected geometry, category, status, evidence links. |
| Fact / Evidence / Source | Subject, predicate, typed value, units, source ID, retrieval time, validity, review state, license. |
| Trip / Preference / Subscription | User ID, destination IDs, travel dates, interests, consent and delivery preferences. |
| TripSegment / Reservation / Dependency | Time windows, status, upstream/downstream links, confirmation evidence. |
| EnvironmentalObservation / ActivityWindow | AQI standard, UV, humidity, marine conditions, seasonal activity evidence. |
| Provider / Verification / Experience | Credential scope and expiry, creator rights, visit date, expense currency and evidence. |
| Consent / Alert / Delivery | Purpose, audience, expiry, event version, deduplication key and delivery state. |

### Temporal and provenance rules

Maintain observed_at, retrieved_at, valid_from, valid_to and recorded_at separately. Preserve historical versions; never overwrite conflicting advisories from different jurisdictions. Use unique provider IDs and canonical UUID mappings. Spatial indexes support point-in-polygon and distance queries; explicit relationship edges support multi-hop navigation.

A recommendation is a derived assertion with input fact IDs, algorithm version and explanation. Unverified or expired critical facts must not be presented as current. Crime data must retain reporting period and methodology; do not invent comparable safety scores.

## 6. Data ingestion and intelligence

| Domain / candidate source | Proposed refresh target |
| --- | --- |
| Geography: GeoNames, OSM, Wikidata | Monthly or dataset release |
| Climate: ERA5, NOAA, Open-Meteo | On revision; retain reference periods |
| Forecast: Open-Meteo, local agencies | 1–3 hours, within provider limits |
| Safety: State Department, FCDO, GDACS | 5–15 minutes where supported; urgent events prioritized |
| News: GDELT, licensed feeds, local RSS | 15–60 minutes for relevant events; weekly user digest |
| Airports / transit: OurAirports, GTFS | Daily to monthly depending on dataset |
| Entry: immigration authorities, Timatic | Daily or on detected changes |
| Crime / tourism: official statistics | On publication; never fabricate missing coverage |
| Environment / aviation | AQI and UV hourly where supported; flight events via licensed feed. |
| Provider / community | On submission and expiry; moderation before publication. |

### Pipeline contract

Each connector emits provider ID, source URL, fetch time, content hash, schema version and licensing metadata. Use incremental cursors, bounded retries, backoff, idempotent writes and dead-letter queues. Validate units and timestamps; resolve geography; cluster duplicate news into events; quarantine ambiguous or contradictory critical records. Publish validated changes atomically with an outbox event.

### Freshness and failure behavior

Track last successful retrieval and source-specific expiry. Serve last-known data with a visible stale label where safe; suppress expired critical assertions and link to official sources. Reprocess corrected records and issue alert corrections. Measure ingestion lag, coverage, failure rate and duplicate rate. Provider access, licensing and commercial costs remain unverified.

## 7. AI and agentic architecture

Use bounded workflows rather than autonomous agents with broad privileges. The orchestrator classifies intent, resolves destination IDs, retrieves structured facts and relevant evidence, then invokes domain tools and verifies the output.

| Workflow | Implementation |
| --- | --- |
| Seasonality | Multi-objective ranking of climate, crowds, price and activities; explain trade-offs and missing inputs. |
| News and safety | Extract and cluster events; match geometry and travel dates; prioritize official sources and severity. |
| Itinerary | Generate candidate activities; validate opening hours, travel time, budget and accessibility constraints. |
| Travel assistant | Hybrid retrieval filtered by geography, validity and source trust; cited answers and abstention. |
| Monitoring | Event-driven relevance scoring, deduplication, consent checks and delivery; weekly summaries. |
| Data quality | Detect anomalies, stale facts and conflicting sources; route critical cases to human review. |
| Trip impact | Traverse time-bounded dependencies; propose alternatives, never change bookings automatically. |
| Readiness / simulator | Deterministic rules and cost ranges; distinguish completed tasks from travel eligibility. |

### Example: Bali trip monitoring

A volcanic activity report is ingested, geocoded and matched to official hazard or aviation information. The system determines which saved trips overlap the affected area and time window. A verified, relevant event generates an alert with source, timestamp and practical next steps. Unconfirmed claims are labeled or held; corrections supersede prior alerts.

### Evaluation and guardrails

Build a golden dataset for geography, seasonality, visa and safety questions, itinerary feasibility and alert relevance. Test citation entailment, freshness, hallucination, prompt injection, tool permissions and multilingual ambiguity. Require deterministic checks for critical claims; models cannot invent emergency numbers, entry rules or forecasts. Version prompts and models; enforce token, cost and execution limits.

## 8. APIs, security and reliability

| Endpoint (illustrative) | Contract |
| --- | --- |
| GET /v1/destinations?q= | Ranked canonical IDs, aliases and disambiguation context. |
| GET /v1/destinations/{id} | Profile, fact provenance, coverage and freshness. |
| GET /v1/destinations/{id}/events | Paginated, time-filtered relevant events. |
| POST /v1/comparisons | Destination IDs, dates, preferences; ranked evidence and trade-offs. |
| POST /v1/trips | Authenticated trip creation; idempotency key. |
| POST /v1/trips/{id}/itineraries | Async generation job; validated result and citations. |
| PATCH /v1/trips/{id}/subscription | Owner-only notification consent and cadence. |
| GET /v1/explore?month= | Filtered destination candidates, coverage and explained ranking. |
| POST /v1/trips/{id}/imports | Consent-scoped reservation extraction; user confirmation. |
| GET /v1/trips/{id}/impacts | Versioned affected segments, evidence and suggested actions. |
| POST /v1/scenarios | Cost ranges, assumptions and alternative dates. |
| GET /v1/destinations/{id}/areas | Spatially scoped observations, coverage and uncertainty. |

### Security and privacy

Enforce object-level authorization on trips; encrypt transport and storage; use workload identity and least privilege. Treat external articles as untrusted input; restrict connector egress and protect against SSRF and prompt injection. Avoid storing passport numbers or exact location unless necessary. Provide export, deletion, retention limits and audit trails; redact sensitive logs. Review applicable privacy, copyright and travel liability obligations.

### Proposed service objectives

99.9% serving availability; P95 cached profile under 300 ms and search under 500 ms at an agreed test load; RPO 1 hour and RTO 4 hours. AI requests use streaming or async jobs with bounded timeouts. Monitor queue lag, freshness, delivery failures and cost per active trip. Use retries, circuit breakers, backups and restore drills. WCAG 2.2 AA is the accessibility target.

## 9. Business strategy and roadmap

### Commercial model

Free destination research and basic safety information; test premium planning and monitoring subscriptions (see section 18 for revised pricing hypotheses) and a per-trip pass. Later add disclosed affiliate referrals and licensed B2B APIs. Never paywall basic critical safety guidance or allow commissions to distort rankings.

Acquire early users through Journey with Ris, useful search-indexed destination pages, creator partnerships and customer referrals. Target 20 candidate markets, subject to coverage gates in section 16.

| Checkpoint | Deliverable / exit condition |
| --- | --- |
| A–C | Discovery, platform and geographic knowledge |
| D–F | Environmental, safety and discovery intelligence |
| G–I | Planning, trip monitoring and hyperlocal intelligence |
| J–N | Community, trust, assistance, commercialization and predictive intelligence |

Roadmap is milestone-based, not a fixed short-term MVP deadline. Keep the long-term global architecture extensible while limiting initial operational scope. The expanded A–N roadmap in section 15 supersedes the original A–G summary.

## 10. Acceptance gates and open decisions

### Release acceptance

Unit, integration and end-to-end tests cover canonical identity, temporal facts, source outages, replay and idempotency. Security tests cover cross-user access, injection, secrets and connector egress. Critical claims must carry valid evidence; alert tests must cover duplicates, cancellation and correction. Load and recovery tests must demonstrate agreed SLOs before production expansion.

| Risk / open decision | Required resolution |
| --- | --- |
| Brand | DestinaIQ is a working name; trademark, domain and app-store clearance pending. |
| Market differentiation | Hands-on competitor testing and customer validation pending. |
| Data rights and cost | Verify contracts, attribution, retention, redistribution and commercial use for each source. |
| Safety liability | Define escalation, review, disclaimers and correction policy with appropriate legal review. |
| Cloud and budget | Choose hosting after estimating traffic, provider fees, AI cost and operational capacity. |
| Coverage and ranking | Approve pilot locations, coverage thresholds and evidence-based ranking methodology. |
| Operating ownership | Assign on-call, data stewardship and incident response before public release. |

### Decision record

Proposed ADRs: canonical PostgreSQL store; modular monolith with isolated workers; temporal provenance; provider-neutral AI; no arbitrary crime score; event-driven monitoring; web-first launch. These are recommendations, not approved decisions.

### Next action

Complete Checkpoint A and convert this design into version-controlled PRD, data contracts, threat model, provider registry and architecture decision records. Revisit this document after discovery and before implementation.

## 11. Competitive gap analysis

V2 incorporates the prior public-offering comparison, not independently tested product capabilities. Absence of public evidence is not evidence of absence. DestinaIQ remains a proposed product; breadth is not proof of superiority.

| Competitor / strength | Gap addressed in V2 | DestinaIQ proposed broader scope |
| --- | --- | --- |
| Travel Intel — seasonal atlas, AQI, travel scoring | Atlas, environmental data, explainable suitability, activity windows | Trip monitoring, logistics, readiness and itinerary optimization |
| TripGuard AI — provider trust and document sharing | Credential checks, verified reviews, total pricing; defer document vault | Temporal destination intelligence, climate and event correlation |
| Aurora Travel — experiences and community | Creator videos, location-linked experiences, reported costs; defer messaging | Structured provenance, seasonality, trip dependency modeling |
| Sitata — protection and assistance | Reservation imports, flight status, check-ins; partner-led care | Discovery, comparisons, activity seasons and planning |
| WARNPOINT — risk monitoring | Daily briefings, advisory comparisons, incident maps, quiet hours | Broader discovery, budgeting and itinerary optimization |
| Outroad — hyperlocal risk | Neighborhood and hotel-area assessments, scams and route disruption | Climate, global planning and experience intelligence |

Benchmark protocol: run identical destination/date and saved-trip scenarios; record coverage, source dates, correctness, usability, alert relevance, pricing and limitations. Test French Polynesia, Bali and a multi-city journey. Validate willingness to pay through interviews and prototype trials.

Reference websites supplied for the comparison: travelintel.tech; tripguardai.com; auroratravelapp.com; sitata.com; warnpoint.com/trip-watch; getoutroad.com. No new live verification was performed for this revision.

## 12. Enhanced product domains

| Domain | Responsibility |
| --- | --- |
| Destination IQ | Canonical geography, profiles and practical living |
| Season IQ | Climate, AQI, seasonal atlas and activity windows |
| Safety IQ | Advisories, incidents, scams and neighborhood evidence |
| Pulse IQ | News, event correlation, history and briefings |
| Plan IQ | Itineraries, constraint optimization and trip graph |
| Transit IQ | Airports, flights, ferries, transfers and disruptions |
| Budget IQ | Cost ranges, comparisons and what-if scenarios |
| Experience IQ | Attractions, creator experiences and expense reports |
| Ready IQ | Packing, entry rules and preparation checklist |
| Care IQ | Health guidance, emergency contacts and partners |
| Circle IQ | Consent-based shared trips and check-ins |
| Trust IQ | Provider credentials, reviews and provenance |

These are logical domain boundaries, not twelve separately deployed services or required consumer brands. P0 is foundational, P1 advanced consumer intelligence, P2 ecosystem, P3 deferred strategic scope. The numbered catalog below preserves the prior 30 requirements and adds 44 proposed requirements.

## Requirements catalog | Baseline FR-001–030

| ID | Required capability |
| --- | --- |
| FR-001 | Search destinations |
| FR-002 | Resolve aliases and ambiguous names |
| FR-003 | Structured destination profiles |
| FR-004 | Monthly climate statistics |
| FR-005 | Peak, shoulder and low seasons |
| FR-006 | Personalized travel windows |
| FR-007 | Relevant news and events |
| FR-008 | Multi-government advisories |
| FR-009 | Contextual crime statistics |
| FR-010 | Safety and scam guidance |
| FR-011 | Attractions and experiences |
| FR-012 | Airport gateways |
| FR-013 | Transport connections |
| FR-014 | Destination comparisons |
| FR-015 | Saved destinations and dates |
| FR-016 | Personalized itineraries |
| FR-017 | Packing checklists |
| FR-018 | Nationality-specific entry guidance |
| FR-019 | Budget estimates |
| FR-020 | Relevant notifications |
| FR-021 | Weekly briefings |
| FR-022 | Natural-language questions |
| FR-023 | Sources and timestamps |
| FR-024 | Stale/conflicting information detection |
| FR-025 | Offline trip summaries |
| FR-026 | Accuracy reporting |
| FR-027 | Adaptive itineraries |
| FR-028 | Administrative review |
| FR-029 | Data export and deletion |
| FR-030 | Multilingual and multicurrency support |

## Requirements catalog | P0 — FR-031–042

| ID | Required capability |
| --- | --- |
| FR-031 | Interactive seasonal atlas |
| FR-032 | Month-based discovery |
| FR-033 | AQI and environmental intelligence |
| FR-034 | Explainable suitability ranking |
| FR-035 | Activity-specific seasonal intelligence |
| FR-036 | Geospatial incident mapping |
| FR-037 | Government advisory comparisons |
| FR-038 | Historical intelligence |
| FR-039 | Dynamic briefing cadence |
| FR-040 | Trip-relevant event correlation |
| FR-041 | Quiet hours and notification controls |
| FR-042 | Practical local living intelligence |

## Requirements catalog | P1 — FR-043–056

| ID | Required capability |
| --- | --- |
| FR-043 | Neighborhood intelligence |
| FR-044 | Know Your Stay accommodation assessment |
| FR-045 | Reservation confirmation import |
| FR-046 | Flight status and gate tracking |
| FR-047 | Travel Digital Twin |
| FR-048 | Destination What-If Simulator |
| FR-049 | Travel Readiness Center |
| FR-050 | Constraint-based itinerary optimization |
| FR-051 | Verified creator contributions |
| FR-052 | Location-linked videos |
| FR-053 | Traveler-reported expenses |
| FR-054 | Community scam/disruption reports |
| FR-055 | Personal traveler profiles |
| FR-056 | Printable intelligence reports |

## Requirements catalog | P2 — FR-057–066

| ID | Required capability |
| --- | --- |
| FR-057 | Verified provider marketplace |
| FR-058 | Credential verification |
| FR-059 | Confirmed-trip reviews |
| FR-060 | Transparent total pricing |
| FR-061 | Travel Circle and shared itineraries |
| FR-062 | Voluntary safety check-ins |
| FR-063 | Insurance partner integration |
| FR-064 | Telemedicine and assistance partners |
| FR-065 | Creator monetization |
| FR-066 | Enterprise intelligence APIs |

## Requirements catalog | P3 — FR-067–074

| ID | Required capability |
| --- | --- |
| FR-067 | Encrypted document vault |
| FR-068 | Revocable identity document sharing |
| FR-069 | Document access audit |
| FR-070 | Community groups |
| FR-071 | Private messaging |
| FR-072 | Traveler meetups |
| FR-073 | Predictive travel analytics |
| FR-074 | Partner-operated rebooking assistance |

## 13. Detailed V2 subsystem design

### Seasonal explorer and simulator

Rank by month, weather, crowds, budget and activity conditions using versioned inputs. Expose weights, missing data and trade-offs. Separate safety and entry constraints from suitability. Cost scenarios use ranges, currency, dates, taxes and occupancy assumptions; never imply a booking quote.

### Travel Digital Twin

Represent reservations, segments, activities and transfers as a directed dependency graph with UTC instants and local time zones. On verified event changes, intersect affected geometry and time, traverse impacted dependencies and calculate connection slack. Handle cycles and unknown schedules explicitly. Present proposed alternatives and require approval for external actions.

### Hyperlocal intelligence

Use PostGIS boundaries and route intersections; attach evidence, reporting period and coverage to every assessment. Do not infer neighborhood risk from demographics or extrapolate missing statistics. Know Your Stay combines hotel-area observations, transport, accessibility and nearby services.

### Briefing and notification engine

At launch use weekly briefings and urgent verified alerts. From V1.2, default weekly beyond 30 days, twice weekly at 8–30 days, daily within 7 days and during travel. Resolve boundary days consistently (daily at 7 days). Urgent verified events use separate consent-aware delivery rules. Deduplicate by event version and trip, respect quiet hours, support corrections and stop monitoring after return.

### Reservation imports and readiness

Accept forwarded confirmations or explicitly authorized integrations. Extract structured fields, validate dates and require user confirmation; retain minimal raw content. Readiness tracks reviewed tasks, not guaranteed entry or safety.

### Experience and provider trust

Record creator rights, visit date, location, expense currency and moderation status. Verification is scoped to evidence, issuer, check date and expiry; never a safety guarantee. Confirmed reviews require transaction evidence. Disclose total price and commercial relationships.

## 14. Security, data and evaluation

### Consent and partner boundary

Travel Circle uses explicit audience, purpose and expiry; revocation stops future access. No background location by default. Defer passport storage until threat model, encryption/key management, deletion and legal review pass. Insurance, medical care and evacuation are partner-operated; no in-house underwriting, claims adjudication or medical service.

### Data contracts and operations

Add event version, affected geometry, effective interval, source reliability, correction link and license to the canonical event contract. Use transactional outbox and idempotent consumers; retry with bounded backoff. Separate user trip data from public knowledge. Monitor source lag, false alerts, correction latency, delivery and cost per monitored trip.

### AI and optimization

Use deterministic rules for entry and safety facts, geospatial algorithms for distance, constraint optimization for scheduling, and bounded LLM workflows for extraction and explanation. Require source-backed claims, tool allowlists, prompt-injection tests and human escalation for ambiguous critical facts.

### V2 acceptance tests

Atlas rankings explain input changes and missing data; serious advisories cannot be averaged away. Synthetic delayed-flight scenarios identify downstream impacts without modifying bookings. Neighborhood queries return unknown when coverage is insufficient. Reservation extraction requires confirmation; cross-user access and revoked sharing fail. Alerts deduplicate, honor preferences and propagate corrections. Provider expiry removes verification status.

### Business and operational constraints

Test per-trip passes, subscriptions and disclosed affiliate referrals. Creator and provider networks require moderation and dispute workflows. Validate data rights, pricing, availability and regional coverage before integration. Keep critical safety guidance free. Track cost per active trip and willingness to pay before expanding paid data sources.

## 15. Revised engineering checkpoints

| Gate | Exit condition |
| --- | --- |
| A — Discovery | Competitor tests, interviews, name clearance and provider feasibility approved. |
| B — Platform | Secure CI/CD, migrations, identity, telemetry and recovery tests. |
| C — Geography | Canonical IDs, temporal evidence and spatial search verified. |
| D — Environment | Climate, AQI and activity season pipelines meet freshness and coverage targets. |
| E — Safety and news | Event clustering, advisory comparisons, corrections and incident maps tested. |
| F — Discovery | Atlas, comparisons and explainable ranking validated with users. |
| G — Planning | Grounded itineraries, simulator and readiness pass feasibility tests. |
| H — Trip monitoring | Imports, flight events, dependency graph and alert delivery tested. |
| I — Hyperlocal | Neighborhood and hotel-area assessments pass coverage and bias review. |
| J — Experiences | Creator rights, moderation and expense provenance operational. |
| K — Provider trust | Credential expiry, reviews and transparent pricing verified. |
| L — Care and Circle | Consent, revocation and qualified partner contracts validated. |
| M — Commercial | Pricing experiments, payment controls and enterprise API economics validated. |
| N — Expansion | Predictive models calibrated; deferred features justified by demand and risk review. |

A–N is the authoritative V3 roadmap; milestones are acceptance-driven, not fixed deadlines. Dependencies may be delivered in vertical slices, with P0 data quality and safety gates preceding public expansion.

Revision decisions: retain web-first, modular monolith and PostgreSQL/PostGIS; add 12 logical domains and 44 requirements. Cloud, provider contracts, staffing, pricing, geographic coverage and brand clearance remain open. V3 is a proposal, not a claim of implemented functionality.

## 16. Launch scope and release strategy

V3 supersedes V2 for release assignment, pricing and gates. Strategic priority is independent of release. The first release is responsive English-language web, with 15 customer-facing capabilities plus mandatory security, provenance, administration and privacy controls. No paid flight feed, mailbox access, neighborhood risk rating or marketplace is required at launch.

| Launch ID | Capability | FR mapping |
| --- | --- | --- |
| L01 | Search and aliases | 001,002 |
| L02 | Destination profiles | 003,023,024 |
| L03 | Monthly climate | 004 |
| L04 | Weather forecasts | 003 (expanded) |
| L05 | Tourism seasons | 005 |
| L06 | Best travel windows | 006 |
| L07 | Compare up to four destinations | 014 |
| L08 | Official advisories | 008 |
| L09 | Relevant news | 007 |
| L10 | Attractions | 011 |
| L11 | Airports and transport; basic parking where sourced | 012,013 |
| L12 | Practical travel essentials | 042 |
| L13 | Saved destinations and dates | 015 |
| L14 | Weekly briefings and urgent alerts | 020,021,040,041 |
| L15 | Basic grounded itineraries | 016 |

Launch support controls: FR-026, 028 and 029 are mandatory. Forecasts are explicitly added to FR-003 without renumbering existing IDs. Basic parking is a sourced field in FR-013; dedicated parking search follows later. No unsupported claim may be filled by an LLM.

### Release assignments

| Product release | Scope |
| --- | --- |
| V1.0 | Destination intelligence and launch controls above. |
| V1.1 | Seasonal atlas, environment, activity windows, packing, budget, entry guidance, Q&A, readiness, simulation. |
| V1.2 | Manual reservations then consented imports, flight tracking, digital twin, adaptive planning, daily briefings. |
| V1.3 | Hyperlocal intelligence, incident maps, parking, local scam reporting; only where coverage passes. |
| V2.0 | Creator and provider networks, travel circle, assistance partners, enterprise APIs, native apps subject to demand. |
| V3.0 | Predictive intelligence, deferred document and social features only after separate approval. |

### Coverage gate

Candidate markets (not commitments): French Polynesia, Maldives, Seychelles, Mauritius, UAE, Singapore, Japan, Thailand, Indonesia, Egypt, Qatar, Turkey, Greece, Italy, Switzerland, France, United Kingdom, Hawaii, Puerto Rico, Mexico. Maintain separate searchable and fully supported catalogs. For each launched market require canonical geography, sourced climate and forecast, advisory authority, attractions, airport/transport and practical essentials; verify licensing and freshness. News may explicitly report no verified recent items. Unsupported categories return unknown, not safe. Publish coverage status per category; exclude markets failing mandatory coverage. Neighborhood safety is deferred to V1.3 and requires local evidence, reporting methodology, bias review and geographic precision.

## 17. Competitive validation

Checkpoint A.1: independently test Travel Intel, TripGuard AI, Aurora, Sitata, WARNPOINT and Outroad using the same scenarios, account tier and dates where feasible. Record screenshots, timestamps, source links, observed output, pricing, limitations and unavailable access. Do not treat marketing claims or inaccessible paid features as verified gaps.

| Scenario | Test focus |
| --- | --- |
| French Polynesia in August | Island coverage, seasonality |
| Dubai luxury trip | Attractions, transport, cost |
| Japan cherry blossom | Activity-specific timing |
| Bali seven days | Itinerary feasibility |
| Multi-stop trip | Reservation dependencies |
| Known disruption | Alert relevance and latency |
| Unfamiliar hotel | Local coverage and uncertainty |
| Budget traveler | Affordability and personalization |

Score each category 0–5 with evidence: accuracy 20%, coverage 15%, freshness 15%, personalization 10%, completeness 10%, UX 10%, transparency 10%, value 5%, performance 5%. Mark inaccessible tests N/A; disclose tested weight and do not rank incomparable totals. Exit: six documented attempts, evidence-backed gap matrix, access blockers recorded, and launch scope re-approved. No hands-on tests have yet been performed.

## 18. Unit economics and pricing

Illustrative USD assumptions only; obtain vendor quotes and measure usage before charging. Monthly subscriber contribution = price minus allocated data, infrastructure, AI, flight monitoring, support/delivery and payment fees. Payment assumption 2.9% + $0.30 per transaction; app-store fees, taxes, refunds, free-tier subsidy, acquisition and engineering payroll excluded from the table.

| Scenario | Price | AI/data/infra/flight/support | Cost | Contribution |
| --- | --- | --- | --- | --- |
| Launch light | 9.99 | 0.5/1/0.5/0/0.5 | 3.09 | 6.90 (69%) |
| Connected base | 14.99 | 1/1.5/0.75/2/0.5 | 6.48 | 8.51 (57%) |
| Heavy usage | 14.99 | 3/3/1.5/6/1 | 15.23 | -0.24 (-2%) |
| Trip pass example | 9.99 | 0.75/1.5/0.75/2/0.5 | 6.09 | 3.90 (39%) |

Trip pass assumes one bounded trip, not unlimited monthly service. Test free Explorer, $9.99–19.99 trip pass, $14.99 Plus and $24.99 Pro; enterprise custom. Prior $6.99 trip / $9.99 monthly hypotheses are superseded, not validated. Calculate shared fixed costs per active user, free-tier subsidy per payer, and provider minimums at 1k/10k/100k active users. Require positive contribution under expected usage and proposed ≥60% contribution margin target before scaling paid acquisition; heavy-use negative scenarios require caps, pricing or provider changes. Keep critical safety guidance free.

Cost controls: cache shared destination briefings, reuse event clusters, batch retrieval, cap model tokens and paid API polling, deduplicate alerts, meter per trip and tenant, set budget alarms and circuit breakers. Flight feeds and daily briefings require a separate V1.2 cost gate. Collect per-provider quote, licensing rights, rate limits, minimum commitments, retention and geographic coverage.

## 19. Reservation privacy architecture

V1.2 sequence: manual entry → user-selected upload → unique forwarding address → optional Gmail/Outlook OAuth only after approval. No continuous mailbox monitoring by default. Do not request full mailbox access where narrower methods suffice. Provider verification/security assessments depend on scopes and handling; assess applicable GDPR, state privacy law and contractual requirements with counsel.

Flow: consented input → isolated quarantine and malware scan → bounded extraction treating content as untrusted → field minimization → user confirmation → encrypted reservation record → trip dependency graph. Strip payment card and passport data; do not send raw email to general-purpose model providers without approved processing terms. Use per-user authorization, short-lived upload URLs, isolated workers, encrypted tokens, revocation, redacted logs and audit events.

Proposed retention: raw confirmations deleted within 24 hours after successful confirmation, failed/unconfirmed uploads within 7 days; structured records retained until user deletion or approved retention expiry. Backup expiry target 30 days; document exceptions and legal holds. Export and deletion requests tracked, with proposed completion within 30 days subject to applicable law. Test deletion across primary storage, indexes and queued jobs; restore must reapply deletion tombstones.

Release gate: data inventory and lawful basis, privacy impact assessment where required, processor agreements, transfer assessment where applicable, scope review, provider approval if required, threat model, incident response and penetration tests. Verify cross-user isolation, malicious attachments, prompt injection, token revocation and retention jobs. No OAuth release until gate passes.

## 20. Parking intelligence

Transit IQ adds parking facilities, location, operator, type, hours, price/currency, restrictions, accessible spaces, EV charging, source and observed/expiry timestamps. Link facilities to airports, hotels and attractions via PostGIS. Never infer availability from capacity or stale feeds. Basic sourced parking notes may ship in L11; advanced features are V1.3. Live availability requires a licensed feed and explicit freshness SLA.

| ID | Capability |
| --- | --- |
| FR-075 | Parking discovery |
| FR-076 | Prices, hours and restrictions |
| FR-077 | Airport parking and transfers |
| FR-078 | Accessible parking and EV charging |
| FR-079 | Parking-aware driving itineraries |
| FR-080 | Live parking availability |

## 21. Requirement acceptance register

All 80 stable IDs retain their V2 meaning except the explicit FR-003 forecast extension and six new parking IDs. Release assignment below is authoritative. Each criterion is a minimum testable exit condition; all requirements additionally require automated positive/negative tests, documentation, telemetry where relevant, and security review. Dependencies are grouped by domain; no feature ships until its upstream data and controls pass.

### FR-001–010

| ID | Capability | Release | Acceptance test |
| --- | --- | --- | --- |
| FR-001 | Search destinations | 1.0 | Search exact and alias fixtures; ≥95% top-5 recall on curated set. |
| FR-002 | Resolve aliases and ambiguous names | 1.0 | Ambiguous names return distinct candidates with region labels; no silent selection. |
| FR-003 | Structured destination profiles | 1.0 | Profile displays source-backed required fields and forecast timestamp; expired forecast marked stale or withheld. |
| FR-004 | Monthly climate statistics | 1.0 | All 12 months show units and reference period or explicit missing status. |
| FR-005 | Peak, shoulder and low seasons | 1.0 | Season labels include evidence and rationale; unsupported months unknown. |
| FR-006 | Personalized travel windows | 1.0 | Changing month or preference changes ranking on deterministic fixture; explain trade-offs. |
| FR-007 | Relevant news and events | 1.0 | Duplicate articles cluster into one event; unrelated geography excluded. |
| FR-008 | Multi-government advisories | 1.0 | Show issuer, source and dates; conflicting advisories separate; expired critical claims withheld. |
| FR-009 | Contextual crime statistics | 1.3 | Crime figures retain period, denominator and methodology; incomparable data not ranked. |
| FR-010 | Safety and scam guidance | 1.3 | Scam guidance cites local evidence; unsupported claims return unknown. |

### FR-011–020

| ID | Capability | Release | Acceptance test |
| --- | --- | --- | --- |
| FR-011 | Attractions and experiences | 1.0 | Attractions show canonical location and source; unknown hours labeled. |
| FR-012 | Airport gateways | 1.0 | Airport codes resolve to correct gateways on fixture; distinguish serving vs located in. |
| FR-013 | Transport connections | 1.0 | Transport modes and sourced parking notes shown; unknown fares/times labeled. |
| FR-014 | Destination comparisons | 1.0 | Compare 2–4 destinations with common units and missing values; reject fifth. |
| FR-015 | Saved destinations and dates | 1.0 | Save/edit/delete dates; cross-user access denied. |
| FR-016 | Personalized itineraries | 1.0 | Generate editable itinerary; reject known closed hours and impossible transfers; unknowns flagged. |
| FR-017 | Packing checklists | 1.1 | Packing changes with trip conditions; user can edit and check items. |
| FR-018 | Nationality-specific entry guidance | 1.1 | Entry result uses nationality, transit and dates; source and validity shown; unknown if unsupported. |
| FR-019 | Budget estimates | 1.1 | Budget shows currency, dates, occupancy and range; no quote implied. |
| FR-020 | Relevant notifications | 1.0 | Verified relevant urgent event triggers one alert per trip/version; irrelevant event suppressed. |

### FR-021–030

| ID | Capability | Release | Acceptance test |
| --- | --- | --- | --- |
| FR-021 | Weekly briefings | 1.0 | Weekly digest sent once per opted-in trip/week; stops after return. |
| FR-022 | Natural-language questions | 1.1 | Answers cite retrieved evidence; unsupported critical query abstains. |
| FR-023 | Sources and timestamps | 1.0 | Every critical claim has source ID and timestamp; missing evidence blocks publication. |
| FR-024 | Stale/conflicting information detection | 1.0 | Stale/conflicting fixtures visibly labeled; critical expired facts suppressed. |
| FR-025 | Offline trip summaries | 1.1 | Offline summary opens without network and shows last sync date. |
| FR-026 | Accuracy reporting | 1.0 | Report creates tracked review item; reporter receives reference. |
| FR-027 | Adaptive itineraries | 1.2 | Disruption proposes alternatives without modifying bookings. |
| FR-028 | Administrative review | 1.0 | Reviewer can approve/reject quarantined fact; decision audit recorded. |
| FR-029 | Data export and deletion | 1.0 | Export includes user records; deletion removes active copies and queues backup expiry. |
| FR-030 | Multilingual and multicurrency support | 1.1 | Locale and currency fixtures preserve units, original value and rate timestamp. |

### FR-031–040

| ID | Capability | Release | Acceptance test |
| --- | --- | --- | --- |
| FR-031 | Interactive seasonal atlas | 1.1 | Atlas filters month and climate; unsupported regions visibly marked. |
| FR-032 | Month-based discovery | 1.1 | Month filter returns only eligible supported destinations; rationale shown. |
| FR-033 | AQI and environmental intelligence | 1.1 | AQI shows standard, observation time and source; stale readings labeled. |
| FR-034 | Explainable suitability ranking | 1.1 | Ranking exposes inputs and weights; serious advisory cannot be averaged away. |
| FR-035 | Activity-specific seasonal intelligence | 1.1 | Activity window includes evidence and uncertainty; missing season unknown. |
| FR-036 | Geospatial incident mapping | 1.3 | Incident map uses verified geometry and time; uncertain location not shown as precise pin. |
| FR-037 | Government advisory comparisons | 1.3 | Compare at least two available authorities without merging conflicting advice. |
| FR-038 | Historical intelligence | 1.3 | Historical query returns correct as-of versions and reporting caveats. |
| FR-039 | Dynamic briefing cadence | 1.2 | Boundary tests: >30 weekly, 8–30 twice weekly, ≤7 daily; stop after return. |
| FR-040 | Trip-relevant event correlation | 1.0 | Spatial and temporal overlap matches relevant trip; unrelated event suppressed. |

### FR-041–050

| ID | Capability | Release | Acceptance test |
| --- | --- | --- | --- |
| FR-041 | Quiet hours and notification controls | 1.0 | Quiet hours respected for nonurgent alerts; urgent override requires consent. |
| FR-042 | Practical local living intelligence | 1.0 | Practical facts include local source and date; missing values explicit. |
| FR-043 | Neighborhood intelligence | 1.3 | Neighborhood assessment returns unknown below coverage threshold; no demographic proxy. |
| FR-044 | Know Your Stay accommodation assessment | 1.3 | Hotel-area report distinguishes distance, access and evidenced risk; unknowns visible. |
| FR-045 | Reservation confirmation import | 1.2 | Extract selected confirmation fields; user confirms; raw deletion and isolation tested. |
| FR-046 | Flight status and gate tracking | 1.2 | Flight update matches flight/date; stale feed labeled; duplicates suppressed. |
| FR-047 | Travel Digital Twin | 1.2 | Delayed-flight fixture identifies downstream dependencies; cycles handled; no booking changes. |
| FR-048 | Destination What-If Simulator | 1.1 | Scenario changes dates/occupancy and recalculates ranges with assumptions. |
| FR-049 | Travel Readiness Center | 1.1 | Checklist generated from trip facts; completion not presented as safety or entry guarantee. |
| FR-050 | Constraint-based itinerary optimization | 1.2 | Optimizer respects hard constraints; infeasible case returns explanation. |

### FR-051–060

| ID | Capability | Release | Acceptance test |
| --- | --- | --- | --- |
| FR-051 | Verified creator contributions | 2.0 | Creator contribution records rights, visit date and moderation status before publication. |
| FR-052 | Location-linked videos | 2.0 | Video links to canonical location; rights revocation removes access. |
| FR-053 | Traveler-reported expenses | 2.0 | Expense records include currency, date and category; aggregation excludes invalid records. |
| FR-054 | Community scam/disruption reports | 1.3 | Report enters moderation; unverified report not promoted to critical alert. |
| FR-055 | Personal traveler profiles | 1.1 | Optional preferences editable/deletable; sensitive defaults absent. |
| FR-056 | Printable intelligence reports | 1.1 | Export report includes sources, generation time and uncertainty. |
| FR-057 | Verified provider marketplace | 2.0 | Marketplace lists only eligible providers; expired verification removed. |
| FR-058 | Credential verification | 2.0 | Credential check records issuer, scope and expiry; failed check not verified. |
| FR-059 | Confirmed-trip reviews | 2.0 | Review requires transaction evidence; duplicate review rejected. |
| FR-060 | Transparent total pricing | 2.0 | Total price includes known mandatory charges; unknown charges disclosed. |

### FR-061–070

| ID | Capability | Release | Acceptance test |
| --- | --- | --- | --- |
| FR-061 | Travel Circle and shared itineraries | 2.0 | Share only selected trip fields; revoked or expired link denied. |
| FR-062 | Voluntary safety check-ins | 2.0 | Check-in requires opt-in; recipients and timestamp visible; stop on revocation. |
| FR-063 | Insurance partner integration | 2.0 | Insurance referral discloses partner and terms; no underwriting by platform. |
| FR-064 | Telemedicine and assistance partners | 2.0 | Assistance handoff uses approved partner and verified contact; no medical claims. |
| FR-065 | Creator monetization | 2.0 | Creator earnings ledger reconciles transactions; disclosures visible. |
| FR-066 | Enterprise intelligence APIs | 2.0 | API tenant isolation, rate limits and licensing restrictions tested. |
| FR-067 | Encrypted document vault | 3.0 | Vault encrypted with access controls; threat model and deletion gate passed. |
| FR-068 | Revocable identity document sharing | 3.0 | Document share scoped and expiring; revoked access fails. |
| FR-069 | Document access audit | 3.0 | Document access events record actor/time/action; unauthorized log access denied. |
| FR-070 | Community groups | 3.0 | Group membership controls and moderation tested; reporting available. |

### FR-071–080

| ID | Capability | Release | Acceptance test |
| --- | --- | --- | --- |
| FR-071 | Private messaging | 3.0 | Messaging blocks unauthorized access; block/report controls tested. |
| FR-072 | Traveler meetups | 3.0 | Meetup visibility opt-in; reporting and location privacy tested. |
| FR-073 | Predictive travel analytics | 3.0 | Predictive model evaluated against holdout baseline; uncertainty and drift monitored. |
| FR-074 | Partner-operated rebooking assistance | 3.0 | Rebooking suggestion requires explicit approval and partner confirmation; no autonomous purchase. |
| FR-075 | Parking discovery | 1.3 | Search radius returns correct facilities by distance; missing coordinates excluded. |
| FR-076 | Prices, hours and restrictions | 1.3 | Display sourced price, hours and restrictions; unknown values labeled. |
| FR-077 | Airport parking and transfers | 1.3 | Airport parking links to correct terminal/transfer; source shown. |
| FR-078 | Accessible parking and EV charging | 1.3 | Accessible/EV attributes only displayed when documented; unknown explicit. |
| FR-079 | Parking-aware driving itineraries | 1.3 | Driving itinerary includes parking and walk time where known; unknowns flagged. |
| FR-080 | Live parking availability | 1.3 | Live availability shows observation time; expired feed returns unknown, never available. |

## 22. Release gates and open decisions

A.1 competitor benchmarking; A.2 20–30 customer interviews and prototype; A.3 market/source coverage and license registry; A.4 vendor quotations and usage model; A.5 privacy and threat assessment; A.6 name clearance and launch scope sign-off. All remain open. Preserve A–N architecture roadmap, but split D–H into launch slices and later enhancements; V1.0 does not require completion of advanced atlas, simulator, flight feeds or digital twin.

Launch gate: all V1.0 register tests pass; approved market coverage; 100% critical claim attribution; no unresolved critical security findings; restore and load tests meet section 8 targets at agreed load; alert deduplication and correction verified; usability study measures search success and research time. Publish supported coverage and limitations. Release owner records evidence and approval; rollback plan required. Subsequent releases repeat applicable gates plus privacy, cost and coverage checks.

Decision record: user approved V3 scope direction; 20 markets, numerical targets, pricing, retention and release assignments remain proposed pending validation. No competitor hands-on testing, vendor quotes, legal assessment or trademark clearance completed in this revision. Architecture remains modular monolith, isolated workers, PostgreSQL/PostGIS/pgvector and bounded AI; cloud choice remains open.

## Conversion record

[Original DOCX](design-v3.docx). Body paragraphs, headings and tables are transcribed in source order. Pagination, decorative layout, and repeated page furniture are omitted. Header text was “RISWANLABS  /  DESTINAIQ                                      ENGINEERING DESIGN” and footer label was “DestinaIQ  •  Draft v3.0”. Source statements and historical proposals are preserved as written.
