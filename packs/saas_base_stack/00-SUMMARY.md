# SaaS base stack — decision brief

**13 September 2026 · Horizontal template · Client-owned VPS only · Research status: PARTIAL**

[analysis] **Person/segment:** a designed, not interviewed, three-person US SaaS founder serving 200 self-service B2B workspace organizations at $50/month. Customers buy a usable, permissioned reporting workspace. The base handles acquiring, admitting, charging, helping and retaining those customers—not the product’s differentiating reporting logic. [Person](01-person.md) · [Workflow](02-workflow.md).

[analysis] **Wedge:** turn a verified “paid but cannot access” conversation into one evidence-linked account/subscription case and a human-approved correction. Start read-only. Never infer entitlement from an email match or screenshot. [Assembly](05-superapp.md).

[analysis] **Counts:** 132 distinct repositories examined; **98 ALREADY IN THE BANK / 34 NEW**; 15 conditional ADOPT, 85 STUDY, 27 SKIP, 5 STEAL-pattern decisions; 10 Tier-1 companies; 11 Tier-2 offerings; 8 practitioner complaints; 10 workflow stages; 12 assembly gaps; 27 bank submissions; 8 proposed corrections. Three search lanes cover every stage; 34 searches across four rounds. **Two consecutive zero-new rounds were not achieved**, so this is not honestly `complete`. [Repository funnel](04-oss-candidates.md).

[analysis] **Stack tax:** $11,623/year in the modeled basket, including $4,200 payment processing. Only $4,999 is potentially replaceable software; $6,624 is retained. Proposed host/backups $1,212 plus assumed maintenance $1,800 = $3,012/year. Conditional recurring difference **$1,987/year**; with assumed $3,000 migration, **first-year difference is −$1,013**. No cancelled invoices or savings were measured. [Commercial arithmetic](03-companies.md) · [Value case](06-value.md).

[analysis] **Spine:** Account · IdentityMembership · CommercialAgreement · ConversationCase · WorkItem · EvidenceEvent. Existing payment, support and task systems keep explicit authority; stable mappings and approval evidence join them.

## Top ten — not ten mandatory services

| Repository | Verdict / reuse | Bank |
|---|---|---|
| [wasp-lang/open-saas](https://github.com/wasp-lang/open-saas/blob/cbd30162b05d798b3a3f955ab5781940b67bec89/README.md) | ADOPT for trial — Integrated SaaS starter: auth, payments, email, jobs, landing, admin, docs/blog | ALREADY IN THE BANK |
| [chatwoot/chatwoot](https://github.com/chatwoot/chatwoot/blob/2f1ed80f894ed9a3eba636ebab90ca61deec110a/README.md) | ADOPT for trial — Shared conversation inbox and customer-facing support channels | ALREADY IN THE BANK |
| [stripe/stripe-node](https://github.com/stripe/stripe-node/blob/d9d092737b4a891f0beaf47c26c222972a4c7b0f/README.md) | ADOPT for trial — Official server-side Stripe API client | ALREADY IN THE BANK |
| [withastro/astro](https://github.com/withastro/astro/blob/7a698ca6e70d778343786cbf8fedd5f49d169ea4/README.md) | ADOPT for trial — Static-first content frontend | NEW |
| [nodemailer/nodemailer](https://github.com/nodemailer/nodemailer/blob/c7cc7ce41a3602441747476a2a2c4a8ff466a83e/README.md) | ADOPT for trial — Node.js email submission library | NEW |
| [formbricks/formbricks](https://github.com/formbricks/formbricks/blob/cd1c6a3d79d6d3dca9ee97e44f2e62f44f8dc474/README.md) | ADOPT for trial — Purpose-limited in-app, website and link surveys | ALREADY IN THE BANK |
| [umami-software/umami](https://github.com/umami-software/umami/blob/ca661c7057984aa98ed4f7083d84dae2f65bfcb0/README.md) | ADOPT for trial — Self-hosted web and event analytics on PostgreSQL | ALREADY IN THE BANK |
| [go-vikunja/vikunja](https://github.com/go-vikunja/vikunja/blob/bfc91c83536cf1d57676a7f31815bc9ba7af5138/README.md) | ADOPT for trial — Self-hosted task and handoff management | NEW |
| [caddyserver/caddy](https://github.com/caddyserver/caddy/blob/56e3a88efe39be6e380496778e7b94cb97f60c00/README.md) | ADOPT for trial — TLS-by-default web server and reverse proxy | ALREADY IN THE BANK |
| [restic/restic](https://github.com/restic/restic/blob/ba802d42b7294c98b62c16d1157ea3e80820c019/README.md) | ADOPT for trial — Encrypted backup and restore tooling | ALREADY IN THE BANK |

[analysis] **Gap list:** external payment/tax and delivery obligations; provider-channel approval; identity migration/MFA/SSO; actual-path licensing; untested event/link glue; imports/files/deletion; one-box failure and independent restore evidence; measured resources/maintenance; real customer baselines/population; feedback validity, editor usability and accessibility. Twelve explicit gap records are in [05-assembly.json](05-assembly.json).

[vendor] **Material correction:** Foundry defines positive `fame_gap` as adoption outrunning fame, not fame outrunning adoption. [Pinned scoring-loader explanation](https://github.com/sisodias/siso-foundry/blob/11f459597ce0c67dbfa89deeeafa3202e47dc6d5/pipelines/github/load_adoption_signal.py).

[analysis] **Verdict: YES to a bounded reusable-template and reconciliation pilot; NO to wholesale migration or a guaranteed-savings claim.** The 6.15-hours/week capacity illustration is wholly unmeasured; the narrow billing wedge contributes only 24 minutes/week in that fixture. No application code, client deployment, security certification or production admission was produced.
