# Stage 6 — The value case

**As of 2026-09-13. USD, before taxes. All operating volumes, labour rates and build/migration hours below are explicitly unmeasured planning assumptions.**

[analysis] **Verdict: YES to a bounded, paid, supervised intake/evidence pilot; NO to claiming an economical whole-stack replacement today.** The specific wedge is the transition from scattered messages/files to a correct, complete, source-linked packet accepted by the responsible lawyer. The [practitioner evidence](01-person.md) supports this as a problem hypothesis. It does not establish demand, achievable savings or willingness to pay. Compare against configuring the firm's existing software before building another system.

## 1. Subscription stack tax is not subscription savings

[vendor] Current list-price evidence and the full arithmetic are in [Stage 3](03-companies.md): MyCase Pro, Microsoft 365 Business Standard, Airtable Team, QuickBooks Essentials, Gusto Simple, Quo Starter and two individual Acrobat Pro subscriptions total **$9,527.76/year** for the defined four-person design case. This excludes unknown legal-research subscriptions, court/service fees, usage charges, taxes and implementation quotes; the exact all-in business bill is **null**.

[analysis] The first wedge might eliminate **four Airtable Team editing seats: 4 × $20 × 12 = $960/year**, only after a real cancellation and proof that its bespoke linked-record workflows have been replaced. It does **not** justify cancelling the practice manager, Office, trust/general accounting, payroll, telephone network, final PDF tools or legal-research content. Avoid a double charge for calendar/signature features already bundled with other products. Actual installed subscriptions, renewal dates and cancellation terms must be read from the customer's contracts before any cash claim.

| Item | Amount / year | Evidence status |
|---|---:|---|
| Selected incumbent subscription basket | $9,527.76 | [vendor + analysis] Dated vendor tariffs × specified quantities; not an observed invoice. |
| Initially cancellable hypothesis | $960.00 | [analysis, unmeasured] Airtable only; conditional on successful replacement and cancellation. |
| Incumbent subscriptions retained in that scenario | $8,567.76 | [analysis] 9,527.76 − 960. |
| Actual verified cash savings | **null** | [analysis] No client bill or cancellation was inspected. |

## 2. What the client's own box costs

[vendor] [DigitalOcean's current Droplet price table](https://www.digitalocean.com/pricing/droplets) lists Basic 8 GiB/4 vCPU/160 GiB at **$48/month** and 16 GiB/8 vCPU/320 GiB at **$96/month**. [Basic daily backups](https://docs.digitalocean.com/products/backups/details/pricing/) add **30%** of Droplet cost. [Spaces Standard](https://docs.digitalocean.com/products/spaces/details/pricing/) starts at **$5/month** for 250 GiB shared storage and 1,024 GiB outbound transfer; additional storage is $0.02/GiB/month. These are vendor prices observed 2026-09-13, not benchmarks proving workload fit.

[analysis] Budget the fuller review pilot on one **client-owned 16 GiB VPS**, with constrained extraction jobs and no GPU. An 8 GiB lean intake-only profile is a test candidate, not a promise to run every shortlisted application concurrently. The client also owns the encrypted off-box backup destination and keys. One compute box does not mean one copy of the files. A same-provider bucket in another region is a different storage location but not complete provider/account-failure independence; a separately administered second-provider copy needs a separate quote. No client documents, backups or telemetry payloads live on SISO servers.

| Proposed annual operating item | Arithmetic | USD/year |
|---|---|---:|
| 16 GiB client-owned VPS | 96 × 12 | $1,152.00 |
| Daily provider image backups | 96 × 30% × 12 | $345.60 |
| Encrypted off-box backup storage allowance | 5 × 12, within included usage | $60.00 |
| Domain allowance | Explicit unmeasured procurement allowance | $20.00 |
| **Infrastructure subtotal** | 1,152 + 345.60 + 60 + 20 | **$1,577.60** |
| Maintenance, updates, restore rehearsal and support | **Unmeasured** 2 hours/month × $75/hour × 12 | $1,800.00 |
| **Steady operational resource cost** | 1,577.60 + 1,800 | **$3,377.60** |

[analysis] This is a floor scenario, not a fixed quote. It excludes overage, a separately governed second-provider backup, paid module entitlements, incident response, insurance, customer support spikes, new templates, legal review, external channels/content and implementation. A crash-consistent image backup does not demonstrate application-consistent restoration. Representative data volume, extraction concurrency, retained originals/derivatives, log growth and full restore duration must be measured. If 250 GiB is insufficient, the vendor storage formula must be applied to retained backup bytes, not merely today's source-folder size.

[analysis] **Subscription-only steady cash/resource result: $960 − $3,377.60 = −$2,417.60/year.** That is a cost increase before recovering build or migration work. The firm would retain $8,567.76 in incumbent subscriptions and consume $3,377.60 in new operating resources: $11,945.36 versus the $9,527.76 basket. Do not present the $9,527.76 tax as money the project has saved.

[analysis] For sensitivity, the lean 8 GiB infrastructure profile is `(48 × 1.30 + 5) × 12 + 20 = $828.80/year`; with the same assumed support it is $2,628.80/year, still $1,668.80 above the proposed $960 cancellation. Resource sufficiency and support load, not the cheapest advertised VPS, determine admission.

## 3. Hours returned — a hypothesis to falsify

[analysis] These are **proposed weekly pilot volumes and net-minute targets**, not observations. “Net” includes review, corrections, exception handling, retries and chase. Each item corresponds to the event units in [Stage 2](02-workflow.md). The work categories must be made mutually exclusive in measurement: do not count the same client-message handling under both intake and follow-up or count document review twice.

| Work category | Hypothesised weekly volume | Target net minutes returned per unit | Hypothesised minutes/week |
|---|---:|---:|---:|
| Accepted intake packets, including missing-information chase | 20 | 6 | 120 |
| Approved-template work products, including review/rework | 6 | 12 | 72 |
| Evidence batches, excluding substantive legal review | 10 | 5 | 50 |
| Approved administrative client updates, excluding intake chase | 20 | 3 | 60 |
| Time-entry exceptions, excluding activity already counted above | 80 | 1 | 80 |
| **Total, entirely unmeasured** | — | — | **382 minutes = 6.37 hours/week** |

[analysis] **Baseline needed:** observe a baseline period and a shadow/pilot period using comparable matter complexity and channel mix. Timestamp start, interruption, handoff, review, acceptance, rework and abandonment. Track incomplete/rejected packets as well as successful ones, and report medians, tails, task mix and sample counts. Record lawyer minutes separately from staff minutes. If moving work from a paralegal to a lawyer produces a superficially shorter process at higher total cost, it is not the claimed benefit.

[analysis] Required unit metrics: human minutes per complete accepted intake; human minutes per correct reviewed document; accepted source-supported findings per reviewer hour; coordination minutes per correctly completed signing task; minutes per accurate approved update including retries; minutes per resolved billing exception and actual corrections. These preserve the [Foundry metrics](https://github.com/sisodias/great-library-of-siso/blob/main/research/industries/source/intelligence/agency/industries/law_firms.json). There is no pre-existing measurement in this pack.

[analysis] A shadow value using **46 working weeks and $75/hour**, both assumptions, is `382/60 × 46 × 75 = $21,965/year`. This is **capacity at an assumed valuation, not cash, collected fees, contribution margin or an avoided hire**. It becomes cash only through a separately observed mechanism such as reduced paid overtime, a genuinely avoided hire or additional work accepted, performed and paid—with its incremental costs deducted. Do not count the same hours as all three. This separation follows [SISO's observed-value model](https://github.com/sisodias/great-library-of-siso/blob/main/research/industries/source/intelligence/agency/economics/observed-value-model.json).

[analysis] At that hypothetical $75/hour shadow rate, the steady incremental $2,417.60 requires approximately **0.70 genuinely usable hours/week** across 46 weeks just to offset operating resource cost; the target 6.37 hours is not proof it clears that bar. At zero marginal cash value for freed time, there is no labour-based cash payback. Quality improvements may still matter, but their monetary value is unmeasured rather than filled with a speculative malpractice-loss estimate.

## 4. Enter through one door, not a forced migration

[analysis] **Pilot one intake mailbox, one approved template/checklist family and one document class.** Run proposed links/findings in shadow beside the incumbent. Human staff reconcile every result. Keep the current practice manager authoritative and use reversible exports first; enable live outgoing messages only after identity, current-status and idempotency tests pass. Compare three arms where practical: current process; better configuration of the current product; proposed local sidecar. A sidecar that merely reproduces already paid-for incumbent functionality loses.

[analysis] The wedge is accepted only when the responsible lawyer receives a better packet with no extra reconstruction, missing source, wrong party or hidden ambiguity. “The form submitted successfully” is not success. The weakest viable pilot deliberately excludes automatic conflict clearance, deadline calculation, court filing, trust accounting and external AI processing of client documents.

## 5. Migration and exit — priced rather than waved away

[analysis] Proposed **second-firm onboarding** assumes a modest document population, a supported incumbent export and reuse of an already tested assembly. These are allowances, not a fixed bid:

| Work | Staff/engineering hours, unmeasured |
|---|---:|
| Inventory subscriptions, access, retention and export rights | 4 |
| Map party/matter identifiers, aliases, custom fields and message links | 8 |
| Configure approved checklist/template and routing boundaries | 6 |
| Trial import, reconciliation, representative attachment/version checks | 8 |
| Training and parallel operation | 6 |
| Restore/exit rehearsal and handover | 4 |
| **Total** | **36 hours** |

[analysis] At assumed $75/hour, that is **$2,700**, plus **8 hours of responsible lawyer review at an assumed $150/hour = $1,200**, or **$3,900 of onboarding resource cost**. Staff/lawyer figures represent different work and must not be billed twice when the same person performs both. API access charges, blocked exports, unusual file formats, inaccessible historical message bodies, corrupt files and new jurisdictional templates are extras requiring a quote or a no-go. [Stage 3](03-companies.md) identifies lock-in objects and explicitly unverified export/API entitlements.

[analysis] Adding this first-year migration allowance to steady incremental cost gives **$6,317.60** before reusable product R&D. At the same hypothetical $75/hour and 46-week convention, that requires **1.83 usable hours/week** of capacity value. It still does not establish cash payback.

[analysis] **Exit is an acceptance test:** export stable IDs, party roles, complete original messages where permitted, original and released document bytes, family/provenance links, source spans, task/deadline verification history, financial references, access policy and a manifest of exclusions. Compare counts and hashes, then restore in an isolated client-controlled environment. Vendor exportability is not inferred from the existence of an API. Leave old services read-only for an agreed overlap, retain rollback ability, and delete only on separately authorised policy decisions.

## 6. Vertical economics and the second deployment

[vendor/source] The ABA's [2025 population release](https://dev.americanbar.org/news/abanews/aba-news-archives/2025/12/aba-2025-profile-of-the-legal-profession-report/) reports **1,374,720 US lawyers in 2025**. That is a dated broad population statistic, **not the number of plaintiff-employment firms, not a 2026 census, and not the addressable customer count**.

[analysis] **Eligible operators in the selected segment: null — not established by the retrieved sources.** Dividing all lawyers by four would mix lawyers with staff, double-count organisations and include unrelated practice areas. The missing denominator is a material commercial gap. A lawful, deduplicated public-firm inventory and actual discovery calls must establish practice focus, workflow pain, incumbent configuration and willingness to pay before a market-size forecast. The public pack contains no harvested contact database.

[analysis] Reusable first-assembly allowance: **240–400 engineering/security/integration hours at $75/hour plus 40 legal-template/acceptance hours at $150/hour = $24,000–$36,000**, entirely unmeasured. This includes spine/adapters, access policy, audit, failure handling, export/restoration, accessible screens and a representative test corpus. It does not assume that adopting 95% of functional components leaves only 5% of integration effort. The second deployment reuses this work but still incurs the **$3,900** onboarding allowance above, its own VPS/backup account and per-firm template/permissions acceptance.

[analysis] An illustrative—not validated—commercial model charges a **$3,000 annual support/assembly fee**, with infrastructure paid directly by the client and separately scoped onboarding. Against the assumed $1,800 annual support labour, it contributes **$1,200/customer-year before sales, insurance, incident reserves, taxes and product maintenance**. Recovering $24,000–$36,000 of reusable build cost would require **20–30 customer-years at that contribution**, before those omitted costs. Onboarding sold at its estimated cost contributes no R&D recovery. This is unit arithmetic, not a sales forecast.

| Hypothetical active clients | Annual support revenue | Assumed direct support labour | Contribution before omitted costs |
|---:|---:|---:|---:|
| 10 | $30,000 | $18,000 | $12,000 |
| 50 | $150,000 | $90,000 | $60,000 |
| 100 | $300,000 | $180,000 | $120,000 |

[analysis] These are sensitivity cases, **not the number of firms that exist or will buy**. Doubling support to four hours/month at $75/hour makes direct labour $3,600/year, exceeding the illustrative $3,000 fee before all other costs. Conversely, more reliable repeatable deployment and lower measured support can improve economics without moving client data onto shared SISO infrastructure. Cross-industry reuse comes from the document/message/approval/export contracts, not from merging client databases or relaxing professional gates.

## 7. Falsifiers for the whole thesis

[analysis] Stop or redesign if any of the following holds in an admitted pilot: the existing vendor can deliver the same accepted workflow with materially less total setup/operating cost; human review and rework erase preparation gains; the firm cannot safely export the required objects; the one-box design cannot meet measured capacity/restoration needs at an acceptable price; repeat support exceeds the fee model; the eligible segment or willingness to pay is too small to recover reuse costs; or any wrong-matter disclosure, lost source, suppressed identity ambiguity, unapproved external action or financial-authority overwrite survives testing.

[analysis] The [GQ-004 contract](https://github.com/sisodias/great-library-of-siso/blob/main/registry/works/frontier-question-gq-004.json) also makes an adoption-cost overrun greater than 2× a falsifier of the estimate's grounding. The [GQ-013 contract](https://github.com/sisodias/great-library-of-siso/blob/main/registry/works/frontier-question-gq-013.json) warns that a larger catalogue can increase integration work without improving the accepted application. Therefore the broad OSS sweep is a rejection funnel, not a mandate to deploy every attractive tool.

[analysis] **Investment decision now:** fund only a reversible, evidence-preserving wedge with an explicit measurement and exit budget. Do not sell verified savings, an autonomous legal practitioner, production-admitted trust accounting, a universal e-filing gateway or a complete replacement for licensed legal content. The blueprint becomes a business case only when the missing customer and acceptance evidence is collected.
