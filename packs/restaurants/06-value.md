# 06 — Value case: the integration must earn its keep

Research date **2026-09-13 UTC**. **Verdict [analysis]: yes to a bounded, evidence-producing client pilot; no to an immediate whole-POS replacement or a claimed industry-wide cash-saving offer.** AC remains a medium-priority client job, not an admitted priority vertical. No client runtime was deployed, no application was built, and no operator outcome was measured in this research.

## Three numbers that must not be confused

| Quantity | Value | What the evidence supports |
|---|---:|---|
| Reference priced software basket | **$12,631/year** | [vendor / arithmetic] One hypothetical US-location basket, with 20 paid employees, one POS/KDS, three office users and two Airtable editors. Every price and exclusion is in [Stage 3](03-companies.md). It is not a tested compatible bundle or AC's invoice. |
| Candidate 16-GiB VPS plus daily disk backups | **$1,497.60/year** | [vendor / arithmetic] DigitalOcean's regular Basic 8-vCPU, 16-GiB, 320-GiB SSD plan is $96/month; percentage-based daily backup adds 30%. `(96 + 96×0.30)×12 = 1497.60`. This is a planning reference, not a measured resource floor or a complete run cost. [VM pricing](https://www.digitalocean.com/pricing/droplets) · [backup pricing](https://www.digitalocean.com/pricing/backups). |
| Verified removable AC spend / achieved net cash | **null / null** | [analysis] No invoices, termination clauses, incumbent entitlements, payroll displacement, additional contribution margin or complete implementation/operating costs have been supplied. Null is unknown, not zero. |

[analysis] The subtraction `$12,631 − $1,497.60 = $11,133.40` is **not a savings estimate**. It compares an unvalidated purchasing basket against only two infrastructure line items. It excludes the retained till/processor, marketplace and communication fees, setup, integrations, support, restore testing, devices, connectivity, accounting/payroll services, taxes, rights costs and any lost acquisition value. It must not appear in an offer as client value.

[vendor] Chatwoot recommends 8GB+ RAM and four or more cores for production by itself, so a tiny general-purpose box is not evidence that a multi-application restaurant assembly fits. [Requirements](https://developers.chatwoot.com/self-hosted). ODK documents a low-volume 1GB scenario, but also recommends more memory for media/export cases and notes migration memory pressure. [Install](https://docs.getodk.org/central-install/) · [troubleshooting](https://docs.getodk.org/central-troubleshooting/). [analysis] Test 8GiB for a reduced inbox/direct-order pilot and 16GiB for an expanded assembly; these are **unbenchmarked sizing hypotheses**. The $48/month 8GiB VM plus daily backups would be $748.80/year, but the lower price is not a claim that it can support all modules. No GPU is required by the proposed deterministic workflow; no paid hosted model is included by default.

## The first useful door

[analysis] The proposed wedge is **one assigned conversation-to-reservation/order handoff with a visible exception queue**, preserving the existing marketing website, till, payment provider and accountant. Staff should not have to infer whether a message was answered, retype the same details twice without lineage, or treat a draft as a confirmed booking. The expected improvement is a traceable accepted handoff, not an autonomous promise to a guest.

[analysis] This wedge is a hypothesis: Stage 1 contains industry practitioner evidence, not AC's actual messages. Before implementing it, compare three alternatives on the same work: configure the incumbent properly, use a low-cost/free incumbent feature, or introduce the proposed assembly. GloriaFood and Loyverse have free base offerings; existing email, forms or Sheets may resolve a small problem without a new platform. See [Stage 3's floor](03-companies.md). A ten-minute acknowledgement target in Stage 2 is merely an example to discuss, not a promised SLA.

[analysis] Reject this wedge if AC has few such enquiries, if the current booking/POS channel already captures them once, or if the new queue adds more review than it removes. A supplier-invoice/recipe-cost exception wedge may then be worth testing, but should not be silently substituted for demonstrated client demand.

## Hours returned — measure before multiplying

[analysis] For each W01–W12 stage, collect matched weekly volume `n_i`, baseline minutes `b_i`, assisted minutes `a_i` including all review, correction and exception handling, and added weekly maintenance/coordination minutes `m`:

`weekly_capacity_hours = (Σ[n_i × (b_i − a_i)] − m) / 60`

The source fields are null in [02-workflow.json](02-workflow.json). Stages that share a benefit use the same benefit ID so time is not counted once for the host, again for the order screen and a third time for the dashboard. Measure distributions and peak-period errors, not only an average on easy cases. Keep negative results.

[analysis — synthetic formula test only] Suppose a fixture contains 30 enquiries/week, 5 baseline minutes, 3 assisted minutes and 20 added coordination minutes: `(30×(5−3)−20)/60 = 0.667 hours/week`. Those numbers are invented test inputs, **not estimates of AC's activity or expected performance**. Their purpose is to demonstrate that review overhead can erase an apparently large per-case saving. The actual hours-returned field remains **null, unmeasured**.

[analysis] Record at minimum original source IDs, volumes, before/after human time, errors, missed/duplicate commitments, privacy events, manager acceptance and ongoing support effort. Compare equivalent types of enquiry/order across the incumbent and candidate workflows. Do not count time as cash unless an observed reduction in paid overtime/payroll or other monetisation is separately evidenced.

## Cash model and commercial gate

The public SISO [observed-value model](https://github.com/sisodias/great-library-of-siso/blob/main/research/industries/source/intelligence/agency/economics/observed-value-model.json) requires unknown inputs to remain null and separates capacity from cash. Apply it to this bounded process:

`first_year_net_cash = verified_cancelled_software_spend + verified_realised_labour_cash_savings + verified_incremental_contribution_margin + verified_risk_loss_reduction − annual_operating_cost − first_year_change_cost`

[analysis] Every benefit needs a dated baseline, owner acceptance and a non-overlapping benefit ID. Cancelling a reservations-network subscription can remove discovery traffic as well as fees. Direct ordering does not automatically eliminate card fees or the cost of acquiring a customer or delivering a meal. A refund or corrected payout is cash only when it is actually recovered and attributable to this process. No automation percentage, forecast interval, SISO fee or client ROI is claimed here.

[vendor] Uber Eats requires approved production scopes and distinguishes sandbox testing from merchant-facing operation; additional use cases can require a separate business agreement. [Authentication](https://developer.uber.com/docs/eats/guides/authentication) · [getting started](https://developer.uber.com/docs/eats/guides/getting-started). Deliveroo's portal has business activation/partner onboarding. [Portal](https://developers.deliveroo.com/). [analysis] API access, channel terms and settlement exports are acquisition costs and admission gates, not things an OSS wrapper makes disappear.

## Migration cost — an itemised estimate to obtain, not a free glue layer

| Work package [analysis] | Quantity / acceptance evidence | Current priced amount |
|---|---|---:|
| Client discovery and retention decision | Accepted country, service model, installed-system list, permissions, invoices and termination constraints | null |
| Identity and channel setup | Each approved mailbox/number/account; negative tests for wrong recipient, missing membership and revoked token | null |
| Menu, supplier and recipe migration | Counts of items, aliases, pack conversions, modifiers, recipe versions, yields and opening balances; sampled chef acceptance | null |
| Device and kitchen validation | Each supported till/printer/station; order amendment, reprint, restart and lost-connectivity tests | null |
| Booking/order handoff adapter | Named authoritative system, idempotency and reconciliation; no double payment or duplicate kitchen work | null |
| Finance/payroll export | Accountant-approved mapping, reference period, retained source evidence and reversible posting | null |
| Training and parallel operation | Staff roles trained, observed shifts, exception ownership and fallback drills | null |
| Backup, restoration and rollback | Successful data restore and documented reversal of the bounded change | null |
| Ongoing support | Measured support minutes, monitoring, updates, incident response and vendor escalation | null |

[analysis] Price these as measured/quoted hours × the accepted delivery rate plus named vendor/device costs. Obtain a fixed or capped pilot price only after scoping. No site-specific migration quote can be derived from GitHub stars, source size, a clean README or the assertion that only 5% is glue. The assembly design aims to minimise bespoke code; the **actual bespoke fraction is unmeasured**.

## Second deployment and vertical economics

[analysis] Reusable work includes version-pinned component recipes, canonical mappings, contract tests, installer/checklist documentation, fixtures and reversal procedures. The **second** deployment still needs its own VPS, credentials, data mapping, training, device validation and owner acceptance. It becomes materially cheaper only when country, incumbent interfaces and operating model match the first. A new processor or proprietary POS can dominate the incremental cost.

`second_deployment_change_cost = client_discovery + data_mapping + account_setup + device_checks + training + parallel_validation + rollback_setup + genuinely_new_adapter_work`

`portfolio_contribution = Σ(client_revenue − client_specific_delivery_cost − client_specific_operating/support_cost) − shared_build_and_maintenance_cost`

[analysis] Both outputs remain null. Do not multiply all restaurant establishments by a guessed SaaS price. The US Census [County Business Patterns](https://www.census.gov/programs-surveys/cbp.html) is an available source for employer establishments by industry and size; the page currently points to 2023 data. It does **not** directly count independent mixed dine-in/takeaway operators willing and technically able to migrate. **Eligible operator count: null.** Country choice, ownership/segment filters, installed-system compatibility, evidence of demand and reachable adoption need a separate measured market cut. This is an unfinished market-sizing gate, not evidence that the opportunity is small.

## The whole thesis is false if...

[analysis] Do not proceed when any of the following holds: the incumbent/free configuration solves the problem more cheaply; matched human effort including review does not fall; the operator cannot approve access or export its data; a material privacy, allergen/safety, payment or kitchen-fulfilment error is introduced; the single-box deployment cannot sustain peak service and recovery requirements; migration/support costs consume the attainable benefit; required marketplace/device interfaces cannot be obtained; or the second deployment needs essentially the same bespoke integration again.

[analysis] There are two separate decisions. A learning pilot can be justified by an explicitly accepted research budget. A **cash-saving commercial offer** requires positive observed first-year net cash and preserved quality. Do not call the latter approved merely because the former is interesting.

## Present decision

[analysis] Preserve the website and existing operational authorities. Prepare a bounded, reversible prototype specification around the accepted-message handoff and exception queue. Finish repository qualification and the remaining research gates before calling the pack complete; obtain AC's baseline and permissions before implementation. The evidence in this repository supports research choices and tests, not a deployed restaurant operating system.
