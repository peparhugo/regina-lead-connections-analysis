# Data discovery notes

## How the city page map is populated
- Page embeds ArcGIS WebAppViewer:
  - `https://regina.maps.arcgis.com/apps/webappviewer/index.html?appid=55fad6b70c4f4c0bbd4efaa67197040d`
- App data references web map id:
  - `12fe6e7a97da4bdea637cafbb8490a10`
- Web map operational layer:
  - `https://opengis.regina.ca/arcgis/rest/services/CGISViewer/LeadConnectionAreas/MapServer`

## Layer used for analysis
- `.../MapServer/0` fields:
  - `NAME`
  - `WC_Total`
  - `Lead_Total`
  - `Lead_Per`
- GeoJSON query endpoint:
  - `.../0/query?where=1%3D1&outFields=NAME%2CWC_Total%2CLead_Total%2CLead_Per&f=geojson`

## Additional potentially relevant service
- `CGISViewer/SewerWaterCondition` includes a layer named `Lead & POLY B Water Connections`.
