/* ============================================
   REGINA LEAD INVESTIGATION — APP.JS
   ScrollyTelling, Map, Tabs, Copy
   ============================================ */

document.addEventListener('DOMContentLoaded', () => {
  initScrollObserver();
  initMap();
  initTabs();
});

/* ─── SCROLL OBSERVER ─── */
function initScrollObserver() {
  const beats = document.querySelectorAll('.beat');
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  if (prefersReducedMotion) {
    beats.forEach(b => b.classList.add('in-view'));
    return;
  }

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('in-view');
      }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -60px 0px' });

  beats.forEach(b => observer.observe(b));
}

/* ─── MAP ─── */
function initMap() {
  const container = document.getElementById('map');
  if (!container) return;

  const map = L.map('map', {
    center: [50.445, -104.618],
    zoom: 12,
    scrollWheelZoom: false,
    dragging: !L.Browser.mobile,
    tap: true,
  });

  L.tileLayer('https://{s}.basemaps.cartocdn.com/light_nolabels/{z}/{x}/{y}{r}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OSM</a> &copy; <a href="https://carto.com/">CARTO</a>',
    maxZoom: 18,
  }).addTo(map);

  // Label layer on top
  L.tileLayer('https://{s}.basemaps.cartocdn.com/light_only_labels/{z}/{x}/{y}{r}.png', {
    maxZoom: 18,
    pane: 'overlayPane',
  }).addTo(map);

  fetch('public/data/ct_harm_analysis.geojson')
    .then(r => r.json())
    .then(data => {
      const maxBurden = Math.max(...data.features.map(f => f.properties.total_burden_npv || 0));

      function getColor(val) {
        const t = Math.sqrt(val / maxBurden); // sqrt scale for better distribution
        if (t < 0.33) return interpolateColor('#e8f0ea', '#4a7c59', t / 0.33);
        return interpolateColor('#4a7c59', '#b91c1c', (t - 0.33) / 0.67);
      }

      function interpolateColor(c1, c2, t) {
        const r1 = parseInt(c1.slice(1,3), 16), g1 = parseInt(c1.slice(3,5), 16), b1 = parseInt(c1.slice(5,7), 16);
        const r2 = parseInt(c2.slice(1,3), 16), g2 = parseInt(c2.slice(3,5), 16), b2 = parseInt(c2.slice(5,7), 16);
        const r = Math.round(r1 + (r2-r1)*t), g = Math.round(g1 + (g2-g1)*t), b = Math.round(b1 + (b2-b1)*t);
        return `rgb(${r},${g},${b})`;
      }

      function style(feature) {
        return {
          fillColor: getColor(feature.properties.total_burden_npv || 0),
          weight: 1.5,
          opacity: 0.8,
          color: '#555',
          fillOpacity: 0.65,
        };
      }

      function onEachFeature(feature, layer) {
        const p = feature.properties;
        const fmt = n => n ? n.toLocaleString() : '0';
        const fmtM = n => n ? '$' + (n / 1e6).toFixed(1) + 'M' : '$0';

        layer.bindPopup(`
          <div style="font-family:'DM Sans',sans-serif;font-size:13px;line-height:1.5;max-width:260px">
            <div style="font-weight:700;font-size:14px;margin-bottom:4px">CT ${p.ct_name || p.ct_uid}</div>
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:4px 12px;font-size:12px">
              <span>Lead connections</span><strong>${fmt(p.pb_connections)}</strong>
              <span>Children 0-14</span><strong>${fmt(p.children_0_14)}</strong>
              <span>Indigenous</span><strong>${(p.indigenous_pct||0).toFixed(1)}%</strong>
              <span>Low income</span><strong>${(p.low_income_pct||0).toFixed(1)}%</strong>
              <span>Renter</span><strong>${(p.renter_pct||0).toFixed(1)}%</strong>
              <span>Replacement rate</span><strong>${(p.replacement_rate||0).toFixed(1)}%</strong>
            </div>
            <div style="margin-top:8px;padding-top:6px;border-top:1px solid #ddd;font-size:12px">
              <div>Realized: ${fmtM(p.realized_npv)} &middot; At risk: ${fmtM(p.atrisk_npv)}</div>
              <div style="font-weight:700;color:#b91c1c">Total burden: ${fmtM(p.total_burden_npv)}</div>
            </div>
          </div>
        `, { closeButton: true, maxWidth: 280 });

        layer.on('mouseover', function() {
          this.setStyle({ weight: 3, color: '#2b2b2b', fillOpacity: 0.8 });
          this.bringToFront();
        });
        layer.on('mouseout', function() {
          geojsonLayer.resetStyle(this);
        });
      }

      const geojsonLayer = L.geoJSON(data, { style, onEachFeature }).addTo(map);

      // Fit bounds to the data
      const bounds = geojsonLayer.getBounds();
      if (bounds.isValid()) {
        map.fitBounds(bounds, { padding: [20, 20] });
      }
    })
    .catch(err => {
      console.error('Failed to load GeoJSON:', err);
      container.innerHTML = '<p style="padding:2rem;text-align:center;color:#888">Map data unavailable. <a href="public/data/ct_harm_analysis.geojson">Download GeoJSON</a></p>';
    });
}

/* ─── TABS ─── */
function initTabs() {
  const tabs = document.querySelectorAll('.action-tab');
  const panels = document.querySelectorAll('.action-panel');

  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      tabs.forEach(t => { t.classList.remove('is-active'); t.setAttribute('aria-selected', 'false'); t.tabIndex = -1; });
      panels.forEach(p => { p.classList.remove('is-active'); p.hidden = true; });

      tab.classList.add('is-active');
      tab.setAttribute('aria-selected', 'true');
      tab.tabIndex = 0;

      const panelId = tab.getAttribute('aria-controls');
      const panel = document.getElementById(panelId);
      if (panel) { panel.classList.add('is-active'); panel.hidden = false; }
    });

    tab.addEventListener('keydown', (e) => {
      const tabArray = Array.from(tabs);
      const idx = tabArray.indexOf(tab);
      let next;
      if (e.key === 'ArrowRight') next = tabArray[(idx + 1) % tabArray.length];
      if (e.key === 'ArrowLeft') next = tabArray[(idx - 1 + tabArray.length) % tabArray.length];
      if (e.key === 'Home') next = tabArray[0];
      if (e.key === 'End') next = tabArray[tabArray.length - 1];
      if (next) { e.preventDefault(); next.click(); next.focus(); }
    });
  });
}

/* ─── COPY TEMPLATE ─── */
function copyTemplate(btn) {
  const block = btn.previousElementSibling;
  if (!block) return;
  const text = block.innerText;
  navigator.clipboard.writeText(text).then(() => {
    const orig = btn.textContent;
    btn.textContent = 'Copied';
    setTimeout(() => { btn.textContent = orig; }, 2000);
  }).catch(() => {
    // Fallback
    const ta = document.createElement('textarea');
    ta.value = text;
    document.body.appendChild(ta);
    ta.select();
    document.execCommand('copy');
    document.body.removeChild(ta);
    const orig = btn.textContent;
    btn.textContent = 'Copied';
    setTimeout(() => { btn.textContent = orig; }, 2000);
  });
}
