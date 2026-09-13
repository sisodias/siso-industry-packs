"""Research-only public GitHub inventory collection. Never executes candidate code.
Runs once on the named research branch; writes only this pack's research receipts.
No customer data, external account tokens, deployments or application code are used.
"""
import base64, concurrent.futures, datetime, hashlib, json, os, re, time
import urllib.request, urllib.parse, urllib.error

REPO = 'sisodias/siso-industry-packs'
BRANCH = 'research/marketing-agencies-20260913'
ROOT = 'packs/marketing_social_media_agencies/'
AS_OF = '2026-09-13'
MAX_EXAMINED = 160
TOKEN = os.environ.get('GH_TOKEN', '')
assert os.environ.get('GITHUB_REF_NAME', BRANCH) == BRANCH
STARTED = datetime.datetime.now(datetime.timezone.utc).isoformat()
errors = []

def api(path, method='GET', data=None, missing_ok=False):
    assert path.startswith('/') and not path.startswith('//')
    headers = {'Accept':'application/vnd.github+json','User-Agent':'SISO-agency-research-receipts','X-GitHub-Api-Version':'2022-11-28'}
    if TOKEN: headers['Authorization'] = 'Bearer ' + TOKEN
    for attempt in range(4):
        try:
            req = urllib.request.Request('https://api.github.com'+path, data=None if data is None else json.dumps(data).encode(), headers=headers, method=method)
            with urllib.request.urlopen(req, timeout=60) as response:
                raw = response.read()
                return json.loads(raw) if raw else None
        except urllib.error.HTTPError as e:
            if missing_ok and e.code in (404,409,451): return None
            if e.code in (403,429,500,502,503,504) and attempt < 3:
                delay = min(90, max(3, int(e.headers.get('Retry-After','3'))))
                time.sleep(delay * (attempt+1)); continue
            raise RuntimeError('GitHub HTTP %s for %s' % (e.code,path.split('?')[0])) from None
        except (TimeoutError, urllib.error.URLError):
            if attempt < 3: time.sleep(3*(attempt+1)); continue
            raise RuntimeError('Public source transport failure for '+path.split('?')[0]) from None

def now(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha256(b): return hashlib.sha256(b).hexdigest()
def clean_repo(x):
    if not isinstance(x,str): return None
    m=re.search(r'github\.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)',x)
    if m: return m.group(1).removesuffix('.git')
    return x if re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+',x) else None

def primary_name(row):
    for k in ('full_name','repository_full_name','repo_full_name','repository','repo','github_url','repository_url','source_url','url'):
        v=row.get(k)
        n=clean_repo(v)
        if n: return n
        if isinstance(v,dict):
            n=primary_name(v)
            if n: return n
    return None

bank_head=api('/repos/sisodias/siso-repo-bank/commits/main')['sha']
bank_files=['bank/bank_capability_top.jsonl','bank/bank_capability.jsonl','capability-shelf/source-registry.jsonl','bank/bank_best.jsonl','bank/bank_adoption_v2.jsonl','bank/bank_liftable_ranked.jsonl','bank/bank_contractcard.jsonl','bank/bank_gold.jsonl']
bank_names=set(); bank_rows={}; bank_counts={}; shelf=[]; tops=[]; vocabulary=[]
for path in bank_files:
    url='https://raw.githubusercontent.com/sisodias/siso-repo-bank/'+bank_head+'/'+path
    count=0; h=hashlib.sha256(); keys=[]
    with urllib.request.urlopen(url,timeout=90) as response:
        for line in response:
            h.update(line)
            if not line.strip(): continue
            row=json.loads(line); count+=1
            if not keys: keys=list(row)
            name=primary_name(row)
            if name:
                key=name.lower(); bank_names.add(key)
                bank_rows.setdefault(key,{})[path]=row
            if path.endswith('source-registry.jsonl'): shelf.append(row)
            if path.endswith('bank_capability_top.jsonl'): tops.append(row)
            if path.endswith('bank_capability.jsonl'): vocabulary.append(row['capability'])
    bank_counts[path]={'rows':count,'sha256':h.hexdigest(),'first_row_keys':keys,'source_url':url}
print('BANK_STREAMED',json.dumps({k:v['rows'] for k,v in bank_counts.items()}),flush=True)

# Workflow-derived three lanes: keyword, topic and artifact format/protocol.
stages=[
('S01','shared inbox email self hosted','topic:customer-support','IMAP MIME parser'),
('S02','CRM proposal electronic signature','topic:crm','iCalendar CalDAV'),
('S03','digital asset management','topic:digital-asset-management','IPTC XMP metadata'),
('S04','social media content calendar','topic:social-media-management','CSV content import social'),
('S05','video subtitles image processing','topic:subtitles','WebVTT SRT C2PA'),
('S06','client content approval proofing','topic:approval-workflow','document signature PAdES'),
('S07','social media scheduler self hosted','topic:social-media-scheduler','Instagram Graph API SDK'),
('S08','omnichannel customer inbox','topic:chatwoot','WhatsApp Cloud API webhook'),
('S09','marketing analytics reporting','topic:web-analytics','GA4 analytics data API'),
('S10','invoice accounting self hosted','topic:invoicing','Stripe webhook idempotency'),
('S11','time tracking project management','topic:time-tracking','iCalendar timesheet import')]

# These are unqualified reference candidates, not recommendations. Every retained
# candidate is resolved through the API before an examination receipt is issued.
seeds='''chatwoot/chatwoot papercups-io/papercups freescout-help-desk/freescout zammad/zammad erxes/erxes espocrm/espocrm salesagility/SuiteCRM frappe/crm twentyhq/twenty odoo/odoo Dolibarr/dolibarr frappe/erpnext documenso/documenso docusealco/docuseal LibreSign/libresign OpenSignLabs/OpenSign calcom/cal.com BookStackApp/BookStack sabre-io/dav kewisch/ical.js icalendar/icalendar nextcloud/server nextcloud/calendar nextcloud/deck nextcloud/spreed nocodb/nocodb baserow/baserow bram2w/baserow directus/directus strapi/strapi payloadcms/payload AppFlowy-IO/AppFlowy outline/outline makeplane/plane vikunja/vikunja Leantime/leantime kanboard/kanboard opf/openproject taigaio/taiga-back gitroomhq/postiz-app inovector/mixpost socioboard/Socioboard-5.0 socioboard/Socioboard-Core shlinkio/shlink YOURLS/YOURLS thedevs-network/kutt dubinc/dub mautic/mautic knadh/listmonk Mailtrain-org/mailtrain postalserver/postal Mailu/Mailu foxcpp/maddy akeneo/pim-community-dev pimcore/pimcore alchemy-fr/Phraseanet ResourceSpace/ResourceSpace LycheeOrg/Lychee immich-app/immich photoprism/photoprism Piwigo/Piwigo thumbor/thumbor imgproxy/imgproxy lovell/sharp libvips/libvips ImageMagick/ImageMagick FFmpeg/FFmpeg PyAV-Org/PyAV ffmpegwasm/ffmpeg.wasm SubtitleEdit/subtitleedit Aegisub/Aegisub plausible/analytics umami-software/umami matomo-org/matomo rudderlabs/rudder-server snowplow/snowplow metabase/metabase apache/superset lightdash/lightdash getredash/redash airbytehq/airbyte meltano/meltano singer-io/tap-facebook singer-io/tap-google-analytics googleapis/python-analytics-data googleads/google-ads-python facebook/facebook-python-business-sdk facebook/facebook-nodejs-business-sdk twitterdev/twitter-api-typescript-sdk PLhery/node-twitter-api-v2 abraham/twitteroauth bluesky-social/atproto mastodon/mastodon tus/tusd tus/tus-js-client adobe/XMP-Toolkit-SDK contentauth/c2pa-rs contentauth/c2patool c2pa-org/specifications heyform/heyform ohmyform/ohmyform formbricks/formbricks formio/formio OpnForm/OpnForm invoiceninja/invoiceninja akaunting/akaunting InvoicePlane/InvoicePlane crater-invoice/crater solidinvoice/solidinvoice frappe/hrms kimai/kimai ever-co/ever-gauzy activepieces/activepieces n8n-io/n8n windmill-labs/windmill huginn/huginn triggerdotdev/trigger.dev node-red/node-red GrapesJS/grapesjs mjmlio/mjml foundation/foundation-emails Kozea/WeasyPrint gotenberg/gotenberg Stirling-Tools/Stirling-PDF OpenLineage/OpenLineage dbt-labs/dbt-core frictionlessdata/frictionless-py restic/restic caddyserver/caddy healthchecks/healthchecks louislam/uptime-kuma awesome-selfhosted/awesome-selfhosted awesome-selfhosted/awesome-selfhosted-data'''.split()
pool={}; search_log=[]; rounds=[]
def add(name,via,stage=None,metadata=None):
    n=clean_repo(name)
    if not n: return False
    k=n.lower(); new=k not in pool
    row=pool.setdefault(k,{'full_name':n,'discovered_via':[],'stages':[]})
    if via not in row['discovered_via']: row['discovered_via'].append(via)
    if stage and stage not in row['stages']: row['stages'].append(stage)
    if metadata:
        row['search_stars']=metadata.get('stargazers_count')
        row['search_description']=' '.join((metadata.get('description') or '').split()[:20])
    return new

# Product-base shelf skim precedes bank_best capability expansion and web discovery.
terms=('marketing','social media','social-media','inbox','crm','approval','digital asset','invoice','time tracking','newsletter','calendar','analytics')
shelf_matches=[]
for row in shelf:
    text=json.dumps(row).lower()
    if any(t in text for t in terms):
        shelf_matches.append(row)
        name=primary_name(row)
        if name: add(name,'bank-product-base-shelf')
for name in seeds: add(name,'reference-candidate-verification')
seed_count=len(pool)

def search(q,stage,lane,rnd):
    path='/search/repositories?'+urllib.parse.urlencode({'q':q,'sort':'stars','order':'desc','per_page':8})
    started=now()
    try:
        data=api(path)
        names=[]; added=0
        for r in data.get('items',[]):
            names.append(r['full_name']); added+=int(add(r['full_name'],f'round-{rnd}:{lane}:{q}',stage,r))
        search_log.append({'round':rnd,'stage':stage,'lane':lane,'query':q,'sort':'stars-desc','per_page':8,'total_count':data.get('total_count'),'returned':names,'new_names':added,'observed_at':started,'source_url':'https://api.github.com'+path})
    except Exception as e:
        search_log.append({'round':rnd,'stage':stage,'lane':lane,'query':q,'error':str(e),'observed_at':started}); errors.append(str(e))
    time.sleep(2.1)

def run_round(number,queries,label):
    before=set(pool)
    for stage,lane,q in queries: search(q,stage,lane,number)
    added=sorted(set(pool)-before)
    rounds.append({'round':number,'purpose':label,'queries':len(queries),'new_names':len(added),'names':added})
    print('ROUND',number,'NEW',len(added),'POOL',len(pool),flush=True)

r1=[]
for sid,a,b,c in stages: r1.extend([(sid,'A-keyword',a),(sid,'B-topic',b),(sid,'C-format-protocol',c)])
run_round(1,r1,'Three discovery lanes for every workflow stage; applications, topics and wire/artifact formats')
run_round(2,[
('S01','bridge','email conversation CRM webhook'),('S02','engine','e-signature self hosted'),('S03','spec','C2PA IPTC'),('S04','plugin','content calendar wordpress plugin'),('S05','library','video metadata subtitle parser'),('S06','app','open source alternative Planable'),('S07','app','open source alternative Buffer Hootsuite'),('S08','protocol','ActivityPub inbox client'),('S09','connector','singer tap facebook ads'),('S10','format','invoice UBL parser'),('S11','registry','awesome selfhosted time tracking')], 'Different artifact classes: engines, bridges, plugins, specifications, alternatives and registries')
run_round(3,[
('S07','maintainer','user:inovector'),('S07','maintainer','user:gitroomhq'),('S01','maintainer','org:chatwoot'),('S09','maintainer','org:singer-io facebook'),('S05','maintainer','org:contentauth'),('S06','registry','awesome digital asset management'),('S04','registry','awesome social media tools'),('S09','registry','awesome web analytics'),('S07','protocol','OpenRTB VAST'),('S03','format','IPTC photo metadata'),('S06','library','PDF digital signature validation')], 'Maintainer neighborhoods, registries and neglected metadata/ad-tech formats')
# Gap-directed rounds are real searches for the missing transaction boundary, not
# repeats of earlier queries. Zero results are local search findings, not proof of absence.
gap_rounds=[
[('S06','gap','"social" "approval" "content hash"'),('S07','gap','"Instagram" "publication receipt"'),('S02','gap','"WhatsApp" "scope creep"')],
[('S06','gap','"approval manifest" social'),('S03','gap','"IPTC" "client approval"'),('S09','gap','"social metrics" "provenance ledger"')],
[('S07','gap','"Facebook" "version-bound approval"'),('S06','gap','"PAdES" "social campaign"'),('S10','gap','"content revision" "change order"')],
[('S06','gap','"C2PA" "scope change"'),('S07','gap','"approved payload" "wrong account"'),('S09','gap','"client report" "metric provenance"')]]
dry=0
for rnd,qs in enumerate(gap_rounds,4):
    run_round(rnd,qs,'Targeted search for a missing approval/scope/receipt integration boundary')
    dry=dry+1 if rounds[-1]['new_names']==0 else 0
    if dry>=2: break

# Examine at least the named reference alternatives, then fill with search results.
# No final fit/adoption verdict is assigned by this collection program.
ordered=[]; seen=set()
for name in seeds:
    key=name.lower()
    if key not in seen: ordered.append(pool[key]); seen.add(key)
for row in sorted(pool.values(),key=lambda x:(-len(x['stages']),-(x.get('search_stars') or 0),x['full_name'].lower())):
    key=row['full_name'].lower()
    if key not in seen: ordered.append(row); seen.add(key)

receipt_terms=['docker','compose','self-host','self hosted','api','webhook','approval','workflow','oauth','postgres','redis','mysql','sqlite','memory','ram','cpu','gpu','license','enterprise','commercial','analytics','scheduling','calendar','imaps','smtp','webvtt','iptc','xmp','c2pa','activitypub','ubl','pades']
def examine(candidate):
    requested=candidate['full_name']; observed=now()
    try:
        meta=api('/repos/'+requested,missing_ok=True)
        if not meta: return {'requested':requested,'verification_status':'not_resolved','observed_at':observed}
        name=meta['full_name']; base='/repos/'+name
        commits=api(base+'/commits?per_page=1',missing_ok=True) or []
        if not commits: return {'requested':requested,'full_name':name,'verification_status':'empty_repository','observed_at':observed}
        head=commits[0]; pin=head['sha']
        readme=api(base+'/readme?ref='+pin,missing_ok=True)
        rb=base64.b64decode(readme.get('content','')) if readme and readme.get('encoding')=='base64' else b''
        rt=rb.decode('utf-8','replace')
        lic=api(base+'/license?ref='+pin,missing_ok=True)
        lb=base64.b64decode(lic.get('content','')) if lic and lic.get('encoding')=='base64' else b''
        lt=lb.decode('utf-8','replace')
        recent=api(base+'/commits?'+urllib.parse.urlencode({'since':'2026-03-13T00:00:00Z','until':'2026-09-13T23:59:59Z','per_page':20}),missing_ok=True) or []
        contributors=api(base+'/contributors?per_page=5',missing_ok=True) or []
        issues=api(base+'/issues?state=all&sort=updated&direction=desc&per_page=5',missing_ok=True) or []
        issue_evidence=[]
        for issue in [x for x in issues if 'pull_request' not in x][:2]:
            comments=[]
            if issue.get('comments'):
                comments=api(base+'/issues/'+str(issue['number'])+'/comments?per_page=5',missing_ok=True) or []
            responses=[x for x in comments if x.get('author_association') in ('OWNER','MEMBER','COLLABORATOR') and x.get('user',{}).get('login')!=issue.get('user',{}).get('login')]
            issue_evidence.append({'url':issue['html_url'],'created_at':issue['created_at'],'updated_at':issue['updated_at'],'state':issue['state'],'comments':issue['comments'],'maintainer_response_in_sample':bool(responses),'sample_response_at':responses[0]['created_at'] if responses else None})
        root=api(base+'/contents?ref='+pin,missing_ok=True) or []
        rootfiles=[x['path'] for x in root if x.get('type')=='file'] if isinstance(root,list) else []
        manifest_names=[x for x in rootfiles if x in ('package.json','pyproject.toml','requirements.txt','composer.json','go.mod','Cargo.toml','Gemfile')]
        dependency_refs=[]
        for path in manifest_names[:1]:
            f=api(base+'/contents/'+path+'?ref='+pin,missing_ok=True)
            text=base64.b64decode(f.get('content','')).decode('utf-8','replace') if f and f.get('encoding')=='base64' else ''
            dependency_refs=sorted(set(re.findall(r'https?://github\.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)',text)))[:30]
        licence_signals=[]
        for token in ('MIT License','GNU AFFERO GENERAL PUBLIC LICENSE','GNU GENERAL PUBLIC LICENSE','Apache License','Business Source License','Sustainable Use License','Elastic License','Server Side Public License','FSL','commercial','enterprise'):
            if token.lower() in lt.lower(): licence_signals.append(token)
        record={'requested':requested,'full_name':name,'github_id':meta['id'],'url':meta['html_url'],'observed_at':observed,'verification_status':'examined_metadata_readme_license','stars':meta['stargazers_count'],'archived':meta['archived'],'fork':meta['fork'],'default_branch':meta['default_branch'],'language':meta['language'],'description_excerpt':' '.join((meta.get('description') or '').split()[:20]),'topics':meta.get('topics',[]),'head_sha':pin,'last_commit_at':head['commit']['committer']['date'],'last_commit_url':head['html_url'],'readme_source':readme.get('html_url') if readme else None,'readme_sha256':sha256(rb) if rb else None,'readme_bytes':len(rb),'readme_opening_excerpt':' '.join(rt.split()[:20]),'readme_signals':[t for t in receipt_terms if t in rt.lower()],'license_metadata':(meta.get('license') or {}).get('spdx_id'),'license_source':lic.get('html_url') if lic else None,'license_path':lic.get('path') if lic else None,'license_sha256':sha256(lb) if lb else None,'license_bytes':len(lb),'license_opening_excerpt':' '.join(lt.split()[:20]),'license_text_signals':licence_signals,'license_review_scope':'actual root license text retrieved and hashed; directory/edition review not yet complete','root_license_paths':[p for p in rootfiles if any(t in p.lower() for t in ('license','licence','copying','notice'))],'deployment_file_candidates':[p for p in rootfiles if any(t in p.lower() for t in ('docker','compose','install'))],'commits_last_six_months_sample_count':len(recent),'commit_sample_cap':20,'recent_committers_sample':sorted(set(x.get('author',{}).get('login','unknown') for x in recent if isinstance(x.get('author'),dict))),'top_contributors_sample':[{'login':x.get('login'),'contributions':x.get('contributions'),'type':x.get('type')} for x in contributors if isinstance(x,dict)],'contributor_sample_cap':5,'issue_response_sample':issue_evidence,'manifest_paths_checked':manifest_names[:1],'dependency_github_refs':dependency_refs,'discovery':candidate}
        keys=[name.lower(),requested.lower()]
        matches={}
        for key in keys:
            for layer,row in bank_rows.get(key,{}).items(): matches[layer]=row
        record['bank_status']='ALREADY IN THE BANK' if matches else 'NEW'
        record['bank_membership_basis']=sorted(matches)
        record['bank_adoption']=matches.get('bank/bank_adoption_v2.jsonl')
        record['bank_liftability']=matches.get('bank/bank_liftable_ranked.jsonl')
        record['bank_best']=matches.get('bank/bank_best.jsonl')
        record['bank_contractcard']=matches.get('bank/bank_contractcard.jsonl')
        return record
    except Exception as e:
        return {'requested':requested,'verification_status':'error','error':str(e),'observed_at':observed}

receipts=[]; resolved_ids=set(); attempted=set()
for offset in range(0,len(ordered),20):
    if len(receipts)>=MAX_EXAMINED: break
    batch=ordered[offset:offset+20]
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        results=list(executor.map(examine,batch))
    for r in results:
        attempted.add(r['requested'].lower())
        if r.get('github_id') and r['github_id'] not in resolved_ids:
            receipts.append(r); resolved_ids.add(r['github_id'])
        elif r.get('verification_status') in ('error','not_resolved','empty_repository'):
            errors.append(r)
    print('EXAMINED',len(receipts),'ATTEMPTED',len(attempted),flush=True)
receipts=receipts[:MAX_EXAMINED]

# Dependency closure receipts: identify novel referenced repos; never silently mark
# these as examined or count them toward the quota without resolving/reading them.
dependency_frontier=[]
for r in receipts:
    for name in r.get('dependency_github_refs',[]):
        if name.lower() not in pool:
            dependency_frontier.append({'from':r['full_name'],'candidate':name,'manifest':r['manifest_paths_checked']})

# Mirror the exact nine-column workflow table into JSON, without invented extra rows.
wf=api('/repos/'+REPO+'/contents/'+ROOT+'02-workflow.md?ref='+urllib.parse.quote(BRANCH,safe=''))
wftext=base64.b64decode(wf['content']).decode()
columns=['id','stage','trigger','inputs','outputs','pain','frequency','handoff','data_object']
workflow_rows=[]
for line in wftext.splitlines():
    if re.match(r'^\| S\d\d \|',line):
        values=[x.strip() for x in line.strip().strip('|').split('|')]
        assert len(values)==len(columns)
        workflow_rows.append(dict(zip(columns,values)))
assert len(workflow_rows)==11

summary={'as_of':AS_OF,'started_at':STARTED,'finished_at':now(),'commercial_stage_commit':'163f1c53d59d2a12cc23ef7f0fe6e11501415a96','bank_head':bank_head,'bank_stream_order':bank_files,'bank_files':bank_counts,'bank_distinct_primary_names':len(bank_names),'shelf_matching_rows':len(shelf_matches),'seed_and_shelf_pool':seed_count,'discovered_distinct_names':len(pool),'examined_distinct_github_ids':len(receipts),'max_examined':MAX_EXAMINED,'rounds':rounds,'two_consecutive_search_rounds_without_new_names':dry>=2,'dependency_frontier_not_yet_examined':dependency_frontier,'search_saturation_claim':'bounded queries only; not proof that no other open-source project exists','examination_scope':'metadata, default-branch head, actual root README and LICENSE bytes, capped commit/contributor/issue samples and one root dependency manifest; no runtime execution or legal clearance','bank_membership_scope':'public eight-layer SISO export at pinned bank head; not the unpublished identity database','errors':errors,'actual_new_repos':sum(r['bank_status']=='NEW' for r in receipts),'actual_already_in_bank':sum(r['bank_status']=='ALREADY IN THE BANK' for r in receipts)}
files={ROOT+'02-workflow.json':json.dumps({'as_of':AS_OF,'evidence_class':'analysis','frequency_status':'unmeasured','stages':workflow_rows},indent=2)+'\n',ROOT+'research/harvest-summary.json':json.dumps(summary,indent=2)+'\n',ROOT+'research/search-log.json':json.dumps(search_log,indent=2)+'\n',ROOT+'research/discovery.jsonl':'\n'.join(json.dumps(r,ensure_ascii=False) for r in sorted(pool.values(),key=lambda x:x['full_name'].lower()))+'\n',ROOT+'research/oss-receipts.jsonl':'\n'.join(json.dumps(r,ensure_ascii=False) for r in receipts)+'\n',ROOT+'research/bank-vocabulary.json':json.dumps(vocabulary,indent=2)+'\n',ROOT+'research/bank-product-base-matches.jsonl':'\n'.join(json.dumps(r,ensure_ascii=False) for r in shelf_matches)+'\n',ROOT+'research/bank-capability-top.jsonl':'\n'.join(json.dumps(r,ensure_ascii=False) for r in tops)+'\n'}
# Small review chunks avoid the connector's large-file limit.
for i in range(0,len(receipts),8):
    compact=[]
    for r in receipts[i:i+8]:
        keep={k:v for k,v in r.items() if k not in ('bank_best','bank_contractcard','bank_liftability','bank_adoption','discovery')}
        keep['bank_adoption']=r.get('bank_adoption')
        compact.append(keep)
    files[ROOT+f'research/review-{i//8+1:02d}.jsonl']='\n'.join(json.dumps(r,ensure_ascii=False) for r in compact)+'\n'

# Atomic branch-only data commit. Re-read head so other pack edits are preserved.
for attempt in range(3):
    head=api('/repos/'+REPO+'/git/ref/heads/'+BRANCH)['object']['sha']
    base_tree=api('/repos/'+REPO+'/git/commits/'+head)['tree']['sha']
    tree=api('/repos/'+REPO+'/git/trees',method='POST',data={'base_tree':base_tree,'tree':[{'path':p,'mode':'100644','type':'blob','content':s} for p,s in files.items()]})
    commit=api('/repos/'+REPO+'/git/commits',method='POST',data={'message':'research(marketing): record bounded search, bank joins and dated upstream receipts','tree':tree['sha'],'parents':[head]})
    try:
        api('/repos/'+REPO+'/git/refs/heads/'+BRANCH,method='PATCH',data={'sha':commit['sha'],'force':False})
        print('RESEARCH_RECEIPT_COMMIT',commit['sha'],flush=True); break
    except Exception:
        if attempt==2: raise
        time.sleep(2)
print('FINAL_COUNTS',json.dumps({k:summary[k] for k in ('discovered_distinct_names','examined_distinct_github_ids','actual_new_repos','actual_already_in_bank','two_consecutive_search_rounds_without_new_names')}),flush=True)
