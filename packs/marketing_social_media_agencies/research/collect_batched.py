"""Bounded PUBLIC research collection only. Does not run candidate code.
GraphQL batches avoid spending one REST request for every metadata field.
Source bytes are read at exact commits; only hashes/short excerpts are published.
"""
import ast,base64,concurrent.futures,datetime,hashlib,json,os,re,time,urllib.request,urllib.error
REPO='sisodias/siso-industry-packs'; BRANCH='research/marketing-agencies-20260913'
ROOT='packs/marketing_social_media_agencies/'; DATE='2026-09-13'
assert os.environ['GITHUB_REF_NAME']==BRANCH
TOKEN=os.environ['GH_TOKEN']; START=datetime.datetime.now(datetime.timezone.utc).isoformat()

def now(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
def digest(b): return hashlib.sha256(b).hexdigest()
def gql(query,variables=None):
    req=urllib.request.Request('https://api.github.com/graphql',data=json.dumps({'query':query,'variables':variables or {}}).encode(),headers={'Authorization':'Bearer '+TOKEN,'Content-Type':'application/json','User-Agent':'SISO-public-research'},method='POST')
    for i in range(4):
        try:
            with urllib.request.urlopen(req,timeout=90) as r: obj=json.load(r)
            if obj.get('errors') and not obj.get('data'): raise RuntimeError(json.dumps(obj['errors'])[:800])
            return obj
        except (urllib.error.URLError,TimeoutError):
            if i==3: raise
            time.sleep(3*(i+1))

def raw(repo,ref,path):
    url='https://raw.githubusercontent.com/'+repo+'/'+ref+'/'+path
    try:
        with urllib.request.urlopen(url,timeout=60) as r: return r.read()
    except urllib.error.HTTPError as e:
        if e.code in (404,451): return None
        raise

def name(row):
    for k in ('full_name','repository_full_name','repo_full_name','github_repo','repo','repository','github_url','repository_url','source_url','url'):
        v=row.get(k)
        if isinstance(v,dict):
            n=name(v)
            if n:return n
        if not isinstance(v,str):continue
        m=re.search(r'github\.com/([\w.-]+/[\w.-]+)',v)
        if m:return m.group(1).removesuffix('.git')
        if re.fullmatch(r'[\w.-]+/[\w.-]+',v):return v
    return None

# Read only literal public search inputs from our previously committed collector.
source=raw(REPO,'8e35abe47830314d333a3a8a16cf2f8e347c2287',ROOT+'research/collect_receipts.py').decode()
module=ast.parse(source); seeds=[]; stages=[]
for node in module.body:
    if isinstance(node,ast.Assign):
        keys=[x.id for x in node.targets if isinstance(x,ast.Name)]
        if 'stages' in keys:stages=ast.literal_eval(node.value)
        if 'seeds' in keys:seeds=ast.literal_eval(node.value.func.value).split()
assert len(seeds)>100 and len(stages)==11
# Add overlooked vertical applications and actual linked maintainer projects, not UI kits.
seeds += ['gitroomhq/postiz-agent','gitroomhq/postiz-docker-compose','getopenpost/openpost','trypostit/trypost','postmill-ai/postmill-app','plankanban/planka','alextselegidis/easyappointments','ExifTool/exiftool','pyhanko/pyHanko','w3c/webvtt','InteractiveAdvertisingBureau/openrtb2.x','InteractiveAdvertisingBureau/vast','invoice-x/zugferd-corpus']

bank_head=gql('{repository(owner:"sisodias",name:"siso-repo-bank"){defaultBranchRef{target{oid}}}}')['data']['repository']['defaultBranchRef']['target']['oid']
bank_files=['bank/bank_capability_top.jsonl','bank/bank_capability.jsonl','capability-shelf/source-registry.jsonl','bank/bank_best.jsonl','bank/bank_adoption_v2.jsonl','bank/bank_liftable_ranked.jsonl','bank/bank_contractcard.jsonl','bank/bank_gold.jsonl']
bank={}; counts={}; shelf=[]; tops=[]; vocab=[]
for p in bank_files:
    url='https://raw.githubusercontent.com/sisodias/siso-repo-bank/'+bank_head+'/'+p
    h=hashlib.sha256(); count=0; keys=[]
    try:
        with urllib.request.urlopen(url,timeout=90) as r:
            for line in r:
                h.update(line)
                if not line.strip():continue
                x=json.loads(line);count+=1
                if not keys:keys=list(x)
                n=name(x)
                if n:bank.setdefault(n.lower(),{})[p]=x
                if p.endswith('source-registry.jsonl'):shelf.append(x)
                if p.endswith('bank_capability_top.jsonl'):tops.append(x)
                if p.endswith('bank_capability.jsonl'):vocab.append(x.get('capability') or x.get('tag') or x.get('name'))
        counts[p]={'rows':count,'sha256':h.hexdigest(),'keys':keys,'url':url}
    except urllib.error.HTTPError as e:
        counts[p]={'rows':count,'error':'HTTP '+str(e.code),'url':url}
print('BANK',json.dumps(counts),flush=True)
assert len(vocab)==51 and all(vocab)

pool={}; log=[]; rounds=[]
def add(n,why,s=None,meta=None):
    k=n.lower();fresh=k not in pool
    row=pool.setdefault(k,{'full_name':n,'via':[],'stages':[]})
    if why not in row['via']:row['via'].append(why)
    if s and s not in row['stages']:row['stages'].append(s)
    if meta:row['search_stars']=meta.get('stargazerCount',0)
    return fresh
terms=('marketing','social media','social-media','inbox','crm','approval','digital asset','invoice','time tracking','newsletter','calendar','analytics')
shelf_matches=[r for r in shelf if any(t in json.dumps(r).lower() for t in terms)]
for x in shelf_matches:
    n=name(x)
    if n:add(n,'bank-product-base-shelf')
for n in seeds:add(n,'reference-candidate')
initial=len(pool)

def round_search(i,qs,purpose):
    before=set(pool)
    for s,l,q in qs:
        observed=now()
        query='query($q:String!){search(type:REPOSITORY,query:$q,first:8){repositoryCount nodes{...on Repository{nameWithOwner stargazerCount}}}}'
        data=gql(query,{'q':q+' sort:stars-desc'})
        result=data.get('data',{}).get('search') or {}
        returned=[]; new=0
        for r in result.get('nodes',[]):
            if not r:continue
            returned.append(r['nameWithOwner']);new+=add(r['nameWithOwner'],f'round-{i}:{l}:{q}',s,r)
        log.append({'round':i,'stage':s,'lane':l,'query':q,'sort':'stars-desc','limit':8,'total_count':result.get('repositoryCount'),'returned':returned,'new_names':new,'observed_at':observed,'errors':data.get('errors',[]),'url':'https://github.com/search?type=repositories&q='+urllib.parse.quote(q+' sort:stars-desc')})
        time.sleep(.35)
    added=sorted(set(pool)-before)
    rounds.append({'round':i,'purpose':purpose,'queries':len(qs),'new_names':len(added),'names':added})
    print('ROUND',i,'NEW',len(added),'POOL',len(pool),flush=True)

import urllib.parse
qs=[]
for s,a,b,c in stages:qs.extend([(s,'A-keyword',a),(s,'B-topic',b),(s,'C-format-protocol',c)])
round_search(1,qs,'Three lanes for all eleven workflow stages')
round_search(2,[('S01','bridge','email conversation CRM webhook'),('S02','engine','e-signature self hosted'),('S03','spec','C2PA IPTC'),('S04','plugin','content calendar wordpress plugin'),('S05','library','video metadata subtitle parser'),('S06','app','open source alternative Planable'),('S07','app','open source alternative Buffer Hootsuite'),('S08','protocol','ActivityPub inbox client'),('S09','connector','singer tap facebook ads'),('S10','format','invoice UBL parser'),('S11','registry','awesome selfhosted time tracking')],'Different artifact classes, not rewordings')
round_search(3,[('S07','maintainer','user:inovector'),('S07','maintainer','user:gitroomhq'),('S01','maintainer','org:chatwoot'),('S09','maintainer','org:singer-io facebook'),('S05','maintainer','org:contentauth'),('S06','registry','awesome digital asset management'),('S04','registry','awesome social media tools'),('S09','registry','awesome web analytics'),('S07','protocol','OpenRTB VAST'),('S03','format','IPTC photo metadata'),('S06','library','PDF digital signature validation')],'Maintainer neighborhoods, registries and neglected artifact formats')
dry=0
for i,qs in enumerate([
[('S06','gap','"social" "approval" "content hash"'),('S07','gap','"Instagram" "publication receipt"'),('S02','gap','"WhatsApp" "scope creep"')],
[('S06','gap','"approval manifest" social'),('S03','gap','"IPTC" "client approval"'),('S09','gap','"social metrics" "provenance ledger"')],
[('S07','gap','"Facebook" "version-bound approval"'),('S06','gap','"PAdES" "social campaign"'),('S10','gap','"content revision" "change order"')],
[('S06','gap','"C2PA" "scope change"'),('S07','gap','"approved payload" "wrong account"'),('S09','gap','"client report" "metric provenance"')]],4):
    round_search(i,qs,'Bounded gap-directed queries; zero results are not proof of global absence')
    dry=dry+1 if rounds[-1]['new_names']==0 else 0
    if dry>=2:break

ordered=[]; seen=set()
for n in seeds:
    if n.lower() not in seen:ordered.append(n);seen.add(n.lower())
for x in sorted(pool.values(),key=lambda x:(-len(x['stages']),-x.get('search_stars',0),x['full_name'])):
    if x['full_name'].lower() not in seen:ordered.append(x['full_name']);seen.add(x['full_name'].lower())

fields='''id nameWithOwner url description stargazerCount isArchived isFork primaryLanguage{name} licenseInfo{spdxId name} repositoryTopics(first:10){nodes{topic{name}}} defaultBranchRef{name target{...on Commit{oid committedDate history(first:20,since:"2026-03-13T00:00:00Z",until:"2026-09-13T23:59:59Z"){totalCount nodes{committedDate author{user{login}}}}}}} object(expression:"HEAD:"){...on Tree{entries{name type}}} issues(first:2,orderBy:{field:UPDATED_AT,direction:DESC}){nodes{url createdAt updatedAt state author{login} comments(first:5){nodes{authorAssociation createdAt author{login}}}}}'''
terms2=['docker','compose','self-host','self hosted','api','webhook','approval','workflow','oauth','postgres','redis','mysql','sqlite','memory','ram','cpu','gpu','license','enterprise','commercial','analytics','scheduling','calendar','smtp','webvtt','iptc','xmp','c2pa','activitypub','ubl','pades']
license_tokens=['MIT License','MIT Expat','GNU AFFERO GENERAL PUBLIC LICENSE','GNU GENERAL PUBLIC LICENSE','Apache License','Business Source License','Sustainable Use License','Elastic License','Server Side Public License','Functional Source License','commercial','enterprise']
receipts=[]; failures=[]; resolved=set(); dependency_frontier=[]

def enrich(pair):
    requested,m=pair
    head=m['defaultBranchRef']['target'];pin=head['oid'];n=m['nameWithOwner'];root=m.get('object') or {};entries=root.get('entries',[])
    rootfiles=[x['name'] for x in entries if x['type']=='blob']
    rpaths=sorted([p for p in rootfiles if p.lower().startswith('readme')],key=lambda p:(p.lower()!='readme.md',p))
    lpaths=sorted([p for p in rootfiles if any(p.lower().startswith(t) for t in ('license','licence','copying','copyright'))],key=lambda p:('license' not in p.lower(),p))
    rb=raw(n,pin,rpaths[0]) if rpaths else None;rt=(rb or b'').decode('utf-8','replace')
    licenses=[]
    for p in lpaths[:4]:
        b=raw(n,pin,p) or b'';text=b.decode('utf-8','replace')
        licenses.append({'path':p,'url':f'https://github.com/{n}/blob/{pin}/{p}','bytes':len(b),'sha256':digest(b),'opening_excerpt':' '.join(text.split()[:20]),'signals':[t for t in license_tokens if t.lower() in text.lower()]})
    manifests=[p for p in rootfiles if p in ('package.json','composer.json','go.mod','Cargo.toml','pyproject.toml','requirements.txt','Gemfile')]
    deps=[]; manifest_receipts=[]
    for p in manifests[:2]:
        b=raw(n,pin,p) or b'';text=b.decode('utf-8','replace')
        deps+=re.findall(r'https?://github\.com/([\w.-]+/[\w.-]+)',text)
        package_names=[]
        if p.endswith('.json'):
            try:
                j=json.loads(text)
                for key in ('dependencies','require','devDependencies'):
                    if isinstance(j.get(key),dict):package_names+=list(j[key])
            except json.JSONDecodeError:pass
        manifest_receipts.append({'path':p,'url':f'https://github.com/{n}/blob/{pin}/{p}','sha256':digest(b),'github_refs':sorted(set(deps)),'package_names':package_names[:100]})
    matches={}
    for key in (requested.lower(),n.lower()):matches.update(bank.get(key,{}))
    issue_sample=[]
    for issue in m['issues']['nodes']:
        responses=[c for c in issue['comments']['nodes'] if c['authorAssociation'] in ('OWNER','MEMBER','COLLABORATOR') and c.get('author')!=issue.get('author')]
        issue_sample.append({'url':issue['url'],'created_at':issue['createdAt'],'updated_at':issue['updatedAt'],'state':issue['state'],'maintainer_response_in_sample':bool(responses),'sample_response_at':responses[0]['createdAt'] if responses else None})
    hist=head['history']
    return {'requested':requested,'full_name':n,'github_id':m['id'],'url':m['url'],'observed_at':now(),'verification_route':'GitHub connector-authored research run -> GitHub GraphQL metadata and commit-pinned raw files -> connector-readable receipts','verification_status':'examined_metadata_readme_license','stars':m['stargazerCount'],'archived':m['isArchived'],'fork':m['isFork'],'default_branch':m['defaultBranchRef']['name'],'language':(m.get('primaryLanguage') or {}).get('name'),'description_excerpt':' '.join((m.get('description') or '').split()[:22]),'topics':[x['topic']['name'] for x in m['repositoryTopics']['nodes']],'head_sha':pin,'last_commit_at':head['committedDate'],'last_commit_url':f'https://github.com/{n}/commit/{pin}','readme_source':f'https://github.com/{n}/blob/{pin}/{rpaths[0]}' if rpaths else None,'readme_sha256':digest(rb) if rb else None,'readme_bytes':len(rb or b''),'readme_opening_excerpt':' '.join(rt.split()[:22]),'readme_signals':[t for t in terms2 if t in rt.lower()],'licenses':licenses,'license_metadata':(m.get('licenseInfo') or {}).get('spdxId'),'license_review_scope':'actual root license files read; edition/subdirectory legal clearance not implied','root_license_paths':lpaths,'deployment_file_candidates':[p for p in rootfiles if any(t in p.lower() for t in ('docker','compose','install'))],'commits_last_six_months_total':hist['totalCount'],'commits_last_six_months_sample_count':len(hist['nodes']),'recent_committers_sample':sorted({c['author']['user']['login'] for c in hist['nodes'] if c.get('author',{}).get('user')}),'issue_response_sample':issue_sample,'manifest_receipts':manifest_receipts,'dependency_github_refs':sorted(set(deps)),'bank_status':'ALREADY IN THE BANK' if matches else 'NEW','bank_membership_basis':sorted(matches),'bank_adoption':matches.get('bank/bank_adoption_v2.jsonl'),'bank_best':matches.get('bank/bank_best.jsonl'),'bank_liftability':matches.get('bank/bank_liftable_ranked.jsonl'),'bank_contractcard':matches.get('bank/bank_contractcard.jsonl'),'discovery':pool.get(requested.lower(),{})}

for offset in range(0,len(ordered),8):
    if len(receipts)>=180:break
    names=ordered[offset:offset+8];parts=[]
    for i,n in enumerate(names):
        owner,r=n.split('/',1);parts.append(f'r{i}:repository(owner:{json.dumps(owner)},name:{json.dumps(r)}){{{fields}}}')
    result=gql('{'+''.join(parts)+' rateLimit{remaining cost}}')
    pairs=[]
    for i,n in enumerate(names):
        m=result.get('data',{}).get('r'+str(i))
        if not m or not m.get('defaultBranchRef'):
            failures.append({'requested':n,'status':'unresolved_or_empty','errors':result.get('errors',[])});continue
        if m['id'] in resolved:continue
        resolved.add(m['id']);pairs.append((n,m))
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
        for pair in pairs:
            pass
        futures=[(p,ex.submit(enrich,p)) for p in pairs]
        for p,f in futures:
            try:receipts.append(f.result())
            except Exception as e:failures.append({'requested':p[0],'status':'source_read_failed','error':type(e).__name__})
    print('EXAMINED',len(receipts),'RATE',result.get('data',{}).get('rateLimit'),flush=True)
receipts=receipts[:180]
for r in receipts:
    for n in r['dependency_github_refs']:
        if n.lower() not in pool:dependency_frontier.append({'from':r['full_name'],'candidate':n})

summary={'as_of':DATE,'started_at':START,'finished_at':now(),'commercial_stage_commit':'163f1c53d59d2a12cc23ef7f0fe6e11501415a96','bank_head':bank_head,'bank_files':counts,'bank_distinct_primary_names':len(bank),'shelf_matching_rows':len(shelf_matches),'initial_pool':initial,'discovered_distinct_names':len(pool),'examined_distinct_github_ids':len(receipts),'actual_new_repos':sum(r['bank_status']=='NEW' for r in receipts),'actual_already_in_bank':sum(r['bank_status']!='NEW' for r in receipts),'rounds':rounds,'two_consecutive_search_rounds_without_new_names':dry>=2,'dependency_frontier_not_yet_examined':dependency_frontier,'failures':failures,'examination_scope':'automated live metadata and actual commit-pinned README/root LICENSE/manifest bytes; capped author/issue evidence. Not runtime/security/legal audits. Shortlist receives additional direct connector review.','saturation_scope':'bounded query classes only; unexamined dependency frontier must be closed or disclosed','bank_membership_scope':'union of eight pinned public export layers, not unpublished identity database'}
files={ROOT+'research/batched-summary.json':json.dumps(summary,indent=2)+'\n',ROOT+'research/batched-search-log.json':json.dumps(log,indent=2)+'\n',ROOT+'research/batched-discovery.jsonl':'\n'.join(json.dumps(x) for x in pool.values())+'\n',ROOT+'research/batched-receipts.jsonl':'\n'.join(json.dumps(x) for x in receipts)+'\n',ROOT+'research/bank-vocabulary.json':json.dumps(vocab,indent=2)+'\n',ROOT+'research/bank-product-base-matches.jsonl':'\n'.join(json.dumps(x) for x in shelf_matches)+'\n',ROOT+'research/bank-capability-top.jsonl':'\n'.join(json.dumps(x) for x in tops)+'\n'}
for i in range(0,len(receipts),15):
    compact=[]
    for r in receipts[i:i+15]:
        keep={k:r[k] for k in ['full_name','stars','archived','language','description_excerpt','head_sha','last_commit_at','readme_signals','license_metadata','licenses','commits_last_six_months_total','recent_committers_sample','issue_response_sample','bank_status','bank_membership_basis','bank_adoption']}
        compact.append(keep)
    files[ROOT+f'research/batched-review-{i//15+1:02d}.jsonl']='\n'.join(json.dumps(x) for x in compact)+'\n'
# Table copy is exact, and labels its frequency assumptions.
b=raw(REPO,BRANCH,ROOT+'02-workflow.md').decode();rows=[]
cols=['id','stage','trigger','inputs','outputs','pain','frequency','handoff','data_object']
for line in b.splitlines():
    if re.match(r'^\| S\d\d \|',line):
        values=[x.strip() for x in line.strip().strip('|').split('|')];assert len(values)==9;rows.append(dict(zip(cols,values)))
assert len(rows)==11
files[ROOT+'02-workflow.json']=json.dumps({'as_of':DATE,'evidence_class':'analysis','frequency_status':'unmeasured','stages':rows},indent=2)+'\n'
# GraphQL branch compare-and-swap preserves unrelated concurrent work.
for attempt in range(3):
    q='query($expr:String!){repository(owner:"sisodias",name:"siso-industry-packs"){ref(qualifiedName:$expr){target{oid}}}}'
    head=gql(q,{'expr':'refs/heads/'+BRANCH})['data']['repository']['ref']['target']['oid']
    mutation='mutation($input:CreateCommitOnBranchInput!){createCommitOnBranch(input:$input){commit{oid url}}}'
    inp={'branch':{'repositoryNameWithOwner':REPO,'branchName':BRANCH},'expectedHeadOid':head,'message':{'headline':'research(marketing): publish batched search, bank joins and upstream source receipts'},'fileChanges':{'additions':[{'path':p,'contents':base64.b64encode(s.encode()).decode()} for p,s in files.items()]}}
    result=gql(mutation,{'input':inp})
    if result.get('data',{}).get('createCommitOnBranch'):
        print('RECEIPT_COMMIT',json.dumps(result['data']['createCommitOnBranch']),flush=True);break
    if attempt==2:raise RuntimeError(json.dumps(result)[:800])
print('FINAL_COUNTS',json.dumps({k:summary[k] for k in ['examined_distinct_github_ids','discovered_distinct_names','actual_new_repos','actual_already_in_bank','two_consecutive_search_rounds_without_new_names']}),flush=True)
