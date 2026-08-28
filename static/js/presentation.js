(() => {
  'use strict';

  const deck = document.querySelector('.deck');
  if (!deck) return;

  const stage = deck.querySelector('.deck-stage');
  const slides = Array.from(deck.querySelectorAll('.deck-slide'));
  const previousButton = deck.querySelector('[data-action="previous"]');
  const nextButton = deck.querySelector('[data-action="next"]');
  const overviewButton = deck.querySelector('[data-action="overview"]');
  const fullscreenButton = deck.querySelector('[data-action="fullscreen"]');
  const currentCount = deck.querySelector('[data-current-count]');
  const totalCount = deck.querySelector('[data-total-count]');
  const countGroup = deck.querySelector('[data-count-group]');
  const liveStatus = deck.querySelector('[data-live-status]');
  const progress = deck.querySelector('.deck-progress span');
  const languageLink = deck.querySelector('.deck-language');
  const languageBaseHref = languageLink ? languageLink.href.split('#')[0] : '';
  const interactiveSelector = 'a, button, input, select, textarea, summary, [contenteditable="true"]';

  let currentIndex = 0;
  let overview = false;
  let pointerStart = null;

  const coreCount = slides.filter((slide) => slide.dataset.group === 'core').length;
  const appendixCount = slides.length - coreCount;
  const hashFor = (index) => `#${slides[index].id}`;
  const idFromHash = () => {
    try {
      return decodeURIComponent(window.location.hash.slice(1));
    } catch (error) {
      return '';
    }
  };
  const indexFromHash = () => {
    const id = idFromHash();
    return slides.findIndex((slide) => slide.id === id);
  };

  const groupPosition = () => {
    const appendix = slides[currentIndex].dataset.group === 'appendix';
    return {
      appendix,
      current: appendix ? currentIndex - coreCount + 1 : currentIndex + 1,
      total: appendix ? appendixCount : coreCount,
      label: appendix ? document.body.dataset.appendixLabel : document.body.dataset.coreLabel
    };
  };

  const formatStatus = (template, values) => {
    let output = template;
    values.forEach((value) => {
      output = output.replace(/%[ds]/, String(value));
    });
    return output;
  };

  const announce = () => {
    if (!liveStatus) return;
    if (overview) {
      liveStatus.textContent = formatStatus(document.body.dataset.overviewStatus, [slides.length]);
      return;
    }
    const group = groupPosition();
    liveStatus.textContent = `${group.label} · ${formatStatus(document.body.dataset.statusTemplate, [
      group.current,
      group.total,
      slides[currentIndex].querySelector('h2').textContent.trim()
    ])}`;
  };

  const render = ({ shouldAnnounce = true } = {}) => {
    slides.forEach((slide, index) => {
      const active = index === currentIndex;
      slide.classList.toggle('is-active', active);
      slide.setAttribute('aria-hidden', overview || active ? 'false' : 'true');
      slide.querySelector('.overview-select')?.setAttribute('aria-current', active ? 'true' : 'false');
    });

    const group = groupPosition();
    currentCount.textContent = group.appendix ? `A${group.current}` : String(group.current);
    totalCount.textContent = group.appendix ? `A${group.total}` : String(group.total);
    countGroup.textContent = group.label;
    progress.style.width = `${(group.current / group.total) * 100}%`;
    previousButton.disabled = !overview && currentIndex === 0;
    nextButton.disabled = !overview && currentIndex === slides.length - 1;
    overviewButton.setAttribute('aria-pressed', String(overview));
    overviewButton.querySelector('span').textContent = overview
      ? document.body.dataset.slidesLabel
      : document.body.dataset.overviewLabel;
    overviewButton.setAttribute('aria-label', overview
      ? document.body.dataset.slidesLabel
      : document.body.dataset.overviewLabel);

    if (languageLink) languageLink.href = `${languageBaseHref}${hashFor(currentIndex)}`;
    if (!overview) stage.scrollTop = 0;
    if (shouldAnnounce) announce();
  };

  const setSlide = (index, { historyMode = 'push', focusSlide = false } = {}) => {
    currentIndex = Math.max(0, Math.min(index, slides.length - 1));
    if (historyMode === 'push' && window.location.hash !== hashFor(currentIndex)) {
      window.history.pushState(null, '', hashFor(currentIndex));
    } else if (historyMode === 'replace' && window.location.hash !== hashFor(currentIndex)) {
      window.history.replaceState(null, '', hashFor(currentIndex));
    }
    render();
    if (focusSlide) {
      slides[currentIndex].tabIndex = -1;
      slides[currentIndex].focus({ preventScroll: true });
    }
  };

  const setOverview = (enabled) => {
    overview = Boolean(enabled);
    deck.classList.toggle('is-overview', overview);
    render();
    if (overview) {
      const selectButton = slides[currentIndex].querySelector('.overview-select');
      slides[currentIndex].scrollIntoView({ block: 'nearest', inline: 'nearest' });
      selectButton.focus({ preventScroll: true });
    }
  };

  const move = (delta) => {
    if (overview) setOverview(false);
    setSlide(currentIndex + delta);
  };

  const toggleFullscreen = async () => {
    try {
      if (document.fullscreenElement) {
        await document.exitFullscreen();
      } else {
        await deck.requestFullscreen();
      }
    } catch (error) {
      fullscreenButton.hidden = true;
    }
  };

  previousButton.addEventListener('click', () => move(-1));
  nextButton.addEventListener('click', () => move(1));
  overviewButton.addEventListener('click', () => setOverview(!overview));
  fullscreenButton.addEventListener('click', toggleFullscreen);

  deck.querySelectorAll('[data-select-slide]').forEach((button) => {
    button.addEventListener('click', () => {
      const index = Number(button.dataset.selectSlide);
      setOverview(false);
      setSlide(index, { focusSlide: true });
    });
  });

  document.addEventListener('fullscreenchange', () => {
    const active = Boolean(document.fullscreenElement);
    const label = active
      ? document.body.dataset.exitFullscreenLabel
      : document.body.dataset.fullscreenLabel;
    fullscreenButton.setAttribute('aria-label', label);
    fullscreenButton.title = label;
    fullscreenButton.setAttribute('aria-pressed', String(active));
  });

  document.addEventListener('keydown', (event) => {
    if (event.defaultPrevented || event.altKey || event.ctrlKey || event.metaKey || event.shiftKey) return;
    const interactiveTarget = event.target.closest?.(interactiveSelector);
    if (interactiveTarget && !interactiveTarget.classList.contains('overview-select')) return;

    switch (event.key) {
      case 'ArrowRight':
      case 'PageDown':
        event.preventDefault();
        move(1);
        break;
      case 'ArrowLeft':
      case 'PageUp':
        event.preventDefault();
        move(-1);
        break;
      case 'Home':
        event.preventDefault();
        if (overview) setOverview(false);
        setSlide(0);
        break;
      case 'End':
        event.preventDefault();
        if (overview) setOverview(false);
        setSlide(slides.length - 1);
        break;
      case 'Escape':
        event.preventDefault();
        setOverview(true);
        break;
      case 'o':
      case 'O':
        event.preventDefault();
        setOverview(!overview);
        break;
      case 'f':
      case 'F':
        event.preventDefault();
        toggleFullscreen();
        break;
      default:
        break;
    }
  });

  stage.addEventListener('pointerdown', (event) => {
    if (overview || event.pointerType === 'mouse' || event.target.closest(interactiveSelector)) return;
    pointerStart = { id: event.pointerId, x: event.clientX, y: event.clientY };
  });

  stage.addEventListener('pointerup', (event) => {
    if (!pointerStart || pointerStart.id !== event.pointerId) return;
    const deltaX = event.clientX - pointerStart.x;
    const deltaY = event.clientY - pointerStart.y;
    pointerStart = null;
    if (Math.abs(deltaX) < 55 || Math.abs(deltaX) <= Math.abs(deltaY) * 1.2) return;
    move(deltaX < 0 ? 1 : -1);
  });

  stage.addEventListener('pointercancel', () => { pointerStart = null; });

  const syncFromLocation = () => {
    if (idFromHash() === stage.id) {
      stage.focus({ preventScroll: true });
      return;
    }
    const hashIndex = indexFromHash();
    setSlide(hashIndex >= 0 ? hashIndex : 0, {
      historyMode: hashIndex >= 0 ? 'none' : 'replace'
    });
  };

  window.addEventListener('hashchange', syncFromLocation);

  if (!document.fullscreenEnabled || typeof deck.requestFullscreen !== 'function') {
    fullscreenButton.hidden = true;
  }

  const initialId = idFromHash();
  const initialIndex = indexFromHash();
  currentIndex = initialIndex >= 0 ? initialIndex : 0;
  if (initialIndex < 0 && initialId !== stage.id) {
    window.history.replaceState(null, '', hashFor(currentIndex));
  }
  render({ shouldAnnounce: false });
  document.documentElement.classList.replace('no-js', 'js');
  if (initialId === stage.id) {
    window.requestAnimationFrame(() => stage.focus({ preventScroll: true }));
  }
})();
