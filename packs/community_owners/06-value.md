# 06 — The value case and falsifier

**2026-09-14 · research hypothesis · no observed customer savings, deployment or retention lift.**

## Decision

[analysis] **Yes to a narrowly scoped, measured reconciliation/onboarding pilot; no to committing to a full community-platform replacement yet.** The evidence points toward joining the conversation, receipt, entitlement and first useful peer connection. It does not establish that another Skool-style interface alone deserves migration. The incomplete 100-repository funnel, bank reconciliation, live-call testing and migration fidelity prevent a production-build verdict.

## Stack tax versus cost to operate

[analysis] Stage 3 prices a hypothetical 300-member, $49/month community: **$4,800/year fixed subscriptions + $1,764 Circle platform fee = $6,564/year**. This is a selected basket, not every competing vendor added together. Keep Workspace and QuickBooks at **$624/year**. Maximum candidate displacement is therefore **$5,940/year**, not proven savings. Full source links and arithmetic are in [03-companies.md](03-companies.md) and [03-cost-model.json](03-cost-model.json).

| Replacement input | Annual USD | Evidence and qualification |
|---|---:|---|
| Client VPS, 16 GiB / eight shared vCPUs | 1,152.00 | [vendor] $96 × 12, regular bundled [DigitalOcean quote](https://www.digitalocean.com/pricing/droplets), observed 2026-09-14. Not a tested capacity floor. |
| Weekly system backup | 230.40 | [vendor + arithmetic] 20% × $1,152; [backup pricing](https://docs.digitalocean.com/products/backups/details/pricing/). Not a complete recovery design. |
| Routine maintenance allowance | 1,800.00 | [analysis] 2 hours/month × $75/hour × 12; neither rate nor time is a customer invoice or measured labor cost. |
| **Priced infrastructure + assumed maintenance subtotal** | **3,182.40** | [analysis] Excludes unresolved items below. |
| SMTP/email, messaging, selected module license, extra backup storage/egress, incident overhead | **Unknown** | [analysis] Not zero; requires client account, release and workload quotes. |
| **Total replacement operating cost** | **Unknown** | [analysis] Do not turn the subtotal into an all-in offer. |

[analysis] Let **X** be the unpriced annual costs above plus any service that cannot actually be cancelled. Then the optimistic recurring difference is **$5,940 − $3,182.40 − X = $2,757.60 − X/year**, before migration and commercial margin. If X exceeds $2,757.60, there is no cash-saving case at this scenario and labor allowance. A wider machine or licensed video/mobile feature may consume that entire difference.

[analysis] Maintenance sensitivity, keeping the same $75/hour assumption: one hour/month gives a $2,282.40 subtotal and $3,657.60 − X difference; two hours gives $3,182.40 and $2,757.60 − X; four hours gives $4,982.40 and only $957.60 − X. The meaningful unknown is ongoing support effort, not whether the code download is free.

[analysis] The modeled payment rails of $7,430.40/year in Stage 3 are **retained scenario costs**, not replaced software savings. Card fees, processor billing fees, disputes, taxes and FX depend on the actual merchant route. No customer contract or refund ledger was inspected.

[vendor] [Skool Pro](https://www.skool.com/pricing) lists $99/month and a 2.9% fee; [Kajabi Growth](https://www.kajabi.com/pricing) lists $199/month on annual billing at the reviewed scale. [analysis] These are serious counterexamples to a blanket “self-hosting is cheaper” claim: Skool fixed price is $1,188 and Kajabi Growth is $2,388, both below the replacement subtotal before all remaining costs. Their fee bases, included capabilities and fit differ; compare actual matched baskets, not this incomplete fixed-price observation alone.

## Hours returned: explicit unmeasured model

[analysis] The following are planning assumptions from the workflow map, **not measured timings**. “Assisted” includes triage, review and correction. Live community facilitation, content quality, relationship building and exceptional decisions are not assumed to disappear.

| Stage | Cases/week assumed | Baseline minutes/case | Assisted minutes/case | Candidate minutes/week returned |
|---|---:|---:|---:|---:|
| W01 | 20 | 3 | 2 | 20 |
| W02 | 40 | 6 | 4 | 80 |
| W03 | 8 | 12 | 6 | 48 |
| W04 | 3 | 15 | 8 | 21 |
| W05 | 20 | 3 | 2.5 | 10 |
| W06 | 2 | 20 | 10 | 20 |
| W07 | 1 | 45 | 40 | 5 |
| W08 | 10 | 8 | 6 | 20 |
| W09 | 2 | 10 | 6 | 8 |
| W10 | 1 | 45 | 25 | 20 |
| **Total** | | | | **252 = 4.2 hours/week** |

[analysis] The arithmetic annualizes to 218.4 hours only if the same weekly pattern holds all 52 weeks. No cash value, payroll reduction or retention revenue is assigned. Frequency × minutes does not establish causality or adoption. Actual accepted-time savings, customer cancellations and contribution margin remain null under the [Foundry value model](https://github.com/sisodias/great-library-of-siso/blob/main/research/industries/source/intelligence/agency/economics/observed-value-model.json).

[analysis] To prove the claim, collect a consented four-week baseline using stable case definitions; record every touch, waiting period, correction, escalation and outcome separately. Then test the narrow wedge on a matched cohort or controlled sequence, retaining the same quality/authorization bar. Include exception cases and restore/support labor. Report medians, spread, case counts and failure counts, not only a favorable average. A small sample cannot establish retention lift.

## The adoption wedge

[analysis] Start with **conversation → verified receipt → authorized access → first useful peer connection**. A moderator should be able to see why the person paid, which offer version they bought, whether access matches, who owns the exception and whether the first introduction happened, without retyping a chat into a membership spreadsheet. The initial pilot can be read-only reconciliation and human-approved resolution; members need not migrate their entire discussion history to test it.

[practitioner] The underlying signals are [notification/contribution burden](https://www.reddit.com/r/CommunityManager/comments/1s8n61r/im_building_a_community_platform_would_like_to/), [manual renewal checks in an adjacent membership organization](https://www.reddit.com/r/nonprofit/comments/woyt39/membership_management/) and [fragile administrator handoffs](https://www.reddit.com/r/Theatre/comments/rykiri/can_anyone_recommend_a_membership_app/). [analysis] These justify questions to test, not a prevalence estimate or automatic fit to all paid communities.

## Migration and second-deployment economics

[analysis] First migration allowance: **80 hours × $75 = $6,000**, an unmeasured planning budget: offer/permission inventory 12h; member/receipt/consent reconciliation 20h; content/media/event export trials 16h; replay/access/restore tests 16h; moderator training and parallel run 12h; cutover/rollback 4h. This excludes a large proprietary media conversion, bespoke app stores or a merchant-of-record transfer. A failed export trial can invalidate the budget.

[analysis] At the optimistic X = 0 recurring difference, first migration alone takes about **2.18 years** to recover ($6,000 / $2,757.60), before build cost, margin and any incident. There is no warranted fast-payback claim. Community habits and the loss of history may be more costly than engineering; quantify member consent and risk before any cutover.

[analysis] Second deployment allowance after a validated reusable assembly: **24 hours × $75 = $1,800** for configuration/import validation/training, plus its own VPS, backup, license, transport and maintenance costs. This is not measured replication. It is lower only if the same offer/identity/import patterns recur; otherwise bespoke exceptions erase reuse. Do not amortize development against a made-up customer count.

[analysis] **Segment operator count: null.** No independent count for evergreen professional paid peer/accountability communities was established. General creator totals, platform accounts and a vendor’s cumulative communities are not equivalent to paying addressable operators. Build an evidence-backed operator sampling frame, qualify workflow similarity and migration willingness, and separate an owner with several communities from several buyers.

[analysis] Portfolio arithmetic, not a market estimate: for N qualified clients, annual contribution is N × (annual service price − client-specific operating/support cost) minus shared ongoing cost; recovery of the initial build also requires each migration cost and acquisition cost. Both N and a validated service price remain unknown. The second deployment must demonstrate lower *accepted* effort, not just fewer files typed.

## Falsifier for the whole thesis

[analysis] Reject the full replacement if existing low-cost hosted tools deliver the needed outcome at lower all-in cost; if the operator’s problem is weak community value rather than administration; if receipt/identity reconciliation is too rare to justify change; if human review and support erase the modeled 4.2h/week; if permissions/consent cannot survive migration; or if required private live calls cannot fit an acceptably priced single client VPS. Any unauthorized access, unapproved refund/send, privacy leak or lost subscription history stops the pilot until resolved.

[analysis] Continue beyond the pilot only when a real operator chooses the wedge, measured net handling time improves without worse outcomes, matched cancellable spend exceeds complete replacement cost, exports/restores pass, and a second installation reproduces the result. **Current decision: research/pilot candidate, not production admitted.**
