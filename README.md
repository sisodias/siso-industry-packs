# SISO Industry Packs

Deep-research output for every industry SISO is mapping. One folder per industry; each
holds the seven-stage research pack an agent produces.

**Prompts to run the research:** https://siso-superapp-forge.pages.dev

## What a pack is

For one industry: the specific operator, their working day, every commercial tool that owns
a piece of it, the best open-source software on the planet for each piece, how those pieces
assemble into one super-app, and why that operator would switch.

| Stage | File |
|---|---|
| Summary | `00-SUMMARY.md` |
| The person | `01-person.md` |
| The workflow | `02-workflow.md` |
| The companies (Tier 1 + Tier 2) | `03-companies.md` |
| Open-source candidates | `04-oss-candidates.md` |
| The assembled super-app | `05-superapp.md` |
| The value case | `06-value.md` |

## Quotas

Every pack must report actual counts. Below these it is incomplete:

| | Minimum |
|---|---|
| GitHub repos examined | **100** |
| Tier-1 companies (big players) | **10** |
| Tier-2 offerings (small operators) | **10** |
| Quoted practitioner complaints, with links | **8** |
| Workflow stages mapped | **6–12** |

## Industries (26)

| Industry | Name | Priority | Kind | Client | Status |
|---|---|---|---|---|---|
| [`accounting_firms`](packs/accounting_firms/) | US small accounting firms | high | business | — | `queued` |
| [`aviation_parts_distribution`](packs/aviation_parts_distribution/) | Aircraft parts distribution & AOG sourcing | high | business | — | `queued` |
| [`car_rental`](packs/car_rental/) | Car rental operators (independent / small fleet) | high | business | existing clients + possible NM lead | `queued` |
| [`gyms_fitness`](packs/gyms_fitness/) | Gyms, studios and independent fitness operators | high | business | NM (Nick) | `queued` |
| [`it_services_msps`](packs/it_services_msps/) | US small managed IT service providers | high | business | — | `queued` |
| [`law_firms`](packs/law_firms/) | Law firms | high | business | — | `queued` |
| [`marketing_social_media_agencies`](packs/marketing_social_media_agencies/) | US marketing and social-media agencies | high | business | — | `queued` |
| [`recruiting_staffing`](packs/recruiting_staffing/) | US recruiting and staffing agencies | high | business | — | `queued` |
| [`trading`](packs/trading/) | Independent traders and small trading desks | high | business | SISO internal (Polymarket research factory) + prospective | `partial` |
| [`youtube_creators`](packs/youtube_creators/) | YouTube creators and faceless-content operators | high | business | Tristan Grech (SUMERA) — access granted 2026-09-13 | `queued` |
| [`cannabis_dispensary`](packs/cannabis_dispensary/) | Cannabis dispensaries and delivery | medium | business | LC | `queued` |
| [`community_owners`](packs/community_owners/) | Community owners and paid-community operators | medium | business | — | `queued` |
| [`construction`](packs/construction/) | US small construction contractors | medium | business | — | `queued` |
| [`ecommerce`](packs/ecommerce/) | US small ecommerce merchants | medium | business | — | `queued` |
| [`events_management`](packs/events_management/) | Event management companies and promoters | medium | business | BYK (BykonzYard) | `queued` |
| [`healthcare_medical_practices`](packs/healthcare_medical_practices/) | US ambulatory medical practices | medium | business | — | `queued` |
| [`hospitality`](packs/hospitality/) | US small hotels and lodging operators | medium | business | — | `queued` |
| [`insurance_agencies`](packs/insurance_agencies/) | US independent insurance agencies | medium | business | — | `queued` |
| [`real_estate`](packs/real_estate/) | US real-estate brokerages | medium | business | — | `queued` |
| [`restaurants`](packs/restaurants/) | Independent restaurants and small groups | medium | business | AC | `queued` |
| [`saas_base_stack`](packs/saas_base_stack/) | SaaS base stack (horizontal template layer, not a vertical) | medium | horizontal | — | `queued` |
| [`education_training`](packs/education_training/) | US adult vocational and continuing-education providers | low | business | — | `queued` |
| [`logistics_freight`](packs/logistics_freight/) | US logistics and freight service firms | low | business | — | `queued` |
| [`mortgage_brokers`](packs/mortgage_brokers/) | US mortgage brokerages | low | business | — | `queued` |
| [`music_creation`](packs/music_creation/) | Music creators and recording artists | low | consumer | NM | `queued` |
| [`property_management`](packs/property_management/) | US residential property managers | low | business | — | `queued` |

## Shared registries

| File | What |
|---|---|
| `registry/industries.jsonl` | The index. A pack not in it is invisible. |
| `registry/bank-submissions.jsonl` | **New** repos found (not already in the bank), tagged with a capability, queued for [`siso-repo-bank`](https://github.com/sisodias/siso-repo-bank). |
| `registry/corrections.jsonl` | Findings that contradict an existing SISO record — dead project, licence change, superseded repo. |

## Source inventories these packs build on

| Repo | What |
|---|---|
| [`siso-repo-bank`](https://github.com/sisodias/siso-repo-bank) | 23,778 rated repos, 51 capability tags, 126 best-per-capability, 3,010 product bases |
| [`siso-component-bank`](https://github.com/sisodias/siso-component-bank) | 8,538 UI components, 6,212 with source |
| [`great-library-of-siso`](https://github.com/sisodias/great-library-of-siso) | The public registry — 50 Works, 17 Foundry industry records |
| [`siso-foundry`](https://github.com/sisodias/siso-foundry) | The pipelines that produced the banks and the industry records |

## Contributing a pack

1. Copy the industry's prompt from https://siso-superapp-forge.pages.dev
2. Run it in ChatGPT with the GitHub connector on, stage by stage.
3. Replace the placeholder files in `packs/<slug>/` with the real output.
4. Update that industry's row in `registry/industries.jsonl` to `status: complete` with the
   real counts and the wedge.
5. Append new repos to `registry/bank-submissions.jsonl`, contradictions to
   `registry/corrections.jsonl`.

Method and doctrine live in `SISO_Agency/frameworks/superapp-forge`.

_Generated 2026-09-13_
