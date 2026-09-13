# US recruiting & staffing — super-app blueprint

> Research snapshot **2026-09-13**. `[vendor]` = upstream/provider claim; `[practitioner]` = attributed public report; `[analysis]` = our inference/design. No application deployed or candidate code executed.

**Verdict [analysis]: YES to a narrow supervised coordination pilot; NO to a wholesale ATS/payroll replacement.** The primary segment is a five-person US IT/professional W-2 contract-staffing desk, designed around 50 assignments and 12 clients. A real public co-founder account anchors the operator research; headcount, specialty, Tuesday and volumes remain an explicit design fixture, not an invented interview. [Person and 12 complaints](01-person.md).

**Wedge:** inbound conversation → source-linked JobOrder draft → missing-field review → human approval → incumbent ATS receipt. Preserve existing ATS authority, candidate consent and external payroll/ledger authority. No automated hiring decisions. [Workflow](02-workflow.md).

**Economics:** fixed public-price reference **$18,840/year**; later eligible retirements only **$2,760**, not the full stack. A supported integrated one-client-VPS plan budgets **$5,400/year**, including $528 paid on-premises signing integration, giving **$2,640 extra annual fixed cost before migration**. Minimal intake-only plan: $1,896/year versus at most $1,200 retired. The full-scope **5.58 hours/week** capacity hypothesis is **unmeasured**; actual cash and hours saved are null. [Prices](03-companies.md), [value and falsifiers](06-value.md).

**Spine:** Party · JobOrder · Candidacy · Assignment · WorkRecord · Conversation. Client owns one VPS, databases, accounts and off-box encrypted backups; no SISO-hosted application runtime. 16 GiB/8 vCPU is a planning envelope, not a tested floor. External network, payroll and legal services remain. [Assembly](05-superapp.md), [machine-readable architecture](05-assembly.json).

## Top ten selected repositories

| Repository | Verdict | Bounded reuse |
| --- | --- | --- |
| [frappe/frappe](https://github.com/frappe/frappe) | ADOPT | Frappe supplies forms, permissions, jobs and DocTypes for the six-object coordination spine. |
| [frappe/erpnext](https://github.com/frappe/erpnext) | ADOPT | Scoped ERPNext time, customer and draft-invoice modules; incumbent payroll and general ledger retain authority. |
| [chatwoot/chatwoot](https://github.com/chatwoot/chatwoot) | ADOPT | Chatwoot Community inbox for approved email/SMS channels; enterprise licensing and channel-service fees remain separate. |
| [surveyjs/survey-library](https://github.com/surveyjs/survey-library) | ADOPT | MIT schema-driven form core for versioned approved requisitions/feedback; paid Creator/Analytics are not included. |
| [alextselegidis/easyappointments](https://github.com/alextselegidis/easyappointments) | ADOPT | Self-hosted booking application; qualify calendars/time zones and premium feature boundaries before replacing Calendly. |
| [docusealco/docuseal](https://github.com/docusealco/docuseal) | ADOPT | Self-hosted signature UI; integrated production API requires paid Pro seats and completion fees, included separately in economics. |
| [activepieces/activepieces](https://github.com/activepieces/activepieces) | ADOPT | Optional Community connector executor with allowlists, idempotency and human-approved external writes; not an employment engine. |
| [jsvine/pdfplumber](https://github.com/jsvine/pdfplumber) | ADOPT | Local machine-generated PDF text/table extraction with source coordinates; preserve original files and reject unreadable scans to review. |
| [collective/icalendar](https://github.com/collective/icalendar) | ADOPT | Python RFC5545 calendar parsing/creation for persisted event identity, timezone and cancellation fixtures. |
| [moov-io/ach](https://github.com/moov-io/ach) | ADOPT | Moov ACH reader/writer/validator, restricted to file validation; banking/origination authority is not supplied by code. |

**Actual counts:** **138 unique repos examined** (140 requested, one alias duplicate and one failed lookup excluded); **50 already held / 88 new**; **14 ADOPT / 4 STEAL / 91 STUDY / 29 SKIP**; **10 Tier-1 companies**, **11 Tier-2 offerings**, **5 additional enterprise platforms**; **12 quoted complaints from 10 threads**; **12 workflow stages**, **9 subsegments**, **6 discovery rounds**, **10 material gaps**. Final two bounded in-scope discovery passes added no relevant candidates; failed requests were not counted as dry searches. [Full scored funnel](04-oss-candidates.md).

**Gap list:** US statutory payroll/tax authority; licensed sourcing data; screening/I-9/E-Verify services; ATS API/migration parity; complete staffing mappings; carrier/delivery services; paid signing/enterprise rights; state/local/privacy/accessibility review; measured capacity/security/restore/support; observed operator workload and eligible segment count.

**Next admission decision:** fund only an authorized intake pilot with source fidelity, permission isolation, retry/rollback and net reviewed-effort measurements. Reject if it adds reconciliation, sends stale/unapproved messages, bypasses employment/wage authority or cannot justify total operating/migration cost. No candidate application was executed and no deployment, savings, fairness or production-readiness claim is made.
