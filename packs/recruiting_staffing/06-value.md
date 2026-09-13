# 06 — Value case, costs and falsifiers

> Research snapshot **2026-09-13**. `[vendor]` = upstream/provider claim; `[practitioner]` = attributed public report; `[analysis]` = our inference/design. No application deployed or candidate code executed.

## Decision

[analysis] **YES to a bounded, paid coordination pilot; NO to replacing the agency's ATS, payroll bureau, sourcing network and ledger with an unqualified OSS suite.** Lead with conversation-to-approved-requisition, not a wholesale migration. The existing Foundry recommendation survives the wider sweep. [Foundry record](https://raw.githubusercontent.com/sisodias/great-library-of-siso/main/research/industries/source/intelligence/agency/industries/recruiting_staffing.json); [assembly](05-superapp.md).

## Stack tax versus honestly replaceable spend

[analysis] The configured fixed reference stack is **$18,840/year**, not observed expenditure. Potential later retirements are Airtable $1,200 + Calendly $960 + Dropbox Sign $600 = **$2,760/year**, and only after functional parity and actual cancellations. The first intake wedge can at most target the $1,200 Airtable line; even that saving is zero until it is really removed. Payroll $8,880, ATS $3,300, Workspace $840, Quo $1,380 and QuickBooks $1,680 total **$16,080 retained** in the later scenario. [Dated source/price ledger](03-companies.md).

| Scenario [analysis] | Run cost/year | Incumbent costs eligible to retire | Net fixed-cost change before migration |
|---|---:|---:|---:|
| Minimal intake pilot; less functionality, existing communications retained | $576 compute + $120 backup + $1,200 support = **$1,896** | At most **$1,200**, cancellation required | **$696 additional cost** |
| Supported integrated coordination, booking and signing reference | $1,152 compute + $120 backup + $3,600 support + $528 signature = **$5,400** | At most **$2,760**, three cancellations required | **$2,640 additional cost** |

[analysis] Full steady reference: $16,080 retained + $5,400 proposed run = **$21,480/year** versus $18,840. Do not sell this as automatic licence savings. Support assumptions are respectively 1 or 3 hours/month at an assumed $100/hour; backups are a $10/month planning allowance. Compute uses published plan prices, not measured resource requirements. [DigitalOcean](https://www.digitalocean.com/pricing/droplets).

[vendor] DocuSeal's production API/embedding remains paid on-premises. [Pricing](https://www.docuseal.com/pricing). [analysis] The integrated scenario assumes 2 seats x $20/month x 12 plus 240 completions/year x $0.20 = **$528**. Free manual UI could avoid that fee but loses the integrated capability; it cannot support the same automation claim. More documents, paid SSO/RBAC/modules, carrier fees, incidents, taxes and resource expansion increase costs. No cancellation, contractual eligibility or production-price quote was verified.

## Hours returned — hypothesis, never dressed as measurement

[analysis] The following quantities are team-wide design fixtures from [Stage 2](02-workflow.md), not employee diaries. Measure before/after human minutes **including approval, correction, exception handling and reconciliation**. Do not add overlap between stages or value candidate waiting time as saved staff labor.

| Workflow unit | Weekly units (assumed) | Baseline min/unit (unmeasured) | Proposed reviewed min/unit (unmeasured) | Hypothesized minutes returned |
|---|---:|---:|---:|---:|
| Complete approved requisition | 20 | 5 | 3 | 40 |
| Accurate approved status coordination | 80 | 3 | 2 | 80 |
| Correct interview scheduling/change | 20 | 10 | 6 | 80 |
| Worked-time review including exceptions | 50 | 4 | 2.5 | 75 |
| Payroll/invoice evidence reconciliation packet | 12 | 15 | 10 | 60 |
| **Full-scope total** | | | | **335 min = 5.58 hours/week** |

[analysis] At 48 working weeks this is **268 capacity hours/year**, not payroll reduction. An assumed $40/hour shadow value gives $10,720 of capacity; realized cash remains **null** until an actual avoided cost or incremental contribution is evidenced. The intake-only pilot earns only its measured share (the 40-minute hypothesis), not the entire 335-minute full-system estimate. Net outcomes must subtract new support/admin/rework. Baseline data, standard errors, adoption, retention, fairness, wage correctness and accessibility outcomes were not measured.

[analysis] A full-scope sensitivity test is more useful than a savings promise: with $2,640 extra annual fixed costs, pure operating break-even at an assumed $40/hour requires 66 genuinely valuable staff hours/year (1.38 hours/week over 48 weeks), **before migration and shared engineering**. At zero monetizable capacity, the cash case is negative. These assumptions are decision aids, not evidence.

## The wedge and migration sequence

[analysis] One door: preserve the inbound email/thread, approve a complete JobOrder and write it once to the existing ATS with a receipt. P07 reports manual employer/client intake; P03 reports reply-unaware automation. [P07](https://www.reddit.com/r/recruiting/comments/1esqewk/can_anyone_share_their_experiences_with_loxo/); [P03](https://www.reddit.com/r/recruiting/comments/1mmi61u/has_anyone_else_had_a_terrible_experience_with/). The proposed advantage is less retyping and traceable exceptions, not a smarter employment-decision model. Actual superiority remains to be tested.

[analysis] Phase A: authorized read-only export and source/permission map. Phase B: parallel intake drafts and measured reviewer effort. Phase C: explicitly approved limited ATS writes with rollback/reconciliation. Phase D: separately qualify scheduling, time and signing. Only then cancel eligible tools. Full ATS and statutory payroll migration are separate projects, not hidden inside this wedge.

## Migration cost — real work, assumed rates

| Repeatable onboarding task [analysis] | Second-client labor assumption |
|---|---:|
| Export/contract/API entitlement and data inventory | 4–6 h |
| Identity, source-field and permissions mapping | 6–10 h |
| Client-owned account/channel/secret configuration | 4–6 h |
| Import reconciliation and exception fixtures | 8–14 h |
| Training, parallel acceptance and rollback/restore check | 6–12 h |
| Handoff and operating runbook | 4–8 h |
| **Second client total** | **32–56 h = $3,200–$5,600 at assumed $100/h** |

[analysis] First-client migration/onboarding allowance: **60–100 hours = $6,000–$10,000** at the same assumed rate. These are explicit planning estimates, not vendor quotes or measurements; vendor exit charges, history/attachment exports, API tier upgrades and custom integrations are additional. Shared product engineering is **unpriced**, not zero, until a field map and delivery estimate exist. A second deployment removes reusable assembly/design work, not client-specific permissions, data cleanup and account authorization. [Commercial lock-in register](03-companies.md).

## Vertical economics — count the right buyers

[vendor] ASA reports approximately **27,000 US staffing/recruiting companies and 54,000 offices in 2021**. This is a historical parent-industry figure, not a 2026 count of eligible IT contract desks. [ASA statistics](https://americanstaffing.net/research/fact-sheets-analysis-staffing-industry-trends/staffing-industry-statistics/). [analysis] The exact number of US five-person/professional-W-2-contract operators satisfying this workflow and API/privacy criteria is **null** in this research. Do not multiply workforce occupational shares by firm counts or equate establishments with firms.

[analysis] Qualification should count owner-led firms with recurring assignments, existing authorized ATS exports/API, manual coordination load and a named compliance/payroll owner. Segment size is an explicit research gap, not permission to invent TAM. Scenario deployments of 25/100/500 clients would be business-planning quantities, not forecasts or measured market shares. Each client still pays its own hosting/external accounts and incurs the second-deployment work above. Shared engineering must be amortized over **actual** retained clients; an unpriced first build cannot be hidden behind a cheap server.

## Falsifiers and evidence needed

[analysis] Reject or narrow the thesis if: (1) reviewed intake is no faster after exceptions; (2) the desk will not adopt the new queue and continues its spreadsheet; (3) API/exports cannot preserve identities, attachments, permissions or history; (4) unapproved/stale/cross-client sends occur; (5) employment/wage decisions are bypassed; (6) the shared schema creates more reconciliation than it removes; (7) support and resource/edition fees exceed monetizable capacity; (8) no narrow eligible segment will fund the per-client onboarding cost; (9) accessibility or legal/privacy review fails; or (10) one-box outages/restores cannot meet the client's deadlines. No amount of repository stars reverses these tests.

[analysis] Proposed pilot gates: source-fidelity and duplicate-send tests pass; every external action has an accountable approver; no privacy/permission exceptions survive review; actual total human minutes fall for the same completed-work definition; migration reconciles counts and rollback; costs and cancellations have receipts. Test cases suggested in Stage 5 are engineering fixtures, not statistical proof of fair selection outcomes.

## Regulatory/source boundary

[vendor] EEOC/DOJ warn about disability discrimination from employment software; NYC regulates certain automated employment-decision tools; FTC guidance describes background-check obligations. [EEOC/DOJ](https://www.eeoc.gov/newsroom/us-eeoc-and-us-department-justice-warn-against-disability-discrimination), [NYC](https://www.nyc.gov/site/dca/about/automated-employment-decision-tools.page), [FTC](https://www.ftc.gov/business-guidance/resources/background-checks-what-employers-need-know). [analysis] These sources improve on the earlier EEOC-page retrieval gap, but do not constitute fifty-state/local law review, a legal opinion, a bias audit or accessibility certification. Some direct DOL/USCIS retrievals were blocked; indexed official snippets are not represented as complete page reads. Keep selection and restricted verification with authorized humans/providers.

## Accounting for value

[analysis] Separate **cash**, **capacity**, **quality** and **risk**; all actual outcomes remain null. The catalogue and source ratings establish a reuse hypothesis, not adoption, savings or fairness. This follows the [Foundry observed-value model](https://raw.githubusercontent.com/sisodias/great-library-of-siso/main/research/industries/source/intelligence/agency/economics/observed-value-model.json). Final verdict: pursue a supervised, measurable intake/status pilot; do not promise an all-OSS staffing business in a box.
