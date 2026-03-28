const REGISTRY_PATH = "./config/scene-registry.json";
const LEGEND_COPY_PATH = "./config/legend-copy.json";
const tooltip = document.getElementById("tooltip");
const sidePanelTitle = document.querySelector(".side-panel h1");
const sidePanelLede = document.querySelector(".side-panel .lede");
const confidenceCard = document.querySelector(".confidence-card p");

const map = new maplibregl.Map({
  container: "map",
  style: {
    version: 8,
    sources: {
      osm: {
        type: "raster",
        tiles: ["https://tile.openstreetmap.org/{z}/{x}/{y}.png"],
        tileSize: 256,
        attribution: "&copy; OpenStreetMap contributors"
      }
    },
    layers: [{ id: "osm", type: "raster", source: "osm" }]
  },
  center: [-104.62, 50.445],
  zoom: 11,
  hash: false,
});

function colorForCount(count) {
  if (count >= 300) return [8, 81, 156, 190];
  if (count >= 200) return [49, 130, 189, 180];
  if (count >= 100) return [107, 174, 214, 170];
  if (count >= 25) return [158, 202, 225, 160];
  if (count >= 1) return [222, 235, 247, 150];
  return [242, 246, 250, 110];
}

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

Promise.all([
  fetch(REGISTRY_PATH).then((r) => r.json()),
  fetch(LEGEND_COPY_PATH).then((r) => r.json())
])
  .then(([registry, legendCopy]) => {
    const scene = registry.scenes[0];
    const sceneCopy = legendCopy[scene.panel_copy_key];
    if (sceneCopy?.title) sidePanelTitle.textContent = sceneCopy.title;
    if (sceneCopy?.copy) sidePanelLede.textContent = sceneCopy.copy;
    if (legendCopy?.confidence_labels?.observed) confidenceCard.textContent = legendCopy.confidence_labels.observed;
    return fetch(scene.data_path).then((res) => res.json());
  })
  .then((geojson) => {
    const layer = new deck.MapboxOverlay({
      interleaved: true,
      layers: [
        new deck.GeoJsonLayer({
          id: "scene1-observed-area-replacements",
          data: geojson,
          stroked: true,
          filled: true,
          pickable: true,
          getLineColor: [28, 60, 88, 180],
          lineWidthMinPixels: 1,
          getFillColor: (feature) => colorForCount(feature.properties.observed_replacements_2019_2025),
          updateTriggers: { getFillColor: [geojson.features.length] },
          onHover: ({ object, x, y }) => {
            if (!object) {
              tooltip.classList.add("hidden");
              return;
            }
            const p = object.properties;
            tooltip.innerHTML = `
              <div class="badge">${escapeHtml(p.confidence_class)}</div>
              <h3>${escapeHtml(p.tooltip_title)}</h3>
              <p>${escapeHtml(p.tooltip_subtitle)}</p>
              <p><strong>Observed replacements:</strong> ${p.observed_replacements_2019_2025}</p>
              <p><strong>Lead baseline:</strong> ${p.lead_connections_total ?? "n/a"}</p>
              <p><strong>Observed share of lead baseline:</strong> ${p.observed_replacement_share_of_lead == null ? "n/a" : (p.observed_replacement_share_of_lead * 100).toFixed(1) + "%"}</p>
              <p>${escapeHtml(p.confidence_note)}</p>
            `;
            tooltip.style.left = `${x + 12}px`;
            tooltip.style.top = `${y + 12}px`;
            tooltip.classList.remove("hidden");
          },
        }),
      ],
    });

    map.addControl(layer);
    const bounds = geojson.features.reduce((acc, feature) => {
      const coords = feature.geometry.type === "Polygon" ? [feature.geometry.coordinates] : feature.geometry.coordinates;
      coords.forEach((poly) => poly.forEach((ring) => ring.forEach(([lng, lat]) => acc.extend([lng, lat]))));
      return acc;
    }, new maplibregl.LngLatBounds());
    if (!bounds.isEmpty()) map.fitBounds(bounds, { padding: 30, duration: 0 });
  })
  .catch((err) => {
    console.error(err);
    const stage = document.querySelector(".map-stage");
    const msg = document.createElement("div");
    msg.style.padding = "0 20px 20px";
    msg.innerHTML = `<p style="color:#9b1c1c;font-weight:600;">Map failed to load. Check the generated Scene 1 data assets and config files.</p>`;
    stage.appendChild(msg);
  });

map.on("mouseout", () => {
  tooltip.classList.add("hidden");
});
