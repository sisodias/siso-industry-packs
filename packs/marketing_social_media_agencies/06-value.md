# Stage 6 — Value case and falsification

Research date: **2026-09-13**. `[analysis]` Unless explicitly identified as a vendor tariff or official statistic, every number below is a **planning assumption or calculation, not a measured customer result**. No client invoice, labor log, live account, deployment benchmark or revenue result was accessed. Observed savings, eligible customers and accepted capacity gains remain `null / unmeasured`.

## Decision

[analysis] **YES to an approval-first, client-owned operating core with a bounded validation pilot. NO to a wholesale replacement or enterprise-parity claim.** The candidate entry point is conversation → accepted scope → version-bound approval, where copying and interpretation errors have direct practitioner evidence. Scheduling and reporting enter only after permission, delivery and metric-parity tests. The broad tool-replacement economics are considerably weaker than the headline stack tax suggests. [Complaint evidence](01-person.md), [workflow and gates](02-workflow.md), [commercial comparison](03-companies.md)

## 1. The stack tax is not all recoverable cash

[analysis] The selected five-person/ten-brand reference basket costs **$9,419.76/year**. It is a constructed procurement case, not an actual agency bill. The maximum hypothetical avoidable subscriptions total **$5,460**; retained email/creative/accounting/payroll total **$3,959.76**. Taxes, ad spend, carrier/API usage, payment processing and licensed assets are excluded or variable. [Item-by-item arithmetic and vendor URLs](03-companies.md#stack-tax--arithmetic-not-an-inflated-pile-of-alternatives)

[analysis] The proposed full assembly **retains the $120 Calendly host licence initially**, rather than adding a booking service merely to erase a small fee. Its planned conditional displacement ceiling is therefore **$5,340/year**: `ClickUp 720 + Airtable 1,200 + SocialPilot 1,020 + AgencyAnalytics 2,400`. A verified lightweight booking replacement could raise the ceiling back to $5,460. No cancellation is admitted before the corresponding capability is accepted and the contract can actually end.

[analysis] An approval-only wedge may displace **at most Airtable's $1,200** in this basket, and only if its other uses can be retired. It cannot claim the scheduler, report platform or work manager's entire bill merely because it displays approval status. A client who uses Sheets and a cheap scheduler may have **zero cancellable software spend** at entry.

## 2. Cost of one client-owned deployment

[vendor] DigitalOcean's published regular Basic Droplets include 4 GiB / 2 vCPU / 80 GiB at **$24/month**, and 16 GiB / 8 vCPU / 320 GiB at **$96/month**. Its Memory-Optimized 32 GiB / 4 vCPU / 100 GiB configuration is **$168/month**; General Purpose 32 GiB / 8 vCPU / 100 GiB is **$252/month**. These are transparent reference tariffs, **not a claim that DigitalOcean is the cheapest host**. [Droplet pricing, observed 2026-09-13](https://www.digitalocean.com/pricing/droplets)

[vendor] Weekly percentage-priced Droplet backups add **20%**; the referenced Spaces subscription starts at **$5/month**, including a storage allowance before overages. A backup on the same VPS is not the off-machine recovery copy. [Backups](https://docs.digitalocean.com/products/backups/details/pricing/), [Spaces](https://docs.digitalocean.com/products/spaces/details/pricing/)

[analysis] Additional assumptions: **$120/year transactional-email allowance**, **$20/year domain allowance**, and maintenance valued internally at **$75/hour**. These three numbers are **not retrieved tariffs or prevailing staffing rates**. SMTP volume, legal/edition fees, asset retention, traffic and incident labor may exceed them. The client owns the VPS, domain and encrypted backup account; SISO does not hold a shared production database, publication gateway or backup bucket.

| Scenario [analysis] | VPS + weekly backups/year | Backup bucket + email + domain allowances | Maintenance assumption | Modeled annual cost |
|---|---:|---:|---:|---:|
| Approval-only core; 4 GiB load-test candidate, no Chatwoot/Postiz resident | $24 × 1.2 × 12 = $345.60 | $60 + $120 + $20 = $200 | 1 hour/month × 12 × $75 = $900 | **$1,445.60** |
| Full assembly, 16 GiB **only if load tests pass** | $96 × 1.2 × 12 = $1,382.40 | $200 | 2 hours/month = $1,800 | **$3,382.40** |
| Full assembly, 32 GiB memory-oriented planning case | $168 × 1.2 × 12 = $2,419.20 | $200 | 2 hours/month = $1,800 | **$4,419.20** |
| Full assembly, 32 GiB / 8 vCPU CPU-headroom case | $252 × 1.2 × 12 = $3,628.80 | $200 | 2 hours/month = $1,800 | **$5,628.80** |

[analysis] Resource configurations are **capacity hypotheses**, not validated floors for our assembly. The 32 GiB instances have only 100 GiB listed disk; raw video retention or local backups can make additional storage necessary. Off-machine storage, local media quotas, serialized transcodes, database growth and restore time must be tested. One agency's ten client brands remain access-separated within its box; unrelated agency clients never share a box.

[vendor] Postiz's current requirements include Temporal and recommend 8 GiB / four cores for a small deployment; its much smaller minimum is not headroom for a multi-application agency stack. Chatwoot's free self-hosted edition does not include enterprise SSO or advanced roles. Those facts prevent a credible “everything on a tiny VPS with enterprise permissions for free” promise. [Postiz requirements](https://docs.postiz.com/self-host/installation/system-requirements), [Chatwoot editions](https://www.chatwoot.com/pricing/self-hosted-plans)

[analysis] **Net subscription-only economics, before build/migration/fees/overages:** approval wedge `1,200 − 1,445.60 = −$245.60/year`; accepted full 16 GiB case `5,340 − 3,382.40 = $1,957.60`; 32 GiB memory case `5,340 − 4,419.20 = $920.80`; CPU-headroom case `5,340 − 5,628.80 = −$288.80`. These are scenarios, **not savings**. The subtraction uses planned cancellation scope, not the entire $9,419.76 stack.

[analysis] If reporting parity fails and AgencyAnalytics remains, remove $2,400 from avoidable spend. The 32 GiB memory case then becomes **−$1,479.20/year** before migration. If monthly maintenance rises from two to four hours, annual cost rises by $1,800. Either result can eliminate the cash case. Keeping a good inexpensive commercial tool is a valid outcome, not a research failure.

## 3. Hours returned — explicitly unmeasured

[analysis] The following is a **hypothesis to test**, not a promised productivity rate. Monthly units convert to weekly using `12 / 52`; a case appearing in intake and community handling is counted once. “Minutes after” must include automation supervision, all review/rework, exceptions and reconciliation. Waiting for a client is recorded separately from staff working time.

| Work unit | Reference frequency | Proposed before → after human minutes | Hypothetical weekly return |
|---|---:|---:|---:|
| Actionable conversation/request, including community cases | 50/week | 6 → 3 | 150.00 minutes |
| Accepted content package, including its approval/revision work | 120/month | 12 → 7 | 138.46 minutes |
| Channel-publication job, including amortized exception work | 240/month | 3 → 2 | 55.38 minutes |
| Accepted client report, including metric reconciliation | 10/month | 60 → 40 | 46.15 minutes |
| New control/admin overhead | Weekly | Add 45 minutes | **−45.00 minutes** |
| **Net full-assembly hypothesis** | | | **345 minutes = 5.75 hours/week** |

[analysis] That equals **299 hours/year** only under the stated 52-week continuity assumption. The approval-only hypothesis uses the first two rows less new overhead: **about 4.06 hours/week**. Neither is admitted as capacity returned until measured. Creative ideation/editing is not eliminated, and a faster draft that produces more revisions can make the result negative.

[analysis] Multiplying 299 hours by an hourly rate would be **capacity valuation**, not payroll cash saved. Cash can be recognized only through an actual avoided expense or additional accepted work with evidenced incremental gross contribution, without double counting. The underlying Foundry model requires quality/authority gates to pass before value is admitted. [Observed value model](https://github.com/sisodias/great-library-of-siso/blob/main/research/industries/source/intelligence/agency/economics/observed-value-model.json)

### Baseline and acceptance design

[analysis] Proposed pilot: two baseline weeks and four matched pilot weeks across a small, owner-approved set of brands, stratified by image/video, revision count and channel. This is a design, not a scheduled or completed experiment. Log original source-message references, versions, responsible people, active minutes, waiting time, errors, rework, publish attempts, platform receipts, metric completeness and accepted deliverables. Measure the existing tool stack fairly; include a native/manual posting comparator where it is already efficient.

[analysis] Proposed entry acceptance: at least **three net hours/week returned**, no critical rights/claim/accessibility defect, no cross-brand disclosure, no unauthorized/wrong-account publication, no approval surviving a material edit, and no unreviewed financial action. Thresholds are owner-negotiable design targets, not standards. Report confidence and case-mix limits, not just a mean. Any severe authority failure is a stop condition even if average time falls.

## 4. Migration is work, not a CSV button

[analysis] First-agency migration estimate: **24–48 hours × $75 = $1,800–$3,600**, excluding contract overlap and unusual historical media clean-up. Planning allocation: source inventory/ownership 4–8 hours; client/brand/content mapping 6–12; approvals/media/history reconciliation 6–12; training, parallel run and rollback rehearsal 8–16. This is a transparent estimate, not a customer quote.

[analysis] Exports must preserve source IDs, brand boundaries, captions, attachments, comments, version/approval timestamps, open work and report definitions. Do not import a column named “approved” as an authenticated approval event without its provenance. OAuth grants must be re-established by account owners; passwords and MFA codes are not a migration mechanism. Existing accounting/payroll histories remain authoritative. [Lock-in inventory](03-companies.md), [workflow objects](02-workflow.md)

[analysis] Contracts overlap until acceptance and renewal dates allow cancellation. A full additional month of the reference basket would cost `9,419.76 / 12 = $784.98`, but actual overlap is subscription-specific. Exportability is tested by reconstructing a sample campaign and restoring a backup before switching. Preserve a rollback route to native publishing and the existing scheduler until delivery reliability is demonstrated.

[analysis] Using only the 32 GiB subscription-only scenario's $920.80/year margin, a $1,800–$3,600 migration would take roughly **2.0–3.9 years** to recover, before shared build costs or uncertainty. That is not an attractive cost-only argument. The approval wedge has no positive cash-only payback under the stated assumptions. Adoption must therefore be justified by **measured capacity, control, avoided commercial leakage or ownership**, not an inflated software bill.

## 5. Vertical economics and the second deployment

[vendor: official statistics] The Census Bureau profile for advertising agencies reports **15,512 employer establishments** in the **2023** County Business Patterns series. This is a broad historical establishment denominator, **not distinct firms, not all nonemployer operators, not today's agency count, and not the organic-social-retainer segment**. The downloadable national source is separately recorded in `research/market-size.json` when retrieval succeeds. [Census profile](https://data.census.gov/profile/54181_-_Advertising_agencies?n=54181), [2023 downloadable files](https://www2.census.gov/programs-surveys/cbp/datasets/2023/)

[analysis] **Eligible primary-segment operators = null.** No defensible segment share or buyer willingness-to-pay was measured. Do not turn 15,512 establishments into a revenue forecast by multiplying an invented adoption percentage. The segment may also include nonemployers outside that denominator. A prospect qualification study must ask about recurring package volume, current approval failure, tool spend, decision authority, self-hosting preference and maintenance willingness.

[analysis] Shared productization estimate: **240–400 engineering/review hours × $75 = $18,000–$30,000** for the thin spine, integration contracts, migration tooling, release controls and acceptance harness—not a rewrite of every app. No engineering was executed for this blueprint. Upstream software does not make this integration free, and the requested roughly-5% custom portion is an ambition, not a measured code fraction.

[analysis] Once the first implementation is accepted, **second deployment = 16–24 hours × $75 = $1,200–$1,800**, plus its own VPS/backup/usage and ongoing maintenance. This includes 4 hours installation/restore checks, 4–8 mapping and grant setup, and 8–12 migration/training/acceptance. It is not “copy a Docker file for zero cost.” Client-specific historical cleanup can exceed the estimate.

| Deployment-count scenario [analysis, not a market forecast] | Shared $18k–$30k build allocation per deployment | Still paid separately |
|---|---:|---|
| 100 accepted agency clients | $180–$300 | Migration, each client's infrastructure, support and usage |
| 500 accepted agency clients | $36–$60 | Same; standardization must not hide security/edition obligations |
| 1,000 accepted agency clients | $18–$30 | Same; support load and release fleet management become the bottleneck |

[analysis] Cross-industry reuse belongs in the request, approval, evidence, export and deployment contracts—not a shared client-data database. Ten thousand catalogue entries do not reduce the second deployment cost unless the chosen assembly is stable and accepted. This pack supplies candidate evidence to GQ-004/GQ-013, not an accepted answer to either. [GQ-004](https://github.com/sisodias/great-library-of-siso/blob/main/registry/works/frontier-question-gq-004.json), [GQ-013](https://github.com/sisodias/great-library-of-siso/blob/main/registry/works/frontier-question-gq-013.json)

## 6. What falsifies the whole thesis?

[analysis] Reject or substantially narrow the product if a matched pilot does not reduce **net** human work; clients still require parallel WhatsApp/email/spreadsheet systems that erase the benefit; the operator has little approval pain or already solves it cheaply; reliable official platform access cannot be obtained; report connector gaps preserve the largest subscriptions; maintained self-hosting costs exceed accepted value; or migration/removal costs exceed the estimate by more than twofold. A private self-hosted scheduler is not an entitlement to publish on every platform. [TikTok's current Direct Post boundary](https://developers.tiktok.com/docs/en/content-sharing-guidelines)

[analysis] Stop immediately for a cross-client data leak, wrong-account publication, unapproved send, falsified approval, unsupported material claim, unrecoverable backup or unauthorized financial action. Do not trade these defects for a positive average time-saving number. No such incident was observed here because **no production deployment or live account was tested**.

[analysis] Final economic conclusion: **an approval-and-delivery operating core is worth validating; “replace the agency's entire stack cheaply with OSS” is not established.** Keep the wedge small enough to prove, retain specialist authorities and make cancellation, capacity and safety receipts—not a repository star count—the admission criteria.
