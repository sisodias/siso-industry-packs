# 05 — Assemble a restaurant operating layer, not another website

**As of 2026-09-13 UTC. Research blueprint; no application implementation or deployment.** Machine-readable plan: [05-assembly.json](05-assembly.json). This design is **[analysis]** throughout unless a source capability is explicitly labelled **[vendor]**. Sources and pinned revisions for every candidate are in [04-oss-candidates.json](04-oss-candidates.json). ADOPT means a conditional research selection for assembly, **not production admission, a passed runtime test or permission to deploy**.

## Decision: one useful door, then a coherent core

Preserve the existing marketing site and its landing, menu, review and about-us work. The supplied [project brief](README.md) explicitly says it does not supply POS, orders, stock, staffing, bookings or supplier management. The first proposed addition is an **assigned enquiry-to-booking handoff with visible exceptions**, not replacement of the till. Keep the incumbent payment, kitchen, payroll and accounting authorities until their replacements independently earn acceptance.

Start with **Chatwoot plus OpenResto only if the client baseline supports that wedge**. OpenResto is the booking authority; Chatwoot holds the conversation. A small integration record links the two and separately records confirmation delivery. A booking that already exists must not be recreated because a message failed. The existing website links or embeds the accepted booking surface; it is not rebuilt.

[vendor] OpenResto documents scoped admin API keys, booking creation and cancellation, conflict responses and email-status/failure endpoints. It says confirmation email is best-effort and booking creation can succeed when sending fails. These are source claims to test, not demonstrated behaviour in this research. [Pinned API contract](https://github.com/karanshukla/openresto/blob/38c4a129090badc005d4e03b8be127ac9a92bcbd/docs/http-api.md). Its README describes temporary in-memory table holds; restart, race and multi-process behaviour are mandatory qualification tests. [Pinned README](https://github.com/karanshukla/openresto/blob/38c4a129090badc005d4e03b8be127ac9a92bcbd/README.md).

## The six-object spine is an integration contract

Reuse domain schemas rather than rebuilding donor applications. The spine is an index of authoritative IDs, versions, relationships and approvals. It must not copy every database into a competing universal ledger. [Stage 2](02-workflow.md) defines the six aggregate families:

| Family | The connection the assembly owns | Domain authority retained |
|---|---|---|
| Party | Client-scoped external-ID mapping for guests, employees and suppliers | Each module owns its required fields and permissions; no cross-client identity graph or name-only merging. |
| ServiceCase | Original enquiry linked to distinct reservation, waitlist and order state machines | Booking system owns accepted capacity; order/POS system owns accepted orders. |
| ProductDefinition | Versioned mapping from supplier item and pack to ingredient, recipe, modifier and menu item | Approved recipe/menu source, never a public food database or inferred allergen answer. |
| StockMovement | Source IDs and reversal lineage for receipts, use, waste and counts | One chosen stock ledger, not both ERPNext and Odoo. |
| WorkRecord | Typed shift, kitchen task, check, exception and approval references | Employees, chefs and safety owners retain separate actions and access. |
| FinancialRecord | Invoice/credit, order/payment/refund, fee/payout and export references | Approved processor, accountant and payroll system; monetary state is not inferred from a screen status. |

The essential joins are conversation→reservation/order, order→kitchen→payment, supplier pack→ingredient/recipe→stock, and sale/refund/fee→payout. HR and safety remain adjacent modules. A common navigation shell does not make them one authority domain. If AC's actual work does not benefit from these joins, use a simpler suite or incumbent configuration instead.

## Component map: why these beat the alternatives

The named capabilities below are **[vendor]** descriptions supported by the linked upstream source. Selection, exclusions and proposed glue are **[analysis]**. All choices still require version, rights, security, support and behavioural review.

| Workflow | Conditional choice and role | What we would write or configure | Why it beats the named runners-up for this scenario |
|---|---|---|---|
| W01 enquiry/chat | **Chatwoot — ADOPT**; shared conversation queue. [Source](https://github.com/chatwoot/chatwoot) | Approved channel setup, external-ID mapping, assigned enquiry, review screen, safe outbound acknowledgement and reconciliation. | Broader conversation orientation than an email-only setup. **FreeScout** or **LibreDesk** can win if the real need is only email and lower resource use matters; do not promise every channel or SSO edition by default. |
| W02 staffing | **Frappe HRMS — ADOPT for expanded module**, not first-pilot necessity. [Source](https://github.com/frappe/hrms) | Role/availability mapping, acknowledged shifts, approved timesheet export and country-specific rules. | Shares the prospective Frappe back office. **Horilla** is the independent HR alternative; **Kimai** is primarily time capture; **Timefold** is an optimiser, not a complete rota product. |
| W03 purchasing/receiving | **ERPNext + invoice2data — ADOPT conditionally**. [ERPNext](https://github.com/frappe/erpnext) · [invoice2data](https://github.com/invoice-x/invoice2data) | Supplier aliases, units/cases, invoice templates, receipt/invoice/credit match and human review. | ERPNext supplies a business ledger rather than **Grocy/KitchenOwl** household shopping. **Odoo + OCA purchasing/stock** is the credible whole-stack runner-up, not an additional ledger to run simultaneously. |
| W04 recipes/prep/availability | **ERPNext BOM foundation — ADOPT; URY — STUDY/qualify first**. [URY source](https://github.com/ury-erp/ury) | Effective recipe versions, yield/portion conversion, waste, modifiers and approved channel availability. | **Tandoor/Mealie** are useful recipe UX, not demonstrated supplier-to-COGS control. URY advertises the restaurant-specific join, but compatibility and actual depletion behaviour must be reproduced before relying on it. |
| W05 safety records | **ODK Central + released ODK Collect — ADOPT optionally**. [Central](https://github.com/getodk/central) · [Collect](https://github.com/getodk/collect) | Operator-approved forms, roles, check schedule, corrective-action routing, version control and review. | Explicit forms/offline companion rather than a generic survey screen. **KoboToolbox** is a heavier alternative; **LimeSurvey** is suitable only where its online survey model meets the actual workflow. None supplies a legal or safety determination. |
| W06 tables/bookings | **OpenResto — ADOPT subject to acceptance tests**. [Source](https://github.com/karanshukla/openresto) | Enquiry→approved booking link, overlap tests, email outcome, cancellation/retry handling and host exception queue. | Restaurant tables are the native objects, unlike **Easy!Appointments/LibreBooking** general slots/resources. **Cal.diy** explicitly recommends personal non-production use; **TastyIgniter** is the alternative when one ordering/reservation product is preferred. Do not run duplicate booking authorities. |
| W07 orders/payment | **Retain incumbent; TastyIgniter — ADOPT only as optional direct-order component**. [Source](https://github.com/tastyigniter/TastyIgniter) | Menu/modifier mappings, accepted order handoff, reconciliation and processor references; no card-data storage. | Existing restaurant ordering rather than a tutorial clone. **OpenSourcePOS** is a retail-oriented alternative; **Enatega** visible frontends do not establish the separately licensed/private backend needed for a complete self-hosted stack. |
| W08 kitchen/printing | **Retain incumbent KDS; URY — STUDY; python-escpos — ADOPT library where needed**. [URY](https://github.com/ury-erp/ury) · [python-escpos](https://github.com/python-escpos/python-escpos) | Versioned tickets, station acknowledgement, idempotent print jobs, explicit reprints and physical-device qualification. | URY is the integrated qualification target, not its superseded separate POS/Mosaic apps. **ReceiptLine/ReceiptIO**, **escpos-php** and **Star CloudPRNT SDK** are transport/layout alternatives selected by actual host and printer, not extra always-on services. |
| W09 delivery/collection | **Retain approved channel interfaces; no complete OSS aggregator connector admitted** | Import approved order/status/export evidence; ready/collected states, handoff identity and manual exception fallback. | **CoopCycle** serves courier-cooperative workflows, not automatic access to Uber/Deliveroo/Just Eat. Tutorial partner APIs are not real marketplace integrations. |
| W10 close/payout | **ERPNext references + deterministic format adapters under study; no turnkey three-marketplace reconciliation claimed** | Order/refund/fee/tip/tax/payout mapping, period boundaries, discrepancies and approved posting. | **ofxparse/ofxgo/bankstatementparser/Peppol-UBL** address specific formats, not the entire restaurant settlement model. **Firefly III** is personal finance; **OCA account-reconcile** belongs to the alternate Odoo route. |
| W11 accounts/payroll | **ERPNext/HRMS export preparation; retain accountant/payroll authority** | Accepted chart-of-accounts and pay-period mapping, approval, acknowledgement and reversible export. | Avoid mistaking an HR module for verified local payroll. **Manager** is an accounting alternative to review with the accountant, not an automatically accepted replacement. |
| W12 follow-up/loyalty | **listmonk — ADOPT optional email follow-up; no merchant loyalty ledger admitted**. [Source](https://github.com/knadh/listmonk) | Consent/suppression, verified recipients, approved campaigns and any separately justified reward ledger. | Smaller email-focused surface than **Mautic**. **Catima** is a consumer card wallet; **Quickstamp** offers a short-lived QR/redemption pattern to study, not an audited merchant liability system. |

## Version and authority traps

[vendor] URY's current source warns that backward compatibility is not guaranteed during active development. Its installation document specifies ERPNext version 15 and requires Frappe HR. The current source also says support for the older separate POS/Mosaic v1 applications ended in December 2025. [README](https://github.com/ury-erp/ury/blob/71b59edac14ea4c7ce4a108b4ea1bdf714803fb5/README.md) · [installation](https://github.com/ury-erp/ury/blob/71b59edac14ea4c7ce4a108b4ea1bdf714803fb5/INSTALLATION.md). [analysis] A fresh HEAD from each repository is not a compatible bill of materials. Select supported release branches, lock exact revisions, build in isolation and replay the same fixtures. This research performed no such build.

[vendor] Chatwoot documents REST and webhook interfaces, but its conversation-infrastructure page says missed webhook events have no replay mechanism or delivery dashboard. [Source](https://www.chatwoot.com/use-cases/conversation-infra). [analysis] Keep an event inbox and reconciliation cursor; detect gaps by querying authorised current state. Do not promise exactly-once delivery. OpenResto confirmation failure likewise must not cause another reservation.

## Honest glue work

Use allow-listed adapters with per-module service identities and explicit permissions. One front door is not proof of donor SSO support: preserve donor login until a supported authenticated handoff is verified. Avoid sharing browser session cookies, embedding administrator keys or bypassing module authorisation. Guest access must not reveal staff, payroll, supplier contracts or another customer's details.

Every ingested event needs source, object ID, version or timestamp, idempotency key, processing outcome and retry state. An outbox records intended approved external changes; a reconciliation job checks acknowledged state. Out-of-order cancellation, order edits and partial refunds need explicit state transitions. A failed or ambiguous response goes to an assigned exception, not an invented success. Store attachments under client-controlled permissions with size/type checks and retention; preserve invoice and credit provenance without forwarding them to an external OCR/model service by default.

The difficult data mapping is supplier case→unit→ingredient→recipe yield→sold portion/modifier. Compare quantity and money separately, retain currency and period, and never rewrite historical sales when recipes or prices change. Keep order acceptance, kitchen acceptance, payment authorisation, settlement and accounting posting as different events. The small bespoke part is these mappings and approvals; **its percentage and engineering cost are unmeasured**, not automatically 5%.

## Client-owned deployment and architecture

**One application VPS per client, in the client's account. No SISO-hosted client data plane.** Separate services and databases may coexist on that one host. Client-owned backup storage is a separate durability destination, not a second shared application server. Native browser/tablet/Android or printer companions can run on the client's devices; they are not additional SISO-hosted infrastructure.

```text
Existing marketing site / approved message channels
                 |             |
         OpenResto bookings   Chatwoot conversations
                 \             /
          Client-owned integration records
       source IDs | approvals | inbox/outbox | exceptions
                          |
          retained POS / processor / kitchen routes
                          |
       optional later modules on the same client VPS
       TastyIgniter direct orders (not duplicate bookings)
       ERPNext + compatible HRMS; URY qualification branch
       ODK Central; listmonk; local deterministic parsers
                          |
      client-owned databases, files and tested backups
                          |
       authorised external channels / accountant / payroll
```

Use TLS at the edge, private database/cache ports, separate module accounts and data directories, least-privilege backups and explicit version pins. Keep original domain databases authoritative. The integration index must be exportable and reconstructable from source references and accepted event history. Do not host a second global customer/people database.

[vendor] TastyIgniter's installation requirements specify PHP 8.3+ and MySQL 8 or MariaDB 10.6. [Source](https://tastyigniter.com/docs/installation). Chatwoot recommends 8GB+ RAM for production on its own. [Source](https://developers.chatwoot.com/self-hosted). ODK's low-volume installation can start smaller, but exports/media and migrations affect requirements. [Source](https://docs.getodk.org/central-install/) · [troubleshooting](https://docs.getodk.org/central-troubleshooting/).

[analysis] **Planning, not benchmark:** test an 8GiB reduced inbox/booking host and a 16GiB expanded host; do not infer that all optional modules fit from these numbers. The published 16GiB DigitalOcean Basic reference is $96/month, and daily percentage-based backups add 30%: **$1,497.60/year** before support, application-aware recovery, channel fees, taxes or other costs. [VM price](https://www.digitalocean.com/pricing/droplets) · [backup price](https://www.digitalocean.com/pricing/backups). [Stage 6](06-value.md) preserves the distinction between this budget and complete operating cost. No GPU or hosted AI service is assumed.

A remote VPS cannot directly control a USB kitchen printer. Select an approved local companion, private connection or supported polling printer protocol. Do not expose printer ports to the public internet. Internet or VPS failure must leave the retained till/payment route and an agreed manual kitchen fallback usable. One box is a failure domain; no high-availability or offline guarantee was demonstrated. Database-aware restore and an application rollback test are required, not just a successful disk-backup setting.

## Twelve unresolved gaps

Each is **[analysis]**, a limitation of the examined evidence and proposed assembly, not a universal claim that no OSS exists.

| Gap | What is still missing / acceptance evidence |
|---|---|
| G01 Client fit and baseline | AC's actual jurisdiction, channels, service mix, incumbent systems, invoices, volumes and owner-approved wedge. |
| G02 Commercial channel access | Approved marketplace/WhatsApp accounts, scope, terms and permitted exports. Uber production scopes and Deliveroo onboarding are external gates. [Uber](https://developer.uber.com/docs/eats/guides/authentication) · [Deliveroo](https://developers.deliveroo.com/). |
| G03 Payment and fiscal devices | Approved processor/till/tax and cash/tip semantics, hardware compatibility, reversals and country acceptance. |
| G04 Peak service and failure recovery | Actual load, printer routing, lost WAN, host restart, no duplicated kitchen work and tested manual fallback. |
| G05 Table capacity and confirmation | Race/restart behaviour, host pacing/waitlist requirements, no duplicate booking and independent delivery status. |
| G06 Restaurant recipe costing | Accepted pack conversions, yields, wastage, recipe versions and modifier-to-depletion fixtures. |
| G07 Supplier document coverage | Real invoice/credit/receipt templates, ambiguous units, OCR exceptions and verified supplier identity. |
| G08 Three-marketplace settlement | Accepted Deliveroo/Uber Eats/Just Eat payout schemas and fee/refund/tax mapping; bank parsing alone is insufficient. |
| G09 Food-safety authority | Approved procedures/forms, trained measurement, corrective actions, audit trail and local professional review. |
| G10 Payroll/accounting and loyalty | Local payroll/accountant acceptance, consent and reward-liability handling; no autonomous approvals. |
| G11 Version, rights and support | Compatible released components, directory/edition terms, security review, operational ownership and restoration. |
| G12 Research completion | Two genuinely dry discovery rounds, stronger adoption/maintainer evidence and remaining unsourced workflow-specific complaints; current three rounds were not dry. |

## Verification before any pilot or cutover

Run a reversible fixture pilot with synthetic or expressly authorised redacted data. Tests must include duplicate and out-of-order messages; wrong-recipient and revoked-key rejection; two simultaneous holds on one table; restart during a hold; booking succeeds/email fails; order amendment and printer reprint; sold modifier/recipe-version/pack conversion; partial refund and payout-period mismatch; approved payroll/export reversal; offline form sync; and complete database/file restoration. Record expected outputs, actual results and named acceptance. None is marked passed in this blueprint.

Only after the bounded handoff beats the existing/free configuration on matched human effort and preserved quality should the expanded back office be considered. The choice is **lift first, integrate explicitly, preserve authority, and add a module only when its measured benefit pays for its operational burden**.
