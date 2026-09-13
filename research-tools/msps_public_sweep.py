"""Public-source research collector, not application code. Never executes upstream code."""
import concurrent.futures as cf, datetime as dt, hashlib, json, os, pathlib, re, time, urllib.parse, urllib.request, urllib.error
R=pathlib.Path('evidence/repo-sweep'); R.mkdir(parents=True,exist_ok=True)
BASE='https://api.github.com'
HEAD={'User-Agent':'SISO-MSP-evidence-research','Accept':'application/vnd.github+json','Authorization':'Bearer '+os.environ['GH_TOKEN'],'X-GitHub-Api-Version':'2022-11-28'}
now=lambda: dt.datetime.now(dt.timezone.utc).isoformat()
def get(url,raw=False):
    head=HEAD if url.startswith(BASE+'/') else {'User-Agent':'SISO-MSP-evidence-research'}
    for attempt in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url,headers=head),timeout=30) as res:
                body=res.read(); return body if raw else json.loads(body)
        except urllib.error.HTTPError as e:
            if e.code in (403,429) and attempt<2:
                time.sleep(min(90,max(3,int(e.headers.get('Retry-After','5')))));continue
            return {'_error':str(e),'url':url,'observed_at':now()}
        except Exception as e:
            if attempt<2:time.sleep(1);continue
            return {'_error':str(e),'url':url,'observed_at':now()}
def save(path,data):
    p=R/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
seedgroups={
'S01':['itflow-org/itflow','ninjamsp/atlassian-asap','microsoft/Partner-Center-DotNet','frappe/crm','frappe/erpnext','Dolibarr/dolibarr','invoiceninja/invoiceninja','InvoicePlane/InvoicePlane','solidtime-io/solidtime','kimai/kimai','ErpNet/ErpNet.FP'],
'S02':['glpi-project/glpi','glpi-project/glpi-agent','glpi-project/glpi-inventory-plugin','netbox-community/netbox','netbox-community/netbox-docker','snipe/snipe-it','Combodo/iTop','RackTables/racktables','nautobot/nautobot','OCSInventory-NG/OCSInventory-Server','OCSInventory-NG/UnixAgent','netdisco/netdisco','phpipam/phpipam','Orange-OpenSource/noria-ontology'],
'S03':['BookStackApp/BookStack','Requarks/wiki','passbolt/passbolt_api','dani-garcia/vaultwarden','Ylianst/MeshCentral','rustdesk/rustdesk-server','rustdesk/rustdesk','guacamole/guacamole-server','apache/guacamole-server','apache/guacamole-client','dwservice/agent','openziti/ziti','juanfont/headscale'],
'S04':['chatwoot/chatwoot','zammad/zammad','freescout-helpdesk/freescout','osTicket/osTicket','RotherOSS/otobo','django-helpdesk/django-helpdesk','erxes/erxes','postalserver/postal','snikket-im/snikket-server','closeio/sync-engine','microsoftgraph/msgraph-sdk-powershell','microsoftgraph/msgraph-sdk-python'],
'S05':['makeplane/plane','opf/openproject','leantime/leantime','governikus/akav','alextselegidis/easyappointments','frappe/helpdesk','tastyigniter/TastyIgniter','joplin/server','kanboard/kanboard','stackstorm/st2','activepieces/activepieces'],
'S06':['ansible/awx','ansible/ansible','saltstack/salt','rudder-project/rudder','ansible-collections/ansible.windows','ansible-collections/community.windows','PowerShell/DSC','PowerShell/PSDesiredStateConfiguration','diyan/pywinrm','jborean93/pypsrp','jborean93/pyspnego','masterzen/winrm','netmiko/netmiko','ktbyers/netmiko','napalm-automation/napalm','scrapli/scrapli'],
'S07':['amidaware/tacticalrmm','amidaware/rmmagent','fleetdm/fleet','osquery/osquery','munkireport/munkireport-php','munki/munki','gorilla-devs/gorilla','opsi-org/opsi-server','uyuni-project/uyuni','open-uem/openuem-console','microMDM/micromdm','fleetdm/nano-mdm','nanomdm/nanomdm','sophos-ai/Sophos-PowerShell','CIPP-org/CIPP','CIPP-org/CIPP-API','KelvinTegelaar/RunAsUser','KelvinTegelaar/PowerShellMonitoring','microsoft/Microsoft365DSC'],
'S08':['wazuh/wazuh','wazuh/wazuh-docker','elastic/detection-rules','SigmaHQ/sigma','SigmaHQ/pySigma','MISP/MISP','MISP/PyMISP','OISF/suricata','zeek/zeek','greenbone/openvas-scanner','greenbone/gvmd','DFIR-IRIS/iris-web','TheHive-Project/TheHive','Velocidex/velociraptor','Yamato-Security/hayabusa','cisagov/ScubaGear','cisagov/ScubaGoggles','CISOfy/lynis','ComplianceAsCode/content','OpenSCAP/openscap','restic/restic','borgbackup/borg','kopia/kopia','garethgeorge/backrest','uroni/urbackup_backend','bareos/bareos','duplicati/duplicati','rclone/rclone','borgbase/vorta','Z-DBackup/duplicacy-web','librenms/librenms','zabbix/zabbix','Checkmk/checkmk','OpenNMS/opennms','netdata/netdata','louislam/uptime-kuma','prometheus/snmp_exporter','net-snmp/net-snmp','etingof/pysnmp','lextudio/pysnmp','pysnmp/pysnmp','ytti/oxidized','hpvanwyk/pySNMP'],
'S09':['microsoftgraph/msgraph-metadata','microsoftgraph/msgraph-sdk-dotnet','microsoftgraph/msgraph-sdk-go','microsoftgraph/msgraph-sdk-php','Azure/azure-sdk-for-python','pingidentity/scim2','wso2/charon','thomasmarsh/SCIMple','AzureAD/SCIMReferenceCode','go-ldap/ldap','python-ldap/python-ldap','samba-team/samba','netwrix/pingcastle','canix1/ADACLScanner'],
'S10':['panoramicdata/HaloPsa.Api','homotechsual/HaloAPI','homotechsual/NinjaOne','homotechsual/DattoRMM','KelvinTegelaar/ITGlueAPI','lwhitelock/HuduAPI','signl4/signl4-integration-glpi','softkat/mspp.io','financialforce/erp-devtools','intuit/QuickBooks-V3-PHP-SDK','intuit/QuickBooks-V3-DotNET-SDK','XeroAPI/xero-python','XeroAPI/Xero-OpenAPI'],
'S11':['invoice-x/invoice2data','HolgerBranse/Factur-X','ZUGFeRD/mustangproject','OCA/edi','OCA/account-invoicing','akretion/odoo-py3o-report-templates','dineshappavoo/braintree-recurring-billing','frappe/hrms','odoo/odoo','tryton/tryton','weclapp/api-specification'],
'S12':['gchq/CyberChef','defectdojo/django-DefectDojo','GibbonEdu/core','docusealco/docuseal','Documenso/documenso','paperless-ngx/paperless-ngx','opencontrol/compliance-masonry','usnistgov/OSCAL','defenseunicorns/go-oscal','CycloneDX/specification','spdx/spdx-spec','oasis-tcs/cti-stix2-json-schemas','oasis-open/cti-python-stix2','oasis-open/cti-taxii-client','awesome-selfhosted/awesome-selfhosted','awesome-foss/awesome-sysadmin','mikeroyal/Self-Hosting-Guide','MSPGeek/Community-Scripts','lwhitelock/PowerShell-Scripts','microsoft/winget-pkgs','chocolatey/choco','sounditsolutions/soundit-psa','Nine-Minds/alga-psa']}
terms={
'S01':('MSP PSA quote contract','psa','managed service provider API invoice'),
'S02':('CMDB inventory IT asset','cmdb','SNMP MIB inventory'),
'S03':('MSP onboarding documentation','it-documentation','SCIM provisioning'),
'S04':('helpdesk shared inbox email','helpdesk','IMAP MIME ticket'),
'S05':('service desk dispatch scheduling','itsm','iCalendar CalDAV scheduling'),
'S06':('IT change automation runbook','configuration-management','WinRM WSMan'),
'S07':('remote monitoring management RMM','rmm','CIM WMI inventory'),
'S08':('backup restore monitoring','backup','SCAP OVAL STIX'),
'S09':('Microsoft 365 MSP multi tenant','microsoft365','GDAP Microsoft Graph'),
'S10':('MSP billing reconciliation','msp','ConnectWise Autotask API'),
'S11':('invoice timesheet accounting self hosted','invoicing','UBL Factur-X invoice'),
'S12':('compliance evidence asset report','it-asset-management','OSCAL CycloneDX SPDX')}
queries=[]
for stage,(a,b,c) in terms.items():
    for lane,q in [('A',a),('B','topic:'+b),('C',c)]:
        queries.append({'round':1,'stage':stage,'lane':lane,'artifact_class':'applications' if lane=='A' else 'topic graph' if lane=='B' else 'protocols/specifications','q':q+' fork:false','sort':'stars','order':'desc','per_page':20})
round2=[('S01','A','MSP PSA open source alternative'),('S02','B','topic:ipam'),('S03','C','vault password sharing MSP'),('S04','A','helpdesk email parser library'),('S05','C','CalDAV iCalendar library'),('S06','B','topic:winrm'),('S07','B','topic:mdm'),('S08','C','STIX TAXII library'),('S09','A','Microsoft 365 license reporting PowerShell'),('S10','C','HaloPSA API'),('S11','C','OFX parser'),('S12','A','awesome sysadmin')]
for stage,lane,q in round2:queries.append({'round':2,'stage':stage,'lane':lane,'artifact_class':'bridges/libraries/registries','q':q+' fork:false','sort':'stars','order':'desc','per_page':20})
seen=set();lineage={};results=[];metadata_cache={};metadata_sources={}
for stage,names in seedgroups.items():
    for name in names:lineage.setdefault(name.lower(),[]).append({'route':'seed-hypothesis','stage':stage})
for ix,q in enumerate(queries):
    url=BASE+'/search/repositories?'+urllib.parse.urlencode({k:q[k] for k in ('q','sort','order','per_page')})
    obj=get(url);items=obj.get('items',[]);new=[]
    for it in items:
        name=it['full_name'];key=name.lower();metadata_cache[key]=it;metadata_sources[key]=url
        if key not in seen:new.append(name);seen.add(key)
        lineage.setdefault(key,[]).append({'route':'search','stage':q['stage'],'round':q['round'],'lane':q['lane'],'query':q['q']})
    receipt={**q,'query_url':url,'observed_at':now(),'total_count':obj.get('total_count'),'returned':len(items),'new_unique_names':new,'error':obj.get('_error')}
    results.append(receipt);save(pathlib.Path('search')/f'{ix+1:03d}.json',{'receipt':receipt,'response':obj})
    print('QUERY',ix+1,q['stage'],q['lane'],len(items),'new',len(new),flush=True);time.sleep(2.1)
save('search-log.json',results)
seed_names=list(dict.fromkeys(n for names in seedgroups.values() for n in names));selected=list(seed_names)
for ix in range(len(queries)):
    d=json.loads((R/'search'/f'{ix+1:03d}.json').read_text())
    for it in d['response'].get('items',[])[:1]:
        if it['full_name'].lower() not in {n.lower() for n in selected}:selected.append(it['full_name'])
save('selection-input.json',{'seed_hypotheses':seed_names,'dossier_retrieval_candidates':selected,'all_discovered_names':sorted(seen),'note':'Retrieval only, not recommendations. Invalid names and unrelated results cannot count as examined.'})
DEEP={'itflow-org/itflow','glpi-project/glpi','chatwoot/chatwoot','activepieces/activepieces','makeplane/plane','bookstackapp/bookstack','restic/restic','ylianst/meshcentral','zammad/zammad','netbox-community/netbox','cipp-org/cipp','cipp-org/cipp-api','nine-minds/alga-psa','fleetdm/fleet','amidaware/tacticalrmm'}
def dossier(name):
    out={'requested_name':name,'observed_at':now(),'lineage':lineage.get(name.lower(),[]),'sources':[],'files':[]}
    meta=metadata_cache.get(name.lower()) or get(BASE+'/repos/'+name)
    out['metadata_source']=metadata_sources.get(name.lower(),BASE+'/repos/'+name)
    if '_error' in meta:return {**out,'error':meta['_error']}
    full=meta['full_name'];out.update(full_name=full,repository=meta)
    commiturl=BASE+'/repos/'+full+'/commits?per_page=1';commits=get(commiturl)
    if not isinstance(commits,list) or not commits:return {**out,'error':'default-branch commit unavailable','commit_response':commits}
    co=commits[0];sha=co['sha'];out.update(commit=co,commit_sha=sha,last_commit_at=co['commit']['committer']['date'])
    rooturl=BASE+'/repos/'+full+'/contents/?ref='+sha;tree=get(rooturl)
    out['root_entries']=[{k:x.get(k) for k in ('name','path','type','sha','size')} for x in tree] if isinstance(tree,list) else tree
    out['sources']=[out['metadata_source'],commiturl,rooturl]
    if isinstance(tree,list):
        manifests={'package.json','composer.json','go.mod','pyproject.toml','requirements.txt','Gemfile','Cargo.toml','docker-compose.yml','docker-compose.yaml','compose.yml','compose.yaml'}
        choices=[x for x in tree if x['type']=='file' and (re.match(r'(?i)^(readme|licen[sc]e|copying|notice)(\.|$)',x['name']) or x['name'] in manifests)]
        for x in choices:
            if re.match(r'(?i)^readme\.',x['name']) and re.search(r'(?i)\.(zh|cn|jp|ja|ru|es|fr|de|ko|pt)',x['name']):continue
            if (x.get('size') or 0)>1500000:continue
            url='https://raw.githubusercontent.com/'+full+'/'+sha+'/'+urllib.parse.quote(x['path']);b=get(url,raw=True)
            if isinstance(b,bytes):out['files'].append({'path':x['path'],'url':url,'git_blob_sha':x['sha'],'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b),'text':b.decode('utf8',errors='replace')})
        for sub in [x for x in tree if x['type']=='dir' and x['name'].lower() in ('ee','enterprise','premium','licenses','licences')]:
            u=BASE+'/repos/'+full+'/contents/'+sub['path']+'?ref='+sha;parts=get(u)
            out.setdefault('license_subdirectories',[]).append({'path':sub['path'],'entries':parts,'source':u})
            if isinstance(parts,list):
                for x in parts:
                    if x['type']=='file' and re.match(r'(?i)^(licen[sc]e|copying|notice)(\.|$)',x['name']):
                        url='https://raw.githubusercontent.com/'+full+'/'+sha+'/'+urllib.parse.quote(x['path']);b=get(url,raw=True)
                        if isinstance(b,bytes):out['files'].append({'path':x['path'],'url':url,'git_blob_sha':x['sha'],'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b),'text':b.decode('utf8',errors='replace')})
    health=[('issue_sample','issues?state=all&sort=updated&direction=desc&per_page=5')]
    if full.lower() in DEEP:health.append(('contributors','contributors?per_page=5'))
    for key,suffix in health:
        u=BASE+'/repos/'+full+'/'+suffix;out[key]=get(u);out['sources'].append(u)
    out['finished_at']=now();return out
outputs=[]
with cf.ThreadPoolExecutor(max_workers=4) as pool:
    for i,out in enumerate(pool.map(dossier,selected),1):
        name=out.get('full_name',out['requested_name']);save(pathlib.Path('dossiers')/(name.replace('/','__')+'.json'),out)
        outputs.append({k:out.get(k) for k in ('requested_name','full_name','commit_sha','last_commit_at','observed_at','error')});print('DOSSIER',i,name,'ERROR' if out.get('error') else len(out['files']),flush=True)
save('dossier-index.json',outputs)
save('manifest.json',{'observed_at':now(),'stage3_complete_before_sweep':'2026-09-13T15:35:12Z','queries':len(queries),'discovery_rounds':2,'dossiers_requested':len(selected),'dossiers_retrieved':sum(not x.get('error') for x in outputs),'unique_search_names':len(seen),'examination_status':'Collected for reading and judgement; collection is not an examined count. Further novelty rounds required.','security':'Public source GET only; no upstream code, installers or dependencies executed; token never persisted.'})
