# Benchmark methodology

Protocol fixed before detailed evaluation on 2026-11-27 (America/Los_Angeles). Use [scenario inputs](SCENARIOS.md) unchanged, and record any unsupported field or surrogate explicitly. Start on a public, signed-out web surface. Follow official links to read public destination outputs or use controls with synthetic inputs when available. Record page, tier, retrieval timestamp, output, expected checks and limitations. One narrowed read-only observation may be hands-on for the observed output; record unexercised features independently. Landing pages and embedded illustrative outputs are vendor claims. A rendered live output is direct observation of presentation only; underlying factual accuracy still needs an independent reference. Optional tests requiring new accounts, payment, installation, private data or special permissions are gated.

| Dimension | Weight | Five observable checks, one point each |
| --- | ---: | --- |
| Accuracy | 20% | Correct place or identity, date, numeric/unit value, relevant constraint, correct conclusion against independent authoritative fixtures |
| Coverage | 15% | Resolve all named places, all needed geographic levels, requested dates, core scenario feature, secondary use case |
| Freshness | 15% | Show record date, retrieval date, validity window, stale indication, traceable update or correction |
| Personalization | 10% | Capture date, party, budget, interests/constraints, visibly adapt output when one input changes |
| Completeness | 10% | Complete task start, deliver usable output, handle missing/invalid input, allow revision, preserve or export results where requested |
| User experience | 10% | Visible starting action, clear feedback, readable units/labels, visible task completion, documented recovery from a failed input |
| Source transparency | 10% | Show source name, retrievable source link, applicable date/version, method or coverage, uncertainty/caveat |
| Pricing and value | 5% | Publish tier or price, currency/market, billing interval, usage limits, feature boundaries covering the task |
| Observed performance | 5% | On three timings using the same browser/network, view opens ≤3 s, input responds ≤1 s, result P50 ≤5 s, slowest ≤10 s, zero timeouts |

0 = verified unsupported/failed on all applicable checks; 1 = very limited; 2 = below expectations; 3 = adequate; 4 = strong; 5 = excellent. A dimension is scored only when all five published checks can meaningfully be evaluated at the declared tier and scope. Official commercial documentation can support the pricing checks; output accuracy requires an independent reference. Unsupported scope must be explicitly documented by the vendor or demonstrated with an eligible, repeated control and clear failure. Network fetching time is excluded from product performance. Partial observations are recorded without a score when remaining criteria cannot be tested.

Evidence labels are **Hands-on verified**, **Official documentation verified**, **Vendor-advertised only**, **Third-party reported**, **Access restricted**, **Not tested**, and **Unknown**. In scenario results, outcomes are Hands-on (at least one matching live output), Documentation-only (scenario-relevant product material without a tested output), Restricted (material gated workflow), or Untested (no meaningful applicable operation). A row can describe a restriction and still be Hands-on when a public slice was exercised. Confidence refers to the recorded observation within scope.

Weights are listed above. Normalized percent is 100 × sum(weight × score) / (5 × sum(eligible weight)). Use one decimal place. No eligible weight means N/A. Record the denominator and scored evidence coverage. Do not rank across products unless the same scenario tasks, same tier conditions and same dimension set are eligible with at least 70% weight for each product; a restricted or untested task cannot be scored as zero. An observed feature without comparable end-to-end evidence may be used qualitatively.

Use synthetic trips only. Keep source references and paraphrased factual observations. No vendor images or copied product outputs beyond short factual fields. The [register](EVIDENCE_REGISTER.tsv) records UTC observation times, surfaces and limitations. The approved source method is [Design V3 §17](../../product/DESIGN.md#17-competitive-validation).


## Owner-authorized evidence closure

- Review policy authorization — CP-0.2 Evidence Closure and Review Finalization, project-owner assignment following review of b3f72328469172b425645af10a132f3fbafc239f.
- Research elapsed — 2026-11-28 00:42:14–00:45:08 UTC (2 minutes, 54 seconds wall-clock upper bound for active research; parallel observations counted once). Local research date 2026-11-27 in America/Los_Angeles.
- Research cap — One bounded public pass, at most 90 minutes of active effort. No accounts, purchases, installation, vendor contact or restricted access.
- Review entry — Complete scenario accounting, evidence-supported scoring, explicit incomplete coverage, all 13 dispositions, launch recommendation and designated follow-up. End-to-end competitors' restricted workflows are optional unless needed for a specific future decision.
- Fully verified scenario — All specified inputs and material checks exercised with attributable evidence. The current log has no fully verified scenarios. Hands-on in the TSV means partial coverage only.
- Owner acceptance — Approved on 2026-11-27 for reviewed commit cad78ba6e9b4019034010a3e7cf3bcbbf9abbd40 in [PR #2](https://github.com/riswan-labs/DestinaIQ/pull/2). The accepted baseline is preliminary.
