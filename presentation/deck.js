(() => {
  'use strict';
  const slides = [...document.querySelectorAll('.slide')];
  let current = 0;
  function show(n) {
    current = Math.max(0, Math.min(slides.length - 1, n));
    slides.forEach((slide, i) => { slide.hidden = i !== current; });
  }
  document.addEventListener('keydown', event => {
    if (event.altKey || event.ctrlKey || event.metaKey ||
        /^(INPUT|TEXTAREA|SELECT)$/.test(event.target.tagName) || event.target.isContentEditable) return;
    if (event.key === ' ' && event.target.closest('a,button')) return;
    if (['ArrowRight', 'PageDown', ' '].includes(event.key)) {
      event.preventDefault(); show(current + 1);
    } else if (['ArrowLeft', 'PageUp'].includes(event.key)) {
      event.preventDefault(); show(current - 1);
    } else if (event.key === 'Home') {
      event.preventDefault(); show(0);
    } else if (event.key === 'End') {
      event.preventDefault(); show(slides.length - 1);
    }
  });
  show(0);
})();
