# 05 — The assembled staffing operating system

> Research snapshot **2026-09-13**. `[vendor]` = upstream/provider claim; `[practitioner]` = attributed public report; `[analysis]` = our inference/design. No application deployed or candidate code executed.

## Thesis and scope

[analysis] Build an **evidence-preserving coordination layer around the incumbent ATS**, not an unsupervised hiring engine or a replacement payroll bureau. The client owns one VPS, accounts, databases, keys and backups. Nothing in the application runs on SISO servers. Client-owned external payroll, ledger, carrier, sourcing and government services remain explicit dependencies; a Linux process cannot replace their legal authority or network access. [Foundry boundary](https://raw.githubusercontent.com/sisodias/great-library-of-siso/main/research/industries/source/intelligence/agency/industries/recruiting_staffing.json); [workflow](02-workflow.md).

## 1. The six-object spine

[analysis] Our differentiated schema is the following set of roots. Source files, messages, approval events and rate revisions are child entities with hashes and retention labels. Candidate identities and candidacies are separate: one person can legitimately have several client-specific applications. An assignment is not just an ATS stage label; it carries employer, commercial and effective-date authority.

| Root object | Key persisted fields | Authority |
| --- | --- | --- |
| Party | id; person_or_organization; external_ids; contact_methods; consent_versions; role_scoped_visibility | Incumbent identity plus reviewed link; no autonomous fuzzy merge. |
| JobOrder | id; client_party_id; external_ats_id; approved_requirements; terms_version; approver_id; effective_dates | Client/account approver; approved ATS version remains authoritative in pilot. |
| Candidacy | id; candidate_party_id; job_order_id; representation_consent; submitted_artifact_hash; human_status; feedback_refs | Recruiter and hiring authority; never model-derived selection. |
| Assignment | id; candidacy_id; employer_party_id; client_party_id; work_location; start_end; effective_rate_versions; provider_ids | Authorized employment/commercial signatories and payroll owner. |
| WorkRecord | id; assignment_id; period; dated_hours; expenses; revision; client_approval; payroll_receipt; invoice_refs | Worker reports; client approves billing; payroll and accountant retain separate wage/ledger authority. |
| Conversation | id; channel; provider_thread_id; participants; source_message_ids; linked_objects; consent; owner; reply_state | Client-owned channel and role-scoped staff; external sends through approval outbox. |

[analysis] During the pilot, external IDs plus immutable source links anchor records; the spine may own coordination state and approved mappings, not silently replace source facts. Every changed approved requirement or rate creates a new version with an effective interval. No generic last-write-wins sync may overwrite an employment decision, approved rate or signed artifact.

## 2. Component selection and named counterfactuals

All ADOPT selections below are conditional on release, rights, security and workflow qualification. Detailed upstream evidence, licences and research pins are in [Stage 4](04-oss-candidates.md); these are not live deployment pins.

| Stages | Chosen component / verdict | What we write | Why these beat named runners-up |
| --- | --- | --- | --- |
| S01; S02; S12 | [frappe/frappe](https://github.com/frappe/frappe) ADOPT; [chatwoot/chatwoot](https://github.com/chatwoot/chatwoot) ADOPT; [surveyjs/survey-library](https://github.com/surveyjs/survey-library) ADOPT | Party/JobOrder/Conversation links, versioned intake and approved outbox. | Frappe owns structured workflow and Chatwoot conversation context; avoid parallel sales databases. LibreDesk remains lean-inbox counterfactual. Runners-up: espocrm/espocrm, freescout-help-desk/freescout, abhinavxd/libredesk, Django-CRM/Django-CRM |
| S03; S04; S05 | [jsvine/pdfplumber](https://github.com/jsvine/pdfplumber) ADOPT; [python-openxml/python-docx](https://github.com/python-openxml/python-docx) ADOPT; [surveyjs/survey-library](https://github.com/surveyjs/survey-library) ADOPT; [frappe/frappe](https://github.com/frappe/frappe) ADOPT | Source-artifact retention, approved extraction fields and Candidacy permissions. | Local bounded extraction beats inferred strengths or a new JVM/model runtime; failed extraction goes to humans. Runners-up: OmkarPathak/pyresparser, OmkarPathak/ResumeParser, apache/tika, dedupeio/dedupe |
| S06 | [alextselegidis/easyappointments](https://github.com/alextselegidis/easyappointments) ADOPT; [collective/icalendar](https://github.com/collective/icalendar) ADOPT; [sabre-io/vobject](https://github.com/sabre-io/vobject) ADOPT | Candidacy-to-booking identity, timezone/version/cancellation reconciliation. | Whole booking application plus protocol libraries; Cal.diy production warning is disqualifying for this role. Runners-up: calcom/cal.diy, Tymeslot/tymeslot, thunderbird/appointment, ics-py/ics-py |
| S07; S08 | [docusealco/docuseal](https://github.com/docusealco/docuseal) ADOPT; [frappe/frappe](https://github.com/frappe/frappe) ADOPT | Assignment authorization, signer-role mapping and restricted readiness checklist. | Established signing UI with explicit priced API boundary; early Frappe-native signing remains a service-removal counterfactual, not current admission. Runners-up: documenso/documenso, OpenSignLabs/OpenSign, chiefonboarding/ChiefOnboarding, GoldenJustin/ERPNext-Electronic-Signature, penpact/penpact |
| S09; S10; S11 | [frappe/erpnext](https://github.com/frappe/erpnext) ADOPT; [intuit/oauth-pythonclient](https://github.com/intuit/oauth-pythonclient) ADOPT; [moov-io/ach](https://github.com/moov-io/ach) ADOPT | Effective rates, WorkRecord versioning, separate wage/bill states and reviewed provider exports. | Keep one operational schema; retain external payroll and general ledger. ACH validation does not originate money. Runners-up: kimai/kimai, solidtime-io/solidtime, Payroll-Engine/PayrollEngine, VonHoltenCodes/SlowBooks-Pro-2026, invoiceninja/invoiceninja |
| S01; S05; S10; S11; S12 | [activepieces/activepieces](https://github.com/activepieces/activepieces) ADOPT; [frappe/frappe_docker](https://github.com/frappe/frappe_docker) ADOPT | Only missing authorized adapters, idempotent receipts and deployment configuration. | Optional connector engine only where it removes custom adapter work; migration tools are per-client, not default resident services. Runners-up: odoo/odoo, frappe/crm, bullhorn/sdk-rest, bullhorn/dataloader |

## 3. The glue that actually costs work

[analysis] **Identity and schema.** Define deterministic client-owned UUIDs with external-ID namespaces; preserve original values and source timestamps. ATS client/company/contact, Frappe Customer/Contact and inbox contact do not have identical semantics. Candidacy is candidate × job × representation version; never use email alone as a universal identity. Merge suggestions require a reviewer and reversible link history.

[analysis] **Dates, money and time.** Keep original timezone and UTC event instants, all-day semantics, recurrence IDs and calendar sequence/cancellation states. Effective rate intervals must not overlap silently. Store decimal currency with currency code, actual dated hours and explicit adjustments; do not use binary floating point for money or replace worked hours with the client's billable approval. Payroll-provider rules remain authoritative; approved exports reconcile totals and individual lines.

[analysis] **Auth and permissions.** Recruiters see assigned clients/candidacies; client approvers only their orders/submissions/time; workers only their own intake and work records; payroll/compliance roles have restricted access; accountant owns invoice finalization; operator/admin access is logged and break-glass. Test object-level checks at APIs and attachment URLs, not just hidden UI buttons. Community product editions do not automatically include enterprise SAML/RBAC. Deep links and explicit scoped sessions are acceptable in the pilot; a fake universal login that bypasses authorization is not.

[analysis] **Write outbox.** Each external action has actor, permitted destination, payload hash, source version, expiry, approval and idempotency key. Workers recheck consent, reply state, recipient, job status and permission immediately before sending. Store success/failure/provider IDs; retries reuse the same idempotency identity. Expired or changed requests return to review. Reply/opt-out/webhook duplicates and reordered events must never cause duplicate outreach or cross-client disclosures. Human approval is for the exact action, not a permanent blanket token.

[analysis] **Files.** Originals are immutable, hash-linked and scanned/quarantined before bounded extraction. Limit size, execution time, nested archives and process memory; do not execute macros, embedded scripts or fetched links. Local PDF/DOCX extraction produces evidence-linked draft fields, never candidate rankings or inferred strengths. Machine-generated PDF is the preferred input; scanned/unreadable documents go to accessible human review, not silent discard. Restricted background/I-9/bank records never enter general chat/search or public research repositories. No remote AI extraction is enabled by default.

[analysis] **Reconciliation and deletion.** Use inbound receipt IDs, source cursors and a dead-letter queue; human owners repair partial writes. Deletion, consent withdrawal and retention holds propagate by explicit policy, with exceptions recorded. File retention and legal holds may conflict; do not promise one universal delete button. Backups have client-approved expiry and restore procedures. A signed PDF hash is not a complete legal signing ceremony or an independent identity guarantee.

## 4. Build versus lift

[analysis] Lift product capabilities by default: Frappe forms/permissions/jobs, ERPNext operational records, Chatwoot conversations, SurveyJS approved fields, booking/signature applications and existing protocol libraries. Write only the six-root identity/authority model, missing mappings, approval outbox and acceptance fixtures. The brief's roughly **5% custom** is a design aspiration, **not a measured engineering estimate**: migration and permissioning may dominate cost. No application code was written in this research.

[analysis] Extra ADOPT libraries and optional services are a reuse menu, not a mandate to run fourteen apps. Frappe Docker is deployment packaging, not another resident product. Activepieces starts only if it replaces adapter work beyond Frappe's existing jobs. A second CRM, time database or signing service must justify its integration/operating cost against the named runner-up or removal test. This implements [GQ-004](https://github.com/sisodias/great-library-of-siso/blob/main/registry/works/frontier-question-gq-004.json) and [GQ-013](https://github.com/sisodias/great-library-of-siso/blob/main/registry/works/frontier-question-gq-013.json): contextual best primitives and a smaller useful building set, not largest catalogue.

## 5. One-client, one-VPS deployment plan

[analysis] **Default bases:** Frappe + scoped ERPNext in the same site/version family; Chatwoot Community; packaged reverse proxy; isolated MariaDB and PostgreSQL databases, queues, local document storage and workers. Add EasyAppointments and DocuSeal only in later admitted phases. Keep database/user credentials separate even when sharing a database engine. Bind internal services to private networks, expose only TLS endpoints, pin releases/images by digest and keep secrets in the client's restricted configuration—not GitHub. No Kubernetes, GPU, hosted SISO database or cross-client shared compute.

[vendor] A Chatwoot deployment guide specifies at least 4 vCPU/8 GB for that application path; this is not a benchmark of the combined assembly. [Official guide](https://developers.chatwoot.com/self-hosted/deployment/gcp). [analysis] **16 GiB / 8 shared vCPU is a planning envelope, not a certified minimum** for Frappe/ERPNext plus Chatwoot and carefully limited optional work. An 8 GiB / 4 vCPU lean trial covers only minimal Frappe intake coordination with existing communication tools retained; it does not promise the full suite fits. Resource floors are null until tested. Enforce bounded attachment work and queue concurrency; if load or restore tests fail, reduce resident scope or resize and recalculate economics.

[vendor] The observed DigitalOcean Basic price examples are $48/month for the 8 GiB plan and $96/month for 16 GiB. [Pricing](https://www.digitalocean.com/pricing/droplets). [analysis] The full planning run cost is $1,152 compute + $120 assumed client-owned backup + $3,600 assumed support + $528 illustrative paid signature integration = **$5,400/year**, before incident overruns, extra modules, domain/taxes and external-service usage. The minimal trial is $576 + $120 + $1,200 = **$1,896/year** and has less functionality. These are not hosting quotes or measured capacity results.

[analysis] Backups must be encrypted and off the compute box in a **client-owned account**. A same-disk copy is not recovery. Proposed targets: daily restore points, documented restore drill, no public database ports, timed patch windows and a named support owner; contractual RPO/RTO are not promised until measured. A one-box outage stops local operations, so retain approved provider access/export fallback and wage-deadline escalation.

[analysis] Frappe development HEAD currently requires a newer Python line than older deployment recipes; select mutually compatible stable Frappe/ERPNext/optional HRMS releases and container digests, not the latest HEAD of each. EasyAppointments' audited Composer requirement is PHP >=8.2; older generic web instructions are not the deployment contract. [Frappe manifest](https://github.com/frappe/frappe/blob/develop/pyproject.toml); [EasyAppointments manifest](https://github.com/alextselegidis/easyappointments/blob/develop/composer.json); [deployment audit](04-oss-candidates.md).

## 6. Architecture sketch — data ownership, not a tab bundle

```text
Client-owned email / SMS / approved channels
                 | webhook or approved import
                 v
       Chatwoot CE -- Conversation/source IDs
                 | allowlisted event mapping
                 v
 Frappe + scoped ERPNext: six-root coordination spine
   | SurveyJS forms       | bounded local PDF/DOCX libraries
   | approvals/outbox     | hashes + restricted client storage
   |                      | separate queues and DB credentials
   +--> optional booking service --> client calendars
   +--> optional self-hosted signing --> sealed files/receipts
   +--> optional Activepieces --> approved incumbent ATS writes
   +--> approved payroll export --> CLIENT payroll provider
   +--> approved invoice mapping --> CLIENT accounting ledger
                 |
     encrypted backups --> CLIENT-owned off-box storage
```

[analysis] Services communicate through versioned IDs and explicit adapters; they do not directly edit one another's databases. Libraries run within bounded workers. External accounts are client-owned retained authorities. All application compute remains on that client's VPS. The public research repository contains only source metadata, design and test specifications.

## 7. Required screens, not another UI-kit survey

[analysis] Inbox/owner queue; source-linked requisition review; client/job workspace; candidate/CV evidence viewer; submission/feedback packet; interview board; assignment/rate timeline; restricted onboarding checklist; weekly time/exception review; payroll and invoice reconciliation; redeployment list; permissions/audit/restore admin. Reuse existing [SISO component bank](https://github.com/sisodias/siso-component-bank) sources and notes. Accessibility, keyboard operation, clear errors and restricted/no-data states are acceptance tests, not asserted achievements.

## 8. Honest gaps and admission tests

| Gap | What remains external or unmeasured |
| --- | --- |
| 1 | Maintained independently validated US staffing payroll/tax filing, remittance and employer authority |
| 2 | Lawful access to sourcing networks, job-board inventory and current candidate contact data |
| 3 | Background checks, Form I-9/E-Verify participation and licensed verification services |
| 4 | Per-client ATS API entitlement, rate limits and lossless history/attachment migration |
| 5 | Complete US assignment/rate/time/pay-bill schema and authority-aware mappings |
| 6 | Carrier/email deliverability, authorized WhatsApp/SMS accounts and usage fees |
| 7 | Paid signature API/SSO/enterprise permissions and legal ceremony qualification |
| 8 | Fifty-state/local employment, privacy, retention and accessibility review |
| 9 | One-box capacity benchmarks, security hardening, tested restore and support ownership |
| 10 | Observed operator workload, measurable savings and eligible segment count |

[analysis] These mean **no qualified replacement was established by this bounded search**, not that no open-source code can ever exist. Current government sources address part of the old EEOC retrieval gap, but this is not a state/local legal opinion or accessibility certification. [EEOC/DOJ warning](https://www.eeoc.gov/newsroom/us-eeoc-and-us-department-justice-warn-against-disability-discrimination); [NYC AEDT](https://www.nyc.gov/site/dca/about/automated-employment-decision-tools.page); [FTC background checks](https://www.ftc.gov/business-guidance/resources/background-checks-what-employers-need-know).

[analysis] Before a pilot: authorize the data map and roles; reconcile an export; test 50 reviewed requisitions, 50 scheduling changes and one complete payroll reconciliation cycle. Include duplicate/reordered webhook, stale role, withdrawal, wrong recipient, lost attachment, DST, rate change, partial payroll failure, invoice retry, restricted-client access and backup restore fixtures. These are proposed engineering fixtures, not statistically powered proof of fairness or savings. Reject the candidate assembly on any unresolved cross-client leak, wage-authority bypass, silent source change, unapproved send or worse net reviewed effort.
