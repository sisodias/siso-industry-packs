# Workflow — music creation, not a replacement DAW

**Observed 2026-09-13. Ten proposed stages.** The operator scenario and complaint IDs come from [01-person.md](01-person.md); the priced incumbent map is [03-companies.md](03-companies.md). This is a design hypothesis, not a recorded NM workday. Every frequency below is a proposed measurement unit with its actual value **unmeasured**. [analysis]

## The workflow table

Complaint fragments identify the exact quotation in Stage 1. A historical or adjacent-product complaint does not prove a current defect in a proposed component. Where no direct complaint was substantiated, the row says so. The JSON companion carries the same ten rows, including these limits. [analysis]

| id | stage | trigger | inputs | outputs | pain: quoted fragment and source | frequency | handoff | data_object |
|---|---|---|---|---|---|---|---|---|
| W01 | Intake and explicit commitment | A new reference, idea or collaborator message | User-selected message/voice note; reference; intended use; proposed deadline | Draft brief linked to a person and thread; human-approved commitment if agreed | No intake-specific NM complaint established. P05's coordination concern is adjacent, not evidence of NM's channel use: https://forum.ableton.com/viewtopic.php?t=245828 | Per idea/conversation; unmeasured | Creator and collaborator approve scope, recipient and deadline | PartyThread; Work |
| W02 | Sample selection and provenance | A sound is shortlisted | Original/purchased sample; receipt or source URL; permitted-use evidence | Local asset record and provenance status; unresolved rights flagged | P01: “stay subscribed” — unused-credit complaint, not loss of downloaded rights: https://apps.apple.com/ca/app/splice-make-music-now/id1108532275 | Per imported sample; unmeasured | Creator; rights-holder or sample supplier where clarification is needed | AssetRevision; RightsAgreement |
| W03 | Compose and record in the existing DAW | A creative brief or idea is ready | Native project; instruments; packs; audio/MIDI; reference | Updated native project and rough bounce | P06: “Factory Packs” — historical dependency-management concern: https://forum.ableton.com/viewtopic.php?p=1824674 | Per creative session; unmeasured | Creator; performing collaborator | Work; AssetRevision |
| W04 | Checkpoint and recoverable backup | A meaningful revision or session ends | Quiescent native project; referenced assets; rendered bounce | Immutable manifest; backup receipt; separately recorded restore-test result | P04: “missing” — historical missing-file report: https://dnbforum.com/threads/ableton-problem-samples-are-missing.100399/ | Per checkpoint and scheduled restore test; unmeasured | Creator; only explicitly approved backup locations | AssetRevision |
| W05 | Collaboration, review and contribution agreement | A bounce or contribution is ready for review | Exact revision; timestamped comments; contributor identities; proposed shares | Review decision linked to the heard revision; separate composition/master agreement records | P05: “at a time” — version-coordination question: https://forum.ableton.com/viewtopic.php?t=245828 | Per review/contribution; unmeasured | Each collaborator approves their contribution and relevant agreement | PartyThread; AssetRevision; RightsAgreement |
| W06 | Optional AI transformation | Creator explicitly requests separation or transcription | Authorised source audio; selected model/tool; settings | Derived asset plus input hash, model identity, parameters and quality-review result | P08: “import” — historical app-specific import failure, with later changes noted: https://apps.apple.com/in/app/stem-split-ai-vocal-remover/id6742150522 | Per requested transform; unmeasured; never mandatory for every track | Creator approves input use and checks artefacts/output | AssetRevision; RightsAgreement |
| W07 | Mix/master and technical quality checks | A creative revision is ready for delivery | Native session; rendered references; export specification | Human-approved master and stems; format/loudness/peak check results | No direct current mix-quality complaint substantiated. P07's “links” is only a historical recovery/dependency analogy: https://forum.ableton.com/viewtopic.php?sid=e015a01a5121c4a460ea443e32861190&start=30&t=81395 | Per deliverable/revision; unmeasured | Creator; optional engineer and reviewer | AssetRevision; Work |
| W08 | Metadata and release-package preparation | Master selected and required approvals collected | Titles; credits; artwork; identifiers; rights evidence; dates | Versioned release package; missing-field and approval checklist | P03: “tedious” — historical registration-entry report: https://musiclibraryreport.com/forums/topic/should-i-become-a-harry-fox-publishing-affiliate/ | Per release or metadata correction; unmeasured | Creator; contributors; distributor/publisher reviewer | Work; RightsAgreement; Release |
| W09 | Distribution and statement reconciliation | Approved submission or incoming statement/payment | Approved package; portal acknowledgement; original CSV/PDF statement; payment reference | External submission status; normalised statement lines with retained source and reconciliation decisions | P02: “removed” — an individual's distribution-removal report, not an established reason: https://support.google.com/youtubemusic/thread/387216488/youtube-music-removed-all-my-distrokid-releases-%E2%80%93-need-partner-operations-review?hl=en | Per submission and received statement; unmeasured | Distributor, relevant rights organisation, creator and accountant where applicable | Release; LedgerEntry; RightsAgreement |
| W10 | Fan/storefront follow-up and commerce | Approved release, fan reply or order | Approved assets; consent/channel record; external order/payment reference | Human-approved post/reply; fulfilment reference; follow-up task | No fan-specific practitioner complaint established in this sample. Do not infer one from vendor marketing. | Per release, conversation or sale; unmeasured | Creator; fan/buyer; payment/storefront provider | PartyThread; Release; LedgerEntry |

## The chat surface — where a conversation becomes work

NM's actual business channels are **unknown**. The proposed comparison operator uses email plus user-selected WhatsApp/Instagram conversations, not a claim that all three are essential. WhatsApp's Business app documents profiles and messaging tools, but its availability does not establish NM's usage, API permissions or a fully local channel integration. [vendor] https://faq.whatsapp.com/641572844337957 [analysis]

One person—the creator—answers in this scenario. **Response time is unmeasured; no service-level promise is invented.** Record received time, first human review, first reply and accepted commitment separately. Calls, voice notes and paper notes enter through an explicit user action; do not scrape personal inboxes or silently turn a discussion into an order. [analysis]

Five **proposed repeated intents to test**, not measured top-five frequency rankings: availability/deadline; price or licence/use; reference/style/BPM/key; requested file formats/stems; and revision/status/payment questions. An assistant may retrieve approved facts or draft an answer. It cannot invent a price, agree exclusivity, assign a contributor's share, mark a payment settled or send externally without approval. [analysis]

The exact transition is:

```
message/reference → draft brief → creator review → other party's recorded agreement
                  → accepted Work commitment + linked PartyThread
```

The accepted record must name the intended use, deliverable, recipient, deadline and relevant agreement reference; unknown fields remain unknown. A self-generated idea can create a draft Work without a commercial agreement. A release approval is a different transition from accepting a creative brief. [analysis]

## Six shared object families — the possible spine

| Object family | Persistent identity and boundary [analysis] |
|---|---|
| **Work** | Stable creative-work identity with explicitly typed composition and recording references. Do not collapse a musical composition, its sound recording and its release into one identifier. |
| **AssetRevision** | Original/native file or derived render, content hash, parent revision, source provenance, settings and tool/model version. File identity is not a licence or an approval. |
| **PartyThread** | Person/organisation identity plus user-selected conversation, permission and commitment references. Private message bodies are optional, minimised and local. |
| **RightsAgreement** | Source receipt, permission or contribution agreement; composition shares and master shares are separate schemes. “Unknown,” “disputed,” “proposed” and “approved” must remain different states. |
| **Release** | The exact package submitted, approved asset revisions, metadata version, destination and external acknowledgement. Prepared, submitted, accepted and available are distinct statuses. |
| **LedgerEntry** | A statement/payment line with source document, period, currency, external IDs and a reconciliation decision. A calculated royalty estimate is not a settled payment. |

DDEX's Recording Information Notification standard is relevant prior art for carrying contributor and recording-session metadata with audio, not proof of automatic DAW or distributor support. [vendor — standards body] https://ddex.net/standards/recording-information-notification/ [analysis]

## Is it really one super-app?

The proposed stages repeatedly touch the same Work, its AssetRevisions, people/agreements and Release. A **local evidence/coordination spine is plausible**. That does not make all underlying tools one application: native DAWs, proprietary plug-ins, social platforms, distribution and settlement remain separate systems. The honest architecture is a local work binder with adapters, not a browser full of unrelated embedded tabs and not an offline replacement for music distribution. [analysis]

The architecture is worth testing only if linking these objects removes real re-entry, search or review work. If NM only needs a stem-separation operation, or an existing catalogue solves the problem, the multi-object product is unnecessary. [analysis]

## Measurement plan and authority boundaries

Observe one real track from first reference to the next meaningful handoff. Count re-keyed fields, minutes searching for assets, missing-file incidents, revision misunderstandings and review/rework time. Then compare the same class of tasks using the existing stack plus a minimal binder. Do not count machine processing time as human hours saved. All baseline, assisted and returned-hours fields start as **null**. [analysis; value method: https://github.com/sisodias/great-library-of-siso/blob/main/research/industries/source/intelligence/agency/economics/observed-value-model.json]

Creative approval, rights/contract decisions, external sends, distribution submission, payment and account changes remain human-authorised. Local-first means the proposed product stores and processes its working records on the user's device; it does not relocate Spotify, WhatsApp, a royalty administrator or a payment processor onto that device. Spotify's own onboarding identifies the distributor as the delivery route. [vendor] https://artists.spotify.com/get-started [analysis]
