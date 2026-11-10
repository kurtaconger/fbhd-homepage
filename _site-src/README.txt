Site generator for factbasedhealthcaredecisions.com.

  cd _site-src
  python build.py

Rebuilds index.html, 404.html, sitemap.xml, robots.txt, llms.txt, about/, questions/ and counties/ in the site root
from the templates here and ra_premiums.json (HealthCare.gov Marketplace API prices, pulled by
covanu-insure/Research/carteret-2027/ra12.mjs). nc_map.svg and zones.json come from build_map.mjs
(needs: npm install us-atlas topojson-client d3-geo). Update UPDATED / UPDATED_H in fbsite.py each plan year.

The guides for rating areas 9, 10, 11, 13 and 15 and Nash County are built by county_multi.py from zones_2027.json, which
covanu-insure/Research/zones-2027 produces from the Marketplace API (node pull_zones.mjs plans | details | zips | hospitals | hosp2,
then python prep_zones.py <path to this folder>/zones_2027.json). New Hanover County keeps its own module (county_nh.py, nh_2027.json).
