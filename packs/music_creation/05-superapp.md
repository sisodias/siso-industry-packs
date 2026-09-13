# Stage 5 — A local companion contract, not an admitted component stack

Date: **2026-09-13**. **Preliminary architecture only.** [Stage4](04-oss-candidates.md) has2 source inspections and no completed broad comparison; therefore no OSS component is selected or labelled ADOPT here. This chapter preserves the proposed object model, integration work and acceptance boundary without pretending the assembly has been built. Machine-readable contract: [05-assembly.json](05-assembly.json).

All proposed architecture, tests, screens and sequencing below are `[analysis]`. The source basis is the [operator study](01-person.md), [ten-stage workflow](02-workflow.md), [company/competitor map](03-companies.md) and [format inspections](04-oss-candidates.md). No user files, DAW session, plugins, models or accounts were operated.

## 1. The six-object spine

Keep **Project, Asset, Revision, Conversation, RightsRecord and Release** from Stage2. Do not introduce a second set of differently named objects in each module. The native DAW owns musical editing; the companion owns only a transparent record of the surrounding work.

The proposed relationships are:

```
Conversation --confirmed request--> Project
Project --has--> Revision --references exact bytes--> Asset
Asset --derived from--> Asset
RightsRecord --documents supplied evidence/decisions for--> Asset / Project
Release --pins--> Revision + RightsRecord
Conversation --approval/send/feedback event--> Revision / Release
```

An original path and a content hash serve different purposes: the path locates a file; the hash records byte identity. Preserve both, with relative paths in portable packages. A duplicate title does not merge two projects. Changing a source asset creates a new referenced version rather than silently rewriting an accepted delivery.

RightsRecord stores provenance and attributed approvals, not an automatic declaration of ownership. A Release records local preparation, approval, submission, external acceptance and statement references as distinct events. It must never infer “paid” merely because a local package exists.

## 2. Component map — selection deliberately pending

No runner-up was beaten because the required wide sweep and scoring are incomplete. The candidates to compare are **classes of tools**, not fabricated named winners. Commercial/native baselines resolve to the sourced profiles in Stage3.

| Stages | Existing authority to preserve | OSS unit to compare in the sweep | What might need to be ours | Current decision / meaningful comparison |
|---|---|---|---|---|
| S01 | Creator's chosen messaging and calendar | Selected-message/file import adapters | Confirmed request → stable project/revision link | Unselected. Compare with manual paste plus an ordinary checklist; no inbox harvest. |
| S02–S04 | Existing DAW and licensed plugins | Whole DAWs as benchmarks; project parsers and interchange validators | Read-only project inventory, source/version references, adapter boundary | Unselected. Native project collection and Saltado are baselines, not ignored competitors. |
| S03 | Original media and supplier receipts | Local sample catalogue, metadata reader and duplicate-detection tools | Asset-to-provenance links with explicit unresolved items | Unselected. Compare native browser and existing companion before building a catalogue. |
| S05 | Creator's audible acceptance | Local batch processing, stem separation and measurement tools | Reproducible job manifest and accepted derived-asset links | Unselected. Compare native DAW functions first; do not assume AI is the useful missing piece. |
| S06 | Original project files and user-owned backup destination | Snapshot/backup and restore-verification components | Exact revision manifest plus separate restore evidence | Unselected. Generic backup is a bank reuse problem, not an excuse for a new backup engine. |
| S07 | Human recipient/delivery approval | Package validation and media-metadata tools | Approved revision → expected deliverables → receipt linkage | Unselected. Kora/Export Flow is a direct baseline; a folder of renamed files is not differentiation. |
| S08–S09 | Contributors, creator and external release service | Rights/identifier/metadata parsers and export templates | Decision provenance and destination-specific package projection | Unselected. No automatic clearance, registration, publication or payout. |
| S10 | Fan channels, distributor statements and existing accounting authority | Statement import/reconciliation and consent-bound export components | Release-linked observations without a competing financial ledger | Unselected. A spreadsheet may remain sufficient. |

**Inspected interfaces, not selected engines:** DAWproject and CLAP supply different reference boundaries as recorded in Stage4. They are not substitutes for the missing whole-application comparison, and merely supporting one of them does not pass a musical round-trip test.

## 3. The glue that has to be demonstrated

**Snapshot consistency.** Scanning a project while the DAW is saving can observe a mixed state. The design needs a stable-read rule, changed-during-read detection and an explicit retry/incomplete state. Never call a directory copy a recoverable checkpoint without testing it.

**Native identifiers and semantic loss.** Track IDs, names, channel counts, musical time, automation and plugin resources have different meanings across formats. Each adapter needs a capability/unsupported-fields report. Unknown fields should survive as source evidence where possible; unsupported material must not disappear behind a green “converted” label.

**External dependencies.** A project may reference media or settings outside its own folder. Inventory user-approved roots only. Record missing/inaccessible files and unresolved plugin versions; do not search every personal directory, copy licence activations or load arbitrary plugins merely to inspect a project.

**Safe media jobs.** Preserve the source; put generated variants in a staging area. Record input hashes, tool/model revision, settings, outputs, failure and user acceptance. A cancelled or partial job must not replace the prior accepted revision. Concurrency, memory pressure and interruptions need tests on the actual machine before an automatic queue is enabled.

**Review and delivery.** A delivery manifest names the approved revision, target media properties, naming/folder rules and intended recipient. Test expected-versus-produced files and record any unresolved check. Human approval of a particular package does not approve a later changed package. Default to manual external sending.

**Persistence and recovery.** Keep catalogue data exportable alongside plain manifests. Back up metadata and referenced media separately and test restore into a separate location. A successful metadata restore does not prove that licensed plugins are available or that the result sounds right.

## 4. Build versus lift

The brief's roughly5% differentiated-code target is a design intention, **not a measured estimate** for this assembly. No honest ratio can be assigned before component selection, adapter spikes and tests.

Lift existing processing, parsing, storage and UI capability where suitable; build only the identity/provenance joins and workflow decisions that a measured need requires. Do not rebuild a DAW, backup system, chat platform, accounting package or distribution service. A compatible existing companion may be the best outcome, including a small export adapter rather than a new app.

For UI, reuse the existing [SISO component-bank selection process](https://github.com/sisodias/siso-component-bank/blob/main/README.md), preserving each author's rights. Required screen concepts are an idea/project inbox, revision/dependency inspector, asset/provenance view, render-job queue, delivery review and release/statement view. These are proposed screens, not selected components or a tested design.

## 5. Deployment contract — entirely user-owned

```
USER'S LAPTOP
  Desktop/local UI
       |
  Local project catalogue + plain export manifests
       |
  Read-only adapters ----> approved native projects / sample folders
       |
  Explicitly requested worker ----> staging outputs ----> creator approval
       |
  Revision/package store ----> user-owned backup destination

EXTERNAL, ONLY WHEN THE USER CHOOSES
  selected message/file import; manual delivery; distributor submission;
  supplier receipts; downloaded statement files

NO SISO application server, media relay, hosted catalogue or hosted model runtime.
```

Preferred operational shape is a small desktop companion with optional on-demand workers, not a collection of always-on server applications. This is a constraint to test against candidates, not a promise that the selected stack will be one binary.

**Resource floor is unknown.** The client's OS, processor architecture, RAM, free storage, audio workload and need for local models are unknown. No16GB/GPU requirement or low-memory compatibility is claimed. Measure idle memory, full-scan memory, job peak memory, CPU/GPU use, job duration, scratch space and impact on the running DAW for each selected route. Keep model download size and model-weight terms separate from code licence.

**Cost per deployment is unknown.** Catalogue size, audio retained, backup copies, optional hardware, electricity and support all depend on the actual machine/use. Zero SISO hosting in the proposed architecture is a boundary, not proof that running it costs zero. Never move work to SISO servers simply because a local candidate is too heavy.

## 6. Honest gaps

1. **Client fit:** no recovered specification or measured baseline; the proposed primary pain may be wrong.
2. **Selection breadth:**98 further distinct inspections at minimum, plus full scoring/membership reconciliation and dry-round evidence, remain before a final stack.
3. **Cross-DAW fidelity:** portable structure is not proof of equivalent sound, plugin availability or complete preference/activation recovery.
4. **Rights and external authority:** local metadata cannot provide missing permission, contributor agreement, distributor acceptance, bank execution or an audience.
5. **Private/local AI:** model suitability, resource cost, quality and code/weight/data rights remain untested; no cloud fallback is assumed.
6. **Differentiation and maintenance:** native workflows and existing companions may already satisfy the need for less effort. No claim of an empty market.

## 7. Smallest acceptance experiment — proposed, not executed

Use one voluntarily supplied, rights-appropriate project and its normal workflow. First document the operator's existing reopen-and-handoff result. Then compare the relevant existing companion and, only where needed, a bounded adapter prototype. Work on copies in approved locations.

Acceptance requires unchanged originals; correctly identified source/revision; complete expected package or explicit blockers; successful separate-location restore; creator-approved audible result; and lower total human effort after review, repair and maintenance. Unrequested network traffic, silent media loss, unsupported green checks or any unauthorized external action fails the experiment regardless of speed.

**Current verdict:** a record-level companion is coherent, but a new full super-app is **not justified for implementation yet**. This is a preliminary decision from the current evidence, not a final negative verdict on every OSS route or the remaining sweep.
