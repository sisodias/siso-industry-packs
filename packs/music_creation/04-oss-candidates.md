# Stage 4 — Source-inspection checkpoint; the 100-repository sweep is incomplete

Observed **2026-09-13**. **2 upstream repositories inspected; 0 fully scored; 0 adopted.** This is not the final candidate table. The required100-repository floor, all-stage three-lane search, bank reconciliation and two consecutive dry rounds have **not** been met. Do not promote this pack to complete.

The company-first reference is [03-companies.md](03-companies.md), committed at `ba82cb4fd2365e64c7ca211b5de84d6b1ef82ca2`. These two direct checks follow documented vendor format leads. They establish what the formats do, not a selected product stack. Machine-readable observations: [04-oss-candidates.json](04-oss-candidates.json). [analysis]

## What was actually examined through the GitHub connector

`[vendor]` here means upstream-maintainer documentation and GitHub repository metadata. Scores and adoption decisions remain pending until the discovery pile is wide, as the brief requires. Licence readings are metadata, not reasons for rejecting a candidate; any eventual reuse must still respect the applicable terms.

| Repository | Stars at observation | Licence actually read | Latest default-branch commit observed | Source-backed mechanism | Bank status / decision |
|---|---:|---|---|---|---|
| [bitwig/dawproject](https://github.com/bitwig/dawproject) | **1,027** on2026-09-13 | [MIT](https://github.com/bitwig/dawproject/blob/ee4dcdde75940f30e14e55401a26955a58b8322b/LICENSE) | [ee4dcdde75940f30e14e55401a26955a58b8322b](https://github.com/bitwig/dawproject/commit/ee4dcdde75940f30e14e55401a26955a58b8322b), **2025-07-12T10:16:49Z** | [README](https://github.com/bitwig/dawproject/blob/ee4dcdde75940f30e14e55401a26955a58b8322b/README.md): ZIP/XML interchange for project structure, musical/audio timelines, automation and plugin state. Native DAW format and preferences are non-goals. | **UNKNOWN**, not NEW. A code search found no match, but that does not prove absence from large bank layers. Final verdict and scores withheld. |
| [free-audio/clap](https://github.com/free-audio/clap) | **2,345** on2026-09-13 | [MIT](https://github.com/free-audio/clap/blob/a47f6badb49d948fd009998f28309cdab78979c9/LICENSE) | [a47f6badb49d948fd009998f28309cdab78979c9](https://github.com/free-audio/clap/commit/a47f6badb49d948fd009998f28309cdab78979c9), **2026-07-28T21:29:46Z** | [README](https://github.com/free-audio/clap/blob/a47f6badb49d948fd009998f28309cdab78979c9/README.md): C host/plugin ABI with state, parameters, ports and rendering extensions; some resource-related interfaces are explicitly draft. | **UNKNOWN**, not NEW. Bank membership, adoption evidence and final scores not yet reconciled. |

Metadata sources: [DAWproject repository API](https://api.github.com/repos/bitwig/dawproject), [latest commit](https://api.github.com/repos/bitwig/dawproject/commits?per_page=1); [CLAP repository API](https://api.github.com/repos/free-audio/clap), [latest commit](https://api.github.com/repos/free-audio/clap/commits?per_page=1). Both reported `archived:false`. Metadata and README/LICENCE were fetched separately from the default branch; the JSON records their blob hashes as well as the observed head. No build, plugin loading, schema replay or audio comparison was performed. [vendor]

**Interpretation:** session exchange and plugin hosting solve different parts of the problem. A file that parses successfully does not establish correct plugin availability, transferable sample rights, sample-accurate rendering or an accepted restore. Neither project is itself the proposed creator operating system. A stable specification's older commit date is not, by itself, a dead-project verdict. [analysis]

## Counting and membership rules

An inspected repository means its upstream identity, metadata, README and actual root licence were read. **Fully scored** additionally requires the five-axis appraisal, reconciled bank membership, adoption provenance and bounded health evidence. Search hits, repeated forks, bank inventory rows, failed requests and framework names mentioned in a README do not add to the inspected count. This checkpoint has2 inspected and0 fully scored; it does not disguise the difference. [analysis]

The final table must replace UNKNOWN with **ALREADY IN THE BANK** or **NEW**, backed by a dated/pinned search of the bank layers. A source-registry discovery row counts as already held, but not admitted or production-qualified. Absence from one file or an empty connector code search is insufficient for NEW. No bank submissions are justified by this checkpoint. [analysis; [bank query guidance](https://github.com/sisodias/siso-repo-bank/blob/main/README.md)]

Use one of the51 supplied capability tags where it genuinely fits. Proposed provisional mappings are `data-serialization` for DAWproject and `video-audio-codec` as a coarse parent for CLAP. The latter is semantically imperfect: plugin-host ABI is not a codec. A proposed **audio-plugin-protocol** refinement should be recorded as a taxonomy gap, not silently added to the shared vocabulary. [analysis]

## Search contract — planned queries, not executed rounds

The following matrix is a continuation plan derived from the company/workflow map. Format names are search leads, not claims that a suitable parser, licence or reliable implementation exists. Broad generic SaaS/UI/library hunting is excluded; those banks were already supplied. Queries must retain actual result counts, duplicates, failures, repository identities and their stage/artifact-class origin. [analysis]

| Stage | Lane A: practitioner task / runnable application or library | Lane B: topic graph | Lane C: format, protocol or persistent artifact |
|---|---|---|---|
| S01 Intake | music collaboration brief; audio review comments; email attachment intake | `topic:music-collaboration`; `topic:audio-annotation` | EML/MIME attachments; timestamped review annotations |
| S02 Ideas | beat sequencer; music recorder; MIDI sketchpad | `topic:sequencer`; `topic:music-production` | MIDI/SMF; tempo maps; MusicXML where notation is actually needed |
| S03 Samples | sample manager; sample library deduplication; licence receipt catalogue | `topic:sample-library`; `topic:audio-metadata` | WAV/RIFF/BWF; SFZ/SF2; ID3/Vorbis metadata |
| S04 Arrange | DAW session parser; open-source DAW; plugin-host engine | `topic:daw`; `topic:audio-plugin` | ALS/FLP/RPP; DAWproject; CLAP/VST3/LV2 |
| S05 Mix/variants | stem separation; loudness meter; batch audio render | `topic:source-separation`; `topic:audio-processing` | WAV/FLAC; EBU R128/BS.1770 measurement implementations; plugin rendering interfaces |
| S06 Recovery | audio project backup; project dependency inventory; session versioning | `topic:backup`; `topic:audio-archiving` | Content manifests/checksums; referenced versus embedded media; native session structures |
| S07 Handoff | audio delivery validator; stem naming; music version comparison | `topic:music-collaboration`; `topic:audio-annotation` | DAWproject/AAF; channel layouts; delivery manifests; OSC only where a host exposes it |
| S08 Rights | music credits catalogue; royalty split register; rights metadata | `topic:music-publishing`; `topic:music-business` | ISRC/ISWC/IPI identifiers; CWR; supplied licence receipts |
| S09 Release | music release metadata validator; distributor package preparation | `topic:music-distribution`; `topic:music-metadata` | DDEX/ERN; distributor CSV/XML; artwork/audio validation specifications |
| S10 Audience/accounts | artist store; release statement reconciliation; consent-bound fan list | `topic:music-store`; `topic:music-business` | Sales/royalty CSV; RSS/Atom; statement identifiers and accounting exports |

In addition, follow domain awesome lists, actual dependency manifests and other work by maintainers found in the pile. The CLAP README supplies adapter, validator and host/example leads, but those linked repositories have **not** been verified here and are not counted or recommended. Do not turn links into implied inspections. [analysis; CLAP README above]

## Rounds and scoring — no fabricated saturation

The earlier search workflow [run34766764792](https://github.com/sisodias/siso-industry-packs/actions/runs/34766764792) failed before publishing its evidence tree. It does not supply a recoverable discovery-round count. This continuation performed the two direct source checks above, not a completed all-stage discovery round. **Verified completed discovery rounds:0. Verified consecutive dry rounds:0.** [source: workflow job status/log; analysis]

A next sweep needs at least3 genuinely recorded rounds, and must continue if either of the last2 adds previously unseen relevant candidates. HTTP errors, inaccessible pages, changing queries, arbitrary limits and stopping at100 are not dry-round evidence. [analysis]

Only after the pile is wide, score0–5 with a reason and evidence for each axis: **fit** to the actual six-object workflow; **liftability** of the selected unit; **health** using dated commit and issue evidence without pretending contributors measure bus factor; **adoption** from resolved dependence/usage sources rather than stars; and **integration** with the required artifacts. Missing evidence stays null rather than receiving a fabricated middle score. Final choices use ADOPT, STEAL for a pattern-only reimplementation, STUDY or SKIP. [analysis]

**Adoption caution:** the bank README/brief's gloss of `fame_gap` conflicts with the Foundry loader's explanation of adoption outrunning fame. Preserve the contradiction and read the actual scoring provenance before applying a directional penalty. Downloads, dependent counts, `resolved`, `link_method` and source dates can be reported independently; no new score was computed here. [sources: [bank README](https://github.com/sisodias/siso-repo-bank/blob/main/README.md), [Foundry loader](https://github.com/sisodias/siso-foundry/blob/main/pipelines/github/load_adoption_signal.py)]

**Unfinished work is substantive:** this chapter is the initial format-inspection and continuation record, not the requested100-repository result. The final top10, whole-application comparison, local resource floors, adoption scores, new-bank submissions and saturation receipt remain open.
