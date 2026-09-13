# The super-app — SUMERA as a local-first creator studio

Read of `github.com/tristangrech/sumera` @ `6a3e0a3`, cloned and inspected 2026-09-13.
**92,100 lines · 580 TS/TSX files · 106 test files · 31 tables · 9 migrations.**

---

## 1. What SUMERA already is

Not a prototype. A shipped SaaS with auth, billing, affiliates, referrals, courses,
community, moderation, admin funnel/metrics, rate limiting, programmatic SEO, and cron jobs.

### The core: a 5-stage scriptwriting pipeline

`draft → questions → elaboration → footage → professionalisation`
(`src/lib/ai/stages/`, 713 lines)

Not one prompt — a methodology. **Stage 2 generates questions back to the creator**
(categorised content/audience/examples/services/personal), and Stage 3 folds the answers in.
That interview loop is the real product insight, and nothing in the open-source field does it.

Six brand-value styles — authority, authenticity, entertainment, education, inspiration,
persuasion — each with an explicit structural template, e.g.

> `vulnerable hook → honest personal story → real lessons learned (raw, not polished) →
> genuine reflection → authentic closing`

Two things here are better than most commercial tools:

**A factual-integrity block in every prompt.** Verbatim from `stage1-draft.ts`:

> *"Never invent the creator's biography, credentials, clients, results, statistics, quotes,
> research, citations, or named organizations. When a personal detail or source is needed but
> was not supplied, write a clear placeholder such as `[add your experience]` or
> `[add a source]` instead of guessing. Treat examples as examples. Do not present an
> illustrative number as measured evidence."*

**Prompt-injection defence.** `UNTRUSTED_SYSTEM_LINE` / `untrustedBlock` wrap user topic and
profile text as content, never instructions, with an explicit trailing guard.

### The seam he has already found

`src/lib/export/elevenlabs.ts` — **757 lines** doing the genuinely hard, unglamorous job:
classifying every line of a generated script as *spoken narration* or *stage direction*.
Handling `[CHAPTER 2: WHY FAKE IT?]` as a heading while bracketed narration ending in a
question mark stays speech. Nobody writes that unless they have hit the problem for real.

`src/lib/editor-handoff/` exports a real timeline model (assets, clips, captions, canvas/fps)
plus a CapCut package. `src/lib/video-integration/` is 35 files: credit ledger with
reservations, R2 storage, Replicate webhooks with signature verification, SRT handling.

### He is shipping the video pipeline right now

| Date | Migration |
|---|---|
| 2026-08-23 | admin_notification_outbox |
| 2026-09-02 | registration intelligence, first-party auth |
| 2026-09-05 | billing_foundation |
| **2026-09-13** | **video_generation → video_credit_ledger → video_credit_invoice_receipts → editable_narration** |

Three weeks from first migration to a working video pipeline. Four migrations on the day of
this research.

## 2. The spine — the one architectural intervention

**`scripts.content` is `text`.** Stages live in a JSON column. There is no scene, segment or
shot table. Every stage re-parses a blob.

But `narration_paragraph_versions`, migrated **today**, already has:

```
paragraphId · approvedScriptVersionId · parentVersionId (lineage)
voiceId · modelId · pronunciationOverrides
audioObjectKey · speechDurationMs · audioDurationMs · alignment (word-level)
```

**Verified: no code outside `schema-pg.ts` references `paragraphId`.** The structured model is
designed and migrated but not wired up.

That is the intervention. Not "rebuild it" — **finish the model he started today**:

```
Project
  └── Script (version-controlled)
       └── Paragraph ──── Narration (audio + word alignment + pronunciation)
            └── Shot ──── Footage (asset + rights)
                 └── Clip ──── Timeline ──── Render
```

Everything downstream depends on it and nothing downstream is possible without it:
per-paragraph regeneration without re-rendering the whole script · B-roll matched to
individual shots · timeline assembly from alignment data rather than guessed WPM ·
multi-platform recuts (a 12-minute long-form becoming six Shorts) · caption timing that is
derived rather than synced.

The current `src/lib/scripts/timing.ts` estimates duration from words-per-minute
(80–240 WPM, default 150). Once alignment data is wired through, timing is **measured, not
estimated** — and every downstream cut becomes frame-accurate.

## 3. Component map — what to lift

131 OSS repos verified. The pipeline is barbell-shaped: the middle is superbly served, both
ends are near-empty.

| Workflow stage | Lift | Verdict | Why this one |
|---|---|---|---|
| Timeline model | [OpenTimelineIO](https://github.com/AcademySoftwareFoundation/OpenTimelineIO) (1,980★, Apache-2.0) | **ADOPT** | SUMERA's `timeline.ts` is 129 lines of a model the industry already standardised. Runners-up: hand-rolled (current), `editly` JSON. |
| Render | [hyperframes](https://github.com/heygen-com/hyperframes) (49,434★, Apache-2.0) | **ADOPT** | HTML → video, built for agents; SUMERA is already a Next.js app so the authoring language is free. Runners-up: `html-video` (4,570★), `motionforge` (MIT, avoids Remotion licence), `editly` (5,500★). |
| TTS | [Chatterbox-TTS-Server](https://github.com/devnen/Chatterbox-TTS-Server) (1,440★, MIT) + [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) (61,770★, MIT) | **ADOPT** | Removes the single largest per-use cost and the largest source of credit anxiety. Runners-up: VoxCPM, fish-speech, CosyVoice, OmniVoice — all viable; this area is over-served. |
| Audio post | [pedalboard](https://github.com/spotify/pedalboard) (6,303★, GPL-3.0) | **ADOPT** | Spotify's FX chain. Licence is GPL — fine for self-host, material if redistributed. |
| Dead air | [auto-editor](https://github.com/WyattBlue/auto-editor) (5,201★, Unlicense) | **ADOPT** | Public domain, does one thing perfectly. |
| Caption sync | [ffsubsync](https://github.com/smacke/ffsubsync) (7,870★, MIT) | **ADOPT** | Only needed until alignment data makes it redundant. |
| Editor handoff | [pyJianYingDraft](https://github.com/GuanYixuan/pyJianYingDraft) (4,343★, Apache-2.0) | **STEAL** | SUMERA hand-rolled CapCut export in 91 lines; this is the mature version. |
| Shot vocabulary | [video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) (8,365★, Apache-2.0) | **STEAL** | 152 shot recipes + 209 motion previews — the missing vocabulary for Stage 4 footage. |
| Research | [youtube-transcript-api](https://github.com/jdepoix/youtube-transcript-api) (8,319★, MIT) + [popyt](https://github.com/brandonbothell/popyt) (45★, Unlicense) | **ADOPT** | Competitor transcripts without API quota; popyt is zero-dep TypeScript. |
| B-roll library | [immich](https://github.com/immich-app/immich) (114,018★, AGPL-3.0) | **ADOPT** | Best self-hosted media manager. AGPL — self-host only. |
| Publishing | [postiz-app](https://github.com/gitroomhq/postiz-app) (35,753★, AGPL-3.0) | **ADOPT** | Category leader. AGPL. |
| Analytics | [metabase](https://github.com/metabase/metabase) (49,229★) | **ADOPT** | No YouTube retention tool exists; ingest + model + visualise. |
| Thumbnail A/B | [growthbook](https://github.com/growthbook/growthbook) (8,348★) + [sharp](https://github.com/lovell/sharp) (32,658★, Apache-2.0) | **ADOPT** | Complete experimentation engine; needs only a YouTube-CTR adapter. |
| Sponsorship CRM | [twenty](https://github.com/twentyhq/twenty) (56,693★) | **ADOPT** | Nothing creator-shaped exists; this is the best base. |

**What stays SUMERA's own** (the ~5% that is genuinely differentiated):
the 5-stage interview pipeline · the six brand-value style templates · the factual-integrity
constraints · the 757-line narration/direction parser · the data spine.

**Warning on the monoliths.** MoneyPrinterTurbo (123,122★) is the most-starred repo in the
entire sweep, and the "end-to-end faceless generator" category is crowded and largely low
quality. These bundle script + TTS + stock + assembly in ways that are hard to pull apart.
**STEAL the pipeline shape; do not fork one.** Composable primitives beat a monolith.

## 4. The glue — where the real cost is

- **Wiring `paragraphId` through** the existing generation stages, the editor, and the
  handoff. This is the load-bearing work and it is not small.
- **Alignment → timeline**: converting ElevenLabs word alignment into OTIO clip boundaries.
- **BYO-key management**: secure local storage of the creator's own provider keys, per-provider
  fallback, and honest cost display *before* a call rather than credit deduction after it.
- **Packaging for non-technical install.** "Runs on their laptop" is only true if it installs
  without a terminal. This is the single biggest risk in the whole thesis.
- **Licence split**: keep the core MIT/Apache (OTIO, hyperframes, Chatterbox, GPT-SoVITS,
  auto-editor, ffsubsync, sharp). Immich, Postiz, pedalboard and most schedulers are
  AGPL/GPL — fine self-hosted, material if ever redistributed.

## 5. Deployment

Per SISO doctrine §6, and here it is also the product thesis:

- **Creator's own machine** — local-first. `mlx-audio` (7,879★, MIT) runs TTS natively on
  Apple silicon, which matches the target creator's hardware.
- **Optional client VPS** for creators who want rendering off their laptop.
- **Nothing on SISO servers.** No credit ledger, no metering, no expiring balances.

**Resource floor is the honest constraint**: quality TTS and video rendering want real
compute. A creator on a base MacBook Air will have a worse experience than one on an M-series
Pro, and that must be stated rather than hidden.

## 6. What we cannot get from OSS

- **A scriptwriting engine.** Nothing standalone exists. SUMERA's own pipeline is already ahead
  of the entire open-source field.
- **Retention-curve analysis.** Zero repos. Must be built.
- **Sponsorship CRM and media kits.** Nothing. Must be built over a generic CRM.
- **Rights tracking per clip.** DAMs store assets; none track usage rights.
- **Thumbnail design.** No OSS designer exists.

## 7. Architecture sketch

```
┌─ Creator's machine ────────────────────────────────────────────┐
│                                                                │
│  Next.js app (SUMERA core, unchanged)                          │
│    ├── 5-stage pipeline ── BYO keys → Anthropic / OpenAI / …   │
│    ├── narration parser (757 lines, kept)                      │
│    └── Postgres ── Project→Script→Paragraph→Shot→Clip          │
│                                                                │
│  Local services (Docker or native)                             │
│    ├── Chatterbox / GPT-SoVITS ── TTS + cloning                │
│    ├── pedalboard ── audio post                                │
│    ├── hyperframes ── HTML → video render                      │
│    ├── auto-editor, ffsubsync ── cleanup                       │
│    └── immich ── B-roll library                                │
│                                                                │
│  Export: OpenTimelineIO → CapCut / Premiere / Resolve          │
└────────────────────────────────────────────────────────────────┘
        Optional: client VPS for heavy renders. Never SISO's.
```

The creator's keys. The creator's machine. The creator's data. No meter.
