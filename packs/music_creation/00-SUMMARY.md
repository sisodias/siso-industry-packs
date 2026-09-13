# Music creation — research summary

**2026-09-13 · low-priority consumer favour · local-first · research only.** [analysis]

**Person and segment:** NM makes beats and wants AI help; the original detailed specification is unavailable. The primary design scenario is an independent beatmaker/self-releasing artist, not an editing-for-hire studio or an observed NM workday. Preserve that uncertainty and the consumer priority. [analysis; source: https://github.com/sisodias/siso-industry-packs/blob/main/packs/music_creation/README.md]

**Verdict: NO broad super-app build now.** Test one exact-revision project/release handoff against the existing DAW, backup route and local catalogue products. Saltado already advertises free local cataloguing; a catalogue-only clone has no established wedge. [vendor] https://www.saltadosessions.com/ [analysis]

**Proposed wedge:** preserve the exact native project, referenced assets, provenance receipts, reviewed bounce, contributor approvals and release package in a recoverable local binder. Keep the creative workstation; make separation/transcription optional. [analysis; design: https://github.com/sisodias/siso-industry-packs/blob/main/packs/music_creation/05-superapp.md]

**Stack tax:** the deliberately overlapping comparison basket is **USD 1,457.87/year recurring**, plus **383** of initial licences/fees; first-year cash is **USD 1,790.87** using the stated introductory price. This is neither NM's spending nor removable savings. Actual cancelled spend, hours returned, migration cost, operating cost and second-deployment cost remain **null / unmeasured**. [analysis; arithmetic and vendor URLs: https://github.com/sisodias/siso-industry-packs/blob/main/packs/music_creation/03-companies.md ; https://github.com/sisodias/siso-industry-packs/blob/main/packs/music_creation/06-value.md]

**Spine:** Work; AssetRevision; PartyThread; RightsAgreement; Release; LedgerEntry. Composition, master, release approval and payment authority remain separate. Everything proposed runs on the user's machine; distributors, messaging platforms, fans and payment/rights organisations remain external counterparts, not SISO-hosted services. [analysis; architecture source above]

**Actual coverage:** **142 repositories examined**, **143 verified**, **128 licence files retrieved**, **10 Tier-1 companies**, **10 Tier-2 offerings**, **8 practitioner complaint sources**, **10 workflow stages**, **8 conditional ADOPT choices**, **8 gaps**. Bank comparison: **37 already held / 106 NEW verified**, of which **92 NEW entries are retained for intake consideration**. All NEW records include a keep/reject disposition; none is silently admitted into the canonical bank. Six search rounds ended with two targeted gap rounds adding no names; this is not global search-exhaustion proof. [analysis; evidence: https://github.com/sisodias/siso-industry-packs/blob/main/packs/music_creation/evidence/pack-validation.json]

**Gap list:** actual operator baseline; native-project/plug-in fidelity; sample clearance; contributor agreement; distributor/registration acceptance; AI code/weight/output qualification; device/installer/restore proof; and network reach/payment/economic value. Some complaints are historical or indexed-excerpt evidence, and source availability does not equal current defect prevalence. No model, candidate application or NM device was executed/tested. [analysis; limitations: https://github.com/sisodias/siso-industry-packs/blob/main/packs/music_creation/01-person.md ; https://github.com/sisodias/siso-industry-packs/blob/main/packs/music_creation/05-superapp.md]

## Top ten research choices

| Repository | Verdict | Role |
|---|---|---|
| [restic/restic](https://github.com/restic/restic) | ADOPT | Local snapshot/restore mechanism [evidence](https://github.com/sisodias/siso-industry-packs/blob/6913ada47d9517ca254627cdaef12aed40ed342e/packs/music_creation/evidence/repo-118.json) |
| [FFmpeg/FFmpeg](https://github.com/FFmpeg/FFmpeg) | ADOPT | Audio inspection and explicit conversion [evidence](https://github.com/sisodias/siso-industry-packs/blob/6913ada47d9517ca254627cdaef12aed40ed342e/packs/music_creation/evidence/repo-050.json) |
| [quodlibet/mutagen](https://github.com/quodlibet/mutagen) | ADOPT | Local metadata bridge [evidence](https://github.com/sisodias/siso-industry-packs/blob/6913ada47d9517ca254627cdaef12aed40ed342e/packs/music_creation/evidence/repo-065.json) |
| [nomadkaraoke/python-audio-separator](https://github.com/nomadkaraoke/python-audio-separator) | ADOPT | Optional local stem separation [evidence](https://github.com/sisodias/siso-industry-packs/blob/6913ada47d9517ca254627cdaef12aed40ed342e/packs/music_creation/evidence/repo-033.json) |
| [spotify/basic-pitch](https://github.com/spotify/basic-pitch) | ADOPT | Optional audio-to-MIDI [evidence](https://github.com/sisodias/siso-industry-packs/blob/6913ada47d9517ca254627cdaef12aed40ed342e/packs/music_creation/evidence/repo-044.json) |
| [slhck/ffmpeg-normalize](https://github.com/slhck/ffmpeg-normalize) | ADOPT | Reproducible technical export/QC [evidence](https://github.com/sisodias/siso-industry-packs/blob/6913ada47d9517ca254627cdaef12aed40ed342e/packs/music_creation/evidence/repo-098.json) |
| [duckdb/duckdb](https://github.com/duckdb/duckdb) | ADOPT | In-process statement analysis [evidence](https://github.com/sisodias/siso-industry-packs/blob/6913ada47d9517ca254627cdaef12aed40ed342e/packs/music_creation/evidence/repo-122.json) |
| [roex-audio/dawproject-py](https://github.com/roex-audio/dawproject-py) | ADOPT | Supported DAWproject interchange [evidence](https://github.com/sisodias/siso-industry-packs/blob/6913ada47d9517ca254627cdaef12aed40ed342e/packs/music_creation/evidence/repo-142.json) |
| [swendlcode/stack-desktop](https://github.com/swendlcode/stack-desktop) | STUDY | Whole offline catalogue comparator [evidence](https://github.com/sisodias/siso-industry-packs/blob/6913ada47d9517ca254627cdaef12aed40ed342e/packs/music_creation/evidence/repo-136.json) |
| [DefaultMo/nash-royalty-engine](https://github.com/DefaultMo/nash-royalty-engine) | STUDY | Existing royalty-parser comparator; noncommercial terms [evidence](https://github.com/sisodias/siso-industry-packs/blob/6913ada47d9517ca254627cdaef12aed40ed342e/packs/music_creation/evidence/repo-139.json) |

ADOPT is a conditional design choice, not installation or runtime verification. Full comparisons, source dates, licences, all scores and exclusions are in [04-oss-candidates.md](04-oss-candidates.md); machine-readable design and acceptance tests are in [05-assembly.json](05-assembly.json). [analysis]
