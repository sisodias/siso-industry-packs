#!/usr/bin/env python3
"""Public-source research collector, NOT application code or a deployment.
GET-only network operations. Never execute, build, install, or import upstream code.
The GitHub Actions token is used only with api.github.com and never saved or printed.
Outputs are research receipts, not recommendations, adoption claims, or test results.
"""
from __future__ import annotations
import base64
import concurrent.futures
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import re
import time
import urllib.error
import urllib.parse
import urllib.request

NAMES = '''gitroomhq/postiz-app
inovector/mixpost
brightbeanxyz/brightbean-studio
trypostit/trypost
getopenpost/openpost
Matthew-Selvam/Open-Dispatch
chatwoot/chatwoot
freescout-help-desk/freescout
zammad/zammad
frappe/helpdesk
uvdesk/community-skeleton
papercups-io/papercups
abhinavxd/libredesk
espocrm/espocrm
frappe/crm
twentyhq/twenty
SuiteCRM/SuiteCRM
odoo/odoo
frappe/erpnext
Dolibarr/dolibarr
idurar/idurar-erp-crm
kanboard/kanboard
Leantime/leantime
opf/openproject
makeplane/plane
go-vikunja/vikunja
wekan/wekan
documenso/documenso
docusealco/docuseal
OpenSignLabs/OpenSign
elonen/clapshot
davidguva/OpenVidReview
yusufipk/OpenFrame
ringlesoft/laravel-process-approval
w3c/web-annotation
nextcloud/server
alchemy-fr/Phraseanet
atrocore/atrocore
atrocore/atrodam
daminikhq/daminik
sveltia/sveltia-cms
penpot/penpot
FFmpeg/FFmpeg
libvips/libvips
lovell/sharp
svg/svgo
AcademySoftwareFoundation/OpenTimelineIO
glaxnimate/glaxnimate
Zulko/moviepy
OpenShot/openshot-qt
mozilla/vtt.js
umami-software/umami
plausible/analytics
matomo-org/matomo
rybbit-io/rybbit
apache/superset
metabase/metabase
allinurl/goaccess
Countly/countly-server
dlt-hub/dlt
meltano/meltano
singer-io/tap-facebook
airbytehq/airbyte
GoogleCloudPlatform/marketing-analytics-jumpstart
knadh/listmonk
mautic/mautic
dittofeed/dittofeed
pentacent/keila
Mailtrain-org/mailtrain
kimai/kimai
solidtime-io/solidtime
saeloun/miru-web
ever-co/ever-gauzy
invoiceninja/invoiceninja
crater-invoice-inc/crater
akaunting/akaunting
bigcapitalhq/bigcapital
frappe/books
baserow/baserow
teableio/teable
formbricks/formbricks
heyform/heyform
alextselegidis/easyappointments
calcom/cal.com
contentauth/c2pa-rs
exiftool/exiftool
drewnoakes/metadata-extractor
kewisch/ical.js
MatthiasValvekens/pyHanko
php-mime-mail-parser/php-mime-mail-parser
zbateson/mail-mime-parser
stalwartlabs/mail-parser
facebook/facebook-python-business-sdk
facebook/facebook-nodejs-business-sdk
intuit/QuickBooks-V3-PHP-SDK
intuit/oauth-jsclient
WhatsApp/WhatsApp-Nodejs-SDK
netflie/whatsapp-cloud-api
LibraryOfCongress/bagit-python
dtinit/data-transfer-project
jseutter/ofxparse
activepieces/activepieces
windmill-labs/windmill
n8n-io/n8n
YOURLS/YOURLS
shlinkio/shlink
getfider/fider
BookStackApp/BookStack
docmost/docmost
24eme/signaturepdf
LibreSign/libresign
vbuch/node-signpdf
CarboneIO/carbone
gotenberg/gotenberg
piotrkulpinski/open-source-alternatives
vkoul/awesome-Marketing-Analytics
awesome-selfhosted/awesome-selfhosted'''.split()
DEEP = set('chatwoot/chatwoot gitroomhq/postiz-app inovector/mixpost knadh/listmonk activepieces/activepieces documenso/documenso docusealco/docuseal elonen/clapshot invoiceninja/invoiceninja metabase/metabase formbricks/formbricks n8n-io/n8n'.lower().split())
OUT = Path(os.environ.get('RESEARCH_OUTPUT', 'agency-evidence'))
TOKEN = os.environ.get('GH_TOKEN', '')
START = dt.datetime.now(dt.timezone.utc)
SINCE = (START - dt.timedelta(days=183)).isoformat().replace('+00:00', 'Z')
OUT.mkdir(parents=True, exist_ok=True)


def get(url: str, *, json_response: bool = True) -> object:
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme != 'https' or parsed.hostname not in {'api.github.com', 'raw.githubusercontent.com'}:
        raise ValueError('Only allowlisted public-source hosts are supported')
    headers = {'User-Agent': 'siso-marketing-agencies-public-research/1', 'Accept': 'application/vnd.github+json' if json_response else 'text/plain'}
    if parsed.hostname == 'api.github.com' and TOKEN:
        headers['Authorization'] = 'Bearer ' + TOKEN
        headers['X-GitHub-Api-Version'] = '2022-11-28'
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=35) as response:
            data = response.read(8_000_001)
        if len(data) > 8_000_000:
            return {'error': 'response-size-limit', 'url': url}
        return json.loads(data) if json_response else data.decode('utf-8', errors='replace')
    except urllib.error.HTTPError as exc:
        return {'error': 'HTTP_' + str(exc.code), 'url': url}
    except (OSError, ValueError) as exc:
        return {'error': type(exc).__name__, 'url': url}


def api(path: str) -> object:
    return get('https://api.github.com/' + path)


def raw_file(repo: str, sha: str, path: str) -> dict:
    qpath = urllib.parse.quote(path, safe='/')
    url = f'https://raw.githubusercontent.com/{repo}/{sha}/{qpath}'
    text = get(url, json_response=False)
    if not isinstance(text, str):
        return {'path': path, 'url': url, 'read': False, 'error': text}
    return {'path': path, 'url': url, 'blob_url': f'https://github.com/{repo}/blob/{sha}/{qpath}', 'read': True, 'sha256': hashlib.sha256(text.encode()).hexdigest(), 'bytes': len(text.encode()), 'text': text}


def collect(name: str) -> dict:
    if not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', name):
        raise ValueError('Invalid repository name')
    observed = dt.datetime.now(dt.timezone.utc).isoformat()
    m = api('repos/' + name)
    if not isinstance(m, dict) or m.get('error') or m.get('private') is not False:
        return {'requested_name': name, 'collected_at': observed, 'status': 'blocked', 'error': m.get('error', 'not-verified-public') if isinstance(m, dict) else 'bad-response'}
    repo = m['full_name']
    r = {'requested_name': name, 'full_name': repo, 'github_id': m['id'], 'url': m['html_url'], 'collected_at': observed, 'status': 'collected_not_reviewed', 'metadata_source': 'https://api.github.com/repos/' + repo, 'stars': m['stargazers_count'], 'forks': m['forks_count'], 'archived': m['archived'], 'disabled': m.get('disabled'), 'default_branch': m['default_branch'], 'description': m.get('description'), 'language': m.get('language'), 'topics': m.get('topics', []), 'license_api': m.get('license'), 'open_issues_and_prs': m.get('open_issues_count'), 'homepage': m.get('homepage'), 'evidence_files': [], 'warnings': []}
    commits = api(f'repos/{repo}/commits?per_page=1')
    if not isinstance(commits, list) or not commits:
        r['status'] = 'blocked'; r['warnings'].append('Default-branch head could not be read'); return r
    head = commits[0]
    sha = head['sha']
    r['head_sha'] = sha
    r['last_commit'] = head['commit']['committer']['date']
    r['last_commit_source'] = head['html_url']
    root = api(f'repos/{repo}/contents/?ref={sha}')
    entries = root if isinstance(root, list) else []
    r['root_listing_source'] = f'https://api.github.com/repos/{repo}/contents/?ref={sha}'
    r['root_paths'] = [x['path'] for x in entries]
    readmes = [x['path'] for x in entries if x['type'] == 'file' and x['name'].lower().startswith('readme')]
    for path in sorted(readmes, key=lambda p: (p.lower() not in ('readme.md', 'readme.rst', 'readme'), len(p)))[:1]:
        r['evidence_files'].append(raw_file(repo, sha, path))
    if not readmes:
        rd = api(f'repos/{repo}/readme?ref={sha}')
        if isinstance(rd, dict) and rd.get('path'):
            r['evidence_files'].append(raw_file(repo, sha, rd['path']))
    license_paths = [x['path'] for x in entries if x['type'] == 'file' and re.match(r'^(licen[cs]e|copying|copyright)', x['name'], re.I)]
    if repo.lower() in DEEP or not license_paths:
        tree = api(f'repos/{repo}/git/trees/{sha}?recursive=1')
        if isinstance(tree, dict) and isinstance(tree.get('tree'), list):
            r['license_tree_truncated'] = tree.get('truncated', False)
            nested = [x['path'] for x in tree['tree'] if x['type'] == 'blob' and re.match(r'^(licen[cs]e|copying)', x['path'].split('/')[-1], re.I) and not any(p in x['path'].lower() for p in ('node_modules/', 'vendor/', 'third_party/', 'test/fixtures/'))]
            r['discovered_license_paths'] = nested
            license_paths = list(dict.fromkeys(license_paths + nested))[:20]
    for path in license_paths:
        r['evidence_files'].append(raw_file(repo, sha, path))
    if not license_paths:
        r['warnings'].append('No licence file located; permission is not inferred from a README badge')
    manifests = {'package.json', 'composer.json', 'pyproject.toml', 'Cargo.toml', 'Gemfile', 'go.mod', 'requirements.txt', 'docker-compose.yml', 'compose.yaml', 'compose.yml'}
    if repo.lower() in DEEP:
        for x in entries:
            if x['type'] == 'file' and x['name'] in manifests and x.get('size', 0) < 150_000:
                r['evidence_files'].append(raw_file(repo, sha, x['path']))
    health = api(f'repos/{repo}/commits?since={urllib.parse.quote(SINCE)}&per_page=100')
    r['commits_183d_lower_bound'] = len(health) if isinstance(health, list) else None
    r['commits_183d_capped'] = isinstance(health, list) and len(health) == 100
    contributors = api(f'repos/{repo}/contributors?per_page=30')
    r['contributor_sample_count'] = len(contributors) if isinstance(contributors, list) else None
    r['contributor_sample_capped'] = isinstance(contributors, list) and len(contributors) == 30
    r['contributor_measure_caveat'] = 'Lifetime top-contributor sample, not current bus factor or independent adoption'
    issues = api(f'repos/{repo}/issues?state=closed&sort=updated&direction=desc&per_page=20')
    r['closed_issue_sample'] = [{k: x.get(k) for k in ('number', 'title', 'html_url', 'created_at', 'closed_at', 'comments')} for x in issues if 'pull_request' not in x][:5] if isinstance(issues, list) else []
    r['issue_measure_caveat'] = 'Closed-issue sample is not first-response latency; no response SLA is established'
    safe = repo.replace('/', '__')
    (OUT / (safe + '.json')).write_text(json.dumps(r, indent=2) + '\n')
    return r


def bank_matches(rows: list[dict]) -> dict:
    names = {r.get('full_name', r['requested_name']).lower() for r in rows}
    result = {n: {'bank_best': [], 'capability_shelf': [], 'adoption_v2': [], 'contractcard': []} for n in names}
    bank = 'sisodias/siso-repo-bank'
    head = api(f'repos/{bank}/commits?per_page=1')
    if not isinstance(head, list) or not head:
        return {'complete': False, 'error': 'bank-head-unreadable', 'matches': result}
    pin = head[0]['sha']
    sources = {}
    for key, path in [('bank_best', 'bank/bank_best.jsonl'), ('capability_shelf', 'capability-shelf/source-registry.jsonl'), ('adoption_v2', 'bank/bank_adoption_v2.jsonl'), ('contractcard', 'bank/bank_contractcard.jsonl')]:
        url = f'https://raw.githubusercontent.com/{bank}/{pin}/{path}'
        total, digest = 0, hashlib.sha256()
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'siso-marketing-agencies-public-research/1'})
            with urllib.request.urlopen(req, timeout=90) as response:
                for line in response:
                    digest.update(line)
                    if not line.strip():
                        continue
                    total += 1
                    obj = json.loads(line)
                    # The shelf stores repo identities in its nested source object; inspect all strings exactly.
                    def identities(value):
                        if isinstance(value, dict):
                            for v in value.values(): yield from identities(v)
                        elif isinstance(value, list):
                            for v in value: yield from identities(v)
                        elif isinstance(value, str):
                            yield value.lower().removeprefix('https://github.com/').rstrip('/').removesuffix('.git')
                    matched = set(identities(obj)) & names
                    for name in matched:
                        result[name][key].append(obj)
            sources[key] = {'url': url, 'rows_scanned': total, 'sha256': digest.hexdigest(), 'complete': True}
        except (OSError, ValueError) as exc:
            sources[key] = {'url': url, 'rows_scanned': total, 'complete': False, 'error': type(exc).__name__}
    return {'revision': pin, 'sources': sources, 'complete': all(v['complete'] for v in sources.values()), 'matches': result, 'fame_gap_note': 'Retain raw values. Foundry load_adoption_signal.py defines high fame_gap as adoption outrunning stars, not the reverse.'}


def main() -> None:
    assert len(NAMES) == len(set(n.lower() for n in NAMES))
    rows = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        for r in pool.map(collect, NAMES):
            rows.append(r)
            print(r['requested_name'], r['status'], flush=True)
    banks = bank_matches(rows)
    (OUT / 'bank-matches.json').write_text(json.dumps(banks, indent=2) + '\n')
    compact = [{k: v for k, v in r.items() if k != 'evidence_files'} | {'evidence_files': [{k: v for k, v in f.items() if k != 'text'} for f in r.get('evidence_files', [])]} for r in rows]
    (OUT / 'repository-receipts.json').write_text(json.dumps(compact, indent=2) + '\n')
    summary = {'started_at': START.isoformat(), 'finished_at': dt.datetime.now(dt.timezone.utc).isoformat(), 'requested': len(NAMES), 'public_repositories_collected': len({r['github_id'] for r in rows if r.get('head_sha')}), 'blocked': [r['requested_name'] for r in rows if r['status'] == 'blocked'], 'bank_scan_complete': banks['complete'], 'review_status': 'collected_not_reviewed', 'upstream_code_executed': False, 'application_code_written': False}
    (OUT / 'audit-summary.json').write_text(json.dumps(summary, indent=2) + '\n')
    print(json.dumps(summary), flush=True)


if __name__ == '__main__':
    main()
