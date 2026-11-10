Site generator for factbasedhealthcaredecisions.com.

  cd _site-src
  python build.py

Rebuilds index.html, 404.html, sitemap.xml, robots.txt, llms.txt, about/, questions/ and counties/ in the site root
from the templates here and ra_premiums.json (HealthCare.gov Marketplace API prices, pulled by
covanu-insure/Research/carteret-2027/ra12.mjs). nc_map.svg and zones.json come from build_map.mjs
(needs: npm install us-atlas topojson-client d3-geo). Update UPDATED / UPDATED_H in fbsite.py each plan year.

The guides for rating areas 1 to 11, 13 and 15 and Nash County are built by county_multi.py from zones_2027.json, which
covanu-insure/Research/zones-2027 produces from the Marketplace API (node pull_zones.mjs plans | details | zips | hosp2,
then python prep_zones.py <path to this folder>/zones_2027.json). New Hanover County keeps its own module (county_nh.py, nh_2027.json).

Hospitals: hosp_config.json (in zones-2027) lists each county's hospitals and their NPIs. HealthCare.gov's lookup often
lists a hospital under several NPIs and insurers do not all use the same one, so the NPIs were chosen by street address
with hscan.mjs and audited per network with hdeep.mjs (hcov.mjs probes one ZIP). A network listed only under a hospital's
behavioral health unit (HOSP_BH in prep_zones.py) shows as "Unclear" on the page instead of in network.

Networks: prep_zones.py names each network from the plan names. Within a county the short name is unique ("Blue Home",
"Blue Local", "Ambetter", "Oscar"); the full name ("Blue Home with Novant Health", "Oscar with Atrium Health") is in
net_long and is what the tables show. Every NC county now has a guide, so counties.py makes no "coming soon" zone pages.
