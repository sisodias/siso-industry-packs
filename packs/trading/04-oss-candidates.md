# OSS candidates — a wide collected pool, a bounded reviewed shortlist

Research cut: **2026-09-13**. Status: **partial**. This report separates discovery, documentation screening, technical selection and actual qualification. No application code was written, no candidate package was installed, no broker account was accessed and no candidate build was run.

## What the counts mean

| Evidence level | Actual count | What it does and does not establish |
|---|---:|---|
| Unique repositories with collected documentation/metadata | **435** | 430 in the [sealed collection](evidence/batched-collection-summary.json), plus five [supplemental records](evidence/supplemental-receipts.json); see [compact index](evidence/compact-index.json). Collection is not individual review. |
| Repositories comparatively screened in this report | **110** | The complete [JSON table](04-oss-candidates.json) records name, URL, dated stars, latest default-branch commit date, root licence metadata, BANK/NEW status, three provisional scores, two explicitly unknown scores, verdict and bounded role. Screening used the preserved documentation views; it is not 110 full code audits. |
| Provisional ADOPT selections across core and optional extensions | **10** | Proposed use of existing components for evaluation, not ten installed or accepted dependencies. |
| Repositories fully scored on all five requested axes | **0** | Robust health and current adoption assessment are not complete; those values are null rather than manufactured. |
| Candidate builds / integrated laptop tests | **0 / 0** | Earlier user-reported MiroFish tests are not new test evidence. |
| Proven consecutive dry discovery rounds | **0** | Three inherited rounds exist, but the two-dry-round stopping condition was not reached. |

[analysis] The minimum breadth of a hundred names has been surpassed at documentation-screening level, but **the full Stage-4 method has not been completed**. Therefore the registry must stay partial. The remaining 325 collected records are not silently promoted to reviewed candidates by this report.

## Source and reuse discipline

[vendor/project-owner] The [Repo Bank](https://github.com/sisodias/siso-repo-bank/blob/main/README.md) contains rated, liftable, adoption and product-shelf layers. The inherited pass read the small capability tables, filtered the large banks and preserved content hashes. Relevant receipts: [bank extraction](evidence/batched-bank-receipts.json), [product bases](evidence/compact-product-bases.md), [rated leads](evidence/compact-rated-bank-leads.md), [identity review](evidence/bank-identity-review.json).

[analysis] **ALREADY IN THE BANK** means a match to the four compared public layers, including verified aliases. **NEW** means no match in those layers. It does not mean the repository is absent from the unpublished 1.36-million-identity source database, every placement export or every historical SISO list. That narrower definition matters: a discovery label is not a claim to have searched inaccessible data.

[vendor/project-owner] Generic picks already exist: authentication `panva/jose`, browser/server search `nextapps-de/flexsearch`, logging `pinojs/pino`, workflow `PrefectHQ/prefect`, diagrams `mermaid-js/mermaid`. These are **bank leads**, not additional selections or fresh audits in this pack: [capability top table](https://github.com/sisodias/siso-repo-bank/blob/main/bank/bank_capability_top.jsonl). The [Component Bank](https://github.com/sisodias/siso-component-bank/blob/main/README.md) already covers the UI layer; no new UI-library sweep was performed.

## Search provenance and the method gap

[vendor/project-owner] The inherited [three-round query log](evidence/batched-search-rounds-1-3.json) includes keyword, topic and format/protocol searches, followed by maintainer and related-topic searches. Examples include trading journals, market-data topics, backtesting, FIX, Flex XML, OFX, XBRL and tax-lot formats. Results were limited to eight per query, so they are not an exhaustive search result set.

[analysis] The first pass also collected companies/workflow prerequisites out of the required report sequence. [03-companies.md](03-companies.md) records that correction rather than inventing a completed earlier freeze. This continuation adds no new repository discovery; it converts the existing pool into an explicit comparative review after completing the incumbent map.

[analysis] Further discovery must use the existing deduplicated repository IDs, paginate where appropriate, inspect useful dependency and maintainer leads, and log newly added relevant identities. Two genuinely consecutive no-new-candidate rounds are still needed; repeating a saturated top-eight query is not sufficient evidence that the domain is dry. One useful lead exposed by the selected parser's README is its related importer/analysis ecosystem; those links are leads, not extra reviewed repositories in the count.

## Scoring without invented precision

[analysis] Each row in [04-oss-candidates.json](04-oss-candidates.json) has a five-slot score vector **fit / liftability / health / adoption / integration**. Fit and integration are provisional judgments for the named bounded role, based on documentation rather than tested compatibility. Liftability rates a detachable library above an engine, service or whole application; it is not a reason to rebuild an application whose existing workflow already fits.

| Axis | Interpretation |
|---|---|
| Fit 0–5 | 0 unrelated; 1 historical/peripheral; 2 different segment; 3 useful extension; 4 close bounded match; 5 primary workflow match. |
| Liftability 0–5 | 0 unusable payload; 1 reference/pattern; 2 large application; 3 service/framework/application process; 4 detachable engine/CLI; 5 library/SDK. |
| Health | **null** pending issue-response, contributor concentration, dependency/security and release review. Commit totals alone do not earn a quality score. |
| Adoption | **null** pending correct current package identity and real dependence checks. Stars are recorded but never substituted for dependents. |
| Integration 0–5 | 0 no meaningful object match; 1 conceptual; 2 substantial translation; 3 plausible structured bridge; 4 documented near-fit needing adapter tests; 5 reserved for demonstrated contract-level compatibility. No row is awarded 5 here. |

[analysis] No aggregate ranking is computed with missing axes. The provisional choices can change after fixtures and qualified maintenance/adoption evidence. ADOPT means evaluate the existing component rather than rewrite its capability; STUDY means retain a comparison/reference, not add it to the default install; SKIP means not selected for this bounded use. No STEAL verdict is needed in this cut. Were it used, it would mean learning a design pattern and independently implementing necessary glue, not copying code without rights.

## Top ten selections and why they are not just the biggest repositories

| Repository | Bank status | Proposed verdict and role | Why this over the named alternatives [analysis] | Remaining decisive gate |
|---|---|---|---|---|
| [GeneBO98/tradetally](https://github.com/GeneBO98/tradetally) | NEW | ADOPT — primary journal application base. | It already offers journal/import/review surfaces, unlike assembling a fresh UI from analytics libraries. TradeNote is the nearest journal runner-up; Ghostfolio is more wealth-tracking shaped. | Exact broker fixture fidelity, export/backup recovery, remote-call controls, maintenance/security review, laptop footprint. |
| [csingley/ibflex](https://github.com/csingley/ibflex) | NEW | ADOPT — primary supplied-file Flex XML parser. | It speaks the initial broker artifact directly; OFX tools and live SDKs solve different interfaces. | Unknown-field warnings, report date/section restrictions, complete event and fee coverage, idempotent imports. |
| [duckdb/duckdb](https://github.com/duckdb/duckdb) | ALREADY IN THE BANK | ADOPT — optional rebuildable analytical projections. | Reuse embedded analytical queries rather than introduce a hosted warehouse. Keep journal/PostgreSQL write authority singular. | Snapshot lineage, decimal/time conventions and bounded memory on real export size. |
| [marimo-team/marimo](https://github.com/marimo-team/marimo) | ALREADY IN THE BANK | ADOPT — optional reproducible research surface. | Its versionable notebook approach is a useful experiment surface. JupyterLab/Jupytext remain bank/evidence alternatives, not additional reviewed rows in this 110-table cut. | Isolate arbitrary code, remove account secrets, preserve deterministic experiment receipts. |
| [QuantConnect/Lean](https://github.com/QuantConnect/Lean) | ALREADY IN THE BANK | ADOPT — optional event-driven experiment engine. | Fits an explicit event/result boundary. NautilusTrader is a strong runner-up, not a defeated implementation; a same-fixture comparison may reverse selection. Vectorbt is a different simulation style. | Fresh local build, data/fill/cost model fidelity, licence route, platform/CLI entitlement separation. |
| [PyPortfolio/PyPortfolioOpt](https://github.com/PyPortfolio/PyPortfolioOpt) | ALREADY IN THE BANK | ADOPT — optional allocation-research library. | A narrow research module instead of adopting an institutional risk platform. Riskfolio-Lib and skfolio remain close alternatives. | Input/covariance/constraint validation; never mistake an optimized allocation for an enforceable broker limit. |
| [dgunning/edgartools](https://github.com/dgunning/edgartools) | ALREADY IN THE BANK | ADOPT — optional filing evidence adapter. | Richer filing structure than download-only clients when the case genuinely needs it; sec-edgar-downloader may win for simple retrieval. | Access terms, source/as-of timestamps, extraction review and cached offline behavior. |
| [Polymarket/py-sdk](https://github.com/Polymarket/py-sdk) | NEW | ADOPT — optional public-read prediction-market adapter. | Official unified Python route aligns with the selected research/parser language. Old CLOB clients are archived; TypeScript SDK is an alternative, not a parallel mandatory dependency. | Pin API version and identities; prohibit signing/account writes in the research profile. |
| [beancount/beancount](https://github.com/beancount/beancount) | NEW | ADOPT — optional reviewed accounting export target. | Text-based inspectable output suits evidence handoff. Ledger/hledger/GnuCash may be better when already used by the operator/accountant. | Accountant acceptance, transaction semantics, round-trip checks and rights; no tax-certification claim. |
| [beancount/fava](https://github.com/beancount/fava) | NEW | ADOPT — optional local reader for that export. | Reuse an existing reader instead of build another accounting UI. It is not an extra source of account truth. | Bind locally, confirm privacy and export lineage; accounting extension not required for pilot. |

[vendor/project-owner] All metadata for these and the other 100 rows is in the [complete machine-readable table](04-oss-candidates.json) and the immutable [source bundle](https://github.com/sisodias/siso-industry-packs/tree/3ec8bee84ca4c378448f447a4e8b78a32500ee59/packs/trading/evidence). Scores and the comparisons above are **[analysis]**, not upstream endorsements.

## Critical source findings that change the blueprint

**The parser is not a completeness guarantee.** [vendor] The [ibflex README](https://github.com/csingley/ibflex/blob/master/README.rst) describes a standard-library parser with an optional network client. It says unknown XML elements/attributes are skipped with warnings by default, lists report date/section restrictions, and explicitly distinguishes reading reports from programmatic trading. [analysis] Preserve raw XML and warnings; do not mark an import complete when fields were silently dropped. Disable the optional network fetch in the first profile. The [actual root licence](https://github.com/csingley/ibflex/blob/master/LICENSE.txt) was read.

**A journal can still leak data outward.** [vendor] [TradeTally's README](https://github.com/GeneBO98/tradetally/blob/main/README.md) describes Vue/Node/PostgreSQL self-hosting, optional AI providers, paid-data-dependent features and browser logo requests to external providers. Its [actual licence](https://github.com/GeneBO98/tradetally/blob/main/LICENSE) is Apache-2.0. [analysis] Self-hosting does not prove offline/private behavior: disable external AI, telemetry, automatic enrichment and logo fallbacks until a network audit demonstrates the intended boundary.

**IBC was retired, not merely quiet.** [vendor] [IbcAlpha/IBC](https://github.com/IbcAlpha/IBC/blob/master/README.md) explicitly records retirement on **2026-09-01**. [analysis] A recently updated gateway Docker wrapper is not independent evidence that its underlying login automation remains actively supported. This is an argument for supplied statements first, not for weakening broker authentication.

**Current official SDKs and similarly named repositories are not interchangeable.** [vendor] The collected Polymarket originals are archived; current V2 and unified SDK records are in [supplemental evidence](evidence/supplemental-receipts.json) and [compact page 7](evidence/compact-07.md). The [Python SDK](https://github.com/Polymarket/py-sdk/blob/main/README.md) documents public, account and trading workflows, 0.x compatibility caveats and experimental perps APIs. [analysis] Use only the selected public-read surface. The bank's `dev-polymarket/clob-client-v2` is a different repository ID/owner from official `Polymarket/clob-client-v2`; a name resemblance is not an alias proof: [identity evidence](evidence/bank-identity-review.json), [non-official locator](https://github.com/dev-polymarket/clob-client-v2), [official locator](https://github.com/Polymarket/clob-client-v2).

**A bank licence label can hide an important condition.** [vendor] [vectorbt's actual LICENSE.md](https://github.com/polakowo/vectorbt/blob/master/LICENSE.md) is Apache-2.0 with Commons Clause, not plain Apache-2.0. [analysis] Record that accurately; the technical STUDY decision is based on role/simulation fit, not an automatic licence exclusion. Actual distribution and paid-service use still need a rights review before shipping.

**MiroFish is not a local-core replacement.** [vendor] The [SISO fork README](https://github.com/sisodias/MiroFish/blob/main/README.md) and [backend dependency list](https://github.com/sisodias/MiroFish/blob/main/backend/requirements.txt) describe LLM API and Zep Cloud dependencies. [analysis] Preserve it as the earlier scenario-module lead, but disable it in the strict-local core. A local replacement for those dependencies has not been built or verified here, and a simulation is not established predictive power.

**Adoption joins need identity checks.** [vendor] The preserved Qlib bank row names package `msqlib`, while the [project README](https://github.com/microsoft/qlib/blob/main/README.md) documents `pyqlib`; [bank identity receipt](evidence/bank-identity-review.json). TradingAgents' preserved adoption row is unresolved; yfinance/ffn have historical dependence records. [analysis] None of those is a newly measured adoption score. Keep them as dated evidence and repair the package mapping before ranking by dependence.

## Complete screening coverage

[analysis] The first 100 rows of the JSON table correspond to the first five compact pages: research/backtesting/portfolio primitives (1–30), crypto frameworks/feed adapters (31–40), legacy brokers/FIX/data clients (41–60), data formats/filings/accounting/portfolio applications (61–80), and tax/prediction-market components (81–100). Ten explicit additions complete the 110: TradeTally, ibflex, DuckDB, marimo, the SISO MiroFish fork, NautilusTrader, official Polymarket Python/TypeScript SDKs, current alpaca-py, and TradeNote. These are distinct repository identities; wrappers, forks and legacy versions are labelled rather than counted as interchangeable implementations.

## Taxonomy and resource gaps

[analysis] Existing tags cover much of the glue: `data-serialization`, `etl-data-integration`, `dataframe-numeric`, `client-sdk-generic`, `data-viz-charts` and `workflow-orchestration`. They do not precisely name a trade journal, broker-event ledger, backtesting engine or tax-lot workflow. Propose `trade-journal`, `broker-statement-reconciliation`, `backtesting-engine` and `accounting-ledger` for taxonomy review; do not silently mutate the frozen vocabulary. Bank submissions carry an existing coarse tag where defensible and a proposed narrower tag where necessary.

[analysis] **Measured laptop resource floors are null for every candidate.** A library being local, a Docker command existing, or a README mentioning a small machine is not an integrated memory/CPU/storage measurement. Default to the smallest core profile in [05-superapp.md](05-superapp.md), then measure before adding engines, notebooks, local models or historical datasets.
