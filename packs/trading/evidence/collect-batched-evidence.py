"""Research-only evidence collection. No upstream package is installed or executed.
Uses bounded GraphQL batches and revision-pinned public raw files. No trading/account APIs.
"""
import os,json,urllib.request,urllib.error,urllib.parse,base64,hashlib,time,re,datetime,concurrent.futures,ast
REPO='sisodias/siso-industry-packs'; BRANCH='research/trading-20260913'; PREFIX='packs/trading/evidence/'
assert os.environ['GITHUB_REPOSITORY']==REPO and os.environ['GITHUB_REF_NAME']==BRANCH
TOKEN=os.environ['GH_TOKEN']; HEADERS={'Authorization':'Bearer '+TOKEN,'Accept':'application/vnd.github+json','User-Agent':'siso-public-research'}
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
def raw(url):
    try:
        with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'siso-public-research'}),timeout=35) as r:return r.read()
    except Exception:return b''
def gql(query,variables=None):
    for retry in range(3):
        try:
            req=urllib.request.Request('https://api.github.com/graphql',headers=HEADERS,data=json.dumps({'query':query,'variables':variables or {}}).encode())
            with urllib.request.urlopen(req,timeout=75) as r:result=json.load(r)
            if result.get('errors'):print(json.dumps({'graphql_errors':result['errors']})[:1500],flush=True)
            return result.get('data') or {}
        except Exception as e:
            print(type(e).__name__,flush=True);time.sleep(2)
    return {}
def publish(files,title):
    ref=gql('query{repository(owner:"sisodias",name:"siso-industry-packs"){ref(qualifiedName:"refs/heads/'+BRANCH+'"){target{oid}}}}')
    sha=ref['repository']['ref']['target']['oid']
    result=gql('mutation($input:CreateCommitOnBranchInput!){createCommitOnBranch(input:$input){commit{oid url}}}',{'input':{'branch':{'repositoryNameWithOwner':REPO,'branchName':BRANCH},'expectedHeadOid':sha,'message':{'headline':title},'fileChanges':{'additions':[{'path':p,'contents':base64.b64encode(c.encode()).decode()} for p,c in files.items()]}}})
    if not result.get('createCommitOnBranch'):raise RuntimeError('Research publication failed; no result assumed')
    print(json.dumps(result),flush=True)
# Preserve original query plan; parse literal declarations, never execute the old collector.
source=raw('https://raw.githubusercontent.com/'+REPO+'/536d9c6deeb4821d7f4c185869f7864cc5e48922/'+PREFIX+'collect-public-evidence.py').decode()
module=ast.parse(source);seeds=[];queries=[]
for n in module.body:
    if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='seeds' for t in n.targets):seeds=ast.literal_eval(n.value.func.value).split()
    if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='queries' for t in n.targets):queries=ast.literal_eval(n.value)
seeds+=['csingley/ibflex','camel-ai/oasis','Polymarket/ts-sdk','Polymarket/py-sdk']
# Exact bank joins, not a failed-search inference. No full bank is printed into chat.
banks={};bank_receipts={}
for p,key in [('bank/bank_best.jsonl','full_name'),('capability-shelf/source-registry.jsonl','repo'),('bank/bank_adoption_v2.jsonl','full_name'),('bank/bank_liftable_ranked.jsonl','full_name')]:
    url='https://raw.githubusercontent.com/sisodias/siso-repo-bank/main/'+p;data=raw(url)
    assert data, 'Bank source unavailable; stop rather than mislabel NEW'
    rows=[json.loads(x) for x in data.decode().splitlines() if x.strip()]
    banks[p]={r[key].lower():r for r in rows if r.get(key)};bank_receipts[p]={'url':url,'sha256':hashlib.sha256(data).hexdigest(),'rows':len(rows)}
seen={n.lower():{'name':n,'discovery':[{'round':0,'lane':'prior-lead'}]} for n in seeds};log=[]
for start in range(0,len(queries),5):
    part=queries[start:start+5];q='query{'+''.join('s'+str(j)+':search(type:REPOSITORY,query:'+json.dumps(text+' sort:stars')+',first:8){repositoryCount nodes{...on Repository{nameWithOwner}}}' for j,(_,_,_,text) in enumerate(part))+'}'
    response=gql(q)
    for j,(rnd,stage,lane,text) in enumerate(part):
        item=response.get('s'+str(j)) or {};names=[x['nameWithOwner'] for x in item.get('nodes',[]) if x];new=[]
        for name in names:
            if name.lower() not in seen:seen[name.lower()]={'name':name,'discovery':[]};new.append(name)
            seen[name.lower()]['discovery'].append({'round':rnd,'stage':stage,'lane':lane,'query':text})
        log.append({'round':rnd,'stage':stage,'lane':lane,'query':text,'source_url':'https://github.com/search?type=repositories&q='+urllib.parse.quote(text)+'&s=stars&o=desc','total_count':item.get('repositoryCount'),'returned':names,'new':new,'query_success':bool(item)})
    print(json.dumps({'search_batch':start,'candidates':len(seen)}),flush=True)
    time.sleep(1)
publish({PREFIX+'batched-search-rounds-1-3.json':json.dumps(log,indent=2),PREFIX+'batched-bank-receipts.json':json.dumps(bank_receipts,indent=2)},'research(trading): checkpoint three discovery rounds and exact bank identities')
records=[];unavailable=[];items=list(seen.values())
fields='''databaseId nameWithOwner url description stargazerCount forkCount isArchived isFork primaryLanguage{name} licenseInfo{spdxId name} defaultBranchRef{name target{...on Commit{oid committedDate history(first:50,since:"2026-03-13T00:00:00Z"){totalCount nodes{author{name user{login}}}}}}} object(expression:"HEAD:"){...on Tree{entries{name type}}} issues(first:2,orderBy:{field:UPDATED_AT,direction:DESC}){nodes{url createdAt state comments(first:10){nodes{createdAt authorAssociation}}}}'''
def examine(pair):
    seed,repo=pair
    n=repo['nameWithOwner'];head=(repo.get('defaultBranchRef') or {}).get('target') or {};sha=head.get('oid');root=(repo.get('object') or {}).get('entries') or []
    names=[x['name'] for x in root];docs={};licenses=[];manifests={}
    readme=next((p for p in names if p.lower() in ('readme.md','readme.rst','readme','readme.markdown')),None)
    for p in names:
        if re.match(r'^(license|licence|copying)(\.|$|-)',p,re.I):licenses.append(p)
    paths=([readme] if readme else [])+licenses[:5]+[p for p in names if p in ('pyproject.toml','package.json','Cargo.toml','requirements.txt','setup.py')][:2]
    for p in paths:
        u='https://raw.githubusercontent.com/'+n+'/'+str(sha)+'/'+urllib.parse.quote(p)
        content=raw(u).decode('utf-8','replace');docs[p]={'url':'https://github.com/'+n+'/blob/'+str(sha)+'/'+p,'sha256':hashlib.sha256(content.encode()).hexdigest(),'bytes':len(content.encode()),'text':content}
    rt=docs.get(readme,{}).get('text','');lt='\n'.join(docs.get(p,{}).get('text','') for p in licenses)
    memberships={p:table.get(n.lower()) or table.get(seed['name'].lower()) for p,table in banks.items()};memberships={p:r for p,r in memberships.items() if r is not None}
    recent=head.get('history') or {};authors=sorted(set((x.get('author') or {}).get('user',{}).get('login') if (x.get('author') or {}).get('user') else (x.get('author') or {}).get('name','unknown') for x in recent.get('nodes',[])))
    r={'full_name':n,'requested_name':seed['name'],'id':repo['databaseId'],'url':repo['url'],'stars':repo['stargazerCount'],'observed_at':NOW,'latest_commit':sha,'last_commit_date':head.get('committedDate'),'archived':repo['isArchived'],'fork':repo['isFork'],'description':repo.get('description'),'language':(repo.get('primaryLanguage') or {}).get('name'),'license':(repo.get('licenseInfo') or {}).get('spdxId'),'actual_license_paths':[p for p in licenses if docs.get(p,{}).get('bytes')],'license_headings':re.findall(r'(?im)^.{0,10}(?:MIT License|Apache License|GNU .{0,60}|BSD.{0,80}|Copyright.{0,100}|This project.{0,100}|Business Source.{0,100}).*$',lt)[:8],'license_files_read':bool(lt),'readme_path':readme,'readme_read':bool(rt),'readme_headings':re.findall(r'(?m)^#{1,4} .{1,100}$',rt)[:30],'recent_commit_count':recent.get('totalCount'),'recent_authors_sample50':authors,'issue_samples':(repo.get('issues') or {}).get('nodes',[]),'bank_status':'ALREADY IN THE BANK' if memberships else 'NEW','bank_layers':list(memberships),'bank_row':memberships.get('bank/bank_best.jsonl'),'shelf_row':memberships.get('capability-shelf/source-registry.jsonl'),'adoption_row':memberships.get('bank/bank_adoption_v2.jsonl'),'lift_row':memberships.get('bank/bank_liftable_ranked.jsonl'),'discovery':seed['discovery'],'root_entries':names,'source_files':{p:{k:v for k,v in d.items() if k!='text'} for p,d in docs.items()},'upstream_urls':{'commit':'https://github.com/'+n+'/commit/'+str(sha),'metadata':'https://api.github.com/repos/'+n},'build_status':'NOT_EXECUTED','review_status':'documentation_collected_not_scored'}
    # Short excerpts: unlicensed/ambiguous README at most 25 words; headings are structural evidence.
    cleaned=' '.join(re.sub(r'<[^>]*>',' ',rt).split());permissive=bool(lt) and r['license'] not in (None,'NOASSERTION')
    r['readme_excerpt']=' '.join(cleaned.split()[:180 if permissive else 25])
    # Read the actual full files; publish small identifying excerpts and immutable receipts only.
    r['license_excerpt']=' '.join(lt.split()[:25]);r['license_warnings']=[term for term in ['non-commercial','Commons Clause','BUSL','source available','commercial license','Zep Cloud','ZEP_API_KEY','cloud only'] if term.lower() in (lt+'\n'+rt).lower()]
    r['runtime_clues']=[line.strip()[:260] for line in rt.splitlines() if re.search(r'docker|self.host|local|minimum|memory|RAM|GPU|license|licence|archived|deprecat|successor|replaced|Python|Rust|requires',line,re.I)][:18]
    r['dependency_repos']=sorted(set(re.findall(r'https://github.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)',rt)))[:70]
    return r
for start in range(0,len(items),8):
    part=items[start:start+8];q='query{'+''.join('r'+str(j)+':repository(owner:'+json.dumps(x['name'].split('/')[0])+',name:'+json.dumps(x['name'].split('/')[1])+'){'+fields+'}' for j,x in enumerate(part))+'}'
    response=gql(q);pairs=[]
    for j,x in enumerate(part):
        if response.get('r'+str(j)):pairs.append((x,response['r'+str(j)]))
        else:unavailable.append(x)
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:batch=list(ex.map(examine,pairs))
    records.extend(batch);idx=start//8+1
    cards=[]
    for r in batch:
        compact={k:r[k] for k in ['id','stars','observed_at','latest_commit','last_commit_date','license','actual_license_paths','license_files_read','archived','recent_commit_count','recent_authors_sample50','bank_status','bank_layers','build_status','license_warnings']}
        cards.append('## '+r['full_name']+'\n'+r['url']+'\n'+json.dumps(compact)+'\n[vendor] '+str(r['description'])+'\nREADME: '+r['readme_excerpt']+'\nHeadings: '+'; '.join(r['readme_headings'])+'\nRuntime: '+' | '.join(r['runtime_clues'])+'\nLICENSE: '+r['license_excerpt']+'\nAdoption: '+json.dumps(r['adoption_row'])+'\nIssue sample: '+json.dumps(r['issue_samples'])+'\n')
    publish({PREFIX+f'batch-{idx:03d}.json':json.dumps(batch,indent=2),PREFIX+f'batch-{idx:03d}.md':'\n'.join(cards)},'research(trading): checkpoint public upstream documentation batch '+str(idx))
    print(json.dumps({'checkpoint':idx,'collected':len(records),'unavailable':len(unavailable)}),flush=True)
# ID-based de-duplication; aliases do not increase the count.
unique={r['id']:r for r in records}
summary={'observed_at':NOW,'status':'documentation_collected_requires_human_scoring','collected_unique_repositories':len(unique),'batch_count':(len(items)+7)//8,'unavailable':unavailable,'search_queries':len(log),'search_rounds':3,'two_dry_rounds_proven':False,'bank_sources':bank_receipts,'repo_index':[{'full_name':r['full_name'],'id':r['id'],'bank_status':r['bank_status'],'readme_read':r['readme_read'],'license_files_read':r['license_files_read']} for r in unique.values()]}
publish({PREFIX+'batched-collection-summary.json':json.dumps(summary,indent=2)},'research(trading): seal bounded public-source collection counts, no solution or build claim')
