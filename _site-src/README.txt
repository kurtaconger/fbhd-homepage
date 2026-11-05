Site generator for factbasedhealthcaredecisions.com.

  cd _site-src
  python build.py

Rebuilds index.html, 404.html, sitemap.xml, robots.txt, llms.txt, about/, questions/ and counties/ in the site root
from the templates here and ra_premiums.json (HealthCare.gov Marketplace API prices, pulled by
covanu-insure/Research/carteret-2027/ra12.mjs). nc_map.svg and zones.json come from build_map.mjs
(needs: npm install us-atlas topojson-client d3-geo). Update UPDATED / UPDATED_H in fbsite.py each plan year.
