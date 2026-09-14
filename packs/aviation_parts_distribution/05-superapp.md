# 05 — Provisional assembly: one case, six aggregates, one client VPS

Original design **2026-09-13**, updated **2026-09-14**. **Research blueprint only; not implemented, benchmarked or production-qualified.** The repository sweep has reached 23 direct reviews and remains incomplete. Architectural choices are `[analysis]`; linked upstream capability descriptions are `[vendor]`. The seven original ADOPT preferences and six aggregates are retained. [Component evidence](04-oss-candidates.md) · [Assembly JSON](05-assembly.json) · [New standards/adapter evidence](evidence/standards-boundaries-2026-09-14.md).

## The spine

[analysis] Extend the commercial system's records instead of rebuilding a ledger. Stable client-local IDs preserve original external IDs. A conversation creates a requirement; only an approved quote revision becomes the accepted commercial commitment. [Workflow](02-workflow.md).

| Aggregate | Minimum contract | Authority and invariant |
|---|---|---|
| TradingParty | Legal entity, contacts, customer/supplier/end-user roles, account IDs, supplier approval, credit and screening references. | ERP party master; screening is a dated decision, not a permanent badge. |
| PartIdentity | Manufacturer/raw PN, normalised search key, evidenced alternatives; linked StockUnit with condition, serial/lot, qty/UOM, location/disposition. | ERP stock authority. Listing is not owned stock; serial is not globally unique; string match is not eligibility. |
| DealCase | Source conversation IDs, requirements, urgency, airport/handler, deadline, owner, supplier requests and holds. | Custom case aggregate; Chatwoot owns original message events, not a second CRM. |
| CommercialDocument | Supplier RFQ/offer, customer quote, PO/SO, invoice/credit; issued revision, currency, expiry, freight/core terms and approvals. | ERP commercial records. Link accepted revision explicitly; distinguish supplier promise from reservation. |
| EvidenceDossier | Original bytes/hash, source, issuer/type, PN/SN/lot links, provenance, customer requirements, reviewer/decision/time and discrepancies. | Client-local evidence store and case metadata; extraction or cryptographic validity is not regulatory acceptance. |
| Fulfilment | Reservation, receiving/quarantine, direct ship, packing, milestones, delivery proof, RMA/core/credit links. | ERP fulfilment authority; carrier observations are not proof of correct-unit delivery. |

## Component map and runners-up

[analysis] ADOPT is a provisional preference, not deployed/qualified status. Directly inspected alternatives are compared; unexamined alternatives are not declared inferior. [Pinned source and edition evidence](04-oss-candidates.md).

| Stages | Component / verdict | What must be ours | Why this choice, and comparison limit |
|---|---|---|---|
| W01–02 | Chatwoot community + ERPNext / ADOPT | Message-to-case IDs, safe ingestion, confirmed requirements and duty ownership. | Preserve a real inbox rather than inventing chat. Native ERP communication is a simpler pilot option; no complete helpdesk benchmark was performed. |
| W02–03, W05–07, W09–10 | ERPNext / ADOPT | Aviation fields, evidence/hold transitions, quote/core relationships and external IDs. | Broader purchasing/order spine than inspected InvenTree. OCA purchasing patterns require Odoo, not Frappe; a full Odoo alternative remains unqualified. |
| W04 | pypdf / ADOPT; pyHanko / STUDY | Original custody, provenance, human review and trust policy. | Local library avoids a second document application. pyHanko's beta warning prevents production approval; text extraction and signature validation are different functions. |
| W04, W10 | Paperless / STUDY, optional index | Keep dossier authority and unchanged originals in the spine. | Native file links suffice until indexing value is measured; no second source of truth. |
| W07–08 | ZXing-C++ reader + GS1 syntax engine / ADOPT where applicable | Physical unit reconciliation and label profiles. | Multiple barcode symbologies plus separate GS1 semantics; neither implements ATA release semantics. Writer dependencies remain unreviewed. |
| W08 | Karrio core / ADOPT conditionally | AOG route/handler requirements, holds and client-owned audit. | Reuse carrier adapters; manual carrier/forwarder portal remains fallback. Core lacks some enterprise audit/workflow features. |
| All | restic / ADOPT | Schedule, key custody, consistent DB exports and restore drill. | Reuse backup implementation. Same-host copy is not disaster recovery; no exhaustive backup-product comparison was completed. |

[analysis] **Lift by default; do not call glue free.** Reuse purchasing, stock, readers, inbox, carrier adapters and backup. The differentiated work is the six-object contract, state transitions, identity and adapters. “Roughly 5% custom” is an aspiration, not a measured code or effort fraction. First reusable assembly planning range: 300–700 hours. [Value case](06-value.md).

## Honest integration work

[analysis] **Identity and permissions:** retain manufacturer PN, serial/lot, conditions and unmapped original values. Never merge suffixes or invent approved alternates. Use native accounts/least-privilege service tokens first; define sales, stores, quality, finance and admin permissions. Check exact-edition SSO availability. A person allowed to draft a quote need not be allowed to clear quality/export/credit holds.

[vendor] ERPNext's RFQ documentation describes sending attached files with supplier requests. [Official RFQ documentation](https://docs.frappe.io/erpnext/request-for-quotation).

[analysis] **Files and fan-out:** per-supplier explicit attachment allowlist; do not forward the entire customer/supplier dossier. Preserve original signed bytes and separate OCR/text/PDF-A derivatives. Bound file size, pages and archive expansion. Parse without network/credentials. Failed parsing creates a review task, not an empty success.

[analysis] **Jobs:** durable outbox, idempotency keys and receipts. Do not blindly retry a timed-out purchased label or invoice. Store request/response IDs, failures, attempts and reconciliation state. Reordered webhooks and duplicate messages must not duplicate RFQs or orders.

[analysis] **Money:** offered, quoted, committed and invoiced amounts are distinct. Preserve currency, FX source/time, tax, delivery basis, allocations and core liability. Live exchange-rate changes never rewrite accepted quotes. Retain statutory accounting/payroll until local requirements and reconciliation tests pass.

[analysis] **Audit:** application append-only events are not tamper-proof against root on the same VPS. Hashes establish byte consistency, not truth, issuer authority or complete provenance. Use independently retained client-controlled exports/backups and reconstruction tests. Do not advertise WORM or regulatory certification from an audit table.

## Runtime and architecture

```text
Email / existing storefront / optional authorised messaging
                         |
                client-owned VPS boundary
                         |
               TLS + native authentication
                         |
       inbox ----------> DealCase / aviation extension
                                |
                  ERPNext + supported database
                                |
              original files + dossier metadata
                    |                    |
             local parsers          durable outbox
                                         |
               authorised marketplace / carrier / accounting APIs

Consistent database + file exports -> restic -> client-owned off-host backup
Optional Paperless working index is removable, never dossier authority.
```

[vendor] ERPNext distinguishes its disposable demo from production/custom-app deployment. An inspected default-branch commit is a research pin, not a production release selection. [Upstream guidance](https://github.com/frappe/erpnext/blob/fe25746febc8731bbbc0880dcb18d528dcf08a63/README.md).

[analysis] One client VPS, separate processes/containers and database roles. Independently audit/pin supported framework and deployment dependencies; do not splice donor database schemas together. Chatwoot's PostgreSQL requirement is not a reason to swap ERP databases ad hoc. Databases and queues remain private; only required HTTPS endpoints are exposed. Queue scans/indexing/backups to protect the interactive AOG desk.

[vendor] Chatwoot publishes hardware/dependency requirements; Karrio's hobby deployment recommends 4 GB memory. Component recommendations do not prove combined-stack capacity. [Chatwoot](https://developers.chatwoot.com/self-hosted/deployment/requirements) · [Karrio](https://github.com/karrioapi/karrio/blob/deea10f8568b2d48c71bbcc11ec11c62cdaf2a6a/README.md).

[analysis] **16 GiB RAM, one VPS, no GPU: unbenchmarked budget.** Start without optional index/shipping services until needed. Measure peak memory, imports, concurrency, queue latency, storage growth and restores using representative catalogue/documents. An 8 GiB trial is not approved before those tests. No Kubernetes, local LLM or second identity platform is justified here.

[analysis] The **13 September cost scenario**, not repriced in this continuation, is reference infrastructure **$1,466.40/year** plus assumed maintenance **$1,800/year** = **$3,266.40/year**. It excludes tax, external services, exceptional recovery, guaranteed 24/7 support and the unpriced optional adapters/data discussed below. Client owns VPS/domain/backup account/keys; off-host backup storage is not a SISO-hosted application. [Sourced arithmetic and assumptions](06-value.md).

[analysis] One box is a single point of failure. Keep phone/email duty procedures, exported open-AOG handoffs, tested restore and agreed recovery objectives. Backups do not create high availability. No production AOG SLA is claimed. Retained Shopify, marketplace memberships, transport, accounting and payment settlement are external services, not allegedly self-hosted modules.

## Optional standards-specific adapters — not added to the deployment

[analysis] The twelve new reviews narrow the selection questions; they do not justify running twelve more services. Only introduce an adapter for a confirmed partner contract. The following comparisons are **STUDY**, with no runtime qualification. All factual interface/runtime observations and primary URLs are retained in the [standards review](evidence/standards-boundaries-2026-09-14.md) and [pinned candidate register](04-oss-candidates.json).

| Business need | Inspected alternatives / reference | Decision boundary [analysis] |
|---|---|---|
| Permitted technical-publication processing, W04/W10 | kibook/s1kd-tools | S1000D issue compatibility and source permissions first; not an electronic release-certificate engine. |
| Custody/movement event exchange, W04/W07/W08/W10 | ift-gftc/opentraceability versus openepcis/openepcis-models | Compare .NET and Java libraries on actual EPCIS fixtures. Select normative profiles separately; do not use GS1 draft HEAD as the production contract. |
| Event integration testing | openepcis/epcis-testdata-generator | Synthetic fixtures remain isolated from real stock, customer files and provenance. Resolve selected release build/runtime requirements. |
| Trading-message import/export, W03/W05/W06/W09 | nerdocs/pydifact versus xlate/staedi; phax/ph-ubl for UBL | Python convenience cannot overcome unsupported functional groups. JVM adapters need an explicit contract and resource budget. UBL syntax is not national invoice/tax approval. |
| Partner document transport | OpenAS2/OpenAs2App | AS2 acknowledgement, schema acceptance, commercial acceptance and quality release have distinct states. Keep administration private and qualify retries/certificates. |
| Cargo visibility, W08 | IATA-Cargo/ONE-Record | Specification and version negotiation only; a partner server, shared data and access agreement are still required. |
| Trade-screening assistance, W06 | moov-io/watchman versus opensanctions/yente | Compare coverage, update evidence, matching errors and retained decisions. No engine is a complete export determination. |

[vendor] Watchman's inspected UK downloader uses the current FCDO UKSL feed although the README links the retired OFSI list. Yente requires Elasticsearch/OpenSearch, and OpenSanctions commercial data rights are separate from the MIT software licence. [Watchman adapter](https://github.com/moov-io/watchman/blob/328f7c3bcd4cb7e574440fd08be2f78362a6e5a0/pkg/sources/csl_uk/download_uk.go) · [Yente requirements](https://github.com/opensanctions/yente/blob/3bc1b14ea884aba9f0728d67b76a461f5339dc59/README.md) · [Commercial-data terms](https://www.opensanctions.org/docs/commercial/exemption/).

[analysis] **Screening receipt contract:** persist the subject/queried identity, source and list/version identifiers, retrieval and screening timestamps, candidate matches, reviewer/disposition and linked order. A missing/stale feed leaves screening unresolved. Preserve current UKSL Unique IDs and any source-provided legacy IDs. Watchman's source-code read does not prove successful live refresh; the supported correction is documentation drift, not an alleged broken adapter.

[analysis] **Resource and cost gate:** no new JVM/.NET service, search index or licensed dataset is presumed included in the existing one-box allowance. Measure selected adapters and update the budget before use. Local matching preserves the client application boundary, but authorised data updates and commercial terms remain real dependencies. [Cost boundaries](06-value.md).

## Eight gaps — not proofs of global OSS nonexistence

[analysis] These are unmet boundaries in this research. [Regulatory/workflow context](02-workflow.md) · [Commercial/API context](03-companies.md) · [Research limits](04-oss-candidates.md).

| ID | Gap | Consequence |
|---|---|---|
| G01 | Authorised marketplace feeds, semantics and redistribution rights. | Retain contracts/manual exports; no scraping or paywall-bypass assumption. |
| G02 | Qualified ATA Spec 2000/electronic release-certificate interoperability. | Obtain permitted specifications, test fixtures and partner agreement; XML/GS1/PDF is not enough. Keep release documents distinct from publications, events and cargo messages. |
| G03 | Issuer authority, complete trace, approved alternates and installation eligibility. | Qualified human/customer decisions; no autonomous airworthiness release. |
| G04 | Export classification, end-use/end-user, sanctions and licence determination. | Current jurisdiction-specific advice/data and explicit holds; list matching is insufficient. Screening tools do not close this gap. |
| G05 | Physical stock certainty, supplier reliability, AOG routing/handler/dangerous goods. | Software cannot create inventory, capacity or 24/7 staff. |
| G06 | Validated exchange/core liability, repair disposition and life-limited-part history. | No completeness claim before audited transaction fixtures and approvals. |
| G07 | Qualified accounting/payroll/settlement and final self-hosted storefront. | Retain current authorities; do not count all SaaS as cancelled. |
| G08 | Full research/adoption/licence/security/load/recovery qualification. | 23 of 100 required reviews. Scoped bank reconciliation is done for those identities, not full qualification or production admission. |

## Screens and admission gates

[analysis] Screens: RFQ/duty queue; requirement clarification; supplier comparison; evidence/holds; quote approval; AOG board; receiving/quarantine; shipment history; core/RMA follow-up; margin/cash/admin. Use the existing component bank, not another UI-library sweep. [UI bank](https://github.com/sisodias/siso-component-bank).

[analysis] Before release: authorised pilot proves duplicate-safe ingestion, correct PN/unit links, attachment isolation, accepted quote-version fidelity, hold enforcement, recoverable jobs, original-evidence exports, ledger reconciliation and timed restore. Test malformed PDFs, wrong serials, missing certs, revoked access and concurrent orders. Add normative/draft profile tests, grouped/ungrouped partner messages, synthetic-data isolation, stale-feed handling and reproducible screening receipts. **None of these tests was performed in this research.**

[analysis] Evidence contributes to GQ-004's call-site fitness and GQ-013's coherent replaceable building set; neither question is resolved here. Preserve Great Library Work identity and immutable release/snapshot semantics. Publish research, not a fictitious production release. [Library registry](https://github.com/sisodias/great-library-of-siso/tree/main/registry).
