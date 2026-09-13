# Aircraft parts distribution & AOG sourcing — research blueprint

**13 September 2026 · INCOMPLETE · client-owned VPS only · no application built**

[analysis] **Verdict: conditional yes to an RFQ pilot**, not wholesale ERP replacement or a production release. The market case is credible; the required OSS research funnel is unfinished. [Value](06-value.md) · [Audit limitations](04-oss-candidates.md).

| Actual coverage | Delivered | Required |
|---|---:|---:|
| Directly reviewed repositories | **11** | **100** |
| Provisional ADOPT / STUDY | **7 / 4** | Judge after a wide funnel |
| Confirmed in bank / unresolved / confirmed NEW | **3 / 8 / 0** | Every membership reconciled |
| Tier-1 companies / Tier-2 offerings | **10 / 14** | **10 / 10** |
| Linked practitioner complaint excerpts | **10** | **8** |
| Workflow stages | **10** | **6–12** |
| Verified dry rounds / runtime-qualified components | **0 / 0** | Two dry rounds / qualification before use |

[analysis] **Person/segment:** sales/sourcing coordinator at an APE-like UK independent civil/business-aviation distributor, modeled as five staff—not an assertion about APE's team. **Wedge:** incoming email/site RFQ becomes one case linking exact part requirements, supplier offers, release evidence, holds and the accepted quote revision. [Person](01-person.md) · [Workflow](02-workflow.md).

[analysis] **Stack tax:** conditional selected basket **$14,848 + £1,248/year**, or **$16,470.40** at assumed $1.30/£. Actual APE spend is unknown. Initial RFQ/register subscriptions potentially displaced: **$6,588/year**; wider final scope: **$10,292.40/year**, both requiring invoices and parity. Marketplaces, email transport, statutory accounting and settlement are not magically self-hosted. [Companies/arithmetic](03-companies.md).

[analysis] **Economics:** one client-owned 16 GiB VPS is an **unbenchmarked budget**. Reference infrastructure **$1,466.40/year** plus assumed maintenance **$1,800/year** = **$3,266.40/year**, excluding external fees, taxes and guaranteed 24/7 support. Proposed **9.42 hours/week benefit is unmeasured**. First-build **$22,500–$52,500** and second compatible deployment **$1,800–$4,500** are planning estimates. Subscription savings alone do not justify the first bespoke build. [Model/falsifiers](06-value.md).

[analysis] **Spine:** TradingParty · PartIdentity/StockUnit · DealCase · CommercialDocument · EvidenceDossier · Fulfilment. ERPNext is provisional commercial/stock authority; preserve original messages/documents instead of creating competing databases. [Assembly](05-superapp.md).

**Ten leading inspected candidates:** [analysis] ERPNext—ADOPT; Chatwoot community—ADOPT; pypdf—ADOPT; ZXing-C++ reader—ADOPT; GS1 syntax engine—ADOPT where applicable; Karrio core—ADOPT conditionally; restic—ADOPT; InvenTree—STUDY runner-up; Paperless—STUDY optional index; pyHanko—STUDY, beta warning. OCA purchase-workflow is the eleventh reviewed pattern source. Verdicts are provisional, not production approval. [Pinned licences/scores](04-oss-candidates.md).

[analysis] **Eight gaps:** marketplace rights/adapters; qualified release/Spec 2000 interoperability; issuer/provenance/installation decisions; export determinations; physical stock/AOG execution; core/exchange/repair qualification; local accounting/payroll/final storefront; full research/security/licence/load/recovery qualification. These are unmet findings here, not proofs that no OSS exists anywhere. [Gap register](05-superapp.md#eight-gaps--not-proofs-of-global-oss-nonexistence).

[analysis] **Correction recorded:** bank README and Foundry loader describe `fame_gap` in opposite directions. Do not apply a directional penalty before reconciling the producer formula. [Shared correction](https://github.com/sisodias/siso-industry-packs/blob/main/registry/corrections.jsonl).

**Completion boundary:** bulk audit failed. Seeds do not count. **89 additional direct reviews**, search closure and bank/adoption/health reconciliation remain before `status: complete` is valid. The pack contains an `incomplete` registry proposal; shared `industries.jsonl` was not replaced or marked complete. No unverified NEW repos were submitted. [Registry proposal](07-registry-proposal.jsonl) · [Submission status](07-bank-submission-status.json).
