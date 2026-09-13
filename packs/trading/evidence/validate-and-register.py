"""Validate research artifacts and atomically update only the trading registries.
No candidate software, trading APIs, private protocol or application runtime is used.
Requires the explicitly scoped GitHub Actions research branch; no third-party packages.
"""
import concurrent.futures
import datetime
import hashlib
import json
import os
import posixpath
import re
import urllib.parse
import urllib.request
from decimal import Decimal

REPO = 'sisodias/siso-industry-packs'
BRANCH = 'research/trading-20260913'
PREFIX = 'packs/trading/'
assert os.environ['GITHUB_REPOSITORY'] == REPO
assert os.environ['GITHUB_REF_NAME'] == BRANCH
SHA = os.environ['GITHUB_SHA']
assert re.fullmatch(r'[0-9a-f]{40}', SHA)
TOKEN = os.environ['GH_TOKEN']
API = 'https://api.github.com/repos/' + REPO
HEADERS = {'Authorization': 'Bearer ' + TOKEN,
           'Accept': 'application/vnd.github+json',
           'User-Agent': 'siso-trading-artifact-validation'}

def raw(path, ref=SHA):
    url = 'https://raw.githubusercontent.com/' + REPO + '/' + ref + '/' + urllib.parse.quote(path, safe='/')
    with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'siso-trading-artifact-validation'}), timeout=45) as response:
        return response.read()

def api(path, data=None, method=None):
    req = urllib.request.Request(API + path, headers=HEADERS,
        data=None if data is None else json.dumps(data).encode(), method=method)
    with urllib.request.urlopen(req, timeout=45) as response:
        return json.load(response)

def blob_sha(data):
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()

md_names = ['00-SUMMARY.md', '01-person.md', '02-workflow.md', '03-companies.md',
            '04-oss-candidates.md', '05-superapp.md', '06-value.md', 'RESEARCH-HANDOFF.md']
json_names = ['02-workflow.json', '04-oss-candidates.json', '05-assembly.json',
              '06-value.json', 'registry-update.json']
all_paths = [PREFIX + name for name in md_names + json_names]
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
    payloads = dict(zip(all_paths, executor.map(raw, all_paths)))
doc = {name: payloads[PREFIX + name].decode('utf-8') for name in md_names}
data = {name: json.loads(payloads[PREFIX + name]) for name in json_names}
assert all('Not yet researched' not in text for text in doc.values())
assert all(len(doc[name]) > 1000 for name in md_names[:7])
assert not any(re.search(r'sk-(?:proj-)?[A-Za-z0-9_-]{24,}', text) for text in doc.values())
assert not any('siso-agent-zero-protocol' in text for text in doc.values())

workflow = data['02-workflow.json']
matrix = data['04-oss-candidates.json']
assembly = data['05-assembly.json']
value = data['06-value.json']
plan = data['registry-update.json']
assert len(workflow['stages']) == 10
stage_ids = {row['id'] for row in workflow['stages']}
assert stage_ids == {'W%02d' % i for i in range(1, 11)}
assert set(re.findall(r'^\| (W\d\d) \|', doc['02-workflow.md'], re.M)) == stage_ids
assert len(re.findall(r'^\| P0[1-8] \|', doc['01-person.md'], re.M)) == 8
companies = doc['03-companies.md']
tier1 = companies.split('## Tier 1', 1)[1].split('## Tier 2', 1)[0]
tier2 = companies.split('## Tier 2', 1)[1].split('## The gap', 1)[0]
assert len([line for line in tier1.splitlines() if line.startswith('| ')]) - 1 == 10
assert len([line for line in tier2.splitlines() if line.startswith('| ')]) - 1 == 10

columns = matrix['columns']
assert len(columns) == len(set(columns))
assert all(len(row) == len(columns) for row in matrix['rows'])
rows = [dict(zip(columns, row)) for row in matrix['rows']]
by_name = {r['full_name'].lower(): r for r in rows}
assert len(rows) == len(by_name) == 110
for r in rows:
    assert r['url'] == 'https://github.com/' + r['full_name']
    datetime.date.fromisoformat(r['last_default_branch_commit_date'])
    assert r['bank_status'] in ('NEW', 'ALREADY IN THE BANK')
    assert len(r['scores']) == 5
    assert all(v is None or (type(v) is int and 0 <= v <= 5) for v in r['scores'])
    assert r['scores'][2:4] == [None, None]
    assert r['verdict'] in ('ADOPT', 'STEAL', 'STUDY', 'SKIP')
    assert r['source_page'] in matrix['source_pages']
adopted_names = {r['full_name'].lower() for r in rows if r['verdict'] == 'ADOPT'}
assert len(adopted_names) == 10
assert {c['repository'].lower() for c in assembly['components']} == adopted_names
assert len(assembly['spine']) == 6 and set(assembly['spine']) == set(workflow['data_objects'])
assert len(assembly['gaps']) == 9
assert not any(assembly['consequential_actions'].values())
assert assembly['siso_hosted_services'] == []
assert all(c['selected_release_revision'] is None for c in assembly['components'])
assert all(c['minimum_ram_gb'] is None for c in assembly['components'])
assert matrix['counts']['repositories_fully_scored_on_all_five_axes'] == 0
assert matrix['counts']['candidate_builds_executed'] == 0
assert not matrix['search_status']['two_consecutive_dry_rounds_proven']
assert not workflow['pilot']['tests_executed']
assert not value['pilot_executed']
assert all(v is None for v in value['cash_inputs'].values())
assert value['actual_stack_tax_usd_year'] is None and value['first_year_net_cash'] is None
subtotal = sum(Decimal(str(item['annual_reference'])) for item in value['reference_usd_items'])
assert subtotal == Decimal('1450.80') == Decimal(str(value['reference_stack_subtotal_usd_year']))
assert Decimal('599.40') + Decimal('240') == Decimal(str(value['reference_journal_and_caseboard_usd_year']))
for item in value['reference_usd_items']:
    assert Decimal(str(item['monthly_equivalent'])) * 12 == Decimal(str(item['annual_reference']))

# Compare manually authored metadata against the preserved, immutable collection.
# This reads existing receipts, not new upstream discovery or code execution.
source_ref = matrix['source_bundle_commit']
summary = json.loads(raw(PREFIX + 'evidence/batched-collection-summary.json', source_ref))
source_paths = [PREFIX + 'evidence/batch-%03d.json' % i for i in range(1, summary['batch_count'] + 1)]
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
    batches = list(executor.map(lambda path: json.loads(raw(path, source_ref)), source_paths))
source_records = [r for batch in batches for r in batch]
source_records.extend(json.loads(raw(PREFIX + 'evidence/supplemental-receipts.json', source_ref)))
source_by_id = {r['id']: r for r in source_records}
source_by_name = {r['full_name'].lower(): r for r in source_by_id.values()}
assert len(source_by_id) == 435
metadata_comparisons = 0
for r in rows:
    saved = source_by_name[r['full_name'].lower()]
    assert r['stars'] == saved['stars'], ('stars', r['full_name'])
    assert r['last_default_branch_commit_date'] == saved['last_commit_date'][:10], ('date', r['full_name'])
    assert r['bank_status'] == saved['bank_status'], ('bank', r['full_name'])
    metadata_comparisons += 3

# Resolve relative authored-document links at this exact source commit.
linked_paths = set()
for name, text in doc.items():
    for target in re.findall(r'\]\(([^)]+)\)', text):
        if target.startswith(('https://', 'http://', 'mailto:', '#')):
            continue
        path = target.split('#', 1)[0].split('?', 1)[0]
        if not path:
            continue
        normalized = posixpath.normpath(posixpath.join(PREFIX, urllib.parse.unquote(path)))
        assert not normalized.startswith('../') and not normalized.startswith('/')
        linked_paths.add(normalized)
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
    for content in executor.map(raw, sorted(linked_paths)):
        assert content is not None

registry_paths = ['registry/industries.jsonl', 'registry/bank-submissions.jsonl', 'registry/corrections.jsonl']
original = {path: raw(path) for path in registry_paths}
for path, content in original.items():
    assert blob_sha(content) == plan['expected_registry_blobs'][path], ('registry changed since authorized read', path)
lines = original[registry_paths[0]].splitlines(keepends=True)
indices = [i for i, line in enumerate(lines) if line.strip() and json.loads(line)['slug'] == 'trading']
assert len(indices) == 1
index = indices[0]
old_trading = json.loads(lines[index])
new_trading = dict(old_trading)
new_trading.update(plan['industry_fields'])
assert new_trading['status'] == 'partial' and new_trading['repos_examined'] == 110
assert new_trading['repos_adopted'] == 0 and new_trading['repos_selected_provisionally'] == 10
assert new_trading['deployment'] == 'client_local'
assert new_trading['base_state'] == old_trading['base_state']
assert new_trading['existing_base'] == old_trading['existing_base']
new_lines = list(lines)
new_lines[index] = (json.dumps(new_trading, ensure_ascii=True) + '\n').encode()
assert all(a == b for i, (a, b) in enumerate(zip(lines, new_lines)) if i != index)
output = {registry_paths[0]: b''.join(new_lines).decode('utf-8')}

vocabulary = json.loads(raw(PREFIX + 'evidence/bank-bank--bank_capability.jsonl.json', source_ref))
tags = {row['capability'] for row in vocabulary['rows']}
assert len(tags) == 51
proposals = plan['bank_submissions']
assert len(proposals) == 5
assert {p['full_name'].lower() for p in proposals} == {name for name in adopted_names if by_name[name]['bank_status'] == 'NEW'}
for p in proposals:
    tag = p['capability_tag']
    assert tag in tags or (tag is None and p['proposed_capability_tag'] and p['status'].startswith('taxonomy_review_required'))
    p['research_evidence'] = 'https://github.com/' + REPO + '/blob/' + SHA + '/' + PREFIX + '04-oss-candidates.json'
    p['bank_membership_scope'] = 'four compared public bank layers; not the unpublished identity corpus'
    p['production_admission'] = False
assert len(plan['corrections']) == 6
for path, additions, key in [(registry_paths[1], proposals, 'full_name'), (registry_paths[2], plan['corrections'], 'id')]:
    existing = original[path].decode('utf-8')
    existing_rows = [json.loads(line) for line in existing.splitlines() if line.strip()]
    old_keys = {r[key].lower() for r in existing_rows}
    assert len({r[key].lower() for r in additions}) == len(additions)
    assert not (old_keys & {r[key].lower() for r in additions})
    separator = '\n' if existing and not existing.endswith('\n') else ''
    output[path] = existing + separator + ''.join(json.dumps(r, ensure_ascii=True) + '\n' for r in additions)
    assert output[path].startswith(existing)

report = {
    'schema_version': '0.1.0', 'checked_source_commit': SHA,
    'validated_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'result': 'PASS', 'scope': 'research artifact integrity and registry preservation only',
    'counts': {'workflow_stages': 10, 'complaint_rows_with_links': 8, 'tier1_profiles': 10,
               'tier2_profiles': 10, 'source_repositories': 435, 'screened_rows': 110,
               'provisional_adopt': 10, 'complete_five_axis_scores': 0, 'candidate_builds': 0,
               'gaps': 9, 'new_bank_proposals': 5, 'taxonomy_held_proposals': 1, 'corrections': 6},
    'metadata_comparisons_against_saved_receipts': metadata_comparisons,
    'relative_links_resolved': len(linked_paths),
    'other_industry_lines_preserved_byte_for_byte': len(lines) - 1,
    'report_sha256': {path: hashlib.sha256(content).hexdigest() for path, content in payloads.items()},
    'not_verified': ['upstream build or dependency security', 'integrated laptop runtime or resource floor',
                     'operator demand, costs or savings', 'external link availability', 'independent complaint truth',
                     'complete maintenance/adoption scores', 'two dry discovery rounds', 'production or Library admission']
}
output[PREFIX + 'evidence/report-validation.json'] = json.dumps(report, indent=2) + '\n'
assert set(output) == set(registry_paths + [PREFIX + 'evidence/report-validation.json'])
ref_path = '/git/ref/heads/' + BRANCH
head = api(ref_path)['object']['sha']
assert head == SHA, 'Research branch advanced; stop rather than overwrite concurrent work'
parent = api('/git/commits/' + SHA)
tree = api('/git/trees', {'base_tree': parent['tree']['sha'], 'tree': [
    {'path': path, 'mode': '100644', 'type': 'blob', 'content': content}
    for path, content in output.items()]})
commit = api('/git/commits', {'message': 'research(trading): validated partial pack and scoped registry updates',
                            'tree': tree['sha'], 'parents': [SHA]})
api('/git/refs/heads/' + BRANCH, {'sha': commit['sha'], 'force': False}, 'PATCH')
assert api(ref_path)['object']['sha'] == commit['sha']
print(json.dumps({'result': 'PASS', 'commit': commit['sha'], 'counts': report['counts'],
                  'metadata_comparisons': metadata_comparisons,
                  'preserved_other_industry_lines': len(lines) - 1,
                  'changed_paths': sorted(output)}, indent=2))
