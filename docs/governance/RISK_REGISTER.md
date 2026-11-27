# Risk register

All risks are **Open**. Owner roles are proposed for confirmation. The [decision register](DECISION_REGISTER.md) records open validation and approval work.

| ID | Risk | Mitigation | Proposed owner role | Decisions |
| --- | --- | --- | --- | --- |
| R01 | Unproven differentiation and willingness to pay | Run equivalent competitor scenarios and 20–30 traveler interviews. | Product | D01, D02, D10 |
| R02 | Coverage gaps and misleading rankings | Run candidate-market coverage gates and qualify all ranking inputs. | Data stewardship | D03, D12 |
| R03 | Unlicensed data, provider outages and spend escalation | Document rights, caps, failover and per-provider quotes. | Data and finance | D04, D05 |
| R04 | Overprovisioned cloud and missed SLOs | Compare cloud designs and validate expected and peak load. | Engineering | D06, D11 |
| R05 | Reservation, sharing or identity data exposed | Minimize data and verify isolation, revocation and deletion. | Security and privacy | D07, D08, D17 |
| R06 | Name conflict or unavailable domain | Complete trademark, domain and app store checks. | Product owner | D09 |
| R07 | Safety harm from stale, biased or fabricated claims | Establish human review, unknown semantics, correction SLAs and bias gates. | Trust and safety | D12, D13 |
| R08 | Negative unit economics under heavy use | Verify allocation, costs, willingness to pay and usage caps. | Finance | D05, D10 |
| R09 | Operational incidents without adequate response | Assign on-call and data owners and test restore, correction and escalation. | Engineering | D11, D14 |
| R10 | Partner service, licensing or sensitive feature scope exceeds approval | Validate partner contracts, moderation and deferred controls separately. | Product and legal | D04, D08, D16, D17 |
| R11 | Hallucination, untrusted input or inappropriate AI action | Verify source grounding, tool boundaries, abstention and action approval. | AI and security | D08, D13, D15 |

| R12 | Cross-phase slices miss authoritative customer release gates | Sequence slices using explicit dependencies and verify release boundaries against the reconciliation table. | Product and engineering | D21, D22 |
| R13 | Public repository exposes restricted data | Run required scans, use synthetic fixture data, review artifacts and route incidents privately. | Security | D19 |
| R14 | Conflicting inventory total leads to silent scope removal | Keep all 166 enumerated IDs and obtain clarification before changing the inventory. | Project owner | D20 |
