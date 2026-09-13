# Value case — prove reduced reviewed effort, not better predictions

Research cut: 2026-09-13. Status: **unmeasured value hypothesis**. [analysis] The proposed pilot is a read-only statement-import-to-review workflow, not an investment recommendation, a tax service or a promise of trading profit.

## Model and missing-data policy

[vendor/project-owner] The existing [SISO observed-value model](https://github.com/sisodias/great-library-of-siso/blob/main/research/industries/source/intelligence/agency/economics/observed-value-model.json) separates source capability, client value, SISO price/profit and societal value. Unknown mandatory inputs remain null, not zero or invented estimates. Capacity is not realized cash savings, and the same benefit must not be counted twice.

[analysis] Apply that policy here. No participant invoices, observed handling times, accepted outcomes, support costs, eligible market population or second-deployment measurements were collected. Source and feature evidence do not fill those gaps. Machine-readable inputs and references: [06-value.json](06-value.json).

## The stack tax and the much smaller replacement claim

[analysis] [Stage 3](03-companies.md) gives a one-seat hypothetical reference basket, not an observed operator stack:

- TradingView Essential: 12 × $12.95 = **$155.40** ([vendor pricing](https://www.tradingview.com/pricing/)).
- Tradervue Gold: 12 × $49.95 = **$599.40** ([vendor pricing](https://www.tradervue.com/site/pricing/)).
- Airtable Team: 12 × $20 = **$240.00** ([vendor pricing](https://www.airtable.com/pricing)).
- QuickBooks Simple Start, steady regular price: 12 × $38 = **$456.00** ([vendor pricing](https://quickbooks.intuit.com/pricing/)).

[analysis] **USD reference subtotal = $1,450.80/year.** Separately, the retrieved Workspace quote was EUR: 12 × €6.80 = **€81.60/year** ([vendor pricing](https://workspace.google.com/pricing.html)). Do not add currencies without a dated conversion assumption. Broker charges, data/exchange entitlements, accounting services, device, connectivity and other costs remain unknown. Product promotions and renewal conditions must be reconfirmed; the full all-in stack tax is null.

[analysis] The initial wedge plausibly competes with the journal and custom case-board roles, whose selected reference subtotal is **$599.40 + $240 = $839.40/year**. That is not cash saved. It is not proof the operator owns both products, can cancel them, or would replace them with this system. Broker/data, charting and professional bookkeeping are retained until equivalent outcomes and actual avoidable costs are established.

[practitioner] The spreadsheet user who reports “one copy and paste with 2 clicks and done” explicitly challenges the paid-product premise: [P01 thread](https://www.reddit.com/r/Daytrading/comments/14y4zlz/how_do_you_journal_your_trades/). [analysis] For that operator, subscription displacement may be zero. Do not infer willingness to pay from another vendor's price.

## Operating cost is not zero because hosting is local

[analysis] SISO-hosted infrastructure cost is excluded **by design**, not measured away. Actual annual operating cost must include user-side incremental hardware/storage/backup/power, selected feed/API charges, updates, recovery and support. Optional notebooks, engines and local models change the resource profile and should not be bundled into the first trial without measurement.

[analysis] First-deployment change cost includes source-model review, safe packaging, importer configuration, migration mapping, historical reconciliation, fixture work, privacy/rights review, installation, user training and acceptance. No hours, rates or fixed implementation price have been measured here. One deployment's total cost is therefore **null**, not a guessed inexpensive container bill.

## Hours returned per week: a measurable hypothesis

[analysis] For each eligible stage i, measure weekly completed units N_i and human minutes per accepted unit before and after assistance, including reading, exception handling, correction and review. Then:

```text
weekly_capacity_hours = sum_i(N_i × (baseline_minutes_i − assisted_minutes_i)) / 60
```

[analysis] In the first pilot restrict the calculation to W08 import/reconciliation and W09 review. An automated file import that creates extra reconciliation work can have a negative result. Do not add a second benefit for the same minutes under “journal automation,” “AI productivity” and “accounting savings.” Record a benefit ID and allocation boundary.

[analysis] **Hours returned per week: null / unmeasured.** A useful initial question is whether the system reduces the total time required to reach a correct, source-linked review compared with the participant's actual broker-export/spreadsheet/journal workflow. It is not whether an LLM produces more text or a dashboard contains more statistics.

## Pilot design and acceptance criteria — proposed, not executed

[analysis] Use consented, redacted historical fixtures and then a bounded prospective comparison on the participant's actual laptop. Include normal and exception cases; do not compare an easy assisted sample with difficult baseline work. A before/after design can be confounded by learning or changing trading activity, so preserve the case mix and state those limits.

| Measurement | Required receipt | Failure condition |
|---|---|---|
| Import completeness | Source-file hash; counts by event type; parser warnings; accepted/unmatched/corrected records. | Unknown fields, dropped fees or duplicate events are silently accepted. |
| Reconciliation quality | Source-linked amounts, currency and identities; explicit unresolved differences; reviewer acceptance. | A difference is hidden or a balancing record is invented. |
| Review usefulness | Same concrete questions answered under baseline and assisted workflows; original thesis preserved. | More output does not improve the ability to recover why a decision was made and what happened. |
| Total human time | Timestamped active minutes including setup, review, rework, support and exceptions, normalized to accepted cases. | Assisted reviewed effort is not lower for the intended population/case mix. |
| Local privacy / resilience | Network observation, local storage inventory, sleep/offline recovery and a clean restore. | Core operation depends on an undeclared remote service or private records leave the intended boundary. |
| Avoidable spend | Actual invoice, cancellation eligibility/date, substitute acceptance and benefit owner sign-off. | A list price is counted despite no real cancellable subscription. |
| Incremental cost | Change log, support time, resource measurements and external-service bills. | Deployment/support/rework exceeds the value being claimed. |

[analysis] Ten fixture classes are specified in [05-assembly.json](05-assembly.json): duplicate file, overlapping reports, partial fills, correction/cancellation, fees/currencies, exercise/assignment, unknown XML fields, unmatched instruments, malformed/oversized files, and sleep/network/restore. They are a test plan, not ten passing tests. A small successful sample would establish only bounded evidence, not universal broker correctness.

## Cash and capacity must stay separate

[vendor/project-owner] The existing observed-value formula is:

```text
first_year_net_cash = verified_cancelled_software_spend
                   + verified_realized_labor_cash_savings
                   + verified_incremental_contribution_margin
                   + verified_risk_loss_reduction
                   − annual_operating_cost
                   − first_year_change_cost
```

Source: [observed-value model](https://github.com/sisodias/great-library-of-siso/blob/main/research/industries/source/intelligence/agency/economics/observed-value-model.json).

[analysis] For an own-account operator, recovered personal hours need not reduce payroll. Do not convert them into profit at an invented hourly rate. Do not treat simulated strategy returns as incremental contribution margin, or count an unobserved avoided trading loss as risk reduction. All six cash inputs and the resulting first-year net cash remain **null**. Negative observed results must remain negative rather than be clipped to zero.

## Migration cost and the second installation

[analysis] Exporting trades is not necessarily exporting notes, tags, images, plan revisions and broker identifiers. Before quoting a migration, obtain a representative export from the actual incumbent, map fields, test import/export round trips, reconcile historical totals and preserve the original source. Where an export surface is not verified, cost is unknown; do not call the lock-in free.

[analysis] The second deployment can reuse packaging, mappings and fixtures **only when** the operator has the same broker/report version, OS/architecture and workflow requirements. Its incremental cost is configuration + new data/exception mapping + migration/reconciliation + regression/acceptance + training/support + rights/entitlement differences. Shared engineering is amortizable; customer-specific support is not automatically near-zero. Measure both separately and report the actual second-install receipt.

[analysis] Relevant pilot economics are net benefit per accepted deployment multiplied by the number of eligible, reachable operators who actually adopt, minus acquisition/support and transition costs. **Eligible operators, adoption fraction and willingness to pay are all unknown.** Brokerage-account counts, GitHub stars and vendor customer counts are not interchangeable with this target population. No market-size dollar estimate is generated.

## The wedge and the falsifier

[analysis] **Wedge:** import one broker statement, expose what cannot be reconciled, and connect accepted executions to the operator's original reasoning and review. It is narrower and testable before taking credentials, replacing the broker, rebuilding a research terminal or migrating an accountant's system.

[analysis] **Reject the thesis for this segment if** the incumbent spreadsheet/journal already answers the same questions at equal or lower total effort and acceptable quality; source fidelity cannot be preserved; the strict-local profile needs undeclared cloud services; ongoing exception/support costs exceed observed benefit; or operators will not migrate their context even when the measured result is better. Any critical unauthorized action/data exposure blocks adoption regardless of apparent time savings.

[analysis] **Decision: yes to a bounded read-only pilot; no to a full-product, return-improvement or production-readiness claim.** The first buyer-facing offer cannot honestly be priced until the baseline, migration and operating costs are measured. This conclusion preserves the operating-workflow direction while making the whole investment falsifiable.
