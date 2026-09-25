(function () {
  'use strict';

  var revealTargets = document.querySelectorAll('[data-reveal]');
  if ('IntersectionObserver' in window && revealTargets.length) {
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.25 });
    revealTargets.forEach(function (target) { observer.observe(target); });
  } else {
    revealTargets.forEach(function (target) { target.classList.add('is-visible'); });
  }

  var tabs = document.querySelectorAll('[role="tab"]');
  tabs.forEach(function (tab) {
    tab.addEventListener('click', function () {
      var targetId = tab.getAttribute('aria-controls');
      tabs.forEach(function (item) {
        var selected = item === tab;
        item.setAttribute('aria-selected', selected ? 'true' : 'false');
        item.setAttribute('tabindex', selected ? '0' : '-1');
      });
      document.querySelectorAll('[role="tabpanel"]').forEach(function (panel) {
        panel.hidden = panel.id !== targetId;
      });
    });

    tab.addEventListener('keydown', function (event) {
      if (event.key !== 'ArrowLeft' && event.key !== 'ArrowRight') return;
      event.preventDefault();
      var list = Array.prototype.slice.call(tabs);
      var index = list.indexOf(tab);
      var next = event.key === 'ArrowRight' ? index + 1 : index - 1;
      list[(next + list.length) % list.length].focus();
      list[(next + list.length) % list.length].click();
    });
  });

  var progress = document.querySelector('.progress-fill');
  var chapters = document.querySelector('.chapters');
  if (progress && chapters) {
    var updateProgress = function () {
      var rect = chapters.getBoundingClientRect();
      var total = chapters.offsetHeight - window.innerHeight;
      var travelled = Math.min(Math.max(-rect.top, 0), Math.max(total, 1));
      progress.style.height = (travelled / Math.max(total, 1) * 100) + '%';
    };
    window.addEventListener('scroll', updateProgress, { passive: true });
    updateProgress();
  }
})();
