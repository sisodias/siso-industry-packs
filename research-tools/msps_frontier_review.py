"""Additional public evidence, no execution of upstream software."""
import ast, concurrent.futures as cf, datetime as dt, hashlib, io, json, os, pathlib, re, time, urllib.parse, urllib.request, zipfile
R=pathlib.Path('evidence/repo-sweep'); R.mkdir(parents=True,exist_ok=True)
HEAD={'User-Agent':'SISO-MSP-public-research','Authorization':'Bearer '+os.environ['GH_TOKEN'],'Accept':'application/vnd.github+json'}
BASE='https://api.github.com'
def raw(url,auth=False):
    with urllib.request.urlopen(urllib.request.Request(url,headers=HEAD if auth else {'User-Agent':'SISO-MSP-public-research'}),timeout=90) as r:return r.read()
body=raw(BASE+'/repos/sisodias/siso-industry-packs/actions/artifacts/10320308316/zip',True)
assert hashlib.sha256(body).hexdigest()=='6b53b8013c5d3e7862776284b15158ae3ceb50130fe899dc34c8985722749b90'
with zipfile.ZipFile(io.BytesIO(body)) as z:
    for item in z.infolist():
        assert not item.filename.startswith('/') and '..' not in pathlib.PurePosixPath(item.filename).parts
    z.extractall(R)
source=raw('https://raw.githubusercontent.com/sisodias/siso-industry-packs/1f77eea1da30703d68820c7430455a176d82f4b2/research-tools/msps_public_sweep.py').decode()
tree=ast.parse(source)
ns={};exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,(ast.Import,ast.ImportFrom,ast.FunctionDef))],type_ignores=[]),'own-research-functions','exec'),ns)
ns.update(R=R,HEAD=HEAD,BASE=BASE,now=lambda:dt.datetime.now(dt.timezone.utc).isoformat(),metadata_cache={},metadata_sources={},lineage={},DEEP={'cyberdrain/cipp','cyberdrain/craft','itflow-org/itflow','glpi-project/glpi','nine-minds/alga-psa'})
get,save,dossier=ns['get'],ns['save'],ns['dossier']
previous=json.loads((R/'selection-input.json').read_text()); seen=set(x.lower() for x in previous['all_discovered_names'])
seen.update(x.lower() for x in previous['seed_hypotheses'])
# The seed ledger includes hypotheses; errors remain errors, not verified repositories.
index=json.loads((R/'dossier-index.json').read_text());existing={x.get('full_name','').lower() for x in index if x.get('full_name')}
queries={
3:[('S01','A','"professional services automation" self-hosted'),('S02','B','topic:it-documentation'),('S03','B','topic:gdap'),('S04','C','Exchange EWS email library'),('S05','C','CalDAV server'),('S06','C','topic:wsman'),('S07','B','topic:patch-management'),('S08','C','Veeam PowerShell backup'),('S09','C','PartnerCenter SDK'),('S10','C','Autotask API PowerShell'),('S11','C','FOCUS billing specification'),('S12','A','"IT Glue" "open source"')],
4:[('S02','C','GLPI inventory API bridge'),('S03','A','CIPP Craft'),('S04','C','email message MIME parser'),('S06','C','PSRP Windows remote library'),('S08','B','topic:urbackup'),('S09','A','Microsoft365DSC export tenant'),('S10','B','topic:halopsa'),('S11','C','QuickBooks webhooks SDK')],
5:[('S02','A','"MSP" "documentation" "self-hosted"'),('S04','A','"helpdesk" "IMAP" "tenant"'),('S06','B','topic:psrp'),('S08','C','"backup" "restore" "MSP"'),('S09','C','"GDAP" "Microsoft Graph"'),('S10','C','"HaloPSA" "billing" "API"')]}
log=json.loads((R/'search-log.json').read_text());selected=['CyberDrain/CIPP','CyberDrain/Craft','KelvinTegelaar/CIPP','KelvinTegelaar/CIPP-API','itflow-org/itflow-powershell','ansible-community/ara','ansible-semaphore/semaphore','GoSecure/pyrdp','microsoft/Partner-Center-PowerShell','MicrosoftDocs/partner-center-sdk','Focus-Projects/FOCUS_Specification','glpi-project/docker-images','glpi-project/doc-install','glpi-project/doc-api','mspapi/ConnectWiseControlAPI','goodwithtech/dockle']
novelty=[]
for roundno,qs in queries.items():
    rn=[]
    for stage,lane,q in qs:
        q+=' fork:false';url=BASE+'/search/repositories?'+urllib.parse.urlencode({'q':q,'sort':'stars','order':'desc','per_page':20});obj=get(url);items=obj.get('items',[]);new=[]
        for it in items:
            k=it['full_name'].lower();ns['metadata_cache'][k]=it;ns['metadata_sources'][k]=url
            ns['lineage'].setdefault(k,[]).append({'route':'search','stage':stage,'round':roundno,'lane':lane,'query':q})
            if k not in seen:new.append(it['full_name']);seen.add(k)
        for it in items[:2]:
            if it['full_name'].lower() not in existing and it['full_name'].lower() not in {s.lower() for s in selected}:selected.append(it['full_name'])
        receipt={'round':roundno,'stage':stage,'lane':lane,'artifact_class':'protocol/bridge/maintainer extension','q':q,'query_url':url,'observed_at':ns['now'](),'total_count':obj.get('total_count'),'returned':len(items),'new_unique_names':new,'error':obj.get('_error')}
        log.append(receipt);save(pathlib.Path('search')/f'{len(log):03d}.json',{'receipt':receipt,'response':obj});rn+=new
        print('QUERY',roundno,q,'new',len(new),flush=True);time.sleep(2.1)
    novelty.append({'round':roundno,'new_unique_names':len(rn),'names':rn})
# Explicit source chasing: links in the relevant awesome-list and selected manifests.
frontier=[]
for name in ['capetron/awesome-msp-tools','awesome-foss/awesome-sysadmin','awesome-selfhosted/awesome-selfhosted','itflow-org/itflow','glpi-project/glpi','amidaware/tacticalrmm','ansible/ansible','SigmaHQ/pySigma','Nine-Minds/alga-psa']:
    p=R/'dossiers'/(name.replace('/','__')+'.json')
    if not p.exists():continue
    d=json.loads(p.read_text())
    for f in d.get('files',[]):
        if 'readme' not in f['path'].lower() and f['path'] not in ('composer.json','package.json','go.mod','pyproject.toml'):continue
        for line in f['text'].splitlines():
            if name.startswith('awesome-') and not re.search(r'(?i)(backup|ticket|helpdesk|inventory|remote|monitor|MDM|SNMP|ITSM|CMDB|password|configuration)',line):continue
            for owner,repo in re.findall(r'https://github.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)',line):
                target=owner+'/'+repo.rstrip('.');k=target.lower()
                if owner.lower() in ('sponsors','orgs','features','topics','marketplace','users','login','settings'):continue
                frontier.append({'source_repository':name,'source_file':f['path'],'source_url':f['url'],'target':target,'new_to_search_ledger':k not in seen})
                seen.add(k)
                if name in ('itflow-org/itflow','glpi-project/glpi','amidaware/tacticalrmm','SigmaHQ/pySigma','Nine-Minds/alga-psa') and k not in existing and k not in {s.lower() for s in selected}:selected.append(target)
save('source-chase.json',frontier);save('search-log.json',log);save('extension-rounds.json',novelty)
selected=list(dict.fromkeys(s for s in selected if s.lower() not in existing));save('extension-selection.json',selected)
with cf.ThreadPoolExecutor(max_workers=4) as pool:
    for out in pool.map(dossier,selected):
        name=out.get('full_name',out['requested_name']);save(pathlib.Path('dossiers')/(name.replace('/','__')+'.json'),out)
        index.append({k:out.get(k) for k in ('requested_name','full_name','commit_sha','last_commit_at','observed_at','error')});print('DOSSIER',name,'ERROR' if out.get('error') else len(out['files']),flush=True)
save('dossier-index.json',index)
# Retrieve narrowly-scoped first-party deployment/licensing files, without running them.
extras={'activepieces/activepieces':['packages/ee/LICENSE'],'CyberDrain/CIPP':['LICENSE','LICENSE.md','build/docker-compose.yml','build/docker-compose.yaml','build/Dockerfile'],'Nine-Minds/alga-psa':['docs/deployment-guide.md','docs/overview.md'],'itflow-org/itflow':['SECURITY.md'],'glpi-project/glpi':['SECURITY.md']}
for name,paths in extras.items():
    for p in paths:
        url=BASE+'/repos/'+name+'/contents/'+p;obj=get(url)
        if isinstance(obj,dict) and obj.get('download_url'):
            b=get(obj['download_url'],True)
            if isinstance(b,bytes):save(pathlib.Path('extra-files')/(name.replace('/','__')+'__'+p.replace('/','__')+'.json'),{'repository':name,'path':p,'url':obj['html_url'],'blob_sha':obj['sha'],'sha256':hashlib.sha256(b).hexdigest(),'text':b.decode('utf8',errors='replace'),'observed_at':ns['now']()})
for p in ['registry/industries.jsonl','registry/bank-submissions.jsonl','registry/corrections.jsonl','packs/it_services_msps/README.md']:
    obj=get(BASE+'/repos/sisodias/siso-industry-packs/contents/'+p+'?ref=main')
    if obj.get('download_url'):
        b=get(obj['download_url'],True)
        if isinstance(b,bytes):save(pathlib.Path('publication-inputs')/(p.replace('/','__')+'.json'),{'path':p,'blob_sha':obj['sha'],'text':b.decode(),'url':obj['html_url']})
save('manifest-extended.json',{'observed_at':ns['now'](),'queries':len(log),'rounds':5,'rounds_3_to_5':novelty,'dossiers_total':len(index),'unique_retrieved':len({x['full_name'].lower() for x in index if x.get('full_name') and not x.get('error')}),'discovered_names':len(seen),'saturation':'not asserted; inspect novelty and source-chase ledger','method':'Public GitHub API responses collected by read-only Actions; transported and read through GitHub connector artifact API.'})
