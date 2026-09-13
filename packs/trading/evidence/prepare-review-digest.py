"""Prepare bounded review views from completed public-source receipts; no app code."""
import os,json,urllib.request,urllib.error,urllib.parse,base64,hashlib,time,re,datetime,concurrent.futures,ast
REPO='sisodias/siso-industry-packs';BRANCH='research/trading-20260913';PREFIX='packs/trading/evidence/'
assert os.environ['GITHUB_REPOSITORY']==REPO and os.environ['GITHUB_REF_NAME']==BRANCH
TOKEN=os.environ['GH_TOKEN'];HEADERS={'Authorization':'Bearer '+TOKEN,'Accept':'application/vnd.github+json','User-Agent':'siso-public-research'}
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
url='https://raw.githubusercontent.com/'+REPO+'/3b238f72e13b3a480c4d6ac455ff66634749fbbf/'+PREFIX+'collect-batched-evidence.py'
with urllib.request.urlopen(url,timeout=30) as response: source=response.read().decode()
module=ast.parse(source)
for node in module.body:
    if isinstance(node,ast.FunctionDef) and node.name in ('raw','gql','publish','examine'):
        exec(compile(ast.Module(body=[node],type_ignores=[]),url,'exec'))
    if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='fields' for t in node.targets):fields=ast.literal_eval(node.value)
base='https://raw.githubusercontent.com/'+REPO+'/'+BRANCH+'/'+PREFIX
summary=json.loads(raw(base+'batched-collection-summary.json'))
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
    batches=list(ex.map(lambda i:json.loads(raw(base+f'batch-{i:03d}.json')),range(1,summary['batch_count']+1)))
records=list({r['id']:r for batch in batches for r in batch}.values())
# Supplementary direct-connector leads: owner correction and current versioned SDKs.
banks={};bank_notes={}
for p,key in [('bank/bank_best.jsonl','full_name'),('capability-shelf/source-registry.jsonl','repo'),('bank/bank_adoption_v2.jsonl','full_name'),('bank/bank_liftable_ranked.jsonl','full_name')]:
    data=raw('https://raw.githubusercontent.com/sisodias/siso-repo-bank/main/'+p);assert data
    rows=[json.loads(x) for x in data.decode().splitlines() if x.strip()];banks[p]={r[key].lower():r for r in rows if r.get(key)}
    bank_notes[p]={'rows':len(rows),'sha256':hashlib.sha256(data).hexdigest(),'aliases_to_review':[r for r in rows if re.search(r'openbb|nautilus|alpaca|quantlib|pyportfolio|qlib|polymarket',str(r.get(key,'')),re.I)]}
extra=['nautechsystems/nautilus_trader','alpacahq/alpaca-py','Polymarket/py-clob-client-v2','Polymarket/clob-client-v2','Polymarket/rs-clob-client-v2']
extra=[n for n in extra if n.lower() not in {r['full_name'].lower() for r in records}]
q='query{'+''.join('r'+str(j)+':repository(owner:'+json.dumps(n.split('/')[0])+',name:'+json.dumps(n.split('/')[1])+'){'+fields+'}' for j,n in enumerate(extra))+'}' if extra else None
response=gql(q) if q else {};new=[]
for j,n in enumerate(extra):
    if response.get('r'+str(j)):
        new.append(examine(({'name':n,'discovery':[{'round':4,'lane':'direct-connector owner/version reconciliation'}]},response['r'+str(j)])))
records+=new
files={PREFIX+'supplemental-receipts.json':json.dumps(new,indent=2),PREFIX+'bank-identity-review.json':json.dumps(bank_notes,indent=2)}
def clean(text):return re.sub(r'\s+',' ',str(text or '')).replace('|','/').strip()
for start in range(0,len(records),20):
    lines=['# Compact examination queue '+str(start//20+1),'','All facts [vendor/project-owner] collected 2026-09-13; no build execution. Scores are deliberately absent until reviewed. Full revision and actual LICENSE-file receipts are in the corresponding batch JSON.','', '| Index / repository | Stars; latest default-branch commit; root license | Bank; health evidence | Declared purpose and documentation scope |','|---|---|---|---|']
    for i,r in enumerate(records[start:start+20],start+1):
        purpose=clean(r.get('description'))[:190];heads=clean('; '.join(r['readme_headings'][:7]))[:230]
        license_label=str(r['license'])+' ('+','.join(r['actual_license_paths'])+')'
        health=str(r['recent_commit_count'])+' recent commits; '+str(len(r['recent_authors_sample50']))+' sampled authors; '+('ARCHIVED' if r['archived'] else 'not archived')
        ad=r.get('adoption_row');adtext='no adoption row' if not ad else 'adoption package='+str(ad.get('pkg_name'))+', resolved='+str(ad.get('resolved'))+', dependent repos='+str(ad.get('dependent_repos'))+', fame_gap='+str(ad.get('fame_gap'))
        lines.append('| '+str(i)+' ['+r['full_name']+']('+r['url']+') | '+str(r['stars'])+'; '+str(r['last_commit_date'])+'; '+license_label+' | '+r['bank_status']+'; '+health+'; '+adtext+' | '+purpose+' / '+heads+' |')
    files[PREFIX+f'compact-{start//20+1:02d}.md']='\n'.join(lines)+'\n'
# Whole product shelf and bank leads in compact views: helps check reuse rather than rediscover.
pattern=re.compile(r'trad(e|ing|er)|portfolio|backtest|market.?data|financ|accounting|ledger|prediction.?market|polymarket|broker|quantitative|research.?notebook',re.I)
for p,label in [('capability-shelf/source-registry.jsonl','product-bases'),('bank/bank_best.jsonl','rated-bank-leads')]:
    rows=[r for r in banks[p].values() if pattern.search(json.dumps(r))]
    lines=['# '+label+' — targeted whole-corpus scan, not upstream verification','']
    for r in rows:
        name=r.get('repo') or r.get('full_name');lines.append('- '+name+' | '+clean(r.get('summary') or r.get('family_names'))+' | '+str(r.get('priority_score') or r.get('reuse_value')))
    files[PREFIX+'compact-'+label+'.md']='\n'.join(lines)+'\n'
files[PREFIX+'compact-index.json']=json.dumps({'collected_unique':len(records),'compact_pages':(len(records)+19)//20,'supplemental_new_count':len(new),'reviewed_count':None,'two_dry_rounds_proven':False,'repositories':[{'index':i,'full_name':r['full_name'],'id':r['id']} for i,r in enumerate(records,1)]},indent=2)
publish(files,'research(trading): compact review queue and upstream owner/version corrections')
print(json.dumps({'unique_collected':len(records),'supplemental':len(new),'files':len(files)}))
