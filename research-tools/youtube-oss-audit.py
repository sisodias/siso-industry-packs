"""Bounded PUBLIC research evidence recovery, not application code.
No upstream programs, installers, models, account operations or private sources run.
Uses the job's ephemeral read-only token only for api.github.com; never prints it.
Each completed record is saved immediately. No search-count masquerades as examination.
Commercial map precedes this continuation: commit 585c90dfdf1750063730f0c7845a140383eb4aa7.
"""
import os,json,time,base64,hashlib,pathlib,re,datetime,urllib.request,urllib.parse,urllib.error,concurrent.futures
OUT=pathlib.Path('oss-evidence'); OUT.mkdir(exist_ok=True)
NOW=datetime.datetime.now(datetime.timezone.utc)
SINCE=(NOW-datetime.timedelta(days=183)).isoformat()
TOKEN=os.environ.get('GH_TOKEN','')
def request(url,payload=None):
    headers={'User-Agent':'SISO-public-source-research','Accept':'application/vnd.github+json'}
    if url.startswith('https://api.github.com/') and TOKEN: headers['Authorization']='Bearer '+TOKEN
    if payload is not None: headers['Content-Type']='application/json'
    data=json.dumps(payload).encode() if payload is not None else None
    for attempt in range(2):
        try:
            with urllib.request.urlopen(urllib.request.Request(url,data=data,headers=headers),timeout=25) as r:
                b=r.read()
                return json.loads(b) if url.startswith('https://api.github.com/') else b.decode('utf-8','replace')
        except urllib.error.HTTPError as e:
            if e.code in (429,502,503) and attempt==0: time.sleep(3); continue
            return {'error':e.code,'source':url}
        except Exception as e:
            if attempt==0: time.sleep(1); continue
            return {'error':type(e).__name__,'source':url}
def save(path,obj):
    temp=OUT/(path+'.tmp'); temp.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n'); temp.replace(OUT/path)
def raw(name,sha,path):
    url='https://raw.githubusercontent.com/'+name+'/'+sha+'/'+urllib.parse.quote(path,safe='/')
    r=request(url)
    return {'path':path,'url':'https://github.com/'+name+'/blob/'+sha+'/'+path,'raw_url':url,'content':r if isinstance(r,str) else None,'error':r if not isinstance(r,str) else None,'sha256':hashlib.sha256(r.encode()).hexdigest() if isinstance(r,str) else None}
GROUPS={
'S01':'chatwoot/chatwoot twentyhq/twenty frappe/crm freescout-help-desk/freescout zammad/zammad knadh/listmonk',
'S02':'yt-dlp/yt-dlp pytube/pytube pytubefix/pytubefix jdepoix/youtube-transcript-api GeneralMills/pytrends searxng/searxng FreshRSS/FreshRSS miniflux/v2 ArchiveBox/ArchiveBox meeb/tubesync tubearchivist/tubearchivist iv-org/invidious',
'S03':'nyousefi/Fountain screenplain/screenplain simonw/llm ollama/ollama ggml-org/llama.cpp',
'S04':'OHF-Voice/piper1-gpl rhasspy/piper hexgrad/kokoro hexgrad/misaki remsky/Kokoro-FastAPI coqui-ai/TTS idiap/coqui-ai-TTS Blaizzy/mlx-audio FunAudioLLM/CosyVoice SWivid/F5-TTS fishaudio/fish-speech resemble-ai/chatterbox canopyai/Orpheus-TTS suno-ai/bark myshell-ai/OpenVoice rany2/edge-tts espeak-ng/espeak-ng k2-fsa/sherpa-onnx',
'S05':'mediacms-io/mediacms immich-app/immich photoprism/photoprism nextcloud/server rclone/rclone seaweedfs/seaweedfs minio/minio openverse/openverse musicbrainz/picard beetbox/beets acoustid/chromaprint worldveil/dejavu exiftool/exiftool',
'S06':'FFmpeg/FFmpeg PyAV-Org/PyAV Zulko/moviepy mltframework/mlt mltframework/shotcut OpenShot/libopenshot OpenShot/openshot-qt KDE/kdenlive olive-editor/olive OpenCut-app/OpenCut remotion-dev/remotion motion-canvas/motion-canvas mifi/editly mifi/lossless-cut walterlow/freecut trykimu/videoeditor WebAV-Tech/WebAV ffmpegwasm/ffmpeg.wasm AcademySoftwareFoundation/OpenTimelineIO',
'S07':'SubtitleEdit/subtitleedit m-bain/whisperX SYSTRAN/faster-whisper ggml-org/whisper.cpp openai/whisper linto-ai/whisper-timestamped jianfch/stable-ts pyannote/pyannote-audio libass/libass Aegisub/Aegisub videojs/vtt.js cdown/srt glut23/webvtt-py tkarabela/pysubs2 ImageMagick/ImageMagick libvips/libvips lovell/sharp penpot/penpot tmoroney/auto-subs',
'S08':'cgwire/kitsu cgwire/zou alicevision/Meshroom AcademySoftwareFoundation/OpenImageIO AcademySoftwareFoundation/OpenColorIO',
'S09':'gitroomhq/postiz-app inovector/mixpost postflow/postflow socioboard/Socioboard-5.0 porjo/youtubeuploader tokland/youtube-upload googleapis/google-api-python-client googleapis/google-api-nodejs-client googleapis/google-api-go-client bluenviron/mediamtx',
'S10':'RayVentura/ShortGPT FujiwaraChoki/MoneyPrinter FujiwaraChoki/MoneyPrinterV2 harry0703/MoneyPrinterTurbo WyattBlue/auto-editor Breakthrough/PySceneDetect modelscope/FunClip zhouxiaoka/autoclip Anil-matcha/AI-Youtube-Shorts-Generator SamurAIGPT/AI-Youtube-Shorts-Generator google-ai-edge/mediapipe',
'S11':'ThioJoe/YT-Spammer-Purge youtube/api-samples metabase/metabase apache/superset umami-software/umami',
'S12':'invoiceninja/invoiceninja akaunting/akaunting frappe/erpnext frappe/books InvoicePlane/InvoicePlane TryGhost/Ghost frappe/lms moodle/moodle ContentAuthenticity/c2pa-rs ContentAuthenticity/c2patool w3c/odrl w3c/webvtt w3c/ttml2'}
leads={}
for stage,names in GROUPS.items():
    for name in names.split(): leads.setdefault(name,{'stages':[]})['stages'].append(stage)
save('input-leads.json',leads)
# First metadata only: do not read or preserve private source content even if an input changed visibility.
metadata={}; errors=[]
names=list(leads)
for start in range(0,len(names),12):
    batch=names[start:start+12]; parts=[]
    for i,name in enumerate(batch):
        owner,repo=name.split('/')
        parts.append('r%d:repository(owner:%s,name:%s){nameWithOwner url isPrivate isArchived stargazerCount description updatedAt pushedAt primaryLanguage{name} licenseInfo{spdxId name} defaultBranchRef{name target{... on Commit{oid committedDate history(first:1,since:%s){totalCount}}}}}'%(i,json.dumps(owner),json.dumps(repo),json.dumps(SINCE)))
    response=request('https://api.github.com/graphql',{'query':'query {'+' '.join(parts)+' rateLimit{remaining resetAt}}'})
    data=response.get('data',{}) or {}
    if response.get('errors'): errors.extend(response['errors'])
    for i,name in enumerate(batch):
        meta=data.get('r'+str(i))
        if not meta or meta.get('isPrivate'):
            errors.append({'requested_name':name,'error':'no-readable-public-repository','examined':False}); continue
        metadata[name]=meta
    save('metadata-progress.json',metadata); save('errors.json',errors)
    print('Public metadata',len(metadata),'of',len(names),flush=True)
# Source reads use raw public URLs without authorization. REST tree/README endpoints only after public check.
def audit(item):
    requested,meta=item; canonical=meta['nameWithOwner']; branch=meta.get('defaultBranchRef')
    if not branch: return {'requested_name':requested,'examined':False,'error':'empty-default-branch'}
    commit=branch['target']; sha=commit['oid']; root='https://api.github.com/repos/'+canonical
    tree=request(root+'/git/trees/'+sha+'?recursive=1')
    paths=[x['path'] for x in tree.get('tree',[]) if x.get('type')=='blob']
    root_paths=[p for p in paths if '/' not in p]
    readmes=sorted([p for p in root_paths if re.match(r'^readme(?:\.|$)',p,re.I)],key=lambda p:(p.lower()!='readme.md',len(p)))
    readme=raw(canonical,sha,readmes[0]) if readmes else None
    if not readme or not readme.get('content'):
        rd=request(root+'/readme?ref='+sha)
        if rd.get('encoding')=='base64':
            text=base64.b64decode(rd.get('content','')).decode('utf-8','replace')
            readme={'path':rd.get('path'),'url':rd.get('html_url'),'content':text,'sha256':hashlib.sha256(text.encode()).hexdigest()}
    licpaths=[p for p in paths if re.search(r'(^|/)(licen[cs]e[^/]*|copying[^/]*)$',p,re.I)]
    rootlic=[p for p in licpaths if '/' not in p]
    chosen=sorted(rootlic)[:6]
    for p in sorted(licpaths,key=lambda p:(p.count('/'),len(p),p)):
        if p not in chosen and (len(chosen)<2 or re.search(r'(^|/)(ee|enterprise|commercial)/',p,re.I)) and len(chosen)<9: chosen.append(p)
    licences=[raw(canonical,sha,p) for p in chosen]
    manifests=[raw(canonical,sha,p) for p in root_paths if p in ('package.json','pyproject.toml','requirements.txt','Cargo.toml','go.mod','composer.json','Gemfile')][:3]
    result={'requested_name':requested,'full_name':canonical,'url':meta['url'],'stages':leads[requested]['stages'],'observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'metadata':meta,'last_commit_sha':sha,'last_commit_at':commit['committedDate'],'last_commit_url':meta['url']+'/commit/'+sha,'stars':meta['stargazerCount'],'readme':readme,'licenses':licences,'license_paths':licpaths,'license_scope':'root and selected explicit enterprise licences; model weights and transitive/build-selected licences are separate','manifests':manifests,'tree_truncated':tree.get('truncated'),'tree_error':tree.get('error'),'examined':bool(readme and readme.get('content')),'verification_scope':'public metadata + pinned README + root LICENSE/COPYING when present; research examination, not runtime/adoption certification'}
    save(canonical.replace('/','__')+'.json',result)
    print('Saved',canonical,'examined',result['examined'],'licences',len(licences),flush=True)
    return {k:v for k,v in result.items() if k not in ('readme','licenses','manifests')}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
    results=list(pool.map(audit,metadata.items()))
save('audit-index.json',results)
save('receipt.json',{'started_at':NOW.isoformat(),'finished_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'requested_repos':len(leads),'public_metadata_records':len(metadata),'readme_examined':sum(x['examined'] for x in results),'examined_definition':'public metadata, default-branch commit, pinned README reviewed; licence files preserved for researcher judgment, absence not fabricated','errors':errors,'saturation_claim':False,'new_discovery_rounds':0,'prior_discovery':'run 34766404284: 509 leads, three broad rounds; not 509 audits','application_code_executed':False,'deployment_performed':False})
print('FINISHED',sum(x['examined'] for x in results),'readable repositories',flush=True)
