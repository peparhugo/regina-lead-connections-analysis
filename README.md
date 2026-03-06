# Regina Lead Service Connections — Public Analysis Map

> ✅ This repository was completely created by **OpenClaw** with autonomous assistant workflows.

## Mission
Build a transparent, public, and reproducible analysis of how the City of Regina is handling and replacing lead water service connections, with an interactive map and simple trend views that residents can inspect themselves.

## What this project shows
- Neighborhood-level lead service connection indicators from Regina's ArcGIS/OpenGIS service.
- Choropleth map of estimated lead-connection percentage by community area.
- Summary cards for citywide totals from the same source.
- A reported milestones timeline chart (publicly reported figures) to visualize pace and criticism context.

## Data sources
- City page: https://www.regina.ca/home-property/water/water/lead-service-connections/
- Embedded web map app (appid): `55fad6b70c4f4c0bbd4efaa67197040d`
- Web map id: `12fe6e7a97da4bdea637cafbb8490a10`
- ArcGIS layer used:
  - `https://opengis.regina.ca/arcgis/rest/services/CGISViewer/LeadConnectionAreas/MapServer/0`
  - Query endpoint (geojson):
    `.../query?where=1%3D1&outFields=NAME%2CWC_Total%2CLead_Total%2CLead_Per&f=geojson`

## Notes and caveats
- The neighborhood map layer is a current-state snapshot and not a historical time-series.
- Timeline points are from public reporting/official communication and should be treated as reported milestones unless confirmed by official annual datasets.

## Local preview
Open `index.html` in a browser.

## GitHub Pages
This repo is configured for GitHub Pages (branch `main`, root `/`).
