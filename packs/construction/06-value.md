# 06 · Value case — supervised change control, not a cheap-ERP promise

2026-09-13. **All labor, migration, support and conversion figures are unmeasured scenarios.** The public [Foundry value model](https://github.com/sisodias/great-library-of-siso/blob/main/research/industries/source/intelligence/agency/economics/observed-value-model.json) separates canceled spend/realized contribution from unmonetized capacity and operating/change costs.

## Subscriptions replaced versus retained

[analysis] Reference basket: JobTread $2,678.40 + QBO Plus $1,680 + Gusto Simple $948 + Workspace Starter $420 = **$5,726.40/year**. Sources and seat assumptions: [JobTread](https://www.jobtread.com/pricing), [QBO](https://quickbooks.intuit.com/pricing/), [Gusto](https://gusto.com/product/pricing), [Workspace](https://knowledge.workspace.google.com/admin/getting-started/editions/business-editions). Two Bluebeam Core and two Docusign Standard senders add $660+$600, making **$6,986.40/year**; [Bluebeam](https://www.bluebeam.com/pricing/), [Docusign](https://www.docusign.com/products/electronic-signature/plans-and-pricing).

[analysis] Retain QBO+Gusto+Workspace: **$3,048/year**. Potential JobTread cancellation: **$2,678.40**, only after actually used capabilities are replaced and the subscription canceled. A change-control pilot alone does not qualify. During dual run, assume **zero canceled subscriptions**. Do not automatically claim the optional Bluebeam/Docusign spend as savings.

## Run cost includes the human operator

[vendor] [VPS](https://www.digitalocean.com/pricing/droplets) and [weekly backup](https://www.digitalocean.com/pricing/backups) model: $48×12×1.20=$691.20 for 8 GiB; $96×12×1.20=$1,382.40 for 16 GiB. [Twilio US base SMS](https://www.twilio.com/en-us/sms/pricing/us): ($1.15+1,000×$0.0083)×12=$113.40/year for 500 inbound+500 outbound segments monthly, before carrier/A2P/other charges.

| Annual item | 8-GiB evaluation | 16-GiB planning | Evidence |
|---|---:|---:|---|
| VPS + weekly provider backups | $691.20 | $1,382.40 | Vendor-price arithmetic, not capacity proof |
| Separate encrypted-backup budget | $120 | $120 | Analysis allowance, not a quote |
| Domain budget | $20 | $20 | Analysis allowance |
| SMS base example | $113.40 | $113.40 | Vendor arithmetic; extra charges excluded |
| Routine operation: 2h/month×$75×12 | $1,800 | $1,800 | Analysis, not measured support |
| Incident reserve: 6h/year×$75 | $450 | $450 | Analysis, not measured incidents |
| **Modeled run cost** | **$3,194.60** | **$3,885.80** | Before unknown paid features/APIs/tax/overages/payment fees |

[analysis] Retained subscriptions plus operations = **$6,242.60–$6,933.80/year**, **$516.20–$1,207.40 more** than the core benchmark, before migration/build recovery. Subscription cancellation alone does not justify this model. Cheaper hosting or lower maintenance might change it, but must be measured. Neither RAM configuration is a validated integrated resource floor; plan 16 GiB until tested.

## Hours returned: null measured result, explicit hypothesis

[analysis] Frequencies match Stage 2. Before/after active handling times are assumptions, not measurements.

| Stage | Events/week | Assumed before → after minutes/event | Gross minutes/week |
|---|---:|---|---:|
| W01 lead intake | 10 | 8 → 5 | 30 |
| W06 coordination | 15 | 7 → 5 | 30 |
| W07 field records | 25 | 4 → 3 | 25 |
| W08 changes | 5 | 25 → 13 | 60 |
| W09 billing/reconcile | 5 | 20 → 12 | 40 |
| W10 closeout | 5 | 8 → 6 | 10 |
| **Total** | | | **195** |

[analysis] Deduct 30 minutes/week of internal exception/review work: **195−30=165 minutes=2.75 hours/week**. At 48 weeks: **132 hours/year of hypothetical capacity**. Measured savings remain **null**. Do not double-count internal handling with paid infrastructure operation. Do not price saved waiting time as labor or assume capacity becomes cash.

[analysis] Baseline: observe at least two representative operator weeks with consent, recording accepted complete packets, active handling, interruptions, waiting, re-entry, rework, exceptions, volume/complexity and approval/version errors. Compare matched supervised work against a well-configured incumbent. Include transition/training effort. Cash benefit requires an actual canceled expense or realized incremental contribution that would otherwise be forgone. No faster-collection, avoided-dispute or recovered-revenue benefit is claimed.

## Wedge and migration cost

[analysis] Entry: a homeowner change from an actually used channel becomes a versioned request, reviewed price/schedule impact, recorded approval, acknowledged field release and traceable draft billing packet. The old system remains authoritative during the first comparison. The wedge wins only at equal or better approval/version accuracy and lower all-in effort.

[analysis] Reusable first-assembly allowance: **180–360h×$75 = $13,500–$27,000**. This is a planning scenario, not a delivery quote; unfinished research may change it. First-client migration: **20–40h×$75 = $1,500–$3,000**, separate from reusable build. Inventory source rights/templates/formulas; export original files; map external IDs, sites and cost codes; human-review duplicates; reconcile totals/counts; train; dual-run; prove rollback and complete export. Do not close old accounts just because CSV import worked.

[analysis] Second-client onboarding after an admitted template: **8–16h×$75 = $600–$1,200**, including bounded configuration, standard import, training and restore/smoke test. Excludes bespoke historic cleanup, new integrations, legal customization and recurring hosting/support. Client ownership, permissions and recovery evidence must be established again.

## Vertical economics

[vendor] NAHB's [July 2025 analysis](https://eyeonhousing.org/2025/07/residential-remodelers-outnumber-single-family-builders-in-the-u-s/) reports **128,187 residential-remodeler establishments in the 2022 Economic Census**, versus 102,818 in 2017. Its [February 2026 release](https://www.nahb.org/news-and-economics/press-releases/2026/02/nahb-expects-remodeling-growth-2026) describes about 128,000 remodeling firms at the start of 2025. [analysis] Different dates/units: do not relabel either as 2026 eligible customers. Exact operators in this occupied-home, five-person, self-hosting-ready segment are **unknown**.

[analysis] Allocating a $13,500–$27,000 reusable build across 100 admitted deployments would be $135–$270/client; **acquiring 100 is not established**. Evaluate measured contribution after acquisition, onboarding, support and incident costs. Reuse module contracts and mapping patterns across industries, not client records or infrastructure. No revenue/TAM forecast is asserted.

## Falsifier and verdict

[analysis] Reject or redesign if matched work does not reduce total handling/rework at equal or better approval/version accuracy; field/subcontractor adoption creates more chasing; authority cannot be represented; independent restore/export fails; paid features or support exceed demonstrated customer value; or the second client still requires a bespoke rebuild.

[analysis] **YES to a bounded supervised change-control prototype after admission gates; NO to selling a wholesale replacement or claiming savings today.** The repeated job/party/scope/conversation/commercial objects make a reusable assembly plausible. They do not make accounting, engineering, estimating or contract judgment free.
