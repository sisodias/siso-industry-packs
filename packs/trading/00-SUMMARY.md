# Trader operating workflow — research blueprint

**2026-09-13 · PARTIAL · local-first · no application built or deployed**

**Person / segment [analysis].** One own-account discretionary equity/options trader, working on a laptop with a broker record and separate journal. This is a bounded design target, not an invented interviewee. The supplied prior SISO work already favors an operating workflow over price prediction; this pack extends its missing person, workflow, incumbent and value research. [Person and eight complaints](01-person.md) · [prior entry](README.md).

**Wedge [analysis].** Import a broker statement, expose unmatched or incomplete records, then connect accepted executions to original reasoning and review. Keep broker execution and professional accounting authority outside the pilot. An efficient existing spreadsheet is a genuine competing solution. [Workflow](02-workflow.md).

**Spine [analysis].** Instrument → EvidenceItem → ResearchCase → ExperimentRun / TradePlan → AccountEvent. Reuse a journal application and its local database; keep raw evidence locally and analytics rebuildable. No SISO server. [Architecture](05-superapp.md) · [assembly JSON](05-assembly.json).

**Costs [vendor + arithmetic, not observed spend].** The selected one-seat reference basket totals **$1,450.80/year**, plus a separately localized **€81.60/year** Workspace quote and unknown broker/data/device/support costs. Only **$839.40/year of that reference basket** is the journal/case-board role the first wedge competes with. Actual stack tax, cancellations, hours saved and net cash remain **null**. [Prices and arithmetic](03-companies.md) · [value case](06-value.md).

## Ten provisional selections — not installed or admitted

| Repository | Verdict / bounded role | Bank |
|---|---|---|
| [GeneBO98/tradetally](https://github.com/GeneBO98/tradetally) | ADOPT — journal product base | NEW |
| [csingley/ibflex](https://github.com/csingley/ibflex) | ADOPT — supplied Flex XML parser | NEW |
| [duckdb/duckdb](https://github.com/duckdb/duckdb) | ADOPT — optional local analytical projection | ALREADY IN THE BANK |
| [marimo-team/marimo](https://github.com/marimo-team/marimo) | ADOPT — optional isolated research notebook | ALREADY IN THE BANK |
| [QuantConnect/Lean](https://github.com/QuantConnect/Lean) | ADOPT — optional experiment engine | ALREADY IN THE BANK |
| [PyPortfolio/PyPortfolioOpt](https://github.com/PyPortfolio/PyPortfolioOpt) | ADOPT — optional allocation research, not live limits | ALREADY IN THE BANK |
| [dgunning/edgartools](https://github.com/dgunning/edgartools) | ADOPT — optional filing evidence adapter | ALREADY IN THE BANK |
| [Polymarket/py-sdk](https://github.com/Polymarket/py-sdk) | ADOPT — optional public-read venue adapter | NEW |
| [beancount/beancount](https://github.com/beancount/beancount) | ADOPT — optional reviewed accounting export | NEW |
| [beancount/fava](https://github.com/beancount/fava) | ADOPT — optional local accounting reader | NEW |

All choices are **[analysis]** based on documented capabilities; exact metadata, scores, evidence depth and runners-up are in [110-row candidate table](04-oss-candidates.json) and [review](04-oss-candidates.md). NEW is relative to the four compared public bank layers, not the unpublished identity database. MiroFish remains a scenario-module lead, **disabled from the strict-local core** because its documented cloud dependencies have not been removed or qualified.

## Actual counts and remaining gates

| Item | Actual result |
|---|---|
| Tier-1 / Tier-2 profiles | **10 / 10**; 19 distinct companies because IBKR appears in both tiers |
| Distinct quoted practitioner threads | **8**, with linked excerpts; not verified customers or representative prevalence |
| Workflow stages | **10**, with Markdown and JSON |
| Repositories collected / screened | **435 / 110**; collection is not review, screening is not full code audit |
| Fully five-axis-scored / candidate builds / integrated tests | **0 / 0 / 0**; health/adoption remain unknown |
| Provisional selections / production adoptions | **10 / 0** |
| Inherited search rounds / proven consecutive dry rounds | **3 / 0**; required stopping criterion not met |

**Nine gaps [analysis]:** operator baseline; feed/broker entitlements; complete event reconciliation; consequential-execution qualification; professional accounting/tax review; laptop footprint/recovery; verified local privacy/scenario independence; maintenance/adoption/rights; migration and repeat-deployment economics. [Gap register](05-superapp.md).

**Verdict [analysis]: YES to a bounded read-only import-to-review pilot; NO to declaring the whole super-app finished, profitable or production-ready.** Reject the thesis if the incumbent already performs equally well, reviewed effort does not fall, source fidelity fails, privacy is lost or support/migration costs exceed observed benefit. The registry intentionally remains **partial**, despite replacing all seven report placeholders. [Value and falsifiers](06-value.md) · [handoff](RESEARCH-HANDOFF.md).
