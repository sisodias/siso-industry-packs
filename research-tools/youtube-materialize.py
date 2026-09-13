"""Materialize PUBLIC research documents, never application code or a deployment.
Inputs: fixed/hash-checked evidence artifacts, public bank snapshot and reviewed TSV.
Writes: only this pack, its existing research tools/workflows and three registry edits.
Preserves current main's unrelated files; never updates main or force-pushes a ref.
"""
from __future__ import annotations
import csv,hashlib,io,json,os,pathlib,re,urllib.request,urllib.error,urllib.parse,zipfile,collections,datetime
ROOT=pathlib.Path.cwd(); PACK='packs/youtube_creators/'; REPO='sisodias/siso-industry-packs'; BRANCH='research/youtube-creators-20260913'
API='https://api.github.com'; TOKEN=os.environ.get('GH_TOKEN',''); EXPECTED=os.environ.get('GITHUB_SHA','')
DATE='2026-09-13'; BANK_SHA='2d7d35ecbf7e1158d0a3527e1489040687ac214b'
assert os.environ.get('GITHUB_REPOSITORY',REPO)==REPO
assert os.environ.get('GITHUB_REF_NAME',BRANCH)==BRANCH
class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self,req,fp,code,msg,headers,newurl): return None
def fetch_bytes(url,method='GET',payload=None,redirect=False):
    headers={'User-Agent':'SISO-public-research-materializer'}
    if url.startswith(API+'/'):
        headers['Accept']='application/vnd.github+json'
        if TOKEN: headers['Authorization']='Bearer '+TOKEN
    if payload is not None: headers['Content-Type']='application/json'
    request=urllib.request.Request(url,data=json.dumps(payload).encode() if payload is not None else None,headers=headers,method=method)
    try:
        with urllib.request.build_opener(NoRedirect).open(request,timeout=60) as r: return r.read()
    except urllib.error.HTTPError as e:
        if redirect and e.code in (301,302,303,307,308):
            target=e.headers['Location']; assert target.startswith('https://')
            # Deliberately omit all credentials on GitHub's signed object-storage redirect.
            with urllib.request.urlopen(urllib.request.Request(target,headers={'User-Agent':'SISO-public-research-materializer'}),timeout=60) as r: return r.read()
        raise RuntimeError('HTTP %s for host/path %s'%(e.code,urllib.parse.urlsplit(url).path)) from None
def api(path,method='GET',payload=None): return json.loads(fetch_bytes(API+path,method,payload))
def artifact(aid,digest):
    data=fetch_bytes(API+'/repos/'+REPO+'/actions/artifacts/'+str(aid)+'/zip',redirect=True)
    assert hashlib.sha256(data).hexdigest()==digest,'artifact digest mismatch'
    result={}
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        for name in z.namelist():
            p=pathlib.PurePosixPath(name)
            assert not p.is_absolute() and '..' not in p.parts
            if name.endswith('/'): continue
            assert p.name not in result,'duplicate artifact basename'
            result[p.name]=z.read(name)
    return result
def decode_json(b): return json.loads(b.decode('utf-8'))
def jsonl(b): return [json.loads(l) for l in b.decode('utf-8').splitlines() if l.strip() and not l.lstrip().startswith('#')]
def dump(obj): return json.dumps(obj,ensure_ascii=False,indent=2)+'\n'
def read(path): return (ROOT/path).read_text(encoding='utf-8')
outputs={}
def put(path,text):
    assert path.startswith(PACK) or path in ('registry/industries.jsonl','registry/bank-submissions.jsonl','registry/corrections.jsonl')
    outputs[path]=text
    p=ROOT/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text,encoding='utf-8')
audit=artifact(10321333734,'c4ee9c63b4db72dd666ec384604e488318631ce18c8915e8268bee5a35f61ece')
bank=artifact(10320495886,'4fb257c13de54d3bf3f256342e9170cae75a1daada674ff86553305c5c230805')
discovery=artifact(10321187612,'67e6ef0b20dd5d035e2bcadd4119c380b378fb41e89e0fd156827c6c4e8e2f21')
receipt=decode_json(audit['receipt.json']); assert receipt['readme_examined']==129
curated=list(csv.DictReader(io.StringIO(read('research-tools/youtube-curation.tsv')),delimiter='\t'))
assert len(curated)==129 and len({x['full_name'].lower() for x in curated})==129
records={}
for name,b in audit.items():
    if '__' in name and name.endswith('.json'):
        r=decode_json(b)
        if r.get('examined') and r.get('readme',{}).get('content'): records[r['full_name'].lower()]=r
assert set(records)=={x['full_name'].lower() for x in curated}
vocab={x['capability'] for x in jsonl(bank['bank__bank_capability.jsonl'])}; assert len(vocab)==51
core=set(decode_json(bank['bank-membership-names.json'])); shelf=set(decode_json(audit['shelf-membership-names.json']))
# Read full adoption layer, not the previously filtered 115-row excerpt. Never load bank_best wholesale.
adoption_url='https://raw.githubusercontent.com/sisodias/siso-repo-bank/'+BANK_SHA+'/bank/bank_adoption_v2.jsonl'
adoption_bytes=fetch_bytes(adoption_url); adoption_rows=jsonl(adoption_bytes); assert len(adoption_rows)==2722
adoptions={r['full_name'].lower():r for r in adoption_rows}
other_members=set(adoptions)
for filename in ('bank__bank_capability_top.jsonl','bank__bank_contractcard.jsonl','bank__bank_liftable_ranked.jsonl'):
    for row in jsonl(bank[filename]):
        n=row.get('full_name') or row.get('repo')
        if isinstance(n,str): other_members.add(n.lower())
license_overrides={
'FFmpeg/FFmpeg':'LGPL-2.1-or-later base; GPL/version3/nonfree build options change obligations',
'chatwoot/chatwoot':'MIT outside enterprise/; enterprise paths separately licensed',
'frappe/crm':'AGPL-3.0 (see exact root licence and selected dependencies)',
'akaunting/akaunting':'BSL-1.1 with restricted additional-use grant; dated conversion terms apply',
'invoiceninja/invoiceninja':'Elastic License 2.0; hosted-service, key and notice restrictions',
'InvoicePlane/InvoicePlane':'Own code MIT; trademark and bundled third-party terms separate',
'remotion-dev/remotion':'Custom Remotion licence; free-use/company/derivative conditions differ',
'fishaudio/fish-speech':'Fish Audio Research License; commercial route requires separate permission',
'exiftool/exiftool':'Scope ambiguity: retrieved root GPL text; README references Perl terms',
'acoustid/chromaprint':'MIT source portions and LGPL-2.1-or-later combination/dependencies',
'googleapis/google-api-go-client':'BSD-3-Clause; bundled dependency notices separate',
'googleapis/google-api-nodejs-client':'Apache-2.0',
'googleapis/google-api-python-client':'Apache-2.0',
'ffmpegwasm/ffmpeg.wasm':'MIT wrapper; bundled FFmpeg/build licences separate',
'lovell/sharp':'Apache-2.0 wrapper; libvips and codec dependencies separate',
'yt-dlp/yt-dlp':'Unlicense source; bundled distributions can include GPL-3.0-or-later components',
'rany2/edge-tts':'LGPL-3.0 portions; srt composer MIT; remote-service terms separate',
'pyannote/pyannote-audio':'MIT code; individual model/service terms separate',
'SWivid/F5-TTS':'MIT code; separately obtained model weights not cleared by this code licence',
'tmoroney/auto-subs':'MIT code; optional MMS alignment weights have separate noncommercial terms',
'AcademySoftwareFoundation/OpenImageIO':'Apache-2.0 project with documented remaining third-party exceptions',
'twentyhq/twenty':'AGPL-3.0 with Application Exception; MIT SDK/UI/apps and marked enterprise boundaries',
'w3c/odrl':'W3C Software and Document License; specification repository',
'w3c/ttml2':'W3C Document License; specification repository',
'w3c/webvtt':'W3C Software and Document License; specification repository',
'youtube/api-samples':'No actual licence file retrieved; do not infer permission from public visibility',
'tokland/youtube-upload':'README claims GPL-3.0, but no actual licence file retrieved',
}
resource_notes={
'cpu_library':'Co-located library; incremental and whole-stack peak memory unmeasured.',
'cpu_worker':'Bounded local worker; one heavy job at a time in the planning deployment; benchmark pending.',
'optional_cpu_worker':'Optional bounded CPU job/service, admitted only after resource and output-quality tests.',
'cpu_cli':'Local CLI invocation; no standalone server implied; actual memory/disk workload unmeasured.',
'cpu_service':'Self-hosted service/application; joint 16-GiB planning envelope is not a verified minimum.',
'optional_cpu_service':'Optional client-hosted service; not included in a demonstrated minimum footprint.',
'separate_service':'Additional application/service graph; full resource floor unmeasured, not assumed free.',
'desktop_only':'Editor-side desktop application, not a VPS-hosted service; outside strict all-authoring-on-VPS claim.',
'browser_compute':'Computation on the operator/reviewer browser device, not inside the VPS.',
'model_specific':'Exact model, voice, licence, quality, memory and hardware must be selected and benchmarked.',
'remote_dependency':'Wrapper may self-host but documented capability depends on a remote service; not strict local parity.',
'unofficial_remote_api':'Depends on an unofficial remote platform surface and its availability/terms.',
'apple_silicon':'Apple Silicon-specific path; not the baseline Linux client VPS.',
'workstation_or_gpu':'Specialist workstation/GPU path outside the narrated-production baseline.',
'format_specification':'Specification/pattern, not an executable application or deployment.',
}
rows=[]; compact_evidence=[]
for c in curated:
    r=records[c['full_name'].lower()]; n=r['full_name']; assert c['capability_tag'] in vocab
    aliases={a.lower() for a in r.get('aliases',[n])}|{n.lower()}
    layers=[]
    if aliases&core: layers.append('bank_best complete name index')
    if aliases&shelf: layers.append('capability-shelf complete name index')
    if aliases&other_members: layers.append('adoption/top/contract/liftability layer')
    membership='ALREADY IN THE BANK' if layers else 'NEW'
    hist=r['metadata']['defaultBranchRef']['target']['history']; nodes=hist.get('nodes',[])
    authors=sorted({x['author']['user']['login'] for x in nodes if x.get('author',{}).get('user')})
    issues=r['metadata'].get('issues',{}).get('nodes',[])
    replied=sum(any(y.get('authorAssociation') in ('OWNER','MEMBER','COLLABORATOR') for y in x.get('comments',{}).get('nodes',[])) for x in issues)
    commits=hist.get('totalCount',0)
    health=0 if r['metadata'].get('isArchived') else (1 if commits==0 else (2 if len(authors)<2 else (4 if len(authors)>=3 and replied else 3)))
    a=next((adoptions[k] for k in sorted(aliases) if k in adoptions),None)
    adoption=0
    if a and a.get('resolved'):
        adoption=2 if (a.get('downloads') or 0)>0 else 1
        dependents=(a.get('dependent_repos') or 0)+(a.get('dependent_pkgs') or 0)
        if dependents: adoption=3
        if dependents and (a.get('reach_percentile') or 0)>=90: adoption=4
        if dependents>=1000 and (a.get('reach_percentile') or 0)>=99: adoption=5
        if (a.get('fame_gap') or 0)>=30: adoption=max(1,adoption-1)
    licence_files=[{k:x.get(k) for k in ('path','url','sha256')} for x in r.get('licenses',[]) if x.get('content')]
    label=license_overrides.get(n,(r['metadata'].get('licenseInfo') or {}).get('spdxId') or 'Unknown; inspect retrieved licence files')
    if label=='NOASSERTION': label='Custom/multiple terms; actual retrieved files require route-specific interpretation'
    if not licence_files and n not in license_overrides: label='No actual licence file retrieved; repository metadata is not permission'
    item={
      'full_name':n,'url':r['url'],'evidence_class':'analysis','upstream_evidence_class':'vendor',
      'stars':r['stars'],'observed_at':r['observed_at'],'last_commit_at':r['last_commit_at'],'last_commit_sha':r['last_commit_sha'],'last_commit_url':r['last_commit_url'],
      'bank_status':membership,'bank_layers':layers,'bank_revision':BANK_SHA,'aliases':r.get('aliases',[]),'capability_tag':c['capability_tag'],'stages':r['stages'],
      'unit_class':c['unit_class'],'deployment_class':c['deployment_class'],'resource_floor_measured':None,'resource_note':resource_notes[c['deployment_class']],
      'license':label,'license_files':licence_files,'license_scope':'Actual root/selected enterprise documents inspected; selected modules, dependency builds, fonts, assets and model weights require independent route review.',
      'scores':{'fit':int(c['fit']),'liftability':int(c['liftability']),'health':health,'adoption':adoption,'integration':int(c['integration'])},
      'health_evidence':{'commits_last_183_days':commits,'sampled_commit_count':len(nodes),'sampled_authors':authors,'sampled_issues':issues,'issues_with_associated_reply_in_sample':replied,'actual_bus_factor':None,'median_issue_response_time':None,'archived':r['metadata'].get('isArchived')},
      'adoption_evidence':a,'adoption_source':adoption_url,'adoption_note':'Historical bank measurement, not live downloads.' if a else 'No matching record in the complete 2,722-row pinned adoption layer; actual adoption unknown, not zero.',
      'verdict':c['verdict'],'what_it_gives_us':c['judgment'],'readme_url':r['readme']['url'],'readme_sha256':r['readme'].get('sha256'),
      'examined':True,'examination_scope':'Pinned public metadata, README and actual available licence documents plus source-reviewed curation. Not a build, full code/security audit, deployment, licence clearance or outcome test.',
    }
    assert all(0<=v<=5 for v in item['scores'].values())
    rows.append(item)
rows.sort(key=lambda x:x['full_name'].lower())
counts=collections.Counter(x['verdict'] for x in rows); bank_counts=collections.Counter(x['bank_status'] for x in rows)
assert counts['ADOPT']==14
put(PACK+'04-oss-candidates.json',dump({'schema_version':'1.0','date':DATE,'status':'research_in_progress','counts':dict(counts),'bank_counts':dict(bank_counts),'repos_examined':len(rows),'repos':rows}))
md='''# 04 — Source-reviewed open-source candidates

Snapshot: **2026-09-13 UTC**. **129 canonical repositories examined**, not 509. Examination means pinned public repository metadata, README and actual available licence files reviewed with the authored curation table. It does **not** mean code/security audit, successful build, dependency licence clearance, benchmark, installation or measured business value. [Structured evidence](04-oss-candidates.json) carries each commit, source URL, licence document/hash, health sample and adoption match. [Reviewed judgments](../../research-tools/youtube-curation.tsv).

**Evidence classes:** repository metadata/docs are `[vendor]` primary upstream claims; fit, scores, deployment judgments and verdicts are `[analysis]`. No repository recommendation is an empirical claim about what Tristan uses. Source records were obtained through the authorized GitHub research connection and its public read-only evidence jobs; no upstream application was executed.

## Funnel and stopping-rule honesty

Inherited discovery found **509 unique leads** across **three broad rounds**, including keywords, topic searches and format/protocol searches. New leads per round were **211, 93 and 69**, after 136 seeds. These are discovery counts, not examination counts. The recovery audit requested 136 names; 130 readable public metadata records resolved to **129 canonical repositories** after alias deduplication. Six unresolved names did not count. **Two consecutive zero-new rounds have NOT been achieved.** This is a useful, numerically broad research snapshot, not an exhaustive sweep or a `complete` pack. [Search log](evidence/search-log.json), [rounds](evidence/rounds.json), [receipt](evidence/research-receipt.json).

Queries followed the commercial map and targeted production applications, speech/editing engines, timeline/caption formats, upload APIs, review tools and rights metadata. The inherited lead graph included alternative/awesome-list queries. Exhaustive dependency/maintainer graph closure remains incomplete. This continuation resumed verified saved work instead of inventing completed searches.

## Bank reconciliation and generic infrastructure

Membership compares canonical names **and aliases** with the complete 23,778-name core index, complete 3,010-name product shelf, and available top/contract/liftability/adoption layers at bank commit `2d7d35ecbf7e1158d0a3527e1489040687ac214b`. `NEW` means absent from that pinned membership evidence, not a guarantee that a concurrent later bank import has not occurred. [Bank](https://github.com/sisodias/siso-repo-bank/tree/2d7d35ecbf7e1158d0a3527e1489040687ac214b). New entries are **proposed imports**, not claims that the bank has accepted them.

For every candidate we checked the **complete 2,722-row adoption layer**, not the earlier filtered excerpt. An absent row means unknown adoption. Its score of zero below denotes no verified dependence evidence in this bounded check, **not zero users or downloads**. Historic `built_at`, downloads period, dependents and fame gap are preserved in JSON. Stars never substitute for dependence. A fame gap of 30 or more reduces the evidence score.

The bank's 51 tags are used without invented synonyms. Proposed taxonomy gap: `media-rights-provenance` would distinguish a rights/evidence manifest from generic data serialization; `creator-production-management` would distinguish production/review applications from generic workflow orchestration. These are proposals, not new silently installed vocabulary. Existing UI components are reused from the component bank, not researched again.

## Scoring and verdicts

Five scores run 0–5: **F** fit to the selected production workflow; **L** liftability (library/SDK highest, bounded service next, whole application lower, pattern/spec lowest); **H** bounded maintenance evidence; **A** verified adoption evidence; **I** integration with the six objects. F/L/I are authored judgments, not measurements. H: archived=0; no commits in 183 days=1; recent with fewer than two sampled identified authors=2; multiple authors=3; at least three authors plus an associated issue reply in the bounded sample=4. H=5 is not awarded without stronger investigation. A: no matching verified evidence=0; resolved registry identity=1; downloads=2; dependents=3; high reach with dependence=4; very high reach and at least 1,000 dependents=5, with fame-gap penalty. **Stable software can be useful despite few commits; this rubric is not a security assessment.** Bus factor and typical response latency remain null because 25 commits and three issues cannot establish them.

**ADOPT** selects a bounded assembly test; **STEAL** would mean reimplement a general pattern with licence/attribution review, not copy without permission; **STUDY** retains a source without adopting it; **SKIP** excludes it from this deployment. There are no STEAL selections in this snapshot. Source-available and document repositories are plainly identified rather than mislabeled OSI software. Licences are recorded, not used as a substitute for fit/quality; commercial deployment still requires the appropriate rights.

## Every examined repository

Every row is `[analysis]` joined to `[vendor]` source evidence. Stars and last commits below were observed on the dates carried in each JSON row, **2026-09-13 UTC**. Licence links lead to actual retrieved files where present; absent files are explicitly marked. All per-repository RAM/GPU floors are **unmeasured** unless the source-referenced notes state otherwise. Deployment classes make browser, desktop, remote-service and model-specific dependencies visible.

| Repository / bank | Stars | Last commit (UTC) | Actual licence scope | F/L/H/A/I | Verdict | Deployment class | What it gives us |
|---|---:|---|---|---|---|---|---|
'''
def cell(s): return str(s).replace('|','\\|').replace('\n',' ')
for r in rows:
    sources=r['license_files']; lic='['+cell(r['license'])+']('+sources[0]['url']+')' if sources else cell(r['license'])
    scores='/'.join(str(r['scores'][k]) for k in ('fit','liftability','health','adoption','integration'))
    md+='| ['+r['full_name']+']('+r['readme_url']+') — '+r['bank_status']+' | '+str(r['stars'])+' | ['+r['last_commit_at'][:10]+']('+r['last_commit_url']+') | '+lic+' | '+scores+' | '+r['verdict']+' | '+r['deployment_class']+' | '+cell(r['what_it_gives_us'])+' |\n'
md+='\n## Actual counts\n\n**[analysis]** '+str(len(rows))+' examined; '+str(counts['ADOPT'])+' ADOPT; '+str(counts['STUDY'])+' STUDY; '+str(counts['SKIP'])+' SKIP; '+str(counts['STEAL'])+' STEAL. '+str(bank_counts['ALREADY IN THE BANK'])+' already held and '+str(bank_counts['NEW'])+' NEW against the pinned membership evidence. Four of the 14 ADOPT components are optional modules, not a demand to deploy 14 services. The top-ten core assembly and runners-up are in [05-superapp.md](05-superapp.md).\n'
put(PACK+'04-oss-candidates.md',md)
# The workflow JSON reproduces the authored table rather than creating a second invented process.
workflow=[]
for line in read(PACK+'02-workflow.md').splitlines():
    if re.match(r'^\| S\d\d \|',line):
        cells=[x.strip() for x in line.strip().strip('|').split('|')]; assert len(cells)==9
        keys=('id','stage','trigger','inputs','outputs','pain','frequency','handoff','data_object')
        workflow.append(dict(zip(keys,cells)))
assert len(workflow)==12
put(PACK+'02-workflow.json',dump({'date':DATE,'evidence_class':'analysis','frequency_status':'unmeasured planning case, not observed operator volumes','source':'02-workflow.md','stages':workflow}))
core10=['cgwire/kitsu','cgwire/zou','FFmpeg/FFmpeg','AcademySoftwareFoundation/OpenTimelineIO','ggml-org/whisper.cpp','tkarabela/pysubs2','lovell/sharp','rclone/rclone','googleapis/google-api-nodejs-client','seaweedfs/seaweedfs']
optional=['chatwoot/chatwoot','miniflux/v2','remsky/Kokoro-FastAPI','Breakthrough/PySceneDetect']
spine=[{'name':a,'purpose':b} for a,b in [('WorkOrder','Human-confirmed accepted demand and source conversation'),('Production','Editorial unit with canonical task-system mapping'),('AssetVersion','Immutable media/script/caption version, lineage and rational timebase'),('RightsGrant','Source permission/consent evidence and conditions, not legal adjudication'),('Release','Approval of exact versions plus authorised publication receipt'),('Deal','Contracted deliverables and references to existing financial authority')]]
gaptext=['Observed operator fit and authorised private-asset reuse','Local script/voice quality, model rights and speaker consent','Licensed stock/music and copyright-claim adjudication','Native NLE project/effect/font round-trip fidelity','Platform OAuth/audit eligibility and TikTok private-utility restriction','Native experiments and owner-only analytics','Payment settlement and statutory accounting/payroll authority','Single-box resource, security, upgrade and restore verification','Selected-module/build/enterprise/model licence boundaries','Actual invoices, eligible population and two dry discovery rounds']
gaps=[{'id':'G%02d'%(i+1),'finding':t,'status':'unverified_or_external_boundary'} for i,t in enumerate(gaptext)]
assembly={'schema_version':'1.0','date':DATE,'status':'blueprint_not_deployed','evidence_class':'analysis','primary_segment':'Original faceless educational/documentary producer-owner','wedge':'Version-bound approved-script to editor handoff and release approval','spine':spine,'core_top_10':core10,'optional_components':optional,'components':[{'repository':r['full_name'],'verdict':'ADOPT','optional':r['full_name'] in optional,'stages':r['stages'],'source_commit':r['last_commit_sha'],'source_url':r['readme_url'],'bank_status':r['bank_status'],'deployment_class':r['deployment_class'],'acceptance':'Route rights, integration and workload tests required; not installed.'} for r in rows if r['verdict']=='ADOPT'],'deployment':{'owner':'client','target':'one client-owned VPS; no SISO servers','os':'Linux planning assumption','ram_gib_test_allocation':16,'verified_ram_floor_gib':None,'heavy_jobs_parallel':1,'gpu_required_for_selected_baseline':False,'gpu_claim_scope':'CPU-capable route proposed, not benchmarked','external_boundaries':['platform endpoints','payment/financial authority','licensed media','editor workstation','approved existing script export'],'application_code_written':False,'deployed':False},'gaps':gaps,'go_no_go':'YES bounded handoff pilot; no complete autonomous-stack or verified-savings claim'}
put(PACK+'05-assembly.json',dump(assembly))
# Preserve current main, rather than overwriting 100+ parallel commits with an old registry copy.
branch_ref='/repos/'+REPO+'/git/ref/heads/'+BRANCH
head=api(branch_ref)['object']['sha']; assert not EXPECTED or head==EXPECTED,'branch changed; stop without mutation'
main=api('/repos/'+REPO+'/git/ref/heads/main')['object']['sha']
comparison=api('/repos/'+REPO+'/compare/'+main+'...'+head)
branchfiles=comparison.get('files',[]); assert len(branchfiles)<300,'truncated comparison not safe'
mergebase=comparison['merge_base_commit']['sha']
def pack_identity(ref):
    entries=api('/repos/'+REPO+'/contents/'+PACK.rstrip('/')+'?ref='+ref)
    assert isinstance(entries,list),'pack directory read failed'
    return sorted((x['name'],x['type'],x['sha']) for x in entries)
main_pack_changed = pack_identity(mergebase)!=pack_identity(main)
put(PACK+'evidence/concurrent-main.json',dump({'main_revision_read':main,'main_pack_changed':main_pack_changed,'main_file_identities':pack_identity(main),'action':'Preserve main unchanged. Publish this source-reviewed continuation only on its existing branch; reconcile competing hypotheses before merge.','main_merged':False}))
allowed=lambda p:p.startswith((PACK,'research-tools/youtube-','.github/workflows/youtube-')) or p in ('registry/industries.jsonl','registry/bank-submissions.jsonl','registry/corrections.jsonl')
assert all(allowed(x['filename']) for x in branchfiles),'unrelated branch changes must be preserved explicitly'
def main_text(path):
    return fetch_bytes('https://raw.githubusercontent.com/'+REPO+'/'+main+'/'+path).decode('utf-8')
# Construct only our industry row; all other registry lines remain byte-for-byte from current main.
registry_source=main_text('registry/industries.jsonl'); lines=registry_source.splitlines(keepends=True); found=0
for i,line in enumerate(lines):
    if not line.strip() or line.lstrip().startswith('#'): continue
    obj=json.loads(line)
    if obj.get('slug')=='youtube_creators':
        found+=1; obj.update({'status':'partial','stage_reached':7,'primary_segment':assembly['primary_segment'],'person':'Tristan Grech / SUMERA; actual operating diary unverified','wedge':assembly['wedge'],'stack_tax_usd_year':None,'modeled_subscription_subtotal_usd_year':2794,'modeled_coordination_subtotal_usd_year':1800,'workflow_stages':12,'tier1_companies':10,'tier2_offerings':10,'practitioner_complaints':10,'complaint_threads':7,'repos_examined':129,'repos_adopted':14,'repos_new_at_bank_snapshot':bank_counts['NEW'],'gaps':10,'verdict':assembly['go_no_go'],'date':DATE,'deployment':'client_vps','research_complete':False,'search_saturation_met':False,'operator_baseline_verified':False,'note':'All seven narrative files populated; numerical quotas met. Partial because observed operator evidence, some quotes/entitlements, exhaustive search stopping rule and deployment/rights/value tests remain open. Counts describe research, not installed components.'})
        lines[i]=json.dumps(obj,ensure_ascii=False)+'\n'
assert found==1
industry_line=next(json.loads(l) for l in lines if l.strip() and not l.lstrip().startswith('#') and json.loads(l).get('slug')=='youtube_creators')
put('registry/industries.jsonl',''.join(lines))
keep=[r for r in rows if r['bank_status']=='NEW' and r['verdict'] in ('ADOPT','STUDY') and r['scores']['fit']>=3]
sub_source=main_text('registry/bank-submissions.jsonl'); existing_sub=[]
for l in sub_source.splitlines():
    if l.strip() and not l.lstrip().startswith('#'): existing_sub.append(json.loads(l))
existing_names={str(x.get('full_name','')).lower() for x in existing_sub}; submissions=[]
for r in keep:
    if r['full_name'].lower() in existing_names: continue
    submissions.append({'full_name':r['full_name'],'capability_tag':r['capability_tag'],'verdict':r['verdict'],'why':r['what_it_gives_us'],'source_industry':'youtube_creators','status':'proposed','bank_status':'NEW','bank_revision':BANK_SHA,'source_revision':r['last_commit_sha'],'url':r['url'],'license':r['license'],'evidence_url':r['readme_url'],'date':DATE})
put('registry/bank-submissions.jsonl',sub_source.rstrip()+'\n'+''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in submissions))
correction_notes={
'minio/minio':'Current upstream is archived and explicitly says no longer maintained; do not carry a historical high-reuse selection into a new deployment without review.',
'rhasspy/piper':'Archived source redirects active development to OHF-Voice/piper1-gpl. Preserve the alias and distinguish old MIT code from the successor GPL route.',
'coqui-ai/TTS':'Source is stale relative to the examined idiap/coqui-ai-TTS continuation; preserve provenance rather than silently treating both as the current engine.',
'GeneralMills/pytrends':'Archived unofficial Trends client with backend-change warnings; historical bank rank is not current reliability.',
'OpenCut-app/OpenCut':'Main README announces a ground-up rewrite; classify as current research, not an accepted production editor based on stars.',
'jianfch/stable-ts':'Repository is archived and announces paused development; record maintenance status rather than infer health from its historic rating.',
}
cor_source=main_text('registry/corrections.jsonl'); old=[]
for l in cor_source.splitlines():
    if l.strip() and not l.lstrip().startswith('#'): old.append(json.loads(l))
corrections=[]
for r in rows:
    if r['full_name'] in correction_notes and r['bank_status']=='ALREADY IN THE BANK':
        if any(x.get('full_name')==r['full_name'] and x.get('source_industry')=='youtube_creators' for x in old): continue
        corrections.append({'full_name':r['full_name'],'source_industry':'youtube_creators','status':'review_required','type':'current_upstream_qualification','finding':correction_notes[r['full_name']],'prior_reference':'siso-repo-bank@'+BANK_SHA,'source_revision':r['last_commit_sha'],'evidence_url':r['readme_url'],'date':DATE,'note':'Qualification/correction proposal; not an allegation that every existing bank row claimed current production fitness.'})
put('registry/corrections.jsonl',cor_source.rstrip()+'\n'+''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in corrections))
put(PACK+'bank-submissions.jsonl',''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in submissions))
put(PACK+'corrections.jsonl',''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in corrections))
# Persist discovery facts and compact source receipts; private sources and raw protocol text are never inputs.
for name in ('search-log.json','rounds.json'):
    put(PACK+'evidence/'+name,audit[name].decode() if name in audit else discovery[name].decode())
put(PACK+'evidence/bank-capability-top.jsonl',bank['bank__bank_capability_top.jsonl'].decode())
put(PACK+'evidence/bank-adoption-matches.json',dump([r['adoption_evidence'] for r in rows if r['adoption_evidence']]))
put(PACK+'evidence/research-receipt.json',dump({'date':DATE,'repository_audit':receipt,'audit_artifact_id':10321333734,'audit_sha256':'c4ee9c63b4db72dd666ec384604e488318631ce18c8915e8268bee5a35f61ece','bank_revision':BANK_SHA,'bank_core_names':len(core),'bank_shelf_names':len(shelf),'adoption_rows_checked':len(adoption_rows),'adoption_sha256':hashlib.sha256(adoption_bytes).hexdigest(),'bank_counts':dict(bank_counts),'verdict_counts':dict(counts),'new_submission_lines':len(submissions),'correction_lines':len(corrections),'search_saturation_met':False,'observed_operator_profile':False,'current_main_preserved':main,'application_code_or_deployment':False}))
toptext='; '.join('`'+n+'` (**ADOPT**)' for n in core10)
summary='''# YouTube creators — research decision

**Snapshot: 2026-09-13 UTC · Status: PARTIAL research, not deployed.**

**Person / segment [analysis]:** Tristan Grech / SUMERA is the named lead. Design for an original faceless educational/documentary producer-owner, extending the supplied shipped script-generation and monetisation shell rather than restarting it. The actual operator diary, invoices, team and intake remain unverified. [Person and ten practitioner accounts](01-person.md).

**Wedge [analysis]:** one version-bound handoff from an approved script and rights-supported assets to an editor, then approval of exact release bytes. Preserve the existing script, editor and accounting authorities. [Twelve-stage workflow](02-workflow.md).

**Stack tax [analysis]:** priced model subtotal **$2,794/year**, not a real client bill or complete total. Potential coordination replacement is **$1,800/year**, conditional on actual cancellations and parity. Illustrative 16-GiB hosting plus weekly backups is **$1,382.40/year**, leaving **$417.60 before care/migration**. One assumed support hour/month at $50 makes that **−$182.40/year** before other costs. No verified savings claimed. [Commercial arithmetic](03-companies.md), [falsifiable value case](06-value.md).

**Spine [analysis]:** WorkOrder, Production, AssetVersion, RightsGrant, Release and Deal; stable cross-system links and immutable evidence, not a second task or financial ledger.

**Top ten repositories [analysis]:** TOPTEXT. Four additional optional ADOPT components are Chatwoot, Miniflux, Kokoro-FastAPI and PySceneDetect; 14 selected repositories are not 14 mandatory services. [Every candidate and pinned evidence](04-oss-candidates.md), [assembly and runners-up](05-superapp.md).

**Actual counts:** 129 examined canonical repositories; 10 Tier-1 companies; 10 Tier-2 offerings; 10 complaints from 10 users across 7 threads; 12 workflow stages; 14 ADOPT; STUDYCOUNT STUDY; SKIPCOUNT SKIP; 0 STEAL; NEWCOUNT NEW against the pinned bank and OLDCOUNT already held; 10 explicit gaps. SUBCOUNT new bank-submission proposals and CORCOUNT correction proposals are recorded. Discovery's 509 leads are not 509 examinations.

**Gaps [analysis]:** actual operator/private-asset authorisation; local script/voice quality and consent; licensed media/claim handling; NLE fidelity; platform API eligibility; native experiments/private analytics; financial authority; single-box operations; route-specific licence/edition terms; and evidence/economics closure. Everything runs on the client's own VPS where it is a hosted assembly component, never on SISO servers; platform endpoints and editor workstations remain explicit external boundaries.

**Verdict [analysis]: YES to a bounded editor-handoff pilot; NO to a proven autonomous creator super-app or subscription-savings offer.** The numerical quotas are met, but the required two consecutive dry discovery rounds are not, several prices/entitlements are unresolved, and an observed operator baseline and deployment/rights/quality tests are still missing. Therefore the registry remains `partial`, not falsely `complete`. No application code was written, no client account was operated, and no application was deployed. [Evidence receipt](evidence/research-receipt.json).
'''
summary=summary.replace('TOPTEXT',toptext).replace('STUDYCOUNT',str(counts['STUDY'])).replace('SKIPCOUNT',str(counts['SKIP'])).replace('NEWCOUNT',str(bank_counts['NEW'])).replace('OLDCOUNT',str(bank_counts['ALREADY IN THE BANK'])).replace('SUBCOUNT',str(len(submissions))).replace('CORCOUNT',str(len(corrections)))
summary += '\n## Concurrent-main reconciliation\n\n[analysis] Parallel research appeared on main during this continuation in 00-SUMMARY.md, 01-person.md and 05-superapp.md. It remains unchanged. Its local-first/BYO-key hypothesis and self-reported 131-repository sweep are separate from this branch’s versioned-handoff hypothesis and 129 source-reviewed repositories; the counts must not be added without deduplication. The client-VPS requirement remains this assignment’s deployment boundary. Bring-your-own-key changes billing/custody but does not itself make upstream calls free. Resolve the competing baselines, prices, component choices and private-source publication boundaries before merging. [Pinned main research](https://github.com/'+REPO+'/tree/'+main+'/packs/youtube_creators).\n'
put(PACK+'00-SUMMARY.md',summary)
put(PACK+'07-registry-line.json',dump(industry_line))
# Validate all deliverables before any branch update.
required=['00-SUMMARY.md','01-person.md','02-workflow.md','02-workflow.json','03-companies.md','04-oss-candidates.md','04-oss-candidates.json','05-superapp.md','05-assembly.json','06-value.md']
assert all((ROOT/PACK/f).exists() and (ROOT/PACK/f).stat().st_size>200 for f in required)
assert len(re.findall(r'^### C\d\d',read(PACK+'01-person.md'),re.M))==10
for path in outputs:
    if path.endswith('.json'): json.loads(read(path))
    if path.endswith('.jsonl'):
        for l in read(path).splitlines():
            if l.strip() and not l.lstrip().startswith('#'): json.loads(l)
for i,x in enumerate(rows): assert x['examined'] and x['readme_url'].startswith('https://github.com/') and len(x['last_commit_sha'])==40
assert round(96*1.2*12,2)==1382.4 and 720+360+720+174+144+220+456==2794
validation={'status':'PASS research-structure checks only','date':DATE,'required_files':required,'repos':129,'adopt':14,'workflow_stages':12,'complaints':10,'tier1_profiles':10,'tier2_profiles':10,'new_bank_proposals':len(submissions),'corrections':len(corrections),'saturation':'NOT MET','operator_baseline':'UNMEASURED','runtime':'NOT TESTED','bank_status_counts':dict(bank_counts),'verdict_counts':dict(counts),'application_deployment':False}
put(PACK+'evidence/validation.json',dump(validation))
# Publish only this branch. Concurrent main work is preserved for explicit PR reconciliation.
main_commit=api('/repos/'+REPO+'/git/commits/'+head)
elements={}
for f in branchfiles:
    p=f['filename']; assert allowed(p)
    if p in ('registry/industries.jsonl','registry/bank-submissions.jsonl','registry/corrections.jsonl'): continue
    if f['status']=='removed': elements[p]={'path':p,'mode':'100644','type':'blob','sha':None}
    else: elements[p]={'path':p,'mode':'100644','type':'blob','content':read(p)}
for p,text in outputs.items(): elements[p]={'path':p,'mode':'100644','type':'blob','content':text}
assert len(elements)<60 and all(allowed(p) for p in elements)
assert api(branch_ref)['object']['sha']==head,'concurrent branch update; no commit/ref mutation'
tree=api('/repos/'+REPO+'/git/trees','POST',{'base_tree':main_commit['tree']['sha'],'tree':list(elements.values())})
commit=api('/repos/'+REPO+'/git/commits','POST',{'message':'research(youtube): publish 129-repository blueprint, preserve current main, keep honest partial status','tree':tree['sha'],'parents':[head]})
assert api(branch_ref)['object']['sha']==head,'concurrent branch update; ref not moved'
api('/repos/'+REPO+'/git/refs/heads/'+BRANCH,'PATCH',{'sha':commit['sha'],'force':False})
publication={'commit':commit['sha'],'branch':BRANCH,'base_main':main,'changed_paths':sorted(elements),'validation':validation,'main_updated':False,'main_merged':False,'concurrent_main_review_required':main_pack_changed,'force_push':False}
(ROOT/'youtube-publication-receipt.json').write_text(dump(publication))
print(json.dumps(publication,ensure_ascii=False,indent=2))
# Export the research pack and its per-pack registry proposals; do not archive unrelated client rows.
with zipfile.ZipFile(ROOT/'youtube-creators-research-pack.zip','w',zipfile.ZIP_DEFLATED) as z:
    for p in sorted((ROOT/PACK).rglob('*')):
        if p.is_file(): z.write(p,str(p.relative_to(ROOT)))
    z.write(ROOT/'youtube-publication-receipt.json','publication-receipt.json')
