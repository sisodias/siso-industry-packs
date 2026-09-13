"""Public-source research collector. Never executes upstream code or reads private repositories."""
import os,json,time,base64,hashlib,pathlib,re,datetime,urllib.request,urllib.parse,urllib.error,concurrent.futures
OUT=pathlib.Path('oss-evidence'); OUT.mkdir(exist_ok=True)
TOKEN=os.environ.get('GH_TOKEN','')
NOW=datetime.datetime.now(datetime.timezone.utc); SINCE=(NOW-datetime.timedelta(days=183)).isoformat()
API='https://api.github.com'
errors=[]
def get(url):
    headers={'User-Agent':'SISO-public-research-audit','Accept':'application/vnd.github+json'}
    if url.startswith(API+'/') and TOKEN: headers['Authorization']='Bearer '+TOKEN
    for attempt in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url,headers=headers),timeout=30) as r:
                data=r.read(); return json.loads(data) if url.startswith(API+'/') else data.decode('utf-8','replace')
        except urllib.error.HTTPError as e:
            if e.code in (429,403) and attempt<2:
                time.sleep(35); continue
            return {'_error':e.code,'url':url}
        except Exception as e:
            if attempt<2: time.sleep(2); continue
            return {'_error':type(e).__name__,'url':url}
def api(path): return get(API+path)
def save(name,obj): (OUT/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def decoded(obj):
    if isinstance(obj,dict) and obj.get('encoding')=='base64':
        try: return base64.b64decode(obj.get('content','')).decode('utf-8','replace')
        except Exception: return ''
    return ''
# Query classes come from the commercial map completed 2026-09-13T15:35:57Z.
rows=[
('S01',['creator crm self hosted','shared inbox email'], 'customer-support','email webhook RFC822'),
('S02',['youtube research analytics','youtube keyword'], 'youtube-api','youtube analytics reporting api'),
('S03',['screenplay parser','youtube script generator'], 'screenwriting','fountain screenplay'),
('S04',['local text speech narration','voiceover self hosted'], 'text-to-speech','SSML phonemizer ONNX'),
('S05',['media asset management','music fingerprint'], 'digital-asset-management','XMP IPTC metadata'),
('S06',['video editor self hosted','programmatic video editing'], 'video-editing','OpenTimelineIO FCPXML EDL'),
('S07',['subtitle editor','thumbnail image editor'], 'subtitles','WebVTT SRT ASS'),
('S08',['video review collaboration','production tracking animation'], 'video-review','timecode review annotation'),
('S09',['social media scheduler self hosted','youtube uploader'], 'social-media-management','youtube resumable upload OAuth'),
('S10',['shorts generator','automatic video clipping'], 'video-clipping','scene detection aspect ratio'),
('S11',['youtube comment moderation','youtube analytics dashboard'], 'youtube-analytics','audienceWatchRatio elapsedVideoTimeRatio'),
('S12',['creator invoice self hosted','media rights management'], 'invoicing','ODRL C2PA rights')]
queries=[]
for stage,keywords,topic,fmt in rows:
    for q in keywords: queries.append({'round':1,'lane':'A','stage':stage,'artifact_class':'runnable applications / engines','query':q})
    queries.append({'round':2,'lane':'B','stage':stage,'artifact_class':'topic graph','query':'topic:'+topic})
    queries.append({'round':3,'lane':'C','stage':stage,'artifact_class':'formats / protocols / SDKs','query':fmt})
queries += [
{'round':3,'lane':'C','stage':'S06','artifact_class':'awesome-list','query':'awesome video'},
{'round':3,'lane':'C','stage':'S04','artifact_class':'awesome-list','query':'awesome text to speech'},
{'round':3,'lane':'C','stage':'S09','artifact_class':'alternative','query':'buffer alternative self hosted'},
{'round':3,'lane':'C','stage':'S10','artifact_class':'alternative','query':'opusclip alternative'},
{'round':3,'lane':'C','stage':'S08','artifact_class':'alternative','query':'frame.io alternative'},
{'round':3,'lane':'C','stage':'S06','artifact_class':'plugin bridge','query':'CapCut draft parser'}]
# Broad previously-held/publicly discovered leads, not recommendations. Errors never count as examination.
anchor_groups={
'S01':'chatwoot/chatwoot twentyhq/twenty frappe/crm freescout-help-desk/freescout zammad/zammad knadh/listmonk',
'S02':'yt-dlp/yt-dlp pytube/pytube pytubefix/pytubefix jdepoix/youtube-transcript-api GeneralMills/pytrends searxng/searxng FreshRSS/FreshRSS miniflux/v2 ArchiveBox/ArchiveBox meeb/tubesync tubearchivist/tubearchivist iv-org/invidious',
'S03':'nyousefi/Fountain screenplain/screenplain simonw/llm ollama/ollama ggml-org/llama.cpp',
'S04':'OHF-Voice/piper1-gpl rhasspy/piper hexgrad/kokoro hexgrad/misaki remsky/Kokoro-FastAPI coqui-ai/TTS idiap/coqui-ai-TTS Blaizzy/mlx-audio QwenAudio/CosyVoice SWivid/F5-TTS fishaudio/fish-speech resemble-ai/chatterbox canopyai/Orpheus-TTS suno-ai/bark myshell-ai/OpenVoice rany2/edge-tts espeak-ng/espeak-ng k2-fsa/sherpa-onnx',
'S05':'mediacms-io/mediacms immich-app/immich photoprism/photoprism nextcloud/server rclone/rclone seaweedfs/seaweedfs minio/minio openverse/openverse musicbrainz/picard beetbox/beets acoustid/chromaprint worldveil/dejavu exiftool/exiftool',
'S06':'FFmpeg/FFmpeg PyAV-Org/PyAV Zulko/moviepy mltframework/mlt mltframework/shotcut OpenShot/libopenshot OpenShot/openshot-qt KDE/kdenlive olive-editor/olive OpenCut-app/OpenCut remotion-dev/remotion motion-canvas/motion-canvas mifi/editly mifi/lossless-cut walterlow/freecut trykimu/videoeditor WebAV-Tech/WebAV ffmpegwasm/ffmpeg.wasm AcademySoftwareFoundation/OpenTimelineIO',
'S07':'SubtitleEdit/subtitleedit m-bain/whisperX SYSTRAN/faster-whisper ggml-org/whisper.cpp openai/whisper linto-ai/whisper-timestamped jianfch/stable-ts pyannote/pyannote-audio libass/libass Aegisub/Aegisub videojs/vtt.js cdown/srt glut23/webvtt-py tkarabela/pysubs2 ImageMagick/ImageMagick libvips/libvips lovell/sharp penpot/penpot tmoroney/auto-subs',
'S08':'cgwire/kitsu cgwire/zou meshroom/meshroom OpenImageIO/oiio OpenColorIO/OpenColorIO',
'S09':'gitroomhq/postiz-app inovector/mixpost postflow/postflow socioboard/Socioboard-5.0 porjo/youtubeuploader tokland/youtube-upload googleapis/google-api-python-client googleapis/google-api-nodejs-client googleapis/google-api-go-client bluenviron/mediamtx',
'S10':'RayVentura/ShortGPT FujiwaraChoki/MoneyPrinter FujiwaraChoki/MoneyPrinterV2 harry0703/MoneyPrinterTurbo WyattBlue/auto-editor Breakthrough/PySceneDetect modelscope/FunClip zhouxiaoka/autoclip Anil-matcha/AI-Youtube-Shorts-Generator SamurAIGPT/AI-Youtube-Shorts-Generator google-ai-edge/mediapipe',
'S11':'ThioJoe/YT-Spammer-Purge youtube/api-samples metabase/metabase apache/superset umami-software/umami',
'S12':'invoiceninja/invoiceninja akaunting/akaunting frappe/erpnext frappe/books InvoicePlane/InvoicePlane TryGhost/Ghost frappe/lms moodle/moodle ContentAuthenticity/c2pa-rs ContentAuthenticity/c2patool w3c/odrl w3c/webvtt w3c/ttml2'}
seen={}; seeds=[]
for stage,names in anchor_groups.items():
    for name in names.split():
        if name.lower() not in seen:
            seen[name.lower()]={'full_name':name,'stages':[stage],'discovery':['prior-bank/public-lead'],'first_round':0}; seeds.append(name)
log=[]; roundstats=[]
for roundnum in (1,2,3):
    before=set(seen)
    for q in [q for q in queries if q['round']==roundnum]:
        url=API+'/search/repositories?'+urllib.parse.urlencode({'q':q['query']+' fork:false','sort':'stars','order':'desc','per_page':10})
        response=get(url); items=response.get('items',[]) if isinstance(response,dict) else []
        found=[]
        for item in items:
            if item.get('private'): continue
            name=item['full_name']; key=name.lower(); found.append(name)
            if key not in seen: seen[key]={'full_name':name,'stages':[],'discovery':[],'first_round':roundnum,'description':item.get('description'),'stars_at_search':item.get('stargazers_count')}
            if q['stage'] not in seen[key]['stages']: seen[key]['stages'].append(q['stage'])
            seen[key]['discovery'].append(q['query'])
        log.append(dict(q,url=url,total_count=response.get('total_count') if isinstance(response,dict) else None,repositories=found,error=response.get('_error') if isinstance(response,dict) else 'invalid',observed_at=datetime.datetime.now(datetime.timezone.utc).isoformat()))
        time.sleep(2.2)
    roundstats.append({'round':roundnum,'kind':'broad keyword/topic/format discovery','new_unique_repositories':len(set(seen)-before),'cumulative':len(seen)})
    save('search-log.json',log); save('discovery.json',list(seen.values())); save('rounds.json',roundstats)
# Audit all anchors, then round-robin first discoveries per stage up to 185 unique repositories.
selected=list(dict.fromkeys(n.lower() for n in seeds))
for depth in range(20):
    for stage,_,_,_ in rows:
        eligible=[k for k,v in seen.items() if stage in v['stages'] and k not in selected]
        if eligible and len(selected)<185: selected.append(eligible[0])
# No source code execution, installs, external model calls, private data or publication.
def audit(key):
    lead=seen[key]; name=lead['full_name']; meta=api('/repos/'+name)
    if meta.get('_error') or meta.get('private'):
        return {'requested_name':name,'error':meta.get('_error','private-rejected'),'examined':False}
    canonical=meta['full_name']; root='/repos/'+canonical
    commits=api(root+'/commits?per_page=1'); last=commits[0] if isinstance(commits,list) and commits else None
    if not last: return {'requested_name':name,'full_name':canonical,'examined':False,'error':'no-readable-commit'}
    sha=last['sha']; readme=api(root+'/readme?ref='+sha); text=decoded(readme)
    tree=api(root+'/git/trees/'+sha+'?recursive=1'); paths=[i['path'] for i in tree.get('tree',[]) if i.get('type')=='blob']
    licensepaths=[p for p in paths if re.search(r'(^|/)(licen[cs]e[^/]*|copying[^/]*)$',p,re.I)]
    licensepaths.sort(key=lambda p:(p.count('/'),len(p),p))
    picked=licensepaths[:3]
    for p in licensepaths:
        if re.search(r'(^|/)(ee|enterprise|commercial|apps/web|packages/core)/',p,re.I) and p not in picked and len(picked)<7: picked.append(p)
    files=[]
    for path in picked:
        obj=api(root+'/contents/'+urllib.parse.quote(path)+'?ref='+sha); content=decoded(obj)
        files.append({'path':path,'blob_sha':obj.get('sha'),'url':'https://github.com/'+canonical+'/blob/'+sha+'/'+path,'content':content,'sha256':hashlib.sha256(content.encode()).hexdigest(),'read_ok':bool(content)})
    manifests=[p for p in paths if p in ('package.json','pyproject.toml','requirements.txt','Cargo.toml','go.mod','Gemfile','composer.json','CMakeLists.txt')]
    mf=[]
    for path in manifests[:3]:
        obj=api(root+'/contents/'+path+'?ref='+sha); content=decoded(obj)
        mf.append({'path':path,'url':'https://github.com/'+canonical+'/blob/'+sha+'/'+path,'content':content[:50000],'truncated':len(content)>50000})
    recent=api(root+'/commits?per_page=100&since='+urllib.parse.quote(SINCE)); contributors=api(root+'/contributors?per_page=10')
    issues=api(root+'/issues?state=all&sort=updated&direction=desc&per_page=10')
    issue_sample=[]
    for issue in (issues if isinstance(issues,list) else []):
        if 'pull_request' in issue: continue
        item={k:issue.get(k) for k in ('number','html_url','state','created_at','updated_at','closed_at','comments')}
        item['author_association']=issue.get('author_association')
        if issue.get('comments',0) and len(issue_sample)<2:
            comments=api(root+'/issues/'+str(issue['number'])+'/comments?per_page=30')
            associated=[c for c in comments if c.get('author_association') in ('OWNER','MEMBER','COLLABORATOR') and c.get('user',{}).get('type')!='Bot'] if isinstance(comments,list) else []
            item['first_associated_reply_at_in_sample']=min([c['created_at'] for c in associated],default=None)
        issue_sample.append(item)
        if len(issue_sample)==3: break
    result={'requested_name':name,'full_name':canonical,'url':meta['html_url'],'repository_id':meta['id'],'stars':meta['stargazers_count'],'observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'description':meta.get('description'),'topics':meta.get('topics',[]),'language':meta.get('language'),'archived':meta.get('archived'),'disabled':meta.get('disabled'),'default_branch':meta.get('default_branch'),'pushed_at':meta.get('pushed_at'),'last_commit_sha':sha,'last_commit_at':last['commit']['committer']['date'],'last_commit_url':last['html_url'],'github_license_metadata':meta.get('license'),'readme':{'path':readme.get('path'),'url':'https://github.com/'+canonical+'/blob/'+sha+'/'+str(readme.get('path','README.md')),'content':text,'read_ok':bool(text)},'licenses':files,'all_license_paths':licensepaths,'tree_truncated':tree.get('truncated'),'manifests':mf,'commits_last_183_days_sample_count':len(recent) if isinstance(recent,list) else None,'commits_sample_capped':isinstance(recent,list) and len(recent)==100,'contributors_top10':[{'login':c.get('login'),'type':c.get('type'),'contributions':c.get('contributions')} for c in contributors] if isinstance(contributors,list) else None,'issue_sample':issue_sample,'discovery':lead,'examined':bool(text),'api_source':API+root}
    filename=canonical.replace('/','__')+'.json'; save(filename,result)
    return {k:v for k,v in result.items() if k not in ('readme','licenses','manifests')}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
    results=list(pool.map(audit,selected))
save('audit-index.json',results)
# Reference-graph closure rounds are separate from keyword saturation: they report exactly their bounded scope.
anchors_for_links=['AcademySoftwareFoundation/OpenTimelineIO','mifi/editly','cgwire/kitsu','gitroomhq/postiz-app','remsky/Kokoro-FastAPI','awesome-selfhosted/awesome-selfhosted']
links=[]
for name in anchors_for_links:
    path=OUT/(name.replace('/','__')+'.json')
    obj=json.loads(path.read_text()) if path.exists() else None
    if not obj:
        r=api('/repos/'+name+'/readme'); text=decoded(r); source=r.get('html_url')
    else: text=obj['readme']['content']; source=obj['readme']['url']
    for owner,repo in re.findall(r'https://github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)',text):
        if repo.endswith('.git'): repo=repo[:-4]
        if owner.lower() in ('sponsors','features','topics','orgs'): continue
        links.append({'from':name,'to':owner+'/'+repo,'source':source})
save('readme-reference-edges.json',links)
save('manifest.json',{'research_only':True,'started_at':NOW.isoformat(),'completed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'company_checkpoint':'2026-09-13T15:35:57Z','discovered_unique':len(seen),'selected_for_audit':len(selected),'examined_readme_and_commit':sum(bool(r.get('examined')) for r in results),'errors':sum(not r.get('examined') for r in results),'search_rounds':roundstats,'method':'GitHub connector-created public Actions research job; GitHub REST GET; pinned README, actual licence files, dependency manifests, recent commits and bounded contributor/issue samples; no upstream code execution','limits':['GitHub metadata license is not a legal determination','No model-weight rights inferred from code licence','No global search-saturation claim','No resource benchmark or deployment performed','Issue/contributor samples are not bus-factor certification']})
print(json.dumps(json.loads((OUT/'manifest.json').read_text()),indent=2))
