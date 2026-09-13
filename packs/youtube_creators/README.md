# YouTube creators and faceless-content operators

`youtube_creators` · **high** priority · business · status `queued`

**Client:** Tristan Grech (SUMERA) — access granted 2026-09-13

**Why:** Shaan given access to a live product in this vertical. SISO can own its own stack here and register it in the Great Library. Creator economy is a business vertical (operators monetise), not a consumer one.

**Existing SISO asset:** `github.com/tristangrech/sumera (PRIVATE, access granted 2026-09-13) — Next.js 16 / React 19 / TypeScript, Drizzle + Postgres (Supabase), Clerk auth, Stripe billing, @ai-sdk/anthropic + @ai-sdk/openai, AWS S3, Sentry, PostHog, Vercel`

**Verified state:** READ 2026-09-13 (shallow clone): REAL SHIPPED SAAS, not a prototype. 31 DB tables; modules for auth, billing, affiliates, referrals/rewards, courses+purchases, community (posts/comments/votes/moderation), script generation + editor, editor-handoff assets, video-generation jobs with credit grants/reservations/invoices, admin funnel + metrics, rate limiting, programmatic SEO (per-niche landing pages, llms.txt, IndexNow), cron jobs (daily digest, nightly metrics, return nudge). Scope is SCRIPT GENERATION + the monetisation/growth shell around it — NOT the full creator pipeline (no editing, thumbnails, scheduling, multi-platform publishing, analytics ingestion, sponsorship management). Covers roughly one workflow stage of many. NOTE: it is a strong reference for the SaaS BASE STACK (auth/billing/affiliate/community/admin) — cross-link to saas_base_stack.


## Run the research

Prompt: **https://siso-superapp-forge.pages.dev** → find `youtube_creators` → Copy research prompt.

## Files

| File | Holds |
|---|---|
| `00-SUMMARY.md` | One page. The person, segment, wedge, stack tax, spine, top 10 repos, gap list, verdict. |
| `01-person.md` | Who they are, what they get paid for, their Tuesday, 8+ quoted complaints with links, 5-10 segments. |
| `02-workflow.md` | 6-12 workflow stages with trigger, inputs, outputs, pain, frequency, handoff, data_object. Include the chat surface. |
| `03-companies.md` | Tier 1: 10+ big players. Tier 2: 10+ small-operator offerings. The gap between them. Per-stage tools with real prices. STACK TAX. |
| `04-oss-candidates.md` | 100+ repos examined, 3 lanes per workflow stage, loop until dry, judged last. Each marked ALREADY IN THE BANK or NEW. |
| `05-superapp.md` | The spine (3-6 data objects), component map, glue, build-vs-lift, deployment plan, gap list, architecture. |
| `06-value.md` | Stack tax replaced, hours returned, the wedge, migration cost, vertical economics, falsifier for the thesis. |

Every file is a placeholder until researched. Replace, don't append.

## Quotas

100+ repos examined · 10+ Tier-1 companies · 10+ Tier-2 offerings · 8+ quoted complaints ·
6-12 workflow stages. Report actual counts in `00-SUMMARY.md`.
