/* Trading Científico — interacciones mínimas, sin dependencias */
(function () {
  "use strict";

  var reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---- reveals al hacer scroll ---- */
  var revealed = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && !reduced) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          e.target.classList.add("in");
          io.unobserve(e.target);
        }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -40px 0px" });
    revealed.forEach(function (el) { io.observe(el); });
  } else {
    revealed.forEach(function (el) { el.classList.add("in"); });
  }

  /* ---- dibujo de la curva de capital del hero ---- */
  var chart = document.querySelector(".chart");
  if (chart) {
    requestAnimationFrame(function () { chart.classList.add("chart--draw"); });
  }

  /* ---- contadores (97%, 331, 10) ---- */
  function animateCount(el) {
    var target = parseInt(el.getAttribute("data-count"), 10);
    var suffix = el.getAttribute("data-suffix") || "";
    if (reduced) { el.textContent = target + suffix; return; }
    var dur = 1400;
    var t0 = null;
    function tick(t) {
      if (!t0) t0 = t;
      var p = Math.min((t - t0) / dur, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = Math.round(target * eased) + suffix;
      if (p < 1) requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
  }
  var counters = document.querySelectorAll("[data-count]");
  if ("IntersectionObserver" in window) {
    var cio = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          animateCount(e.target);
          cio.unobserve(e.target);
        }
      });
    }, { threshold: 0.6 });
    counters.forEach(function (el) { cio.observe(el); });
  } else {
    counters.forEach(animateCount);
  }

  /* ---- barra CTA fija en móvil: aparece al pasar el hero ---- */
  var sticky = document.getElementById("stickycta");
  var hero = document.getElementById("top");
  var apply = document.getElementById("aplicar");
  if (sticky && hero && "IntersectionObserver" in window) {
    var pastHero = false, onApply = false;
    function update() {
      var show = pastHero && !onApply;
      sticky.classList.toggle("show", show);
      sticky.setAttribute("aria-hidden", show ? "false" : "true");
    }
    new IntersectionObserver(function (entries) {
      pastHero = !entries[0].isIntersecting;
      update();
    }, { threshold: 0 }).observe(hero);
    if (apply) {
      new IntersectionObserver(function (entries) {
        onApply = entries[0].isIntersecting;
        update();
      }, { threshold: 0.2 }).observe(apply);
    }
  }
})();
