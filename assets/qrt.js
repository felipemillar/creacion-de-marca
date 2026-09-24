/* ============================================================
   qrt^ — Comportamiento compartido de las páginas interiores
   Cabecera con scroll, menú móvil y conmutador de tema.
   El tema se aplica antes del pintado con el script inline del <head>.
   ============================================================ */

(function () {
  'use strict';

  var header = document.getElementById('main-header');
  var themeToggle = document.getElementById('theme-toggle');
  var mobileToggle = document.getElementById('mobile-menu-toggle');

  /* --- Cabecera: expandir el logo al hacer scroll --- */
  if (header) {
    var onScroll = function () {
      if (window.scrollY > 40) {
        header.classList.add('scrolled');
      } else {
        header.classList.remove('scrolled');
      }
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  /* --- Conmutador de tema claro / oscuro --- */
  if (themeToggle) {
    themeToggle.addEventListener('click', function (e) {
      e.preventDefault();
      var isDark = document.documentElement.classList.toggle('dark-theme');
      try {
        localStorage.setItem('theme', isDark ? 'dark' : 'light');
      } catch (err) {
        /* Navegación privada: el tema simplemente no persiste. */
      }
    });
  }

  /* --- Menú móvil --- */
  if (mobileToggle && header) {
    var closeMenu = function () {
      header.classList.remove('menu-open');
      mobileToggle.classList.remove('active');
      mobileToggle.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = '';
    };

    mobileToggle.addEventListener('click', function () {
      var isOpen = header.classList.toggle('menu-open');
      mobileToggle.classList.toggle('active', isOpen);
      mobileToggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
      document.body.style.overflow = isOpen ? 'hidden' : '';
    });

    // Cerrar al navegar, salvo al tocar el padre de un submenú
    document.querySelectorAll('nav a').forEach(function (link) {
      link.addEventListener('click', function () {
        if (link.classList.contains('dropdown-toggle')) return;
        closeMenu();
      });
    });

    // Cerrar con Escape
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && header.classList.contains('menu-open')) closeMenu();
    });

    // Cerrar al volver a escritorio
    window.addEventListener('resize', function () {
      if (window.innerWidth > 991 && header.classList.contains('menu-open')) closeMenu();
    });
  }
})();
