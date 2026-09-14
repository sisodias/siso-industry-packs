# 05 — Proposed super-app assembly

**Research blueprint only · 2026-09-14 · no application code, deployment or production qualification.**

[analysis] This is a provisional assembly inside a ten-repository screen, not the result of the required completed 100-repository funnel. Build nothing until the evidence gates in [04](04-oss-candidates.md) and this file are satisfied. The owner sells an ongoing professional peer community; courses are a secondary benefit, not the architecture’s center.

## The six-object spine

[analysis] The spine is the small layer we own, not a second copy of every product database. It stores references, versions, permissions and decision evidence. Each source application keeps authority for its own records.

| Aggregate | Minimum persistent fields | Authority and boundary |
|---|---|---|
| Member | internal ID; confirmed external identities; contact preference/consent references; role; merge history | Confirm identity before linking channels. Never infer two people are the same from a matching display name. |
| Offer | version; included spaces/events/resources; price reference; claims approval; effective dates | Preserve what was promised at sale, including grandfathered benefits. No rewriting history on a price change. |
| Membership | member; offer version; processor/customer/subscription references; start/end/grace; approved decision | Processor owns financial status; native community groups enforce access. The spine records the reconciled decision and its evidence. |
| Interaction | original channel/message reference; member reference; assigned human; intent; next action; approval | Staff inbox owns conversation history. Private member DMs are not bulk-copied into a staff-readable warehouse. |
| Experience | event/resource/introduction type; owner; access group; timezone; capacity; content/recording references | Native platform owns discussion/media. RSVP is not attendance; attendance is not member success or learning. |
| LedgerEntry | source system and event ID; received time; effective time; linked object; decision; approver; reversal reference | Append-only operational evidence, not statutory accounting. Keep raw provider payloads only where authorized and needed. |

## Component map and alternatives

[analysis] Candidate choices are tied to the [upstream evidence table](04-oss-candidates.md), not brand familiarity. ADOPT means reuse the existing application rather than rebuild it, contingent on validation. It does not mean install it now.

| Stages | Candidate | What we own | Comparison / remaining decision |
|---|---|---|---|
| W01–02 intake | Chatwoot community edition | Verified Member/Interaction cross-links; approved FAQ and next-action context | Discourse member chat is not an omnichannel staff inbox. Wider helpdesk comparison remains unfinished. |
| W03 payment/access | Discourse native subscription/group mechanism; processor stays external | Read-only receipt checks, exception review and approved membership transition evidence | PMPro is a serious alternative for an existing WordPress site, not an extra billing engine on top. |
| W04–05 onboarding/community | Discourse | First-peer-introduction queue, notification preferences and benefit eligibility | NodeBB/Flarum are forum comparators; HumHub’s social spaces may fit better. No final comparative UX verdict. |
| W06 events | Community event metadata; Jitsi is STUDY, not admitted | Private-room eligibility, capacity, calendar linkage and manual host controls | Self-hosted live-call parity is a release blocker. The plan must not silently substitute public meet.jit.si or Zoom. |
| W07 secondary resources | Discourse content and access groups | Offer-to-resource version mapping and rights/accessibility review | Full SCORM/LMS/credentialing is not this segment’s primary need and is not claimed. |
| W08 retention | Listmonk + permissioned Directus operations views | Consent-aware cohorts, risk flags and a human next-action queue | A newsletter manager is not proven equivalent to the entire Email Hub marketing-journey feature set. |
| W09 referrals | Directus operational ledger; manual payout approval | Attribution, refund reversals and fraud-review records | A production affiliate engine is a gap. Do not pretend a table is an audited payout system. |
| W10 close/handoff | Directus exports and evidence; retain accountant/QBO | ID-preserving export, source reconciliation and owner handoff | Do not rebuild accounting or payroll. Full accounting replacement is not counted as savings. |
| Cross-stage | Activepieces only where native tools do not suffice | Allowlisted routing, review tasks, idempotency and compensating actions | Omit redundant automation. No unrestricted agent gets refund, access or publication authority. |

[vendor] Evidence anchors: [Discourse](https://github.com/discourse/discourse), [bundled subscriptions](https://github.com/discourse/discourse-subscriptions/blob/main/README.md), [Chatwoot](https://github.com/chatwoot/chatwoot), [Directus license](https://github.com/directus/directus/blob/main/license), [Listmonk](https://github.com/knadh/listmonk), [Activepieces](https://github.com/activepieces/activepieces), [Jitsi](https://github.com/jitsi/jitsi-meet). Exact observations and qualifications are in [04 JSON](04-oss-candidates.json).

## The glue that must be paid for

[analysis] The difficult work is identity and authority, not putting five logos in one menu. A community login, a Stripe customer, an email subscription and an Instagram conversation are different identities. Link them through an authenticated account-linking challenge or a reviewed reconciliation; preserve merges and reversals. Member access and staff access are different permission systems. Never solve single sign-on by sharing one administrator credential or directly editing another application’s tables.

[analysis] A verified receipt starts a case, not an irreversible action. Deduplicate provider event IDs; tolerate retry, delayed delivery, out-of-order cancellation and changed offer versions. Store both received time and effective time. Fetch the provider’s current state for reconciliation. An authorized human approves refunds, non-routine access transitions and other consequential actions. Keep a reasoned exception queue when evidence conflicts; do not grant broad access just because a workflow timed out.

[analysis] Record source version and external ID, not just a copied display label. Give integrations narrowly scoped credentials, rotate them without rebuilding member identities, redact logs, and keep secrets out of exports. Signed short-lived attachment access, upload scanning, deletion requests, consent suppression and audit retention need specific implementation review. These are design requirements, not security claims about a running system.

[analysis] Native application APIs are the mutation surface. Any polling/import fallback has an explicit staleness window and owner. Jobs require bounded retries, a dead-letter/exception state, replay logs and a tested way to reverse errors. Permission failures must remain visible. A green job result is not proof that a member can enter the correct space.

[analysis] Before enabling native payment/group automation, verify it can honor the retained authorization boundary. If its automatic lifecycle cannot wait for the required approval, do not enable that mutation mode: keep the first wedge read-only reconciliation plus approved manual group changes. Existing upstream functionality is not permission to automate refunds or access decisions.

## Client-owned deployment

[analysis] All application state, jobs, databases and primary uploads live on **one VPS owned and paid for by this client**. Separate client: separate VPS and credentials. There is no SISO-hosted control plane or shared member database. The client retains DNS, processor, email-provider and backup accounts. A managed payment network or authorized messaging transport is an external rail, not a self-hosted application; the distinction cannot be engineered away.

```text
Member browser                         Operator browser
     |                                      |
     +----------- client HTTPS edge --------+
                         |
           +-------------+-----------------+
           |             |                 |
       Discourse     Chatwoot       permissioned operations UI
       members/chat  staff inbox       Directus spine
           |             |                 |
           +-------- approved API links ---+
                         |
                bounded jobs / optional Activepieces
                         |
          Listmonk      PostgreSQL databases     upload volumes
          email jobs    separate app roles       client-owned
                         |
              encrypted recovery/export to client storage

External, client-owned rails: processor; SMTP delivery; authorized channel APIs.
Jitsi live-call services: candidate on this same box, OFF until capacity/access tests.
No member data or runtime hosted by SISO.
```

[analysis] **Planning budget, not a proven minimum:** 16 GiB RAM, eight shared vCPUs and 320 GiB disk. Non-video RAM allowances: OS/edge 1; PostgreSQL 2; Discourse 3; Chatwoot/workers 3; Directus 1; Listmonk 0.5; optional Activepieces/workers 1.5; cache/headroom 4 GiB. These sum to 16. They are not vendor minimums or a claim all components can safely run concurrently. Background imports, backups, antivirus, bursts and migrations must be included in load tests. Compatible database/cache versions and separate application users are mandatory design checks, not assumed compatibility.

[vendor] The regular bundled [DigitalOcean price table](https://www.digitalocean.com/pricing/droplets), observed 2026-09-14, lists that 16-GiB/8-vCPU/320-GiB/6,000-GiB-transfer plan at **$96/month**. [Weekly system backups](https://docs.digitalocean.com/products/backups/details/pricing/) add 20%. [analysis] This is a transparent comparison quote, not a provider recommendation, purchase or claim of current account/region availability. New flexible v5 configurations have different pricing; verify the selected SKU before an offer.

[analysis] One box means one failure domain; no high-availability claim. Weekly provider snapshots do not establish a sufficient membership/payment recovery point. Require client-controlled encrypted database/upload exports, a documented recovery objective, a separate recovery destination, credential recovery and a real restore test. Additional backup storage, email deliverability, taxes, domains, licenses and egress are not fully priced. No GPU or model-provider subscription is assumed.

[analysis] **Live calls are a hard gate.** Test two weekly private sessions, up to 15 simultaneous participants, while moderation, email jobs and backups run. Measure CPU, memory, loss/jitter, outbound traffic and recovery. Recording/transcoding is excluded until separately tested. If the client requires larger calls or heavy recording and the same-box design fails, either resize and reprice the single client box or reject this target configuration. Do not quietly move it onto SISO servers or call a hosted video service self-hosted.

## Build versus lift, screens and acceptance

[analysis] Reuse native community, inbox, email, admin and workflow components. Write only the cross-system model, carefully scoped adapters, permissioned operator screens and migration/verification work. “Roughly five percent bespoke” is an aspiration, not an estimate: glue and acceptance may dominate effort. No new UI-library search is needed; use the existing component bank for screens after permissioned workflow design.

[analysis] Required screens: operator Today/Exceptions; member record with provenance; inbox-to-membership case; offer/benefit versions; onboarding/introduction queue; event/RSVP view; moderation appeal queue; retention/consent queue; referral review; finance/export/recovery checklist. Members keep a coherent community front door rather than a bundle of staff application tabs. UI accessibility and actual member comprehension remain untested.

[analysis] Acceptance requires: identity-linking challenges; least-privilege roles; replay of duplicated/delayed/reordered events; cancellation/grace/refund cases; consent suppression and approved sends; 15-person private calls; complete trial exports and restored permissions; recovery from a failed upgrade; measured moderator/member usability; and release-specific license/security review. Pin stable release/image digests only after this work. The latest development commit in Stage 4 is not a deployment recommendation.

## Honest gaps — 10

[analysis] (1) live-call co-hosting capacity; (2) native mobile distribution/push parity; (3) DM/history/media migration fidelity; (4) external processor/email/messaging rails; (5) useful peer matching and retention effects; (6) human moderation/claims/refund authority; (7) selected module licensing and commercial clearance; (8) restore, availability, security and accessibility acceptance; (9) affiliate fraud, tax and reversal handling; (10) target-segment population and repeatable deployment cost. These are gaps in this examined assembly, **not a universal claim that no OSS exists**.

Machine-readable proposal: [05-assembly.json](05-assembly.json).
