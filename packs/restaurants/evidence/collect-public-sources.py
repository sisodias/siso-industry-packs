"""Bounded public-source evidence collection, never application execution."""
import base64, concurrent.futures, datetime, hashlib, json, os, pathlib, re, time, urllib.request, urllib.error, urllib.parse
API='https://api.github.com'; TOKEN=os.environ['GH_TOKEN']; OUT=pathlib.Path('evidence'); OUT.mkdir(exist_ok=True)
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
assert os.environ['GITHUB_REPOSITORY']=='sisodias/siso-industry-packs'
assert os.environ['GITHUB_REF']=='refs/heads/research/restaurants-ac-blueprint-20260913'
def api(path):
    assert path.startswith('/repos/') or path.startswith('/search/repositories?')
    for attempt in range(3):
        request=urllib.request.Request(API+path,headers={'Authorization':'Bearer '+TOKEN,'Accept':'application/vnd.github+json','User-Agent':'siso-restaurants-ac-public-evidence'})
        try:
            with urllib.request.urlopen(request,timeout=40) as response: return json.load(response)
        except urllib.error.HTTPError as e:
            error={'_error':e.code,'path':path,'message':e.read().decode('utf-8','replace')[:250]}
            if e.code in (403,429,500,502,503,504) and attempt<2:
                delay=max(5,int(e.headers.get('Retry-After','5')))
                if e.headers.get('X-RateLimit-Remaining')=='0': delay=max(delay,int(e.headers.get('X-RateLimit-Reset','0'))-int(time.time())+2)
                if delay>90:return error
                time.sleep(delay);continue
            return error
        except (OSError,TimeoutError):
            if attempt<2:time.sleep(3);continue
            return {'_error':'network','path':path}
def save(name,value):
    assert re.fullmatch(r'[A-Za-z0-9_.-]+',name)
    text=value if isinstance(value,str) else json.dumps(value,ensure_ascii=False,indent=2)+'\n'
    assert TOKEN not in text
    (OUT/name).write_text(text,encoding='utf-8')
def identity(row):
    for key in ('full_name','repo_full_name','repository_full_name','repository','repo','name','url','repo_url','repository_url','source_url','github_url'):
        v=row.get(key)
        if isinstance(v,str):
            v=v.removeprefix('https://github.com/').removesuffix('.git').strip('/')
            if re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+',v):return v.lower()
# Bank sources were read through the connector before commercial research; stream for exact matching.
bankrepo='sisodias/siso-repo-bank'; meta=api('/repos/'+bankrepo); assert meta.get('private') is False
head=api('/repos/'+bankrepo+'/commits/main').get('sha'); assert head
paths=['bank/bank_capability_top.jsonl','bank/bank_capability.jsonl','capability-shelf/source-registry.jsonl','bank/bank_best.jsonl','bank/bank_adoption_v2.jsonl','bank/bank_liftable_ranked.jsonl','bank/bank_contractcard.jsonl']
layers={}; bank_rows={}; receipts=[]
for path in paths:
    rec={'path':path,'revision':head,'rows':0,'identities':0};h=hashlib.sha256()
    try:
        url='https://raw.githubusercontent.com/'+bankrepo+'/'+head+'/'+path
        with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'siso-restaurants-ac-public-evidence'}),timeout=90) as stream:
            for line in stream:
                h.update(line)
                if not line.strip():continue
                row=json.loads(line);rec['rows']+=1;n=identity(row)
                if n:
                    rec['identities']+=1;layers.setdefault(n,set()).add(path)
                    bank_rows.setdefault(n,{}).setdefault(path,[]).append(row)
        rec.update(status='read',sha256=h.hexdigest(),source_url=url)
    except Exception as e:rec.update(status='failed',error=type(e).__name__,http_status=getattr(e,'code',None))
    receipts.append(rec);print('BANK',path,rec.get('status'),rec['rows'],flush=True)
save('bank-receipt.json',{'observed_at':NOW,'revision':head,'layers':receipts,'new_definition':'Absent by canonical identity and requested alias from all seven specified published layers; unpublished bank not claimed.'})
rounds=[
 [('W01','A','shared inbox whatsapp self hosted'),('W02','A','employee scheduling self hosted'),('W03','A','food inventory purchase'),('W04','A','recipe costing'),('W05','A','HACCP'),('W06','A','restaurant table reservation'),('W07','A','restaurant point of sale'),('W08','A','kitchen display system'),('W09','A','food delivery dispatch'),('W10','A','delivery payout reconciliation'),('W11','A','payroll accounting self hosted'),('W12','A','loyalty points self hosted')],
 [('W01','B','topic:customer-support topic:self-hosted'),('W02','B','topic:employee-scheduling'),('W03','B','topic:inventory-management food'),('W04','B','topic:recipe-manager'),('W05','B','topic:food-safety'),('W06','B','topic:reservation-system'),('W07','B','topic:restaurant-management'),('W08','B','topic:kitchen-display-system'),('W09','B','topic:food-delivery'),('W10','B','topic:bank-statement'),('W11','B','topic:accounting'),('W12','B','topic:loyalty')],
 [('W01','C','WhatsApp Cloud API SDK'),('W02','C','iCalendar recurrence'),('W03','C','UBL invoice parser'),('W04','C','GS1 Digital Link'),('W05','C','XLSForm'),('W06','C','restaurant booking API'),('W07','C','ESC POS'),('W08','C','CloudPRNT'),('W09','C','Uber Eats API'),('W10','C','OFX parser'),('W11','C','ISO 20022 camt'),('W12','C','vCard parser')]
]
seeds=['tastyigniter/TastyIgniter','ury-erp/ury','ury-erp/pos','ury-erp/mosaic','frappe/erpnext','frappe/hrms','OCA/pos','OCA/stock-logistics-workflow','OCA/purchase-workflow','OCA/account-bank-statement-import','OCA/account-reconcile','OCA/edi','OCA/manufacture','odoo/odoo','opensourcepos/opensourcepos','NexoPOS/NexoPOS','WallaceIT/iris','SambaPOS/SambaPOS-3','grocy/grocy','TandoorRecipes/recipes','mealie-recipes/mealie','tombursch/kitchenowl','open-eats/OpenEats','foodcoops/foodsoft','FoodCoopShop/foodcoopshop','openfoodfoundation/openfoodnetwork','coopcycle/coopcycle-web','openfoodfacts/openfoodfacts-server','openfoodfacts/open-prices','alextselegidis/easyappointments','LibreBooking/librebooking','calcom/cal.com','getodk/central','getodk/collect','kobotoolbox/kpi','LimeSurvey/LimeSurvey','horilla-opensource/horilla','OCA/hr','kimai/kimai','timeoff-management/timeoff-management-application','chatwoot/chatwoot','freescout-help-desk/freescout','uvdesk/community-skeleton','zammad/zammad','knadh/listmonk','mautic/mautic','mike42/escpos-php','python-escpos/python-escpos','lsongdev/node-escpos','receipt-print-hq/escpos-tools','receiptline/receiptline','receiptline/receiptio','qzind/tray','OpenPEPPOL/peppol-bis-invoice-3','phax/ph-ubl','invoice-x/invoice2data','jseutter/ofxparse','eelkevdbos/mt940','OCA/mis-builder','awesome-selfhosted/awesome-selfhosted','openfoodfacts/taxonomy-editor']
# Seeds are hypotheses, not recommendations. Every identity is subsequently fetched and canonicalised.
seen=set();records=[];round_receipts=[]
for rnd,queries in enumerate(rounds,1):
    added=[]
    for stages,lane,q in queries:
        endpoint='/search/repositories?'+urllib.parse.urlencode({'q':q,'sort':'stars','order':'desc','per_page':8})
        result=api(endpoint);hits=[]
        for m in result.get('items',[]):
            hits.append({k:m.get(k) for k in ('full_name','description','html_url','stargazers_count','archived','topics')});n=m['full_name']
            if n.lower() not in seen:seen.add(n.lower());added.append(n)
        rec={'round':rnd,'workflow_stages':stages.split(','),'lane':lane,'query':q,'source_url':API+endpoint,'observed_at':NOW,'total_count':result.get('total_count'),'incomplete_results':result.get('incomplete_results'),'error':result.get('_error'),'hits':hits}
        records.append(rec);print('QUERY',rnd,q,'hits',len(hits),'error',rec['error'],flush=True);time.sleep(2.3)
    round_receipts.append({'round':rnd,'new_repositories':len(added),'new_names':added})
# Preserve first connector topic search, and distribute remaining collection across artifact classes.
connector=['enatega/food-delivery-multivendor','enatega/food-delivery-singlevendor','harismuneer/Restaurant-Management-System','haxxorsid/food-ordering-system','BryanTheLai/RestaurantProject','olasunkanmi-SE/restaurant','codergogoi/Online_Food_Order_App','hiramvillarreal/iotpos','SajeebChakraborty/Restaurant_Ecommerce_System_Laravel','madebyaris/poinf-of-sales','Quanghihicoder/restaurant-ordering-system','edinsoncs/Sistema-Restaurante','vanadiuz/table-reservation','longnick/small-pos-open-source','karanshukla/openresto','aashishpeepra/RestaurantReactApp','FreeOpenSourcePOS/FloCafe','munshiji/pos-billing-and-invoicing-software','uiters/restaurant-management','mungwa-agu/restaurant-app','sopnopriyo/restaurant-management-system','rezadrian01/Kasirku','ahmedali5530/restaurant-pos','hector-jewell/react-native-based-food-delivery-app','thepetronics/PetroFDS','davepartner/Ionic3-firebase-authentication-geofire-geolocation']
chosen=list(dict.fromkeys(seeds+connector));used={n.lower() for n in chosen}
for offset in range(8):
    for record in records:
        if len(record['hits'])>offset:
            n=record['hits'][offset]['full_name']
            if n.lower() not in used:chosen.append(n);used.add(n.lower())
chosen=chosen[:160]
save('discovery.json',{'observed_at':NOW,'rounds':round_receipts,'queries':records,'seed_hypotheses':seeds,'connector_discoveries':connector,'unique_discovered_including_seeds':len(seen|used),'selected_for_source_collection':chosen,'exhaustion_reached':False,'selection':'Seed hypotheses, prior connector topic discovery, then round-robin by stage/lane. Bounded pages; not an exhaustive search. Agent review occurs after collection.'})
def decode(obj,name,rev):
    if not isinstance(obj,dict) or not obj.get('content'):return {'error':obj.get('_error','unavailable') if isinstance(obj,dict) else 'unavailable'}
    raw=base64.b64decode(obj['content']);text=raw.decode('utf-8','replace')
    return {'path':obj.get('path'),'blob_sha':obj.get('sha'),'sha256':hashlib.sha256(raw).hexdigest(),'characters':len(text),'text':text,'source_url':'https://github.com/'+name+'/blob/'+str(rev)+'/'+obj.get('path','')}
def collect(pair):
    number,name=pair;out={'audit_id':'R'+str(number).zfill(3),'requested_full_name':name,'observed_at':NOW};m=api('/repos/'+name)
    if m.get('_error'):return out|{'error':m['_error']}
    if m.get('private') is not False:return out|{'error':'not_verified_public'}
    n=m['full_name'];b='/repos/'+n
    out.update({k:m.get(k) for k in ('id','full_name','html_url','description','stargazers_count','forks_count','default_branch','archived','disabled','pushed_at','size','open_issues_count','topics','license')})
    cs=api(b+'/commits?per_page=30');rev=cs[0]['sha'] if isinstance(cs,list) and cs else None
    out['revision']=rev;out['last_commit']=cs[0]['commit']['committer']['date'] if rev else None;out['commit_source']=cs[0]['html_url'] if rev else None
    out['commits_in_six_months_from_latest_30_sample']=sum(c['commit']['committer']['date']>='2026-03-13T00:00:00Z' for c in cs) if isinstance(cs,list) else None
    out['commit_sample_capped']=isinstance(cs,list) and len(cs)==30;suffix='?ref='+rev if rev else ''
    out['readme']=decode(api(b+'/readme'+suffix),n,rev);out['license_file']=decode(api(b+'/license'+suffix),n,rev)
    people=api(b+'/contributors?per_page=10');out['contributors_sample']=[{'login':p.get('login'),'contributions':p.get('contributions')} for p in people] if isinstance(people,list) else None
    issues=api(b+'/issues?state=all&sort=updated&direction=desc&per_page=10')
    out['issues_sample']=[{k:i.get(k) for k in ('number','title','state','created_at','updated_at','closed_at','comments','html_url','author_association')} for i in issues if 'pull_request' not in i][:3] if isinstance(issues,list) else None
    out['maintainer_response_sample']=[]
    for issue in out['issues_sample'] or []:
        if issue['comments']:
            comments=api(b+'/issues/'+str(issue['number'])+'/comments?per_page=30')
            if isinstance(comments,list):out['maintainer_response_sample']=[{k:c.get(k) for k in ('created_at','author_association','html_url')} for c in comments if c.get('author_association') in ('OWNER','MEMBER','COLLABORATOR')][:2]
            break
    out['bus_factor']=None;out['maintainer_response_time_population']=None
    aliases={name.lower(),n.lower()};matched=sorted({p for a in aliases for p in layers.get(a,set())});ok=all(r.get('status')=='read' for r in receipts)
    out['bank_status']='ALREADY IN THE BANK' if matched else ('NEW' if ok else 'UNKNOWN');out['bank_layers']=matched;out['bank_revision']=head
    out['bank_rows']={a:bank_rows[a] for a in aliases if a in bank_rows};out['adoption_bank_rows']=[x for a in aliases for x in bank_rows.get(a,{}).get('bank/bank_adoption_v2.jsonl',[])]
    print('RETRIEVED',out['audit_id'],n,'README',bool(out['readme'].get('text')),'LICENSE',bool(out['license_file'].get('text')),flush=True)
    return out
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:raw_rows=list(pool.map(collect,enumerate(chosen,1)))
unique={};failures=[]
for row in raw_rows:
    if not row.get('id'):failures.append(row);continue
    if row['id'] in unique:unique[row['id']].setdefault('aliases',[]).append(row['requested_full_name'])
    else:unique[row['id']]=row
rows=list(unique.values());save('repositories.jsonl',''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows));save('retrieval-failures.json',failures)
for start in range(0,len(rows),8):
    cards=[]
    for r in rows[start:start+8]:
        card={k:r.get(k) for k in ('audit_id','full_name','description','stargazers_count','archived','last_commit','revision','license','commits_in_six_months_from_latest_30_sample','bank_status','bank_layers','adoption_bank_rows','contributors_sample','issues_sample','maintainer_response_sample')}
        card['readme']={k:v for k,v in r['readme'].items() if k!='text'}|{'excerpt':r['readme'].get('text','')[:4500]}
        card['license_file']={k:v for k,v in r['license_file'].items() if k!='text'}|{'excerpt':r['license_file'].get('text','')[:900],'tail':r['license_file'].get('text','')[-350:]};cards.append(card)
    save('review-'+str(start//8+1).zfill(2)+'.jsonl',''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in cards))
save('receipt.json',{'observed_at':NOW,'workflow_revision':os.environ['GITHUB_SHA'],'requested_candidates':len(chosen),'unique_repositories_retrieved':len(rows),'readmes_retrieved':sum(bool(r['readme'].get('text')) for r in rows),'license_files_retrieved':sum(bool(r['license_file'].get('text')) for r in rows),'commit_revisions_retrieved':sum(bool(r['revision']) for r in rows),'already_in_bank':sum(r['bank_status']=='ALREADY IN THE BANK' for r in rows),'new':sum(r['bank_status']=='NEW' for r in rows),'bank_unknown':sum(r['bank_status']=='UNKNOWN' for r in rows),'failure_count':len(failures),'upstream_code_executed':False,'application_code_written':False,'review_status':'Collected, not yet examined/scored; no production admission.'})
print('COMPLETE public source collection only',len(rows),flush=True)
