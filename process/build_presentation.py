"""Build the 14-slide, keyboard-only offline presentation. No notes or print UI."""
from pathlib import Path
import re, json

ROOT = Path(__file__).resolve().parents[1]
P = ROOT / 'presentation'
samples = re.findall(r'<section\b.*?</section>', (P/'preview.html').read_text(encoding='utf-8'), re.S)
papers = {p.name[:3]: p.name for p in (ROOT/'raw/papers').glob('*.pdf')}
AUTHORS = {'P01':'Kusano 等（2025）', 'P02':'Di Lillo 等（2024）',
           'P04':'Scanlon 等（2024）', 'P05':'Scanlon 等（2025）',
           'P08':'Koopman 與 Wagner（2017）', 'P09':'Galéra 等（2012）'}

def source(pid, page, locator=''):
    label = AUTHORS[pid] + ('，'+locator if locator else '')
    return f'<a href="../raw/papers/{papers[pid]}#page={page}" target="_blank" rel="noopener">{label}</a>'

def table(head, rows):
    return '<table><thead><tr>'+''.join('<th>'+x+'</th>' for x in head)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+str(x)+'</td>' for x in row)+'</tr>' for row in rows)+'</tbody></table>'

slides=[]
def footer(ref):
    return (f'<div class="scope">資料來源：{ref}</div>' if ref else '')+'<footer><span class="page-no"></span></footer>'

def add(id,title,deck,body,ref,tag='比較安全的方式'):
    slides.append(f'<section class="slide" id="{id}" hidden><div class="topline"><span>{tag}</span><span class="edition">AI 與駕駛安全</span></div><h2>{title}</h2><p class="deck">{deck}</p><div class="content">{body}</div>{footer(ref)}</section>')

def sample(index,id,ref,changes=()):
    s=samples[index]
    s=re.sub(r'id="[^"]+"',f'id="{id}"',s,count=1)
    s=re.sub(r'aria-label="[^"]*測試"','aria-label="教學投影片"',s,count=1)
    s=re.sub(r'<div class="scope">.*?</div>', '', s, flags=re.S)
    s=re.sub(r'<footer>.*?</footer>', footer(ref), s, flags=re.S)
    s=re.sub(r'<span class="edition">.*?</span>', '<span class="edition">AI 與駕駛安全</span>',s)
    for old,new in changes:
        assert old in s, old
        s=s.replace(old,new)
    slides.append(s)

sample(0,'s01','')
add('s02','先看道路結果，再理解風險從何而來','六篇研究提供三種視角：實際結果、比較方法，以及人與系統的風險。',
    '<div class="research-route"><div><span class="route-no">01</span><h3>實際結果</h3><p>道路事故<br><strong>約5,670萬英里</strong></p><p>責任理賠<br><strong>約387萬英里</strong></p></div><div><span class="route-no">02</span><h3>比較方法</h3><p>人類事故基準<br>如何選擇與調整？</p><p>研究品質清單<br>哪些條件要一致？</p></div><div><span class="route-no">03</span><h3>風險來源</h3><p>人類內在分心<br><strong>955名受傷駕駛</strong></p><p>系統失效<br>如何監測與安全處置？</p></div></div>'
    '<p class="takeaway">道路與理賠研究來自同一 Waymo 車隊，部分時期重疊，里程不能相加。</p>',
    '；'.join(source(pid,1) for pid in ['P01','P02','P04','P05','P09','P08']), '研究資料 / 三種視角')

add('s03','主要道路證據來自美國的 Waymo 車隊','Waymo 是提供自動駕駛叫車服務的業者；這裡比較車內沒有駕駛員的營運。',
    '<div class="geo-layout"><div><h3>四個研究地區</h3><p class="body-copy">鳳凰城、舊金山<br>道路與理賠研究都涵蓋</p><p class="body-copy">洛杉磯、奧斯汀<br>另納入道路事故研究</p><p class="body-copy geo-period">道路研究：一般道路，排除高速公路<br>累積里程至2025年1月</p></div><div class="geo-plot" role="img" aria-label="美國城市地理定位示意，非營運邊界。舊金山與洛杉磯在加州，鳳凰城在亞利桑那州，奧斯汀在德州。"><span class="geo-direction">北 ↑　地理定位示意・非營運邊界</span><span class="city sf">● 舊金山<small>加州</small></span><span class="city la">● 洛杉磯<small>加州</small></span><span class="city phx">● 鳳凰城<small>亞利桑那州</small></span><span class="city aus">● 奧斯汀<small>德州</small></span><span class="geo-west">美國西部</span><span class="geo-east">中南部</span></div></div>',
    source('P01',10,'PDF 5–7、10–11，表2')+'；'+source('P02',3,'PDF 3–4'), '研究場景 / 業者與地區')

add('s04','先分清楚：駕駛責任交給誰？','名稱相似的功能，可能需要完全不同的人類參與。',
    '<div class="responsibility"><div><p class="label">需要人類監督</p><h3>駕駛輔助</h3><p>人類持續注意道路<br>並負責駕駛與應變</p></div><div class="selected"><p class="label">接下來的比較對象</p><h3>無車內駕駛服務</h3><p>在指定營運條件內<br>由系統負責駕駛與處置</p></div></div><p class="takeaway">Waymo 的研究結果，適用於指定地區與道路條件下的無車內駕駛營運。</p>',
    source('P01',6,'PDF 2、6、19–20、26'))

add('s05','比較事故次數，也要看行駛距離','教學假設：乙車隊出事較多，但也跑了更長的距離。',
    table(['車隊','涉事車次','行駛距離','每百萬英里涉及率'],[['甲','1次','100萬英里','<strong>1</strong>'],['乙','2次','400萬英里','<strong>0.5</strong>']])+
    '<div class="formula">每百萬英里事故涉及率<br><strong>＝ 涉事車次 ÷ 行駛英里 × 100萬</strong></div><p class="definition">「涉事車次」數的是車輛涉及事故的次數；不代表負肇責，也不是傷者人數。</p>',
    source('P01',8,'PDF 8–10'))

add('s06','公平比較需要相近的行駛條件','換成相同里程後，還要確認環境與記錄方式是否可比。',
    '<div class="questions"><div><b>01</b><h3>在哪裡、走什麼路？</h3><p>地區、道路與車種<br>是否相近？</p></div><div><b>02</b><h3>哪些事件算事故？</h3><p>擦撞、受傷與重傷<br>使用不同門檻</p></div><div><b>03</b><h3>兩邊怎麼記錄？</h3><p>自動通報與警察紀錄<br>可能有不同漏報</p></div></div><p class="takeaway">接下來的道路研究調整了地區、道路、行駛位置與部分漏報；<br>時段、天候等仍未完全對齊，因此不能把差異全部歸因於 AI。</p>',
    source('P04',11,'PDF 11–16')+'；'+source('P05',6,'PDF 6–12')+'；'+source('P01',5,'PDF 5–10、18–20'))

sample(1,'s07',source('P01',12,'PDF 10–12，表2–4'),[
    ('Waymo 的受傷事故涉及率較低','Waymo 的受傷相關事故涉及率較低'),
    ('比較相同行駛距離，涉及有人回報受傷事故的頻率。','四區一般道路，累積至2025年1月；比較「有人回報受傷」的事故涉及率。'),
    ('人類基準經作者調整；這不是乘客個人的受傷率。','人類多為2022年資料，基準經研究者調整；這不是乘客個人的受傷率。'),
    ('95% 信賴區間：71%–85%','95% 信賴區間：71%–85%<br><span class="ci-explain">區間呈現估計的精確程度</span>')])

def bars(human,waymo,maxval,ticks):
    x=lambda v:150+float(v)/maxval*480
    g=''.join(f'<path d="M{x(v)} 35V245" stroke="#ddd8ce"/><text x="{x(v)}" y="280" class="axis">{v:g}</text>' for v in ticks)
    return f'<svg class="bar-svg" viewBox="0 0 760 310" role="img" aria-label="人類基準{human}，Waymo {waymo}涉事車次每百萬英里，橫軸從零起算">{g}<text x="0" y="102" class="chart-label">人類基準</text><text x="0" y="202" class="chart-label">Waymo</text><rect x="150" y="62" width="{x(human)-150}" height="58" fill="#b66c50"/><rect x="150" y="162" width="{x(waymo)-150}" height="58" fill="#557365"/><text x="{x(human)+12}" y="104" class="chart-number">{human}</text><text x="{x(waymo)+12}" y="204" class="chart-number">{waymo}</text><path d="M150 245H630" stroke="#8a8d83"/></svg>'

add('s08','Waymo 在鳳凰城的被追撞涉及率較高','整體較低，不代表每種情境都較低：這裡同樣觀察「有人回報受傷」。',
    '<div class="data-layout"><div><p class="unit">涉事車次／百萬英里</p>'+bars('0.22','0.48',.6,[0,.2,.4,.6])+'<p class="chart-note">後車 → 撞上前車；此處統計前車被撞，不代表前車負肇責。</p></div><aside class="finding"><p class="finding-label">作者報告的增幅</p><div class="big-number">117<span>%</span></div><p class="interval">95%信賴區間<br>11%–281%</p></aside></div><p class="method-note">這是追加的細分分析：人類基準假設追撞與被追撞各半；<br>未校正同時檢驗多個細組所增加的偶然顯著機會。</p>',
    source('P01',40,'PDF 20、39–40，表A9'), '真實道路 / 被追撞情境')

add('s09','疑似重傷以上的涉及率也較低','Waymo 只觀察到2次事件，減幅估計的區間較寬。',
    '<div class="ci-story"><div class="count"><strong>2</strong><span>次觀察事件</span></div><div class="ci-panel"><p>作者報告的減幅及95%信賴區間</p><div class="ci-line"><i style="left:39%;width:60%"></i><b style="left:85%"></b><span style="left:39%">39%</span><span style="left:85%">85%</span><span style="left:99%">99%</span></div><div class="ci-axis"><span>0%　無減幅</span><span>100%</span></div><p class="ci-key">圓點：減幅估計　　線段：估計區間</p></div></div><p class="takeaway">這項指標合併「疑似重傷與死亡」，不能解讀成死亡率降低85%。</p>',
    source('P01',11,'PDF 11–12，表3–4；PDF 15、20、35'), '真實道路 / 罕見嚴重事件')

def dotchart():
    x=lambda v:155+v/4*580
    s='<svg class="dot-svg" viewBox="0 0 1000 320" role="img" aria-label="人類3.26，95%信賴區間3.24至3.27；Waymo 0.78，區間0.16至2.27，件每百萬英里。">'
    for v in range(5):
        s+=f'<path d="M{x(v)} 40V240" stroke="#ddd8ce"/><text x="{x(v)}" y="280" class="axis">{v}</text>'
    for i,(label,val,lo,hi,color) in enumerate([('人類基準',3.26,3.24,3.27,'#b66c50'),('Waymo',.78,.16,2.27,'#557365')]):
        y=95+i*105
        s+=f'<text x="0" y="{y+9}" class="chart-label">{label}</text><path d="M{x(lo)} {y}H{x(hi)} M{x(lo)} {y-9}V{y+9} M{x(hi)} {y-9}V{y+9}" stroke="{color}" stroke-width="4"/><circle cx="{x(val)}" cy="{y}" r="9" fill="{color}"/><text x="780" y="{y+8}" class="rate-text">{val:g} [{lo:g}, {hi:g}]</text>'
    return s+'</svg>'

add('s10','Waymo 的第三方財損責任理賠較少','鳳凰城與舊金山，約387萬英里的無車內駕駛資料；比較對他人的財損責任理賠。',
    '<p class="unit">件／百萬英里　　點：各率估計　線及方括號：各率95%信賴區間</p>'+dotchart()+'<p class="chart-note">Waymo總資料期2018–2023年，人類2016–2021年。<br>理賠頻率不是所有事故率，也不是法院肇責判定。</p>',
    source('P02',5,'PDF 3–6，圖2C'), '保險資料 / 第三方財損')

add('s11','眼睛看路，心裡仍可能想著別的事','法國單一醫院的955名受傷駕駛：事故後訪談分心情況，再依評分區分責任。',
    '<div class="attention"><div class="attention-phrase"><span>眼睛看路</span><em>心裡想著別的事</em><small>內在分心的教學示意</small></div><div><p class="label">比較已出事故的受傷駕駛</p><h3>強烈分心</h3><p class="body-copy">與較高的事故責任勝算相關<br><small>即「有責任／無責任」機率的比值較高</small></p><p class="body-copy muted">較弱分心、合併所有分心<br>均未達統計顯著</p></div></div><p class="takeaway">研究包含不同車種，也沒有自動駕駛對照，無法推算 AI 能避免多少事故。</p>',
    source('P09',7,'PDF 1–3、5–7'), '人類因素 / 內在分心')

sample(2,'s12',source('P08',2,'接受稿 PDF 2–6'),[
    ('安全設計要涵蓋正常駕駛，也要考慮故障與陌生情況。','安全設計要涵蓋正常駕駛，也要考慮故障與陌生情況；下圖為概念示意。'),
    ('</div></div>\n ', '</div></div>\n <p class="concept-context">這是安全設計的概念，並非 Waymo 實際架構，也未量測該車隊的失效比例。</p>\n ')])

add('s13','兩種記錄管道，仍來自同一車隊','道路事故與保險理賠提供互補視角；不同論文不等於獨立車隊重現。',
    '<div class="evidence-map"><div class="result-pair"><div><h3>道路事故研究</h3><p>作者全為 Waymo 員工</p></div><span class="dependency">同一車隊<br>部分時期重疊</span><div><h3>責任理賠研究</h3><p>Swiss Re／Waymo 合作</p></div></div><div class="support-row"><p><strong>比較方法</strong><br>檢查資料是否可比</p><p><strong>人類分心</strong><br>理解人的注意力風險</p><p><strong>系統安全</strong><br>理解機器的失效風險</p></div></div><p class="takeaway">公開事故資料可供部分核對，原始理賠資料未公開；<br>其他方法與風險研究，也沒有新增車隊安全成效樣本。</p>',
    source('P01',22,'PDF 22、26')+'；'+source('P02',6,'PDF 6')+'；'+source('P05',14,'PDF 14'), '證據解讀 / 作者與資料關係')

add('s14','研究中的 Waymo，兩類安全指標較好','在各研究涵蓋的無車內駕駛營運條件下，兩項結果都低於各自的人類基準。',
    '<div class="conclusion"><p><span>道路事故</span>受傷相關事故涉及率較低</p><p><span>責任理賠</span>第三方財損理賠頻率較低</p></div><p class="closing">回答「誰更安全」，需要一起說清楚<br><strong>哪個系統、什麼條件、哪一種安全指標。</strong></p>',
    source('P01',12,'PDF 12，表4')+'；'+source('P02',5,'PDF 5，圖2C'), '回答標題 / 研究支持的結論')

assert len(slides)==14
for i,s in enumerate(slides):
    slides[i]=s.replace('<span class="page-no"></span>',f'<span class="page-no">{i+1:02d} / 14</span>')
doc='<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>AI 與人類駕駛，誰更安全？</title><link rel="stylesheet" href="assets/fonts.css"><link rel="stylesheet" href="deck.css"></head><body><main aria-label="教學簡報">'+''.join(slides)+'</main><script src="deck.js"></script></body></html>'
(P/'index.html').write_text(doc,encoding='utf-8')
print(json.dumps({'slides':len(slides),'appendix':0,'notes':False,'controls':False,'print':False}))
