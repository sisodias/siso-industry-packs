# How SUMERA uses this research

A build plan mapped onto `tristangrech/sumera` as it stands at commit `6a3e0a3` (2026-09-13).
Nothing here is a rewrite. Every phase either finishes something already started or lifts a
permissively-licensed component into a seam that already exists.

---

## The one-sentence version

SUMERA's homepage already promises four stages — **Script (live) → ElevenLabs (text export
only) → AI video (in testing) → CapCut (coming soon)**. Three of the four are unbuilt, the
creator leaves the product at stage 1, and **every missing piece exists as MIT/Apache open
source**. The work is to make the product his marketing already describes.

## What he has, measured

| | lines | state |
|---|---|---|
| `ai/stages` — the 5-stage pipeline | 713 | **Live. The differentiated asset.** |
| `export/elevenlabs.ts` — narration/direction parser | 757 | Live. Hardest problem, solved. |
| `video-integration` — credits, R2, Replicate webhooks, SRT | 3,362 | Built this week |
| `video-generation` — Replicate/WAN adapter | 571 | In testing |
| `editor-handoff` — timeline model + CapCut package | 337 | Stub. **Needs 16,870 lines it can lift.** |
| Video editing dependencies | **0** | None. No Remotion, wavesurfer, ffmpeg, dnd-kit, Radix |

And the finding that sets the whole sequence: `narration_paragraph_versions` was migrated on
**2026-09-13** with `paragraphId`, `voiceId`, `pronunciationOverrides`, word-level `alignment`
and version lineage — and **no code outside the schema file references `paragraphId`**. The
structured spine is designed, migrated, and not wired up.

---

## Phase 0 — Finish the spine he started (1–2 weeks)

**Do this before anything else. Everything downstream depends on it and nothing downstream is
possible without it.**

`scripts.content` is a `text` blob with stages in a JSON column. Every stage re-parses it.
Wire `paragraphId` through generation, the editor and the handoff so a script becomes
addressable units:

```
Project → Script → Paragraph → Narration(audio + word alignment) → Shot → Clip → Timeline
```

Once alignment data flows, timing is **measured, not estimated** — `src/lib/scripts/timing.ts`
currently guesses duration from words-per-minute (80–240, default 150). Frame-accurate cuts,
per-paragraph regeneration, B-roll matched to a specific line, and multi-platform recuts all
become possible the moment this exists, and stay impossible while it does not.

**Lift:** nothing. This is his own migration, finished.

## Phase 1 — Close stage 02: real narration (1–2 weeks)

Today SUMERA exports text and the creator goes to ElevenLabs. Close the loop.

| Lift | ★ | Licence | For |
|---|---|---|---|
| `devnen/Chatterbox-TTS-Server` | 1,440 | MIT | Drop-in self-hosted TTS server |
| `RVC-Boss/GPT-SoVITS` | 61,770 | MIT | Voice cloning from 1 min of the creator's own audio |
| `Blaizzy/mlx-audio` | 7,879 | MIT | Runs natively on the creator's Mac |
| `spotify/pedalboard` | 6,303 | GPL-3.0 | Audio post — self-host only |

The `narration_paragraph_versions` table already has `voiceId`, `modelId`,
`pronunciationOverrides` and `providerStatus`. It was built for exactly this. Keep ElevenLabs
as the premium path; add a local path that costs nothing per word.

**Why it matters commercially:** the loudest complaint in this entire market is expiring
credits — *"I paid month after month, accumulated around 100,000 credits, and then discovered
that credits were gone"* (ElevenLabs, 1★). A local TTS path removes the largest per-use cost
in the product.

## Phase 2 — Close stage 04: the real editor (3–6 weeks)

**`opencut-app/opencut-classic` — 91,028 lines, MIT, React 19.**
16,870 lines of timeline · 5,463 preview · mediabunny (WebCodecs) · wavesurfer ·
`@huggingface/transformers` for in-browser Whisper.

Stack overlap with SUMERA is real: both run React 19, Tailwind, lucide, class-variance-authority.
This is a merge, not a rewrite.

> **Correction worth carrying:** `OpenCut-app/OpenCut` (89,332★) is *not* the one. I cloned it —
> 6,991 lines, three routes, no timeline, mid-rewrite. The working editor is `opencut-classic`,
> which has only 247★ because the stars stayed on the rewrite.

Alongside it:

| Lift | ★ | Licence | For |
|---|---|---|---|
| `AcademySoftwareFoundation/OpenTimelineIO` | 1,981 | Apache-2.0 | The interchange model his 129-line `timeline.ts` should become |
| `GuanYixuan/pyJianYingDraft` | 4,343 | Apache-2.0 | The mature version of his 91-line CapCut export |
| `Vincentwei1021/video-shotcraft` | 8,365 | Apache-2.0 | 152 shot recipes — the missing vocabulary for Stage 4 footage |

**The architectural decision that cannot be retrofitted:** frame accuracy. HTML5
`video.currentTime` is keyframe-bound, and 33ms drift at 30fps reads as a word highlighting
late. opencut-classic already chose WebCodecs via mediabunny — so taking it makes the decision
correctly and for free. Building a timeline first and adding frame accuracy later is a rewrite.

## Phase 3 — Serve the 81% (4–8 weeks)

**This is the strategic move, and SUMERA's own site makes the argument.**

Of his 54 niche pages, **only one is `faceless`**. Classified by how they are actually made:

| shape | count | |
|---|---|---|
| On-camera (films themselves) | 17 | tech reviews, cooking, fitness, beauty, DIY, travel |
| Talking-head to camera | 17 | motivation, parenting, mental health, freelancing |
| Screen capture | 8 | gaming, coding, productivity, VFX |
| Multi-cam | 2 | interview format, podcast clips |
| Faceless | **10** | the only shape the current pipeline serves |

**44 of 54 — 81% — require shooting and editing footage.** And the editing burden is the real
number: working professionals independently report **~1 hour of post per finished minute**.
Interview format, his longest niche at 30–60 minutes, is a **45-hour edit**. One video in each
of his 54 niches is 828 finished minutes ≈ **104 working days** of editing.

SUMERA currently saves the first hour of that.

| Lift | ★ | Licence | For |
|---|---|---|---|
| `m-bain/whisperX` | 24,018 | BSD-2 | **Word-level timestamps + diarisation. Build this first — everything else is a view over it** |
| `WyattBlue/auto-editor` | 5,201 | **Unlicense** | Silence and dead-air removal. Public domain |
| `snakers4/silero-vad` | 10,205 | MIT | Speech/silence primitive |
| `Breakthrough/PySceneDetect` | 5,174 | BSD-3 | Segments rushes into takes |
| `Rikorose/DeepFilterNet` + `resemble-enhance` + `nara_wpe` | — | permissive | Denoise, enhance, de-reverb — the Studio Sound analogue |
| `getopenscreen/openscreen` | 2,839 | MIT | Screen capture with auto-zoom — 8 niches need it |
| `jlecomte/voice-activated-teleprompter` | 81 | MIT | **Nobody in the competitive set has a teleprompter** |

## Phase 4 — Own what cannot be lifted

Everything above is commodity. These are the parts with **no open-source answer**, which is
exactly why they are worth building and why they are defensible.

**1. Take selection.** Targets the sharpest complaint found anywhere in the research:

> *"I also spend an inordinate amount of time tidying up a sentence or paragraph only to move
> on and find another, but perfect take, of the exact same line immediately after."*

That is not slow work, it is **wasted** work. Segment rushes (PySceneDetect), transcribe each
(whisperX), rank by delivery and completeness. **Ship it as ranked, navigable selects with
transcript evidence — never an opaque auto-cut.** r/editors pushes back hard on replacing the
review pass: *"going through the footage is the best way to get familiar with what you have."*
Augment it; do not replace it.

**2. Retention-to-transcript alignment.** Pull the `audienceWatchRatio` curve from the
Analytics API, join it to the word-timestamped transcript, find negative-slope segments.
Output: *"you lost 8% of viewers across these 40 words."* **Zero repos do this.** It is the
only thing that tells a creator *why* a video underperformed rather than *that* it did, it
compounds across the whole back catalogue, and it feeds the title scorer and idea ranker.

**3. Rights manifest.** Per video: asset → source → licence → proof of purchase → permitted
uses → expiry, with claim state. Searching "music license tracking" returns **zero results**;
GitHub's entire copyright topic is software SBOM tooling. A single unlicensed track can
demonetise a video permanently — this converts an unbounded risk into a tracked liability.

**4. The niche system as production profiles.** His 54 niches are currently prompt variations
— tone and target length. Each already declares a format (`Code-Along`, `Day in the Life`,
`Head-to-Head Comparison`). Turn each into a **production profile**: a shot list, an edit
template, a B-roll plan, a default timeline. That turns 54 SEO pages into 54 working
configurations of the whole app, and it is the cheapest differentiation available because the
taxonomy already exists.

## Phase 5 — Re-point the business machinery he already has

SUMERA holds roughly **20,000 lines of working business code** — billing 11,639 · admin 5,142
· analytics 1,884 · notifications 871 · affiliate 589 · courses 122.

**All of it serves SUMERA's business, not the creator's.** `affiliate_stats` tracks people who
refer SUMERA. `course_purchases` tracks who bought SUMERA's course. `stripe_webhook_events`,
`referral_rewards`, `video_credit_grants` — all SUMERA's revenue.

Every one of those is a working implementation of something the creator needs, pointed the
wrong way. **Re-pointing them is a schema change and a permissions boundary, not a build.**
The creator has their own affiliates, their own course, their own sponsors, their own revenue.

Then add what has no OSS answer at all:

- **Auto-generated media kit** — live analytics, audience demographics, past sponsor
  performance, rate card. Does not exist in open source; changes what a creator can *charge*,
  which is a revenue line rather than a time saving.
- **Unified revenue ingestion** — `firefly-iii` (ledger + rules + API) and `vas3k/TaxHacker`
  (MIT, LLM receipt parsing) exist and are excellent; the platform connectors do not.

## The business-model decision

SUMERA prices at **€10.80 Starter / €39.59 Pro**, token-metered, with
`video_credit_grants` / `video_credit_reservations` / `video_credit_invoice_receipts` built
this week.

That is the model earning 1★ reviews across the entire category — **InVideo 1.9/5** (32%
one-star), **ElevenLabs 3.0/5** (38% one-star) — and the complaints are structural, not about
quality:

> *"a single unfinished 35-second video consumed all my monthly credits."*
> *"I blew through 2000 credits in one afternoon trying to make a couple of YouTube videos so I deleted my account."*

The stack tax a serious creator pays is **$1,905/yr prepaid**, $2,519.76 billed monthly — a
$615 penalty for not prepaying. At $2 RPM that is **952,000 views a year just to pay for
tools**, and 38% of a $5,000/yr channel.

**The option worth putting to Tristan:** a bring-your-own-key, self-hosted tier alongside the
metered one. Same pipeline, creator's own API keys, creator's own machine, no expiring credits.
It converts the category's dominant complaint into the product's defining feature, and the
incumbents cannot copy it because their revenue *is* the meter.

**Falsifier, stated honestly:** if creators will not self-host — if the friction of running a
local stack exceeds the pain of credit anxiety — this collapses and conventional SaaS is
right. Untested. Test before building.

## Licence discipline

The MIT/Apache path is complete; nothing forces a restricted dependency.

**Avoid:** Remotion (paid company licence above 3 employees) · tldraw (proprietary, watermark)
· twick (Sustainable Use) · react-virtuoso (**no LICENSE file at all**) · Kimu, OpenChatCut
(AGPL) · peaks.js (LGPL).

**Safe core:** opencut-classic · OpenTimelineIO · mediabunny · wavesurfer · whisperX ·
auto-editor (public domain) · PySceneDetect · Chatterbox · GPT-SoVITS · TipTap · dnd-kit ·
TanStack · Ghost.

AGPL is fine self-hosted but material if redistributed — that affects Immich, Postiz,
firefly-iii, Karakeep and most schedulers.

## Sequence, and why

1. **Spine** — unblocks everything, and it is his own half-finished work.
2. **Narration** — smallest closure of a promise already on the homepage; kills the biggest
   per-use cost.
3. **Editor** — the largest lift by value; 91k lines of MIT that turns three "coming soon"
   stages into one product.
4. **81% of niches** — stops the creator leaving after stage 1.
5. **Take selection · retention alignment · rights · production profiles** — the moat,
   precisely because none of it can be lifted.
6. **Re-point the business machinery** — already written, pointed the wrong way.

**Evidence:** `00-SUMMARY.md`, `01-person.md`, `05-superapp.md` in this pack ·
214 verified repos at https://siso-loot-list.pages.dev
