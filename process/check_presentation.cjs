const { chromium } = require('C:/Users/kingd/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const fs = require('fs');
const path = require('path');
const {pathToFileURL} = require('url');
const root=path.resolve(__dirname,'..');
const out=path.join(root,'presentation','renders','revision2');
fs.mkdirSync(out,{recursive:true});
const url=pathToFileURL(path.join(root,'presentation','index.html')).href;
(async()=>{
  const results={revision:2,localFile:true,offline:true,browsers:[],requests:[],errors:[]};
  for(const [name,exe] of [['Edge','C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'],['Chrome','C:/Program Files/Google/Chrome/Application/chrome.exe']]){
    const browser=await chromium.launch({executablePath:exe,headless:true});
    const context=await browser.newContext({viewport:{width:1600,height:1000},offline:true});
    const page=await context.newPage();
    page.on('pageerror',e=>results.errors.push({name,error:e.message}));
    page.on('request',r=>{if(/^https?:/.test(r.url()))results.requests.push(r.url());});
    await page.goto(url); await page.evaluate(()=>document.fonts.ready);
    const assert=(v,m)=>{if(!v)throw Error(name+': '+m);};
    const active=()=>page.locator('.slide:not([hidden])').getAttribute('id');
    const checks={name,version:browser.version()};
    assert(await page.locator('.slide').count()===14,'exactly 14 slides');
    assert(await page.locator('nav,button,select,dialog,.speaker-note').count()===0,'no controls or notes');
    const text=await page.locator('main').textContent();
    assert(!/P0[124589]|附錄|本專案|講稿/.test(text),'no internal identifiers, appendix or production prose');
    assert(await active()==='s01','initial');
    for(const key of ['ArrowLeft','PageUp','Home'])await page.keyboard.press(key);
    assert(await active()==='s01','first boundary');
    for(const key of ['ArrowRight','PageDown',' '])await page.keyboard.press(key);
    assert(await active()==='s04','forward shortcuts');
    for(const key of ['ArrowLeft','PageUp'])await page.keyboard.press(key);
    assert(await active()==='s02','back shortcuts');
    await page.keyboard.press('End');
    for(const key of ['ArrowRight','PageDown',' '])await page.keyboard.press(key);
    assert(await active()==='s14','last boundary');
    await page.keyboard.press('Home');
    await page.keyboard.press('n'); await page.keyboard.press('f');
    assert(await active()==='s01' && !await page.evaluate(()=>!!document.fullscreenElement),'removed shortcuts inactive');
    assert(await page.evaluate(()=>location.hash)==='','no hash state');
    await page.keyboard.press('Control+ArrowRight');
    assert(await active()==='s01','modified shortcut ignored');
    checks.keyboard=true; checks.removedFeatures=true;
    checks.fonts=await page.evaluate(()=>({sans:document.fonts.check('20px PreviewSans'),serif:document.fonts.check('20px PreviewSerif')}));
    checks.sizes=[];
    for(const [width,height] of [[1600,1000],[1920,1080],[1366,768]]){
      await page.setViewportSize({width,height}); await page.keyboard.press('Home');
      const slides=[];
      for(let i=0;i<14;i++){
        if(i)await page.keyboard.press('ArrowRight');
        if(width===1600)await page.screenshot({path:path.join(out,name.toLowerCase()+'-'+String(i+1).padStart(2,'0')+'.png')});
        slides.push(await page.locator('.slide:not([hidden])').evaluate(s=>{
          const box=s.getBoundingClientRect();
          const source=s.querySelector('.scope')?.getBoundingClientRect();
          const content=[...s.querySelectorAll(':scope > .content,:scope > .data-layout,:scope > .flow,:scope > .monitor,:scope > .concept-context')].map(e=>e.getBoundingClientRect().bottom);
          return {id:s.id,title:s.querySelector('h1,h2').textContent,sourceOverlap:source&&Math.max(...content)>source.top,
            overflow:[...s.querySelectorAll('h1,h2,h3,p,table,svg,.scope,footer')].filter(e=>{
              if(e.classList.contains('road-art'))return false;
              const b=e.getBoundingClientRect();return b.left<box.left-1||b.right>box.right+1||b.bottom>box.bottom+1||b.top<box.top-1;
            }).map(e=>e.tagName+':'+e.textContent.slice(0,35)),
            source:s.querySelector('.scope')?.textContent||null};
        }));
      }
      checks.sizes.push({width,height,slides});
    }
    await page.setViewportSize({width:390,height:844}); await page.keyboard.press('Home');
    await page.screenshot({path:path.join(out,name.toLowerCase()+'-mobile.png')});
    await page.keyboard.press('ArrowRight'); assert(await active()==='s02','mobile emulation opens and switches');
    checks.mobileEmulation={width:390,height:844,visibleSlides:await page.locator('.slide:not([hidden])').count(),horizontalOverflow:await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth)};
    results.browsers.push(checks); await browser.close();
  }
  fs.writeFileSync(path.join(root,'process','presentation_revision2_checks_2026-11-21.json'),JSON.stringify(results,null,2));
  console.log(JSON.stringify({browsers:results.browsers.map(b=>({name:b.name,version:b.version,keyboard:b.keyboard,removedFeatures:b.removedFeatures,fonts:b.fonts,mobile:b.mobileEmulation,problems:b.sizes.flatMap(z=>z.slides.filter(s=>s.sourceOverlap||s.overflow.length).map(s=>({size:[z.width,z.height],...s})))})),requests:results.requests,errors:results.errors}));
})().catch(e=>{console.error(e);process.exit(1)});
