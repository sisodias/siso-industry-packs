# Super-app blueprint — a local project and release binder

**As of 2026-09-13. Research design, not application code or an authorised build.** The working title describes a proposed coordination layer around the existing DAW. The value verdict remains **NO broad build now**; validate one real handoff against existing tools first. [analysis; scope: https://github.com/sisodias/siso-industry-packs/blob/main/packs/music_creation/README.md]

**Eight ADOPT decisions are conditional component selections**, not installation, performance, security, redistribution or customer-acceptance claims. Every selected repository has retrieved source metadata, an exact commit, a README and an actual licence file. Their revisions, source URLs and scores are recorded in `04-oss-candidates.json` and the source audit at commit `6913ada47d9517ca254627cdaef12aed40ed342e`. No candidate code or model was executed. [analysis; evidence: https://github.com/sisodias/siso-industry-packs/blob/6913ada47d9517ca254627cdaef12aed40ed342e/packs/music_creation/evidence/candidate-audit-receipt.json]

## 1. The spine: six object families, not six competing databases

The schema below is proposed. Preserve the distinctions already established in [02-workflow.md](02-workflow.md); implement none until the actual task warrants it. [analysis]

| Object | Minimal persistent contract | What must never be inferred |
|---|---|---|
| **Work** | Stable internal ID; title; typed composition and recording references; brief; responsible person; state and history. | A musical composition, a recording and a release are not interchangeable identities. A file name is not an ISRC or proof of ownership. |
| **AssetRevision** | Content hash; original path; size/type; parent revision; work reference; dependency manifest; source receipt; transform/model/settings; technical observations. | Hash equality does not prove that a DAW project has every external dependency, will render identically or may legally be distributed. |
| **PartyThread** | Person/organisation ID; explicit channel/consent reference; selected message evidence; commitments; review links. | No inferred identity match, unapproved inbox access or automatic external reply. Store only the private content needed for the task. |
| **RightsAgreement** | Document/source reference; parties; relevant work/recording; composition or master share scheme; proposed/approved/disputed/unknown state; named approvals. | An AI result cannot assign shares or convert a missing receipt into permission. Composition and master shares must not be summed together. |
| **Release** | Package ID; selected asset revisions; metadata version; destinations; approved/submitted/accepted/available states; external acknowledgement and correction history. | A valid local package is not an accepted distribution submission or a live release. |
| **LedgerEntry** | Original statement/document hash; source row; external identifier; period; currency; exact amount; deductions; payment reference; reconciliation decision. | Estimated earnings are not settled payments; different currencies and reporting periods must not be combined silently. |

The local database is an index and relationship store; original audio, native projects, statements and agreement evidence remain ordinary files with a manifest. Export plain JSON/CSV plus those permitted files. No second hidden catalogue becomes the only source of truth. [analysis]

## 2. Lift the product base before designing another one

The search found whole applications, not only libraries. **Stack Desktop** describes an offline sample manager using Tauri/Rust/SQLite; **Saempl** offers sample clustering; **SlunderStudio** describes a local AI workstation. These are immediate comparison candidates. Stack's inspected installation guidance does not establish a signed/notarised package, so no security bypass was performed or recommended. SlunderStudio's advertised model collection is not a benchmark or a blanket model licence. [vendor] https://github.com/swendlcode/stack-desktop ; https://github.com/jonasblome/Saempl ; https://github.com/SysAdminDoc/SlunderStudio [analysis]

**LazyCreatives Backups** is close to the project-backup wedge but its source licence is explicitly evaluation-only, not open source. **Nash Royalty Engine** is a client-side statement-parser candidate with PolyForm Noncommercial terms. Record their mechanisms and compare behaviour; do not call their public visibility permission to copy or commercially redistribute them. **Django Music Publisher** supplies a genuine publisher back-office model, but that is broader than NM's known needs. [vendor] https://github.com/LazyCreatives/lazycreatives-backups ; https://github.com/DefaultMo/nash-royalty-engine ; https://github.com/matijakolaric-com/django-music-publisher [analysis]

Commercial **Saltado** is an especially important no-build comparator: free local cataloguing and a low-cost Pro option already exist. Its preview route uses available bounces rather than rendering arbitrary native projects and plug-ins. A catalogue-only clone is therefore not a demonstrated wedge. [vendor] https://www.saltadosessions.com/ ; https://saltadosessions.com/preview-projects-without-opening-daw [analysis]

The first product-base decision is consequently **STUDY/compare, then lift a suitable existing application if it passes**. The eight components below are a conditional assembly recipe, not an excuse to start a greenfield workstation before that comparison. A claimed “95% reused / 5% ours” ratio would be unmeasured here; the intended custom surface is identities, relationships, approval states, manifests and narrowly scoped adapters. [analysis]

## 3. Component map and named runners-up

All repository capability descriptions derive from their inspected upstream READMEs; selection and comparisons are `[analysis]`. ADOPT denotes the preferred bounded mechanism, not a tested product. [analysis]

| Stage | Preferred mechanism / verdict | What would be ours | Why this route rather than its runners-up |
|---|---|---|---|
| **W01 Intake** | User-selected message/file import; **STUDY** existing inbox patterns. | Draft-to-accepted commitment state, person/work links and explicit send approval. | `chatwoot/chatwoot` is already banked but a support-centre server and channel permissions are excessive for this single laptop. `jstedfast/MimeKit` is an option only if a .NET import route is actually chosen. Sources: https://github.com/chatwoot/chatwoot ; https://github.com/jstedfast/MimeKit |
| **W02 Samples** | **ADOPT** `quodlibet/mutagen`; **STUDY** Stack/Saempl as whole catalogue bases. | Asset identity, receipt/provenance link and selected-work association. | Mutagen fits the proposed Python utility layer; `Borewit/music-metadata` is the runner-up for a JavaScript-only design. Avoid maintaining two competing tag authorities. Sources: https://github.com/quodlibet/mutagen ; https://github.com/Borewit/music-metadata ; https://github.com/swendlcode/stack-desktop ; https://github.com/jonasblome/Saempl |
| **W03 Creation / supported interchange** | Keep the existing DAW. **ADOPT** `roex-audio/dawproject-py` only for a supported DAWproject path. | Bind imported project references to Work/AssetRevision; retain unknown fields and original files. | `bitwig/dawproject` is the governing format reference; `git-moss/ProjectConverter` and `DawVert/DawVert` are conversion runners-up. `demberto/PyFLP` is read-only research until version fixtures demonstrate safety. No claim that any parser reproduces every plug-in or proprietary project. Sources: https://github.com/roex-audio/dawproject-py ; https://github.com/bitwig/dawproject ; https://github.com/git-moss/ProjectConverter ; https://github.com/DawVert/DawVert ; https://github.com/demberto/PyFLP |
| **W04 Checkpoint / backup** | **ADOPT** `restic/restic` with a local user-approved target. | Quiescent-project manifest, source/receipt linkage, backup receipt and a separate restore-test record. | `syncthing/syncthing` synchronises devices rather than proving recovery. `borgbackup/borg` is a capable alternative but its development branch explicitly needs stability qualification. Do not copy restricted LazyCreatives code. Sources: https://github.com/restic/restic ; https://github.com/syncthing/syncthing ; https://github.com/borgbackup/borg ; https://github.com/LazyCreatives/lazycreatives-backups |
| **W05 Review / splits** | Local revision-specific comments and agreement evidence; **STUDY** publisher schemas. | Separate human approvals for the heard revision, composition agreement and master agreement. | `jamulussoftware/jamulus`, `jacktrip/jacktrip` and `sonosaurus/sonobus` solve network-audio sessions, not offline project merging or signed shares. Source comparisons: https://github.com/matijakolaric-com/django-music-publisher ; https://github.com/jamulussoftware/jamulus ; https://github.com/jacktrip/jacktrip ; https://github.com/sonosaurus/sonobus |
| **W06 Optional AI** | **ADOPT** `nomadkaraoke/python-audio-separator` and `spotify/basic-pitch` as separately invoked local jobs. | Job approval, input/output hashes, weight and parameter manifest, cancellation and human quality review. | `Anjok07/ultimatevocalremovergui` is the whole-app no-build alternative. `ssmall256/demucs-mlx` is device-specific; `deezer/spleeter` and `magenta/mt3` are comparison baselines. Training/generation stacks are not base dependencies. Sources: https://github.com/nomadkaraoke/python-audio-separator ; https://github.com/spotify/basic-pitch ; https://github.com/Anjok07/ultimatevocalremovergui ; https://github.com/ssmall256/demucs-mlx ; https://github.com/deezer/spleeter ; https://github.com/magenta/mt3 |
| **W07 Technical QC / export** | **ADOPT** `FFmpeg/FFmpeg` and `slhck/ffmpeg-normalize`. | Per-deliverable recipe, safe output location, acceptance record and comparison to the source. | `csteinmetz1/pyloudnorm` / `jiixyj/libebur128` are focused measurement alternatives; `spotify/pedalboard` is useful when actual effects/plug-in hosting is required. Do not rewrite DSP or silently “master” everything to one target. Sources: https://github.com/FFmpeg/FFmpeg ; https://github.com/slhck/ffmpeg-normalize ; https://github.com/csteinmetz1/pyloudnorm ; https://github.com/jiixyj/libebur128 ; https://github.com/spotify/pedalboard |
| **W08 Release package** | Reuse metadata/probe tools; **STUDY** BWF and DDEX/CWR-oriented sources. | Required-field checklist, asset selection, agreement gates and destination-specific export mapping. | `MediaArea/BWFMetaEdit` is a relevant inspection alternative; a MusicBrainz tagger does not verify unreleased rights. DDEX RIN is prior art for recording metadata, not an automatic distributor API. Sources: https://github.com/MediaArea/BWFMetaEdit ; https://github.com/metabrainz/picard ; https://ddex.net/standards/recording-information-notification/ |
| **W09 Statements** | **ADOPT** optional `duckdb/duckdb` analysis; **STUDY** Nash and Django Music Publisher for domain mapping. | Source-preserving column mappings, decimal/currency checks, duplicate detection and reconciliation approvals. | Nash already offers a domain parser; do not claim a blank field or rewrite its capability without evaluating rights and quality. DuckDB is the local analysis substrate, not a ready-made royalty contract interpreter. Sources: https://github.com/duckdb/duckdb ; https://github.com/DefaultMo/nash-royalty-engine ; https://github.com/matijakolaric-com/django-music-publisher |
| **W10 Fan / commerce** | Local drafts and external-system references; **STUDY** existing newsletter/storefront products, no new public service. | Consent/reference record, approval state and export to a separately authorised service. | `knadh/listmonk` requires database/SMTP/deliverability operations; `robsassack/merch-table` is a multi-service public commerce stack. A sleeping laptop cannot be assumed to receive payment webhooks or provide an always-available storefront. Sources: https://github.com/knadh/listmonk ; https://github.com/robsassack/merch-table |

## 4. The glue is the main unknown cost

**File identity and safe processing.** Never write into the open DAW project. Import a user-selected snapshot or wait for an explicit quiescent checkpoint; stage every transform under a separate output path. Resolve relative references, symlinks, case sensitivity and removable-drive paths. Preserve originals and unknown fields. Hashes identify bytes, not the successful reproduction of a musical performance. [analysis]

**Untrusted archives and parsers.** Treat projects, XML, MIDI, tags and media as untrusted input. Bound expanded archive size and path traversal; disable external XML entities; constrain parser/process resources; reject unexpected executable content; avoid loading third-party plug-ins in the binder process. These are proposed acceptance requirements, not completed security tests. [analysis]

**One job queue, no audio-thread surprise.** Use a local persistent job journal, explicit concurrency limits and an immutable recipe. Job identity includes input hash, executable/model version, parameters and output specification. Cancellation leaves an incomplete result, not an approved asset. Pause expensive work during creative sessions. A successful process exit does not imply perceptual quality or permission to release. [analysis]

**Agreements and money.** Keep writer/performer/producer roles, composition shares, master shares and payment allocations separate. Preserve the source statement before normalisation, use exact decimal amounts, retain original currency and period, and reconcile totals with exceptions. Never infer a missing party or share to make a table sum neatly. [analysis]

**External auth.** Base operation needs no SISO account. Use operating-system permissions for local files; any future provider credentials belong in the user's secure credential store, not the repo, logs or exported package. External sends, uploads and account/payment changes remain explicit user actions. Initial message/statement import avoids pretending every platform grants a suitable public API. [analysis]

**Exit and recovery.** Plain files plus versioned JSON/CSV exports must reconstruct the binder without the application. Test a restore to a different authorised directory, and test uninstall without deleting original media. Retain the local recovery key separately from the encrypted backup; no key is published or transferred to SISO. [analysis]

## 5. Deployment and resource envelope

```
USER'S LAPTOP — no SISO-hosted product service

Existing DAW / ordinary files / selected messages / statements
                         |
                  explicit safe import
                         v
  Chosen local product base or minimal binder surface
     |  SQLite relationships + append-only local event journal
     |  Original files / immutable manifests / staged outputs
     |
     +-- local metadata and DAWproject adapters
     +-- bounded FFmpeg/QC jobs
     +-- optional separation / transcription jobs (off by default)
     +-- optional in-process statement analysis
     +-- restic --> user's approved local backup device

External counterparts: collaborator, distributor, rights organisation,
storefront, messaging platform, payment processor.
Export/send only with approval; acknowledgements are imported evidence.
```

This is a data-flow sketch, not deployed software. No inbound public listener, permanent server, Docker requirement, cloud model API, hosted database or SISO telemetry is part of the base proposal. A local UI may use a desktop shell or loopback-only interface; choose after the product-base comparison and device inventory. [analysis]

**Core floor:** no GPU is intended for cataloguing, hashes and records. A numeric minimum RAM/CPU/storage figure is **unmeasured**. Actual libraries, audio files, export sets and backup retention determine the installation envelope. **Optional AI floor:** qualify per model/runtime. AudioLDM2 documents about 20 GB RAM for one MPS route; ACE-Step describes an 8 GB VRAM reduced-memory setting; neither establishes that an arbitrary laptop can run the intended workload. These generation candidates are excluded from the base assembly. [vendor] https://github.com/haoheliu/AudioLDM2 ; https://github.com/ace-step/ACE-Step [analysis]

Downloads are separate from offline execution. A model manifest must record the upstream source, exact version/hash, code licence, weight licence, permitted route and storage requirement before a user-approved download. No private recording is uploaded to qualify a model. Local caching alone does not resolve model/output rights. [analysis]

**Single deployment cost:** no SISO server rental is introduced by design, but complete installed cost is **null/unmeasured** until device inventory, build packaging, migration, storage, restore validation and support are priced. [06-value.md](06-value.md) gives the full cost equation and a clearly synthetic audio-storage calculation. No zero-cost deployment claim is made. [analysis]

## 6. Eight explicit gaps

| Gap | What is missing / who retains authority [analysis] |
|---|---|
| **G01 Actual operator baseline** | NM's precise task, device, existing tools, channels and spending are unknown. No code can substitute for the missing specification. |
| **G02 Native project fidelity** | No audited adapter proves lossless rendering across arbitrary DAWs, plug-ins, licensed packs and hardware. Preserve native files and rendered handoffs. |
| **G03 Sample clearance** | Tags, similarity, separation and provenance receipts do not settle sample-clearance or downstream-use disputes. Rights-holders and qualified reviewers remain necessary. |
| **G04 Contributor agreement** | Proposed composition/master shares are not approved contracts. Named parties must resolve disputes and authorise the relevant scheme. |
| **G05 Release/registration acceptance** | Distributor and rights-organisation interfaces, account eligibility, standards licences and acknowledgements are external. A locally valid export is not acceptance. |
| **G06 AI route qualification** | Code, model weights, input permission, output provenance and destination policy differ. Optional generation/separation is not a universal publication licence. |
| **G07 Device and packaging proof** | No NM installation, memory/latency benchmark, signed-package audit, restore test or adversarial parser test was performed. |
| **G08 Network and economic value** | Fan reach, payment settlement, reliable public availability and measurable consumer support economics cannot be supplied by a private laptop catalogue alone. |

These are scoped findings, **not claims that no open-source tool exists anywhere**. In particular, the sweep found royalty and project-management candidates; their correctness and authority are what remain unproven. Spotify documents delivery through distributors, and Bandcamp's current policy is a concrete example of a destination rejecting wholly or substantially AI-generated music. [vendor] https://artists.spotify.com/get-started ; https://blog.bandcamp.com/2026/01/13/keeping-bandcamp-human/comment-page-2/ [analysis]

## 7. Screens and cross-industry reuse

Screens needed if the narrow comparison passes: selected-message/brief inbox; work/project catalogue; asset/provenance/revision view; sample auditioning; exact-revision review and agreements; local-job/QC queue; release-package checklist; and statement/fan follow-up records. Reuse the existing component bank rather than researching another UI framework. Its component index is a discovery aid, not a blanket licence for every author's component. [analysis; source: https://github.com/sisodias/siso-component-bank/blob/main/README.md]

The adjacent course-creator record contributes version/approval/support boundaries; the marketing-agency record contributes consent, draft and final-publication separation. Neither justifies deploying all of its services onto this laptop. Shared search/storage/email primitives already appear in the repository bank, whose capability shelf was inspected before this vertical sweep. [analysis; sources: https://github.com/sisodias/great-library-of-siso/blob/main/research/industries/source/intelligence/agency/industries/course_creators.json ; https://github.com/sisodias/great-library-of-siso/blob/main/research/industries/source/intelligence/agency/industries/marketing_social_media_agencies.json ; https://github.com/sisodias/siso-repo-bank/blob/2d7d35ecbf7e1158d0a3527e1489040687ac214b/bank/bank_capability_top.jsonl]

This pack supplies comparison evidence for GQ-004, Best Software Primitive, and GQ-013, A Useful Reusable Building Set, as named in the research brief. It does not register a new Library Work, publish a Release, select a Snapshot, install a consumer or prove a usable screen. Research publication and product acceptance are different events. [analysis]
