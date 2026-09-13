"""Research-only collector. Never imports, installs, builds or executes candidate code.
GET public GitHub sources, stream SISO bank membership, publish receipts on the
isolated research branch only. No deployment, no schedule, no client data.
"""
import base64, concurrent.futures, datetime, hashlib, json, os, re, time
import urllib.request, urllib.error, urllib.parse

REPO = 'sisodias/siso-industry-packs'
BRANCH = 'research/car-rental-20260913'
OUT = 'packs/car_rental/evidence/'
DATE = datetime.datetime.now(datetime.timezone.utc).isoformat()
TOKEN = os.environ['GH_TOKEN']
HEADERS = {'Authorization': 'Bearer ' + TOKEN, 'Accept': 'application/vnd.github+json', 'User-Agent': 'siso-car-rental-research', 'X-GitHub-Api-Version': '2022-11-28'}

def api(path, data=None, method='GET'):
    url = 'https://api.github.com/' + path.lstrip('/')
    raw = None if data is None else json.dumps(data).encode()
    for attempt in range(5):
        try:
            req = urllib.request.Request(url, data=raw, headers=HEADERS, method=method)
            with urllib.request.urlopen(req, timeout=45) as response:
                return json.load(response)
        except urllib.error.HTTPError as exc:
            if exc.code == 404: return None
            if exc.code in (403, 429, 500, 502, 503, 504) and attempt < 4:
                time.sleep(min(65, max(5, int(exc.headers.get('Retry-After', '0')))) + attempt * 5)
            else: raise
    return None

def raw_lines(repo, ref, path):
    url = 'https://raw.githubusercontent.com/' + repo + '/' + ref + '/' + path
    req = urllib.request.Request(url, headers={'User-Agent': 'siso-car-rental-research'})
    with urllib.request.urlopen(req, timeout=90) as response:
        for line in response:
            yield line.decode('utf-8')

# Stages 1-3 were completed before this collector was admitted.
queries = [
(1,'W01,W10','A','shared inbox self hosted'),
(1,'W02','A','car rental'),
(1,'W03','A','driver license parser'),
(1,'W04,W06','A','vehicle inspection'),
(1,'W05','A','GPS tracking server'),
(1,'W07','A','toll invoice'),
(1,'W08','A','vehicle maintenance'),
(1,'W09','A','accounting invoice self hosted'),
(1,'W03','A','electronic signature self hosted'),
(1,'W09','A','rental Odoo'),
(2,'W01,W10','B','topic:customer-support'),
(2,'W02','B','topic:car-rental'),
(2,'W03','B','topic:pdf417'),
(2,'W04,W06','B','topic:vehicle-inspection'),
(2,'W05','B','topic:telematics'),
(2,'W07','B','topic:open-banking'),
(2,'W08','B','topic:cmms'),
(2,'W09','B','topic:einvoice'),
(2,'W03','B','topic:digital-signature'),
(2,'W08','B','topic:fleet-management'),
(3,'W01,W10','C','WhatsApp webhook'),
(3,'W02','C','ACRISS'),
(3,'W02','C','VehAvailRateRQ'),
(3,'W02','C','OpenTravel'),
(3,'W02','C','RFC5545'),
(3,'W03','C','AAMVA'),
(3,'W03','C','PAdES'),
(3,'W04,W06','C','OpenRosa'),
(3,'W04,W06','C','EXIF orientation'),
(3,'W05','C','Teltonika codec'),
(3,'W05','C','GT06'),
(3,'W07','C','camt.053'),
(3,'W07','C','OFX parser'),
(3,'W08','C','OBD-II'),
(3,'W08','C','J1939'),
(3,'W09','C','UBL invoice'),
(3,'W09','C','ISO20022'),
(3,'W10','C','vCard CardDAV'),
(4,'W02','graph','user:aelassas'),
(4,'W02,W08','graph','org:OCA rental'),
(4,'W05','graph','org:traccar'),
(4,'W08','graph','awesome automotive'),
(4,'W02','gap','Rentalcars supplier API'),
(4,'W02','gap','DiscoverCars supplier API'),
(4,'W07','gap','rental toll reconciliation'),
(4,'W03','gap','rental insurance eligibility'),
]
# These are leads, not admitted or examined repositories; HTTP/source reads decide.
seeds = '''aelassas/bookcars aelassas/movinin fleetbase/fleetbase fleetbase/fleetops fleetbase/console OCA/fleet OCA/vertical-rental OCA/rental OCA/maintenance OCA/field-service OCA/contract OCA/sale-workflow OCA/account-invoicing OCA/account-payment OCA/bank-statement-import OCA/account-financial-tools odoo/odoo frappe/erpnext frappe/hrms Dolibarr/dolibarr traccar/traccar traccar/traccar-web traccar/traccar-client-android traccar/traccar-manager-android hargata/lubelog openremote/openremote thingsboard/thingsboard OwnTracks/recorder gpsd/gpsd COVESA/vehicle_signal_specification COVESA/vss-tools python-can/python-can cantools/cantools brendan-w/python-OBD pylessard/python-udsoncan adamschwartz/awesome-cars chatwoot/chatwoot freescout-help-desk/freescout zammad/zammad docusealco/docuseal documenso/documenso OpenSignLabs/OpenSign mfirst/pyHanko sumsign/pdfsign getodk/central getodk/collect enketo/enketo-express enketo/enketo-core jieter/Leaflet.encoded zxing/zxing zxing-cpp/zxing heuer/pdf417gen Kononnable/mrz nodeca/pako python-pillow/Pillow exiftool/exiftool photostructure/exiftool-vendored.js libvips/libvips libvips/pyvips invoice-ninja/invoiceninja InvoicePlane/InvoicePlane akaunting/akaunting Quba-viewer/Quba-Viewer ZUGFeRD/mustangproject itplr-kosit/validator phax/ph-ubl moov-io/iso20022 moov-io/ofx ofxparse/ofxparse Activiti/Activiti awesome-selfhosted/awesome-selfhosted OCA/rest-framework OCA/server-auth OCA/server-ux OCA/queue snipe/snipe-it shelf-nu/shelf.net formbricks/formbricks getlago/lago stripe/stripe-node pennersr/django-allauth panva/jose jsvine/pdfplumber Kozea/WeasyPrint minio/minio-go restic/restic caddyserver/caddy gotenberg/gotenberg calcom/cal.com LibreBooking/app idurar/idurar-erp-crm NHN/tui.calendar yeqifu/carRental CyanAsterisk/FreeCar iamareebjamal/car-rental-php agriya/rentnride Daniel-Krzyczkowski/Cars-Island-On-Azure'''.split()
pool = {x.lower(): {'requested':x,'discovery':['seed; unverified until source read']} for x in seeds}
search_log = []
for round_no, stages, lane, query in queries:
    try:
        result = api('search/repositories?' + urllib.parse.urlencode({'q':query,'sort':'stars','order':'desc','per_page':5})) or {}
        names=[]; new=[]
        for item in result.get('items', []):
            name=item['full_name']; key=name.lower(); names.append(name)
            if key not in pool: pool[key]={'requested':name,'discovery':[]}; new.append(name)
            pool[key]['discovery'].append({'round':round_no,'stages':stages,'lane':lane,'query':query})
        search_log.append({'round':round_no,'stages':stages,'lane':lane,'query':query,'sort':'stars desc','page':1,'page_size':5,'total_count':result.get('total_count'),'returned':names,'new':new,'observed_at':DATE,'source_url':'https://github.com/search?'+urllib.parse.urlencode({'q':query,'type':'repositories','s':'stars','o':'desc'})})
        print('SEARCH',round_no,lane,query,'returned',len(names),'new',len(new),flush=True)
    except Exception as exc:
        search_log.append({'round':round_no,'stages':stages,'lane':lane,'query':query,'error':type(exc).__name__})
    time.sleep(2.2)

bank_paths=['bank/bank_capability_top.jsonl','bank/bank_capability.jsonl','bank/bank_best.jsonl','bank/bank_adoption_v2.jsonl','bank/bank_liftable_ranked.jsonl','bank/bank_contractcard.jsonl','capability-shelf/source-registry.jsonl']
bank_ref = api('repos/sisodias/siso-repo-bank/commits?per_page=1')[0]['sha']
bank_receipts=[]; bank_matches={}; adoption={}; capabilities=[]
for path in bank_paths:
    digest=hashlib.sha256(); rows=0; matched=0; top_tags=set()
    try:
        for text in raw_lines('sisodias/siso-repo-bank',bank_ref,path):
            digest.update(text.encode());
            if not text.strip(): continue
            rows+=1
            try: row=json.loads(text)
            except json.JSONDecodeError: continue
            name=row.get('full_name') or row.get('repo') or row.get('repository')
            if isinstance(name,dict): name=name.get('full_name')
            if path.endswith('bank_capability.jsonl'): capabilities.append(row)
            if path.endswith('bank_capability_top.jsonl'): top_tags.add(row.get('capability'))
            if isinstance(name,str):
                key=name.lower().removeprefix('https://github.com/').removesuffix('.git').rstrip('/')
                if key in pool:
                    matched+=1
                    bank_matches.setdefault(key,[]).append({'path':path,'row':rows,'record':row})
                    if path.endswith('bank_adoption_v2.jsonl'): adoption[key]=row
        bank_receipts.append({'path':path,'ref':bank_ref,'rows_streamed':rows,'sha256':digest.hexdigest(),'candidate_matches':matched,'distinct_top_capabilities':len(top_tags) if top_tags else None,'complete':True,'url':'https://github.com/sisodias/siso-repo-bank/blob/'+bank_ref+'/'+path})
    except Exception as exc: bank_receipts.append({'path':path,'complete':False,'error':type(exc).__name__})

terms=['rental','booking','reservation','availability','fleet','vehicle','driver','license','licence','VIN','odometer','mileage','fuel','damage','inspection','maintenance','invoice','accounting','payment','deposit','refund','signature','PDF417','AAMVA','MRZ','OBD','CAN','J1939','Teltonika','GT06','OpenTravel','ACRISS','OpenRosa','PAdES','OFX','camt','UBL','Docker','PostgreSQL','MySQL','MariaDB','MongoDB','Redis','SQLite','Firebase','Supabase','Azure','AWS','SaaS','student','tutorial','demo','deprecated','archived','unmaintained','enterprise','AGPL','SSPL','BSL','MIT','GPL']

def decode_content(obj):
    if not obj: return ''
    if obj.get('encoding')=='base64': return base64.b64decode(obj.get('content','')).decode('utf-8',errors='replace')
    return obj.get('content','')

def examine(lead):
    name=lead['requested']; base='repos/'+name
    try:
        meta=api(base)
        if not meta: return {'requested':name,'exists':False,'error':'HTTP404','observed_at':DATE}
        canonical=meta['full_name']; base='repos/'+canonical
        commits=api(base+'/commits?per_page=1') or []; commit=commits[0] if commits else None
        ref=commit['sha'] if commit else meta['default_branch']
        read_obj=api(base+'/readme?ref='+ref); readme=decode_content(read_obj)
        lic_obj=api(base+'/license?ref='+ref); lic=decode_content(lic_obj)
        root=api(base+'/contents?ref='+ref) or []
        root_names=[x.get('name') for x in root] if isinstance(root,list) else []
        license_files=[x for x in root_names if re.search(r'(?i)licen[cs]e|copying|notice',x or '')]
        if not lic:
            for filename in license_files[:3]:
                x=api(base+'/contents/'+urllib.parse.quote(filename)+'?ref='+ref)
                if isinstance(x,dict) and x.get('type')=='file':
                    lic_obj=x; lic=decode_content(x)
                    if lic: break
        dependencies={}
        for filename in ['package.json','composer.json','pyproject.toml','requirements.txt','go.mod','Cargo.toml','pom.xml']:
            if filename not in root_names: continue
            obj=api(base+'/contents/'+filename+'?ref='+ref); text=decode_content(obj)
            if filename in ['package.json','composer.json']:
                try:
                    parsed=json.loads(text); dependencies[filename]={k:parsed.get(k) for k in ['dependencies','devDependencies','require','license'] if parsed.get(k)}
                except json.JSONDecodeError: dependencies[filename]={'sha256':hashlib.sha256(text.encode()).hexdigest()}
            else: dependencies[filename]={'sha256':hashlib.sha256(text.encode()).hexdigest(),'lines':len(text.splitlines())}
        # Public receipt contains small excerpts, never entire upstream READMEs.
        cleaned=re.sub(r'<!--.*?-->',' ',readme,flags=re.S)
        cleaned=re.sub(r'!\[[^\]]*\]\([^)]*\)',' ',cleaned)
        cleaned=re.sub(r'\[([^\]]+)\]\([^)]*\)',r'\1',cleaned)
        good_lines=[line.strip(' #*-|>') for line in cleaned.splitlines() if len(line)>35 and not re.search(r'(?i)password|secret|token|badge|https?://|copyright',line)]
        excerpt=' '.join((' '.join(good_lines)).split()[:12])
        license_excerpt=' '.join(lic.split()[:8])
        license_markers=[t for t in ['MIT License','Apache License','GNU AFFERO','GNU GENERAL','GNU LESSER','Business Source','Server Side Public','Elastic License','Commons Clause','Sustainable Use','Open Software License','Mozilla Public'] if t.lower() in lic.lower()]
        key=canonical.lower(); matches=bank_matches.get(key,[])+([] if key==name.lower() else bank_matches.get(name.lower(),[]))
        source='https://github.com/'+canonical
        return {'full_name':canonical,'requested':name,'exists':True,'url':source,'observed_at':DATE,'stars':meta['stargazers_count'],'forks':meta['forks_count'],'archived':meta['archived'],'default_branch':meta['default_branch'],'language':meta.get('language'),'topics':meta.get('topics',[]),'created_at':meta['created_at'],'pushed_at':meta['pushed_at'],'open_issues':meta['open_issues_count'],'last_commit':{'sha':ref,'date':commit['commit']['committer']['date'],'url':commit['html_url']} if commit else None,'readme':{'path':read_obj.get('path') if read_obj else None,'sha':read_obj.get('sha') if read_obj else None,'chars_read':len(readme),'excerpt':excerpt,'term_hits':[t for t in terms if re.search(re.escape(t),readme,re.I)],'url':read_obj.get('html_url') if read_obj else None},'license':{'github_spdx':(meta.get('license') or {}).get('spdx_id'),'path':lic_obj.get('path') if lic_obj else None,'sha':lic_obj.get('sha') if lic_obj else None,'chars_read':len(lic),'excerpt':license_excerpt,'markers':license_markers,'url':lic_obj.get('html_url') if lic_obj else None,'root_license_files':license_files,'scope_audit':'root only; chosen subdirectories require separate audit'},'root_names':root_names,'dependencies':dependencies,'bank_status':'ALREADY IN THE BANK' if matches else ('NEW' if all(x.get('complete') for x in bank_receipts) else 'UNRESOLVED'),'bank_matches':matches,'adoption':adoption.get(key),'discovery':lead['discovery'],'assessment_status':'UNREVIEWED: collection is not human examination or adoption','sources':{'metadata':'https://api.github.com/'+base,'commits':'https://api.github.com/'+base+'/commits?per_page=1','contents':'https://api.github.com/'+base+'/contents?ref='+ref}}
    except Exception as exc: return {'requested':name,'exists':None,'error':type(exc).__name__,'observed_at':DATE}

leads=list(pool.values())
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    records=list(executor.map(examine,leads))
records.sort(key=lambda x:(x.get('full_name') or x['requested']).lower())
files={
 OUT+'search-rounds.json':json.dumps(search_log,ensure_ascii=False,indent=2)+'\n',
 OUT+'bank-receipts.json':json.dumps({'observed_at':DATE,'bank_commit':bank_ref,'files':bank_receipts,'capabilities':capabilities},ensure_ascii=False,indent=2)+'\n',
 OUT+'collection-summary.json':json.dumps({'observed_at':DATE,'leads':len(leads),'repositories_read':sum(x.get('exists') is True for x in records),'repositories_manually_examined':0,'collection_is_not_examination':True,'readme_success':sum(bool(x.get('readme',{}).get('chars_read')) for x in records),'license_file_success':sum(bool(x.get('license',{}).get('chars_read')) for x in records),'failed':[x for x in records if x.get('exists') is not True],'bank_scan_complete':all(x.get('complete') for x in bank_receipts)},indent=2)+'\n'}
for i in range(0,len(records),10):
    files[OUT+f'repositories-{i//10+1:02d}.jsonl']=''.join(json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n' for x in records[i:i+10])
# One atomic commit on the isolated research branch. Never updates main.
branch=api('repos/'+REPO+'/git/ref/heads/'+BRANCH)
parent=branch['object']['sha']; parent_obj=api('repos/'+REPO+'/git/commits/'+parent)
tree=api('repos/'+REPO+'/git/trees',{'base_tree':parent_obj['tree']['sha'],'tree':[{'path':path,'mode':'100644','type':'blob','content':text} for path,text in files.items()]},'POST')
commit=api('repos/'+REPO+'/git/commits',{'message':'research(car_rental): collect public-source receipts; assessments explicitly unreviewed','tree':tree['sha'],'parents':[parent]},'POST')
api('repos/'+REPO+'/git/refs/heads/'+BRANCH,{'sha':commit['sha'],'force':False},'PATCH')
print('RECEIPTS_COMMIT',commit['sha'])
print('LEADS',len(leads),'REPOSITORIES_READ',sum(x.get('exists') is True for x in records),'MANUALLY_EXAMINED',0)
