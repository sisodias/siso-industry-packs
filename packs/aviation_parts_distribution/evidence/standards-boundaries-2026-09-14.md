# Standards and screening continuation — 14 September 2026

[analysis] This checkpoint adds twelve direct repository reviews to the eleven preserved from 13 September: **23 examined, not 100**. It does not implement the application or qualify any component for production. The original RFQ wedge, six business aggregates and client-owned VPS boundary remain unchanged. [Candidate register](../04-oss-candidates.json) · [Bank receipt](bank-reconciliation-2026-09-14.json).

## 1. Five distinct contracts, not interchangeable forms of traceability

| Contract | What its publisher supports [vendor] | Consequence for the blueprint [analysis] |
|---|---|---|
| ATA Spec 2000 Chapter 16 | Electronic regulatory documentation, including release-certificate exchange. [ATA working group](https://ataebiz.org/WG-regulatory-documentation/) | Obtain permitted specification versions and partner fixtures. Neither an EPCIS event nor a parsed PDF substitutes for this contract. |
| S1000D | Structured technical-publication information. [Specification publisher](https://s1000d.org/) | Useful for permitted technical-document workflows; not the certificate-acceptance engine. |
| GS1 EPCIS | Supply-chain event visibility. [GS1](https://www.gs1.org/standards/epcis) | May represent custody and movement observations. Does not establish issuer authority, component eligibility or complete aviation provenance. |
| IATA ONE Record | Cargo data model and associated API/security specifications. [Pinned repository](https://github.com/IATA-Cargo/ONE-Record/blob/ad5f40d539b29692881672cf91878a4d2dbe59c2/README.md) | Connect shipment observations to Fulfilment; negotiate versions and partner access. A specification is not a deployed server or a data-sharing agreement. |
| EDIFACT / X12 / UBL carried over agreed transport | Parsers, document models and transport are separate implementations. [StAEDI](https://github.com/xlate/staedi/blob/23fc5ea19e708451a4d9f69572b50c7ae7712737/README.md) · [ph-ubl](https://github.com/phax/ph-ubl/blob/ae5d4c08ed17c30fcca5fcc4e648280b35f2f8c6/README.md) · [OpenAS2](https://github.com/OpenAS2/OpenAs2App/blob/fbe1e8778eba08993d320d97a133dc45263c054d/README.md) | Transport delivery, syntactic validation, commercial acceptance and regulatory decisions must have different states. |

[vendor] ATA identifies Chapter 15's Aircraft Transfer Parts List as a legacy approach and points new implementations toward the Installed Component Status capability in Spec 2500. That is an additional interface-discovery lead, not a licence to copy a specification or proof that this small distributor needs aircraft-transfer scope. [ATA standards map](https://ataebiz.org/standards/).

[analysis] The necessary invariants are: preserve original evidence; identify the document/event profile and version; record source, receipt time and external IDs; retain partner acknowledgements separately from accepted business state; and require a qualified decision for unresolved quality/export/credit holds. A successful schema check never clears all holds.

## 2. What the newly reviewed repositories actually change

### Technical documents, event models and test fixtures

[vendor] `kibook/s1kd-tools` provides small S1000D utilities, with issue-specific compatibility and no planned SGML support. [Pinned README](https://github.com/kibook/s1kd-tools/blob/faa99f59894003b4c67e3e76059dd4146db204fd/README.md).

[analysis] Keep it as a document-processing comparison candidate for W04/W10, not as an automatic FAA/EASA certificate validator. First obtain representative, permitted publication files. A product name containing an aviation standard is not sufficient fit evidence.

[vendor] The inspected `gs1/EPCIS` README separates development artefacts from ratified normative resources. The inspected ONE Record README also distinguishes versioned releases and working drafts. [GS1 development repository](https://github.com/gs1/EPCIS/blob/6f71468231838e424bb5dfa836e006e8dc69615c/README.md) · [ONE Record](https://github.com/IATA-Cargo/ONE-Record/blob/ad5f40d539b29692881672cf91878a4d2dbe59c2/README.md).

[analysis] **SKIP GS1's draft HEAD as the production contract**, while retaining it as a research reference. Choose normative versions only after partner agreement. This verdict is about draft suitability, not rejection on licence alone and not a claim that EPCIS is unsuitable generally.

[vendor] `ift-gftc/opentraceability` documents C# EPCIS XML/JSON-LD support and extensions. Its Java wording is inconsistent with the accompanying package link; no equivalent Java capability was established here. One example uses a dummy header to satisfy a schema. [Pinned README](https://github.com/ift-gftc/opentraceability/blob/05a392128730367424b0c26048d6199de9cfa71f/README.md).

[analysis] Compare its .NET library with the Java alternative, using actual partner messages. Never turn a demonstration dummy header into alleged sender identity or production provenance. Food-sector extensions need explicit mapping before aviation use.

[vendor] `openepcis/openepcis-models` supplies shared XML/JSON-LD models and requires Java 25 in the inspected build guidance. `epcis-testdata-generator` supplies synthetic EPCIS fixtures; its recent build moved to Java 25 while parts of its runnable-jar guidance mention Java 21+. [Models](https://github.com/openepcis/openepcis-models/blob/a481b0827dd43a0a4282d8db840eaf98477f7730/README.md) · [Generator](https://github.com/openepcis/epcis-testdata-generator/blob/b25e32997987c88cf2b8d3b1b3f5f3cffb0beb4d/README.md) · [Build change](https://github.com/openepcis/epcis-testdata-generator/commit/b25e32997987c88cf2b8d3b1b3f5f3cffb0beb4d).

[analysis] A Java boundary is an integration and maintenance cost beside a Python/Frappe application. Verify the selected release's build/runtime contract; no measured RAM floor is established. Synthetic events belong in isolated tests, never customer trace packs or production stock history.

### Trading documents and transport

[vendor] `nerdocs/pydifact` is a Python EDIFACT parser/serializer whose README marks the API as work in progress and states that optional UNG/UNE functional groups are unsupported. `xlate/staedi` documents grouped-message handling and configurable schema validation in a Java streaming interface. [pydifact](https://github.com/nerdocs/pydifact/blob/f62d8f7bd499f2ba3f130bcbd6d6d8469c6563ed/README.md) · [StAEDI](https://github.com/xlate/staedi/blob/23fc5ea19e708451a4d9f69572b50c7ae7712737/README.md).

[analysis] For simple agreed EDIFACT subsets, pydifact is the smaller language-boundary candidate; for grouped or richer validation needs, StAEDI is a stronger candidate on the documented interface. Neither wins without partner fixtures, rejection cases and version compatibility. Do not disable validation merely to pass an import.

[vendor] `phax/ph-ubl` provides UBL bindings, code lists and test resources and specifies Java 17+. `OpenAS2/OpenAs2App` is a Java AS2 transport implementation rather than an invoice or aviation-document approval engine. [ph-ubl](https://github.com/phax/ph-ubl/blob/ae5d4c08ed17c30fcca5fcc4e648280b35f2f8c6/README.md) · [OpenAS2](https://github.com/OpenAS2/OpenAs2App/blob/fbe1e8778eba08993d320d97a133dc45263c054d/README.md).

[analysis] Only add these where a real counterparty requires them. National invoice profiles, tax rules, acknowledgements, commercial state and certificate decisions remain separate requirements. Transport receipts must not silently create an accepted order or release inventory. Administrative interfaces should stay private; demonstration deployment options are not a security design.

## 3. Watchman: documentation drift, not a falsely alleged broken feed

[vendor: regulator] The OFSI Consolidated List stopped updating on **28 January 2026**. The UK Sanctions List is the current list for UK designations; the migration guidance explains UKSL Unique IDs and historic OFSI Group IDs. [Official transition guidance](https://www.gov.uk/guidance/moving-to-a-single-list-for-uk-sanctions-designations-28-january-2026).

[vendor] At commit `328f7c3bcd4cb7e574440fd08be2f78362a6e5a0`, Watchman's README links the old consolidated-list page. However, its UK download adapter defaults to `https://sanctionslist.fcdo.gov.uk/docs/UK-Sanctions-List.csv`, and its model contains the current Unique ID plus legacy Group ID fields. [README](https://github.com/moov-io/watchman/blob/328f7c3bcd4cb7e574440fd08be2f78362a6e5a0/README.md) · [Download adapter](https://github.com/moov-io/watchman/blob/328f7c3bcd4cb7e574440fd08be2f78362a6e5a0/pkg/sources/csl_uk/download_uk.go) · [Model](https://github.com/moov-io/watchman/blob/328f7c3bcd4cb7e574440fd08be2f78362a6e5a0/pkg/sources/csl_uk/uk_csl.go).

[analysis] The supported finding is **an outdated README link**. It would be wrong to infer a broken current feed from that link. Successful live download, parsing, refresh, matching and failure handling have **not** been tested in this research.

[vendor] Watchman describes in-memory lists, periodic refresh, no persisted search queries, and a static-data image for testing. [Pinned README](https://github.com/moov-io/watchman/blob/328f7c3bcd4cb7e574440fd08be2f78362a6e5a0/README.md).

[analysis] The aviation application therefore needs its own screening receipt: subject identity, queried fields, list/source/version, retrieval and screening timestamps, candidate matches, reviewer, disposition and linked order. Reject static test data as a live feed. Missing or stale feeds should produce an unresolved screening state, not an implicit pass. A name match/no-match alone is not a full export classification, ownership/control, end-use or licensing determination; qualified review remains outside this parser comparison.

## 4. Yente: local queries do not eliminate data and index costs

[vendor] Yente is MIT-licensed matching/search software and requires Elasticsearch or OpenSearch. OpenSanctions separates software rights from commercial rights to its bulk data. [Pinned README](https://github.com/opensanctions/yente/blob/3bc1b14ea884aba9f0728d67b76a461f5339dc59/README.md) · [MIT licence](https://github.com/opensanctions/yente/blob/3bc1b14ea884aba9f0728d67b76a461f5339dc59/LICENSE) · [Self-hosting explanation](https://www.opensanctions.org/articles/2026-06-25-should-you-run-the-opensanctions-api-yourself/) · [Commercial-data terms](https://www.opensanctions.org/docs/commercial/exemption/).

[analysis] Compare Yente with Watchman only after the required coverage, licensed datasets, matching tests, update guarantees and client-VPS resource budget are known. Do not invent a licence price or assume an extra search engine fits within the prior 16 GiB allowance. Local matching can preserve the client boundary, but data updates still require an authorised source. Neither engine owns the human compliance decision.

## 5. Acceptance work still not performed

[analysis] The proposed tests are: distinguish normative and draft profiles; reject wrong profiles; process grouped and ungrouped partner messages; preserve source IDs and signed originals; keep transport acknowledgement separate from order acceptance; keep synthetic data out of production; retain reproducible screening receipts; detect stale/missing feeds; enforce quality/export/credit holds; and measure adapter/index memory plus restore behaviour. **No test listed here has run.** [Assembly contract](../05-superapp.md).

[analysis] Bank reconciliation now classifies eight identities as held and fifteen as NEW relative to six pinned published layers. Fourteen non-SKIP NEW candidates are candidates for bank review, not admitted components. The minimum 100-repository funnel, all-stage search-round closure, external dependence evidence, maintainership/issue-response analysis and production qualification remain unfinished. [Pinned receipt](bank-reconciliation-2026-09-14.json) · [Candidate register](../04-oss-candidates.json).
