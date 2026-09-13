# 05 · Proposed super-app assembly

2026-09-13. **Research design only; no application code, build, deployment or production admission.** All resident services run on **one client-owned VPS per client**, never SISO infrastructure. The unfinished repository sweep can change these provisional selections. Machine-readable counterpart: `05-assembly.json`.

## The spine: six objects, explicit authority

[analysis] The schema below is the design, not an implemented database. Upstream native records remain authoritative within their components; the spine stores canonical links, immutable evidence references and allowed transitions rather than a second financial ledger.

| Object | Stable identity and key fields | Authority boundary |
|---|---|---|
| Party | Party ID; person/business; roles; contact/channel IDs; distinct billing/site relationships | Verified contact matching; no inferred authority from a phone number alone |
| Job | Job ID; site; parties; scope baseline; external system IDs; retention/access policy | One party can have many sites/jobs; address is not a unique identity |
| WorkPackage | Package ID; job; reviewed scope revision; trade; readiness/holds; schedule; acknowledgement | Scheduling does not establish safety, quantity or readiness truth |
| Conversation | Thread/message IDs; channel; sender; timestamps; attachments; links to job/request | Preserve originals and attribution; notes are not fabricated transcripts |
| EvidenceDocRevision | Original-file hash; revision ID; source; receipt time; parent/supersedes; access/export metadata | Append revisions; never silently overwrite signed/issued evidence |
| CommercialRecord | Estimate/PO/change/invoice type; exact revision; amount/currency; approval evidence; ledger reference | Draft administration; incumbent accounting, payment and contract authority remain separate |

## Component map and runners-up

[vendor] Component capabilities are described in the linked READMEs. [analysis] Selection rationale and authored integration work are proposals, not benchmark results.

| Workflow | Component / verdict | Authored glue | Why over reviewed alternatives |
|---|---|---|---|
| W01 intake | [Chatwoot](https://github.com/chatwoot/chatwoot/blob/develop/README.md), ADOPT core | Map thread/contact to party/site/job; human qualification and exception queue | An invoice customer list in InvoicePlane/ERPNext is not the same conversation surface; avoid rebuilding a shared inbox |
| W02 scope | [ERPNext](https://github.com/frappe/erpnext/blob/fe25746febc8731bbbc0880dcb18d528dcf08a63/README.md), ADOPT base | EvidenceDocRevision and original-file provenance; scope holds | Paperless is useful retrieval but not proof of approved construction revision; IFC import optional |
| W03 estimate/bids | ERPNext ADOPT; [Bidwright](https://github.com/braedonsaunders/bidwright/blob/main/README.md) STUDY | Reviewed bid/estimate version mapping; source quantities, assumptions and exclusions | GEstimator is desktop; Bidwright is more vertical but runtime/adoption/autonomy require deeper admission. Do not rebuild estimating casually |
| W04 contracting/selections | ERPNext plus [DocuSeal](https://github.com/docusealco/docuseal/blob/master/README.md), ADOPT bounded flow | Bind exact revision to signer/authority/event; keep signature evidence | InvoicePlane invoice/quote acceptance is not independently established full signing workflow; paid DocuSeal features remain separate |
| W05 purchasing/documents | ERPNext ADOPT | PO/site/supplier links and evidence exception list | InvoicePlane is narrower; a second task app would duplicate procurement records |
| W06 schedule | ERPNext task view first; [OpenProject](https://github.com/opf/openproject/blob/a6be9b2e376655655ba98537e08929905d9e8a37/README.md) STUDY | Readiness/hold and field acknowledgement, not autonomous critical-path claims | OpenProject may win deeper scheduling; admit only if measured needs justify another full service |
| W07 field/time/expense | ERPNext ADOPT base | Reviewed capture, upload receipt, idempotency and offline exception handling | Paperless search does not establish field adoption or payroll readiness; no claim a reviewed repo already solves offline UX |
| W08 changes | ERPNext + Chatwoot + DocuSeal | Exact-revision state machine, authority, release and billing eligibility | An additional all-in-one app does not by itself solve the cross-system approval chain |
| W09 billing | ERPNext draft export; [WeasyPrint](https://github.com/Kozea/WeasyPrint/blob/main/README.rst), ADOPT | Idempotent accounting reference; human review and reconciliation | InvoicePlane is a viable narrow alternative, not another concurrent financial authority |
| W10 closeout/warranty | ERPNext + WeasyPrint; [restic](https://github.com/restic/restic/blob/master/README.md), ADOPT | Complete export manifest, original evidence, reopening history, restore verification | Paperless may improve retrieval later; do not add it merely to make the suite look complete |

[analysis] Five provisional ADOPT repositories. A release pin, verified dependencies, security review, edition/rights check and installation/restore test are required before any becomes an admitted component. README functionality is not working-integration evidence.

## Honest glue cost

[analysis] Identity: external contact IDs, duplicate names, job sites and cost codes differ. Keep reversible mapping tables; never merge parties solely by name. Schema: estimates, signed documents and accounting entries have different precision/currency/tax/status semantics; preserve original amounts and references. Authorization: the role allowed to draft is not necessarily allowed to approve, release or bill. Do not invent common SSO or free role features across products.

[analysis] Events: authenticate webhooks, store provider event IDs, handle duplicates/out-of-order events, use durable outbox/retries and visible failed queues. Never infer successful billing from HTTP delivery alone. Files: preserve original bytes and hashes, detect MIME, quarantine untrusted uploads, constrain parser/rendering network/CPU/memory, and store source and receipt timestamps distinctly. Export: manifests plus original attachments, relationships and approval history, not only CSV rows.

[analysis] State machine: requested → scoped → priced → sent_for_approval → approved/rejected/superseded → released_to_field → billing_eligible. Bind each transition to actor, exact revision and evidence. Repricing means a new revision and renewed approval, not silently editing a signed record. A legally meaningful acceptance or payment decision remains with the designated human/professional. A queued offline capture is not acknowledged receipt or permission to work.

[analysis] The brief's roughly 5% authored differentiation is a direction, **not a measured engineering fraction**. Lift existing apps/libraries by default, but budget mapping, tests, migration and operations honestly. The only new design here is the shared identity/evidence/approval assembly; no code was written.

## Deployment and ownership

[analysis] One client-owned Linux VPS; separate component containers/processes and least-privilege database identities. ERPNext retains its supported database/worker/cache topology; Chatwoot its supported database/workers; DocuSeal its documented database/storage choices. Share host resources only where supported; do not force heterogeneous apps into one database schema. Reverse proxy/TLS and supervised background jobs remain on that box. Secrets stay in the client's private runtime configuration, never GitHub or public documents.

[vendor] The [DigitalOcean Droplet page](https://www.digitalocean.com/pricing/droplets) lists the priced 8-GiB/4-vCPU configuration at $48/month and the 16-GiB alternative at $96/month; [weekly backups](https://www.digitalocean.com/pricing/backups) add 20% in the modeled option. [analysis] These yield $691.20 or $1,382.40/year. **Capacity is untested.** Budget the 16-GiB case for planning; 8 GiB is an evaluation hypothesis. No local LLM or GPU is required by this proposed administrative wedge. Large OCR/model conversions are optional bounded jobs, not included free capacity.

[analysis] The client owns the domain, VPS account, application admins, message numbers/accounts, merchant accounts and encrypted backup destination/key custody. Keep off-host backups under the client, not SISO. Provider snapshots alone are not a demonstrated application restore. Proposed objectives to test: daily app-consistent exports, a 24-hour recovery-point target, four-hour restore target, documented restore rehearsal and complete vendor-neutral export. These are design targets, not achieved SLAs. A one-box deployment is a single failure domain, not high availability.

[vendor] [DocuSeal](https://github.com/docusealco/docuseal/blob/master/README.md) places SSO, user roles, automated reminders, SMS verification and embedded signing/builder in Pro. [analysis] Use a permitted linked flow or quote required features; do not represent the whole UI as a seamless free embedded product. [Chatwoot](https://github.com/chatwoot/chatwoot/blob/develop/LICENSE) has separate enterprise terms; review the actual used paths.

## Architecture sketch

```text
Client-owned email/SMS/social accounts        Client-owned accounting/payroll/payment systems
                 |                                       ^
        authenticated events                         reviewed export/reconcile
                 v                                       |
+------------------------ ONE CLIENT VPS -----------------+---------+
| Reverse proxy / TLS                                               |
| Chatwoot inbox ---- canonical party/job/thread links ---- ERPNext  |
|       |                  six-object spine                   |      |
|       +---- request -> scoped/priced revision -> DocuSeal ---+      |
|                      human approval + separate field release      |
| Original-file store + immutable revision references + event log    |
| WeasyPrint: controlled PDF packets / complete export manifest       |
| Isolated DB identities, durable queues, retry/exception surfaces    |
| restic + app-consistent exports                                    |
+----------------------------|--------------------------------------+
                             v
              Client-owned encrypted off-host backup
```

[analysis] This is a design diagram, not running topology. Optional read-only IFC/MPP/XER import modules are outside the default resident set. External transport and bank settlement cannot be made self-hosted by a local inbox/ERP; only their adapters and retained records reside here.

## Required screens, not a UI-library sweep

[analysis] Shared inbox; lead/survey queue; job/site overview; versioned scope/estimate; selection/deadline board; procurement/document exceptions; acknowledged daily plan; field upload/time queue; change request/review/sign/release view; billing reconciliation; punch/warranty; export/restore/admin. Use the existing [component-bank inventory](https://github.com/sisodias/siso-component-bank) as source context, with actual component rights/quality checked; no new UI library research or assumed free licence for every component.

## Ten honest gaps

[analysis] G1 validated US estimating inputs; G2 engineering/safety/permit/labor/tax/contract authority; G3 approval/dispute edge cases; G4 proven offline field behavior; G5 accounting/payroll reconciliation; G6 external channels/payment rails; G7 edition/API/SSO/role entitlements; G8 one-box capacity, updates and recovery; G9 migration and operator/sub adoption; G10 unfinished 100-repo, bank, health/adoption and dry-round audit. These are gaps in this assembly/evidence, not a global claim that no OSS exists.

[analysis] Acceptance must use redacted fixtures and adversarial cases: wrong job/site, repeated webhook, stale approval, amended price, offline retry, partial upload, rejected change, missing authority, conflicting accounting status and independent restore. No deployment follows merely from an ADOPT label.
