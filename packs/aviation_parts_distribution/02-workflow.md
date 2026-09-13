# 02 — Ten-stage workflow and the conversation-to-order boundary

Observed 2026-09-13. The stage model, frequencies and control proposals are `[analysis]`; the pain excerpts are `[practitioner]` with attribution and caveats in [01-person.md](01-person.md). JSON is the same table, not an independently measured dataset. [Machine-readable table](02-workflow.json).

| id | stage | trigger | inputs | outputs | pain (quoted + source) | frequency | handoff | data_object |
|---|---|---|---|---|---|---|---|---|
| W01 | Capture and triage | Email, website RFQ or chat arrives | Original message; attachments; contact; airport; required-by time | Owned case; acknowledgement; AOG priority and duty owner | “crashes are inconvenient” [Q02](https://www.capterra.com/p/76813/Quantum-Control/) | 10 customer RFQs/day (hypothesis) | Customer → sales/duty desk | DealCase + TradingParty |
| W02 | Clarify and normalise requirement | Case accepted | PN as supplied; manufacturer; qty/UOM; aircraft context; condition; cert requirement | Confirmed requirement lines; unresolved ambiguities and approved alternate evidence | “Workflow is not intuitive.” [Q07](https://www.capterra.com/p/16508/AeroTrac/reviews/) | 10 cases/day (hypothesis) | Sales ↔ customer maintenance/purchasing | DealCase + PartIdentity |
| W03 | Find supply and fan out RFQs | Requirement is sufficiently defined | Owned-stock view; approved supplier list; authorised locator results | Supplier RFQs; timestamped offers; price/availability/cert comparison | “especially in general aviation.” [Q01](https://www.g2.com/products/partsbase/reviews/) | 30 supplier enquiries/day (hypothesis) | Sales ↔ suppliers and locator services | CommercialDocument + TradingParty + PartIdentity |
| W04 | Review traceability and release evidence | Offer and documents arrive | Original CoC/release PDFs; issuer; PN/SN/lot; ownership/provenance; customer acceptance requirements | Reviewed dossier or named quality hold; expiry/review decisions | “a separate login” [Q08](https://www.capterra.com/p/265431/Veryon-Publications/reviews/) | 5 offer dossiers/day (hypothesis) | Sales → quality reviewer ↔ supplier/customer | EvidenceDossier + PartIdentity |
| W05 | Price and issue a customer quote | Offer and delivery route are credible | Confirmed supply; currency; freight/tax assumptions; core liability; margin policy | Versioned quote, validity, conditions, delivery basis, approval record | “training but is expensive.” [Q03](https://www.capterra.com/p/76813/Quantum-Control/) | 5 customer quotes/day (hypothesis) | Sales → owner/commercial approver → customer | CommercialDocument + DealCase |
| W06 | Accept order and clear commercial/export holds | Customer PO or acceptance received | Accepted quote revision; legal buyer/end user; destination; classification evidence; credit/payment | Sales order and linked PO; authorised decisions or shipment hold | “It does not provide instructions” [Q10](https://arsa.org/recordkeeping-guidance/) | 3 accepted orders/day (hypothesis) | Sales ↔ finance/export adviser ↔ customer | CommercialDocument + TradingParty + EvidenceDossier |
| W07 | Procure, reserve and receive | Order authorised for procurement | Purchase order; expected unit/lot; delivery and certificate terms | Reservation/receipt; accepted physical identity; quarantine or discrepancy | “Parts and inventory are very difficult” [Q04](https://www.capterra.com/p/147614/Quantum-MX/reviews/) | 3 orders/day; direct-ship and stock-receipt branches | Buyer → supplier → stores/quality | Fulfilment + PartIdentity + EvidenceDossier |
| W08 | Pack, dispatch and prove delivery | All dispatch holds cleared | Released item; packing/doc set; named consignee/handler; carrier confirmation | Shipment/airwaybill; milestones; proof of handoff/delivery | “the list included bin location.” [Q06](https://www.capterra.com/p/142475/Veryon-Tracking/reviews/) | 3 dispatches/day (hypothesis) | Stores → forwarder/courier → handler/customer | Fulfilment + EvidenceDossier |
| W09 | Invoice, reconcile and administer | Shipment/payment/supplier invoice event | Order and receipt; invoice; bank/payment/FX facts; payroll/admin calendar | Matched ledger entry; receivable/payable; discrepancy task; month-end export | “edging out the smaller operators” [Q09](https://www.capterra.com/p/265431/Veryon-Publications/reviews/) | 3 order reconciliations/day; monthly payroll/close | Finance ↔ bank/accountant; owner approves exceptions | CommercialDocument + TradingParty |
| W10 | Manage returns, cores and retention | Return request, core due date or audit query | Original serial/lot and sale; return terms; repairer disposition; evidence history | RMA/core credit; stock disposition; customer resolution; auditable closed case | “Inventory and maintenance tracking are completely separate.” [Q05](https://www.capterra.com/p/7377/Aircraft-Maintenance-Systems/reviews/) | 5 returns/core follow-ups/week (hypothesis) | Customer ↔ sales/stores/repairer ↔ finance | Fulfilment + EvidenceDossier + CommercialDocument |

## The chat surface is part of the transaction

[vendor] APE publicly exposes email, a website RFQ journey and live chat. Its AOG instructions request the aircraft, part and airport details needed to begin sourcing. **We did not verify APE use of WhatsApp, Instagram DMs or SMS.** [APE](https://www.aircraftpartseurope.com/) · [AOG instructions](https://www.aircraftpartseurope.com/pages/business-private-jet-aog-support-uk-europe-global).

[vendor] Comparable suppliers expose WhatsApp and structured RFQ uploads. Aeronova accepts PDF, XLS/XLSX, CSV, DOC/DOCX, TXT and ZIP uploads; Aerogate's RFQ form captures urgency, conditions and release requirements. That is evidence for optional channel/file adapters, not evidence about APE's installed stack. [Aeronova](https://aeronova.ae/) · [Aerogate RFQ](https://www.aerogateafrica.com/rfq).

[analysis] One named sourcing coordinator owns the conversation; a duty backup owns escalation. Proposed staffed-hours acknowledgement is five minutes, with a separate target for a *qualified* quote after missing information is resolved. Do not advertise 24/7 coverage merely because software runs continuously. Measure actual coverage and response percentiles first.

[analysis] Five repeated intents to validate against mailbox samples: **Do you have this exact part and quantity? Which condition and release documents are available? What is the delivered price and quote expiry? Can it reach this airport/handler by this time? Where is my shipment/core credit?** These are design hypotheses derived from supplier RFQ fields, not a measured top-five intent distribution. [RFQ evidence](https://www.aerogateafrica.com/rfq).

[analysis] Conversion happens at **W01 → W02**: retain Message-ID/channel ID, immutable original attachment and customer identity, then create a DealCase and requirement lines without retyping. At **W05 → W06**, an acceptance must identify the exact quote revision; a conversational “yes” cannot authorise a different price, unit or delivery promise. Messages remain linked through fulfilment and returns.

## Controls attached to stages

- **W01:** [analysis] Acknowledge within 5 minutes during staffed cover (target, unmeasured); escalation must have a named backup.
- **W02:** [analysis] Keep raw PN and normalised search key; never erase dash/suffix meaning or accept an alternate from string similarity.
- **W03:** [analysis] Human chooses recipients; preserve source/listing age and avoid leaking one supplier’s terms to another.
- **W04:** [analysis] A readable form is not authentic evidence; valid release is not installation approval.
- **W05:** [analysis] Quote does not silently clear outstanding quality/export/credit holds.
- **W06:** [analysis] Sanctions matching is one check, not a complete EAR/ITAR/UK export determination.
- **W07:** [analysis] Catalogue listing, supplier promise, physical receipt and released stock are different states.
- **W08:** [analysis] AOG priority cannot override physical safety, dangerous-goods or export checks.
- **W09:** [analysis] Keep statutory accounting/payroll authority in the current package until local requirements and reconciliation tests pass.
- **W10:** [analysis] A returned item never becomes saleable through a stock-count correction alone.

[analysis] The shared objects recur across all ten stages, so a super-app is plausible. Accounting, payroll and external market networks remain bounded external authorities; their presence does not justify unrelated duplicate CRMs or task databases. The six aggregates and ownership rules are specified in [05-superapp.md](05-superapp.md).

## Evidence boundaries for release and export checks

[vendor: regulator] EASA's Form 1 instructions distinguish the certificate from approval to install. FAA Order 8130.21J, issued 25 September 2025, is active and addresses completion under Part 21. The maintenance-release path must not be inferred from that order alone. [EASA instructions](https://www.easa.europa.eu/en/document-library/easy-access-rules/online-publications/easy-access-rules-initial-airworthiness-and?page=34) · [FAA order record](https://www.faa.gov/regulations_policies/orders_notices/index.cfm/go/document.information/documentID/1044438).

[vendor: regulator] UK controls include specified goods, software and technology; US EAR scope can include reexports. Hosting on a UK/client VPS is not a classification, end-use, licence or reexport determination. [UK export controls](https://www.gov.uk/guidance/export-controls-military-goods-software-and-technology) · [BIS EAR 734](https://www.bis.gov/regulations/ear/734).

[analysis] The system records qualified decisions and blocks prohibited/unresolved dispatches. It neither fabricates certificates nor issues regulatory release approval, and an AOG timer never supplies an override.
