"""Public-source research collector; does not execute candidate software or read client records."""
import base64, concurrent.futures, datetime, hashlib, json, os, pathlib, re, subprocess, tempfile, time, urllib.error, urllib.parse, urllib.request
REPO='sisodias/siso-industry-packs'; ROOT='packs/recruiting_staffing/evidence/'; NOW=datetime.datetime.now(datetime.timezone.utc).isoformat(); TOKEN=os.environ['GH_TOKEN']; OUT={}
assert os.environ['GH_REPOSITORY']==REPO

def texturl(url):
    assert url.startswith('https://raw.githubusercontent.com/')
    for attempt in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'SISO-public-research'}),timeout=90) as r:return r.read()
        except urllib.error.HTTPError as e:
            if e.code==404:return None
            if attempt==2:raise
            time.sleep(2)

def ownjson(name,ref='main'):
    b=texturl('https://raw.githubusercontent.com/'+REPO+'/'+ref+'/'+ROOT+name)
    if b is None:raise RuntimeError('Required public receipt missing: '+name)
    return json.loads(b)

def gql(query):
    for attempt in range(3):
        req=urllib.request.Request('https://api.github.com/graphql',data=json.dumps({'query':query}).encode(),headers={'Authorization':'Bearer '+TOKEN,'Content-Type':'application/json','User-Agent':'SISO-public-research'})
        try:
            with urllib.request.urlopen(req,timeout=90) as r:obj=json.load(r)
            if obj.get('errors') and not obj.get('data'):raise RuntimeError('GraphQL: '+str([e.get('type',e.get('message')) for e in obj['errors']]))
            return obj
        except urllib.error.HTTPError as e:
            if attempt==2:raise RuntimeError('GraphQL HTTP '+str(e.code)) from None
            time.sleep(3)

def out(name,value):
    assert re.fullmatch(r'[a-zA-Z0-9_.-]+',name)
    OUT[ROOT+name]=value if isinstance(value,str) else json.dumps(value,ensure_ascii=False,indent=2)+'\n'

def short(s,n=35):return ' '.join((s or '').split()[:n])

def normalize(obj):
    for q in obj['queries']:
        for x in q.get('hits',[]):x['description']=short(x.get('description'),25)
    return obj

def searchfiles(obj):
    rnd=str(obj['round']).zfill(2);out('search-round-'+rnd+'.json',obj)
    out('search-round-'+rnd+'-brief.jsonl',''.join(json.dumps({k:v for k,v in q.items() if k!='hits'}|{'hits':[(x['full_name'],x['stargazers_count'],x['description']) for x in q.get('hits',[])]},ensure_ascii=False)+'\n' for q in obj['queries']))

cfg=ownjson('audit-request.json',os.environ['REQUEST_REVISION']);assert cfg['mode'] in ('search','candidates','normalize')
known=set(n.lower() for n in cfg.get('previously_seen',[]))
for rnd in cfg.get('previous_rounds',[]):
    old=normalize(ownjson('search-round-'+str(rnd).zfill(2)+'.json'))
    for q in old['queries']:
        for x in q.get('hits',[]):known.add(x['full_name'].lower())
    searchfiles(old)
if cfg['mode']=='search':
    queries=cfg['queries'];assert 1<=len(queries)<=60;records=[];added=set()
    for q in queries:
        n=q.get('per_page',8);assert 1<=n<=30
        query=q['query']+' sort:stars-desc';cursor=q.get('after')
        args='query:'+json.dumps(query)+',type:REPOSITORY,first:'+str(n)+((',after:'+json.dumps(cursor)) if cursor else '')
        result=gql('query { search('+args+') { repositoryCount pageInfo { hasNextPage endCursor } nodes { ... on Repository { nameWithOwner description url stargazerCount isArchived pushedAt licenseInfo { spdxId name } repositoryTopics(first:10) { nodes { topic { name } } } } } } }')
        data=result.get('data',{}).get('search') or {};row={**q,'observed_at':NOW,'source_url':'https://github.com/search?type=repositories&q='+urllib.parse.quote(query),'total_count':data.get('repositoryCount'),'pagination':data.get('pageInfo'),'error':result.get('errors'),'hits':[],'new_names':[]}
        for x in data.get('nodes',[]):
            if not x:continue
            name=x['nameWithOwner'];row['hits'].append({'full_name':name,'description':short(x.get('description'),25),'html_url':x['url'],'stargazers_count':x['stargazerCount'],'archived':x['isArchived'],'pushed_at':x['pushedAt'],'license':x.get('licenseInfo'),'topics':[t['topic']['name'] for t in x['repositoryTopics']['nodes']]})
            if name.lower() not in known:known.add(name.lower());added.add(name);row['new_names'].append(name)
        records.append(row);time.sleep(.4)
    searchfiles({'round':cfg['round'],'observed_at':NOW,'queries':records,'unique_new_count':len(added),'new_names':sorted(added),'scope':'Bounded declared queries and first pages, not an exhaustive global GitHub search. Errors are not dry results.'})
elif cfg['mode']=='candidates':
    names=list(dict.fromkeys(cfg['repositories']));assert 100<=len(names)<=160 and all(re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+',n) for n in names)
    fields='nameWithOwner url description stargazerCount isArchived isDisabled licenseInfo { spdxId name } defaultBranchRef { name target { ... on Commit { oid committedDate history(first:10) { nodes { oid committedDate } } } } } object(expression:"HEAD:") { ... on Tree { entries { name type oid } } } issues(first:3,orderBy:{field:UPDATED_AT,direction:DESC},states:[OPEN,CLOSED]) { nodes { number title createdAt updatedAt closedAt url comments(first:5) { nodes { authorAssociation createdAt url } } } }'
    rows=[]
    for start in range(0,len(names),8):
        batch=names[start:start+8];parts=[]
        for i,name in enumerate(batch):
            owner,repo=name.split('/');parts.append('r'+str(i)+':repository(owner:'+json.dumps(owner)+',name:'+json.dumps(repo)+') {'+fields+'}')
        result=gql('query {'+' '.join(parts)+'}');data=result.get('data') or {}
        for i,name in enumerate(batch):
            x=data.get('r'+str(i));r={'audit_id':'R'+str(start+i+1).zfill(3),'requested_full_name':name,'observed_at':NOW}
            if not x:rows.append(r|{'retrieval_error':result.get('errors','not found')});continue
            branch=x.get('defaultBranchRef') or {};commit=branch.get('target') or {};r.update({'full_name':x['nameWithOwner'],'html_url':x['url'],'description':short(x['description']),'stargazers_count':x['stargazerCount'],'archived':x['isArchived'],'disabled':x['isDisabled'],'license':x.get('licenseInfo'),'default_branch':branch.get('name'),'revision':commit.get('oid'),'last_commit':commit.get('committedDate'),'recent_commits':[{'sha':c['oid'],'date':c['committedDate']} for c in commit.get('history',{}).get('nodes',[])],'root_entries':(x.get('object') or {}).get('entries',[]),'issue_sample':x['issues']['nodes'],'bus_factor':'Not measured; issue participation is not maintainership redundancy.'})
            r['sources']={'repository':x['url'],'commit':x['url']+'/commit/'+str(r['revision'])};rows.append(r)
    def file_record(r,path,words=120):
        if not path:return {'error':'No matching root filename; not an assertion that no nested license exists.'}
        b=texturl('https://raw.githubusercontent.com/'+r['full_name']+'/'+r['revision']+'/'+urllib.parse.quote(path,safe='/'))
        if b is None:return {'path':path,'error':'404'}
        t=b.decode('utf-8','replace');return {'path':path,'sha256':hashlib.sha256(b).hexdigest(),'characters_read':len(t),'excerpt':short(t,words),'source_url':r['html_url']+'/blob/'+r['revision']+'/'+path,'edition_flags':[s for s in ('enterprise','commercial','non-production','self-host','docker','payroll','recruit','api') if s in t.lower()]}
    def files(r):
        if not r.get('revision'):return r
        entries=r['root_entries'];readmes=[e['name'] for e in entries if re.fullmatch(r'README(?:\.(?:md|rst|txt|markdown))?',e['name'],re.I)];lics=[e['name'] for e in entries if re.fullmatch(r'(?:LICENSE|LICENCE|COPYING)(?:\.(?:md|txt|rst))?',e['name'],re.I)]
        r['readme']=file_record(r,readmes[0] if readmes else None)
        r['license_file']=file_record(r,lics[0] if lics else None,100)
        r['root_license_files']=lics;r['edition_review']='Root only; final selected edition and subdirectory rights require separate audit.'
        return r
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:rows=list(pool.map(files,rows))
    bankrepo='sisodias/siso-repo-bank';head=gql('query { repository(owner:"sisodias",name:"siso-repo-bank") { defaultBranchRef { target { oid } } } }')['data']['repository']['defaultBranchRef']['target']['oid']
    paths=['bank/bank_capability_top.jsonl','bank/bank_capability.jsonl','capability-shelf/source-registry.jsonl','bank/bank_best.jsonl','bank/bank_adoption_v2.jsonl','bank/bank_liftable_ranked.jsonl','bank/bank_contractcard.jsonl'];wanted={n.lower() for n in names}|{r['full_name'].lower() for r in rows if r.get('full_name')};bank={};receipts=[]
    def fullname(row):
        for k in ('full_name','repo_full_name','repository_full_name','repository','repo','name','url','repo_url','repository_url','source_url'):
            v=row.get(k)
            if isinstance(v,str):
                v=v.removeprefix('https://github.com/').removesuffix('.git').strip('/')
                if re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+',v):return v.lower()
    for path in paths:
        digest=hashlib.sha256();count=0;idx={};url='https://raw.githubusercontent.com/'+bankrepo+'/'+head+'/'+path
        with urllib.request.urlopen(url,timeout=90) as stream:
            for line in stream:
                digest.update(line)
                if not line.strip():continue
                row=json.loads(line);count+=1;n=fullname(row)
                if n in wanted:idx.setdefault(n,[]).append(row)
        bank[path]=idx;receipts.append({'path':path,'rows':count,'sha256':digest.hexdigest(),'source_url':'https://github.com/'+bankrepo+'/blob/'+head+'/'+path})
    for i,r in enumerate(rows,1):
        aliases={r['requested_full_name'].lower(),r.get('full_name','').lower()};r['bank_revision']=head;r['bank_rows']={p:[x for a in aliases for x in idx.get(a,[])] for p,idx in bank.items() if p!='bank/bank_capability.jsonl'};r['bank_membership_layers']=[p for p,v in r['bank_rows'].items() if v];r['bank_status']='ALREADY IN THE BANK' if r['bank_membership_layers'] else 'NEW';r['adoption_evidence']=r['bank_rows'].get('bank/bank_adoption_v2.jsonl',[]);out('repo-'+str(i).zfill(3)+'.json',r)
    for start in range(0,len(rows),5):
        review=[]
        for r in rows[start:start+5]:
            x={k:r.get(k) for k in ('audit_id','full_name','description','stargazers_count','archived','last_commit','revision','license','bank_status','adoption_evidence','readme','license_file','retrieval_error')};x['recent_commit_sample']=len([c for c in r.get('recent_commits',[]) if c['date']>='2026-03-13']);x['issues']=[{'number':i['number'],'closed_at':i['closedAt'],'comments':len(i['comments']['nodes']),'source_url':i['url']} for i in r.get('issue_sample',[])];review.append(x)
        out('review-'+str(start//5+1).zfill(2)+'.jsonl',''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in review))
    out('candidate-index.jsonl',''.join(json.dumps({k:r.get(k) for k in ('audit_id','full_name','description','stargazers_count','archived','last_commit','license','bank_status')},ensure_ascii=False)+'\n' for r in rows))
    out('candidate-audit-receipt.json',{'observed_at':NOW,'bank_revision':head,'files':receipts,'requested':len(names),'unique_canonical_repositories':len({r['full_name'].lower() for r in rows if r.get('full_name')}),'repositories_retrieved':sum(bool(r.get('full_name')) for r in rows),'readmes_retrieved':sum(bool(r.get('readme',{}).get('excerpt')) for r in rows),'license_files_retrieved':sum(bool(r.get('license_file',{}).get('excerpt')) for r in rows),'current_commit_retrieved':sum(bool(r.get('revision')) for r in rows),'already_in_bank':sum(r.get('bank_status')=='ALREADY IN THE BANK' for r in rows),'new':sum(r.get('bank_status')=='NEW' for r in rows),'execution':'Public text and metadata only; candidate applications never executed. Analyst review required before counting as examined.','membership_definition':'Exact case-insensitive requested/canonical name match in six exported repo-bearing layers; missing adoption is unknown, not zero users.'})
else:out('normalization-receipt.json',{'observed_at':NOW,'rounds':cfg.get('previous_rounds',[]),'description_words':25})

# Persist every output before publication. Git transport avoids consuming REST request quota.
work=pathlib.Path(tempfile.mkdtemp(prefix='recruiting-evidence-'));env=os.environ.copy();env.update({'GIT_CONFIG_COUNT':'1','GIT_CONFIG_KEY_0':'http.https://github.com/.extraheader','GIT_CONFIG_VALUE_0':'AUTHORIZATION: basic '+base64.b64encode(('x-access-token:'+TOKEN).encode()).decode(),'GIT_TERMINAL_PROMPT':'0'})
def git(*args,check=True):
    p=subprocess.run(['git',*args],cwd=work,env=env,capture_output=True,text=True)
    if check and p.returncode:raise RuntimeError('Git operation failed: '+args[0]+'; exit '+str(p.returncode))
    return p
for p,t in OUT.items():
    dest=work/p;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(t)
git('init','-q');git('remote','add','origin','https://github.com/'+REPO+'.git');git('config','user.name','SISO Research');git('config','user.email','research@users.noreply.github.com')
for attempt in range(6):
    git('fetch','--depth=1','origin','main');git('read-tree','origin/main')
    for p,t in OUT.items():
        dest=work/p;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(t)
    git('add','--',*list(OUT));tree=git('write-tree').stdout.strip();parent=git('rev-parse','origin/main').stdout.strip();commit=git('commit-tree',tree,'-p',parent,'-m','research(recruiting_staffing): publish '+cfg['mode']+' public evidence').stdout.strip()
    result=git('push','origin',commit+':refs/heads/main',check=False)
    if result.returncode==0:print('Published',len(OUT),'research files at',commit);break
    time.sleep(2)
else:raise RuntimeError('Publication blocked by repeated concurrent updates; local outputs retained at '+str(work))
print('No candidate application code executed; no deployment or client data access.')
