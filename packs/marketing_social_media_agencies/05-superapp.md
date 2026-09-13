# Stage 5 — The assembled operating core

Research date: **2026-09-13**. `[analysis]` This is a **candidate architecture, not implemented application code or a tested deployment**. ADOPT means selected for a bounded integration qualification, not already installed, legally cleared or proven safe. Upstream evidence and dated pins are in [Stage 4](04-oss-candidates.md); machine-readable decisions are in `05-assembly.json`.

## 1. The spine: six objects, one authority for each

[analysis] Use **EspoCRM's existing entity, relationship, task, role and portal machinery** as the product base; define a thin agency-specific model and approval policy on it. Do not build a CRM, table editor, generic project manager or authentication system from scratch. The spine's stable IDs and event contracts are ours; upstream applications keep their own internal schemas. [EspoCRM architecture/custom entities](https://github.com/espocrm/espocrm), [portal relationship and access rules](https://docs.espocrm.com/administration/portal/)

| Object [analysis] | Required fields and relationships | Authority / prohibited shortcut |
|---|---|---|
| **PartyAccount** | Agency ID, client/brand ID, contacts, named approver, platform account IDs, grant references, allowed actions, expiry/revocation, owner | Agency-controlled identity mapping; platform account owner controls grants. A contact is not automatically a subscriber or an authorized approver. Store secret references, not tokens in visible fields |
| **ConversationRequest** | Source channel/message/thread ID, sender identity, received time, attachments, intent, owner, status, linked brand/scope/work item, consent/context reference | Conversation source is evidence; staff explicitly accept routing. Deduplicate by source ID; ambiguous messages do not become an order or approval automatically |
| **EngagementScope** | Deliverables, channels, quantity/duration, exclusions, dates, revision allowance, commercial acceptance evidence, authorized approvers, external invoice/contract IDs, change orders | Owner/customer explicitly agree scope. General ledger, payment processor and payroll provider remain external authorities |
| **CampaignWorkItem** | Brief, audience/claim evidence, content ID, caption and asset versions, per-channel variants, source/derivative relationship, rights/expiry/accessibility checklist, assigned task, proposed schedule | One canonical editable copy/asset reference per version. AssetVersion is subordinate to the work item, not a competing DAM authority |
| **ApprovalRelease** | Work/version hash, account/channel, scope reference, approver identity, decision, timestamp, source evidence, schedule/timezone, idempotency key, release state | Human release authority. Material changes invalidate approval. Queue admission is not publication success; staff cannot bypass the gate through an unrestricted scheduler UI |
| **OutcomeLedger** | Typed publication receipt, metric snapshot, definition/timezone/window, reconciliation result, reviewed report, external invoice/payment status, time/export/revocation/restore receipts | Evidence collection **not a new accounting ledger**. Each record declares its authoritative source. No unsupported causal interpretation or silent financial write |

[analysis] All tables carry agency/brand relationships and stable external IDs. A second agency gets a separate VPS, database credentials, encryption material, domains and backups. Ten brands within one agency are not ten unrelated agency tenants sharing SISO infrastructure. Portal access is an enforced policy, not a filtered view.

## 2. Component map — lift by default, choose against named alternatives

[analysis] The following choices follow the wide sweep, not star ranking. Runners-up remain in the candidate register. Optional modules are **not** all installed on day one. Resource and licence uncertainty can block deployment without deleting the candidate from research.

| Stage | Selected component / disposition | What we own or configure | Why it beats the runners-up in this case |
|---|---|---|---|
| S01/S08 conversation intake | **Chatwoot CE — ADOPT, optional after wedge**; Espo email/manual source-reference capture first | Brand/thread identity mapping, classified request, owner handoff, source evidence and portal access | Broader advertised official-channel surface than an email-only starting point. **FreeScout** is attractive for shared email; **Libredesk** for a lightweight single-binary desk; **Zammad** for service operations. None is assumed to preserve personal WhatsApp groups or confer platform permissions |
| S02 scope, quote and agreement | **EspoCRM core — ADOPT**; retain existing meeting/contract/bookkeeping tools | EngagementScope, approved price/scope record, accepted change order, external contract/invoice references | **SuiteCRM**, **Frappe CRM**, **Twenty**, **Dolibarr** remain viable product bases; Espo's customizable entities and client portal reduce custom surface. **Docuseal/Documenso** remain STUDY optional signature services; no full accounting/signature engine is rebuilt |
| S03 onboarding/assets/account authority | **tusd + tus-js-client — ADOPT** for resumable uploads; **ExifTool — ADOPT** for metadata; **c2patool — ADOPT, optional provenance inspection** | Brand-scoped upload authorization, media manifest, rights evidence, retention, account-owner grant checklist | **ResourceSpace**, **Phraseanet**, **Pimcore** provide richer DAM systems but introduce another asset authority. **Immich/PhotoPrism/Piwigo** are not assumed to supply agency scope/approval semantics. **XMP Toolkit/c2pa-rs** are library alternatives when an actual embedding need appears |
| S04 brief/calendar | **EspoCRM core — ADOPT**; **Activepieces MIT connector pieces — ADOPT selectively**, full engine off by default | Campaign/content entities, calendar projection, import mapping and version references | **Baserow/NocoDB** are strong tabular bases but would still need the same relationship/approval authority; **Plane/Leantime/Kanboard/Planka** are work-management alternatives. Do not recreate all their features or install all of them |
| S05 creative derivatives and QA | **imgproxy + FFmpeg — ADOPT** as restricted workers; keep Adobe/native authoring | Canonical source/derivative links, permitted presets, timeout/resource limits, manual rights/claim/accessibility review | **Sharp/libvips/Thumbor** are close image alternatives; imgproxy offers a service boundary across the mixed-language stack. **PyAV** is useful only if custom frame processing is needed. **Subtitle Edit/ffsubsync/WebVTT** are study/reference tools, not proof of accessible output |
| S06 approval and scope control | **EspoCRM portal/entity framework — ADOPT; thin policy extension is ours** | Exact-version approval, approver authority, signed-in or narrowly scoped review access, change invalidation, append-only application events | A task checkbox in **Kanboard/Plane** or a signature on an unrelated **Docuseal** PDF is not the required approval-to-payload contract. This is the genuine vertical gap; do not claim an upstream app already implements it |
| S07 publication/reconciliation | **Postiz — ADOPT, conditional full phase**; reference its compose dependencies | Approved-release adapter, account/timezone binding, idempotency, queue/receipt reconciliation, revoked-grant block, restricted publishing role | **Mixpost Lite** has a narrower public edition than broad marketing descriptions; **OpenPost**, **TryPost**, **BrightBean Studio**, **Postmill** are real alternatives, not dismissed by low stars alone. Postiz wins provisionally on documented self-host/API integration, not on proven uptime or automatic provider approval |
| S08 community → business lead | **Chatwoot CE — ADOPT, optional**, same service as S01 | FAQ retrieval/drafts, escalation, explicit client-sales handoff receipt; no new audience consent inferred | **Frappe Helpdesk**, **FreeScout** and **Libredesk** remain lower-complexity options where email dominates. No separate chatbot platform is necessary for five initially hypothesized intents |
| S09 reporting/renewal | **Frictionless framework + WeasyPrint — ADOPT** for validated tabular inputs and reviewed report rendering; **Meta Python Business SDK — ADOPT only for authorized supported endpoints** | Metric dictionary, raw snapshot/source ID, mapping/reconciliation, reviewed narrative and accepted report | **Meltano/Singer** and **Airbyte** are connector options, not instant social-report parity; **Metabase/Superset/Lightdash/Redash** display data but do not obtain its rights or definitions. **Umami — ADOPT optional** for owned-web analytics, never a substitute for social metrics |
| S10 invoice/collection | **EspoCRM scope/reference model — ADOPT**; keep QuickBooks and Stripe | Approved draft/handoff and reconciled external status; no autonomous financial mutation | **Invoice Ninja/InvoicePlane/SolidInvoice/ERPNext/Akaunting/Bigcapital** were examined; none is admitted as a replacement for this customer's existing US books, accountant process or payment obligations |
| S11 capacity/time/offboarding | **Espo tasks — ADOPT**; **Kimai — ADOPT optional** after time-capture acceptance; retain Gusto | Task/scope links, reviewed timesheets, approved payroll-input export, explicit account revocation and client export | **Solidtime**, **Ever Gauzy**, **Worklenz** are alternatives. Kimai's JSON API and time/budget functions fit a bounded time ledger; its MySQL/MariaDB requirement is an extra cost, not silently compatible with the shared PostgreSQL plan |

[vendor] Espo's portal documentation specifies relationship-based account/contact access for custom entities. Its core extensibility does **not** make Advanced Pack workflow/BPM/reporting or Sales Pack capabilities free. Build only the narrow agency approval transition and configure supported core features; quote any extension actually selected. [Portal docs](https://docs.espocrm.com/administration/portal/), [core README](https://github.com/espocrm/espocrm/blob/master/README.md)

[vendor] Chatwoot's root licence excludes `enterprise/` from the MIT core; enterprise production use has separate terms. Its free edition lacks enterprise SSO and advanced permissions. Activepieces similarly excludes named enterprise directories from the MIT core. **Neither root badge is a blanket licence for the entire repository.** [Chatwoot licence](https://github.com/chatwoot/chatwoot/blob/develop/LICENSE), [enterprise licence](https://github.com/chatwoot/chatwoot/blob/develop/enterprise/LICENSE), [editions](https://www.chatwoot.com/pricing/self-hosted-plans), [Activepieces licence](https://github.com/activepieces/activepieces/blob/main/LICENSE)

[vendor] Mixpost's public repository is explicitly Lite, separate from Pro/Enterprise. Postiz's current documented dependencies include Temporal. FFmpeg's resulting licence depends on enabled components and external libraries; `--enable-nonfree` has a different redistribution consequence. These are implementation/deployment facts, not reasons to erase good code from the research funnel. [Mixpost](https://github.com/inovector/mixpost/blob/main/README.md), [Postiz requirements](https://docs.postiz.com/self-host/installation/system-requirements), [FFmpeg actual licence discussion](https://github.com/FFmpeg/FFmpeg/blob/master/LICENSE.md)

### Carry forward the original Foundry modules exactly in scope

[analysis] **Activepieces:** allowlisted draft, notification and report-sync pieces only; explicit approval before external publication or sends. Do not run a second full orchestration stack next to Postiz's Temporal merely because a workflow UI exists. **listmonk:** optional consent-bound newsletter sidecar with synchronized suppression/unsubscribe state; **not the CRM contact authority**. Where email lifecycle is not contracted, do not deploy it. [Original record](https://github.com/sisodias/great-library-of-siso/blob/main/research/industries/source/intelligence/agency/industries/marketing_social_media_agencies.json), [listmonk binary/PostgreSQL architecture](https://github.com/knadh/listmonk/blob/master/README.md)

## 3. The glue is the product work

[analysis] **Identity and authorization:** map `agency_id / brand_id / upstream_account_id / external_user_id`; never join on display name alone. Maintain separate service credentials and API scopes. Client reviewers access only their brand's portal and review object, never internal inbox administration or arbitrary scheduler accounts. CE apps do not magically gain cross-application SSO from a reverse proxy. Test every list, search, export, attachment and direct-ID endpoint for cross-brand leakage.

[analysis] **Version and event contract:** an approval binds canonical caption bytes, asset hashes, channel/account, scope and relevant schedule fields. A proposed envelope contains event ID, object ID/version, agency/brand, event type, actor/authority, occurrence time, payload hash, source reference and idempotency key. The release adapter checks approval and grant status again at dispatch. A queue admission response is not a live-post receipt. Reconcile an ambiguous timeout before retrying; “exactly once across social APIs” is not promised.

[analysis] **File handling:** quarantine uploads, enforce size/type limits, use per-brand storage paths and signed short-lived access, preserve originals, and create immutable derivatives. Media tools get no social tokens or general outbound network access. Parsing or transcoding untrusted files requires patching, sandboxing and resource limits. Metadata/C2PA assertions are evidence to inspect, **not proof that a claim is true or that a licence/model release exists**. A privacy-safe derivative may omit unnecessary personal metadata while the private provenance record is retained.

[analysis] **Schema mismatch:** each source reports different IDs, revisions, time zones, metrics, deletion semantics and pagination. API retries must not create duplicate comments, invoices or posts. Retain raw metric snapshots with retrieval time, account, period and definition; a rate-limited/missing value is not zero. Monetary records store currency and authoritative external ID. Suppression wins over a stale imported contact. Deletes/revocations propagate as explicit events with receipts.

[analysis] **Operational authority:** staff publishing directly through an unrestricted Postiz UI would bypass the spine; restrict publication credentials and interactive access accordingly. Manual emergency/native publication requires an accountable override record and later reconciliation. An LLM may propose copy or classify a request but cannot grant permissions, approve its own output, issue an invoice or release content. No LLM or GPU is required for the core; optional external AI needs client authorization, a cost cap and a data-handling decision.

[analysis] Application-level append-only events and hashes improve auditability; a privileged VPS/database administrator can still alter local state. This is **not** a tamper-proof legal notarization service. Client-owned off-machine backups, access logs and restoration tests provide an independent recovery trail; qualified timestamp/signature requirements would need separate design and review.

## 4. Deployment: phased, one client-owned VPS

```text
Client's existing email / authorized social APIs / native manual handoff
                    │ webhooks or explicit staff capture
                    ▼
┌────────────── ONE AGENCY-OWNED VPS ────────────────────────────┐
│ Caddy TLS ingress → EspoCRM core + agency entities / portal    │
│                         │                                     │
│             six-object spine + approval/release policy        │
│              │             │                 │                │
│ private uploads      approved outbox      metric snapshots     │
│ tusd/client          + reconciliation    + validation          │
│      │                    │                    │               │
│ ExifTool / imgproxy   OPTIONAL Postiz      WeasyPrint report     │
│ FFmpeg / c2patool     + its Temporal        rendering job       │
│ bounded workers      dependencies             │               │
│      │                    │                    │               │
│ client-owned volumes; separate app databases/roles and secrets │
│ OPTIONAL: Chatwoot | Kimai (+ MySQL/MariaDB) | listmonk          │
│           allowlisted Activepieces pieces, not another engine  │
│ restic backup/export + resource/queue/grant monitoring          │
└───────────────────────────────────────────────────────────────┘
       │ encrypted backup                     │ reviewed handoffs
       ▼                                      ▼
Client-owned off-machine storage        QuickBooks / Gusto / Stripe
(no SISO bucket)                        remain authoritative
```

[analysis] **Phase A — approval-only:** EspoCRM core/portal and narrow agency schema/policy; Caddy; one qualified database; private asset volumes; restricted upload/media/report jobs; restic backups. Existing email, scheduler, reporting and accounting remain. A **4 GiB / two-vCPU** VPS is a **load-test starting hypothesis**, not a validated floor. No Chatwoot, Postiz, general BI server, local LLM, full workflow engine or second database by default.

[analysis] **Phase B — delivery integration:** add only the component whose acceptance tests pass. Chatwoot adds inbox operations; Postiz brings its application and Temporal/database/queue dependencies; Kimai can add a different database engine. Keep app databases and users distinct even where a compatible PostgreSQL engine can be shared. The exact version intersection must be checked against each chosen stable release; default-branch research SHAs are **evidence pins, not production release recommendations**.

[analysis] **Phase C — optional adjacencies:** listmonk/newsletter, Shlink links, Umami owned-web metrics and Kimai time capture require explicit business demand. They are selectable modules, not a compulsory container zoo. Use upstream API/UI boundaries and existing jobs; do not rebuild a generic workflow engine or install a warehouse to render ten reports a month.

[analysis] For the fuller co-located assembly, treat **16 GiB as conditional on concurrency/load tests** and **32 GiB as a planning budget**, with no GPU and one heavy media job at a time initially. Budget disk separately: the referenced 32 GiB machines list only 100 GiB local SSD. Media retention and client-owned backup storage may dominate. Annual modeled costs including assumed maintenance are **$1,445.60 approval-only**, **$4,419.20 for the 32 GiB memory-oriented full case**, or **$5,628.80 with more CPU headroom**. These are estimates with explicit assumptions, not measured running costs. [Complete arithmetic/vendor sources](06-value.md)

[analysis] Deployment ownership: client-controlled VPS/cloud account, DNS/TLS domain, social application registrations, OAuth grants and encrypted backup account. Secrets stay outside git/logs/reports. Use pinned qualified image digests, least privilege, nonpublic database ports, tested upgrades and rollback. An optional observability UI on the same failed host cannot alert by itself; agree an independent client-owned monitor or provider alert. There is **no SISO-hosted control plane requirement**.

### Suggested smoke/acceptance receipts — all unexecuted

[analysis] Restore a clean client-owned VPS from encrypted backup; reconstruct one campaign with original/derivative/approval references; prove a different brand cannot list or fetch it; edit an approved caption and observe release blocked; revoke a grant and observe dispatch blocked; simulate timeout/replay and reconcile without duplicate publication; import a missing metric and retain unknown rather than zero; prove suppression survives contact resync; verify keyboard-only review and readable mobile approval; export all six objects and media manifests into documented portable files.

[analysis] Proposed operating targets: daily recoverable off-machine copy and a four-hour restoration objective, to be measured in rehearsal. Weekly provider snapshots alone do not establish that recovery point. No high availability is claimed on one box. The client must accept downtime/restore tradeoffs or change the deployment requirement.

## 5. Screens, not another UI-library hunt

[analysis] Required screens: Today/blocked work; unified request queue; brand/account/grant health; accepted scope/change orders; campaign calendar; asset/version review; client approval portal; publication exception queue; reconciled report/renewal; and capacity/invoice-status/offboarding. Reuse core product screens and the already-curated SISO component shelf only where a genuine gap remains. Client branding does not justify copying an enterprise-only feature without its rights. [Existing component bank](https://github.com/sisodias/siso-component-bank)

## 6. Honest gap register — twelve gaps

| ID | Missing or unproven capability | Response / admission gate [analysis unless source says otherwise] |
|---|---|---|
| G01 | Agency-specific exact-version, scope-bound approval-to-release contract | Narrow spine extension plus adversarial tests; no claim that a generic task checkbox provides it |
| G02 | Platform API availability, app review, quotas and permitted use | Obtain client-owned permissions and test each account/channel. TikTok Direct Post guidance excludes internal team-upload utilities; native/qualified provider handoff remains. [TikTok](https://developers.tiktok.com/docs/en/content-sharing-guidelines) |
| G03 | Universal inbox coverage, particularly personal WhatsApp/group history | Official APIs or explicit staff capture only. No session scraping/password-sharing workaround; measure retained handoff effort. [WhatsApp platform](https://www.whatsappbusiness.com/products/platform-pricing/) |
| G04 | Broad social-listening and proprietary historical/audience datasets | OSS dashboards do not create data rights; retain paid sources where contracted. [Brandwatch plans](https://www.brandwatch.com/plans/), [Meltwater](https://www.meltwater.com/en/pricing) |
| G05 | Complete authorized social-metric connector parity and causal measurement | Reconcile source-by-source; keep AgencyAnalytics if parity fails; do not turn correlation into campaign lift. [AgencyAnalytics capabilities](https://agencyanalytics.com/pricing) |
| G06 | Creative truth, asset rights, endorsements and accessibility judgment | Human QA and explicit evidence; C2PA is not a rights database. Add disclosure gates without pretending automated legal compliance. [FTC disclosures](https://www.ftc.gov/business-guidance/resources/disclosures-101-social-media-influencers) |
| G07 | US accounting, payroll/tax filings and payment execution | Retain specialist authorities and accountable humans; no OSS invoice UI is admitted as statutory payroll replacement. [QuickBooks](https://quickbooks.intuit.com/pricing/), [Gusto](https://gusto.com/product/pricing), [Stripe](https://stripe.com/pricing) |
| G08 | Free cross-app enterprise SSO, fine-grained roles and white-label parity | Quote licensed editions or narrow access; test portal policy. No MIT-root shortcut into enterprise code. [Chatwoot editions](https://www.chatwoot.com/pricing/self-hosted-plans) |
| G09 | Independently evidenced adoption, maintainability, security and production fit | Bank dependence absent for many apps; sampled activity is not an audit. Qualified release/SBOM/backup/load tests remain unexecuted |
| G10 | Reliable migration and complete historic approvals/media provenance | Sample-reconstruct imports, preserve source evidence, budget overlap and rollback; treat undocumented approvals as unresolved |
| G11 | Fleet operations, resource floor, recovery and bounded support cost | Per-client ownership remains mandatory; measure maintenance, storage growth, restoration and update failure before scaling |
| G12 | Validated operator demand, time returned and viable willingness-to-pay | Interview/pilot required; synthetic operator, labor model and eligible-segment size remain explicitly unmeasured |

[vendor] Commercial email rules and a consent-bound product policy are not identical. CAN-SPAM's published duties include opt-out handling and apply to commercial messages; do not falsely state that every US B2B commercial email legally requires prior opt-in. The proposed listmonk integration deliberately uses a stricter consent/suppression gate. [FTC business guide](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business)

[analysis] **Build versus lift:** retain upstream applications, libraries, parsers and operations tools. Own only the agency schema, authority transitions, mapping adapters, policy tests and accepted deployment contract. The requested roughly-5% custom share is a direction, **not a measured estimate of code or labor**. If the design requires rewriting an adoptable CRM, scheduler, media engine or report renderer, narrow it instead. An accepted building set still requires interaction, rights, accessibility and removal tests; this research is candidate evidence, not execution proof. [GQ-004](https://github.com/sisodias/great-library-of-siso/blob/main/registry/works/frontier-question-gq-004.json), [GQ-013](https://github.com/sisodias/great-library-of-siso/blob/main/registry/works/frontier-question-gq-013.json)
