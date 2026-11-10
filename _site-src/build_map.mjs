import fs from "fs";
import * as topojson from "topojson-client";
import { geoConicConformal, geoPath, geoCentroid } from "d3-geo";
const us = JSON.parse(fs.readFileSync("node_modules/us-atlas/counties-10m.json"));
const counties = topojson.feature(us, us.objects.counties).features.filter(f => f.id.startsWith("37"));
const names = JSON.parse(fs.readFileSync("/mnt/user-data/uploads/covanu-insure/Research/carteret-2027/nc_county_plans.json"));
const RA = JSON.parse(fs.readFileSync("ra.json"));
const LIVE = new Set([9, 10, 11, 12, 13, 14, 15, 16]);
// counties with a guide outside the all-live rating areas (none at the moment)
const LIVE_FIPS = new Set([]);
const proj = geoConicConformal().parallels([34.33, 36.17]).rotate([79, 0]).fitSize([900, 360], { type: "FeatureCollection", features: counties });
const path = geoPath(proj);
let paths = [], labels = {}, geo = { type: "FeatureCollection", features: [] };
const slug = (n) => n.toLowerCase().replace(/[^a-z]+/g, "-");
for (const f of counties) {
  const d = path(f); const ra = RA[f.id]; const nm = (names[f.id]?.name || f.properties.name).replace(" County", "");
  const live = LIVE.has(ra) || LIVE_FIPS.has(f.id);
  const href = live ? `/counties/${slug(nm)}/` : `/counties/zone-${ra}/`;
  const cls = live ? "live" : "soon";
  paths.push(`<a href="${href}" class="${cls}" data-zone="${ra}"><path d="${d}"><title>${nm} County · rating area ${ra}${live ? " · guide available" : " · coming soon"}</title></path></a>`);
  const c = proj(geoCentroid(f)); (labels[ra] ||= []).push(c);
  if (live) geo.features.push({ type: "Feature", properties: { fips: f.id, name: nm }, geometry: f.geometry });
}
const zoneLabels = Object.entries(labels).map(([z, pts]) => { const x = pts.reduce((a, p) => a + p[0], 0) / pts.length, y = pts.reduce((a, p) => a + p[1], 0) / pts.length; return `<text x="${x.toFixed(1)}" y="${y.toFixed(1)}">${z}</text>`; }).join("\n");
const svg = `<svg class="nc-map" viewBox="0 0 900 360" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="nc-map-title">
<title id="nc-map-title">North Carolina counties grouped into the 16 CMS rating areas. Click a county.</title>
<g class="counties">
${paths.join("\n")}
</g>
<g class="zone-labels" aria-hidden="true">
${zoneLabels}
</g>
</svg>`;
fs.writeFileSync("nc_map.svg", svg);
const round = (c) => Array.isArray(c[0]) ? c.map(round) : [Math.round(c[0] * 1000) / 1000, Math.round(c[1] * 1000) / 1000];
for (const f of geo.features) f.geometry.coordinates = round(f.geometry.coordinates);
fs.writeFileSync("geo-zone.json", JSON.stringify(geo));
// zone -> counties listing with carriers for the coming-soon pages
const zones = {};
for (const [fips, v] of Object.entries(names)) { const z = RA[fips]; (zones[z] ||= { counties: [], issuers: new Set(), plans: [] }); zones[z].counties.push(v.name.replace(" County", "")); v.issuers.forEach(i => zones[z].issuers.add(i)); zones[z].plans.push(v.n); }
const out = {}; for (const [z, v] of Object.entries(zones)) out[z] = { counties: v.counties.sort(), issuers: [...v.issuers].sort(), plans_min: Math.min(...v.plans), plans_max: Math.max(...v.plans) };
fs.writeFileSync("zones.json", JSON.stringify(out, null, 1));
console.log("svg bytes", svg.length, "zones", Object.keys(out).length);
