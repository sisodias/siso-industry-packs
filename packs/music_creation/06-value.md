# Value case — useful favour first, commercial thesis unproven

**As of 2026-09-13.** Verdict: **NO to commissioning a broad music super-app now.** Preserve the existing creative workstation and compare a narrow, local project/release handoff workflow against existing tools. A favourable result could justify a bounded assembly; this research does not establish it yet. [analysis]

NM's surviving scope is a low-priority consumer favour, not an admitted commercial client delivery. The original detailed specification is unavailable. Source: https://github.com/sisodias/siso-industry-packs/blob/main/packs/music_creation/README.md [analysis]

## 1. Stack tax: catalogue cost is not money returned

The arithmetic in [03-companies.md](03-companies.md) gives **USD 1,457.87/year** on a normalised recurring list/renewal basis, **USD 383** of initial licences/fees, and **USD 1,790.87** in first-year cash using the stated BandLab introductory price. These are the distinct priced tools in the stage comparison, with duplicates counted once. The basket deliberately contains competing DAWs and overlapping services, so it is an **overbuy ceiling**, not a recommended stack or NM's actual spending. [analysis; all individual price URLs and regional caveats are retained in Stage 3]

| Cost/benefit term | What this research establishes | What it does not establish |
|---|---|---|
| Existing DAW, plug-ins and sample catalogue | Their creative function should normally remain in place. [analysis] | No cancelled DAW/plugin/sample bill is evidenced. |
| Notion/Airtable planning subscriptions | Their listed one-seat comparison prices total **USD 360/year**. [analysis; vendor inputs: https://www.notion.com/pricing ; https://airtable.com/pricing] | NM may use neither, may use free tiers, or may need them for other work. This is not a claim that USD 360 is removable. |
| Distribution, rights administration and payment fees | They correspond to external relationships and services, not just local software screens. [analysis; vendor boundaries: https://artists.spotify.com/get-started ; https://www.songtrust.com/pricing ; https://stripe.com/pricing] | No assumption that a local app eliminates these fees or recreates the collection/payment network. |
| Saltado catalogue baseline | Vendor offers a free local catalogue and an early-access **USD 44 one-time** Pro tier. [vendor] https://www.saltadosessions.com/ | No evidence that a custom catalogue is better, or that replacing a one-time purchase provides recurring savings. |
| SISO-hosted product service | The proposed architecture includes **no SISO server deployment**. [analysis] | This does not make electricity, storage, maintenance, packaging, support or user time free. |

**Verified cancelled software spend: null. Annual operating cost: null. First-year migration/change cost: null. Realised net cash saving: null.** These are missing measurements, not zero-valued measurements. [analysis]

The public SISO observed-value model requires this distinction. It separates cash from capacity, requires review/rework costs and forbids converting list prices, repository stars or hypothetical adoption into observed value. Source: https://github.com/sisodias/great-library-of-siso/blob/main/research/industries/source/intelligence/agency/economics/observed-value-model.json [analysis]

## 2. The wedge: one trustworthy handoff, not all of music

The proposed entry point is **prepare and recover the exact project/release handoff**: identify the native project and its referenced media; retain the source/receipt evidence; associate a reviewed bounce with the right revision; record contributor approvals; and export the selected package without changing the original project. [analysis]

This is a plausible continuity problem, supported by particular historical complaints and current packaging documentation. It is **not measured pain for NM**. Ableton's documentation makes media collection an explicit operation and excludes third-party plug-ins; the Stage-1 version-coordination complaint shows why a file named “V3” is not a complete agreement or review trail. [vendor] https://help.ableton.com/hc/en-us/articles/209775645-Collect-All-and-Save [practitioner] https://forum.ableton.com/viewtopic.php?t=245828

The first comparison must include the current DAW's collection/export tools, an existing backup route and Saltado—not just an intentionally fragmented expensive basket. A separate “AI generation” button is not differentiation if an existing tool already performs NM's desired transformation. [analysis; comparator: https://www.saltadosessions.com/]

## 3. Hours returned per week — unmeasured

There is no observed NM task frequency, baseline duration or assisted result. Therefore the current estimate is **null / unmeasured**, not an invented two-hour or ten-hour saving. The ten workflow rows define measurement units; they do not pretend to be a timesheet. [analysis; workflow: https://github.com/sisodias/siso-industry-packs/blob/main/packs/music_creation/02-workflow.json]

For each comparable task class, measure:

```
weekly capacity hours = sum over task classes of
  observed weekly count ×
  (baseline active human minutes
   - assisted active human minutes
   - extra review/rework/exception minutes) / 60
```

Keep human time and unattended processing time separate. A GPU finishing sooner is not automatically an hour returned to the artist. Count later recovery work, incorrect tags, failed imports and clarification messages against the assisted route. Retain the exact baseline files and acceptance criteria so a second reviewer can reproduce the comparison. [analysis]

A proposed pilot uses one real track and its next relevant handoff, then matched tasks from another project if available. Record asset search, repeated metadata entry, package preparation, restore effort, review ambiguity and corrections. No sample count in this proposal establishes statistical confidence; extend measurement until its uncertainty is explicit. [analysis]

Capacity only becomes cash if reduced spend, reduced paid labour or attributable contribution margin is actually observed. A hobbyist enjoying more creative time may value the result without any cash saving; preserve that goal rather than manufacturing a business ROI. [analysis; value model source above]

## 4. Migration cost — retain reversibility

| Migration item | Work that must be priced from the real device [analysis] | Why it cannot be assumed free |
|---|---|---|
| Inventory and permissions | Identify OS/architecture, DAW versions, plug-ins, media locations, account permissions and available storage. | None were inspected for NM. |
| Reference/import mapping | Map work/recording identities, selected messages, receipts, contributor records and release data. | Existing filenames and spreadsheet columns may not agree. |
| Media checkpoint | Copy a closed or explicitly quiescent project; resolve missing references; retain originals. | Active DAW writes and proprietary dependencies can make an apparent copy incomplete. |
| Agreement and release review | Confirm who owns which rights, which revision was approved and which destination accepted what. | A populated field is not a signed agreement or platform acknowledgement. |
| Restore and exit test | Restore to an approved alternate location; verify rendered content and metadata; export the binder's plain files/JSON/CSV. | A successful backup command does not prove a useful restoration. |
| Training and support | Let the operator repeat the task without the implementer; record ongoing exceptions. | The second support session is a real cost, not an implementation footnote. |

The honest cost equation is:

```
first deployment cash cost = measured implementation/packaging labour
                          + measured inventory/migration/validation labour
                          + required incremental hardware/storage/licences
                          + measured first-period support
```

Every input is currently **null**. Do not assign a professional hourly rate, billable volume or budget to NM. Perpetual tools already owned are sunk purchases; moving away from them does not refund the price. [analysis]

## 5. Local resource economics

The core binder should not require a GPU: its proposed work is local records, hashing, file inspection and explicitly requested processes. This is a design boundary, not a benchmark proving a minimum RAM figure. Model-heavy generation is optional and excluded from the base assembly. [analysis]

The source evidence shows why “runs locally” needs qualification. AudioLDM2's README describes approximately **20 GB RAM** for its MPS route. The audited ACE-Step repository describes an **8 GB VRAM** reduced-memory configuration; that is not a guarantee for every model or track. Basic Pitch's README documents platform/runtime-specific installation constraints. These are upstream statements, not measurements on NM's laptop. [vendor] https://github.com/haoheliu/AudioLDM2 ; https://github.com/ace-step/ACE-Step ; https://github.com/spotify/basic-pitch

A storage example can be calculated without inventing market costs. **Synthetic engineering fixture, not NM's library:** a three-minute, 48 kHz, 24-bit stereo render occupies `48,000 × 3 × 2 × 180 = 51,840,000` audio bytes before container overhead. Twenty-four stereo stems plus one stereo master therefore contain about **1.296 decimal GB per render set**; five independent copies contain about **6.48 GB**, before DAW projects, plug-ins, samples, model weights or deduplication. Compression/deduplication savings are unmeasured. [analysis]

Actual device cost and second-copy capacity require the real library. A large commercial sound library alone can dominate storage: Native Instruments lists approximately **320 GB** for the complete Komplete Standard installation. That is a vendor example, not a requirement of this proposed binder. [vendor] https://www.native-instruments.com/products/komplete-standard

For a single deployment, quote separately: device qualification; application/runtime installation; additional free space; backup destination; first model download; CPU/GPU time; and ongoing maintenance. The full installed cost remains **unmeasured**, even where upstream code is available without a purchase price. [analysis]

## 6. Vertical economics and the second deployment

**Eligible operator population: unknown.** The eight workflow segments are analytical categories, not a census. Music-streaming account totals, all musicians, all DAW users or all hobbyists would not establish how many laptop-based beatmakers have this exact handoff problem and will migrate. No revenue forecast or population-times-list-price market size is supported. [analysis]

The reusable part of a second deployment is the researched component selection, package recipe, schema, import/export contracts and tests. What repeats is device compatibility, library inventory, permissions, agreement mapping, user training, restore verification and support. [analysis]

```
second deployment cost = shared build maintenance allocation
                       + device-specific installation and qualification
                       + data-specific migration and validation
                       + operator training and support
```

This cost is not zero and cannot yet be priced. A consumer segment may still justify reuse at scale, but the required evidence is eligible operators × demonstrated unmet need × attainable adoption, minus measured delivery/support costs—not the number of GitHub stars or repos collected. Low ability to pay alone is not a rejection; absence of a differentiated useful mechanism is. [analysis; observed-value-model source above]

## 7. Falsifiers and decision gates

Reject the broad-build thesis if the current DAW plus an existing catalogue/backup route completes the target task with comparable effort and quality; if NM's real request is only an existing stem-separation feature; if review/rework offsets the saved entry/search time; if the proposed integration requires a device upgrade the benefit does not justify; or if ongoing consumer support consumes the value. [analysis]

Stop a pilot regardless of apparent time savings if it corrupts or overwrites a project, loses provenance, silently changes an agreement, leaks private audio/messages, submits a release without approval or mistakes an estimated statement for settled money. These are acceptance boundaries, not events observed in this research. [analysis]

**Decision now:** retain this as a sourced reuse pack and a narrow validation option. Do not build a new DAW, train a music model, deploy a SISO-hosted service, promise royalty collection, or promote the consumer favour above business work. A later affirmative build decision needs the actual task/device and a comparative outcome—not another more impressive architecture diagram. [analysis]

## Value ledger

```json
{
  "as_of":"2026-09-13",
  "evidence_class":"analysis",
  "comparison_basket_usd_year":1457.87,
  "comparison_basket_first_year_usd":1790.87,
  "comparison_basket_is_nm_spend":false,
  "verified_cancelled_software_spend":null,
  "annual_capacity_hours":null,
  "annual_operating_cost":null,
  "first_year_change_cost":null,
  "first_year_net_cash":null,
  "eligible_operators":null,
  "second_deployment_cost":null,
  "status":"unmeasured",
  "verdict":"NO broad build now; compare a narrow local handoff workflow against existing tools"
}
```
