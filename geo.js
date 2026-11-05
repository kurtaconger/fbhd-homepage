/* Shows elements with class "geo-gate" (County Guides menu item and homepage section) only when the
   visitor is very likely inside the covered area: the 21 counties in NC rating areas 12 and 16.
   Location comes from Netlify's edge geolocation (/geo), then a point-in-polygon test (with a 30 km
   buffer) against the county boundaries in /geo-zone.json. Override for testing: ?geo=in or ?geo=out (remembered for the tab). */
(function () {
  var KEY = "fbhd-geo";
  function show() { document.documentElement.classList.add("geo-in"); }
  function inRing(pt, ring) {
    var x = pt[0], y = pt[1], inside = false;
    for (var i = 0, j = ring.length - 1; i < ring.length; j = i++) {
      var xi = ring[i][0], yi = ring[i][1], xj = ring[j][0], yj = ring[j][1];
      if ((yi > y) !== (yj > y) && x < (xj - xi) * (y - yi) / (yj - yi) + xi) inside = !inside;
    }
    return inside;
  }
  function inGeom(pt, g) {
    if (g.type === "Polygon") return inRing(pt, g.coordinates[0]);
    if (g.type === "MultiPolygon") return g.coordinates.some(function (poly) { return inRing(pt, poly[0]); });
    return false;
  }
  // IP geolocation often lands on a nearby hub town (Swansboro, Greenville, Jacksonville) rather than the
  // visitor's county, so a point within BUFFER_KM of the zone boundary also counts as inside.
  var BUFFER_KM = 30;
  function nearGeom(pt, g) {
    var rings = g.type === "Polygon" ? [g.coordinates[0]] : g.type === "MultiPolygon" ? g.coordinates.map(function (p) { return p[0]; }) : [];
    var kx = 111.32 * Math.cos(pt[1] * Math.PI / 180), ky = 110.57, lim = BUFFER_KM * BUFFER_KM;
    for (var r = 0; r < rings.length; r++) {
      var ring = rings[r];
      for (var i = 0; i < ring.length; i++) {
        var dx = (ring[i][0] - pt[0]) * kx, dy = (ring[i][1] - pt[1]) * ky;
        if (dx * dx + dy * dy <= lim) return true;
      }
    }
    return false;
  }
  try {
    var force = new URLSearchParams(location.search).get("geo");
    if (force === "in" || force === "out") sessionStorage.setItem(KEY, force);
    var cached = sessionStorage.getItem(KEY);
    if (cached === "in") { show(); return; }
    if (cached === "out") return;
  } catch (e) {}
  fetch("/geo", { cache: "no-store" })
    .then(function (r) { if (!r.ok) throw new Error("no geo"); return r.json(); })
    .then(function (g) {
      if (!g || g.region !== "NC" || typeof g.lat !== "number" || typeof g.lon !== "number") throw new Error("outside");
      return fetch("/geo-zone.json").then(function (r) { return r.json(); }).then(function (zone) {
        var pt = [g.lon, g.lat];
        var inside = zone.features.some(function (f) { return inGeom(pt, f.geometry); }) ||
                     zone.features.some(function (f) { return nearGeom(pt, f.geometry); });
        try { sessionStorage.setItem(KEY, inside ? "in" : "out"); } catch (e) {}
        if (inside) show();
      });
    })
    .catch(function () { try { sessionStorage.setItem(KEY, "out"); } catch (e) {} });
})();
