"""Research-only collector. Reads public metadata/docs; never imports or executes a candidate.
Writes only packs/trading/evidence on the explicitly allowed research branch.
Company/workflow research was completed first; SHA-256 receipts below identify it.
"""
import os,json,urllib.request,urllib.error,urllib.parse,base64,hashlib,time,re,datetime,concurrent.futures
REPO='sisodias/siso-industry-packs'; BRANCH='research/trading-20260913'
assert os.environ['GITHUB_REPOSITORY']==REPO and os.environ['GITHUB_REF_NAME']==BRANCH
TOKEN=os.environ['GH_TOKEN']; API='https://api.github.com'
HEADERS={'Authorization':'Bearer '+TOKEN,'Accept':'application/vnd.github+json','User-Agent':'SISO-public-trading-research'}
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat(); SINCE='2026-03-13T00:00:00Z'
FREEZE={'03-companies.md':'5366652a2f0d50630928592dfc8c2cb255a7b15c4ec1593a9383534f933142b1','02-workflow.json':'44892d78bb38a77e0f37816a441bdad4d747c2da99ecf58aa9df0c8a6d2bfcdf'}
def api(path,data=None):
    for attempt in range(4):
        try:
            req=urllib.request.Request(API+path,headers=HEADERS,data=None if data is None else json.dumps(data).encode())
            with urllib.request.urlopen(req,timeout=60) as r:return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code in (403,429,500,502,503) and attempt<3:time.sleep(15*(attempt+1));continue
            return {'_error':e.code,'_path':path}
        except Exception as e:
            if attempt<3:time.sleep(2);continue
            return {'_error':type(e).__name__,'_path':path}

def raw(url):
    with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'SISO-public-trading-research'}),timeout=90) as r:return r.read()

def bank(path):
    url='https://raw.githubusercontent.com/sisodias/siso-repo-bank/main/'+path
    data=raw(url)
    return [json.loads(x) for x in data.decode().splitlines() if x.strip()],{'url':url,'sha256':hashlib.sha256(data).hexdigest()}

best,best_receipt=bank('bank/bank_best.jsonl'); shelf,shelf_receipt=bank('capability-shelf/source-registry.jsonl'); adoption,adopt_receipt=bank('bank/bank_adoption_v2.jsonl'); lift,lift_receipt=bank('bank/bank_liftable_ranked.jsonl'); tags,tag_receipt=bank('bank/bank_capability.jsonl')
bestmap={r['full_name'].lower():r for r in best}; shelfmap={r.get('repo','').lower():r for r in shelf}; adoptmap={r['full_name'].lower():r for r in adoption}; liftmap={r['full_name'].lower():r for r in lift if r.get('full_name')}
seeds='''OpenBB-finance/OpenBB NautilusTrader/nautilus_trader QuantConnect/Lean microsoft/qlib vnpy/vnpy mementum/backtrader polakowo/vectorbt kernc/backtesting.py pmorissette/bt pmorissette/ffn stefan-jansen/zipline-reloaded quantopian/zipline quantopian/pyfolio quantopian/alphalens stefan-jansen/pyfolio-reloaded stefan-jansen/alphalens-reloaded ranaroussi/quantstats PyPortfolio/PyPortfolioOpt dcajasn/Riskfolio-Lib skfolio/skfolio lballabio/QuantLib OpenSourceRisk/Engine OpenGamma/Strata finmath/finmath-lib domokane/FinancePy vollib/py_vollib bashtage/arch TA-Lib/ta-lib TA-Lib/ta-lib-python bukosabino/ta twopirllc/pandas-ta quantopian/empyrical freqtrade/freqtrade jesse-ai/jesse hummingbot/hummingbot hummingbot/gateway ccxt/ccxt bmoscon/cryptofeed bmoscon/cryptostore thrasher-corp/gocryptotrader Drakkar-Software/OctoBot Superalgos/Superalgos DeviaVir/zenbot askmike/gekko alpaca-markets/alpaca-py alpacahq/alpaca-trade-api-python InteractiveBrokers/tws-api-public ib-api-reloaded/ib_async erdewit/ib_insync IbcAlpha/IBC gnzsnz/ib-gateway-docker quickfix/quickfix quickfix-j/quickfixj quickfixgo/quickfix quickfixn/quickfixn fix8/fix8 da4089/simplefix fix-trading-community/orchestra nkaz001/hftbacktest ranaroussi/yfinance akfamily/akshare waditu/tushare FinanceData/FinanceDataReader dpguthrie/yahooquery pydata/pandas-datareader databento/databento-python databento/dbn polygon-io/client-python Nasdaq/data-link-python dgunning/edgartools jadchaar/sec-edgar-downloader sec-edgar/sec-edgar Arelle/Arelle ofxparse/ofxparse libofx/libofx csingley/ofxtools beancount/beanprice beancount/beancount beancount/beangulp beancount/fava ledger/ledger simonmichael/hledger Gnucash/gnucash ofxstatement/ofxstatement portfolio-performance/portfolio ghostfolio/ghostfolio rotki/rotki eprbell/rp2 eprbell/dali-rp2 BittyTax/BittyTax Polymarket/py-clob-client Polymarket/clob-client Polymarket/agents Polymarket/ctf-exchange gnosis/conditional-tokens-contracts Polymarket/poly-market-maker Polymarket/py-order-utils Polymarket/order-utils Polymarket/real-time-data-client Polymarket/builder-signing-sdk Polymarket/builder-relayer-client Polymarket/py-builder-signing-sdk Polymarket/py-builder-relayer-client Polymarket/safe-wallet-integration Polymarket/subgraph Kalshi/kalshi-starter-code-python manifoldmarkets/manifold metaculus/metaculus gnosis/prediction-market-agent-tooling gnosis/prediction-market-agent sisodias/MiroFish TauricResearch/TradingAgents AI4Finance-Foundation/FinGPT AI4Finance-Foundation/FinRL AI4Finance-Foundation/FinRobot HKUDS/Vibe-Trading virattt/ai-hedge-fund virattt/dexter Eleven-Trading/TradeNote marketcalls/openalgo StockSharp/StockSharp edtechre/pybroker zvtvz/zvt paperswithbacktest/awesome-systematic-trading wangzhe3224/awesome-systematic-trading wilsonfreitas/awesome-quant QuantLib/QuantLib-SWIG QuantConnect/lean-cli QuantConnect/Lean.DataSource.Polygon duckdb/duckdb jupyterlab/jupyterlab marimo-team/marimo jupytext/jupytext'''.split()
queries=[
(1,'W01','A','trading journal'),(1,'W01','B','topic:trading-journal'),(1,'W01','C','EML trading'),
(1,'W02','A','market data'),(1,'W02','B','topic:market-data'),(1,'W02','C','DBN market'),
(1,'W03','A','investment research'),(1,'W03','B','topic:quantitative-finance'),(1,'W03','C','notebook portfolio'),
(1,'W04','A','backtesting engine'),(1,'W04','B','topic:backtesting'),(1,'W04','C','Parquet backtest'),
(1,'W05','A','portfolio risk'),(1,'W05','B','topic:portfolio-optimization'),(1,'W05','C','options symbol'),
(1,'W06','A','order management trading'),(1,'W06','B','topic:fix-protocol'),(1,'W06','C','FIX trading'),
(1,'W07','A','trading alerts'),(1,'W07','B','topic:orderbook'),(1,'W07','C','WebSocket orderbook'),
(1,'W08','A','broker reconciliation'),(1,'W08','B','topic:portfolio-management'),(1,'W08','C','Flex Interactive Brokers'),
(1,'W09','A','self hosted trade journal'),(1,'W09','B','topic:trade-journal'),(1,'W09','C','trading CSV journal'),
(1,'W10','A','tax lots'),(1,'W10','B','topic:cryptocurrency-tax'),(1,'W10','C','OFX parser'),
(2,'W01-W10','registry','awesome quant'),(2,'W02','format','ITCH market'),(2,'W06','format','DTC trading'),(2,'W06','format','FIXML'),(2,'W10','format','QIF parser'),(2,'W02','format','XBRL parser'),(2,'W08','bridge','IBKR statement'),(2,'W06','SDK','Polymarket client'),(2,'W05','format','ERC1155 prediction'),(2,'W10','format','tax FIFO'),(2,'W03','application','Bloomberg terminal alternative'),(2,'W08','format','prediction market resolution'),(2,'W10','format','options exercise assignment'),
(3,'W02','maintainer','user:databento'),(3,'W10','maintainer','user:beancount'),(3,'W06','maintainer','user:ib-api-reloaded'),(3,'W06','maintainer','user:Polymarket'),(3,'W09','topic','topic:trading-journal pushed:>2026-03-13'),(3,'W04','topic','topic:backtesting language:Rust'),(3,'W03','topic','topic:prediction-market'),(3,'W10','topic','topic:tax-calculator cryptocurrency')]
seen={n.lower():{'name':n,'discovery':[{'round':0,'lane':'prior-lead-not-verified'}]} for n in seeds}; log=[]
for rnd,stage,lane,q in queries:
    url='/search/repositories?'+urllib.parse.urlencode({'q':q,'sort':'stars','order':'desc','per_page':8})
    result=api(url); items=result.get('items',[]); added=[]
    for item in items:
        n=item['full_name']; k=n.lower()
        if k not in seen:seen[k]={'name':n,'discovery':[]};added.append(n)
        seen[k]['discovery'].append({'round':rnd,'stage':stage,'lane':lane,'query':q})
    log.append({'round':rnd,'stage':stage,'lane':lane,'query':q,'url':API+url,'total_count':result.get('total_count'),'returned':[i['full_name'] for i in items],'new':added,'error':result.get('_error')})
    print(json.dumps({'round':rnd,'stage':stage,'lane':lane,'new':len(added),'total':len(seen),'error':result.get('_error')}),flush=True)
    time.sleep(2.2)

def decode_file(doc):
    try:
        if doc.get('content'):return base64.b64decode(doc['content']).decode('utf-8','replace')
        if doc.get('download_url'):return raw(doc['download_url']).decode('utf-8','replace')
    except Exception:return ''
    return ''

def examine(item):
    requested=item['name']; meta=api('/repos/'+requested)
    if meta.get('_error') or meta.get('private'):return {'requested_name':requested,'status':'unavailable','error':meta.get('_error'),'discovery':item['discovery']}
    n=meta['full_name']; base='/repos/'+n
    commits=api(base+'/commits?per_page=100&since='+SINCE)
    recent=commits if isinstance(commits,list) else []
    last=recent[0] if recent else (api(base+'/commits?per_page=1') or [{}])
    if isinstance(last,list):last=last[0] if last else {}
    sha=last.get('sha'); date=last.get('commit',{}).get('committer',{}).get('date')
    ref=urllib.parse.quote(sha or meta['default_branch'],safe='')
    rd=api(base+'/readme?ref='+ref); lic=api(base+'/license?ref='+ref); readme=decode_file(rd); license_text=decode_file(lic)
    roots=api(base+'/contents?ref='+ref); roots=roots if isinstance(roots,list) else []
    contrib=api(base+'/contributors?per_page=30'); contrib=contrib if isinstance(contrib,list) else []
    issues=api(base+'/issues?state=all&sort=updated&direction=desc&per_page=10'); issues=issues if isinstance(issues,list) else []
    issue=next((i for i in issues if not i.get('pull_request')),None)
    issue_receipt=None
    if issue:
        comments=api(base+'/issues/'+str(issue['number'])+'/comments?per_page=20')
        staff=[c for c in comments if c.get('author_association') in ('OWNER','MEMBER','COLLABORATOR')] if isinstance(comments,list) else []
        issue_receipt={'url':issue['html_url'],'created_at':issue['created_at'],'state':issue['state'],'comments':issue['comments'],'first_staff_comment_in_sample':staff[0]['created_at'] if staff else None,'sample_limit':20}
    deps={}
    for p in ['pyproject.toml','requirements.txt','package.json','Cargo.toml','setup.py']:
        entry=next((e for e in roots if e['name']==p),None)
        if entry:
            t=decode_file(api(base+'/contents/'+p+'?ref='+ref));deps[p]={'url':'https://github.com/'+n+'/blob/'+str(sha)+'/'+p,'sha256':hashlib.sha256(t.encode()).hexdigest(),'text':t[:16000]}
            if len(deps)>=2:break
    bm=bestmap.get(n.lower()) or bestmap.get(requested.lower()); sm=shelfmap.get(n.lower()) or shelfmap.get(requested.lower()); am=adoptmap.get(n.lower()) or adoptmap.get(requested.lower()); lm=liftmap.get(n.lower()) or liftmap.get(requested.lower())
    layers=[x for x,v in [('bank_best',bm),('product_shelf',sm),('adoption',am),('liftable',lm)] if v is not None]
    license_id=lic.get('license',{}).get('spdx_id') or (meta.get('license') or {}).get('spdx_id')
    # Text is evidence only. No execution, install, tests, price data, account access or inference calls.
    record={'full_name':n,'requested_name':requested,'id':meta['id'],'url':meta['html_url'],'observed_at':NOW,'status':'documentation_collected','description':meta.get('description'),'stars':meta['stargazers_count'],'forks':meta['forks_count'],'archived':meta['archived'],'fork':meta['fork'],'language':meta.get('language'),'default_branch':meta['default_branch'],'latest_commit':sha,'last_commit_date':date,'pushed_at_not_commit_date':meta['pushed_at'],'commits_since_20260313_count_capped100':len(recent),'recent_commit_authors':sorted(set((c.get('author') or {}).get('login') or c.get('commit',{}).get('author',{}).get('name','unknown') for c in recent)),'contributors_sample':[{'login':c.get('login'),'contributions':c.get('contributions'),'type':c.get('type')} for c in contrib],'issue_response_sample':issue_receipt,'readme_path':rd.get('path'),'readme_sha256':hashlib.sha256(readme.encode()).hexdigest(),'readme_text':readme,'license':license_id,'license_path':lic.get('path'),'license_file_sha256':hashlib.sha256(license_text.encode()).hexdigest(),'license_text':license_text,'license_candidates':[e['path'] for e in roots if re.search('licen[cs]e|copying|notice',e['name'],re.I)],'root_entries':[e['name'] for e in roots],'dependency_manifests':deps,'bank_status':'ALREADY IN THE BANK' if layers else 'NEW','bank_layers':layers,'bank_row':bm,'shelf_row':sm,'adoption_row':am,'liftability_row':lm,'discovery':item['discovery'],'source_urls':{'metadata':API+base,'commit':'https://github.com/'+n+'/commit/'+str(sha),'readme':rd.get('html_url'),'license':lic.get('html_url'),'recent_commits':API+base+'/commits?since='+SINCE,'contributors':API+base+'/contributors','issues':API+base+'/issues'}}
    return record

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex: records=list(ex.map(examine,seen.values()))
# Deduplicate aliases by stable repository ID after collecting redirects.
unique={};unavailable=[]
for r in records:
    if r.get('id'):
        if r['id'] in unique:unique[r['id']]['discovery']+=r['discovery']
        else:unique[r['id']]=r
    else:unavailable.append(r)
records=sorted(unique.values(),key=lambda r:r['full_name'].lower())
files={};prefix='packs/trading/evidence/'
manifest={'observed_at':NOW,'method':'public GitHub API documentation collection; no candidate executed; collected != individually reviewed','company_workflow_freeze_sha256':FREEZE,'candidate_seeds':seeds,'search_results_are_top8_not_exhaustive':True,'search_queries':len(log),'collected':len(records),'unavailable':unavailable,'bank_sources':{'best':best_receipt,'shelf':shelf_receipt,'adoption':adopt_receipt,'liftable':lift_receipt,'tags':tag_receipt},'capability_tags':[r['capability'] for r in tags]}
files[prefix+'collection-manifest.json']=json.dumps(manifest,indent=2)
files[prefix+'search-rounds-1-3.json']=json.dumps(log,indent=2)
pattern=re.compile(r'trad(e|ing|er)|portfolio|backtest|market.?data|financ|accounting|ledger|prediction.?market|polymarket|broker|quantitative|research.?notebook',re.I)
files[prefix+'bank-product-bases.md']='# Product shelf: targeted source scan\n\nSource: '+shelf_receipt['url']+'\n\n'+'\n'.join('| '+r.get('repo','')+' | '+', '.join(r.get('family_names',[]))+' | '+str(r.get('priority_score'))+' | '+'; '.join(r.get('observed_facts',[]))+' |' for r in shelf if pattern.search(json.dumps(r)))
files[prefix+'bank-prior-candidates.md']='# Rated bank: targeted source scan\n\nSource: '+best_receipt['url']+'\n\n'+'\n'.join('| '+r['full_name']+' | '+str(r.get('capability_tag'))+' | '+str(r.get('summary'))+' |' for r in best if pattern.search(json.dumps(r)))
for i in range(0,len(records),8):
    batch=records[i:i+8]; bi=i//8+1; views=[];receipts=[]
    for r in batch:
        # Read full documents in-memory. Commit hashes/URLs and short research excerpts only.
        excerpt=' '.join(re.sub(r'<[^>]+>',' ',r['readme_text']).split())[:1400]
        lic_excerpt=' '.join(r['license_text'].split())[:500]
        views.append('## '+r['full_name']+'\nSource: '+r['url']+'\n'+json.dumps({k:r[k] for k in ['stars','observed_at','latest_commit','last_commit_date','license','license_path','bank_status','bank_layers','archived','commits_since_20260313_count_capped100','language']})+'\nDescription [vendor]: '+str(r['description'])+'\nREADME excerpt [vendor, not an endorsement]: '+excerpt+'\nActual LICENSE excerpt: '+lic_excerpt+'\nRecent author count: '+str(len(r['recent_commit_authors']))+'; sampled contributors: '+str(len(r['contributors_sample']))+'\nAdoption bank: '+json.dumps(r['adoption_row'])+'\nIssue sample: '+json.dumps(r['issue_response_sample'])+'\nManifests: '+', '.join(r['dependency_manifests'])+'\n')
        z=dict(r);z.pop('readme_text');z.pop('license_text');z['readme_excerpt']=excerpt;z['license_excerpt']=lic_excerpt
        z['dependency_manifests']={p:{k:v for k,v in d.items() if k!='text'} for p,d in z['dependency_manifests'].items()}
        receipts.append(z)
    files[prefix+f'review-{bi:03d}.md']='\n'.join(views)
    files[prefix+f'receipts-{bi:03d}.json']=json.dumps(receipts,indent=2)
# One atomic research commit, preserving the branch's existing tree.
ref=api('/repos/'+REPO+'/git/ref/heads/'+urllib.parse.quote(BRANCH,safe='/'));parent=ref['object']['sha'];commit=api('/repos/'+REPO+'/git/commits/'+parent)
tree=api('/repos/'+REPO+'/git/trees',{'base_tree':commit['tree']['sha'],'tree':[{'path':p,'mode':'100644','type':'blob','content':c+'\n'} for p,c in files.items()]})
new=api('/repos/'+REPO+'/git/commits',{'message':'research(trading): public source collection and bank overlap receipts; not build verification','tree':tree['sha'],'parents':[parent]})
req=urllib.request.Request(API+'/repos/'+REPO+'/git/refs/heads/'+BRANCH,data=json.dumps({'sha':new['sha'],'force':False}).encode(),headers=HEADERS,method='PATCH')
with urllib.request.urlopen(req,timeout=60) as r:json.load(r)
print(json.dumps({'collected':len(records),'unavailable':len(unavailable),'files':len(files),'commit':new['sha']}),flush=True)
