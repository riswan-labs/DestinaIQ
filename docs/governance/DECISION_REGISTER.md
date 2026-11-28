# Decision register

D19, D20, D21, D23 and D24 are **Approved by the project owner**. D01–D18 and D22 remain **Open**. The checkpoint indicates the planned decision point or first validation gate. Resolution requires evidence and recorded approval. Reservation and commercialization decisions are prepared during discovery and resolved at their respective gates.

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
| D17 | Deferred document, sharing and community features | Require explicit owner authorization, security and privacy assessment, commercial justification and applicable release gates. Include lawful handling, access control and moderation evidence. | [CP-12.12](../engineering/ROADMAP.md#cp-1212) |
| D18 | Backend coverage measurement and tooling | Agree enforcement metric and tools before implementation CI. | [CP-1.10](../engineering/ROADMAP.md#cp-110) |

## D19

**Approved by the project owner.** DestinaIQ remains public to facilitate independent architecture, code and pull-request review. The Checkpoint 0.1 remediation assignment explicitly approved intentional public visibility. The public security posture requires mandatory secret detection and security scanning. Keep customer information, credentials, production secrets, API keys and confidential commercial agreements out of all repository content and artifacts.

## D20

**Approved by the project owner.** The previous total of 162 was an arithmetic error. The corrected baseline is 13 engineering phases, 166 engineering checkpoints, 90 pre-launch checkpoints, 76 post-launch checkpoints, 80 functional requirements, 14 non-functional requirements and 15 launch capabilities. Every enumerated checkpoint ID and title is preserved.

## D21

**Approved by the project owner.** The [release reconciliation](../product/RELEASE_RECONCILIATION.md) records the approved slices.

| Requirement | Approved customer-facing release |
| --- | --- |
| FR-022 Public destination Q&A | V1.1 |
| FR-025 Offline trip summaries | V1.1 |
| FR-030 Narrow locale and currency support | V1.1 |
| FR-050 Advanced itinerary optimization | V1.2 |
| FR-054 Moderated scam and disruption reporting | V1.3 |
| FR-055 Optional traveler preferences | V1.1 |
| FR-056 Printable intelligence reports | V1.1 |

Engineering phase ownership does not override Design V3 release assignments. Cross-phase work requires explicit task-level authorization, verified dependencies and bounded pull request scope. This decision approves scheduling only.

## D22

**Open.** Approve whether and when to expose billing and native mobile functionality. Earlier cost validation and commercial groundwork confer no customer release authorization. Record demand, scope, pricing, evidence and explicit owner approval.

### Recommendations pending validation

- Deliver a responsive web application first. Evaluate native iOS and Android separately at the distribution decision under D16 and D22.
- Make cost metering, usage quotas and rate limiting mandatory launch controls as a planning recommendation. Validate their scope and thresholds at CP-0.4, CP-0.5 and CP-6.10. The design and thresholds remain subject to approval.
- Enable payment processing and subscriptions only after unit economics are validated and D10 and D22 are approved. Validate provider licensing at CP-0.4, cloud selection at CP-0.5, and privacy obligations at CP-0.8 and CP-8.14.

## D23

**Approved by the project owner.** Retain the existing 15 V1.0 launch capabilities without expansion as a planning decision, subject to subsequent customer discovery, data feasibility, licensing, cost, privacy and production-readiness validation. CP-0.2 acceptance on 2026-11-27 is based on the reviewed commit `cad78ba6e9b4019034010a3e7cf3bcbbf9abbd40` and the bounded preliminary evidence policy.

The approved inventory remains 13 phases, 166 checkpoints (90 pre-launch and 76 post-launch), 80 FRs, 14 NFRs and 15 launch capabilities. Existing authoritative release assignments and acceptance criteria are preserved. F01–F13 are accepted as planning guidance. Formal specification changes and implementation require separate owner authorization. See [PR #2](https://github.com/riswan-labs/DestinaIQ/pull/2) and the [follow-up register](../research/competitive-benchmark/FOLLOW_UP.md).

## D24

**Approved by the project owner.** On 2026-11-27 the owner authorized a CP-0.3 acceptance-policy exception in the CP-0.3 Research Closure and Review Finalization assignment for [Draft PR #3](https://github.com/riswan-labs/DestinaIQ/pull/3), reviewed commit `02d8a39f017746d8aed5186b2f7ce240bbb1d63a`. CP-0.3 may be accepted as a bounded secondary research baseline with incomplete numerical scoring and without completed interviews or surveys. The original roadmap and acceptance criteria remain intact. CP-0.3 remains Under Review pending independent owner acceptance.

Preserve 20–30 completed traveler interviews as an outstanding objective and 50–100 survey responses as an exploratory target subject to owner approval. No fieldwork is authorized by this decision. Carry readiness and risks to [CP-0.9](../engineering/ROADMAP.md#cp-09), then require the owner to review actual primary evidence and explicitly approve remaining research limitations before public V1.0 under [CP-6.14](../engineering/ROADMAP.md#cp-614). The [follow-up register](../research/customer-discovery/PRIMARY_RESEARCH_FOLLOW_UP.md) records the Phase 6 handoffs.

The four [feasibility cohorts](../research/customer-discovery/LAUNCH_MARKET_RECOMMENDATIONS.md) are approved for research planning only. D02 and D03 remain open. D23, the authoritative requirements and release assignments, and the 15 launch capabilities are preserved. Formal specification changes and implementation require separate owner authorization.
