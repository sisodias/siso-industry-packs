"""Research-only public source reads; no candidate code execution or repository writes.
Saves compact attributable receipts for reviewer assessment, not automatic verdicts.
"""
import base64,datetime,hashlib,json,os,pathlib,re,time,urllib.request,urllib.error
OUT=pathlib.Path('/tmp/car-rental-evidence'); OUT.mkdir(exist_ok=True)
DATE=datetime.datetime.now(datetime.timezone.utc).isoformat()
BANK='2d7d35ecbf7e1158d0a3527e1489040687ac214b'
TOKEN=os.environ['GH_TOKEN']
NAMES='''aelassas/bookcars aelassas/movinin fleetbase/fleetbase fleetbase/fleetops fleetbase/console OCA/fleet OCA/vertical-rental OCA/rental OCA/maintenance OCA/field-service OCA/contract OCA/sale-workflow OCA/account-invoicing OCA/account-payment OCA/bank-statement-import OCA/account-financial-tools odoo/odoo frappe/erpnext frappe/hrms Dolibarr/dolibarr traccar/traccar traccar/traccar-web traccar/traccar-client-android traccar/traccar-manager-android hargata/lubelog openremote/openremote thingsboard/thingsboard OwnTracks/recorder gpsd/gpsd COVESA/vehicle_signal_specification COVESA/vss-tools python-can/python-can cantools/cantools brendan-w/python-OBD pylessard/python-udsoncan adamschwartz/awesome-cars chatwoot/chatwoot freescout-help-desk/freescout zammad/zammad docusealco/docuseal documenso/documenso OpenSignLabs/OpenSign mfirst/pyHanko sumsign/pdfsign getodk/central getodk/collect enketo/enketo-express enketo/enketo-core zxing/zxing zxing-cpp/zxing heuer/pdf417gen Kononnable/mrz python-pillow/Pillow exiftool/exiftool photostructure/exiftool-vendored.js libvips/libvips libvips/pyvips invoice-ninja/invoiceninja InvoicePlane/InvoicePlane akaunting/akaunting Quba-viewer/Quba-Viewer ZUGFeRD/mustangproject itplr-kosit/validator phax/ph-ubl moov-io/iso20022 moov-io/ofx ofxparse/ofxparse awesome-selfhosted/awesome-selfhosted OCA/rest-framework OCA/server-auth OCA/server-ux OCA/queue snipe/snipe-it shelf-nu/shelf.net formbricks/formbricks getlago/lago stripe/stripe-node panva/jose jsvine/pdfplumber Kozea/WeasyPrint minio/minio-go restic/restic caddyserver/caddy gotenberg/gotenberg calcom/cal.com LibreBooking/app idurar/idurar-erp-crm NHN/tui.calendar yeqifu/carRental CyanAsterisk/FreeCar iamareebjamal/car-rental-php agriya/rentnride Daniel-Krzyczkowski/Cars-Island-On-Azure Hamed-Hasan/Online-Booking-Management codewithsadee/ridex eduamdev/carhive gerfagerfa/car_rental Shashank02051997/CarRentalUI-Android Singh-Shivani/hopOn ugurkryl41/CarRentalProject Amine-Smahi/CarRental PWB97/carrent poyrazaktas/Car-Rental-Project Ellie-Y/CarRentalSystem devmuhib/React-Car-Rental-Website ahmet-cetinkaya/ReCapProject agriya/burrow AbdullahShahid01/Rent-a-Car-Management-System faisalramdan17/car_rental_lite s1s1ty/CarRentalSystem tustoz/car_rental open-rmf/free_fleet illidanlab/Simulator suxrobGM/logistics-app microsoft/Bing-Maps-Fleet-Tracker orb-community/orb appget/appget alireza787b/mavsdk_drone_show kurator-dev/kurator cantoo-scribe/pdf-lib'''.split()
NAMES=list(dict.fromkeys(NAMES)); keys={n.lower() for n in NAMES}

def save(path,obj): (OUT/path).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def gql(query):
    req=urllib.request.Request('https://api.github.com/graphql',data=json.dumps({'query':query}).encode(),headers={'Authorization':'Bearer '+TOKEN,'Content-Type':'application/json','User-Agent':'siso-car-rental-research'})
    try:
        with urllib.request.urlopen(req,timeout=90) as response: result=json.load(response)
        if result.get('errors'): print('GRAPHQL_ERRORS',json.dumps(result['errors'])[:1000],flush=True)
        return result.get('data') or {}
    except urllib.error.HTTPError as exc:
        # Error body only; never request headers or environment values.
        print('GRAPHQL_HTTP_ERROR',exc.code,exc.read().decode()[:800],flush=True)
        return {}

matches={}; bank_receipts=[]
paths=['bank/bank_capability_top.jsonl','bank/bank_capability.jsonl','bank/bank_best.jsonl','bank/bank_adoption_v2.jsonl','bank/bank_liftable_ranked.jsonl','bank/bank_contractcard.jsonl','capability-shelf/source-registry.jsonl']
for path in paths:
    url='https://raw.githubusercontent.com/sisodias/siso-repo-bank/'+BANK+'/'+path
    digest=hashlib.sha256(); count=0; hit=0
    try:
        with urllib.request.urlopen(url,timeout=90) as response:
            for raw in response:
                digest.update(raw)
                if not raw.strip():continue
                count+=1; row=json.loads(raw)
                name=row.get('full_name') or row.get('repo') or row.get('repository')
                if isinstance(name,dict):name=name.get('full_name')
                if isinstance(name,str):
                    key=name.lower().removeprefix('https://github.com/').removesuffix('.git').rstrip('/')
                    if key in keys:
                        hit+=1; matches.setdefault(key,[]).append({'path':path,'line':count,'record':row})
        bank_receipts.append({'path':path,'rows':count,'sha256':digest.hexdigest(),'complete':True,'matches':hit,'url':url})
    except Exception as exc: bank_receipts.append({'path':path,'complete':False,'error':type(exc).__name__})
    print('BANK',path,count,hit,flush=True)
save('bank-receipts.json',{'commit':BANK,'observed_at':DATE,'files':bank_receipts})
save('bank-matches.json',matches)
complete=all(x['complete'] for x in bank_receipts)

licpaths=['LICENSE','LICENSE.md','LICENSE.txt','LICENCE','COPYING','COPYING.LESSER','license.txt','license.md','LICENSE-MIT']
terms=['rental','booking','reservation','availability','fleet','vehicle','driver','VIN','odometer','fuel','damage','inspection','maintenance','invoice','accounting','payment','deposit','signature','PDF417','AAMVA','MRZ','OBD','CAN','J1939','Teltonika','GT06','OpenTravel','ACRISS','OpenRosa','PAdES','OFX','camt','UBL','Docker','PostgreSQL','MySQL','MariaDB','MongoDB','Redis','SQLite','Firebase','Supabase','Azure','AWS','SaaS','student','tutorial','demo','deprecated','archived','unmaintained','enterprise']
records=[]; failures=[]
for offset in range(0,len(NAMES),8):
    batch=NAMES[offset:offset+8]
    fields=[]
    for i,name in enumerate(batch):
        owner,repo=name.split('/')
        fields.append('r'+str(i)+':repository(owner:'+json.dumps(owner)+',name:'+json.dumps(repo)+'){nameWithOwner url description stargazerCount forkCount isArchived licenseInfo{spdxId} repositoryTopics(first:15){nodes{topic{name}}} defaultBranchRef{name target{...on Commit{oid committedDate history(first:10){nodes{oid committedDate author{user{login}}}}}}} issues(last:5,orderBy:{field:UPDATED_AT,direction:ASC}){nodes{number createdAt closedAt updatedAt comments(first:10){nodes{createdAt authorAssociation}}}}}')
    meta=gql('{rateLimit{remaining resetAt} '+' '.join(fields)+'}')
    if not meta: failures.extend(batch); break
    print('BATCH',offset,'rate',meta.get('rateLimit'),flush=True)
    fields=[]
    for i,name in enumerate(batch):
        item=meta.get('r'+str(i))
        if not item or not item.get('defaultBranchRef'): failures.append(name); continue
        sha=item['defaultBranchRef']['target']['oid']; owner,repo=item['nameWithOwner'].split('/')
        objs=['readme:object(expression:'+json.dumps(sha+':README.md')+'){...on Blob{oid text byteSize}}','root:object(expression:'+json.dumps(sha+':')+'){...on Tree{entries{name type}}}','manifest:object(expression:'+json.dumps(sha+':package.json')+'){...on Blob{oid text}}']
        objs += ['l'+str(j)+':object(expression:'+json.dumps(sha+':'+path)+'){...on Blob{oid text byteSize}}' for j,path in enumerate(licpaths)]
        fields.append('r'+str(i)+':repository(owner:'+json.dumps(owner)+',name:'+json.dumps(repo)+'){'+ ' '.join(objs)+'}')
    data=gql('{'+' '.join(fields)+'}') if fields else {}
    for i,name in enumerate(batch):
        item=meta.get('r'+str(i)); files=data.get('r'+str(i)) or {}
        if not item or not item.get('defaultBranchRef'):continue
        sha=item['defaultBranchRef']['target']['oid']; read=files.get('readme') or {}; text=read.get('text') or ''
        clean=re.sub(r'<!--.*?-->',' ',text,flags=re.S)
        clean=re.sub(r'!\[[^\]]*\]\([^)]*\)',' ',clean)
        clean=re.sub(r'\[([^\]]+)\]\([^)]*\)',r'\1',clean)
        lines=[x.strip(' #*-|>') for x in clean.splitlines() if len(x)>35 and not re.search(r'(?i)password|secret|token|badge|https?://|copyright|<img|<a ',x)]
        excerpt=' '.join((' '.join(lines)).split()[:12])
        licenses=[]
        for j,path in enumerate(licpaths):
            obj=files.get('l'+str(j))
            if not obj:continue
            lt=obj.get('text') or ''
            markers=[t for t in ['MIT License','Apache License','GNU AFFERO','GNU GENERAL','GNU LESSER','Business Source','Server Side Public','Elastic License','Commons Clause','Sustainable Use','Open Software License','Mozilla Public'] if t.lower() in lt.lower()]
            licenses.append({'path':path,'sha':obj['oid'],'chars_read':len(lt),'markers':markers,'excerpt':' '.join(lt.split()[:8]) if not licenses else None,'url':item['url']+'/blob/'+sha+'/'+path})
        manifest={}
        try:
            p=json.loads((files.get('manifest') or {}).get('text') or '{}'); manifest={k:p[k] for k in ['dependencies','devDependencies','license'] if k in p}
        except json.JSONDecodeError: pass
        key=item['nameWithOwner'].lower(); bm=matches.get(key,[])
        record={'full_name':item['nameWithOwner'],'url':item['url'],'observed_at':DATE,'stars':item['stargazerCount'],'forks':item['forkCount'],'archived':item['isArchived'],'last_commit':{'sha':sha,'date':item['defaultBranchRef']['target']['committedDate']},'commit_sample':item['defaultBranchRef']['target']['history']['nodes'],'issue_sample':item['issues']['nodes'],'github_spdx':(item.get('licenseInfo') or {}).get('spdxId'),'licenses':licenses,'readme':{'sha':read.get('oid'),'chars_read':len(text),'excerpt':excerpt,'term_hits':[t for t in terms if t.lower() in text.lower()],'url':item['url']+'/blob/'+sha+'/README.md'},'root_names':[e['name'] for e in (files.get('root') or {}).get('entries',[])],'dependencies':manifest,'bank_status':'ALREADY IN THE BANK' if bm else ('NEW' if complete else 'UNRESOLVED'),'bank_sources':[{'path':m['path'],'line':m['line']} for m in bm],'adoption':[m['record'] for m in bm if m['path'].endswith('bank_adoption_v2.jsonl')],'assessment_status':'UNREVIEWED; source collection is not an examination verdict'}
        records.append(record)
    # Preserve partial results even if later batches fail.
    save('repository-receipts.json',records)
    time.sleep(1)
# Compact index readable through connector; full receipts are the source of each field.
compact=[]
for r in records:
    compact.append({'repo':r['full_name'],'stars':r['stars'],'date':r['last_commit']['date'],'sha':r['last_commit']['sha'],'spdx':r['github_spdx'],'license_files':[{k:l[k] for k in ['path','chars_read','markers']} for l in r['licenses']],'archived':r['archived'],'bank':r['bank_status'],'readme_words':r['readme']['excerpt'],'readme_chars':r['readme']['chars_read'],'hits':r['readme']['term_hits'],'adoption':r['adoption']})
(OUT/'review-index.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n' for x in compact))
for i in range(0,len(compact),10):
    (OUT/f'review-index-{i//10+1:02d}.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n' for x in compact[i:i+10]))
save('collection-summary.json',{'observed_at':DATE,'leads':len(NAMES),'source_receipts':len(records),'readme_read':sum(r['readme']['chars_read']>0 for r in records),'license_files_read':sum(bool(r['licenses']) for r in records),'bank_scan_complete':complete,'failures':failures,'repos_examined':0,'assessment_status':'UNREVIEWED'})
print('COLLECTION_SUMMARY',json.dumps({'leads':len(NAMES),'receipts':len(records),'failures':failures,'bank_complete':complete}),flush=True)
