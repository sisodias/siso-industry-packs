# The assembled super-app — local evidence, decisions and review

Research cut: 2026-09-13. **[analysis] Architecture proposal, not implemented software.** The first deliverable is a supplied-statement import and review workflow. No live broker integration, account access, model inference, installation or deployment was performed for this pack.

## Preserve the earlier thesis

[analysis] The supplied brief identifies the prior SISO conclusion as a trader operating workflow, not a price-prediction product, and MiroFish as a scenario module rather than the platform. This design extends that direction with an operator, a ten-stage workflow, incumbent comparison and falsifiable value case. The private prior report was not independently reopened; its test claims remain attributed prior evidence. Public continuity: [trading entry](README.md). No private research corpus or runtime material is copied here.

## The spine: six linked objects, not six competing databases

[analysis] Use the six proposed objects in [02-workflow.md](02-workflow.md): **Instrument, EvidenceItem, ResearchCase, ExperimentRun, TradePlan, AccountEvent**. Their purpose is an explicit cross-tool identity and provenance contract. They are not new application code or a completed schema migration.

[analysis] Reuse the journal base's existing application/database stack. Proposed authority: one local PostgreSQL-backed write path for imported account-event references, case/plan links and review state; original source files live in a local immutable-by-policy evidence vault. DuckDB contains disposable analytical projections of accepted exports. Beancount/Fava are optional reviewed export/read surfaces, not additional writers to the account-event store. The broker remains authoritative for its own statements and execution state.

[analysis] Before adding tables or a sidecar, inspect the selected revision's existing import, trade-grouping and note models. Extend those models only where the cross-tool link cannot be represented safely. A separate six-object store that duplicates every journal trade would recreate the very reconciliation problem this product is meant to solve.

## Component map and selection boundaries

Selections are provisional technical choices from [the 110-row review](04-oss-candidates.json), not performance winners or admitted dependencies. Source capability statements are **[vendor/project-owner]** at the linked repositories; integration decisions and comparisons are **[analysis]**.

| Workflow | Chosen existing component | What SISO would add, not yet written | Why it provisionally beats the runners-up |
|---|---|---|---|
| W01 source capture; W03 case notes | [TradeTally](https://github.com/GeneBO98/tradetally) existing journal/note surface; local file vault | Source locator/hash, original-versus-review versions, case links and consented import adapter. | Start with a working journal product rather than a new generic UI. TradeNote remains the nearest product comparison; a spreadsheet wins if the participant already uses it effectively. |
| W02 statement instrument/source normalization; W08 reconciliation | [ibflex](https://github.com/csingley/ibflex) for supplied Flex XML | Broker-to-spine identifier mapping; warning/error receipt; overlap/duplicate/correction handling; exceptions requiring human review. | It parses the actual initial artifact. `ofxtools`/`libofx` solve OFX; live `ib_async` solves a different, more consequential interface. |
| W02 optional filing evidence | [EdgarTools](https://github.com/dgunning/edgartools) | Cache/source/as-of references and extraction-review link to ResearchCase. | Rich filing structure is useful when needed; `sec-edgar-downloader` should win instead if download-only is sufficient. |
| W03/W04 optional reproducible research | [marimo](https://github.com/marimo-team/marimo) and [DuckDB](https://github.com/duckdb/duckdb) | Read-only dataset exports, experiment manifest, result-artifact links and process isolation. | Reuse existing notebooks/querying. Do not build a new editor or hosted warehouse; ordinary notebook/CSV workflows remain valid alternatives. |
| W04 optional event-driven experiments | [LEAN](https://github.com/QuantConnect/Lean) | Dataset/event adapter, cost/fill assumptions and reproducibility receipt. | Event-driven experiment contract matches the design. [NautilusTrader](https://github.com/nautechsystems/nautilus_trader) is a close runner-up; choose after same-fixture local evaluation, not star count. Do not install both by default. |
| W05 optional allocation research | [PyPortfolioOpt](https://github.com/PyPortfolio/PyPortfolioOpt) | Explicit input/constraint snapshot and result review; separate operational limits. | Narrow library instead of an institutional risk platform. Riskfolio-Lib/skfolio remain alternatives; optimization is not execution authorization. |
| W06 actual execution | Existing broker interface retained; **no automated adapter enabled in pilot** | Later: separately authorized order-state, idempotency, limits, signing and recovery controls. | A read-only journal does not need trading credentials. Selecting a broker SDK now would add risk before proving the wedge. |
| W07 status/freshness | Existing broker/feed surface and local exception view | Event/receipt timestamps, stale flags and laptop-resume reconciliation. | No new alert SaaS or unsupported promise of uninterrupted local service. |
| W09 reconciled review | [TradeTally](https://github.com/GeneBO98/tradetally) | Link accepted events to original plan/evidence; expose unknown/unmatched state; preserve note export. | Closest fit to the proposed review wedge. [Ghostfolio](https://github.com/ghostfolio/ghostfolio) and [Portfolio Performance](https://github.com/portfolio-performance/portfolio) are stronger wealth/investor alternatives, not identical trade journals. |
| W10 optional accountant export | [Beancount](https://github.com/beancount/beancount) plus [Fava](https://github.com/beancount/fava) | Reviewed mapping/export receipt and unresolved-item pack. | Inspectable text and existing reader; Ledger/hledger/GnuCash or the accountant's incumbent can replace this choice. No tax conclusion is automated. |
| Prediction-market extension across W02/W03 | [Official Polymarket Python SDK](https://github.com/Polymarket/py-sdk), public-read methods only | Question/condition/outcome identity and resolution-source links. | One current official language route rather than archived clients or duplicated TypeScript/Python adapters. Venue access and terms remain external. |
| Optional scenario extension | [SISO MiroFish fork](https://github.com/sisodias/MiroFish), **STUDY / disabled** | A genuinely local dependency route, resource tests and evaluation would be needed before integration. | Preserve the prior module without making it the platform or claiming its documented cloud dependencies are local. |

## The glue is real engineering work

[analysis] These are proposed obligations and test cases, not completed features.

**Import completeness.** [vendor] [ibflex](https://github.com/csingley/ibflex/blob/master/README.rst) skips unknown XML fields with warnings by default and documents date/section constraints. [analysis] Capture those warnings, preserve original XML, count source and accepted records by type, and hold an import in an incomplete state when unsupported fields may matter. “Parsed without throwing” must not mean “reconciled.”

**Identity and precision.** [analysis] Retain broker account/contract/execution identifiers alongside internal IDs. Use explicit decimal quantity/price/fee/currency conventions; avoid converting distinct currency amounts to an unlabelled number. Preserve event time, source reporting time and local capture time. Instrument aliases and corporate actions require versioned mappings, not string replacement across history.

**Overlap and corrections.** [analysis] Hashing an entire file detects the same file twice but does not deduplicate overlapping reports. Build an event-level source-identity strategy and an explicit ambiguous-match queue. Retain partial fills, cancellations and superseding corrections. A plan, order, execution and journal group are separate concepts. Never create a balancing entry merely to eliminate an unexplained difference.

**Authority.** [analysis] A research result or chat message cannot submit an order. Approval attaches to a particular plan revision and expires when its relevant inputs change. The proposed pilot has no broker/wallet credentials at all. A later execution profile would need a separately reviewed state machine, confirmation, limits and reconciliation path; it is not authorized by this document.

**Research isolation.** [analysis] Notebooks and engines execute code; imported notebooks/strategies are not trusted data. Run optional experiments in a separate process/profile with a read-only export and no broker credentials or unrestricted account-vault access. Record code/data/environment revisions. Pin and review dependencies before installation; no downloaded code was executed in this research pass.

**Privacy and network behavior.** [vendor] The [TradeTally README](https://github.com/GeneBO98/tradetally/blob/main/README.md) names optional AI/data providers and browser-side logo fallbacks. [analysis] Disable outbound enrichment, AI, telemetry and remote image fallbacks in the strict-local core until a network audit verifies the intended behavior. Localhost binding still needs authentication, origin/CSRF controls and safe file handling; it is not a security audit result.

**Files and recovery.** [analysis] Preserve original evidence, separate generated exports from originals, enforce import size/type/path limits, and test restoration to a clean local profile. Proposed encrypted backup goes to user-controlled storage, not SISO. A backup job reporting success is not a restore test. Do not store passwords, broker tokens or private account files in GitHub.

**Licence and entitlement.** [analysis] Choose on technical fit while recording accurate rights. Before distribution, review the exact edition, subdirectories, dependencies, notices and data/service terms. This is not an automatic licence-based technical rejection, nor permission to ignore obligations. Example: [vectorbt's actual licence](https://github.com/polakowo/vectorbt/blob/master/LICENSE.md) has a Commons Clause; the software's root label cannot be treated as an unrestricted blanket grant.

## Architecture sketch — proposed, not running

```text
USER'S LAPTOP

User-selected statement / message export / source file
                     |
             local import boundary
       raw-file hash + schema/warning receipt
                     |
          ibflex / bounded source adapter
                     |
     one journal-backed write authority (PostgreSQL)
   Instrument -- EvidenceItem -- ResearchCase -- TradePlan
                         |             |            |
                  original-file vault  |       AccountEvent
                                       |
                                  ExperimentRun
                                       |
            +--------------------------+------------------+
            |                          |                  |
       TradeTally UI           accepted read-only   reviewed accounting
   notes / review / exceptions      export             export
                                       |                  |
                                    DuckDB           Beancount -> Fava
                                       |
                               optional isolated
                                marimo / ONE engine

External, optional and permission-specific:
  public filings / licensed data / broker / prediction-market venue
  Network fetches are separate from local storage and local processing.
  No SISO-hosted database, worker, relay, model server or account proxy.
```

[analysis] This sketch expresses logical ownership, not an implemented physical schema. It deliberately avoids making every component a resident service. The first candidate profile has the existing journal application/database plus a transient importer; analytics, notebooks, engines, accounting reader and scenario model are optional profiles added only when the operator needs them.

## Local deployment and resource plan

| Profile | Proposed contents | Resource / cost status | Admission gate |
|---|---|---|---|
| Core, supplied files | Journal application, its PostgreSQL, local evidence vault, transient XML importer. | **Measured RAM/CPU/disk floor null.** SISO hosting spend is absent by design; user device, electricity, backup and support costs are not zero. | Offline startup, no unauthorized outbound calls, import/review/restore fixtures and usable performance on the participant's actual laptop. |
| Research | Core plus DuckDB and optional marimo; one selected engine only when needed. | Dataset size and engine build/runtime costs unmeasured. No claim that an 8GB laptop or any particular OS is already supported. | Bounded dataset benchmark and isolation test; can remove profile without damaging core data. |
| Accounting review | Approved export plus Beancount/Fava, opened on demand. | Resource floor and accountant acceptance unmeasured. | Exact event-to-export trace and accountant-approved treatment. |
| Scenario simulation | MiroFish or another later qualified module. | **Not admitted**: current documented cloud dependencies and unmeasured compute. | Genuine local route, network/resource audit and task-specific evaluation. |
| Automated live trading | Not in the pilot. | No price, reliability or readiness claim. | Separate explicit authority and engineering/operational qualification. |

[analysis] A laptop can sleep, lose its network, close its lid or run out of disk. Therefore this design cannot promise unattended 24/7 execution or alert delivery. Mark data stale, disable consequential actions and reconcile on resume. Do not evade the local-first constraint by quietly introducing a SISO VPS or an always-on cloud agent.

[analysis] Deployment cost is a measurement ledger, not an invented fixed price: installation/configuration time + migration/reconciliation time + test/acceptance time + user-side hardware/backup/power increment + ongoing support/updates + any chosen external feed/service charges. Every numerical input remains null until observed; [06-value.md](06-value.md) applies the value model without replacing unknowns with zero.

## What OSS does not settle — nine gaps

[analysis] These are unresolved gaps in this design, **not universal claims that no OSS solution exists anywhere**.

| ID | Gap | Evidence needed to close it |
|---|---|---|
| G01 | Specific operator demand and baseline | Consented workflow observation, existing workbook/journal, actual bills and comparative outcome. |
| G02 | Data, brokerage and venue entitlements | Applicable account/feed/region terms, complete data requirements and current compatibility. |
| G03 | Complete event semantics and reconciliation | Fixtures for overlap, partial fills, fees, FX, corrections, exercise/assignment and unknown fields. |
| G04 | Safe consequential execution | Separate authority, limits, signing, order-state/idempotency and recovery evidence; not part of pilot. |
| G05 | Accounting/tax treatment | Jurisdiction-specific professional review, approved mapping and source-linked exceptions. |
| G06 | Laptop footprint and reliability | Actual OS/architecture, RAM/CPU/disk measurements, sleep/network/storage failure tests and clean restore. |
| G07 | Verified local privacy and scenario independence | Network audit; disabled unwanted outbound calls; no unsupported claim that MiroFish cloud dependencies have been removed. |
| G08 | Maintenance, adoption and exact rights | Issue-response/bus-factor assessment, correct package dependence, dependency/security review and route-specific rights. |
| G09 | Migration economics and repeat deployment | Export/round-trip fidelity, accepted historical reconciliation, support hours and measured second-install cost. |

## Decision and reusable output

[analysis] **Proceed only to a bounded read-only import-to-review pilot; do not approve the full super-app or autonomous trading.** Lift the journal, parsers and readers; build only justified cross-tool identity, evidence, exception and approval glue. The brief's rough “5% differentiated glue” is a direction, not a measured implementation fraction or cost estimate.

[analysis] The candidate comparison is a potential input to the brief's GQ-004 Best Software Primitive question; the six-object contract, component boundaries and repeat-deployment tests are potential input to GQ-013 A Useful Reusable Building Set. This pack creates no Library Work, Release, Snapshot or accepted answer. The [Great Library model](https://github.com/sisodias/great-library-of-siso/blob/main/README.md) keeps catalog identity, distribution and actual implementation distinct.
