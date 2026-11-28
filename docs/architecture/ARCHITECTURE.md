# Architecture baseline

[Design V3](../product/DESIGN.md) is the specification. The checkpoint preserves the modular monolith with isolated background and ingestion workers. Next.js and FastAPI are the proposed experience and backend technologies. The 12 product domains are logical boundaries. PostgreSQL is authoritative, PostGIS handles spatial data, and pgvector supports vector retrieval. Search, cache and retrieval projections are rebuildable. Keep major infrastructure changes behind a reviewed ADR. Kubernetes, Kafka, microservices and a dedicated graph database are outside this baseline.

## Destination knowledge and ingestion

A temporal Destination Knowledge Graph models stable canonical IDs, typed geographic relationships, evidence and validity. Store observation, retrieval, validity and record time separately. Preserve conflicts by issuer. Trip dependencies and the later Travel Digital Twin model segments, transfers and reservation impacts without autonomously changing bookings.

Provider-neutral connectors emit source identifiers, hashes, timestamps and licensing metadata. Normalize and resolve entities, quarantine ambiguous critical records, and write accepted facts atomically with an outbox. Workers process replay, deduplication and corrections. Isolate credentials, enforce limited egress, and preserve stale or unknown semantics.

## Intelligence, security and operations

Apply structured deterministic checks for safety, relevance, allowance and travel constraints before bounded retrieval and generation. Constrain tools, budgets and permissions. Require cited evidence and abstain when evidence is insufficient. Apply privacy, authorization and consent to user data and delivery. Separate serving from ingestion. Use staged rollout, backups, restore drills, telemetry and agreed SLOs.

AWS versus Azure and provider contracts are open. See [decisions](../governance/DECISION_REGISTER.md) and [architecture decision records](../adr/README.md).
