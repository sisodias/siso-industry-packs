"""Render the reviewed recruiting research pack. No application or candidate code runs."""
import base64, collections, concurrent.futures, datetime, hashlib, json, os, pathlib, re, subprocess, tempfile, time, urllib.request
REPO='sisodias/siso-industry-packs'; P='packs/recruiting_staffing/'; E=P+'evidence/'; REV=os.environ['REQUEST_REVISION']; TOKEN=os.environ['GH_TOKEN']; DATE='2026-09-13'
assert os.environ['GH_REPOSITORY']==REPO
OUT={}; BASE='https://github.com/'+REPO+'/blob/main/'
def read(path):
    assert path.startswith((P,'registry/'))
    with urllib.request.urlopen('https://raw.githubusercontent.com/'+REPO+'/'+REV+'/'+path,timeout=90) as r:return r.read().decode()
def obj(path):return json.loads(read(path))
def put(path,value):
    assert path.startswith(P)
    OUT[path]=value if isinstance(value,str) else json.dumps(value,ensure_ascii=False,indent=2,allow_nan=False)+'\n'
def cell(x):
    if x is None:return 'null / not established'
    if isinstance(x,list):x='; '.join(map(str,x))
    return str(x).replace('|','&#124;').replace('\n',' ')
def table(headers,rows):return '| '+' | '.join(headers)+' |\n| '+' | '.join('---' for _ in headers)+' |\n'+''.join('| '+' | '.join(cell(c) for c in row)+' |\n' for row in rows)
def link(text,url):return '['+str(text)+']('+url+')'
def heading(title):return '# '+title+'\n\n> Research snapshot **2026-09-13**. `[vendor]` = upstream/provider claim; `[practitioner]` = attributed public report; `[analysis]` = our inference/design. No application deployed or candidate code executed.\n\n'
D=obj(E+'editorial-decisions.json'); C=obj(E+'commercial-price-ledger.json'); PERSON=read(P+'01-person.md')
complaints={}
for m in re.finditer(r'### (P\d+) — ([^\n]+)\n(.*?)(?=\n### |\n## |\Z)',PERSON,re.S):
    quote=re.search(r'^> (.+)$',m[3],re.M);url=re.search(r'\[Primary thread\]\((https://www.reddit.com/[^)]+)\)',m[3])
    if quote and url:complaints[m[1]]={'id':m[1],'author':m[2].split(':')[0],'quote':quote[1],'url':url[1],'evidence_class':'practitioner','observed_at':DATE,'posted_at':None}
assert len(complaints)==12
put(E+'complaints.json',{'observed_at':DATE,'complaints':list(complaints.values()),'unique_threads':len({x['url'] for x in complaints.values()}),'limitation':'Selected pseudonymous reports; not a representative survey, current-bug claim or independent observation of this design operator.'})
W=[dict(zip(D['workflow_columns'],r)) for r in D['workflow']]
for w in W:w.update({'pain':complaints[w['pain_id']],'evidence_class':'analysis','baseline_status':'unmeasured'})
put(P+'02-workflow.json',{'as_of':DATE,'scope':'Five-person US IT/professional W-2 contract staffing design fixture; no measured client baseline.','stages':W})
workflow_intro='''[analysis] This extends the four Foundry processes into twelve linked business stages, retaining the incumbent ATS as record authority during the pilot. The six root objects recur across stages: **Party, JobOrder, Candidacy, Assignment, WorkRecord, Conversation**. It is a potential coherent operating system, not twelve unrelated tabs. Attachments, approvals and events are child records/value objects, not reasons to duplicate the six roots. [Existing Foundry record](https://raw.githubusercontent.com/sisodias/great-library-of-siso/main/research/industries/source/intelligence/agency/industries/recruiting_staffing.json).

[analysis] The frequency column is a design workload, not practitioner measurement. The quoted pain is a workflow signal, not proof that every listed tool fails in that stage. P09/P10/P05 are adjacent signals for onboarding, time and payroll: no direct stage-specific operational interview was obtained. The [JSON](02-workflow.json) carries the same rows and full quotes.

'''
workflow_tail='''
## The chat surface and the conversion point

[analysis] The primary design channels are client-owned email, business SMS, phone and a web form, with authorized LinkedIn interaction. WhatsApp is optional only after the operator confirms actual usage and obtains an authorized Business Platform route; its prevalence for this US desk was **not established**. Phone calls require a human-entered source note unless recording/transcription has a separately approved consent and retention basis. [Practitioner intake complaint](https://www.reddit.com/r/recruiting/comments/1esqewk/can_anyone_share_their_experiences_with_loxo/); [Workspace](https://workspace.google.com/pricing.html); [Quo](https://www.quo.com/pricing); [WhatsApp app](https://whatsappbusiness.com/products/business-app/); [Platform pricing](https://whatsappbusiness.com/products/platform-pricing/); [LinkedIn](https://business.linkedin.com/hire/recruiter).

[analysis] Owner/recruiter answers client role enquiries, recruiter answers candidacy/interview questions, time coordinator answers assignment/time questions, and payroll/accounting owners handle pay/invoice issues. Proposed service targets—not measured promises—are triage within one staffed business hour, an explicit owner by end of day, and immediate escalation near wage/start deadlines. Never promise 24-hour human coverage from a five-person desk.

| Repeated-question hypothesis | Safe action | Authority boundary |
|---|---|---|
| Is the role still open / what are the approved terms? | Retrieve dated approved role facts; draft reply. | Stale/unapproved rates never auto-send. |
| Did you receive my CV / where is my application? | Acknowledge matching receipt and permitted status. | Do not expose other clients or infer rejection. |
| Can we book or move an interview? | Collect timezone/availability and propose valid slots. | Confirm identities, changed invitations and accommodation route. |
| What is missing before my start? | Show approved checklist status and responsible owner. | Restricted background/I-9 evidence stays outside general inbox. |
| Where is my timesheet approval, pay or invoice? | Link exact WorkRecord/provider receipt; route exception. | No autonomous wage, bank, tax or invoice-finalization decision. |

[analysis] These are five **hypotheses for coding real inbound traffic**, not a measured ranking of common questions. At the key transition, a message is linked to its immutable source ID, relevant Party is confirmed, approved fields are copied into a draft JobOrder, missing fields are queued, and a human approves the exact version before the ATS write. Store the external receipt and idempotency key. A reply, opt-out, job closure or version change cancels queued stale messages. This directly tests P03 and P07 rather than building an unsupervised chatbot.

## Approval is not permission to withhold wages

[vendor] US DOL guidance requires compensable worked time to be recorded/paid under applicable rules; an agency must not treat a client's billing approval as the legal trigger for earned wages. [DOL FLSA reference](https://www.dol.gov/agencies/whd/compliance-assistance/handy-reference-guide-flsa). [analysis] S09 therefore has separate submitted, client-approved, disputed, payroll-reconciled and invoiced states; unresolved time routes to the payroll owner before cutoff. This is a design guardrail, not a fifty-state wage-law review.
'''
put(P+'02-workflow.md',heading('02 — Workflow and the chat-to-order wedge')+workflow_intro+table(['id','stage','trigger','inputs','outputs','pain: quoted source','frequency','handoff','data_object'],[[w['id'],w['stage'],w['trigger'],w['inputs'],w['outputs'],'[practitioner] '+link('“'+w['pain']['quote']+'”',w['pain']['url']),w['frequency'],w['handoff'],w['data_object']] for w in W])+workflow_tail)

T1=[dict(zip(C['tier1_columns'],x)) for x in C['tier1']];T2=[dict(zip(C['tier2_columns'],x)) for x in C['tier2']];G=[dict(zip(C['generic_columns'],x)) for x in C['generic']];ENT=[dict(zip(C['enterprise_columns'],x)) for x in C['enterprise']]
company_intro='''## Sequence, scale and price discipline

[analysis] The commercial pass was researched and written before the new upstream repository sweep; the [dated ledger](evidence/commercial-price-ledger.json) preserves its configured prices. Tier 1 is **ten actual staffing/talent-service companies**, not software vendors relabeled as agencies. Five enterprise software platforms are additional; Tier 2 is **eleven smaller-operator offerings**. The ceiling/floor comparison is functional, not a revenue-ranked top-ten claim.

[analysis] Prices observed 2026-09-13 use five internal users, two signing users and 55 payroll people (50 assignments plus five internal staff). Public list prices are real source evidence; quantities, plan selection and annualization are our assumptions. `null` means unverified/quote required, not zero. Taxes, variable usage and implementation are excluded. Workable's employer-headcount bracket cannot be equated with five recruiter seats. Gusto's price is a benchmark **pending acceptance of this staffing business**, not evidence of provider eligibility.

## Tier 1 — operating-capability ceiling (10)

[vendor] Sources below describe service lines and digitized surfaces. [analysis] Human-role columns identify service counterparts, not measured residual hours or proof of autonomous decisions. **All ten agency-specific annual service prices are null / written quote required.** No guessed markup or salary percentage fills the gaps.

'''
company=heading('03 — Companies, tool ownership and stack tax')+company_intro+table(['Company/source','Service/product families [vendor]','Digitized surface [vendor]','Human boundary / measurement limit','Buyers [vendor]'],[[link(x['name'],x['url']),x['services'],x['automation'],x['humans'],x['customers']] for x in T1])
company+='\n## Enterprise software layer (5 additional platforms)\n\n'+table(['Platform/source','Coverage [vendor]','Pricing evidence [vendor]','Integration/authority boundary [analysis]'],[[link(x['name'],x['url']),x['capabilities'],x['pricing'],x['integration_boundary']] for x in ENT])
company+='\n## Tier 2 — small-operator offerings (11)\n\n'+table(['Offering/source','Published pricing [vendor]','Annual USD [analysis]','Quantity/edition basis','Capability [vendor]','API/integration limit','Lock-in [analysis]','Practitioner signal'],[[link(x['name'],x['url']),x['pricing'],x['annual_usd'],x['basis'],x['capabilities'],x['integration'],x['lockin'],'; '.join(link(pid,complaints[pid]['url']) for pid in x['complaint_ids'])] for x in T2])
company+='\n[analysis] '+C['complaint_scope']+' The twelve complete quotations and counterevidence are in [Stage 1](01-person.md). No product-specific complaint was verified for several generic/enterprise tools; that absence is retained rather than filled with invented negative reviews.\n'
company+='''
## The gap between tiers

[analysis] Enterprise service firms show assignment, workforce-program, time/pay/bill and specialist-service capability around the recruiting funnel. Entry software often sells seats, sourcing and pipelines; API access, external-client permissions, contractor operations and back-office services may be separate editions or quotes. The opportunity is **shared identity, approval and evidence across those handoffs**, not pretending open-source code replaces recruiter relationships, payroll authority or licensed candidate networks. Sources and entitlement caveats are the tables above; no causal savings are established by vendor marketing.

## The unglamorous operating stack

'''+table(['Tool/source','Annual USD [analysis]','Pricing basis','Capability [vendor, except manual scenario]','Integration surface','Lock-in [analysis]'],[[link(x['name'],x['url']),x['annual_usd'],x['basis'],x['capabilities'],x['integration'],x['lockin']] for x in G])
company+='''
### Recover the spreadsheet specification, not a fictional spreadsheet

[practitioner] P01 reports an agency chiefly using Excel despite paying for an ATS. **The actual workbook was not accessed**; its columns, formulas and maintainer are unknown. [Primary report](https://www.reddit.com/r/Recruitment/comments/1isk1r4/best_permanent_placement_atscrm/).

[analysis] In the first authorized discovery session, recover client/candidate/job/assignment IDs; representation status; effective pay/bill rates; start/end dates; actual hours and approval; payroll receipt; PO/invoice/payment IDs; consent and next-action owner. Identify who owns every column, repairs each formula and handles exceptions when absent. Airtable/Notion/Monday/ClickUp adapted into these records is the missing-module specification, not proof those exact columns exist today. Reconcile counts, formulas, permissions and exports before switching off anything. Paper/phone/memory may have low technical switching cost but still hide labor and tacit knowledge.

## Workflow ownership — 2–5 tools each

[analysis] Repeated tools are purchased once, not once per stage. Price and entitlement fields above apply to each occurrence. P10/P09/P05 are adjacent risk signals for S08–S11, not firsthand complaints about each listed tool.

'''+table(['Stage','Current tools/alternatives','Quoted workflow pain','Persistent switching object'],[[w['id']+' '+w['stage'],w['commercial_tools'],link('“'+w['pain']['quote']+'”',w['pain']['url']),w['data_object']] for w in W])
stack=C['stack_tax']['selected'];assert sum(stack.values())==18840
company+='\n## STACK TAX — coherent reference basket\n\n'+table(['Selected once','Annual USD'],list(stack.items())+[['TOTAL fixed reference',sum(stack.values())]])
company+='''
[analysis] Arithmetic: **$3,300 + $840 + $1,200 + $1,680 + $8,880 + $960 + $1,380 + $600 = $18,840/year.** This is a configured price basket, not observed expenditure, a staffing-eligible contract quote or recoverable cash. All-in annual spending stays null: add actual sourcing/job-board licences, screening, carrier usage/registration, payment processing, statutory costs/benefits, funding/insurance, support and migration.

'''
alt=sum(x['annual_usd'] or 0 for x in T2+G);assert alt==61674
company+=f'[analysis] Literal purchase of every numerically priced Tier-2 and generic alternative would sum to **${alt:,}/year**; including the separately priced Bullhorn Starter reference gives **${alt+5940:,}**. These deliberately redundant totals are NOT savings and do not include quote-only products. A literal total for all products/services in this report is **undefined**, not a fabricated finite number. The registry uses the coherent $18,840 basket.\n\n'
company+='''[analysis] Variable-payment example: 12 clients x 4 invoices/month x 12 x the $5 ACH cap = **$2,880/year**, only if every payment is at least $625. Both frequency and invoice size are unmeasured assumptions; payment fees survive self-hosting. [Stripe](https://stripe.com/pricing).

### Signing edition correction, carried into the value case

[vendor] DocuSeal on-premises API/embedding requires Pro at $20/user/month plus $0.20 per completed document; its FAQ explicitly applies completion fees on-premises. Free manual signing is a different capability. [Official pricing](https://www.docuseal.com/pricing). [analysis] Two sender seats and 240 completions/year imply **$528/year**, not zero; 240 is an assumed workload and any more restrictive quote controls. Monthly list annualization is used because annual-offer wording on the page is inconsistent. This additional self-hosted cost is not counted as an incumbent expense in the $18,840 basket.

## Commercial handoff to OSS discovery

[analysis] Search artifact classes for approved intake, source CV extraction, ATS/CRM bridges, staffing interchange schemas, calendar protocols, signature evidence, effective assignment rates, worked-time/payroll files, invoice/payment reconciliation and redeployment. UI libraries are already held in SISO's component bank; generic infrastructure is inherited from selected product bases. A scraper, payroll-file writer or signature badge does not supply network rights, tax correctness or legal authority.
'''
put(P+'03-companies.md',company)

with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:raw=list(pool.map(lambda i:obj(E+f'repo-{i:03d}.json'),range(1,141)))
byid={r['audit_id']:r for r in raw};decisions={r[0]:dict(zip(D['decision_columns'],r)) for r in D['decisions']};rows=[];seen=set();excluded=[]
for r in raw:
    n=r.get('full_name')
    if not n:excluded.append({'audit_id':r['audit_id'],'requested':r['requested_full_name'],'reason':'GitHub NOT_FOUND; excluded from examined count'});continue
    if n.lower() in seen:excluded.append({'audit_id':r['audit_id'],'requested':r['requested_full_name'],'canonical':n,'reason':'Canonical alias duplicate; excluded from examined count'});continue
    seen.add(n.lower());d=decisions[r['audit_id']];readme=r.get('readme') or {};lic=r.get('license_file') or {};api_license=(r.get('license') or {}).get('spdxId')
    license_name=D['license_overrides'].get(r['audit_id']) or (api_license if api_license and api_license!='NOASSERTION' and lic.get('characters_read') else 'UNRESOLVED; see actual file/metadata discrepancy')
    if not lic.get('characters_read'):license_name='UNRESOLVED root licence; GitHub metadata: '+str(api_license)
    recent=sum(c['date']>='2026-03-13' for c in r.get('recent_commits',[]));affiliated=sum(c['authorAssociation'] in ('OWNER','MEMBER','COLLABORATOR') for i in r.get('issue_sample',[]) for c in i.get('comments',{}).get('nodes',[]))
    health=0 if r.get('archived') else (min(3,2+int(affiliated>0)) if recent else 1)
    adoption_rows=r.get('adoption_evidence',[]);deps=[a for a in adoption_rows if a.get('resolved')==1 and ((a.get('dependent_repos') or 0)>0 or (a.get('dependent_pkgs') or 0)>0)]
    adoption=3 if any((a.get('dependent_repos') or 0)>=100 for a in deps) else (2 if deps else 0)
    scores={'fit':d['fit'],'liftability':d['liftability'],'health':health,'adoption':adoption,'integration':d['integration']}
    external=r['audit_id'] in {f'R{i:03d}' for i in range(69,92)}|{'R061','R062','R070','R125','R130','R138','R139'}
    row={**d,'full_name':n,'url':r['html_url'],'stars':r['stargazers_count'],'observed_at':r['observed_at'],'last_commit':r['last_commit'],'revision':r['revision'],'archived':r['archived'],'license':license_name,'license_api_metadata':r.get('license'),'license_source':lic.get('source_url'),'license_sha256':lic.get('sha256'),'license_scope':'Root plus explicit audited exclusions only; per-file/module/dependency rights still require production qualification.','readme_source':readme.get('source_url'),'readme_sha256':readme.get('sha256'),'readme_characters_retrieved':readme.get('characters_read',0),'scores':scores,'score_class':'analysis','score_method':'Contextual editorial fit/lift/integration; bounded metadata health; adoption is evidence support, not actual usage quality.','recent_commits_in_10_commit_sample':recent,'affiliated_comments_in_3_issue_sample':affiliated,'bus_factor':'unknown','representative_issue_response_time':None,'adoption_evidence':adoption_rows,'fame_gap_direction':'Not scored: bank README and pinned Foundry loader describe opposite directions; preserve raw evidence.','bank_status':r['bank_status'],'bank_revision':r['bank_revision'],'bank_membership_layers':r['bank_membership_layers'],'resource_floor_gib':None,'resource_floor_status':'Unmeasured; do not infer from stars or Docker availability. Stage 5 supplies a planning envelope, not certification.','self_hosting':('Connector/library can be local but useful operation depends on authorized external account/network; not a self-contained replacement.' if external else 'Local candidate/pattern; no deployment was executed or production footprint measured.'),'evidence_class':'analysis','upstream_claim_class':'vendor','evidence_receipt':BASE+E+f"repo-{int(r['audit_id'][1:]):03d}.json",'qualification':D['qualification']}
    rows.append(row)
assert len(rows)==138 and len(decisions)==138 and {r['audit_id'] for r in rows}==set(decisions)
counts=collections.Counter(r['verdict'] for r in rows);members=collections.Counter(r['bank_status'] for r in rows);assert sum(members.values())==138
R={r['audit_id']:r for r in rows};query_rounds=[obj(E+f'search-round-{i:02d}.json') for i in range(1,7)]
query_count=sum(len(x['queries']) for x in query_rounds);success=sum(not q.get('error') for x in query_rounds for q in x['queries']);lanes={(q['stage'],q['lane']) for x in query_rounds for q in x['queries'] if not q.get('error')}
put(P+'04-oss-candidates.json',{'as_of':DATE,'counts':{'requested':140,'examined':138,'bank':dict(members),'verdicts':dict(counts),'root_licenses_retrieved':sum(bool(r['license_source']) for r in rows),'readmes_retrieved':sum(bool(r['readme_characters_retrieved']) for r in rows),'search_rounds':6,'recorded_query_attempts':query_count,'successful_queries':success,'successful_stage_lane_pairs':len(lanes)},'excluded':excluded,'repositories':rows})
oss=heading('04 — Open-source and source-available candidate funnel')+f'''## Actual funnel and method

[analysis] **140 requested names → 139 retrieved records → 138 canonical repositories examined.** One requested name did not resolve; one was an alias duplicate. {members['ALREADY IN THE BANK']} were **ALREADY IN THE BANK** and {members['NEW']} were **NEW** against the six exported repo-bearing bank layers at `{rows[0]['bank_revision']}`. Shelf presence means already held, NOT product admission. Broader private identity data was not searched. [Collector receipt](evidence/candidate-audit-receipt.json); [editorial decisions](evidence/editorial-decisions.json); [machine-readable complete table](04-oss-candidates.json).

[analysis] Examination means current GitHub identity/stars/HEAD, root entries, retrieved README/licence text and hashes, bounded recent-commit/issue samples, bank joins and an individual editorial decision. It is **not** a full security audit, runtime execution, legal clearance, measured adoption or production certification. Missing README/licence is a documented rejection or qualification gap, never an invented file. All mutable values use each row's observation timestamp. HEAD pins reproduce research, not compatible production releases.

### Search breadth before judgment

[analysis] Six recorded rounds comprise **{query_count} query attempts, {success} successful queries and {len(lanes)} distinct successful stage/lane pairs**. A = practitioner keywords, B = topics, C = formats/protocols. Failed/rate-limited queries are retained and were re-covered rather than counted as dry results. [Round 1](evidence/search-round-01.json), [2](evidence/search-round-02.json), [3](evidence/search-round-03.json), [4](evidence/search-round-04.json), [5](evidence/search-round-05.json), [6](evidence/search-round-06.json).

[analysis] Artifact classes included whole ATS/ERP/inbox apps; parsers/SDKs; workflow/payroll engines; HR-XML/SETU/JSON Resume/ESCO/O*NET/iCalendar/NACHA/OFX/OpenAPI formats; OCA and ATS bridges; and awesome/catalogue sources. Upstream dependency and maintainer follow-through included EasyAppointments' `sabre/vobject`, Frappe dependency manifests, Bullhorn's SDK/import tools, Intuit/Xero clients and SETU XML/ontology siblings. This is targeted vertical coverage, not a second UI-framework survey. Generic forms/infrastructure from the bank are represented once and reused.

[analysis] Round 5 returned five new **off-scope** names (ambiguous SETU matches), zero relevant staffing candidates; round 6 returned zero new names. Thus the last **two declared, bounded in-scope frontier passes** added no relevant candidates. This is not an exhaustive global GitHub saturation claim: first-page limits and remaining large topic spaces are visible in receipts. The search stops on that explicit boundary, not by interpreting errors as zero results.

### Scoring and interpretation

[analysis] Five 0–5 scores are separate, not averaged into false precision: **F** = fit to the selected staffing handoff; **L** = detachable reuse (library 5, service/tool 3–4, app 2, independent pattern 1); **H** = bounded activity evidence (archived 0, older activity 1, recent commits 2, recent plus sampled affiliated issue participation 3; no project earns 4–5 without deeper health evidence); **A** = adoption evidence support (0 unknown, 2 resolved dependent evidence, 3 at least 100 bank-recorded dependent repos; none earns 4–5 on this read); **I** = integration with the six objects, accounting for external dependencies. No-star-based adoption score. Bus factor and representative response latency remain unknown for all projects, even when issues have comments or are closed.

[analysis] A=0 means **not established**, not no users. Existing bank package/dependent data is dated independently from today's repository stars. Dedupe has resolved dependence evidence; most whole apps lack comparable package telemetry. `fame_gap` is retained but no directional penalty is applied: [bank README](https://github.com/sisodias/siso-repo-bank/blob/main/README.md) and [pinned Foundry loader](https://github.com/sisodias/siso-foundry/blob/11f459597ce0c67dbfa89deeeafa3202e47dc6d5/pipelines/github/load_adoption_signal.py) describe opposing directions. The shared correction is preserved for producer-level reconciliation.

[analysis] **ADOPT = {counts['ADOPT']}**, **STEAL = {counts['STEAL']}**, **STUDY = {counts['STUDY']}**, **SKIP = {counts['SKIP']}**. ADOPT selects a bounded future assembly component, not an executed/deployed product. STEAL means independently adapt the pattern, never unlicensed copying. Licences do not exclude discoveries from the funnel, but enterprise terms, source availability and reuse obligations must be resolved before deployment. A missing licence is unresolved, not permissive.

## Complete examined table

Each name links to upstream, commit date to the pinned revision, and licence to the actual fetched file where available. `[vendor]` identity/capability sources are in the linked receipts; verdict and one-line reuse judgment are `[analysis]`. Runtime/footprint and external-account qualifications are also in the JSON, with unknown floors left null.

'''
oss+=table(['ID / repository','Bank status','Stars (observed 2026-09-13)','Actual licence / unresolved','Last commit (UTC)','F/L/H/A/I','Verdict','What it gives us [analysis]'],[[r['audit_id']+' '+link(r['full_name'],r['url']),r['bank_status'],r['stars'],link(r['license'],r['license_source']) if r['license_source'] else r['license'],link(r['last_commit'],r['url']+'/commit/'+r['revision']),'/'.join(str(r['scores'][k]) for k in ['fit','liftability','health','adoption','integration']),r['verdict'],r['what_it_gives_us']+' '+link('evidence',r['evidence_receipt'])] for r in rows])
oss+='\n## Excluded identities (not extra repositories)\n\n'+table(['Requested audit entry','Reason'],[[x['audit_id']+' '+x['requested'],x['reason']] for x in excluded])
oss+='''
## Carry-forward, source exceptions and taxonomy findings

[analysis] Foundry's Activepieces shape remains allowlisted/idempotent coordination with human approval before external writes. SurveyJS remains an owned approved-field/versioned-response form layer, not a separate candidate system of record. Cal.diy remains reference-only under its current production warning; `calcom/cal.com` resolves to the same repository and does not add a second examined project. [Foundry record](https://raw.githubusercontent.com/sisodias/great-library-of-siso/main/research/industries/source/intelligence/agency/industries/recruiting_staffing.json).

[analysis] Important exceptions: OpenCATS is active and has mixed original/current terms, not a dead permissive project; JSON Resume's old schema repository points to the monorepo package; Chatwoot/Activepieces/OpenSign have explicit commercial exclusions; Invoice Ninja, Akaunting and SlowBooks are source-available rather than ordinary permissive-code substitutes. These are documented findings, not automatic rejections. Superseded discoveries not already in the bank are not falsely labeled corrections to an existing SISO rating.

[analysis] A useful connector may run locally while its value remains external: Bullhorn/Greenhouse/Lever/Intuit/Xero require client accounts; Conductor's Desktop SDK requires its hosted service and a Desktop installation; TempGuru exposes vendor event-staffing data rather than a self-hosted worker network. Alternatives are approved exports/local coordination and retained providers, with loss of live network/desktop functionality explicitly accepted. Cal.diy's production substitute is EasyAppointments; no qualified OSS substitute for full US statutory payroll was established.

[analysis] The canonical tags are retained for import, but `workflow-orchestration` is too coarse for agency ATS/CRM and time/pay/bill product bases. Proposed additional tags: **staffing-ats-crm**, **workforce-time-pay-bill**, **employment-data-interchange**. These are proposals, not silently added official tags. No UI component-library research was performed; existing bank/component-bank layers supply that part.
'''
put(P+'04-oss-candidates.md',oss)

objects=[
 {'name':'Party','fields':['id','person_or_organization','external_ids','contact_methods','consent_versions','role_scoped_visibility'],'authority':'Incumbent identity plus reviewed link; no autonomous fuzzy merge.'},
 {'name':'JobOrder','fields':['id','client_party_id','external_ats_id','approved_requirements','terms_version','approver_id','effective_dates'],'authority':'Client/account approver; approved ATS version remains authoritative in pilot.'},
 {'name':'Candidacy','fields':['id','candidate_party_id','job_order_id','representation_consent','submitted_artifact_hash','human_status','feedback_refs'],'authority':'Recruiter and hiring authority; never model-derived selection.'},
 {'name':'Assignment','fields':['id','candidacy_id','employer_party_id','client_party_id','work_location','start_end','effective_rate_versions','provider_ids'],'authority':'Authorized employment/commercial signatories and payroll owner.'},
 {'name':'WorkRecord','fields':['id','assignment_id','period','dated_hours','expenses','revision','client_approval','payroll_receipt','invoice_refs'],'authority':'Worker reports; client approves billing; payroll and accountant retain separate wage/ledger authority.'},
 {'name':'Conversation','fields':['id','channel','provider_thread_id','participants','source_message_ids','linked_objects','consent','owner','reply_state'],'authority':'Client-owned channel and role-scoped staff; external sends through approval outbox.'}
]
component_map=[
 {'stages':['S01','S02','S12'],'chosen':['R010','R031','R035'],'runners_up':['R024','R032','R033','R140'],'ours':'Party/JobOrder/Conversation links, versioned intake and approved outbox.','why':'Frappe owns structured workflow and Chatwoot conversation context; avoid parallel sales databases. LibreDesk remains lean-inbox counterfactual.'},
 {'stages':['S03','S04','S05'],'chosen':['R121','R123','R035','R010'],'runners_up':['R053','R055','R122','R124'],'ours':'Source-artifact retention, approved extraction fields and Candidacy permissions.','why':'Local bounded extraction beats inferred strengths or a new JVM/model runtime; failed extraction goes to humans.'},
 {'stages':['S06'],'chosen':['R036','R049','R132'],'runners_up':['R037','R044','R045','R050'],'ours':'Candidacy-to-booking identity, timezone/version/cancellation reconciliation.','why':'Whole booking application plus protocol libraries; Cal.diy production warning is disqualifying for this role.'},
 {'stages':['S07','S08'],'chosen':['R039','R010'],'runners_up':['R040','R041','R026','R127','R128'],'ours':'Assignment authorization, signer-role mapping and restricted readiness checklist.','why':'Established signing UI with explicit priced API boundary; early Frappe-native signing remains a service-removal counterfactual, not current admission.'},
 {'stages':['S09','S10','S11'],'chosen':['R009','R088','R092'],'runners_up':['R027','R028','R030','R096','R108'],'ours':'Effective rates, WorkRecord versioning, separate wage/bill states and reviewed provider exports.','why':'Keep one operational schema; retain external payroll and general ledger. ACH validation does not originate money.'},
 {'stages':['S01','S05','S10','S11','S12'],'chosen':['R034','R012'],'runners_up':['R018','R011','R069','R072'],'ours':'Only missing authorized adapters, idempotent receipts and deployment configuration.','why':'Optional connector engine only where it removes custom adapter work; migration tools are per-client, not default resident services.'}
]
for m in component_map:
    m['chosen']=[{'audit_id':i,'full_name':R[i]['full_name'],'verdict':R[i]['verdict'],'research_revision':R[i]['revision']} for i in m['chosen']]
    m['runners_up']=[{'audit_id':i,'full_name':R[i]['full_name']} for i in m['runners_up']]
assembly={'slug':'recruiting_staffing','as_of':DATE,'status':'research-blueprint; not deployed or production-qualified','deployment':'client_vps','one_compute_box_per_client':True,'siso_hosted_runtime':False,'objects':objects,'component_map':component_map,'default_product_bases':['frappe/frappe','frappe/erpnext','chatwoot/chatwoot'],'deployment_artifact':'frappe/frappe_docker','optional_services':['activepieces/activepieces','alextselegidis/easyappointments','docusealco/docuseal'],'libraries':[R[i]['full_name'] for i in D['libraries']],'external_authorities':['incumbent ATS','client payroll provider','client accounting ledger','authorized email/SMS/WhatsApp networks','licensed talent sources','screening/government/banking services'],'runtime_plan':{'full_reference_gib':16,'full_reference_vcpu':8,'measured_resource_floor_gib':None,'lean_trial_gib':8,'lean_scope':'Minimal Frappe intake coordination only; no assertion that full Chatwoot/signing/automation assembly fits.','gpu_required':False,'backup':'Encrypted, off-box, client-owned storage; never SISO storage.','qualification':'Load/restore/security tests and compatible release/image digests required before any production deployment.'},'economics':D['economics'],'gaps':D['gaps'],'measured_outcomes':None,'application_code_written':False,'upstream_code_executed':False}
put(P+'05-assembly.json',assembly)
spine=table(['Root object','Key persisted fields','Authority'],[[o['name'],o['fields'],o['authority']] for o in objects])
map_table=table(['Stages','Chosen component / verdict','What we write','Why these beat named runners-up'],[[m['stages'],'; '.join(link(c['full_name'],R[c['audit_id']]['url'])+' '+c['verdict'] for c in m['chosen']),m['ours'],m['why']+' Runners-up: '+', '.join(x['full_name'] for x in m['runners_up'])] for m in component_map])
superapp=heading('05 — The assembled staffing operating system')+'''## Thesis and scope

[analysis] Build an **evidence-preserving coordination layer around the incumbent ATS**, not an unsupervised hiring engine or a replacement payroll bureau. The client owns one VPS, accounts, databases, keys and backups. Nothing in the application runs on SISO servers. Client-owned external payroll, ledger, carrier, sourcing and government services remain explicit dependencies; a Linux process cannot replace their legal authority or network access. [Foundry boundary](https://raw.githubusercontent.com/sisodias/great-library-of-siso/main/research/industries/source/intelligence/agency/industries/recruiting_staffing.json); [workflow](02-workflow.md).

## 1. The six-object spine

[analysis] Our differentiated schema is the following set of roots. Source files, messages, approval events and rate revisions are child entities with hashes and retention labels. Candidate identities and candidacies are separate: one person can legitimately have several client-specific applications. An assignment is not just an ATS stage label; it carries employer, commercial and effective-date authority.

'''+spine+'''
[analysis] During the pilot, external IDs plus immutable source links anchor records; the spine may own coordination state and approved mappings, not silently replace source facts. Every changed approved requirement or rate creates a new version with an effective interval. No generic last-write-wins sync may overwrite an employment decision, approved rate or signed artifact.

## 2. Component selection and named counterfactuals

All ADOPT selections below are conditional on release, rights, security and workflow qualification. Detailed upstream evidence, licences and research pins are in [Stage 4](04-oss-candidates.md); these are not live deployment pins.

'''+map_table+'''
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

'''+table(['Gap','What remains external or unmeasured'],[[str(i+1),g] for i,g in enumerate(D['gaps'])])+'''
[analysis] These mean **no qualified replacement was established by this bounded search**, not that no open-source code can ever exist. Current government sources address part of the old EEOC retrieval gap, but this is not a state/local legal opinion or accessibility certification. [EEOC/DOJ warning](https://www.eeoc.gov/newsroom/us-eeoc-and-us-department-justice-warn-against-disability-discrimination); [NYC AEDT](https://www.nyc.gov/site/dca/about/automated-employment-decision-tools.page); [FTC background checks](https://www.ftc.gov/business-guidance/resources/background-checks-what-employers-need-know).

[analysis] Before a pilot: authorize the data map and roles; reconcile an export; test 50 reviewed requisitions, 50 scheduling changes and one complete payroll reconciliation cycle. Include duplicate/reordered webhook, stale role, withdrawal, wrong recipient, lost attachment, DST, rate change, partial payroll failure, invoice retry, restricted-client access and backup restore fixtures. These are proposed engineering fixtures, not statistically powered proof of fairness or savings. Reject the candidate assembly on any unresolved cross-client leak, wage-authority bypass, silent source change, unapproved send or worse net reviewed effort.
'''
put(P+'05-superapp.md',superapp)

value=heading('06 — Value case, costs and falsifiers')+'''## Decision

[analysis] **YES to a bounded, paid coordination pilot; NO to replacing the agency's ATS, payroll bureau, sourcing network and ledger with an unqualified OSS suite.** Lead with conversation-to-approved-requisition, not a wholesale migration. The existing Foundry recommendation survives the wider sweep. [Foundry record](https://raw.githubusercontent.com/sisodias/great-library-of-siso/main/research/industries/source/intelligence/agency/industries/recruiting_staffing.json); [assembly](05-superapp.md).

## Stack tax versus honestly replaceable spend

[analysis] The configured fixed reference stack is **$18,840/year**, not observed expenditure. Potential later retirements are Airtable $1,200 + Calendly $960 + Dropbox Sign $600 = **$2,760/year**, and only after functional parity and actual cancellations. The first intake wedge can at most target the $1,200 Airtable line; even that saving is zero until it is really removed. Payroll $8,880, ATS $3,300, Workspace $840, Quo $1,380 and QuickBooks $1,680 total **$16,080 retained** in the later scenario. [Dated source/price ledger](03-companies.md).

| Scenario [analysis] | Run cost/year | Incumbent costs eligible to retire | Net fixed-cost change before migration |
|---|---:|---:|---:|
| Minimal intake pilot; less functionality, existing communications retained | $576 compute + $120 backup + $1,200 support = **$1,896** | At most **$1,200**, cancellation required | **$696 additional cost** |
| Supported integrated coordination, booking and signing reference | $1,152 compute + $120 backup + $3,600 support + $528 signature = **$5,400** | At most **$2,760**, three cancellations required | **$2,640 additional cost** |

[analysis] Full steady reference: $16,080 retained + $5,400 proposed run = **$21,480/year** versus $18,840. Do not sell this as automatic licence savings. Support assumptions are respectively 1 or 3 hours/month at an assumed $100/hour; backups are a $10/month planning allowance. Compute uses published plan prices, not measured resource requirements. [DigitalOcean](https://www.digitalocean.com/pricing/droplets).

[vendor] DocuSeal's production API/embedding remains paid on-premises. [Pricing](https://www.docuseal.com/pricing). [analysis] The integrated scenario assumes 2 seats x $20/month x 12 plus 240 completions/year x $0.20 = **$528**. Free manual UI could avoid that fee but loses the integrated capability; it cannot support the same automation claim. More documents, paid SSO/RBAC/modules, carrier fees, incidents, taxes and resource expansion increase costs. No cancellation, contractual eligibility or production-price quote was verified.

## Hours returned — hypothesis, never dressed as measurement

[analysis] The following quantities are team-wide design fixtures from [Stage 2](02-workflow.md), not employee diaries. Measure before/after human minutes **including approval, correction, exception handling and reconciliation**. Do not add overlap between stages or value candidate waiting time as saved staff labor.

| Workflow unit | Weekly units (assumed) | Baseline min/unit (unmeasured) | Proposed reviewed min/unit (unmeasured) | Hypothesized minutes returned |
|---|---:|---:|---:|---:|
| Complete approved requisition | 20 | 5 | 3 | 40 |
| Accurate approved status coordination | 80 | 3 | 2 | 80 |
| Correct interview scheduling/change | 20 | 10 | 6 | 80 |
| Worked-time review including exceptions | 50 | 4 | 2.5 | 75 |
| Payroll/invoice evidence reconciliation packet | 12 | 15 | 10 | 60 |
| **Full-scope total** | | | | **335 min = 5.58 hours/week** |

[analysis] At 48 working weeks this is **268 capacity hours/year**, not payroll reduction. An assumed $40/hour shadow value gives $10,720 of capacity; realized cash remains **null** until an actual avoided cost or incremental contribution is evidenced. The intake-only pilot earns only its measured share (the 40-minute hypothesis), not the entire 335-minute full-system estimate. Net outcomes must subtract new support/admin/rework. Baseline data, standard errors, adoption, retention, fairness, wage correctness and accessibility outcomes were not measured.

[analysis] A full-scope sensitivity test is more useful than a savings promise: with $2,640 extra annual fixed costs, pure operating break-even at an assumed $40/hour requires 66 genuinely valuable staff hours/year (1.38 hours/week over 48 weeks), **before migration and shared engineering**. At zero monetizable capacity, the cash case is negative. These assumptions are decision aids, not evidence.

## The wedge and migration sequence

[analysis] One door: preserve the inbound email/thread, approve a complete JobOrder and write it once to the existing ATS with a receipt. P07 reports manual employer/client intake; P03 reports reply-unaware automation. [P07](https://www.reddit.com/r/recruiting/comments/1esqewk/can_anyone_share_their_experiences_with_loxo/); [P03](https://www.reddit.com/r/recruiting/comments/1mmi61u/has_anyone_else_had_a_terrible_experience_with/). The proposed advantage is less retyping and traceable exceptions, not a smarter employment-decision model. Actual superiority remains to be tested.

[analysis] Phase A: authorized read-only export and source/permission map. Phase B: parallel intake drafts and measured reviewer effort. Phase C: explicitly approved limited ATS writes with rollback/reconciliation. Phase D: separately qualify scheduling, time and signing. Only then cancel eligible tools. Full ATS and statutory payroll migration are separate projects, not hidden inside this wedge.

## Migration cost — real work, assumed rates

| Repeatable onboarding task [analysis] | Second-client labor assumption |
|---|---:|
| Export/contract/API entitlement and data inventory | 4–6 h |
| Identity, source-field and permissions mapping | 6–10 h |
| Client-owned account/channel/secret configuration | 4–6 h |
| Import reconciliation and exception fixtures | 8–14 h |
| Training, parallel acceptance and rollback/restore check | 6–12 h |
| Handoff and operating runbook | 4–8 h |
| **Second client total** | **32–56 h = $3,200–$5,600 at assumed $100/h** |

[analysis] First-client migration/onboarding allowance: **60–100 hours = $6,000–$10,000** at the same assumed rate. These are explicit planning estimates, not vendor quotes or measurements; vendor exit charges, history/attachment exports, API tier upgrades and custom integrations are additional. Shared product engineering is **unpriced**, not zero, until a field map and delivery estimate exist. A second deployment removes reusable assembly/design work, not client-specific permissions, data cleanup and account authorization. [Commercial lock-in register](03-companies.md).

## Vertical economics — count the right buyers

[vendor] ASA reports approximately **27,000 US staffing/recruiting companies and 54,000 offices in 2021**. This is a historical parent-industry figure, not a 2026 count of eligible IT contract desks. [ASA statistics](https://americanstaffing.net/research/fact-sheets-analysis-staffing-industry-trends/staffing-industry-statistics/). [analysis] The exact number of US five-person/professional-W-2-contract operators satisfying this workflow and API/privacy criteria is **null** in this research. Do not multiply workforce occupational shares by firm counts or equate establishments with firms.

[analysis] Qualification should count owner-led firms with recurring assignments, existing authorized ATS exports/API, manual coordination load and a named compliance/payroll owner. Segment size is an explicit research gap, not permission to invent TAM. Scenario deployments of 25/100/500 clients would be business-planning quantities, not forecasts or measured market shares. Each client still pays its own hosting/external accounts and incurs the second-deployment work above. Shared engineering must be amortized over **actual** retained clients; an unpriced first build cannot be hidden behind a cheap server.

## Falsifiers and evidence needed

[analysis] Reject or narrow the thesis if: (1) reviewed intake is no faster after exceptions; (2) the desk will not adopt the new queue and continues its spreadsheet; (3) API/exports cannot preserve identities, attachments, permissions or history; (4) unapproved/stale/cross-client sends occur; (5) employment/wage decisions are bypassed; (6) the shared schema creates more reconciliation than it removes; (7) support and resource/edition fees exceed monetizable capacity; (8) no narrow eligible segment will fund the per-client onboarding cost; (9) accessibility or legal/privacy review fails; or (10) one-box outages/restores cannot meet the client's deadlines. No amount of repository stars reverses these tests.

[analysis] Proposed pilot gates: source-fidelity and duplicate-send tests pass; every external action has an accountable approver; no privacy/permission exceptions survive review; actual total human minutes fall for the same completed-work definition; migration reconciles counts and rollback; costs and cancellations have receipts. Test cases suggested in Stage 5 are engineering fixtures, not statistical proof of fair selection outcomes.

## Regulatory/source boundary

[vendor] EEOC/DOJ warn about disability discrimination from employment software; NYC regulates certain automated employment-decision tools; FTC guidance describes background-check obligations. [EEOC/DOJ](https://www.eeoc.gov/newsroom/us-eeoc-and-us-department-justice-warn-against-disability-discrimination), [NYC](https://www.nyc.gov/site/dca/about/automated-employment-decision-tools.page), [FTC](https://www.ftc.gov/business-guidance/resources/background-checks-what-employers-need-know). [analysis] These sources improve on the earlier EEOC-page retrieval gap, but do not constitute fifty-state/local law review, a legal opinion, a bias audit or accessibility certification. Some direct DOL/USCIS retrievals were blocked; indexed official snippets are not represented as complete page reads. Keep selection and restricted verification with authorized humans/providers.

## Accounting for value

[analysis] Separate **cash**, **capacity**, **quality** and **risk**; all actual outcomes remain null. The catalogue and source ratings establish a reuse hypothesis, not adoption, savings or fairness. This follows the [Foundry observed-value model](https://raw.githubusercontent.com/sisodias/great-library-of-siso/main/research/industries/source/intelligence/agency/economics/observed-value-model.json). Final verdict: pursue a supervised, measurable intake/status pilot; do not promise an all-OSS staffing business in a box.
'''
put(P+'06-value.md',value)

summary=heading('US recruiting & staffing — super-app blueprint')+f'''**Verdict [analysis]: YES to a narrow supervised coordination pilot; NO to a wholesale ATS/payroll replacement.** The primary segment is a five-person US IT/professional W-2 contract-staffing desk, designed around 50 assignments and 12 clients. A real public co-founder account anchors the operator research; headcount, specialty, Tuesday and volumes remain an explicit design fixture, not an invented interview. [Person and 12 complaints](01-person.md).

**Wedge:** inbound conversation → source-linked JobOrder draft → missing-field review → human approval → incumbent ATS receipt. Preserve existing ATS authority, candidate consent and external payroll/ledger authority. No automated hiring decisions. [Workflow](02-workflow.md).

**Economics:** fixed public-price reference **$18,840/year**; later eligible retirements only **$2,760**, not the full stack. A supported integrated one-client-VPS plan budgets **$5,400/year**, including $528 paid on-premises signing integration, giving **$2,640 extra annual fixed cost before migration**. Minimal intake-only plan: $1,896/year versus at most $1,200 retired. The full-scope **5.58 hours/week** capacity hypothesis is **unmeasured**; actual cash and hours saved are null. [Prices](03-companies.md), [value and falsifiers](06-value.md).

**Spine:** Party · JobOrder · Candidacy · Assignment · WorkRecord · Conversation. Client owns one VPS, databases, accounts and off-box encrypted backups; no SISO-hosted application runtime. 16 GiB/8 vCPU is a planning envelope, not a tested floor. External network, payroll and legal services remain. [Assembly](05-superapp.md), [machine-readable architecture](05-assembly.json).

## Top ten selected repositories

'''+table(['Repository','Verdict','Bounded reuse'],[[link(R[i]['full_name'],R[i]['url']),R[i]['verdict'],R[i]['what_it_gives_us']] for i in D['top10']])+f'''
**Actual counts:** **138 unique repos examined** (140 requested, one alias duplicate and one failed lookup excluded); **{members['ALREADY IN THE BANK']} already held / {members['NEW']} new**; **{counts['ADOPT']} ADOPT / {counts['STEAL']} STEAL / {counts['STUDY']} STUDY / {counts['SKIP']} SKIP**; **10 Tier-1 companies**, **11 Tier-2 offerings**, **5 additional enterprise platforms**; **12 quoted complaints from 10 threads**; **12 workflow stages**, **9 subsegments**, **6 discovery rounds**, **10 material gaps**. Final two bounded in-scope discovery passes added no relevant candidates; failed requests were not counted as dry searches. [Full scored funnel](04-oss-candidates.md).

**Gap list:** US statutory payroll/tax authority; licensed sourcing data; screening/I-9/E-Verify services; ATS API/migration parity; complete staffing mappings; carrier/delivery services; paid signing/enterprise rights; state/local/privacy/accessibility review; measured capacity/security/restore/support; observed operator workload and eligible segment count.

**Next admission decision:** fund only an authorized intake pilot with source fidelity, permission isolation, retry/rollback and net reviewed-effort measurements. Reject if it adds reconciliation, sends stale/unapproved messages, bypasses employment/wage authority or cannot justify total operating/migration cost. No candidate application was executed and no deployment, savings, fairness or production-readiness claim is made.
'''
put(P+'00-SUMMARY.md',summary)
regline={'slug':'recruiting_staffing','name':'US recruiting and staffing agencies','status':'complete','primary_segment':'US IT/professional W-2 contract staffing; five-person design desk','person':'Owner-recruiter; public US co-founder anchor plus explicitly hypothetical five-person/50-assignment workload','wedge':'Conversation to evidence-linked approved JobOrder with incumbent ATS receipt','stack_tax_usd_year':18840,'workflow_stages':12,'tier1_companies':10,'tier2_offerings':11,'repos_examined':138,'repos_adopted':counts['ADOPT'],'gaps':10,'verdict':'YES—supervised coordination pilot; NO—unqualified ATS/payroll replacement','date':DATE,'stage_reached':7,'deployment':'client_vps','repos_already_in_bank':members['ALREADY IN THE BANK'],'repos_new':members['NEW'],'practitioner_complaints':12,'complaint_threads':10,'source_scope':'Public-source research blueprint complete; production qualification, actual outcomes and narrow segment count unmeasured','actual_cash_saved':None,'actual_hours_saved':None,'application_code_written':False,'deployed':False}
put(P+'07-registry-line.json',regline)
put(P+'07-bank-submissions.md',heading('Bank submission handoff')+f"[analysis] {members['NEW']} new canonical repos were absent from the six checked exported bank layers. Each has a shared-registry row; **keep=true only for ADOPT/STUDY/STEAL**. SKIP rows are exclusion receipts, not recommendations for admission. Every proposal uses an existing capability tag; richer vertical tags remain proposals.\n\n"+table(['New repository','Tag','Verdict','Keep','Why'],[[link(r['full_name'],r['url']),r['capability_tag'],r['verdict'],r['verdict']!='SKIP',r['what_it_gives_us']] for r in rows if r['bank_status']=='NEW']))
# Preserve metadata/hashes while removing unnecessary long upstream README quotations from current deliverables.
for r in raw:
    r['editorial_reviewed']=True;r['reviewed_at']=DATE
    if r.get('readme'):
        r['readme'].pop('excerpt',None);r['readme']['retention_note']='Full public text was retrieved and hash recorded; long quoted excerpt removed after review. Use pinned source URL.'
    if r.get('description'):r['description']=' '.join(r['description'].split()[:25])
    put(E+f"repo-{int(r['audit_id'][1:]):03d}.json",r)
for start in range(0,140,5):
    rr=[]
    for r in raw[start:start+5]:
        rr.append({k:r.get(k) for k in ('audit_id','full_name','stargazers_count','last_commit','revision','license','bank_status','readme','license_file','retrieval_error')}|{'editorial_verdict':decisions.get(r['audit_id'],{}).get('verdict'),'reviewed_at':DATE})
    put(E+f'review-{start//5+1:02d}.jsonl',''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in rr))
# All artifacts created above are research data/text; no runtime code, templates or migrations are emitted.
assert counts['ADOPT']==14
assert len(lanes)>=36
put(E+'publication-validation.json',{'as_of':DATE,'input_revision':REV,'examined':138,'bank_counts':dict(members),'verdict_counts':dict(counts),'tier1':len(T1),'tier2':len(T2),'stages':len(W),'complaints':len(complaints),'threads':len({x['url'] for x in complaints.values()}),'gaps':len(D['gaps']),'query_attempts':query_count,'successful_queries':success,'covered_stage_lane_pairs':len(lanes),'stack_tax':18840,'integrated_run_cost':5400,'integrated_extra_cost':2640,'application_code_executed':False,'upstream_code_executed':False,'publication_status':'validated-before-atomic-git-push'})

# Fresh-parent, non-force publication preserves other industries and retries concurrent updates.
work=pathlib.Path(tempfile.mkdtemp(prefix='recruiting-pack-'));env=os.environ.copy();env.update({'GIT_CONFIG_COUNT':'1','GIT_CONFIG_KEY_0':'http.https://github.com/.extraheader','GIT_CONFIG_VALUE_0':'AUTHORIZATION: basic '+base64.b64encode(('x-access-token:'+TOKEN).encode()).decode(),'GIT_TERMINAL_PROMPT':'0'})
def git(*args,check=True):
    p=subprocess.run(['git',*args],cwd=work,env=env,capture_output=True,text=True)
    if check and p.returncode:raise RuntimeError('Git '+args[0]+' failed; exit '+str(p.returncode))
    return p

git('init','-q');git('remote','add','origin','https://github.com/'+REPO+'.git');git('config','user.name','SISO Research');git('config','user.email','research@users.noreply.github.com')
for attempt in range(8):
    git('fetch','--depth=1','origin','main');git('read-tree','origin/main');parent=git('rev-parse','origin/main').stdout.strip();outputs=dict(OUT)
    current=git('show','origin/main:registry/industries.jsonl').stdout;newlines=[];found=0
    for line in current.splitlines():
        x=json.loads(line)
        if x.get('slug')=='recruiting_staffing':
            x.update(regline);x['note']='Seven-stage research pack with 138 reviewed canonical repos; actual outcomes and production qualification remain unmeasured.';newlines.append(json.dumps(x,ensure_ascii=False));found+=1
        else:newlines.append(line)
    assert found==1;outputs['registry/industries.jsonl']='\n'.join(newlines)+'\n'
    current=git('show','origin/main:registry/bank-submissions.jsonl').stdout;existing=[l for l in current.splitlines() if l.strip()];kept=[l for l in existing if json.loads(l).get('industry')!='recruiting_staffing']
    for r in rows:
        if r['bank_status']=='NEW':kept.append(json.dumps({'industry':'recruiting_staffing','date':DATE,'full_name':r['full_name'],'url':r['url'],'capability_tag':r['capability_tag'],'verdict':r['verdict'],'keep':r['verdict']!='SKIP','why':r['what_it_gives_us'],'bank_status':'NEW','bank_revision_checked':r['bank_revision'],'source_revision':r['revision'],'evidence_class':'analysis','status':'proposed-not-admitted','evidence':r['evidence_receipt']},ensure_ascii=False))
    outputs['registry/bank-submissions.jsonl']='\n'.join(kept)+'\n'
    current=git('show','origin/main:registry/corrections.jsonl').stdout;lines=[l for l in current.splitlines() if l.strip()];cid='recruiting-20260913-fame-gap-direction';lines=[l for l in lines if json.loads(l).get('id')!=cid]
    correction={'id':cid,'industry':'recruiting_staffing','date':DATE,'evidence_class':'analysis','status':'needs_reconciliation','target_repository':'sisodias/siso-repo-bank','target_field':'fame_gap','finding':'Bank README and pinned Foundry adoption loader describe opposite fame_gap directions. Confirmed during recruiting review; preserve raw dependencies/downloads and do not apply a directional score penalty until producer formula is reconciled.','related_correction':'aviation-20260913-fame-gap-sign','sources':['https://github.com/sisodias/siso-repo-bank/blob/main/README.md','https://github.com/sisodias/siso-foundry/blob/11f459597ce0c67dbfa89deeeafa3202e47dc6d5/pipelines/github/load_adoption_signal.py'],'data_changed':False};lines.append(json.dumps(correction,ensure_ascii=False));outputs['registry/corrections.jsonl']='\n'.join(lines)+'\n'
    for p,t in outputs.items():
        assert p.startswith(P) or p in ('registry/industries.jsonl','registry/bank-submissions.jsonl','registry/corrections.jsonl')
        dest=work/p;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(t)
    for p,t in outputs.items():
        if p.endswith('.json'):json.loads(t)
        if p.endswith('.jsonl'):
            for line in t.splitlines():
                if line.strip():json.loads(line)
    git('add','--',*outputs.keys());tree=git('write-tree').stdout.strip();commit=git('commit-tree',tree,'-p',parent,'-m','research(recruiting_staffing): publish complete seven-stage 138-repo blueprint and registries').stdout.strip()
    push=git('push','origin',commit+':refs/heads/main',check=False)
    if push.returncode==0:print('PUBLISHED_COMMIT='+commit);print('Research files:',len(outputs),'Examined:',len(rows),'ADOPT:',counts['ADOPT'],'Bank:',dict(members));break
    time.sleep(2)
else:raise RuntimeError('Concurrent updates prevented safe publication; no force push attempted.')
