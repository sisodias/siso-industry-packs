# 04 · OSS candidate audit — incomplete, 12 source reviews

Observed **2026-09-13 UTC**. This audit does **not** meet the 100-repository floor. Five ADOPT verdicts are provisional prototype selections, not production admissions. No upstream code was executed, built, deployed or tested with client records.

## Evidence and counting rules

[vendor] Every repository below was read through the GitHub connector: repository metadata, README and the actual root license file or its header/preamble, plus a commit-search result. Stars are dated observations. The long GPL/LGPL files were sampled, not a whole dependency/subdirectory legal audit. [analysis] Latest commit means **latest returned indexed commit search**, not a verified live default-branch HEAD. Do not replace this qualifier with a stronger claim.

[analysis] Scores are fit / liftability / health / adoption / integration, each 0–5 when supported. Fit, liftability and integration are design judgments. **Health and adoption remain null**: issue response, bus factor, six-month activity and real dependents were not fully audited. Stars are not adoption. No numeric total or ranking fills those gaps.

[analysis] Bank reconciliation: the 126-row capability-top file was read, including WeasyPrint. Large bank/shelf/adoption access was incomplete. **WeasyPrint = ALREADY IN THE BANK; the other eleven = UNVERIFIED, not NEW.** Existing Foundry mention is not proof of bank membership. The requested binary label cannot honestly be supplied for those eleven yet. [Bank top source](https://github.com/sisodias/siso-repo-bank/blob/main/bank/bank_capability_top.jsonl), observed blob `876f053f1595e76789a7a21616c4d32671e6fc24`.

## Deduplicated source-review table

[vendor] Repository facts follow linked source/license evidence. [analysis] Verdicts, scores, tags and reuse choices are ours. `?` = null, not zero. All star observations: 2026-09-13.

| Repository / stars | Root/path license observation | Latest indexed commit/date | Scores F/L/H/A/I | Verdict; what it gives us | Bank |
|---|---|---|---|---|---|
| [frappe/erpnext](https://github.com/frappe/erpnext) — 39,179 | [GPL-3.0 license.txt](https://github.com/frappe/erpnext/blob/fe25746febc8731bbbc0880dcb18d528dcf08a63/license.txt) | [fe25746](https://github.com/frappe/erpnext/commit/fe25746febc8731bbbc0880dcb18d528dcf08a63), 2026-09-13 | 5/2/?/?/4 | **ADOPT** project/customer/purchasing/time/draft commercial base; retain ledger authority | UNVERIFIED |
| [InvoicePlane/InvoicePlane](https://github.com/InvoicePlane/InvoicePlane) — 3,139 | [MIT software, separate trademark and bundled CodeIgniter terms](https://github.com/InvoicePlane/InvoicePlane/blob/develop/LICENSE.txt) | [c5cf29c](https://github.com/InvoicePlane/InvoicePlane/commit/c5cf29ce27e9c4d8e8c800a617517f1d32cf1de1), 2026-09-08 | 3/2/?/?/2 | **STUDY** narrow quote/invoice sidecar; do not run duplicate financial authority | UNVERIFIED |
| [opf/openproject](https://github.com/opf/openproject) — 16,092 | [GPL-3.0](https://github.com/opf/openproject/blob/a6be9b2e376655655ba98537e08929905d9e8a37/LICENSE) | [a6be9b2](https://github.com/opf/openproject/commit/a6be9b2e376655655ba98537e08929905d9e8a37), 2026-09-13 | 4/2/?/?/3 | **STUDY** work packages/schedules/meetings; neither field truth nor contract authority | UNVERIFIED |
| [chatwoot/chatwoot](https://github.com/chatwoot/chatwoot) — 36,766 | [MIT outside enterprise/ and third-party exceptions](https://github.com/chatwoot/chatwoot/blob/develop/LICENSE) | [2f1ed80](https://github.com/chatwoot/chatwoot/commit/2f1ed80f894ed9a3eba636ebab90ca61deec110a), 2026-09-11 | 5/2/?/?/4 | **ADOPT** shared inbox/contact/thread surface; client owns external channels | UNVERIFIED |
| [docusealco/docuseal](https://github.com/docusealco/docuseal) — 18,512 | [AGPL-3.0](https://github.com/docusealco/docuseal/blob/master/LICENSE) plus [section 7(b) UI attribution](https://github.com/docusealco/docuseal/blob/master/LICENSE_ADDITIONAL_TERMS) | [11856a1](https://github.com/docusealco/docuseal/commit/11856a17ac0865128333a0ffe1fdfc44e4b8a982), 2026-09-07 | 4/3/?/?/4 | **ADOPT** linked core signing, not unverified free embedded/SSO/role features | UNVERIFIED |
| [paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) — 45,055 | [GPL-3.0](https://github.com/paperless-ngx/paperless-ngx/blob/dev/LICENSE) | [72ea38a](https://github.com/paperless-ngx/paperless-ngx/commit/72ea38ab126e92fb63d68b7f5d0e6d9abaafe589), 2026-09-12 | 3/2/?/?/3 | **STUDY** searchable archive; not immutable construction document control | UNVERIFIED |
| [IfcOpenShell/IfcOpenShell](https://github.com/IfcOpenShell/IfcOpenShell) — 2,783 | [LGPL-3.0 core](https://github.com/IfcOpenShell/IfcOpenShell/blob/v0.9.0/COPYING.LESSER); [README assigns GPL-3.0-or-later to Bonsai](https://github.com/IfcOpenShell/IfcOpenShell/blob/v0.9.0/README.md) | [23f3874](https://github.com/IfcOpenShell/IfcOpenShell/commit/23f3874de19d398451f8926722dc33c21aff5b74), 2026-09-11 | 2/5/?/?/3 | **STUDY** optional IFC conversion/diff and BCF/IDS; no automated quantity authority | UNVERIFIED |
| [manuvarkey/GEstimator](https://github.com/manuvarkey/GEstimator) — 72 | [GPL-3.0](https://github.com/manuvarkey/GEstimator/blob/master/LICENSE) | [0927aa7](https://github.com/manuvarkey/GEstimator/commit/0927aa789f18403ea01fcdf5bf6765f9ae0ffde8), 2025-08-18 | 3/1/?/?/2 | **STEAL** measurement/rate-analysis pattern only; GTK desktop and bundled DSR books are not a validated US VPS module | UNVERIFIED |
| [braedonsaunders/bidwright](https://github.com/braedonsaunders/bidwright) — 49 | [AGPL-3.0, README specifies only](https://github.com/braedonsaunders/bidwright/blob/main/LICENSE) | [6f33cdd](https://github.com/braedonsaunders/bidwright/commit/6f33cdd41d1e3e1aafd31a73f684980b552ffd96), 2026-09-10 | 4/2/?/?/3 | **STUDY** linked bid/takeoff/assembly/revision patterns; provider/agent autonomy not admitted | UNVERIFIED |
| [joniles/mpxj](https://github.com/joniles/mpxj) — 345 | [LGPL-2.1](https://github.com/joniles/mpxj/blob/master/LICENSE), separate third-party terms | [ac7aa7b](https://github.com/joniles/mpxj/commit/ac7aa7b8f3bc90efc08c36757bc0c39b37b2c674), 2026-08-23 | 3/5/?/?/4 | **STUDY** MPP/P6 XER and other schedule exchange; import fidelity still untested | UNVERIFIED |
| [restic/restic](https://github.com/restic/restic) — 36,030 | [BSD-2-Clause](https://github.com/restic/restic/blob/master/LICENSE) | [ba802d4](https://github.com/restic/restic/commit/ba802d42b7294c98b62c16d1157ea3e80820c019), 2026-08-29 | 5/4/?/?/4 | **ADOPT** encrypted off-host backups/restore; app-consistent exports and client keys required | UNVERIFIED |
| [Kozea/WeasyPrint](https://github.com/Kozea/WeasyPrint) — 9,590 | [BSD-3-Clause](https://github.com/Kozea/WeasyPrint/blob/main/LICENSE) | [d21889a](https://github.com/Kozea/WeasyPrint/commit/d21889a799c760399b9e2cd06c8bc7ad5aec7144), 2026-09-10 | 4/5/?/?/4 | **ADOPT** HTML/CSS PDF packets from trusted templates; bound file/network/CPU access | **ALREADY IN THE BANK** |

## Reuse shape, resources and edition boundaries

[vendor] [ERPNext README](https://github.com/frappe/erpnext/blob/fe25746febc8731bbbc0880dcb18d528dcf08a63/README.md) describes the ERP application base. [analysis] Carry forward the Foundry read-oriented customer/project/time/invoice prototype, preserve incumbent accounting/contract authority, and benchmark its full framework/DB/worker footprint.

[vendor] [InvoicePlane README](https://github.com/InvoicePlane/InvoicePlane/blob/develop/README.md) distinguishes development Compose from production configuration. [analysis] Never deploy development defaults as production. Its narrower billing footprint may win a billing-only wedge, not this broader procurement/job spine.

[vendor] [OpenProject README](https://github.com/opf/openproject/blob/a6be9b2e376655655ba98537e08929905d9e8a37/README.md) distinguishes Community and Enterprise. [analysis] Carry forward administrative tasks/milestones only; add it only if ERP task views fail measured needs.

[vendor] [Chatwoot README](https://github.com/chatwoot/chatwoot/blob/develop/README.md) lists self-hosted omnichannel support. [analysis] Core inbox only; channel provider accounts, credentials, consent and transport fees are external dependencies, not local hosting features. Do not assume all enterprise functionality is free.

[vendor] [DocuSeal README](https://github.com/docusealco/docuseal/blob/master/README.md) lists Docker/SQLite with alternate DBs, local files, API/webhooks; SSO, roles, automated reminders, SMS verification and embedded signing/builder are Pro features. [analysis] Start with a linked core flow or price the required edition; prove authorization and webhooks before adoption.

[vendor] [Paperless README](https://github.com/paperless-ngx/paperless-ngx/blob/dev/README.md) warns about unencrypted data on the host. [analysis] OCR/search does not substitute for original-file hashes, revision identity, access control and retention policy. Optional, not another mandatory service.

[vendor] [IfcOpenShell](https://github.com/IfcOpenShell/IfcOpenShell/blob/v0.9.0/README.md), [MPXJ](https://github.com/joniles/mpxj/blob/master/readme.md), [GEstimator](https://github.com/manuvarkey/GEstimator/blob/master/README.md) and [Bidwright](https://github.com/braedonsaunders/bidwright/blob/main/README.md) expose construction-specific formats or estimating structures. [analysis] Batch/import modules belong behind file-size, CPU/memory and fidelity gates; desktop authoring and local AI stacks are not assumed to fit the small VPS.

[analysis] **No validated per-component or integrated resource floor exists in this audit.** Plan 16 GiB for evaluation budgeting; test an 8-GiB reduced profile rather than promising it. License is recorded accurately, not used to reject a candidate merely for copyleft; compliance and edition rights still require review before use. STEAL means study/lift an allowed pattern, not evade licensing.

## Search funnel and unfinished work

[analysis] Four initial GitHub connector queries produced **100 raw hits / 90 unique names**, including irrelevant projects: `construction estimating in:name,description,readme stars:>5` (25), `topic:construction` (30), `topic:ifc` (30), and `"field service" in:name,description` (15). The connector did not provide a star-sort argument; do not call these a star-ranked exhaustive sweep. Search-only names are not counted as examined.

[analysis] **No full round or dry round is complete.** Remaining work: for every workflow stage, query runnable apps, libraries, formats, bridges and registries across keyword/topic/protocol lanes; chase relevant dependencies/maintainers/awesome lists; deduplicate; review at least 100; then complete at least three recorded rounds and two consecutive successful zero-new-result rounds within a stated scope. Failures do not count as dry.

| Stage | Keyword lane A, planned | Topic lane B, planned | Format/protocol lane C, planned |
|---|---|---|---|
| W01 | contractor intake / shared inbox / site CRM | crm, customer-support | email MIME, SMS webhooks, vCard |
| W02 | construction survey / drawing markup / takeoff | construction, ifc, cad | PDF, DXF, IFC, BCF |
| W03 | BOQ / estimate assemblies / subcontract bids | construction-estimating, estimating | XLSX, IFC quantity sets, cost-code CSV |
| W04 | selections / contract packet / signing | document-signing, e-signature | PDF signatures, webhook events |
| W05 | procurement / subcontractor documents / delivery | inventory, procurement | purchase-order CSV/XML, document metadata |
| W06 | contractor scheduling / field dispatch | field-service, project-management | MPP, XER, MSPDI, iCalendar |
| W07 | daily logs / timesheets / receipts | field-service, timesheet | EXIF, CSV, offline sync events |
| W08 | change order / revision / approval records | construction, workflow | BCF, document revision hashes, signature events |
| W09 | progress billing / accounting connector | invoicing, accounting | UBL, invoice CSV, QBO authorized API |
| W10 | punch list / handover / warranty | facility-management, document-management | COBie, IFC, PDF manuals, archive manifests |

[analysis] Bank tags: workflow-orchestration (ERP/task/estimate patterns), email (inbox), pdf-documents (signing/archive/rendering), data-serialization (schedule/model exchange) and file-upload-storage (backup). These are reconciliation tags, not claims that the 51-tag vocabulary fully describes a construction app. Propose a separate `construction-estimating` domain tag and `aec-interoperability` domain tag; do not silently alter the frozen taxonomy.

[analysis] No verified NEW bank submissions or factual corrections are published. A missing path such as uppercase README is not a dead repository; a license badge mismatch is not proof of a license change. Complete source/version comparison before filing corrections.
