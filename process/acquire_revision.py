"""Acquire the independently authored candidates found during selection revision."""
import concurrent.futures
import json
import re
from pathlib import Path
import urllib.request
import xml.etree.ElementTree as ET
from acquire_candidates import fetch, ROOT

def pmc_pdf(pmcid):
    base = 'https://pmc-oa-opendata.s3.amazonaws.com/'
    with urllib.request.urlopen(base + '?list-type=2&prefix=' + pmcid, timeout=30) as r:
        xml = r.read()
    (ROOT / 'extracted' / (pmcid + '_file_listing.xml')).write_bytes(xml)
    keys = [node.text for node in ET.fromstring(xml).iter()
            if node.tag.endswith('}Key') and re.fullmatch(pmcid + r'\.\d+/' + pmcid + r'\.\d+\.pdf', node.text)]
    if len(keys) != 1:
        raise ValueError('Check PMC PDF versions manually: ' + str(keys))
    return base + keys[0]

if __name__ == '__main__':
    items = [
        ('P07_dingus_2016_human_risk', 'papers', [
            'https://www.pnas.org/doi/pdf/10.1073/pnas.1513271113']),
        ('P08_koopman_2017_safety', 'papers', [
            'https://users.ece.cmu.edu/~koopman/pubs/koopman17_ITS_av_safety.pdf']),
    ]
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        results = list(pool.map(fetch, items))
    manifest = ROOT / 'sources' / 'download_manifest.json'
    records = json.loads(manifest.read_text(encoding='utf-8'))
    old = {record['id']: record for record in records}
    for record in results:
        old[record['id']] = record
        print(json.dumps(record, ensure_ascii=False))
    manifest.write_text(json.dumps(list(old.values()), ensure_ascii=False, indent=2), encoding='utf-8')
