"""Render reviewed public research, never execute candidate applications.
Inputs: a verified evidence ZIP directory, manual TSV decisions, and a checkout.
Writes only restaurant research and its own shared-registry additions.
"""
import argparse, collections, csv, hashlib, json, pathlib
DATE = '2026-09-13'
RUN = 34770301947
BANK = '2d7d35ecbf7e1158d0a3527e1489040687ac214b'
RUN_URL = f'https://github.com/sisodias/siso-industry-packs/actions/runs/{RUN}'
TAGS = set('auth-identity workflow-orchestration forms email job-scheduler-cron data-serialization etl-data-integration data-viz-charts client-sdk-generic validation-schema pdf-documents qr-barcode search web-ui-framework ui-component-kit llm-app-framework'.split())
LIC = {'R014':'LGPL-3.0; bundled/edition terms need separate review','R015':'MIT text plus mandatory visible unmodified footer condition','R020':'AGPL-3.0 with Commons Clause; historical MIT text is not the current whole-project grant','R024':'AGPL-3.0-or-later notice','R027':'CoopCycle custom commercial-eligibility terms','R034':'Apache-2.0 root; bundled components separate','R036':'GPL-2.0-or-later notice','R041':'MIT outside enterprise/; enterprise terms separate','R046':'GPL-3.0-or-later notice','R049':'MIT root text','R053':'LGPL-2.1 root; bundled components separate','R060':'CC-BY-SA-4.0 catalogue','R084':'POSR Source Available License v1','R089':'GPL-3.0 root; differs from README MIT badge','R105':'BSD-3-Clause plus dateutil notices','R110':'Star Micronics SDK terms; read source-specific licence','R122':'FSL-1.1 with future Apache-2.0 change terms','R132':'Meta SDK custom API-use terms','R133':'MIT plus dateutil BSD notices','R141':'Root declares Apache-2.0 OR MIT; ancillary licence files not separately audited','R146':'LGPL-3.0 root'}
TOP = ['R041','R076','R001','R005','R002','R006','R033','R056','R048','R045']
GAPS = ['Client fit and baseline','Commercial channel access','Payment and fiscal devices','Peak-service and failure recovery','Table capacity and confirmation','Recipe costing and stock semantics','Supplier document coverage','Three-marketplace settlement','Food-safety authority','Payroll/accounting and loyalty','Versions, rights and support','Research completion']
EXTRA = {'R002':['https://github.com/ury-erp/ury/blob/71b59edac14ea4c7ce4a108b4ea1bdf714803fb5/INSTALLATION.md'], 'R076':['https://github.com/karanshukla/openresto/blob/38c4a129090badc005d4e03b8be127ac9a92bcbd/docs/http-api.md']}

def read_json(path):
    return json.loads(path.read_text(encoding='utf-8'))

def dump(value):
    return json.dumps(value, ensure_ascii=False, indent=2)+'\n'

def health(row):
    if row.get('archived'): return 0
    n = row.get('commits_in_six_months_from_latest_30_sample')
    if n is None: return None
    if n == 0: return 1
    return 3 if n >= 10 else 2

def render(evidence, decisions, root):
    raw = [json.loads(s) for s in (evidence/'repositories.jsonl').read_text().splitlines() if s.strip()]
    manual = list(csv.DictReader(decisions.open(encoding='utf-8'), delimiter='\t'))
    assert len({x['id'] for x in manual}) == len(manual) == 155
    index = {r['audit_id']:r for r in raw}
    assert set(index) == {d['id'] for d in manual}
    rows = []
    for d in manual:
        r = index[d['id']]; examined = bool(r.get('readme',{}).get('text'))
        assert d['verdict'] in ('ADOPT','STUDY','STEAL','SKIP')
        assert d['capability']=='-' or d['capability'] in TAGS
        assert all(0<=int(d[k])<=5 for k in ('fit','liftability','integration'))
        layers = sorted({p for ls in r.get('bank_rows',{}).values() for p,values in ls.items() if values})
        assert bool(layers) == (r['bank_status']=='ALREADY IN THE BANK')
        licence = r.get('license_file',{}); metadata_spdx=(r.get('license') or {}).get('spdx_id')
        label = LIC.get(d['id'], metadata_spdx if metadata_spdx not in (None,'NOASSERTION') else 'Classification unresolved; see root file') if licence.get('text') else 'Root licence not retrieved; no rights conclusion'
        docs = {k:{a:b for a,b in r.get(k,{}).items() if a!='text'} for k in ('readme','license_file')}
        row = { 'audit_id':d['id'],'full_name':r['full_name'],'requested_full_name':r['requested_full_name'],'url':r['html_url'], 'source_revision':r.get('revision'),'stars':r.get('stargazers_count'),'observed_at':r['observed_at'],'last_commit':r.get('last_commit'),'commit_url':r.get('commit_source'), 'examined':examined,'examination_level':'README-led source triage; selected substantive sections, root licence where available and bounded metadata; no full code/runtime audit' if examined else 'metadata only; excluded from examination count', 'bank_status':r['bank_status'],'bank_revision':BANK,'bank_layers':layers,'bank_evidence_urls':[f'https://github.com/sisodias/siso-repo-bank/blob/{BANK}/{p}' for p in layers], 'capability_tag':None if d['capability']=='-' else d['capability'],'tag_scope':'coarse existing parent, not a new restaurant-specific tag' if d['capability']!='-' else 'no useful taxonomy fit for this rejected result', 'workflow_stages':d['stages'].split(','),'unit_class':d['kind'],'deployment_shape':d['deployment'],'deployment_verified':False,'measured_resource_floor':None,'licence':{'review_label':label,'github_spdx_metadata':metadata_spdx,'root_file_read':bool(licence.get('text')),'source_url':licence.get('source_url'),'directory_and_dependency_audit':'not_completed'}, 'scores':{k:int(d[k]) if examined else None for k in ('fit','liftability','integration')},'verdict':d['verdict'],'verdict_scope':'research assembly choice, not production admission','judgment_evidence_class':'analysis','judgment':d['judgment'],'documentation':docs,'additional_sources':EXTRA.get(d['id'],[]),'health_evidence':{'archived':r.get('archived'),'commits_in_latest_30_within_six_months':r.get('commits_in_six_months_from_latest_30_sample'),'sample_capped':r.get('commit_sample_capped'),'contributors_sample':r.get('contributors_sample'),'issues_sample':r.get('issues_sample'),'maintainer_response_sample':r.get('maintainer_response_sample'),'bus_factor':None,'population_response_time':None},'adoption':{'verified_measurement':None,'bank_rows':r.get('adoption_bank_rows',[]),'note':'Absent or unresolved bank evidence; stars are not adoption. No population metric verified.'},'qualification_status':'NOT_QUALIFIED','admission_status':'NOT_ADMITTED','application_executed':False}
        row['scores'].update(health=health(r) if examined else None, adoption=None)
        rows.append(row)
    examined = [r for r in rows if r['examined']]
    assert len(examined)==151
    counts={'requested':160,'collected':155,'repos_examined':151,'metadata_only':4,'retrieval_failures':5,'root_licence_files_read':sum(r['licence']['root_file_read'] for r in examined),'already_in_bank_examined':sum(r['bank_status']=='ALREADY IN THE BANK' for r in examined),'new_examined':sum(r['bank_status']=='NEW' for r in examined),'verdicts_examined':dict(collections.Counter(r['verdict'] for r in examined)),'tier1_companies':10,'tier2_offerings':10,'practitioner_quotes':8,'workflow_stages':12}
    assert counts['already_in_bank_examined']==34 and counts['new_examined']==117
    assert counts['verdicts_examined']=={'ADOPT':10,'STUDY':87,'SKIP':52,'STEAL':2}
    discovery=read_json(evidence/'discovery.json')
    assert [x['new_repositories'] for x in discovery['rounds']]==[77,87,95]
    assert not discovery['exhaustion_reached']
    prefix='packs/restaurants/'
    outputs={}
    def put(path,value): outputs[path]=value if isinstance(value,str) else dump(value)
    put(prefix+'04-oss-candidates.json',{'schema_version':'1.0.0','industry':'restaurants','as_of':DATE,'status':'research_partial','counts':counts,'source_run':RUN_URL,'bank_scope':'Six identity layers plus capability vocabulary, as recorded in bank-receipt; NEW does not mean absent from the unpublished identity database or every other bank export.','rows':rows})
    md=['# 04 — Restaurant OSS source-triage funnel\n',f'**{DATE} UTC. 151 source-examined repositories; 34 already banked and 117 NEW within the stated bank scope.** Ten conditional ADOPT, 87 STUDY, two pattern-only STEAL and 52 SKIP among examined sources. Four additional metadata-only SKIP entries and five retrieval failures are not counted as examined. **Research remains partial.**\n',f'[Public collection run]({RUN_URL}) · [manual decisions](evidence/review-decisions.tsv) · [machine-readable full table](04-oss-candidates.json) · [search evidence](evidence/discovery.json) · [bank receipt](evidence/bank-receipt.json).\n','## What examined means\n','[analysis] This is README-led source triage: substantive capability, requirement and limitation sections were reviewed together with available root licences and bounded repository activity. It is not a full code audit, installation, integration test or field trial. Very short or poor READMEs can be examined and rejected; missing READMEs cannot. Metadata was retrieved through an authorised GitHub research workflow and its hash-verified artifact. Public source text was treated as evidence, never executed.\n','[analysis] Fit, liftability and integration are reviewer judgments on a 0–5 scale. Health is a deliberately narrow activity indicator: 0 archived, 1 no recent commit in the inspected sample, 2 some recent activity, 3 at least ten recent commits in the latest-30 sample. It is not a measured bus factor or support SLA; 4–5 are not assigned. Adoption is **null**, not zero: the bank lookup provided no verified usable population metric. No weighted overall ranking is manufactured from these incomplete dimensions.\n','[analysis] ADOPT selects an unqualified component for a proposed assembly, not unattended production. STUDY is prior art or a runner-up, not permission to ship. STEAL means independently implement a bounded idea if later authorised, respecting source rights; no code was lifted here. Missing or restrictive licences are recorded, not used as the sole rejection reason. Directory, dependency and edition rights remain unreviewed.\n','## Search breadth and outstanding stop condition\n','[analysis] All twelve W01–W12 stages received keyword, topic and format/protocol queries: 36 recorded queries in three rounds. The rounds added **77, 87 and 95** names. They did **not** reach two consecutive dry rounds. The selection retained 160 candidates, not every discovered repository; the long tail remains unexamined. No exhaustive or globally best claim is made.\n','[analysis] Followed source edges include URY→ERPNext/HRMS, main URY→legacy POS/Mosaic, Timefold quickstarts→solver, TastyIgniter composer→core and python-escpos→printer-profile dependencies. The TastyIgniter core README/composer relation was read, but core and every transitive dependency were not added to the 151 count. The self-hosted catalogue was used as a discovery reference, not evidence that all its links were examined. Further maintainer/dependency expansion and two genuinely dry rounds remain required.\n','## Taxonomy and source rights\n',f'[analysis] Existing 51-capability vocabulary was read at [bank revision]('+'https://github.com/sisodias/siso-repo-bank/blob/'+BANK+'/bank/bank_capability.jsonl). Product bases were prioritised over generic libraries; UI components were not re-researched. Coarse tags below are interoperability parents, not proof of vertical coverage. Proposed missing vertical children are `restaurant-pos`, `kitchen-ticket-routing`, `restaurant-table-capacity`, `recipe-yield-costing`, `food-safety-records` and `marketplace-settlement-reconciliation`. Rejected unrelated results may have no useful tag.\n','[analysis] Root-licence labels retain special terms instead of flattening them to badges: Tandoor Commons Clause, OpenSourcePOS visible-footer condition, Chatwoot enterprise separation, and source-specific Star/Meta/FSL licences. A missing root fetch is unknown rights, not no licence or public domain. Exact current root URLs are in every available row.\n','## Examined candidates\n','Scores below are **F/L/H/A/I**: fit, liftability, health, adoption, integration. `?` means unmeasured. All source capabilities are [vendor]; verdict, deployment fit and rationale are [analysis]. Stars and last commit are a dated snapshot, not current forever.\n','| ID / repository and sources | Stars; last commit | Licence | Bank | F/L/H/A/I | Stage / shape / verdict | What it gives us; reason |','|---|---|---|---|---|---|---|']
    for r in examined:
        links=f"[{r['full_name']}]({r['url']}) · [README]({r['documentation']['readme']['source_url']})"
        if r['licence']['source_url']: links+=f" · [licence]({r['licence']['source_url']})"
        scores='/'.join(str(r['scores'][k]) if r['scores'][k] is not None else '?' for k in ('fit','liftability','health','adoption','integration'))
        date=(r['last_commit'] or 'unknown')[:10]
        md.append(f"| {r['audit_id']} {links} | {r['stars']}; [{date}]({r['commit_url'] or r['url']}) | {r['licence']['review_label']} | {r['bank_status']} | {scores} | {','.join(r['workflow_stages'])}; {r['unit_class']}/{r['deployment_shape']}; **{r['verdict']}** | {r['judgment']} |")
    md+=['\n## Not counted as examined\n']
    for r in rows:
        if not r['examined']:md.append(f"- {r['audit_id']} [{r['full_name']}]({r['url']}): metadata only, {r['bank_status']}; README unavailable. No source-fitness scores.")
    md+=['\n[analysis] Five requested repositories returned failed retrievals. A 404 is not proof that a project is dead, private or nonexistent; no unsupported correction is submitted. See [retrieval failures](evidence/retrieval-failures.json). All component resource floors remain unmeasured; [Stage 5](05-superapp.md) records sourced platform requirements and the unbenchmarked one-client deployment budget.\n']
    put(prefix+'04-oss-candidates.md','\n'.join(md)+'\n')
    by={r['audit_id']:r for r in rows}
    assembly={'schema_version':'1.0.0','industry':'restaurants','as_of':DATE,'evidence_class':'analysis','status':'research_partial_not_deployed','deployment':'client_owned_vps_one_application_box_per_client','siso_hosts_client_data':False,'preserve_existing_marketing_site':True,'spine':['Party','ServiceCase','ProductDefinition','StockMovement','WorkRecord','FinancialRecord'],'primary_wedge':'Assigned enquiry-to-approved booking/order handoff with source lineage and an exception queue','top_10':[{'audit_id':i,'repository':by[i]['full_name'],'revision':by[i]['source_revision'],'verdict':by[i]['verdict'],'source_url':by[i]['documentation']['readme']['source_url']} for i in TOP],'phases':[{'phase':'baseline','modules':[],'gate':'Accepted actual client channels, installed systems, authority, matched workload and simpler incumbent alternative.'},{'phase':'bounded_booking_pilot','modules':['R041','R076'],'retain':['website','incumbent POS','payments','kitchen','accountant','payroll'],'gate':'No duplicates, correct capacity, permission isolation, independent confirmation status, lower matched review-inclusive effort.'},{'phase':'optional_direct_orders','modules':['R001'],'gate':'Only if justified; OpenResto remains booking authority, no duplicate reservation module.'},{'phase':'optional_backoffice','modules':['R005','R006','R056'],'qualification_only':['R002'],'gate':'Compatible supported releases, accepted recipes/units, stock/finance mappings and tested reversal.'},{'phase':'optional_adjacent','modules':['R033','R034','R045','R048'],'gate':'Approved safety forms, released offline companion, consented email, qualified actual printer transport.'}],'workflow_component_map':[{ 'stage':f'W{i:02d}','conditional_candidates':[r['audit_id'] for r in rows if f'W{i:02d}' in r['workflow_stages'] and r['verdict']=='ADOPT'],'authority_and_runnerup_detail':'05-superapp.md; candidate inclusion is not an installation instruction'} for i in range(1,13)],'integration':{'owns':'external-ID mappings, versioned relationships, approved event inbox/outbox, reconciliation and exceptions','duplicate_authorities_forbidden':True,'exactly_once_delivery_claimed':False,'booking_and_notification_states_separate':True,'guest_staff_payroll_permissions_separate':True,'default_external_ai_ocr':False,'deployment_verified':False},'resource_budget':{'expanded_vm_ram_gib':16,'reduced_vm_ram_gib':8,'status':'planning_hypotheses_not_measured_minima','vm_usd_month':96,'daily_backup_fraction':0.30,'vm_and_daily_backup_usd_year':1497.60,'complete_operating_cost':None,'sources':['https://www.digitalocean.com/pricing/droplets','https://www.digitalocean.com/pricing/backups','https://developers.chatwoot.com/self-hosted']},'gaps':[{'id':f'G{i:02d}','name':g,'status':'unresolved'} for i,g in enumerate(GAPS,1)],'test_results':None,'production_admissions':0,'client_acceptance':None}
    put(prefix+'05-assembly.json',assembly)
    keep=[r for r in rows if r['examined'] and r['verdict']!='SKIP' and r['bank_status']=='NEW']
    assert len(keep)==70
    submissions=[{'full_name':r['full_name'],'capability_tag':r['capability_tag'],'verdict':r['verdict'],'why':r['judgment'],'industry':'restaurants','date':DATE,'source_revision':r['source_revision'],'source_url':r['documentation']['readme']['source_url'],'bank_status':'NEW','bank_revision':BANK,'bank_scope':'six published identity layers plus vocabulary; unpublished database not checked','qualification_status':'NOT_QUALIFIED','admission_status':'NOT_ADMITTED','submission_source':'restaurants-ac-blueprint-20260913'} for r in keep]
    assert all(r['capability_tag'] in TAGS for r in submissions)
    regpath=root/'registry/industries.jsonl'; lines=regpath.read_text().splitlines(keepends=True)
    hits=[i for i,s in enumerate(lines) if s.strip() and json.loads(s).get('slug')=='restaurants']; assert len(hits)==1
    old=json.loads(lines[hits[0]])
    change={'status':'research_partial','stage_reached':6,'primary_segment':'Mixed dine-in and takeaway casual dining; unconfirmed AC fit','person':'Hypothetical one-site owner-manager; not an observed AC biography','wedge':assembly['primary_wedge'],'stack_tax_usd_year':None,'reference_priced_subtotal_usd_year':12631,'workflow_stages':12,'tier1_companies':10,'tier2_offerings':10,'practitioner_quotes':8,'repos_examined':151,'repos_adopted':10,'production_admissions':0,'already_in_bank_examined':34,'new_examined':117,'gaps':12,'verdict':'Conditional yes to measured reversible pilot; no immediate POS replacement or cash-saving claim','date':DATE,'search_exhausted':False,'completion_note':'Numeric quotas met at README-triage level; two dry rounds, stronger adoption/maintainer evidence, client baseline, market sizing and remaining stage-specific evidence are not complete.','source':'packs/restaurants/00-SUMMARY.md'}
    new=old|change; assert new.get('priority')==old.get('priority') and new.get('client')==old.get('client')
    lines[hits[0]]=json.dumps(new,ensure_ascii=False)+'\n'
    put('registry/industries.jsonl',''.join(lines))
    bpath=root/'registry/bank-submissions.jsonl'; existing=bpath.read_text(); records=[json.loads(s) for s in existing.splitlines() if s.strip()]
    already={r.get('full_name','').lower() for r in records}
    added=[s for s in submissions if s['full_name'].lower() not in already]
    put('registry/bank-submissions.jsonl',existing+('' if not existing or existing.endswith('\n') else '\n')+''.join(json.dumps(s,ensure_ascii=False)+'\n' for s in added))
    put(prefix+'evidence/bank-submissions.jsonl',''.join(json.dumps(s,ensure_ascii=False)+'\n' for s in submissions))
    put(prefix+'evidence/discovery.json',discovery)
    for name in ('bank-receipt.json','retrieval-failures.json','collector-repair-receipt.json','stage3-checkpoint.json'): put(prefix+'evidence/'+name,read_json(evidence/name))
    receipt={'as_of':DATE,'counts':counts,'new_research_candidates_for_bank':70,'shared_registry_new_rows_added':len(added),'verified_corrections_to_existing_bank_records':0,'corrections_note':'Source-specific warnings and licence caveats are recorded per candidate; no substantiated contradiction to an existing bank record was established. Existing corrections registry is unchanged.','search_round_new_names':[77,87,95],'two_dry_rounds':False,'source_run':RUN_URL,'source_artifact_id':10322051172,'source_artifact_sha256':'53c3f496cefc617097e99a1405a2f9cdab3ab6fbc1e4ef5796624a67f3009299','manual_decisions_sha256':hashlib.sha256(decisions.read_bytes()).hexdigest(),'application_executed':False,'application_code_written':False,'evidence_level':'README-led source triage, not full code/runtime verification','status':'research_partial'}
    put(prefix+'evidence/research-receipt.json',receipt)
    toptext='; '.join(f"[{by[i]['full_name']}]({by[i]['url']}) — {by[i]['verdict']}" for i in TOP)
    summary=f'''# Restaurants / AC — the operating-system blueprint

**2026-09-13 UTC · medium priority · RESEARCH PARTIAL · no application code or deployment.**

**The person and segment [analysis]:** design for a mixed dine-in/takeaway owner-manager. One site, 60 seats and 20 paid staff are explicit reference assumptions, not facts about AC. Actual jurisdiction, installed tools, volumes and invoices remain unknown. Preserve the existing marketing website; it is not a restaurant operating system. [Supplied brief](README.md) · [operator and eight attributed complaints](01-person.md).

**The first useful door [analysis]:** an assigned conversation-to-approved-booking/order handoff with original-message lineage, independent confirmation status and a visible exception queue. Retain the till, payment provider and kitchen route. Pilot Chatwoot/OpenResto only after an incumbent/free configuration fails the same measured test. [Workflow](02-workflow.md) · [assembly](05-superapp.md).

**Actual research counts:** 151 README-led source examinations: **34 ALREADY IN THE BANK / 117 NEW** in the six checked identity layers; 10 conditional ADOPT, 87 STUDY, two pattern-only STEAL, 52 SKIP. Four metadata-only entries and five retrieval failures are excluded. **10 Tier-1 companies, 10 Tier-2 offerings, eight practitioner complaints, 12 workflow stages.** Root licence files were retrieved and read for 124 candidates; missing licences remain unknown. [Full candidate table](04-oss-candidates.md) · [machine-readable evidence and counts](evidence/research-receipt.json).

**Stack tax [vendor / arithmetic]:** $12,631/year is the priced subtotal for one hypothetical purchasing basket, not AC's bill, a verified compatible bundle or avoidable spend. Complete stack tax and realised savings are **null**. A 16GiB client-owned VPS plus daily disk-backup planning reference is **$1,497.60/year**, not complete operating cost or a proven resource minimum. [Prices and arithmetic](03-companies.md) · [value case and exclusions](06-value.md).

**The spine [analysis]:** Party, ServiceCase, ProductDefinition, StockMovement, WorkRecord and FinancialRecord. These join authoritative domain IDs and versions; they are not six universal tables or a second financial database. [JSON assembly](05-assembly.json).

**Ten highest-leverage references [analysis]:** {toptext}. ODK Collect is an additional conditional device companion. These are options across phases, not ten always-on services or ten production approvals. URY remains qualification-first because version compatibility and live service behaviour are unproved.

**Gap list [analysis]:** client baseline; channel permissions; fiscal/payment hardware; peak/offline recovery; table/confirmation races; recipe/yield/stock mappings; supplier document coverage; marketplace payout reconciliation; safety authority; payroll/accounting/loyalty acceptance; version/rights/support; research exhaustion. [Twelve gaps and tests](05-superapp.md).

**Verdict [analysis]: yes to a bounded, reversible, evidence-producing pilot; no to an immediate wholesale POS replacement or a savings sales pitch.** All application hosting belongs on AC's own VPS, never SISO infrastructure. The reviewed source supports a useful assembly hypothesis, not measured client value.

**Not complete:** the three discovery rounds added 77, 87 and 95 names, so the required two dry rounds were not reached. Adoption metrics remain unverified, maintenance evidence is bounded, market eligibility is unmeasured and some stage-specific complaints/client facts remain missing. Seventy NEW non-SKIP research candidates are prepared for bank intake, not admitted for production. No unsupported bank correction was invented. [Search ledger](evidence/discovery.json) · [bank intake](evidence/bank-submissions.jsonl).
'''
    put(prefix+'00-SUMMARY.md',summary)
    for path,text in outputs.items():
        assert path.startswith(prefix) or path in ('registry/industries.jsonl','registry/bank-submissions.jsonl')
        if path.startswith(prefix):
            assert '-----BEGIN PRIVATE KEY-----' not in text and '/Users/' not in text
        dest=root/path; dest.parent.mkdir(parents=True,exist_ok=True); dest.write_text(text,encoding='utf-8')
    return outputs,receipt

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--evidence',type=pathlib.Path,required=True);p.add_argument('--decisions',type=pathlib.Path,required=True);p.add_argument('--root',type=pathlib.Path,required=True);args=p.parse_args()
    paths,receipt=render(args.evidence,args.decisions,args.root)
    (args.root/'publication-paths.json').write_text(dump(list(paths)))
    print(json.dumps({'generated_paths':list(paths),'counts':receipt['counts'],'new_bank_candidates':70,'status':'research_partial'}))
