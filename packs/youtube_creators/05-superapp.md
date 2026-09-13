# 05 — Assemble the creator operating system

Research date: **2026-09-13 UTC**. This is a blueprint, not deployed software. **[vendor]** statements describe upstream capabilities at the pinned revisions in [04-oss-candidates.json](04-oss-candidates.json); **[analysis]** statements are our selection, proposed architecture or unmeasured engineering assumptions. Every ADOPT verdict means a component selected for a bounded integration test, not a successful install, licence clearance or production acceptance. Machine-readable counterpart: [05-assembly.json](05-assembly.json).

## Decision: enter through a versioned editor handoff

**[analysis]** Build the link between an accepted brief, approved script, source/rights package, editor revisions and approved release. Do not start by rebuilding an editor, producing the largest pile of AI clips, or replacing the client's accounting package. The repeated pain mechanism is disconnected production context and expensive review/rework, illustrated by the ten attributed records in [01-person.md](01-person.md). That motivates a comparative pilot; it does not prove demand or savings for the named client.

### Preserve the existing SUMERA asset

**[analysis, supplied-brief provenance]** The assignment establishes SUMERA as a shipped script-generation product with an existing monetisation/growth shell, not a prototype. Its covered scope is script generation/editor handoff inputs plus existing authentication, billing, affiliate/referral, course/community and administrative capabilities. It is **not** established as a full media editor, thumbnail/experiment system, multi-platform publishing system, owner-analytics ingester or sponsor-management operating system. This public document deliberately does not reproduce private code, table layouts or operational details. [Source identity, access-controlled](https://github.com/tristangrech/sumera); [public pack scope](https://github.com/sisodias/siso-industry-packs/tree/main/packs/youtube_creators).

Cross-link the existing base-stack learning to [saas_base_stack](../saas_base_stack/), but do not move another project's ownership or assume private code may be relicensed into this public pack. The first pilot can consume an **approved script export** without modifying SUMERA. A later strict-self-hosted port needs authorised reuse, replacement of non-local dependencies, entitlement migration and a fidelity test. This research has not completed that port. An exported script is an integration input, not a claim that the existing SaaS now runs on the client VPS.

## The spine: six object families, one authority per fact

| Object [analysis] | Minimum persistent content | Authority and invariants |
|---|---|---|
| **WorkOrder** | Accepted deliverable, conversation/reference, owner, destination, due date, confirmed requirements and Deal link | A human confirms that a conversation became work. Draft classification cannot authorise a purchase, external send or publication. |
| **Production** | Channel/series, brief, script-version reference, parent/derivative relation and handoff manifest | Kitsu/Zou retains production tasks/review state. Our cross-system ID maps to it rather than maintaining an independently editable second task queue. |
| **AssetVersion** | Content hash, storage pointer, MIME/technical metadata, original and derived lineage, source time range, rational frame/time base and provenance | Bytes are immutable after identification. A new render or corrected caption is a new version. Original media/project files are retained according to the client's policy. |
| **RightsGrant** | Grant/consent document hash, licensor, covered asset/version, client/channel/territory/term and publication conditions | A document is evidence to review, not an automated legal verdict. File possession, a fingerprint or an AI provenance label is not permission. |
| **Release** | Exact render/title/thumbnail/caption versions, approving person/time, account, schedule, upload attempt/receipt, platform state and observation provenance | Approval binds exact bytes and scope. An upload job finishing is not evidence of public visibility. A revised asset invalidates the earlier release approval. |
| **Deal** | Sponsor/affiliate/course offer reference, contractual deliverables, Release links, invoice/payment-provider IDs and reconciliation exceptions | The existing contract/accounting/payment system stays authoritative for settlement, refunds, tax and entitlement. Store references, not raw card details or a competing ledger. |

**[analysis]** The differentiated work is these joins and authority transitions. The claim that only roughly 5% must be written is a design ambition from the brief, **not a measured estimate**. Media timebases, identity, permissions and exception handling can dominate the effort even when nearly every visible feature is lifted.

## Component map and why each choice wins this bounded route

All candidate identities, observed stars/dates, commits, actual licence-file references, alternative verdicts and source-reviewed rationales appear in [04-oss-candidates.md](04-oss-candidates.md). This table is **[analysis]** based on those **[vendor/upstream]** sources, not a runtime comparison benchmark.

| Workflow | Chosen component / verdict | What is ours | Why this instead of the named runners-up |
|---|---|---|---|
| S01 Intake | **chatwoot/chatwoot — ADOPT, optional** | Message-to-WorkOrder confirmation and identity mapping | Whole conversation application beats inventing an inbox. FreeScout is attractive for email-only work; Zammad is broader than demonstrated demand. Keep native email/manual import until real channel volume justifies another service. [Source](https://github.com/chatwoot/chatwoot). |
| S02 Research | **miniflux/v2 — ADOPT, optional** | Source-to-Production references and approved evidence inventory | A narrow feed inbox/OPML/API route is enough initially; FreshRSS is a real alternative. SearXNG adds external search dependencies, and archived pytrends is not a dependable trend-data foundation. None supplies proprietary demand prediction. [Source](https://github.com/miniflux/v2). |
| S03 Script | **Existing SUMERA — preserve** | Approved export/version identifier, not a second script authority | Do not replace a shipped script capability with Fountain samples or a general LLM front end. A local-model route remains an explicit private implementation/quality decision. [Private source identity](https://github.com/tristangrech/sumera). |
| S04 Transcript | **ggml-org/whisper.cpp — ADOPT** | Model/version pin, queued job, language/accuracy review and immutable output | CPU-oriented native route is a plausible small-box starting point. faster-whisper is a strong alternative to benchmark; WhisperX adds alignment/diarisation models and cost not yet required for the original narrated segment. [Source](https://github.com/ggml-org/whisper.cpp). |
| S04 Narration | **remsky/Kokoro-FastAPI — ADOPT, optional** | Approved voice/weight identity, pronunciation guide, listening gate | The wrapper offers a local CPU-serving path. Piper's maintained successor and Chatterbox are genuine alternatives; MLX is Apple-specific and edge-tts is a remote service, not local TTS. No paid-voice savings until the exact voice/quality comparison passes. [Source](https://github.com/remsky/Kokoro-FastAPI). |
| S05 Asset store | **seaweedfs/seaweedfs + rclone/rclone — ADOPT** | AssetVersion/RightsGrant manifest and client retention/restore policy | A single-binary S3 surface plus portable transfers avoids a distributed cluster. MinIO's current source is archived and declares no maintenance. Nextcloud is a whole file platform, appropriate only if it is already the client's chosen file authority. [SeaweedFS](https://github.com/seaweedfs/seaweedfs), [rclone](https://github.com/rclone/rclone), [MinIO notice](https://github.com/minio/minio). |
| S06 Media operations | **FFmpeg/FFmpeg — ADOPT** | Bounded, sandboxed jobs, expected output contract and checks | Use ffprobe/ffmpeg for probes, proxies, transforms and render checks before introducing MoviePy array transfers or PyAV packet handling. MLT/libopenshot are options when their richer edit graphs are actually needed. Pin codec/build obligations. [Source](https://github.com/FFmpeg/FFmpeg). |
| S06 Editorial interchange | **AcademySoftwareFoundation/OpenTimelineIO — ADOPT** | Mapping to Production/AssetVersion and a tested adapter contract | Lift editorial interchange instead of inventing another timeline JSON format. Preserve original native projects: OTIO does not guarantee every plugin, effect, font or NLE round trip. Browser editors OpenCut, FreeCut and Kimu remain STUDY until their exact export/recovery path passes. [Source](https://github.com/AcademySoftwareFoundation/OpenTimelineIO). |
| S07 Packaging | **lovell/sharp + tkarabela/pysubs2 — ADOPT** | Version binding, permitted image templates and caption review | Sharp fits the existing TypeScript seam; ImageMagick is broader than required. pysubs2 handles multiple timed-text formats, unlike an SRT-only parser. Preserve originals because conversion can lose unsupported format semantics. Canva-quality design and native A/B testing are not replaced by image transforms. [sharp](https://github.com/lovell/sharp), [pysubs2](https://github.com/tkarabela/pysubs2). |
| S08 Production/review | **cgwire/kitsu + cgwire/zou — ADOPT** | Terminology adapter, cross-app IDs, handoff manifest and exact-release approval binding | A real production tracker with tasks, preview versions and an API beats recreating review/comments. MediaCMS is a strong media portal, but portal hosting alone is not production-task/revision authority. These two repositories are one application stack, not two independent feature suites. [Kitsu](https://github.com/cgwire/kitsu), [Zou](https://github.com/cgwire/zou). |
| S09 Publish | **googleapis/google-api-nodejs-client — ADOPT; native/manual fallback** | Account-specific permissions, approval, retry/idempotency and publication reconciliation | Official client aligns with the existing TypeScript code. porjo/youtubeuploader is a useful Go binary; Postiz/Mixpost add another application and do not remove platform onboarding restrictions. Direct Post is not promised for an ineligible private TikTok utility. [SDK](https://github.com/googleapis/google-api-nodejs-client), [YouTube](https://developers.google.com/youtube/v3/docs/videos/insert), [TikTok guidelines](https://developers.tiktok.com/doc/content-sharing-guidelines/). |
| S10 Derivatives | **Breakthrough/PySceneDetect — ADOPT, optional**; reuse transcript/media stack | Bounded candidate list, source handles, relevance/context review | Scene detection is honest, narrow automation. auto-editor/FunClip/autoclip are valuable alternatives to test. None has demonstrated that more generated clips means more accepted, useful clips for this operator. [Source](https://github.com/Breakthrough/PySceneDetect). |
| S11 Analytics/community | **Reuse official Node client; native Studio; optional inbox** | Provenance-bearing observation import, exceptions and decisions | Metabase/Superset cannot create owner-only platform metrics; Umami measures a different website surface. Keep official eligibility and native tests rather than inventing third-party private retention data. [Metrics](https://developers.google.com/youtube/analytics/metrics), [native tests](https://support.google.com/youtube/answer/16391400). |
| S12 Commercial work | **Preserve existing shell/accounting; reference adapters only** | Deal-to-Release joins and evidence-backed invoice/claim packets | Invoice Ninja, InvoicePlane, Frappe CRM/ERPNext are studied alternatives, not mandatory extra databases. Ghost/LMS/Moodle duplicate scope already supplied by the brief. Accounting and payment authority are not reimplemented here. [Existing scope](../saas_base_stack/), [payment events](https://docs.stripe.com/webhooks). |

## The glue: explicit work, not magic integrations

**[analysis] Identity and permissions.** Maintain a stable mapping among the client account, script owner, Kitsu user, external reviewer and platform channel. Do not assume every community edition offers the required SSO feature. Separate service credentials, least-privilege roles and read-only reviewers. Rights to a private codebase, an open repository licence and authority to publish to a channel are three different questions.

**[analysis] Files and time.** Hash originals and derivatives, retain source filenames and storage identifiers, record rational frame rates, and distinguish source-relative from clip-relative time. Review proxies must map to the accepted original. Relinking, missing fonts/plugins, variable frame rate and unsupported transitions are test cases. Asset downloaders may consume only owned or explicitly authorised input; they do not confer reuse rights.

**[analysis] Jobs and events.** Use one bounded local job mechanism, with idempotency keys, timeouts, progress, retry limits, cancellation and a dead-letter/exception view. A notification outbox must expose delivery state. Queue success, upload success, scheduled state and verified public state are separately recorded. Repeated webhooks cannot issue repeated grants, charges or posts. No worker may interpret a comment as release authority.

**[analysis] Network and security.** Allowlist platform/provider destinations; reject arbitrary server-side fetch URLs and private-network targets. Constrain media parsing/FFmpeg subprocesses with explicit arguments, CPU/memory/time limits and limited filesystem access. Keep secrets out of source, logs and media manifests. Encrypt client backups and test restore; a storage sync can copy deletions and is not itself a recovery plan.

**[analysis] Generic infrastructure is not the vertical discovery.** Reuse the existing bank for identity, validation, database access, queues, mail and UI rather than inflating the sweep with another hundred generic packages. Bank picks are research leads, not a waiver of current security/rights checks. [Repo bank](https://github.com/sisodias/siso-repo-bank), [component bank](https://github.com/sisodias/siso-component-bank). No UI component-library research is proposed. Needed screens: intake/order confirmation, production board, brief/script link, asset/rights inventory, versioned review player, release checklist/calendar, observations, deal/invoice exceptions and backup/job health.

## Deployment: one box per client, never SISO servers

**[analysis] Proposed baseline envelope:** one client-owned Linux VPS, **16 GiB RAM as a test allocation**, adequate persistent media capacity, and one heavy CPU media/transcription job at a time. This is not a measured minimum. Place the web/review surface and Zou API behind TLS; use a local Postgres instance with distinct service databases/roles; local object storage; bounded worker processes; local log/health records. Do not add Kubernetes, a distributed object cluster or a dedicated BI service to the pilot. Optional inbox/feed/TTS services are admitted only after measuring remaining memory and operational burden.

**[vendor]** whisper.cpp publishes memory guidance for specific models; that is model-runtime evidence, not the memory requirement of the entire stack. MediaCMS publishes its own separate resource guidance; that does not prove Kitsu's capacity. CPU throughput must be measured with the actual duration, resolution, captions and model. [whisper.cpp source](https://github.com/ggml-org/whisper.cpp), [MediaCMS source](https://github.com/mediacms-io/mediacms).

**[analysis] Resource acceptance:** import one representative project; run transcription, proxy and final render serially; measure peak resident memory, disk peaks, runtime and concurrent reviewer responsiveness. Repeat with a failed/oversize input. Verify recovery after an interrupted job and restore database plus media manifest to an empty client-controlled target. Backups must include actual bytes or a documented recoverable source, not only SQL rows. Until these pass, do not quote a smaller VPS as proven sufficient.

**[analysis] Cost illustration:** a publicly priced 16-GiB DigitalOcean allocation at $96/month plus weekly backups at 20% gives **$115.20/month or $1,382.40/year**, before tax, domain, independent backup storage, excess transfer and support. This is a reproducible planning comparator, not a selected supplier or a quote for Tristan's location. [Droplet sizes](https://www.digitalocean.com/products/droplets), [backup pricing](https://www.digitalocean.com/pricing/droplets). The full economics, including care and migration, are in [06-value.md](06-value.md).

**External boundaries:** destination platforms, payment processors, licensed media and any elected cloud voice service remain external providers. Desktop NLE work remains on the editor's own machine; it is not falsely counted as a VPS-hosted browser editor. No SISO execution server is introduced. A strict requirement that *all* authoring and model execution also occur inside the VPS remains an unproven variant: browser/server editing fidelity and local script/voice quality must pass before claiming it.

## Architecture sketch

```text
Authorised messages / approved script export / owned media
                         |
                  human-confirmed WorkOrder
                         |
         client VPS: production shell + Kitsu / Zou
             |              |                 |
       six-object links   local Postgres    reviewer proxy
             |              |                 |
             +------ AssetVersion / RightsGrant --------+
                            |
              local object store + bounded CPU worker
                 ffprobe/FFmpeg; whisper.cpp;
                 OTIO; captions; optional local TTS
                            |
                exact-version release approval
                            |
              authorised official adapter OR export
                            |
                 client-owned platform account
                            |
                reconciled receipt / observations

Deal references existing accounting/payment authority.
Encrypted, tested backups remain controlled by the client.
```

Libraries are linked or invoked inside the relevant worker; they are not each deployed as their own service. Kitsu/Zou is one application pair. Optional services are not assumed present in the minimum deployment. Original sources, client credentials and private script code never enter the public research pack.

## Ten explicit gaps

**[analysis] G01 — Actual operator fit and private-asset reuse:** no observed weekly workflow or grant to republish private implementation. **G02 — Narration/script quality and consent:** code availability does not establish acceptable local output or rights to every voice/weight. **G03 — Stock/music and claims:** no OSS component grants premium catalogue rights or adjudicates copyright. **G04 — NLE fidelity:** no tested complete native-project/effect/font round trip. **G05 — Platform access:** OAuth, API project review and TikTok's private-utility restriction survive self-hosting. **G06 — Experiments and private analytics:** native eligibility and owner authority cannot be replicated from public counts. **G07 — Money and statutory records:** payment settlement, tax/payroll and accountant acceptance remain outside this assembly. **G08 — Single-box operations:** resource, security, upgrade and restore tests are unexecuted. **G09 — Licence/edition boundaries:** model weights, enterprise paths and selected build options require a route-specific review even when a root licence was read. **G10 — Evidence/economics closure:** actual invoices, eligible market population and two consecutive dry discovery rounds remain missing.

These are findings, not invented repositories to fill blanks. A populated architecture is not yet an admissible deployment.

## Build sequence and stop conditions

**[analysis] First:** run the existing-production handoff fixture from Stage 2 with existing script/editor tools unchanged. **Next:** integrate only Kitsu/Zou, immutable asset references and the required media/metadata libraries. **Then:** test one manual/native release followed by one authorised API release where eligible. Admit inbox, feeds, local voice or automatic derivative suggestions only against an observed bottleneck.

Stop if the reviewer cannot reliably identify the approved version, rights evidence is lost, a channel action lacks approval, a caption/timebase changes meaning, or total reviewed human effort is not lower. This contributes an evidence-backed component/assembly hypothesis to **GQ-004 (Best Software Primitive)** and **GQ-013 (Useful Reusable Building Set)**; it does not register a new public Work, publish a Library Release or claim that consumers installed this assembly. [Public Library registry](https://github.com/sisodias/great-library-of-siso/tree/main/registry).
