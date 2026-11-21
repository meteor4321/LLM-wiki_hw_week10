"""Download public research PDFs; preserve bytes and record provenance."""
import concurrent.futures
import hashlib
import json
from pathlib import Path
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
ITEMS = [
    ('P01_kusano_2025_56_7m', 'papers', [
        'https://www.tandfonline.com/doi/pdf/10.1080/15389588.2025.2499887',
        'https://storage.googleapis.com/waymo-uploads/files/documents/safety/Safety%20Impact%20Crash%20Type%20Manuscript.pdf']),
    ('P02_dilillo_2024_insurance', 'papers', [
        'https://pmc-oa-opendata.s3.amazonaws.com/PMC11305169.1/PMC11305169.1.pdf']),
    ('P04_scanlon_2024_benchmarks', 'papers', [
        'https://arxiv.org/pdf/2312.13228v2']),
    ('P05_scanlon_2025_rave', 'papers', [
        'https://research.chalmers.se/publication/544909/file/544909_Fulltext.pdf']),
]

def fetch(item):
    ident, group, urls = item
    record = {'id': ident, 'acquired_date_taipei': '2026-11-21', 'attempts': []}
    for url in urls:
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Academic source verification'})
            with urllib.request.urlopen(req, timeout=45) as response:
                data = response.read()
                final_url = response.url
                content_type = response.headers.get('Content-Type')
            if not data.startswith(b'%PDF-'):
                raise ValueError('Response is not a PDF: ' + str(content_type))
            dest = ROOT / 'raw' / group / (ident + '.pdf')
            dest.write_bytes(data)
            record.update(path=str(dest.relative_to(ROOT)), url=url, final_url=final_url,
                          bytes=len(data), sha256=hashlib.sha256(data).hexdigest(), content_type=content_type)
            break
        except Exception as exc:
            record['attempts'].append({'url': url, 'error': str(exc)})
    return record

if __name__ == '__main__':
    manifest = ROOT / 'sources' / 'download_manifest.json'
    previous = json.loads(manifest.read_text(encoding='utf-8')) if manifest.exists() else []
    completed = {r['id']: r for r in previous if r.get('path')}
    pending = [item for item in ITEMS if item[0] not in completed]
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        new_results = list(pool.map(fetch, pending))
    old = {r['id']: r for r in previous}
    for r in new_results:
        r['attempts'] = old.get(r['id'], {}).get('attempts', []) + r['attempts']
        completed[r['id']] = r
    # Preserve candidates acquired in later selection rounds.
    results_by_id = {r['id']: r for r in previous}
    results_by_id.update(completed)
    results = list(results_by_id.values())
    manifest.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding='utf-8')
    for result in results:
        print(json.dumps(result, ensure_ascii=False))
