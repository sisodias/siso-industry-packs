# 03 · Companies, tier gap and stack tax

Observed **2026-09-13**. **10 Tier-1 companies and 10 Tier-2 offerings.** Company research preceded upstream repository discovery. This is the GitHub review edition; it is a capability comparison, not a market-share ranking.

[analysis] USD before tax unless stated; regular rather than temporary promotional prices. Distinguish annual commitment, annual invoice and month-to-month billing. Five workers do not necessarily require five office licences. Unknown prices/entitlements stay unknown, not zero. Recheck procurement quotes.

## Tier 1 — capability ceiling

[vendor] Product lines, serving segments and prices below are vendor claims from the linked sources. [analysis] The human role and integration cautions are our requirements, not evidence that each vendor fully automates everything else.

| Company / official source | Product and service scope; customer | Pricing | Automated administration [vendor] | Human work and integration boundary [analysis] |
|---|---|---|---|---|
| [Procore](https://www.procore.com/pricing) | Owners, GCs and specialty contractors; project management, financials, preconstruction, field productivity, resources and documents | Annual quote by products/construction volume; five-person price unknown | Workflow routing and connected project/financial/field records | People scope, code costs, interpret field evidence and approve; verify API/export and collaborator entitlements |
| [Autodesk](https://construction.autodesk.com/) | Design/construction teams; Construction Cloud capabilities presented within Forma, documents, coordination and field/project execution | Selected US package unknown | Connected documents and project coordination | Professional design/approval stays human; preserve ACC/Forma project/document IDs; selected platform rights unverified |
| [Trimble](https://www.trimble.com/) | Contractors/design/infrastructure; Construction One/Viewpoint, ProjectSight, Vista/Spectrum, Connect and separate design families | Suite configuration quote unknown | Project/ERP coordination and cost mappings | ERP setup, purchasing/survey/design decisions; one subscription does not imply the whole portfolio or one API |
| [Oracle](https://www.oracle.com/construction-engineering/) | Capital-project owners/EPCs/contractors; Aconex, Primavera Cloud/P6, Unifier, Textura, Construction Intelligence, Submittal Exchange | Product/licence quote; amount unknown | Document routing, scheduling, project controls and payment administration | Schedulers, contract administrators and approvers; preserve schedule/document/commercial identities; API varies by product |
| [Bentley](https://www.bentley.com/products/synchro-4d) | Infrastructure/design/delivery; SYNCHRO 4D, ProjectWise and related products | SYNCHRO 4D starts $4,980/year for one 12-month Virtuoso licence plus two training/service Keys; not a suite/five-seat quote | Model/schedule coordination and 4D sequencing | Planners validate models/progress; desktop specialist tools are not resident VPS modules |
| [Sage](https://www.sage.com/en-us/sage-construction/) | Contractors; 100 Contractor, 300 CRE, Intacct Construction, estimating, field, HCM and document partners | Modules/users/features quote; amount unknown | Job costing, procurement, payroll and financial administration | Accountants/payroll reviewers/estimators and implementation partners; preserve cost codes/history; partner integration is not unrestricted API proof |
| [Nemetschek / Bluebeam](https://www.bluebeam.com/pricing/) | AEC reviewers; Revu and web/mobile collaboration | Basics $260, Core $330, Complete $440/user/year; Max $590 introductory. Two Core $660/year | PDF markup, measurement/comparison and tier-dependent batch/quantity workflows | People calibrate scale, interpret scope and approve quantities; retain annotation/tool-set fidelity |
| [CMiC](https://cmicglobal.com/products/) | Construction ERP/project controls; finance, payroll/HCM, equipment, inventory, procurement, documents and field | Custom quote; amount unknown | Integrated project/financial transaction workflows | Finance, HR and project approval; historical/master-data mappings and integration contract require review |
| [InEight](https://ineight.com/) | Complex capital projects; estimating, controls, contract/change, planning/progress and documents | Product configuration quote; amount unknown | Cost/change coordination and ERP-linked controls | Estimators/controls professionals/approvers validate inputs; integration and small-crew entitlement unverified |
| [RIB](https://www.rib-software.com/en/) | AEC estimating/delivery/specification; 4.0, Candy, CostX, BuildSmart, Connex/CX, Civil, Project, SpecLink/SpecLive and handover families | Per-product quote/licence; amount unknown | Takeoff/estimating, procurement, cost and document coordination | Professional takeoff/specification/contract review; portfolio products are not one interchangeable API |

## Tier 2 — small-operator offering

[vendor] Prices and capabilities below are vendor claims. [analysis] Every row still requires an owner to set scope/prices, approve work/payment and review exceptions; technical integration and migration have not been tested.

| Offering / official source | Product line and customer | Price at specified configuration | Automation / human service | Integration and lock-in questions |
|---|---|---|---|---|
| [JobTread](https://www.jobtread.com/pricing) | Remodelers/builders/trades: CRM, estimating/takeoff, bids, contracts, POs, changes, schedule/time, job cost, selections, portal, warranty | Five internal users: (199+4×20)×12×0.8 = **$2,678.40/year**. Two internal $2,102.40. Limited field/external users free; timekeeping needs internal access | Templates, linked records/reminders; onboarding/training/support | QBO, Gusto, Zapier listed; public API plan rights and complete exports unverified |
| [Buildertrend](https://buildertrend.com/pricing/) | Homebuilders/remodelers/trades: sales, proposals, schedule/time, financials, POs/changes, selections, portal/warranty | **Tailored quote, unknown**; unlimited users/projects advertised. Historical $800 complaint is not a current list price | Connected sales/project/customer/financial workflows; onboarding/migration support | QBO/Xero/Gusto integrations; verify signed-document, message and attachment export/API rights |
| [Contractor Foreman](https://contractorforeman.com/) | Small/medium contractors: estimates, projects, daily logs, schedules/time, POs/changes, docs/RFI/submittals, safety/permit tracking | From $49/month annual; Standard 3 users, Plus 8, Pro 15. **Exact five-person Plus price unknown**; [seat source](https://kb.contractorforeman.com/knowledge-base/billing-manage-users-and-storage/) | Administrative coordination and training; safety/permit decisions remain human | Listed integrations do not establish delivery of announced features, general API access or record fidelity |
| [Houzz Pro](https://www.houzz.com/houzz-pro/pricing) | Residential design/build: leads/CRM, estimates/bids/takeoff, proposals/signatures, invoices/POs/changes, budget/time, schedule/logs, portal | Selected USD/seat price **not reliably rendered; unknown** | Lead/project/document administration; plan-specific training/support | QBO sync advertised; seats, API and full history export unverified |
| [Jobber](https://www.getjobber.com/pricing/) | Service trades: CRM, quotes, visits/dispatch, invoices, time, client hub/reminders; higher tiers costing/SMS/marketing/reception | Connect 5 users **$149/month annual = $1,788/year**; Grow 5 $229/$2,748; Plus 5 $399/$4,788 | Dispatch and follow-up automation; higher-tier onboarding | Connect QBO; exact API entitlement needs confirmation; visit/job model is not full GC contract control |
| [Housecall Pro](https://www.housecallpro.com/pricing/) | Home-service contractors: booking/dispatch, estimates/invoices/payments, customer/time/comms; higher tiers proposals/recurring service | Essentials 5 **$149/month annual = $1,788/year**; Max 8 $299/$3,588 | Reminder/dispatch administration; technicians still diagnose/perform work | Essentials QBO; **Open API and Zapier in Max**; preserve service/job/financial IDs |
| [Joist](https://www.joist.com/pricing/) | Independent contractors: estimates/invoices/payments/client records; Elite changes/reporting; Run broader job management | Elite **$32 month-to-month = $384/year per quoted account**; five-person team rights not verified | Document/payment-status administration; owner measures/prices/approves | QBO/payment connections; team/API/export rights unverified |
| [Buildxact](https://www.buildxact.com/us/pricing/) | Builders/remodelers: takeoff/estimating, dealer/supplier quotes/POs; Pro scheduling/mobile/job management | Exact annual invoices: Foundation **$2,030**, Pro **$4,070**, Master **$6,110**; unlimited users advertised | Linked estimate/purchasing administration and onboarding | Quantities/exclusions require review; dealer/accounting integration tier and API/export contract unverified |
| [Buildern](https://buildern.com/pricing) | Builders/contractors: CRM/estimate/bids/POs/invoices; Pro time approvals/mobile/RFI/submittals/selections/sync | Starter 2 office **$225/month annual = $2,700**; Pro 4 office **$360 = $4,320**; fifth office +$90/month. Field/sub/client/vendor accounts free | Linked preconstruction/commercial/field administration; onboarding/migration assistance | Pro QBO/Xero two-way sync; general API rights unverified; five office users are not four office plus field |
| [Projul](https://projul.com/pricing/) | Contractors: CRM, estimating/changes/invoices, schedule/time/photos/docs; higher-tier reporting/purchasing/costing | Core 8 **$4,788/year**; Core+ 20 $7,188; Pro 50 $14,388; Unlimited $19,188 | Schedule/commercial-record coordination and onboarding/training | QBO/JustiFi/1build; Zapier in Pro; do not assume Core includes Pro functions |

## The gap between tiers

[analysis] The ceiling includes deep project controls, document/model identities, procurement, finance and collaborator workflows. Small-team offerings already cover much of the administrative map; this is **not an unserved dashboard market**. Potential differentiation is preserving evidence and approval across real channels with less configuration/coordination cost. Enterprise feature breadth does not prove a small firm needs every feature. Per-seat/tier integration rights and field participation can matter more than headline price. P04/P09 demonstrate reported setup/participation friction, not universal vendor failure; see their linked quotations in Stage 1.

## Unglamorous tools and real switching costs

| Layer / source | Price observed | Operator-specific configuration and implication [analysis] |
|---|---|---|
| [QuickBooks Online](https://quickbooks.intuit.com/pricing/) | Plus **$140/month** | $1,680/year; retain ledger/accountant authority and reconcile any import/export |
| [Gusto](https://gusto.com/product/pricing) | Simple $49 + $6/person/month | Five payroll people: **$948/year**. Plus $80+$12/person = $1,680/year; review state/feature fit |
| [Workspace / Sheets / Gmail / Calendar](https://knowledge.workspace.google.com/admin/getting-started/editions/business-editions) | Starter $7/user/month annual, $8.40 flexible | Five annual Starter users **$420/year**; retain email/calendar; preserve sheet formulas/scripts |
| [Microsoft 365 / Excel](https://www.microsoft.com/en-us/microsoft-365/blog/2025/12/04/advancing-microsoft-365-new-capabilities-and-pricing-update/) | July 2026 change announcement; selected region/Teams/SKU quote unverified | Annual price **unknown**, not an older price silently reused. Excel cost-code cross-checks are practitioner evidence |
| [Airtable](https://airtable.com/pricing) | Team $20/editor/month annual | Two editors $480/year; five $1,200. Preserve linked IDs, automations and attachments, not just visible cells |
| [Notion](https://www.notion.com/pricing) | Plus $10/member/month displayed annual selection | Two editors $240/year; five $600. Page status is not approval authority |
| [monday.com](https://monday.com/pricing) | Multiple product matrices; chosen work-management SKU not isolated | Price **unknown**; do not substitute CRM/dev price |
| [ClickUp](https://clickup.com/pricing) | Unlimited $7/user/month annual; Business $12 | Five $420/$720/year; contractor-specific approval/cost-code relationships still required |
| [WhatsApp Business](https://business.whatsapp.com/products/business-app) | Selected app/platform configuration and charges unverified | Optional channel, not evidenced dominant in this US segment; client owns account/number |
| [Twilio US SMS](https://www.twilio.com/en-us/sms/pricing/us) | Long code $1.15/month; $0.0083/inbound or outbound base segment | 500+500 segments/month: **$113.40/year base**, plus carrier/A2P/other charges |
| [Docusign](https://www.docusign.com/products/electronic-signature/plans-and-pricing) | Standard $25/user/month annual, 100 envelopes/user/year | Two senders **$600/year**; API contract and excess-envelope treatment separate; may duplicate suite signing |
| [Bluebeam](https://www.bluebeam.com/pricing/) | Core $330/user/year | Two reviewers $660/year; do not claim replaced until markup/takeoff fidelity passes |
| [CompanyCam](https://companycam.com/pricing) | Reliable dollar amount not rendered | **Unknown**; preserve photo originals/exports and test field usability |
| [Stripe](https://stripe.com/pricing), [Square](https://squareup.com/us/en/pricing), ACH/check/cash | Selected US transaction rates unverified | Variable processing costs **unknown**, not zero. Settlement/merchant rails cannot be self-hosted by installing an app |
| Paper, calls, whiteboard, memory | No software subscription assumed for existing manual surface | Not zero organizational switching cost; [practitioners describe calls/in-person/Excel](https://www.reddit.com/r/Contractor/comments/vz3blu/what_all_do_you_use_to_createrecordprocess_change/) |

## Per-stage alternatives and evidence

[analysis] Annual configurations reference the profiles above; U means unknown, not free. Repeated appearances are the same subscription, not additive charges. Pain is stage-level practitioner evidence, not a reproduced defect of every listed tool.

| Stage | 2–5 incumbent alternatives/layers | Pain reference | Integration/lock-in to test |
|---|---|---|---|
| W01 | JobTread $2,678.40; Jobber $1,788; Workspace $420; WhatsApp U | P01 | Number/email ownership; party-to-site matching; inbox rights |
| W02 | Bluebeam $660; Houzz U; Buildxact Pro $4,070; Excel U | P07 | Original plans, calibrated scale, markups, site/billing distinction |
| W03 | JobTread $2,678.40; Buildxact $4,070; Buildern $4,320; Sheets within Workspace | P05 | Cost codes, exclusions, revisions, formula/price provenance |
| W04 | Buildertrend U; JobTread $2,678.40; Houzz U; Docusign $600 | P01/P02 | Exact signed revision, parties, envelope/deposit evidence |
| W05 | Contractor Foreman Plus U; Buildern $4,320; Sage U; QBO $1,680 | P07 | POs, delivery sites, supplier files, document/permit status |
| W06 | Projul $4,788; Jobber $1,788; HCP $1,788; Calendar within Workspace | P09 | Task/event IDs, acknowledgement, holds and readiness |
| W07 | CompanyCam U; JobTread $2,678.40; HCP $1,788; Gusto Plus $1,680 | P08 | Offline queue, originals, time approval, payroll mapping |
| W08 | Buildertrend U; JobTread $2,678.40; Joist $384, team rights U; Excel U | P01/P02 | Request versus approval; immutable revision; field release |
| W09 | QBO $1,680; Gusto Simple $948; Buildern $4,320; Sage U | P03 | Authoritative ledger/payroll; idempotent export/reconciliation |
| W10 | JobTread $2,678.40; Buildertrend U; Airtable two editors $480; Gmail within Workspace | P01 | Complete archive, manuals, acceptance and reopening history |

## STACK TAX

[analysis] **Core chosen basket:** $2,678.40 + $1,680 + $948 + $420 = **$5,726.40/year**. Expanded with two Bluebeam Core and two Docusign Standard senders: $5,726.40 + $660 + $600 = **$6,986.40/year**. These are hypothetical bills, not client invoices. Exclude tax, transaction fees, phones, implementation and unknown specialist tools explicitly.

[analysis] **Literal buy-everything total is unknown.** The duplicative subtotal of the seven numerically priced Tier-2 configurations is $2,678.40+$1,788+$1,788+$384+$4,070+$4,320+$4,788 = **$19,816.40/year**, plus Buildertrend/Foreman/Houzz quotes, horizontal layers and any seat correction. Never advertise that catalogue subtotal as realistic replaced spend.

[analysis] Stage 4 queries should derive from actual artifacts: estimates/BOQs, POs, field/time records, signed documents, IFC/BCF/IDS/COBie/DXF, MPP/XER, invoice/accounting exchange and exports/backups. Generic UI/auth/database research must not stand in for the vertical sweep.
