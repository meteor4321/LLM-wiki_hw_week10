(() => {
 const slides=[...document.querySelectorAll('.slide')];
 const tabs=[...document.querySelectorAll('[data-page]')];
 let current=0;
 function show(n){current=Math.max(0,Math.min(slides.length-1,n));slides.forEach((s,i)=>s.hidden=i!==current);tabs.forEach((b,i)=>{if(i===current)b.setAttribute('aria-current','page');else b.removeAttribute('aria-current')});history.replaceState(null,'','#'+slides[current].id);}
 tabs.forEach(b=>b.addEventListener('click',()=>show(Number(b.dataset.page))));
 document.addEventListener('keydown',e=>{if(e.altKey||e.ctrlKey||e.metaKey)return;if(['ArrowRight','PageDown',' '].includes(e.key)){e.preventDefault();show(current+1)}if(['ArrowLeft','PageUp'].includes(e.key)){e.preventDefault();show(current-1)}if(e.key==='Home')show(0);if(e.key==='End')show(slides.length-1)});
 document.getElementById('fullscreen').addEventListener('click',async()=>{try{if(document.fullscreenElement)await document.exitFullscreen();else await document.documentElement.requestFullscreen()}catch{document.getElementById('fullscreen').textContent='請使用瀏覽器全螢幕'}});
 const index=slides.findIndex(s=>'#'+s.id===location.hash);show(index<0?0:index);
})();
