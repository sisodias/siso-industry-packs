# US small construction contractors — research checkpoint

Observed **2026-09-13**. **IN PROGRESS: 12 repository source reviews, not the required 100.** This is the GitHub review edition of the research draft, not a completed pack, a production admission or application code. An expanded Markdown/JSON working pack accompanies the chat delivery. Mutable prices and repository observations require rechecking before procurement or implementation.

## Person, segment and wedge

[analysis] Design for a reconstructed owner plus four employees and subcontractors doing occupied-home kitchen, bathroom and interior remodeling. A client buys the completed agreed-scope remodel, not its administrative paperwork. The dated practitioner anchor is a [December 2022 contractor discussion](https://www.reddit.com/r/Construction/comments/zcqol9/best_software_for_a_new_company/); this is not an interviewed current customer.

[analysis] Enter through **conversation → reviewed change → exact-revision approval → acknowledged field release → billing evidence**. Do not turn a text message into authorization. Fragmented communication and duplicate accounting records are reported in the [change-order discussion](https://www.reddit.com/r/Contractor/comments/vz3blu/what_all_do_you_use_to_createrecordprocess_change/) and [Sage/Excel discussion](https://www.reddit.com/r/ConstructionManagers/comments/1ij9g2g/change_order_management/).

## Stack tax and value

[analysis] The hypothetical five-person core subscription basket is **$5,726.40/year**: JobTread $2,678.40 + QuickBooks Online Plus $1,680 + Gusto Simple $948 + Google Workspace Starter $420. Published-price sources: [JobTread](https://www.jobtread.com/pricing), [QuickBooks](https://quickbooks.intuit.com/pricing/), [Gusto](https://gusto.com/product/pricing), [Workspace](https://knowledge.workspace.google.com/admin/getting-started/editions/business-editions). This is not measured client spend.

[analysis] Retain accounting, payroll and email: **$3,048/year**. Modeled replacement-stack operations cost **$3,194.60–$3,885.80/year**, including human maintenance and reserves but excluding unknown fees and migration. Retained subscriptions plus operations therefore cost **$6,242.60–$6,933.80/year**. This does **not** establish cheaper software. A net **2.75 hours/week** coordination-capacity hypothesis is **unmeasured**; see Stage 6 for arithmetic and falsifiers.

## Spine and assembly

[analysis] Six persistent objects: **Party, Job, WorkPackage, Conversation, EvidenceDocRevision, CommercialRecord**. The differentiated work is identity mapping, revision/approval rules and evidence-preserving integration. All resident application services belong on **one client-owned VPS**, never SISO servers; external messaging/payment accounts and encrypted off-host backups remain client-owned.

| Repository | Provisional verdict | Intended role |
|---|---|---|
| [frappe/erpnext](https://github.com/frappe/erpnext) | ADOPT | Project, party, purchasing and draft commercial records |
| [chatwoot/chatwoot](https://github.com/chatwoot/chatwoot) | ADOPT | Shared conversation inbox |
| [docusealco/docuseal](https://github.com/docusealco/docuseal) | ADOPT | Linked mobile signing, subject to edition checks |
| [Kozea/WeasyPrint](https://github.com/Kozea/WeasyPrint) | ADOPT | Controlled PDF packet generation |
| [restic/restic](https://github.com/restic/restic) | ADOPT | Encrypted backups and restoration |
| [opf/openproject](https://github.com/opf/openproject) | STUDY | Scheduling/work-package alternative |
| [InvoicePlane/InvoicePlane](https://github.com/InvoicePlane/InvoicePlane) | STUDY | Narrow invoice-sidecar alternative |
| [IfcOpenShell/IfcOpenShell](https://github.com/IfcOpenShell/IfcOpenShell) | STUDY | Optional IFC/BCF/IDS interoperability |
| [joniles/mpxj](https://github.com/joniles/mpxj) | STUDY | Optional schedule-format import |
| [braedonsaunders/bidwright](https://github.com/braedonsaunders/bidwright) | STUDY | Construction estimating/assembly patterns |

[analysis] These are prototype preferences, not deployed or validated components. Stage 4 adds Paperless-ngx and GEstimator and records actual README/license observations, dates and uncertainty.

## Gaps, verdict and actual counts

[analysis] Ten gaps: US estimating inputs; professional/jurisdiction authority; approval/dispute handling; offline field behavior; accounting/payroll fidelity; external channels/payments; paid-edition/API entitlements; one-box operations/recovery; migration/adoption; incomplete research admission.

[analysis] **YES to investigating a bounded supervised change-control prototype; NO to a wholesale replacement or demonstrated-savings claim.** Reject if total coordination effort fails to improve at equal or better approval/version accuracy, or if adoption, restoration and support costs invalidate the economics.

| Measure | Actual |
|---|---:|
| Workflow stages | 10 |
| Tier-1 companies | 10 |
| Tier-2 offerings | 10 |
| Quoted practitioner complaints | 10 across 6 threads |
| Repository source reviews | **12 / 100 required** |
| Raw search hits / distinct search names | 100 / 90; not examinations |
| Provisional ADOPT / production admissions | 5 / 0 |
| Bank membership | 1 confirmed ALREADY, 11 UNVERIFIED, 0 verified NEW |
| Completed dry rounds | 0 |
| Gaps | 10 |
| Builds, deployments, measured savings | None |

The shared registries are unchanged. `07-registry-proposal.json` is explicitly non-complete. No NEW bank submissions are asserted from incomplete searches.
