# Product metrics hypotheses

All results are unmeasured. Quarterly, monthly, weekly and daily frequencies below are proposed after applicable release authorization. Restrict retention, suppress small cohorts and keep behavioral and billing data separate. Preserve [authoritative non-functional targets](../../engineering/TRACEABILITY.md#non-functional-register) and the release gates.

| Metric | Purpose | Calculation | Data needed | Applicable release | Cadence | Privacy | Target hypothesis |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MTR01 | Qualified visitors | Unique visitors reaching a supported intent page or making a non-empty destination query per week | Dedup scope, event type, coverage status | V1.0 | Weekly | Consent-aware coarse dedup | Baseline pilot |
| MTR02 | Organic acquisition | Qualified sessions attributed to organic search / qualified sessions | Allowlisted referrer class | V1.0 | Weekly | Avoid raw query strings | Baseline pilot |
| MTR03 | Referral acquisition | Qualified sessions via first-party referral / qualified sessions | Coarse referral cohort | Future authorized sharing; aggregate V1.0 if applicable | Monthly | No cross-trip disclosure | Baseline only |
| MTR04 | Acquisition cost | Approved attributable acquisition spend / newly acquired qualified customers; report paid customers separately | Aggregated spend and dedup by cohort | Later commercialization | Monthly | No personal stitching | Unknown until spend and cohort evidence |
| MTR05 | Search success | Successful destination selections / eligible search sessions; separate search task audit | Search result and selected canonical ID | V1.0 | Weekly | Avoid raw free text | Design V3 target remains authoritative |
| MTR06 | Comparison completion | Valid evidence-bearing results / comparison starts | Attempt and result | V1.0 | Weekly | Anonymous aggregate | Baseline pilot |
| MTR07 | Saved destinations | Activated users with a first save / eligible users | Save event and eligibility | V1.0 | Weekly | Store only private event metadata | Baseline pilot |
| MTR08 | Trip creation | Eligible users with a first trip / eligible users | Trip creation flag | V1.0 | Weekly | Avoid dates in telemetry | Baseline pilot |
| MTR09 | First itinerary | First usable generated drafts / first eligible requests | Request, result, source check status | V1.0 | Weekly | Redact prompt and place details where sensitive | Baseline pilot |
| MTR10 | Intelligence consumption | Sessions with cited field viewed / qualified sessions | Aggregate field categories and views | V1.0 | Weekly | No raw browsing trail | Baseline pilot |
| MTR11 | Return visits | Qualified users with a repeat visit / first-visit cohort | Pseudonymous cohort and event day | V1.0 | Weekly | Short retention | Baseline pilot |
| MTR12 | Saved-trip monitoring | Consented active monitored trips / eligible active saved trips | Opt-in and eligibility counters | V1.0 | Weekly | No location trail exposed | Baseline pilot |
| MTR13 | Briefing engagement | Voluntary click or view / delivered briefings | Delivery, aggregate click/view | V1.0 | Weekly | Avoid invisible third-party tracking pixels | Baseline pilot |
| MTR14 | Itinerary updates | Edited drafts / generated eligible drafts | Edit and draft flags | V1.0 | Weekly | No raw edit content | Baseline pilot |
| MTR15 | 7-day retention | Cohort users with activity on day 7 / activated cohort | Activation and coarse event day | V1.0 | Weekly | Aggregate cohort floors | Baseline pilot |
| MTR16 | 30-day retention | Cohort users with activity on day 30 / matured activated cohort | Activation and event day | V1.0 | Monthly | Suppression for small cells | Baseline pilot |
| MTR17 | Repeat trip planning | Users starting a distinct later trip / eligible users with ended trips | Dedup trip states | V1.0 | Quarterly | No exact itinerary export | Unknown |
| MTR18 | Seasonal return | Researchers in later season / eligible earlier cohort | Coarse season and activity | V1.0 | Quarterly or seasonally | Aggregate only | Unknown |
| MTR19 | Free-to-paid | First-time paid users / eligible free cohort | Entitlement transitions | Later commercialization | Monthly | Separate billing identifiers | Unknown |
| MTR20 | Trip Pass conversion | Purchased passes / eligible pass offer exposures | Offer and order counts | Later commercialization | Monthly | Restricted payment access | Unknown |
| MTR21 | Subscription conversion | New subscriptions / eligible recurring offer exposures | Offer and transitions | Later commercialization | Monthly | No billing or card data in analytics | Unknown |
| MTR22 | Revenue per payer | Recognized net revenue / distinct paying users in period | Ledger aggregates | Later commercialization | Monthly | Restrict finance access | Unknown |
| MTR23 | Contribution margin | (Net revenue minus attributable variable cost) / net revenue | Source, compute, fees and delivery costs | Later commercialization | Monthly | Aggregate only | Use Design V3 target as hypothesis where applicable |
| MTR24 | Churn | Subscriptions ending / subscribers active at start; expiry separate | Entitlement counts | Later commercialization | Monthly | Avoid inferring reasons | Unknown |
| MTR25 | Source attribution | Consequential sampled claims with valid sources / sampled claims | Source evidence audit | V1.0 | Release and weekly | Public claims only in sampling | Design V3 critical attribution gate unchanged |
| MTR26 | Freshness | Eligible claimed-current fields within source expiry / eligible fields | Timestamps and expiry | V1.0 | Daily | No traveler profile in evidence logs | Per-source targets await validation |
| MTR27 | Correction frequency | Published fact corrections / published fact updates in period | Version transitions and correction flags | V1.0 | Weekly | No contributor identity in rollups | Baseline pilot |
| MTR28 | Reported inaccuracies | Eligible distinct inaccurate-report cases / published facts viewed or sampled; state denominator | Case outcomes and aggregate views | V1.0 | Weekly | Protect reporter and redacted notes | Baseline pilot |
| MTR29 | Recommendation usefulness | Optional useful responses / valid responses; report response rate | Voluntary vote and exposure | V1.0 | Weekly | No mandatory feedback | Baseline pilot |
| MTR30 | Critical alert relevance | Relevant alerts / audited delivered critical alerts; separately measure misses | Gold fixtures and consented feedback | V1.0 | Release and weekly | Keep location and opt-in metadata private | Evidence gate unchanged |
| MTR31 | Unsupported AI claims | Unsupported consequential claims / audited AI claims | Redacted citations and independent audit | V1.0 | Release and weekly | Redact free text and user context | Zero unsupported critical claims is a proposed test aspiration; preserve NFRs |
