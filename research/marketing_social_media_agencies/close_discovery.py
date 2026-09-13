#!/usr/bin/env python3
"""Research-only follow-up: explicit query pagination and exact bank identities.
No upstream code is executed. No application is built, changed or deployed.
Two empty pagination rounds close only the documented bounded search frontier,
not the universe of software. Errors and GitHub's 1,000-result limit block closure.
"""
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import re
import time
import urllib.parse
import urllib.request

PIN = '26bec4050143bcb53b76f15db3159bbdc31eba55'
URL = f'https://raw.githubusercontent.com/sisodias/siso-industry-packs/{PIN}/research/marketing_social_media_agencies/collect_public_evidence.py'
with urllib.request.urlopen(URL, timeout=60) as response:
    authored_source = response.read().decode()
helpers = {'__name__': 'pinned_authored_research_helpers'}
exec(compile(authored_source, 'pinned_authored_research_helpers.py', 'exec'), helpers)
api, get = helpers['api'], helpers['get']
names = {x.lower() for x in helpers['NAMES']}
out = Path(os.environ.get('RESEARCH_OUTPUT', 'agency-discovery'))
out.mkdir(exist_ok=True)

# These complement the completed A/B/C workflow matrix; they are not a substitute.
queries = [
    ('S01,S08', '"shared inbox" "social"'),
    ('S03', '"digital asset management" "self-hosted"'),
    ('S04,S07', 'topic:social-media-scheduler'),
    ('S06', '"content approval"'),
    ('S05,S06', '"video review" "self-hosted"'),
    ('S09', '"social media analytics" "self-hosted"'),
    ('S04,S07,S08', 'topic:social-media-management'),
    ('maintainer,publishing', 'org:gitroomhq'),
    ('maintainer,email', 'user:knadh email'),
    ('maintainer,provenance', 'org:contentauth'),
]
log, seen = [], set(names)
empty_rounds = 0
closed = False
blocked = False
for page in range(1, 11):
    total_returned = 0
    successful = True
    new_in_round = set()
    for stages, query in queries:
        # Respect the conservative 10 requests/minute search budget.
        time.sleep(6.2)
        url = 'search/repositories?' + urllib.parse.urlencode({'q': query, 'sort': 'stars', 'order': 'desc', 'per_page': 100, 'page': page})
        result = api(url)
        ok = isinstance(result, dict) and 'items' in result and not result.get('incomplete_results', False)
        items = result.get('items', []) if isinstance(result, dict) else []
        count = result.get('total_count') if isinstance(result, dict) else None
        if not ok or (isinstance(count, int) and count > 1000):
            successful = False
        rows = [{'full_name': x['full_name'], 'github_id': x['id'], 'url': x['html_url'], 'description': x.get('description'), 'stars': x['stargazers_count'], 'archived': x['archived'], 'default_branch': x['default_branch'], 'license_api': x.get('license')} for x in items]
        new = {x['full_name'].lower() for x in rows} - seen
        new_in_round.update(new)
        total_returned += len(rows)
        log.append({'round': page + 3, 'stages': stages.split(','), 'query': query, 'page': page, 'per_page': 100, 'source_url': 'https://api.github.com/' + url, 'observed_at': dt.datetime.now(dt.timezone.utc).isoformat(), 'total_count': count, 'complete_response': ok, 'repositories': rows, 'new_vs_cohort_and_prior_pages': sorted(new), 'error': result.get('error') if isinstance(result, dict) else 'bad-response', 'counts_as_examined': False})
        seen.update(x['full_name'].lower() for x in rows)
        (out / 'closure-search-log.json').write_text(json.dumps(log, indent=2) + '\n')
    empty_rounds = empty_rounds + 1 if successful and total_returned == 0 else 0
    print(json.dumps({'round': page + 3, 'returned': total_returned, 'new_vs_cohort_and_pages': len(new_in_round), 'successful': successful, 'consecutive_empty_rounds': empty_rounds}), flush=True)
    if not successful:
        blocked = True
        break
    if empty_rounds >= 2:
        closed = True
        break

# Search the remaining identity-bearing layers, rather than treating index absence
# as novelty. Only primary row identities count; dependency mentions do not.
revision = '2d7d35ecbf7e1158d0a3527e1489040687ac214b'
matched = {n: {} for n in names}
sources = {}
for key, path in [('liftable_ranked', 'bank/bank_liftable_ranked.jsonl'), ('capability_top', 'bank/bank_capability_top.jsonl')]:
    url = f'https://raw.githubusercontent.com/sisodias/siso-repo-bank/{revision}/{path}'
    count, digest = 0, hashlib.sha256()
    try:
        with urllib.request.urlopen(url, timeout=90) as response:
            for line in response:
                digest.update(line)
                if not line.strip(): continue
                count += 1
                obj = json.loads(line)
                identity = next((obj[k] for k in ('full_name','repo','repository_full_name','repo_full_name','repo_name') if isinstance(obj.get(k), str)), '')
                identity = identity.lower().removeprefix('https://github.com/').rstrip('/').removesuffix('.git')
                if identity in names:
                    matched[identity].setdefault(key, []).append(obj)
        sources[key] = {'url': url, 'rows_scanned': count, 'complete': True, 'sha256': digest.hexdigest()}
    except (OSError, ValueError) as exc:
        sources[key] = {'url': url, 'rows_scanned': count, 'complete': False, 'error': type(exc).__name__}
(out / 'supplemental-bank-matches.json').write_text(json.dumps({'revision': revision, 'sources': sources, 'matches': matched}, indent=2) + '\n')
(out / 'closure-summary.json').write_text(json.dumps({'bounded_query_frontier_closed': closed, 'blocked': blocked, 'consecutive_empty_pagination_rounds': empty_rounds, 'global_exhaustion_claimed': False, 'all_queries': queries, 'responses': len(log), 'unique_names_with_initial_cohort': len(seen), 'upstream_code_executed': False}, indent=2) + '\n')
