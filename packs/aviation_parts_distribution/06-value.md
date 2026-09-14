# 06 — Value case: an RFQ wedge, not a fictional airline-ERP saving

Cost inputs observed **2026-09-13**; research checkpoint updated **2026-09-14** without repricing the basket. Workload, labour, staffing, conversion rates and estimates are `[analysis]` assumptions. No APE invoices, time study, implemented application, benchmark or realised revenue was available. **All benefits are unmeasured.** [Source-priced inputs](03-companies.md).

## Spend displaced and cost to operate

| Item | Annual USD planning amount | Boundary [analysis] |
|---|---:|---|
| Selected purchase basket | 16,470.40 | $14,848 + £1,248 at assumed $1.30/£; not actual APE spend or observed FX. |
| Initial RFQ/register subscriptions potentially displaced | 6,588.00 | Rotabull $5,388 + Airtable $1,200 only if paid, tariff-eligible and replaced at parity. |
| Final wider stack potentially displaced | 10,292.40 | Adds modeled stock ERP and Shopify after actual migration. |
| Retained selected services at final scope | 6,178.00 | Locatory + Workspace + Xero; not a claim to replace networks, banking or authority. |
| **Proven savings** | **0.00** | No invoice/cancellation or before/after evidence. |

[vendor] Reference pricing: DigitalOcean Basic regular CPU, 16 GiB RAM/eight shared vCPUs/320 GiB SSD at $96/month; weekly VM backup at 20% of VM fee; Spaces starts at $5/month for 250 GiB. Observed 2026-09-13, excluding taxes/overage; this is a transparent reference, not a mandatory vendor. [VM](https://www.digitalocean.com/pricing/droplets) · [Backup](https://www.digitalocean.com/pricing) · [Storage](https://www.digitalocean.com/pricing/spaces-object-storage).

[analysis] Infrastructure = $96 × 12 + $96 × 20% × 12 + $5 × 12 + assumed domain allowance $24 = **$1,466.40/year**. Maintenance assumption: two hours/month × $75/hour × 12 = **$1,800/year**. Total **$3,266.40/year**; no guaranteed 24/7 response. Email delivery, external data/API fees, taxes, overages and exceptional recovery are additional. Domain/labour amounts are allowances, not sourced quotes.

[analysis] At proven parity, hypothetical initial subscription benefit = $6,588 − $3,266.40 = **$3,321.60/year** before build/migration. Wider final scope = $10,292.40 − $3,266.40 = **$7,026/year**. A client without these subscriptions saves none of their cost. One low-volume broker does not automatically finance a bespoke programme.

[analysis] The 16 GiB host is an **unbenchmarked design budget**, not a measured minimum. A 100k–170k catalogue is not a load test. Try a smaller deployment only after representative import/indexing, concurrency, document processing and restoration tests. Default scope needs neither GPU nor Kubernetes. [Deployment gates](05-superapp.md).

## Additional costs identified on 14 September — not silently included

[vendor] The newly inspected Yente implementation requires Elasticsearch or OpenSearch. OpenSanctions separates its software licence from commercial rights to bulk data. OpenEPCIS models specify a Java 25 build; other reviewed document/transport adapters introduce their own Java or .NET requirements. [Yente](https://github.com/opensanctions/yente/blob/3bc1b14ea884aba9f0728d67b76a461f5339dc59/README.md) · [Commercial data](https://www.opensanctions.org/docs/commercial/exemption/) · [OpenEPCIS](https://github.com/openepcis/openepcis-models/blob/a481b0827dd43a0a4282d8db840eaf98477f7730/README.md) · [Complete comparison](evidence/standards-boundaries-2026-09-14.md).

[analysis] These are **optional evaluation candidates**, not newly deployed modules. Their required dataset, storage/index, runtime, connector, update and support costs are **unknown, not zero**. Do not claim that they fit inside the original $3,266.40/year or 16 GiB allowance. The next cost revision must price only the interfaces and data the actual client needs, then measure the selected deployment. An extra standards library is not a reason to add an unnecessary service.

[analysis] Screening audit storage and feed-health operations also need allowance. The proposed system retains subject identity, source/list version, receipt/screening timestamps and reviewer disposition. Stale or failed refresh must not become a passing decision. These controls have not been built or costed separately; their existence in the blueprint is not a realised saving. [Source-code and operational boundary](evidence/standards-boundaries-2026-09-14.md#3-watchman-documentation-drift-not-a-falsely-alleged-broken-feed).

## Hours returned — non-overlapping hypotheses

[analysis] Frequencies derive from a constructed Tuesday, not APE telemetry. Exclude overlap and supplier waiting time. [Baseline](01-person.md) · [Stages](02-workflow.md).

| Activity | Weekly cases | Baseline min/case | Target min/case | Hypothesised hours/week |
|---|---:|---:|---:|---:|
| W01–02 capture/normalise, excluding technical clarification | 50 | 8 | 3 | 4.17 |
| W03 compile supplier comparison, excluding supplier wait | 25 | 12 | 6 | 2.50 |
| W04 assemble/cross-reference dossier, excluding qualified approval | 25 | 8 | 5 | 1.25 |
| W08–09 publish shipment status/reconcile references | 15 | 8 | 4 | 1.00 |
| W10 prepare core/return follow-up | 5 | 10 | 4 | 0.50 |
| **Total, unmeasured** | | | | **9.42** |

[analysis] Arithmetic: (50×5 + 25×6 + 25×3 + 15×4 + 5×6) / 60 = **9.4167 hours/week** before added administration/errors. Baseline two representative weeks and compare two controlled pilot weeks: received/acknowledged/complete/quoted timestamps, hands-on minutes, revisions, missing evidence, quote-to-order rate, late shipments, wrong-unit/rejected-certificate events, core-credit delay, support and correction time. Match complexity cohorts; subtract training, validation and duplicate-entry time.

[analysis] Released capacity is not cash savings. Do not multiply hours by wages and call it profit unless overtime/payroll falls or incremental completed business and contribution margin are measured. There is no basis here to price prevented incidents or avoided aircraft downtime. [SISO observed-value model](https://github.com/sisodias/great-library-of-siso/blob/main/research/industries/source/intelligence/agency/economics/observed-value-model.json).

## Migration door

[analysis] **Incoming RFQ → evidence-complete, human-approved quote.** One case preserves conversation, offers, required documents, stock confirmation, delivery assumptions and approved quote revision. Keep storefront, accounting and authorised market access initially. Do not start by replacing every screen. [Competitive overlap](03-companies.md).

[analysis] Proposed pilot: at least 50 mixed-format authorised RFQs and 20 completed orders, in non-production. No unapproved document/alternate clears a hold; repeated imports do not duplicate lines; acceptance maps to the right quote/PO/unit; original evidence exports correctly. These are proposed samples, not records already collected.

## Build, migration and second-deployment economics

| Work | Planning effort [analysis] | At assumed $75/hour | Acceptance |
|---|---:|---:|---|
| First reusable assembly/integrations/test harness | 300–700 h | $22,500–$52,500 | Replace estimate after data/contracts sampled; no app built. |
| First-client discovery/cleanup | 40–100 h | $3,000–$7,500 | Reconcile catalogue/manufacturer PN/unit/lot/conditions; retain originals. |
| Document/history migration | 40–120 h | $3,000–$9,000 | Hashes, relationships, counts and independent spot checks. |
| Connectors/training/parallel run | 40–100 h | $3,000–$7,500 | Written API rights and buyer/stores/quality/finance acceptance. |
| **Second compatible deployment** | **24–60 h** | **$1,800–$4,500** | Clean data and same preset/contracts; new ERP/jurisdiction is extra. |

[analysis] These are planning ranges, not quotes or elapsed-time promises. At $3,321.60/year net subscription benefit, the first-build lower bound $22,500 alone implies about **6.8 years**, excluding migration. The opportunity needs reusable deployment economics or measured throughput/quality gains, not an inflated incumbent software bill.

[analysis] Reversible exit is part of the specification: export parties, part/unit IDs, RFQ/quote revisions, orders, holds, receipts/shipments/returns, ledger mappings and document hashes/relationships; original files in ordinary client-owned storage; client credentials; tested restore and documented external IDs. Removing a donor component is an adoption cost, not a later surprise.

## Segment opportunity without invented TAM

[vendor: trade association] ASA describes **over 1,200 global member companies**, including distributors, suppliers, repair stations, manufacturers, airlines/operators and services. This is **not 1,200 independent AOG brokers or addressable clients**. [ASA](https://www.aviationsuppliers.org/who-we-are).

[analysis] The chosen UK/civil back-to-back operator count is **not established**. A deduplicated company-level universe must classify workflow/ownership and remove integrated groups/non-brokers before a stratified interview study. Do not borrow general freight-company counts.

[analysis] Reuse sensitivity, not a market forecast: $30,000 common assembly amortises to $3,000 at ten clients or $1,200 at 25, before sales, migration, hosting, maintenance and compliance support. Add actual second-deployment costs. Small businesses can be an attractive segment only if workflow repeatability and reach are demonstrated.

## Falsifiers and verdict

[analysis] The thesis is bad if authorised marketplace interfaces are unavailable at viable prices; existing aviation ERP configuration achieves the same results more cheaply; quality/identity errors rise; review overhead erases capture savings; second deployments require near-first-build work; required licensed data/adapter operations erase the margin; or single-host recovery cannot meet the operator's AOG needs. These are disqualifying commercial/operational tests, not implementation details to postpone.

[analysis] **Conditional yes to a narrowly measured RFQ pilot; no to wholesale migration or production admission now.** Require actual spend, authorised sample data, connector rights, independent quality approval and repeatable second-deployment effort. The research itself is incomplete: **23 rather than 100** repositories were directly reviewed. Bank identities are reconciled against six pinned published layers, but external adoption/health evidence and search-round closure remain incomplete. [Audit](04-oss-candidates.md) · [Bank receipt](evidence/bank-reconciliation-2026-09-14.json).
