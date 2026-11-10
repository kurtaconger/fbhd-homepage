r"""Regenerates the FBHD site pages from the templates in this folder.

    cd C:\Users\kurtc\Dev\fbhd-homepage\_site-src
    python build.py

Writes index.html, 404.html, sitemap.xml, robots.txt, llms.txt, about/, questions/, counties/ into the
parent folder (the site root). Premium data comes from ra_premiums.json, pulled from the HealthCare.gov
Marketplace API by covanu-insure/Research/carteret-2027/ra12.mjs. To refresh prices for a new plan year,
re-run that script, copy ra_premiums.json here, update UPDATED / UPDATED_H in fbsite.py, and rebuild.
The New Hanover County guide (county_nh.py) reads nh_2027.json instead: 75 plans from four insurers, collected
from the HealthCare.gov plan preview for ZIP 28401 on November 10, 2026 (see the notes at the top of county_nh.py).
The other guides in rating areas 9, 10, 11, 13 and 15 and Nash County (county_multi.py) read zones_2027.json, built from the
Marketplace API by covanu-insure/Research/zones-2027 (pull_zones.mjs, then prep_zones.py); the rating area 14 prices for
Edgecombe, Greene, Pitt, Wayne and Wilson counties in ra_premiums.json come from the same pull.
"""
import runpy, os, sys
here = os.path.dirname(os.path.abspath(__file__))
os.chdir(here); sys.path.insert(0, here)
for m in ["counties", "county_nh", "county_multi", "guide_meds", "guide_selfemp", "guide_retire", "guide_ppo", "indexes"]:
    runpy.run_module(m, run_name="__main__")
print("site rebuilt into", os.path.abspath(os.path.join(here, "..")))
