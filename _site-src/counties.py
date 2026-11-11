import json
from fbsite import *

import os
RA = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "ra_premiums.json")))

NET_HMO = "https://healthnav.bcbsnc.com/?ci=COMMERCIAL&network_id=6"
NET_PPO = "https://healthnav.bcbsnc.com/?ci=COMMERCIAL&network_id=3"

# plan ids (HMO, PPO) by design
DESIGNS = [
    ("Bronze Basic", "11512NC0430073", "11512NC0060004", "bronze"),
    ("Bronze Standard", "11512NC0430081", "11512NC0060052", "bronze"),
    ("Bronze Complete", "11512NC0430065", "11512NC0060031", "bronze"),
    ("Bronze HSA Eligible Plus", "11512NC0430089", "11512NC0060059", "bronze"),
    ("Silver Preferred", "11512NC0430036", "11512NC0060002", "silver"),
    ("Silver Standard", "11512NC0430052", "11512NC0060051", "silver"),
    ("Silver Choice A", "11512NC0430048", "11512NC0060028", "silver"),
    ("Gold Premier A", "11512NC0430018", "11512NC0060018", "gold"),
    ("Gold Standard A", "11512NC0430022", "11512NC0060050", "gold"),
    ("Gold All Copay A", "11512NC0430027", "11512NC0060067", "gold"),
]
DED = {"Bronze Basic": "$7,000", "Bronze Standard": "$7,500", "Bronze Complete": "$4,000 + $1,000 Rx", "Bronze HSA Eligible Plus": "$8,700",
       "Silver Preferred": "$2,700", "Silver Standard": "$6,400", "Silver Choice A": "$3,500 + $200 Rx",
       "Gold Premier A": "$1,800 + $400 Rx", "Gold Standard A": "$2,500", "Gold All Copay A": "$0"}
MOOP = {"Bronze Basic": "$12,000", "Bronze Standard": "$12,000", "Bronze Complete": "$12,000", "Bronze HSA Eligible Plus": "$8,700",
        "Silver Preferred": "$12,000", "Silver Standard": "$10,300", "Silver Choice A": "$12,000",
        "Gold Premier A": "$12,000", "Gold Standard A": "$8,600", "Gold All Copay A": "$12,000"}

# Plan descriptions (benefits identical in every county that sells these 20 plans)
PLAN_TEXT = {
    "Bronze Basic": ("$7,000 deductible (medical and drugs combined) &middot; $12,000 out-of-pocket max &middot; HSA-eligible",
        "The cheapest plan in the county and the one most subsidized households get for $0. Three primary care visits a year are free, then $95; specialists are $175; preferred generics are $25. Everything else, including brand drugs, imaging, the emergency room and hospital stays, is 50% coinsurance after you meet the $7,000 deductible. You are buying protection against a catastrophe, not day-to-day coverage.",
        "healthy adults, anyone whose subsidy makes it free, HSA savers who want the lowest premium"),
    "Bronze Standard": ("$7,500 deductible &middot; $12,000 out-of-pocket max &middot; HSA-eligible &middot; 4-tier drug list",
        "The federally standardized Bronze design: $50 primary care and $100 specialist copays from day one, $25 generics, and after the deductible flat copays of $50 (preferred brand), $100 (non-preferred) and $500 (specialty). The higher deductible is the trade-off for predictable copays and for the simpler 4-tier drug list where every generic costs the same.",
        "people who want Bronze pricing but see a doctor a few times a year and prefer copays to coinsurance"),
    "Bronze Complete": ("$4,000 medical deductible plus a separate $1,000 drug deductible &middot; $12,000 out-of-pocket max &middot; HSA-eligible",
        "The lowest medical deductible among the Bronze plans. Primary care is $60, specialists $120, generics $20. Brand drugs become $75 (preferred) or $150 (non-preferred) copays once you have met the separate $1,000 drug deductible, which is reached quickly on any brand medication. Hospital care is 50% after the $4,000 medical deductible.",
        "Bronze buyers with one or two brand-name prescriptions, or who want a lower deductible for a likely procedure without paying for Silver"),
    "Bronze HSA Eligible Plus": ("$8,700 deductible equal to the out-of-pocket max &middot; HSA-eligible",
        "A true high-deductible plan: you pay everything except preventive care until you reach $8,700, and then the plan pays 100%. There are no copays to track. The appeal is the hard ceiling: $8,700 is the most you can spend in a year on in-network care, versus $12,000 on the other Bronze plans. Pair it with the maximum HSA contribution and the deductible is partly funded with pre-tax dollars.",
        "disciplined HSA savers and anyone who wants the lowest possible worst-case cost on a Bronze premium"),
    "Silver Preferred": ("$2,700 deductible &middot; $12,000 out-of-pocket max &middot; with cost-sharing reductions at $30,000 income: $325 deductible, $4,000 max",
        "The cheapest Silver and the one that benefits most from cost-sharing reductions. Three free primary care visits then $35, specialists $75, generics $15. The weakness is drugs: every brand and specialty drug is 50% coinsurance after the deductible. For a subsidized household with a $325 deductible that hardly matters; at full price with a brand prescription, Silver Standard is the better Silver.",
        "households under about 250% of the poverty level who want the lowest Silver premium and mostly generic prescriptions"),
    "Silver Standard": ("$6,400 deductible &middot; $10,300 out-of-pocket max &middot; 4-tier drug list &middot; with cost-sharing reductions at $30,000 income: $800 deductible, $3,600 max",
        "The federally standardized Silver and the county's benchmark plan (your subsidy is calculated from its price). The high deductible applies to hospital care, but most everyday care does not touch it: $40 primary care, $80 specialist, $20 generics and $40 preferred brand drugs are copays from day one. Non-preferred brands ($80) and specialty drugs ($350) apply after the deductible.",
        "anyone taking a preferred brand-name drug, and subsidized households who want flat copays for doctor visits and prescriptions"),
    "Silver Choice A": ("$3,500 medical deductible plus $200 drug deductible &middot; $12,000 out-of-pocket max",
        "A middle path between the two other Silvers: three free primary care visits then $45, specialists $95, generics $15, and brand drugs at $35 (preferred) or $70 (non-preferred) copays after a small $200 drug deductible. Specialty drugs and hospital care are 50% after the deductibles. It costs a little more than Silver Standard and in most cases offers less, unless you value the free primary care visits and the lower medical deductible.",
        "people who want a lower medical deductible than Silver Standard and take at most one or two brand drugs"),
    "Gold Premier A": ("$1,800 medical deductible plus $400 drug deductible &middot; $12,000 out-of-pocket max",
        "The cheapest Gold. Three free primary care visits then $15, specialists $45, generics $10, brand drugs $35 or $60 after the $400 drug deductible. Hospital and emergency care are 30% after the $1,800 deductible, and specialty drugs are 50% after the deductible, which is the catch: this plan is strong for doctor visits and ordinary prescriptions but weak for specialty medications.",
        "frequent doctor visits and brand-name (not specialty) prescriptions, at the lowest Gold price"),
    "Gold Standard A": ("$2,500 deductible &middot; $8,600 out-of-pocket max &middot; 4-tier drug list",
        "The federally standardized Gold, with the lowest out-of-pocket maximum in the county. Primary care $30, specialists $60, generics $15, preferred brand $30, non-preferred $60 and specialty $250, all as copays with no deductible. The deductible applies only to hospital-level care, which is then 25% coinsurance. For about $11 a month more than Gold Premier A you get a far better specialty-drug benefit and a $3,400 lower worst case.",
        "anyone on a specialty drug, and people who want the lowest possible out-of-pocket maximum"),
    "Gold All Copay A": ("$0 deductible &middot; $12,000 out-of-pocket max",
        "No deductible at all. Every service is a fixed copay: $30 primary care, $60 specialist, $10 generic, $60 preferred brand, $120 non-preferred, $220 specialty, $1,500 emergency room and $2,500 per hospital stay. You give up the lower out-of-pocket maximum of Gold Standard A in exchange for never having to meet a deductible, which some people find worth about $15 a month for the predictability alone.",
        "people who want to know the price of every visit in advance, and those expecting a hospital stay (a $2,500 copay versus 25&ndash;50% coinsurance elsewhere)"),
}

# County configs. ra: rating area key. towns: for title/lede. hospitals: sentence fragment.
COUNTIES = [
    dict(slug="carteret", name="Carteret", fips="37031", ra="ra16",
         towns="Morehead City, Beaufort, Newport, Emerald Isle, Atlantic Beach, Cape Carteret, Harkers Island and Down East",
         short="Morehead City, Beaufort, Newport, Emerald Isle",
         hospitals="Carteret Health Care in Morehead City, CarolinaEast in New Bern and ECU Health in Greenville are the hospitals most residents use"),
    dict(slug="beaufort", name="Beaufort", fips="37013", ra="ra16",
         towns="Washington, Belhaven, Chocowinity, Aurora and Bath", short="Washington, Belhaven, Chocowinity",
         hospitals="ECU Health Beaufort in Washington and ECU Health Medical Center in Greenville are the hospitals most residents use"),
    dict(slug="craven", name="Craven", fips="37049", ra="ra16",
         towns="New Bern, Havelock, Trent Woods, River Bend, Bridgeton and Vanceboro", short="New Bern, Havelock, Trent Woods",
         hospitals="CarolinaEast Medical Center in New Bern is the hospital most residents use, with ECU Health in Greenville for tertiary care"),
    dict(slug="dare", name="Dare", fips="37055", ra="ra16",
         towns="Manteo, Nags Head, Kill Devil Hills, Kitty Hawk, Southern Shores, Duck and Hatteras Island", short="Nags Head, Kill Devil Hills, Kitty Hawk, Manteo",
         hospitals="Outer Banks Health in Nags Head is the local hospital, with ECU Health in Greenville and Sentara in Norfolk for tertiary care (Norfolk is out of state, which is where the network choice matters)"),
    dict(slug="hyde", name="Hyde", fips="37095", ra="ra16",
         towns="Swan Quarter, Engelhard, Fairfield and Ocracoke", short="Swan Quarter, Engelhard, Ocracoke",
         hospitals="ECU Health Beaufort in Washington and Outer Banks Health in Nags Head are the nearest hospitals"),
    dict(slug="jones", name="Jones", fips="37103", ra="ra16",
         towns="Trenton, Pollocksville and Maysville", short="Trenton, Pollocksville, Maysville",
         hospitals="CarolinaEast in New Bern and UNC Health Lenoir in Kinston are the nearest hospitals"),
    dict(slug="lenoir", name="Lenoir", fips="37107", ra="ra16",
         towns="Kinston, La Grange, Pink Hill and Deep Run", short="Kinston, La Grange, Pink Hill",
         hospitals="UNC Health Lenoir in Kinston is the local hospital, with ECU Health in Greenville for tertiary care"),
    dict(slug="pamlico", name="Pamlico", fips="37137", ra="ra16",
         towns="Bayboro, Oriental, Grantsboro, Alliance and Arapahoe", short="Bayboro, Oriental, Grantsboro",
         hospitals="CarolinaEast in New Bern is the nearest hospital"),
    dict(slug="tyrrell", name="Tyrrell", fips="37177", ra="ra16",
         towns="Columbia and the Scuppernong communities", short="Columbia",
         hospitals="Washington Regional Medical Center in Plymouth and Outer Banks Health in Nags Head are the nearest hospitals"),
    dict(slug="washington", name="Washington", fips="37187", ra="ra16",
         towns="Plymouth, Roper and Creswell", short="Plymouth, Roper, Creswell",
         hospitals="Washington Regional Medical Center in Plymouth is the local hospital, with ECU Health in Greenville for tertiary care"),
    dict(slug="bertie", name="Bertie", fips="37015", ra="ra12",
         towns="Windsor, Aulander, Colerain and Lewiston Woodville", short="Windsor, Aulander, Colerain",
         hospitals="ECU Health Bertie in Windsor is the local hospital, with ECU Health in Greenville for tertiary care"),
    dict(slug="camden", name="Camden", fips="37029", ra="ra12",
         towns="Camden, South Mills and Shiloh", short="Camden, South Mills",
         hospitals="Sentara Albemarle Medical Center in Elizabeth City is the nearest hospital; many residents also use hospitals in Chesapeake and Norfolk, Virginia, which is where the network choice matters"),
    dict(slug="chowan", name="Chowan", fips="37041", ra="ra12",
         towns="Edenton and the surrounding communities", short="Edenton",
         hospitals="ECU Health Chowan in Edenton is the local hospital"),
    dict(slug="currituck", name="Currituck", fips="37053", ra="ra12",
         towns="Currituck, Moyock, Grandy, Corolla and Knotts Island", short="Moyock, Corolla, Grandy",
         hospitals="Sentara Albemarle in Elizabeth City is the nearest North Carolina hospital; many residents use Chesapeake Regional or Sentara hospitals in Virginia, which is where the network choice matters"),
    dict(slug="gates", name="Gates", fips="37073", ra="ra12",
         towns="Gatesville, Sunbury and Gates", short="Gatesville, Sunbury",
         hospitals="Sentara Albemarle in Elizabeth City and ECU Health Roanoke-Chowan in Ahoskie are the nearest North Carolina hospitals; some residents use hospitals in Suffolk and Chesapeake, Virginia"),
    dict(slug="halifax", name="Halifax", fips="37083", ra="ra12",
         towns="Roanoke Rapids, Weldon, Halifax, Scotland Neck, Enfield and Littleton", short="Roanoke Rapids, Weldon, Scotland Neck",
         hospitals="ECU Health North in Roanoke Rapids is the local hospital"),
    dict(slug="hertford", name="Hertford", fips="37091", ra="ra12",
         towns="Ahoskie, Murfreesboro, Winton and Harrellsville", short="Ahoskie, Murfreesboro, Winton",
         hospitals="ECU Health Roanoke-Chowan in Ahoskie is the local hospital"),
    dict(slug="martin", name="Martin", fips="37117", ra="ra12",
         towns="Williamston, Robersonville, Jamesville and Oak City", short="Williamston, Robersonville",
         hospitals="with the Williamston hospital closed, ECU Health Beaufort in Washington and ECU Health Medical Center in Greenville are the hospitals most residents use"),
    dict(slug="northampton", name="Northampton", fips="37131", ra="ra12",
         towns="Jackson, Gaston, Conway, Rich Square, Garysburg and the Lake Gaston communities", short="Jackson, Gaston, Conway, Lake Gaston",
         hospitals="ECU Health North in Roanoke Rapids is the nearest hospital"),
    dict(slug="pasquotank", name="Pasquotank", fips="37139", ra="ra12",
         towns="Elizabeth City and the surrounding communities", short="Elizabeth City",
         hospitals="Sentara Albemarle Medical Center in Elizabeth City is the local hospital; for tertiary care many residents go to Norfolk, Virginia, which is where the network choice matters"),
    dict(slug="perquimans", name="Perquimans", fips="37143", ra="ra12",
         towns="Hertford and Winfall", short="Hertford, Winfall",
         hospitals="Sentara Albemarle in Elizabeth City and ECU Health Chowan in Edenton are the nearest hospitals"),
    # rating area 14: the same 20 Blue Care and Blue Advantage designs under rating-area-14 plan numbers and prices (Nash County, which also has Blue Home, is in county_multi.py)
    dict(slug="edgecombe", name="Edgecombe", fips="37065", ra="ra14", updated="2026-11-10",
         towns="Tarboro, Pinetops, Princeville, Macclesfield and the Edgecombe side of Rocky Mount", short="Tarboro, Pinetops, Princeville",
         hospitals="ECU Health Edgecombe Hospital in Tarboro is the local hospital, with ECU Health Medical Center in Greenville for tertiary care"),
    dict(slug="greene", name="Greene", fips="37079", ra="ra14", updated="2026-11-10",
         towns="Snow Hill, Hookerton, Walstonburg and Maury", short="Snow Hill, Hookerton",
         hospitals="the nearest hospitals are ECU Health Medical Center in Greenville and UNC Health Lenoir in Kinston"),
    dict(slug="pitt", name="Pitt", fips="37147", ra="ra14", updated="2026-11-10",
         towns="Greenville, Winterville, Ayden, Farmville, Grifton and Bethel", short="Greenville, Winterville, Ayden, Farmville",
         hospitals="ECU Health Medical Center in Greenville, the region's academic medical center, is the hospital most residents use"),
    dict(slug="wayne", name="Wayne", fips="37191", ra="ra14", updated="2026-11-10",
         towns="Goldsboro, Mount Olive, Fremont, Pikeville and Seven Springs", short="Goldsboro, Mount Olive, Fremont",
         hospitals="UNC Health Wayne in Goldsboro is the local hospital, with ECU Health Medical Center in Greenville and the Raleigh hospitals for specialty care"),
    dict(slug="wilson", name="Wilson", fips="37195", ra="ra14", updated="2026-11-10",
         towns="Wilson, Elm City, Stantonsburg, Black Creek, Lucama and Sharpsburg", short="Wilson, Elm City, Stantonsburg",
         hospitals="Wilson Medical Center is the local hospital, with ECU Health Medical Center in Greenville and UNC Health Nash in Rocky Mount nearby"),
]
CARTERET_LIKE = [c for c in COUNTIES]

# Guides built by their own module (multi-carrier counties); listed with the others on the index pages
def _m(slug, name, fips, ra, short):
    return dict(slug=slug, name=name, fips=fips, ra=ra, module="county_multi", updated="2026-11-10", short=short)


# Counties built by county_multi.py from zones_2027.json (several insurers or several Blue Cross networks)
MULTI_GUIDES = [
    _m("avery", "Avery", "37011", "ra1", "Newland, Banner Elk, Linville"),
    _m("buncombe", "Buncombe", "37021", "ra1", "Asheville, Black Mountain, Weaverville"),
    _m("cherokee", "Cherokee", "37039", "ra1", "Murphy, Andrews"),
    _m("clay", "Clay", "37043", "ra1", "Hayesville, Warne"),
    _m("graham", "Graham", "37075", "ra1", "Robbinsville, Fontana Lake"),
    _m("haywood", "Haywood", "37087", "ra1", "Waynesville, Canton, Maggie Valley"),
    _m("henderson", "Henderson", "37089", "ra1", "Hendersonville, Fletcher, Mills River"),
    _m("jackson", "Jackson", "37099", "ra1", "Sylva, Cullowhee, Cashiers"),
    _m("macon", "Macon", "37113", "ra1", "Franklin, Highlands"),
    _m("madison", "Madison", "37115", "ra1", "Marshall, Mars Hill, Hot Springs"),
    _m("mcdowell", "McDowell", "37111", "ra1", "Marion, Old Fort"),
    _m("mitchell", "Mitchell", "37121", "ra1", "Bakersville, Spruce Pine"),
    _m("polk", "Polk", "37149", "ra1", "Columbus, Tryon, Saluda"),
    _m("rutherford", "Rutherford", "37161", "ra1", "Rutherfordton, Forest City, Spindale"),
    _m("swain", "Swain", "37173", "ra1", "Bryson City, Whittier"),
    _m("transylvania", "Transylvania", "37175", "ra1", "Brevard, Rosman, Lake Toxaway"),
    _m("yancey", "Yancey", "37199", "ra1", "Burnsville, Micaville"),
    _m("alexander", "Alexander", "37003", "ra2", "Taylorsville, Hiddenite"),
    _m("burke", "Burke", "37023", "ra2", "Morganton, Valdese, Hildebran"),
    _m("caldwell", "Caldwell", "37027", "ra2", "Lenoir, Granite Falls, Hudson"),
    _m("catawba", "Catawba", "37035", "ra2", "Hickory, Newton, Conover"),
    _m("iredell", "Iredell", "37097", "ra2", "Statesville, Mooresville, Troutman"),
    _m("alleghany", "Alleghany", "37005", "ra3", "Sparta, Glade Valley"),
    _m("ashe", "Ashe", "37009", "ra3", "Jefferson, West Jefferson, Lansing"),
    _m("watauga", "Watauga", "37189", "ra3", "Boone, Blowing Rock, Beech Mountain"),
    _m("wilkes", "Wilkes", "37193", "ra3", "Wilkesboro, North Wilkesboro"),
    _m("anson", "Anson", "37007", "ra4", "Wadesboro, Polkton, Ansonville"),
    _m("cabarrus", "Cabarrus", "37025", "ra4", "Concord, Kannapolis, Harrisburg"),
    _m("mecklenburg", "Mecklenburg", "37119", "ra4", "Charlotte, Huntersville, Matthews, Cornelius"),
    _m("rowan", "Rowan", "37159", "ra4", "Salisbury, China Grove, Spencer"),
    _m("stanly", "Stanly", "37167", "ra4", "Albemarle, Locust, Norwood"),
    _m("union", "Union", "37179", "ra4", "Monroe, Indian Trail, Waxhaw"),
    _m("cleveland", "Cleveland", "37045", "ra5", "Shelby, Kings Mountain, Boiling Springs"),
    _m("gaston", "Gaston", "37071", "ra5", "Gastonia, Belmont, Mount Holly"),
    _m("lincoln", "Lincoln", "37109", "ra5", "Lincolnton, Denver"),
    _m("davidson", "Davidson", "37057", "ra6", "Lexington, Thomasville"),
    _m("davie", "Davie", "37059", "ra6", "Mocksville, Bermuda Run, Advance"),
    _m("forsyth", "Forsyth", "37067", "ra6", "Winston-Salem, Kernersville, Clemmons"),
    _m("stokes", "Stokes", "37169", "ra6", "King, Walnut Cove, Danbury"),
    _m("surry", "Surry", "37171", "ra6", "Mount Airy, Elkin, Dobson, Pilot Mountain"),
    _m("yadkin", "Yadkin", "37197", "ra6", "Yadkinville, Jonesville, East Bend"),
    _m("guilford", "Guilford", "37081", "ra7", "Greensboro, High Point, Jamestown"),
    _m("randolph", "Randolph", "37151", "ra7", "Asheboro, Archdale, Randleman"),
    _m("rockingham", "Rockingham", "37157", "ra7", "Reidsville, Eden, Madison"),
    _m("montgomery", "Montgomery", "37123", "ra8", "Troy, Biscoe, Candor, Mount Gilead"),
    _m("moore", "Moore", "37125", "ra8", "Southern Pines, Pinehurst, Aberdeen, Carthage"),
    _m("bladen", "Bladen", "37017", "ra9", "Elizabethtown, Bladenboro, White Lake"),
    _m("cumberland", "Cumberland", "37051", "ra9", "Fayetteville, Hope Mills, Spring Lake"),
    _m("harnett", "Harnett", "37085", "ra9", "Lillington, Dunn, Angier, Erwin"),
    _m("hoke", "Hoke", "37093", "ra9", "Raeford"),
    _m("richmond", "Richmond", "37153", "ra9", "Rockingham, Hamlet, Ellerbe"),
    _m("robeson", "Robeson", "37155", "ra9", "Lumberton, Pembroke, Red Springs"),
    _m("sampson", "Sampson", "37163", "ra9", "Clinton, Roseboro, Newton Grove"),
    _m("scotland", "Scotland", "37165", "ra9", "Laurinburg, Wagram"),
    _m("granville", "Granville", "37077", "ra10", "Oxford, Creedmoor, Butner"),
    _m("vance", "Vance", "37181", "ra10", "Henderson, Kittrell"),
    _m("warren", "Warren", "37185", "ra10", "Warrenton, Norlina, Lake Gaston"),
    _m("alamance", "Alamance", "37001", "ra11", "Burlington, Graham, Mebane, Elon"),
    _m("caswell", "Caswell", "37033", "ra11", "Yanceyville, Milton"),
    _m("chatham", "Chatham", "37037", "ra11", "Pittsboro, Siler City, Fearrington"),
    _m("durham", "Durham", "37063", "ra11", "Durham, Research Triangle Park"),
    _m("lee", "Lee", "37105", "ra11", "Sanford, Broadway"),
    _m("orange", "Orange", "37135", "ra11", "Chapel Hill, Carrboro, Hillsborough"),
    _m("person", "Person", "37145", "ra11", "Roxboro, Timberlake"),
    _m("franklin", "Franklin", "37069", "ra13", "Louisburg, Youngsville, Franklinton"),
    _m("johnston", "Johnston", "37101", "ra13", "Smithfield, Clayton, Selma, Benson"),
    _m("wake", "Wake", "37183", "ra13", "Raleigh, Cary, Apex, Wake Forest"),
    _m("nash", "Nash", "37127", "ra14", "Rocky Mount, Nashville, Spring Hope"),
    _m("brunswick", "Brunswick", "37019", "ra15", "Leland, Southport, Oak Island, Shallotte"),
    _m("columbus", "Columbus", "37047", "ra15", "Whiteville, Tabor City, Chadbourn"),
    _m("duplin", "Duplin", "37061", "ra15", "Wallace, Warsaw, Kenansville, Beulaville"),
    _m("onslow", "Onslow", "37133", "ra15", "Jacksonville, Swansboro, Richlands"),
    _m("pender", "Pender", "37141", "ra15", "Hampstead, Burgaw, Surf City"),
]

# Guides built by their own module (multi-carrier counties); listed with the others on the index pages
OTHER_GUIDES = [
    dict(slug="new-hanover", name="New Hanover", fips="37129", ra="ra15", module="county_nh", updated="2026-11-10",
         short="Wilmington, Carolina Beach, Wrightsville Beach"),
] + MULTI_GUIDES


def money(x):
    return "${:,.0f}".format(round(x))


def designs_for(ra):
    """(design, Blue Care plan id, Blue Advantage plan id, metal) in a rating area. Blue Care plan numbers differ by rating area
    (rating areas 12 and 16 share the ids in DESIGNS); Blue Advantage's are statewide."""
    names = {v["name"]: pid for pid, v in RA[ra]["s45_100k"].items()}
    out = [(d, names["Blue Care " + d], names["Blue Advantage " + d], metal) for d, hmo, ppo, metal in DESIGNS]
    if ra in ("ra12", "ra16"):
        assert out == DESIGNS, ra
    return out


# Blue Advantage's premium over the same Blue Care design (rating areas 12 and 16 keep the published "about 5.5%")
def ppo_pct(ra):
    ds = designs_for(ra)
    r = sum(RA[ra]["s45_100k"][ppo]["premium"] for d, hmo, ppo, m in ds) / sum(RA[ra]["s45_100k"][hmo]["premium"] for d, hmo, ppo, m in ds)
    if ra in ("ra12", "ra16"):
        assert 1.05 < r < 1.06, (ra, r)
        return "5.5%"
    return f"{100 * (r - 1):.1f}%"


def prem(ra, scenario, pid, net=False):
    p = RA[ra][scenario][pid]
    return money(p["net"] if net else p["premium"])


def _county_page(c):
    ra = c["ra"]
    name = c["name"]
    path = f"/counties/{c['slug']}/"
    full_name = f"{name} County"
    import fbsite
    DATE_H = fbsite.UPDATED_H
    DS = designs_for(ra)
    ID = {d: (hmo, ppo) for d, hmo, ppo, m in DS}
    PCT = ppo_pct(ra)
    h = lambda pid: RA[ra]["s45_100k"][pid]
    # price ranges at 45 (HMO)
    def rng(metal):
        vals = [h(hmo)["premium"] for d, hmo, ppo, m in DS if m == metal]
        return f"{money(min(vals))} to {money(max(vals))}"
    bb_hmo, bb_ppo = DS[0][1], DS[0][2]
    ppo_delta_45 = [RA[ra]["s45_100k"][ppo]["premium"] - RA[ra]["s45_100k"][hmo]["premium"] for d, hmo, ppo, m in DS]
    ppo_delta_60 = [RA[ra]["s60_100k"][ppo]["premium"] - RA[ra]["s60_100k"][hmo]["premium"] for d, hmo, ppo, m in DS]
    sp, ss, gs = ID["Silver Preferred"][0], ID["Silver Standard"][0], ID["Gold Standard A"][0]
    gold_vs_bronze = [RA[ra]["s45_100k"][hmo]["premium"] for d, hmo, p, m in DS if m == "gold"]
    bronze_45 = [RA[ra]["s45_100k"][hmo]["premium"] for d, hmo, p, m in DS if m == "bronze"]
    # what the template says about every rating area it serves
    ids = [x for d, hmo, ppo, m in DS for x in (hmo, ppo)]
    assert set(ids) == set(RA[ra]["s45_100k"]), ra
    prem45 = {x: RA[ra]["s45_100k"][x]["premium"] for x in ids}
    silv = sorted((prem45[x], x) for d, hmo, ppo, m in DS if m == "silver" for x in (hmo, ppo))
    assert silv[1][1] == ss and silv[0][1] == sp, "benchmark / cheapest Silver changed"
    assert min(prem45, key=prem45.get) == bb_hmo, "Bronze Basic is no longer the cheapest plan"
    assert min((prem45[hmo], hmo) for d, hmo, ppo, m in DS if m == "gold")[1] == ID["Gold Premier A"][0]
    assert all(RA[ra]["s45_30k"][x]["net"] == 0 for d, hmo, ppo, m in DS if m == "bronze" for x in (hmo, ppo)), "Bronze no longer free at $30,000"
    assert RA[ra]["fam90k"][bb_hmo]["net"] == 0, "family Bronze no longer free"
    assert 10.5 < prem45[gs] - prem45[ID["Gold Premier A"][0]] < 11.5 and 15 < prem45[ID["Gold All Copay A"][0]] - prem45[gs] < 16
    assert prem45[ID["Silver Choice A"][0]] > prem45[ss]
    g_minus_b_lo = min(gold_vs_bronze) - max(bronze_45)
    g_minus_b_hi = max(gold_vs_bronze) - min(bronze_45)

    TITLE = f"{full_name}, NC Health Insurance for 2027: All 20 Blue Cross Plans Explained"
    DESC = f"Every 2027 ACA Marketplace plan in {full_name}, NC ({c['short']}): prices by age and income, Blue Care HMO vs. Blue Advantage PPO, which plan fits which situation, and the drug-list question answered."
    CRUMBS = [("/", "Home"), ("/counties/", "County Guides"), (None, full_name)]

    if ra in ("ra12", "ra16"):
        MOVE = "The same 20 plans are sold in every county from the Crystal Coast to the Albemarle Sound and the Virginia line (see the list at the end of this guide), so a move within that group usually lets you keep your plan; the premium changes if the new county is in a different rating area."
    else:
        MOVE = "The same 20 plans are sold in Edgecombe, Greene, Pitt, Wayne and Wilson counties (see the list at the end of this guide), so a move within that group usually lets you keep your plan. Blue Cross sells the same 10 designs, under different plan numbers and prices, from the Crystal Coast to the Albemarle Sound and in Nash County."
    FAQ = [
        (f"Why is Blue Cross the only insurer in {full_name}?",
         f"For 2027, Blue Cross and Blue Shield of North Carolina is the only carrier offering individual Marketplace plans in {full_name}. The other insurers that sell Marketplace plans elsewhere in North Carolina for 2027 (Ambetter, AmeriHealth Caritas Next, Oscar and UnitedHealthcare) do not include {name} in their service areas. That still leaves 20 plans: 10 designs, each sold with a statewide HMO network (Blue Care) and a nationwide PPO network (Blue Advantage)."),
        ("Is my local hospital in network?",
         f"Blue Care is Blue Cross NC's statewide network and Blue Advantage adds the national BlueCard network. In {full_name}, {c['hospitals']}. Networks change, so confirm your doctors and hospital in the official directory (links in the network section above) before you enroll, and tell us if a specific doctor matters to you."),
        ("Do I need a referral to see a specialist?",
         "No. Neither Blue Care nor Blue Advantage requires a referral from a primary care doctor to see a specialist."),
        ("Should I buy the PPO if I travel or spend winters out of state?",
         f"That is the main reason to. Blue Advantage costs about {PCT} more than the same Blue Care design and gives you in-network access to Blue Cross doctors nationwide. Its out-of-network benefit is weak (50 to 80% coinsurance after the deductible, with no out-of-pocket cap), so the value is the larger in-network footprint, not out-of-network coverage. If you live in North Carolina year-round and your doctors are here, the HMO delivers the same benefits for less."),
        (f"Is there a catastrophic plan in {full_name}?",
         f"No. For 2027 no catastrophic plan is offered in {full_name}, even for people under 30. The Bronze plans are the lowest-premium options."),
        ("What happens if my income is under about $22,000?",
         "North Carolina expanded Medicaid in December 2023. A single adult with income under roughly 138% of the federal poverty level (about $22,000 for one person, $29,900 for a couple, $45,500 for a family of four in 2027) is directed to NC Medicaid rather than receiving a Marketplace subsidy. The Marketplace application checks this automatically."),
        ("Do the two drug lists cover different drugs?",
         "No. We tested 48 common brand and generic drugs against both lists and found no differences in coverage. The three Standard plans use Blue Cross NC's 4-tier list with flat copays; the other seven designs use the 5-tier list, where the lowest copay applies only to Tier 1 preferred generics. What changes your drug costs is the plan design (copay vs. coinsurance, and whether the deductible applies), not which list it uses."),
        ("Can I keep my plan if I move to another county?",
         f"Moving to a new county is a qualifying life event. {MOVE} A move elsewhere gives you a 60-day special enrollment period to pick a new plan."),
        ("When can I enroll?",
         "Open Enrollment for 2027 coverage runs November 1, 2026 through January 15, 2027 on HealthCare.gov. Enroll by December 15 for coverage starting January 1. Outside Open Enrollment you need a qualifying event, such as losing other coverage, moving, marriage or a new baby."),
    ]

    # tables
    age_rows = "".join(
        f'<tr><td>{d}</td><td class="num">{prem(ra,"s30_100k",hmo)}</td><td class="num">{prem(ra,"s45_100k",hmo)}</td><td class="num">{prem(ra,"s60_100k",hmo)}</td><td class="num">{DED[d]}</td><td class="num">{MOOP[d]}</td></tr>'
        for d, hmo, ppo, m in DS)
    sub_rows = "".join([
        f'<tr><td>Single, 45, $30,000</td><td class="num">{prem(ra,"s45_30k",bb_hmo,True)}</td><td class="num">{prem(ra,"s45_30k",sp,True)} (CSR: $325 ded., $4,000 max)</td><td class="num">{prem(ra,"s45_30k",ss,True)} (CSR: $800 ded., $3,600 max)</td><td class="num">{prem(ra,"s45_30k",gs,True)}</td></tr>',
        f'<tr><td>Single, 45, $45,000</td><td class="num">{prem(ra,"s45_45k",bb_hmo,True)}</td><td class="num">{prem(ra,"s45_45k",sp,True)}</td><td class="num">{prem(ra,"s45_45k",ss,True)}</td><td class="num">{prem(ra,"s45_45k",gs,True)}</td></tr>',
        f'<tr><td>Single, 45, $100,000</td><td class="num">{prem(ra,"s45_100k",bb_hmo)}</td><td class="num">{prem(ra,"s45_100k",sp)}</td><td class="num">{prem(ra,"s45_100k",ss)}</td><td class="num">{prem(ra,"s45_100k",gs)}</td></tr>',
        f'<tr><td>Single, 27, $35,000</td><td class="num">{prem(ra,"a27_35k",bb_hmo,True)}</td><td class="num">{prem(ra,"a27_35k",sp,True)} (CSR: $2,000 ded.)</td><td class="num">{prem(ra,"a27_35k",ss,True)} (CSR: $2,900 ded.)</td><td class="num">{prem(ra,"a27_35k",gs,True)}</td></tr>',
        f'<tr><td>Couple, 62 and 60, $58,000</td><td class="num">{prem(ra,"c62_60_58k",bb_hmo,True)}</td><td class="num">{prem(ra,"c62_60_58k",sp,True)}</td><td class="num">{prem(ra,"c62_60_58k",ss,True)}</td><td class="num">{prem(ra,"c62_60_58k",gs,True)}</td></tr>',
        f'<tr><td>Family of four (45, 43, 12, 9), $90,000</td><td class="num">{prem(ra,"fam90k",bb_hmo,True)}</td><td class="num">{prem(ra,"fam90k",sp,True)}</td><td class="num">{prem(ra,"fam90k",ss,True)}</td><td class="num">{prem(ra,"fam90k",gs,True)}</td></tr>',
    ])

    def plan_card(d, hmo, ppo, metal):
        meta, text, best = PLAN_TEXT[d]
        return f"""<details class="plan {metal}">
<summary><span class="plan-name">{d}</span> <span class="plan-price">{prem(ra,"s45_100k",hmo)} / {prem(ra,"s45_100k",ppo)}</span><span class="plan-best">Best for: {best}</span></summary>
<p class="plan-meta">{meta}</p>
<p>{text}</p>
</details>"""

    plans_html = ""
    for metal, label in [("bronze", "Bronze"), ("silver", "Silver"), ("gold", "Gold")]:
        plans_html += f"<h3>{label}</h3>\n" + "\n".join(plan_card(d, hmo, ppo, m) for d, hmo, ppo, m in DS if m == metal) + "\n"

    grp = ("ra12", "ra16") if ra in ("ra12", "ra16") else ("ra14",)
    link = lambda o: f'<a href="/counties/{o["slug"]}/">{o["name"]}</a>'
    others = ", ".join(link(o) for o in COUNTIES if o["slug"] != c["slug"] and o["ra"] in grp)
    rest = ", ".join(link(o) for o in COUNTIES if o["ra"] not in grp)
    if ra in ("ra12", "ra16"):
        related = (f"<strong>Same 20 plans, other counties:</strong> {others}. Premiums differ slightly between the Albemarle-area counties and the Pamlico Sound and coastal counties, which are in different rating areas. "
                   f"The same 10 designs are also sold, under different plan numbers and prices, in {rest}.")
    else:
        related = (f"<strong>Same 20 plans, other counties:</strong> {others}. The same 10 designs are sold under different plan numbers and prices from the Crystal Coast to the Albemarle Sound ({rest}), "
                   f'and with a third Blue Cross network in <a href="/counties/nash/">Nash County</a>.')

    body = f"""
<h1>Health Insurance in {full_name}, NC for 2027: All 20 Blue Cross Plans Explained</h1>
{byline("12 minute read")}

<p class="lede">If you buy your own health insurance in {full_name} ({c['towns']}) you have one insurer, Blue Cross and Blue Shield of North Carolina, and 20 Marketplace plans to choose from. This guide uses the official HealthCare.gov plan data for 2027 to explain what the plans cost, how they differ, and which one fits which situation.</p>

<nav class="toc" aria-label="In this guide">
<strong>In this guide</strong>
<ol>
<li><a href="#market">The market at a glance</a> and <a href="#subsidies">what subsidies do</a></li>
<li><a href="#network">Decision 1: Blue Care (HMO) or Blue Advantage (PPO)</a></li>
<li><a href="#metal">Decision 2: how much coverage</a></li>
<li><a href="#drugs">Decision 3: how prescriptions are priced</a></li>
<li><a href="#plans">The 10 plan designs</a> (click a plan to expand)</li>
<li><a href="#situations">If you are&hellip; look at&hellip;</a></li>
<li><a href="#faq">Questions</a></li>
</ol>
</nav>

<div class="takeaways">
<h2>Key takeaways</h2>
<ul>
<li><strong>20 plans, but only 10 designs.</strong> Each design is sold twice: as a <strong>Blue Care</strong> HMO (statewide network) and a <strong>Blue Advantage</strong> PPO (nationwide network). Deductibles, copays and out-of-pocket maximums are identical within each pair; the PPO costs about {PCT} more.</li>
<li><strong>Full-price premiums for a 45-year-old</strong> run {rng("bronze")} for Bronze, {rng("silver")} for Silver and {rng("gold")} for Gold. A 60-year-old pays about 1.9 times that; a 21-year-old about 0.7 times.</li>
<li><strong>Subsidies change everything below about 400% of the poverty level</strong> ($63,840 for one person, $86,560 for a couple, $132,000 for a family of four). A 45-year-old earning $30,000 gets every Bronze plan for $0 and a cost-sharing-reduced Silver plan for about {prem(ra,"s45_30k",sp,True)} a month. Above the line you pay full price.</li>
<li><strong>Nobody needs a referral</strong> to see a specialist on either network, and emergency care is covered anywhere.</li>
<li><strong>The two drug lists are the same list.</strong> What changes your medication cost is the plan design, especially the three <em>Standard</em> plans with flat brand-drug copays.</li>
<li><strong>No catastrophic plan</strong> is offered in {name} for 2027.</li>
</ul>
</div>

<h2 id="market">The {full_name} market at a glance</h2>
<p>{name} is a one-carrier county. Blue Cross NC offers four Bronze, three Silver and three Gold designs, and every design comes with a choice of network. That makes the decision simpler than it looks: instead of comparing 20 plans, you make three decisions in order: <a href="#network">network</a>, <a href="#metal">how much coverage</a>, and <a href="#drugs">how your prescriptions are priced</a>. The 10 plan designs are then <a href="#plans">described one by one</a>, and a <a href="#situations">situations table</a> maps common {name} households to the plans worth a close look.</p>

<div class="table-wrap">
<table class="data">
<caption>Monthly premiums in {full_name}, Blue Care (HMO) network, full price with no subsidy, 2027. Blue Advantage (PPO) is about {PCT} higher. Source: HealthCare.gov Marketplace API.</caption>
<thead><tr><th>Plan design</th><th class="num">Age 30</th><th class="num">Age 45</th><th class="num">Age 60</th><th class="num">Deductible</th><th class="num">Out-of-pocket max</th></tr></thead>
<tbody>{age_rows}</tbody>
</table>
</div>

<h3 id="subsidies">What subsidies do to those numbers</h3>
<p>The premium tax credit is a fixed dollar amount based on your income and the cost of the second-cheapest Silver plan (here, Blue Care Silver Standard). You can spend it on any plan. Because the enhanced credits of 2021&ndash;2025 have expired, the credit stops entirely at 400% of the federal poverty level, and the Marketplace now recovers any overpaid credit in full at tax time, so your income estimate matters. Here is what the same plans cost real {name} households after the credit:</p>

<div class="table-wrap">
<table class="data">
<caption>Net monthly premium after the premium tax credit, Blue Care network, {full_name}, 2027. "CSR" marks Silver plans with cost-sharing reductions that also cut the deductible. Source: HealthCare.gov Marketplace API.</caption>
<thead><tr><th>Household and income</th><th class="num">Bronze Basic</th><th class="num">Silver Preferred</th><th class="num">Silver Standard</th><th class="num">Gold Standard A</th></tr></thead>
<tbody>{sub_rows}</tbody>
</table>
</div>

<p>Two things to notice. First, for most subsidized households the cheapest Bronze plans are free or nearly free, which is why the question for many {name} families is not "Bronze or Silver?" but "is a $0 Bronze plan with a $7,000 deductible really cheaper than a {prem(ra,"s45_30k",ss,True)} Silver plan with an $800 deductible?" (Usually not, if you expect to use care; see <a href="/questions/bronze-vs-silver-medications/">Bronze vs. Silver when you take medications</a>.) Second, a single adult under about $22,000 or a couple under about $29,900 is sent to NC Medicaid instead of receiving a Marketplace credit; the application sorts this out.</p>

<h2 id="network">Decision 1: Blue Care (HMO) or Blue Advantage (PPO)?</h2>
<p>This is the easiest decision to get right, because the benefits are identical. Pick a design, and the only differences between its Blue Care and Blue Advantage versions are the network and the price.</p>
<ul>
<li><strong>Blue Care</strong> is Blue Cross NC's statewide network. It covers doctors and hospitals across North Carolina, with no referrals required. Out-of-network care is not covered except in an emergency (emergency room visits are covered anywhere in the country at the in-network rate).</li>
<li><strong>Blue Advantage</strong> uses Blue Cross NC's largest network and adds the national BlueCard network, so you are in-network at Blue Cross doctors in every state. It also has an out-of-network benefit, but a thin one: 50% to 80% coinsurance after the deductible, with no out-of-network out-of-pocket maximum. Treat it as a nationwide in-network plan, not as a plan that pays well for out-of-network care.</li>
<li><strong>The price difference is about {PCT}</strong> across the board: {money(min(ppo_delta_45))} to {money(max(ppo_delta_45))} a month at age 45, {money(min(ppo_delta_60))} to {money(max(ppo_delta_60))} at age 60. If your subsidy already covers a Bronze plan with money left over, the PPO upgrade can cost you only a few dollars.</li>
</ul>
<p><strong>Choose Blue Advantage if</strong> you spend months outside North Carolina (snowbirds, a second home), have a dependent at an out-of-state college, run a business that keeps you on the road, regularly use a hospital across the Virginia line, or want a specific out-of-state hospital such as Sentara Norfolk, MUSC, Mayo or Johns Hopkins in network. <strong>Choose Blue Care if</strong> you live here year-round and your doctors are in North Carolina; you get the same benefits for less.</p>
<p>Before enrolling, confirm your doctors in the official directories: <a href="{NET_HMO}" target="_blank" rel="noopener">Blue Care provider search</a> and <a href="{NET_PPO}" target="_blank" rel="noopener">Blue Advantage provider search</a>. In {full_name}, {c['hospitals']}; check the one you would go to.</p>

<h2 id="metal">Decision 2: How much coverage do you expect to use?</h2>
<p>Bronze, Silver and Gold describe how costs are split between you and the plan: roughly 60%, 70% and 80% paid by the plan for an average person. In {name} the practical differences are these:</p>
<ul>
<li><strong>Bronze</strong> ({rng("bronze")} at 45): $7,000&ndash;$8,700 deductibles, so you pay for most care yourself until something serious happens. All four Bronze plans are <strong>HSA-eligible for 2027</strong> under the 2025 federal tax law, which lets you set aside up to $4,500 (single) or $9,000 (family) pre-tax, plus $1,000 if you are 55 or older. Best for people who are healthy, price-driven, or using the plan mainly as protection against a large bill.</li>
<li><strong>Silver</strong> ({rng("silver")}): the plans most people should look at first if they qualify for a subsidy, because incomes under about $39,900 (single) or $82,500 (family of four) unlock <strong>cost-sharing reductions</strong> that only apply to Silver plans. At $30,000 a 45-year-old's Silver Preferred deductible drops from $2,700 to $325 and the out-of-pocket maximum from $12,000 to $4,000. Without a cost-sharing reduction, Silver is a middle ground that often loses to either Bronze or Gold on total cost.</li>
<li><strong>Gold</strong> ({rng("gold")}): $0&ndash;$2,500 deductibles and flat copays for most care. Costs {money(g_minus_b_lo)}&ndash;{money(g_minus_b_hi)} a month more than Bronze at age 45, which is worth it if you take brand-name or specialty drugs, see specialists regularly, or are planning surgery or a pregnancy.</li>
</ul>

<h2 id="drugs">Decision 3: How are your prescriptions priced?</h2>
<p>Blue Cross NC uses two drug lists for these plans: a 4-tier list for the three <strong>Standard</strong> plans (Bronze Standard, Silver Standard, Gold Standard A) and a 5-tier list for the other seven designs. We checked 48 common drugs, from atorvastatin and metformin to Eliquis, Jardiance, Ozempic, Humira and Dupixent, against both lists: <strong>coverage was identical on every one</strong>. Wegovy and Zepbound were not covered on either list; Ozempic, Mounjaro and Trulicity were. The real difference is tiering. On the 5-tier plans the advertised copay ("$25 Tier 1 Rx") applies to preferred generics only; other generics sit in Tier 2 at a higher copay. On the Standard plans every generic gets the same copay.</p>
<p>What matters far more than the list is <strong>how each design treats brand-name and specialty drugs</strong>:</p>
<ul>
<li>On <strong>Bronze Basic, Silver Preferred, Silver Choice A and Gold Premier A</strong>, brand drugs are subject to the deductible (and specialty drugs to 50% coinsurance after it). Someone on a $650-a-month brand drug pays the full deductible before the plan contributes.</li>
<li>On <strong>Silver Standard and Gold Standard A</strong>, preferred brand drugs are a flat $40 or $30 copay with <em>no deductible</em>, and specialty drugs are $350 (after deductible) or $250 (no deductible).</li>
<li>On <strong>Gold All Copay A</strong>, everything is a copay from day one: $60 preferred brand, $120 non-preferred, $220 specialty.</li>
</ul>
<p>The arithmetic is in <a href="/questions/bronze-vs-silver-medications/">Bronze vs. Silver when you take medications</a>, built on these same plans. The short version: one brand-name prescription is enough to make Silver Standard cheaper than Bronze Basic over a year, and a specialty drug makes Gold the cheapest plan on the shelf.</p>

<h2 id="plans">The 10 plan designs, one by one</h2>
<p>Prices are full-price monthly premiums for a 45-year-old in {full_name}, Blue Care / Blue Advantage. Click a plan to expand its details. Benefit amounts are in-network, individual coverage, no cost-sharing reduction.</p>
{plans_html}

<h2 id="situations">If you are&hellip; look at&hellip;</h2>
<div class="table-wrap">
<table class="data">
<caption>Starting points, not recommendations. Prices are monthly in {full_name}, Blue Care network, after any subsidy. Run your own numbers before deciding.</caption>
<thead><tr><th>Situation</th><th>Start with</th><th>Why</th></tr></thead>
<tbody>
<tr><td>Healthy 30-year-old, no prescriptions, $100,000 income</td><td>Bronze Basic ({prem(ra,"s30_100k",bb_hmo)}) or Bronze HSA Eligible Plus ({prem(ra,"s30_100k",ID["Bronze HSA Eligible Plus"][0])})</td><td>No subsidy; you want the lowest premium and a hard cap on a bad year. Fund an HSA.</td></tr>
<tr><td>Self-employed contractor, family of four, $90,000</td><td>Bronze Basic ({prem(ra,"fam90k",bb_hmo,True)}) if everyone is healthy; Silver Standard ({prem(ra,"fam90k",ss,True)}) if anyone takes a brand drug</td><td>Subsidy covers Bronze fully. Bronze Complete ({prem(ra,"fam90k",ID["Bronze Complete"][0],True)}), with its separate $1,000 Rx deductible, is another option for one brand drug.</td></tr>
<tr><td>Single, 45, $30,000, sees a doctor a few times a year</td><td>Silver Preferred ({prem(ra,"s45_30k",sp,True)}) or Silver Standard ({prem(ra,"s45_30k",ss,True)})</td><td>Cost-sharing reductions cut the deductible to $325 or $800. That beats a free Bronze with a $7,000 deductible if you use care at all.</td></tr>
<tr><td>Early retirees, 62 and 60, $58,000 investment and part-time income</td><td>Silver Preferred ({prem(ra,"c62_60_58k",sp,True)}); Bronze Basic ({prem(ra,"c62_60_58k",bb_hmo,True)}) if you can self-insure the deductible</td><td>Keep income under $86,560 or the subsidy disappears. See <a href="/questions/retiring-before-65-north-carolina/">Retiring before 65 in NC</a>.</td></tr>
<tr><td>Spends January through March in Florida</td><td>Blue Advantage version of whichever design fits</td><td>Nationwide in-network access for about {PCT} more. Blue Care covers only emergencies out of state.</td></tr>
<tr><td>Parent with a child at an out-of-state college</td><td>Blue Advantage, or the college's student health plan plus Blue Care for the rest of the family</td><td>The student's routine care near campus is in network on the PPO; a student plan can be cheaper than upgrading the whole family. See <a href="/questions/blue-care-vs-blue-advantage/">Blue Care vs. Blue Advantage</a>.</td></tr>
<tr><td>Takes Eliquis, Jardiance or another preferred brand drug</td><td>Silver Standard or Gold Standard A</td><td>$40 / $30 brand copays with no deductible. See the <a href="/questions/bronze-vs-silver-medications/">medication guide</a>.</td></tr>
<tr><td>Takes a specialty drug (Dupixent, Skyrizi, Enbrel, Rinvoq)</td><td>Gold Standard A or Gold All Copay A</td><td>$250 / $220 specialty copays versus 50% coinsurance on most other plans.</td></tr>
<tr><td>Planning surgery or a pregnancy next year</td><td>Gold Standard A ($8,600 max) or Gold All Copay A ($2,500 per stay)</td><td>You will reach the deductible anyway; buy the plan with the lowest ceiling.</td></tr>
<tr><td>Income near $22,000 (single) or $45,500 (family of four)</td><td>Apply through HealthCare.gov and let it check Medicaid</td><td>NC Medicaid may cover you at no premium; the Marketplace cannot subsidize you below the line.</td></tr>
</tbody>
</table>
</div>

<div class="callout caution">
<p><strong>About the prices on this page.</strong> Premiums come from the HealthCare.gov Marketplace API for {full_name} (FIPS {c['fips']}), plan year 2027, non-tobacco users, pulled {DATE_H}. Your own price depends on each household member's age, your income estimate and whether anyone uses tobacco. Benefit details are from the plans' official data; confirm them in the Summary of Benefits and Coverage before you enroll.</p>
</div>

<p class="related">{related}</p>

{cta(f"See every {name} County plan with your subsidy applied")}

{author_box()}

{sources([
    '<a href="https://www.healthcare.gov/developers/" target="_blank" rel="noopener">HealthCare.gov Marketplace API</a>, plan year 2027, county FIPS ' + c['fips'] + ', retrieved ' + DATE_H + '.',
    '<a href="https://aspe.hhs.gov/topics/poverty-economic-mobility/poverty-guidelines" target="_blank" rel="noopener">HHS 2026 Poverty Guidelines</a> (used for 2027 Marketplace eligibility).',
    '<a href="https://kff.org/affordable-care-act/9-things-to-watch-for-the-2027-aca-open-enrollment-period/" target="_blank" rel="noopener">KFF, 9 Things to Watch for the 2027 ACA Open Enrollment Period</a> (expiration of enhanced credits, repayment caps, catastrophic plan eligibility).',
    'IRS Rev. Proc. 2026-24 (2027 HSA limits) and IRS Notice 2026-5 (Bronze and catastrophic Marketplace plans treated as HSA-eligible high-deductible plans).',
    'Blue Cross NC provider directories: <a href="' + NET_HMO + '" target="_blank" rel="noopener">Blue Care</a>, <a href="' + NET_PPO + '" target="_blank" rel="noopener">Blue Advantage</a>.',
])}
"""
    page(path, TITLE, DESC, "/counties/", CRUMBS, body, faq=FAQ, reading="12 minute read")


def county_page(c):
    """Counties whose prices were pulled on a later date than the rest carry that date in the byline and structured data."""
    import fbsite
    saved = fbsite.UPDATED, fbsite.UPDATED_H
    if "updated" in c:
        fbsite.UPDATED, fbsite.UPDATED_H = c["updated"], "November 10, 2026"
    try:
        _county_page(c)
    finally:
        fbsite.UPDATED, fbsite.UPDATED_H = saved


if __name__ == "__main__":
    for c in COUNTIES:
        county_page(c)


# ---------- "coming soon" pages for rating areas without guides (none since every county has one) ----------
ZONES = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "zones.json")))
LIVE_ZONES = {str(z) for z in range(1, 17)}  # every NC rating area has guides
SHORT_ISSUER = {"Ambetter of North Carolina": "Ambetter", "AmeriHealth Caritas Next": "AmeriHealth Caritas", "Blue Cross and Blue Shield of NC": "Blue Cross NC",
                "Oscar Health Plan of North Carolina, Inc": "Oscar", "UnitedHealthcare": "UnitedHealthcare"}


def zone_pages():
    for z, v in ZONES.items():
        if z in LIVE_ZONES:
            continue
        counties = v["counties"]
        issuers = [SHORT_ISSUER.get(i, i) for i in v["issuers"]]
        path = f"/counties/zone-{z}/"
        clist = ", ".join(counties)
        live = {g["name"]: g for g in OTHER_GUIDES if g["name"] in counties}
        def county_li(c):
            if c in live:
                return f'<li><a href="/counties/{live[c]["slug"]}/">{c} County</a> (guide available)</li>'
            return f'<li>{c} County</li>'
        ready = "".join(f' The <a href="/counties/{g["slug"]}/">{g["name"]} County guide</a> is ready.' for g in live.values())
        plans = f"{v['plans_min']} plans" if v["plans_min"] == v["plans_max"] else f"{v['plans_min']} to {v['plans_max']} plans, depending on the county"
        title = f"Health Insurance Guides for {clist} (NC Rating Area {z}): Coming Soon"
        desc = f"County-by-county 2027 Marketplace plan guides for {clist} are in preparation. {len(issuers)} carrier{'s' if len(issuers) > 1 else ''} ({', '.join(issuers)}) sell {plans} here. Compare them now with Covanu."
        crumbs = [("/", "Home"), ("/counties/", "County Guides"), (None, f"Rating area {z}")]
        body = f"""
<h1>{clist}: county guides coming soon</h1>
{byline()}
<p class="lede">These {len(counties)} counties make up North Carolina's CMS rating area {z}, which means insurers price their plans the same way across the group. For 2027, {len(issuers)} carrier{'s' if len(issuers) > 1 else ''} sell{'' if len(issuers) > 1 else 's'} Marketplace plans here ({', '.join(issuers)}), {plans}. We are writing the plan-by-plan guides for this area the same way we did for the <a href="/counties/carteret/">Crystal Coast and Albemarle counties</a>: every plan, local prices by age and income, and which plan fits which situation.{ready}</p>
<h2>Counties in this area</h2>
<ul>
{''.join(county_li(c) for c in counties)}
</ul>
<h2>Until the guide is ready</h2>
<p>Our Covanu tool already has every 2027 plan for these counties, with your subsidy applied and your medications priced on each plan's drug list. And the three <a href="/questions/">common questions</a> apply statewide: the subsidy math, the 400% cliff and the Bronze-vs-Silver arithmetic are the same in {counties[0]} County as on the coast; only the premiums and the carriers differ.</p>
{nc_map()}
{cta(f"See every plan in your county now")}
"""
        page(path, title, desc, "/counties/", crumbs, body, reading=None)


if __name__ == "__main__":
    zone_pages()
