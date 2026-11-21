"""Validate and package only the final presentation and its local dependencies."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import unquote
from pypdf import PdfReader
import re, json, zipfile, hashlib

ROOT=Path(__file__).resolve().parents[1]
P=ROOT/'presentation'
class Tags(HTMLParser):
    def __init__(self):
        super().__init__(); self.links=[]; self.text=[]; self.tags=[]
    def handle_starttag(self,tag,attrs):
        self.tags.append(tag)
        for k,v in attrs:
            if k in ['href','src']: self.links.append(v)
    def handle_data(self,data): self.text.append(data)

doc=(P/'index.html').read_text(encoding='utf-8')
css=(P/'deck.css').read_text(encoding='utf-8')
js=(P/'deck.js').read_text(encoding='utf-8')
parser=Tags(); parser.feed(doc)
assert len(re.findall(r'<section\b',doc))==14
assert not set(parser.tags)&{'nav','button','select','dialog'}
assert 'speaker-note' not in doc
assert not re.search(r'P0[124589]|附錄|講稿|本專案',''.join(parser.text))
assert not re.search(r'@media\s+print|@page|fullscreen|\bnav\s*\{|\bbutton\s*\{',css)
assert not re.search(r'window\.print|requestFullscreen|location\.hash|note-dialog',js)
assert not (P/'speaker-notes.md').exists() and not (P/'slides.pdf').exists()
sources=re.findall(r'<div class="scope">(.*?)</div>',doc,re.S)
assert len(sources)==13
for s in sources:
    assert s.startswith('資料來源：')
    # Outside citation links there may only be the source label and separators.
    rest=re.sub(r'<a\b.*?</a>','',s,flags=re.S).replace('資料來源：','').replace('；','').strip()
    assert not rest, rest

links=[]
for href in parser.links:
    assert not re.match(r'https?://',href), href
    target,_,frag=href.partition('#')
    f=(P/unquote(target)).resolve()
    assert f.is_file(), f
    if frag.startswith('page='):
        assert 1<=int(frag[5:])<=len(PdfReader(f).pages), href
    links.append(str(f.relative_to(ROOT)).replace('\\','/'))
for match in re.findall(r'url\([\'"]?([^\)\'\"]+)',(P/'assets/fonts.css').read_text(encoding='utf-8')):
    assert (P/'assets'/match).is_file(), match

md_missing=[]; md_count=0
for relative in ['README.md','PROJECT_HANDOFF.md','presentation/design-spec.md','presentation/outline.md']:
    f=ROOT/relative
    for ref in re.findall(r'\]\(([^)]+)\)',f.read_text(encoding='utf-8')):
        if re.match(r'https?://|#',ref):continue
        md_count+=1
        target=(f.parent/ref.split('#')[0]).resolve()
        if target == ROOT/'process/presentation_revision2_delivery_2026-11-21.json':continue
        if not target.exists():md_missing.append([relative,ref])
assert not md_missing, md_missing

review=[]
renders=P/'renders/revision2'
for i in range(1,15):
    start=1+((i-1)//4)*4; j=(i-1)%4
    review.append({'slide':i,'screenshot':f'presentation/renders/revision2/edge-{i:02d}.png'})

files=[P/'index.html',P/'deck.css',P/'deck.js']+sorted((P/'assets').glob('*'))+sorted((ROOT/'raw/papers').glob('*.pdf'))
files=[f for f in files if f.is_file()]
readme='''AI 與人類駕駛，誰更安全？｜14頁離線簡報

解壓縮後，以桌面Edge或Chrome開啟 presentation/index.html。
下一頁：右方向鍵、PageDown或空白。上一頁：左方向鍵或PageUp。
第一頁／最後一頁：Home／End。換頁鍵不顯示於畫面。
左下資料來源可開啟raw/papers中的原始研究PDF。
請保留presentation與raw資料夾的相對位置；本機字型與授權位於presentation/assets。
本版沒有控制列、附錄、講稿或列印PDF功能。
'''
package=ROOT/'presentation-package.zip'
with zipfile.ZipFile(package,'w',compression=zipfile.ZIP_DEFLATED) as z:
    z.writestr('README.txt',readme)
    for f in files:z.write(f,f.relative_to(ROOT).as_posix())
with zipfile.ZipFile(package) as z:
    assert z.testzip() is None
    names=z.namelist()
    for local in links:assert local in names,local
    assert len(names)==len(files)+1
    assert not any(re.search(r'speaker|slides\.pdf|preview|renders|appendix',x) for x in names)
    assert z.read('presentation/index.html')==(P/'index.html').read_bytes()

checks=json.loads((ROOT/'process/presentation_revision2_checks_2026-11-21.json').read_text(encoding='utf-8'))
assert not checks['requests'] and not checks['errors']
for b in checks['browsers']:
    assert b['keyboard'] and b['removedFeatures'] and all(b['fonts'].values())
    assert not b['mobileEmulation']['horizontalOverflow']
    assert not any(s.get('sourceOverlap',False) or s['overflow'] for size in b['sizes'] for s in size['slides'])

result={'revision':2,'main_slides':14,'appendix_slides':0,'notes':False,'print_feature':False,
    'source_only_footer':True,'local_links_checked':len(links),'pdf_source_anchors_valid':True,
    'markdown_links_checked':md_count,'markdown_missing':md_missing,
    'visual_review':{'edge_html_slides':14,'screenshots':review,'print_pdf':'removed at user request; not generated or tested','physical_phone_projector':'not tested'},
    'package':{'path':package.name,'entries':names,'bytes':package.stat().st_size,
        'sha256':hashlib.sha256(package.read_bytes()).hexdigest(),'crc_error':None,'local_targets_present':True}}
(ROOT/'process/presentation_revision2_delivery_2026-11-21.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ['visual_review','package']},ensure_ascii=False))
print(json.dumps(result['package'],ensure_ascii=False))
