# Decision register

D19 is **Approved by the project owner**. All other decisions below are **Open**. The checkpoint indicates the planned decision point or first validation gate. Resolution requires evidence and recorded approval. Reservation and commercialization decisions are prepared during discovery and resolved at their respective gates.

| ID | Decision | Required evidence | Checkpoint |
| --- | --- | --- | --- |
| D01 | Hands-on competitor benchmark | Six attempts with screenshots, prices, weights, tested coverage and access blockers. | [CP-0.2](../engineering/ROADMAP.md#cp-02) |
| D02 | Customer discovery and product hypotheses | 20–30 interviews and prototype usability tests with research time and willingness-to-pay evidence. | [CP-0.3](../engineering/ROADMAP.md#cp-03) |
| D03 | Initial destination coverage and launch sign-off | Validate each candidate and publish searchable versus supported catalog, coverage and owner sign-off. | [CP-0.3](../engineering/ROADMAP.md#cp-03) |
| D04 | Provider licensing and attribution | Record commercial use, storage limits, redistribution, territory, rates and attribution per source. | [CP-0.4](../engineering/ROADMAP.md#cp-04) |
| D05 | Commercial API costs and provider selection | Obtain quotes, assumptions and usage sensitivity across 1k, 10k and 100k active users. | [CP-0.4](../engineering/ROADMAP.md#cp-04) |
| D06 | AWS versus Azure | Compare cost, service fit, reliability, operations and recovery constraints in an ADR. | [CP-0.5](../engineering/ROADMAP.md#cp-05) |
| D07 | Data retention and deletion policy | Approve category and backup TTLs, legal holds and retention verification. | [CP-0.8](../engineering/ROADMAP.md#cp-08) |
| D08 | Reservation import privacy and OAuth | Inventory data, assess obligations and approved terms, test security and request provider approval where required. | [CP-8.14](../engineering/ROADMAP.md#cp-814) |
| D09 | Trademark, domain and app-store name clearance | Document clearance and alternative if needed. | [CP-0.9](../engineering/ROADMAP.md#cp-09) |
| D10 | Pricing, unit economics and monetization | Validate quoted costs, willingness to pay, free-tier subsidy, caps, expected positive contribution and margin threshold. | [CP-11.11](../engineering/ROADMAP.md#cp-1111) |
| D11 | Production SLO and workload | Agree test profiles and final performance, availability, RPO and RTO targets, then run load and restore drills. | [CP-6.3](../engineering/ROADMAP.md#cp-63) |
| D12 | Coverage thresholds, geographic precision and rankings | Approve supported thresholds, bias constraints, provenance and calibrated ranking methodology. | [CP-3.15](../engineering/ROADMAP.md#cp-315) |
| D13 | Safety liability and correction ownership | Review liability, claims wording, escalations and corrections with relevant counsel. | [CP-0.8](../engineering/ROADMAP.md#cp-08) |
| D14 | Staffing, on-call and stewardship | Assign on-call, incident response, data stewardship and launch approval roles. | [CP-6.11](../engineering/ROADMAP.md#cp-611) |
| D15 | AI providers, model/tool governance and launch evaluation thresholds | Approve processing terms, quality dataset, cost caps and policy thresholds. | [CP-5.14](../engineering/ROADMAP.md#cp-514) |
| D16 | Partner, creator and distribution scope | Verify rights, contracts, moderation, dispute workflows and native demand. | [CP-11.11](../engineering/ROADMAP.md#cp-1111) |
| D17 | Deferred document, sharing and community features | Obtain separate approval based on demand, threat model, lawful handling, access control and moderation. | [CP-12.12](../engineering/ROADMAP.md#cp-1212) |
| D18 | Backend coverage measurement and tooling | Agree enforcement metric and tools before implementation CI. | [CP-1.10](../engineering/ROADMAP.md#cp-110) |

## D19

**Approved by the project owner.** DestinaIQ remains public to facilitate independent architecture, code and pull-request review. The Checkpoint 0.1 remediation assignment explicitly approved intentional public visibility. The public security posture requires mandatory secret detection and security scanning. Keep customer information, credentials, production secrets, API keys and confidential commercial agreements out of all repository content and artifacts.

## D20

**Open.** The assignment says 162 checkpoints and lists 166 unique IDs. Phases 0–6 contain 90 and Phases 7–12 contain 76. Preserve every listed ID and name. Owner confirmation is required before any count-driven removal, consolidation or renumbering.

## D21

**Open.** Cross-phase release scheduling for FR-022, FR-025, FR-030, FR-050, FR-054, FR-055 and FR-056 requires confirmation. Retain authoritative releases and schedule constrained earlier/later slices as proposed in [reconciliation](../product/RELEASE_RECONCILIATION.md). For FR-067–072, the tentative planning homes are CP-12.12 and CP-12.13; D17 and separate scope approval remain prerequisites.

## D22

**Open.** Approve whether and when to expose billing and native mobile functionality. Earlier cost validation and commercial groundwork confer no customer release authorization. Record demand, scope, pricing, evidence and explicit owner approval.
