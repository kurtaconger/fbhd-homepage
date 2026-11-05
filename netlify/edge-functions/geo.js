// Returns the visitor's approximate location from Netlify's edge geolocation (IP-based).
// Used by /geo.js to decide whether to show the county-guide menu and section.
export default async (request, context) => {
  const g = context.geo || {};
  const body = {
    country: g.country?.code || null,
    region: g.subdivision?.code || null,
    city: g.city || null,
    lat: typeof g.latitude === "number" ? g.latitude : null,
    lon: typeof g.longitude === "number" ? g.longitude : null,
  };
  return new Response(JSON.stringify(body), {
    headers: { "content-type": "application/json", "cache-control": "no-store", "access-control-allow-origin": "*" },
  });
};

export const config = { path: "/geo" };
