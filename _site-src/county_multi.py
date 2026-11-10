"""County guides for the counties in NC rating areas 9, 10, 11, 13 and 15, and Nash County (rating area 14), 2027 plan year.

Data: zones_2027.json, built by covanu-insure/Research/zones-2027 (pull_zones.mjs, then prep_zones.py) from the
HealthCare.gov Marketplace API on November 10, 2026: every plan in each county for the same eight households used on
the other county guides, HealthCare.gov's tax-credit estimates and cost-sharing reductions, each design's benefits
and coverage examples, and the network status of the main hospitals in HealthCare.gov's doctor and hospital lookup.
Every price on these pages is the API's own figure; nothing is calculated from an age curve.

New Hanover County keeps its own guide (county_nh.py); the Blue Cross-only counties with the 20 Blue Care and
Blue Advantage plans use the template in counties.py.
"""
import json, os
import fbsite
from fbsite import *
from counties import money, MULTI_GUIDES, COUNTIES

HERE = os.path.dirname(os.path.abspath(__file__))
Z = json.load(open(os.path.join(HERE, "zones_2027.json"), encoding="utf-8"))
CHECKED = "2026-11-10"
CHECKED_H = "November 10, 2026"
PREVIEW = "https://www.healthcare.gov/see-plans/"
API = "https://www.healthcare.gov/developers/"
METALS = ["bronze", "silver", "gold"]
INS_FULL = {"AMB": "Ambetter of North Carolina", "AMH": "AmeriHealth Caritas Next", "BCBS": "Blue Cross and Blue Shield of North Carolina",
            "UHC": "UnitedHealthcare", "OSC": "Oscar"}
INS_SHORT = {"AMB": "Ambetter", "AMH": "AmeriHealth Caritas Next", "BCBS": "Blue Cross NC", "UHC": "UnitedHealthcare", "OSC": "Oscar"}
INS_ORDER = ["AMB", "AMH", "BCBS", "UHC", "OSC"]
NET_ORDER = ["Ambetter", "AmeriHealth Caritas Next", "Blue Value", "Blue Home", "Blue Care", "Blue Advantage", "UnitedHealthcare", "Oscar"]
NET_INS = {"Ambetter": "AMB", "AmeriHealth Caritas Next": "AMH", "Blue Value": "BCBS", "Blue Home": "BCBS", "Blue Care": "BCBS",
           "Blue Advantage": "BCBS", "UnitedHealthcare": "UHC", "Oscar": "OSC"}
NET_LONG = {"Blue Home": "Blue Home with UNC Health Alliance"}
STD_NAME = {"AMB": "Signature", "AMH": "Signature", "BCBS": "Standard (Gold Standard A for Gold)", "UHC": "Standard", "OSC": "Classic Standard"}

# ---------- county facts (towns for the title and lede; the hospitals residents use) ----------
CFG = {
    "bladen": dict(towns="Elizabethtown, Bladenboro, Clarkton, White Lake and Dublin",
                   hospitals="Cape Fear Valley Bladen County Hospital in Elizabethtown is the local hospital, with Cape Fear Valley Medical Center in Fayetteville and Novant Health New Hanover Regional in Wilmington for specialty care"),
    "cumberland": dict(towns="Fayetteville, Hope Mills, Spring Lake, Stedman, Eastover and Wade",
                       hospitals="Cape Fear Valley Medical Center in Fayetteville is the hospital most residents use, with FirstHealth Moore Regional Hospital in Pinehurst the nearest alternative"),
    "harnett": dict(towns="Lillington, Dunn, Erwin, Angier, Coats and Buies Creek",
                    hospitals="Cape Fear Valley's Betsy Johnson Hospital in Dunn and Central Harnett Hospital in Lillington are the local hospitals; residents also use Cape Fear Valley Medical Center in Fayetteville and, in the north of the county, WakeMed in Raleigh"),
    "hoke": dict(towns="Raeford and the surrounding communities",
                 hospitals="Cape Fear Valley Hoke Hospital in Raeford is the local hospital, with Cape Fear Valley Medical Center in Fayetteville and FirstHealth Moore Regional Hospital in Pinehurst nearby"),
    "richmond": dict(towns="Rockingham, Hamlet, Ellerbe, Hoffman and Dobbins Heights",
                     hospitals="FirstHealth Moore Regional Hospital - Richmond in Rockingham is the local hospital, with FirstHealth Moore Regional Hospital in Pinehurst and Scotland Memorial Hospital in Laurinburg nearby",
                     hosp_note="FirstHealth Moore Regional Hospital - Richmond, the hospital in Rockingham, did not appear as a separate hospital in HealthCare.gov's lookup, so it is not in the table; ask the insurer whether it is in network."),
    "robeson": dict(towns="Lumberton, Pembroke, Red Springs, St. Pauls, Fairmont, Maxton and Rowland",
                    hospitals="UNC Health Southeastern in Lumberton is the local hospital, with Cape Fear Valley Medical Center in Fayetteville and Scotland Memorial Hospital in Laurinburg nearby"),
    "sampson": dict(towns="Clinton, Roseboro, Garland, Newton Grove, Salemburg and Autryville",
                    hospitals="Sampson Regional Medical Center in Clinton is the local hospital; residents also use Cape Fear Valley in Fayetteville, UNC Health Wayne in Goldsboro and Novant Health New Hanover Regional in Wilmington"),
    "scotland": dict(towns="Laurinburg, Wagram, Gibson and East Laurinburg",
                     hospitals="Scotland Memorial Hospital in Laurinburg is the local hospital, with FirstHealth Moore Regional Hospital in Pinehurst and UNC Health Southeastern in Lumberton nearby"),
    "granville": dict(towns="Oxford, Creedmoor, Butner, Stem and Stovall",
                      hospitals="Granville Health System in Oxford is the local hospital; residents also use Maria Parham Health in Henderson and the Duke hospitals in Durham"),
    "vance": dict(towns="Henderson, Kittrell, Middleburg and the Kerr Lake communities",
                  hospitals="Maria Parham Health in Henderson is the local hospital, with Granville Health System in Oxford and Duke University Hospital in Durham nearby"),
    "warren": dict(towns="Warrenton, Norlina, Macon and the Lake Gaston communities",
                   hospitals="the nearest hospitals are Maria Parham Health in Henderson and ECU Health North in Roanoke Rapids, with Duke University Hospital in Durham for specialty care"),
    "alamance": dict(towns="Burlington, Graham, Mebane, Elon, Gibsonville and Haw River",
                     hospitals="Cone Health Alamance Regional Medical Center in Burlington is the local hospital; residents also use Moses Cone Hospital in Greensboro, UNC Medical Center in Chapel Hill and Duke University Hospital"),
    "caswell": dict(towns="Yanceyville, Milton and the surrounding communities",
                    hospitals="the nearest hospitals are Cone Health Alamance Regional in Burlington, Person Memorial in Roxboro and UNC Health Rockingham in Eden"),
    "chatham": dict(towns="Pittsboro, Siler City, Goldston, Bennett and Fearrington Village",
                    hospitals="UNC Health Chatham in Siler City is the local hospital; residents also use UNC Medical Center in Chapel Hill, Duke University Hospital and, in the northeast of the county, WakeMed Cary"),
    "durham": dict(towns="Durham, Research Triangle Park, Bahama and Rougemont",
                   hospitals="Duke University Hospital and Duke Regional Hospital are in Durham, and UNC Medical Center is in Chapel Hill"),
    "lee": dict(towns="Sanford, Broadway and the surrounding communities",
                hospitals="Central Carolina Hospital in Sanford is the local hospital; residents also use FirstHealth Moore Regional Hospital in Pinehurst, UNC Medical Center and Duke University Hospital"),
    "orange": dict(towns="Chapel Hill, Carrboro, Hillsborough and Efland",
                   hospitals="UNC Medical Center in Chapel Hill and UNC's Hillsborough campus are in the county, and the Duke hospitals in Durham are a few miles away"),
    "person": dict(towns="Roxboro, Timberlake, Hurdle Mills and the Hyco Lake communities",
                   hospitals="Person Memorial Hospital in Roxboro is the local hospital, with the Duke hospitals in Durham for specialty care"),
    "franklin": dict(towns="Louisburg, Youngsville, Franklinton and Bunn",
                     hospitals="residents mostly use hospitals in Raleigh (WakeMed, UNC Health Rex and Duke Raleigh) and Maria Parham Health in Henderson"),
    "johnston": dict(towns="Smithfield, Clayton, Selma, Benson, Four Oaks, Kenly and Princeton",
                     hospitals="UNC Health Johnston in Smithfield and Clayton is the local hospital, with WakeMed, UNC Health Rex and Duke Raleigh in Raleigh"),
    "wake": dict(towns="Raleigh, Cary, Apex, Wake Forest, Holly Springs, Fuquay-Varina, Garner, Morrisville and Knightdale",
                 hospitals="WakeMed, UNC Health Rex and Duke Raleigh Hospital are the main hospital systems, with Duke University Hospital and UNC Medical Center about 25 miles away"),
    "nash": dict(towns="Rocky Mount, Nashville, Spring Hope, Middlesex and Bailey",
                 hospitals="UNC Health Nash in Rocky Mount is the local hospital; residents also use ECU Health Medical Center in Greenville, Wilson Medical Center and WakeMed in Raleigh"),
    "brunswick": dict(towns="Leland, Southport, Oak Island, Shallotte, Ocean Isle Beach, Sunset Beach, Holden Beach and Calabash",
                      hospitals="Novant Health Brunswick Medical Center in Bolivia and J. Arthur Dosher Memorial Hospital in Southport are the local hospitals, with Novant Health New Hanover Regional in Wilmington for most specialty care"),
    "columbus": dict(towns="Whiteville, Tabor City, Chadbourn, Lake Waccamaw and Fair Bluff",
                     hospitals="Columbus Regional Healthcare System in Whiteville is the local hospital, with Novant Health New Hanover Regional in Wilmington for specialty care"),
    "duplin": dict(towns="Kenansville, Wallace, Warsaw, Beulaville, Rose Hill and Faison",
                   hospitals="ECU Health Duplin Hospital in Kenansville is the local hospital; residents also use UNC Health Wayne in Goldsboro, Novant Health New Hanover Regional in Wilmington and ECU Health Medical Center in Greenville"),
    "onslow": dict(towns="Jacksonville, Swansboro, Richlands, Holly Ridge, Sneads Ferry and North Topsail Beach",
                   hospitals="Onslow Memorial Hospital in Jacksonville, managed by UNC Health, is the local hospital, with CarolinaEast in New Bern and Novant Health New Hanover Regional in Wilmington nearby"),
    "pender": dict(towns="Burgaw, Hampstead, Surf City, Topsail Beach, Rocky Point and Atkinson",
                   hospitals="Novant Health Pender Medical Center in Burgaw is the local hospital, and many residents use Novant Health New Hanover Regional in Wilmington or its Scotts Hill Medical Center near Hampstead"),
}

# ---------- plan designs: (best for, description). Benefits are the same in every county and network. ----------
TEXT = {
    # Ambetter
    "AMB|Signature Expanded Bronze": ("the lowest Bronze premiums with copays for office visits; HSA savers",
        "The federally standardized Bronze. Primary care is $50, specialists $100 and urgent care $75 from day one; generics are $25; after the deductible, brand drugs are flat copays of $50 (preferred), $100 (non-preferred) and $500 (specialty). Imaging, the emergency room and hospital stays are 50% coinsurance after the deductible."),
    "AMB|Everyday Bronze": ("healthy adults who take only inexpensive generics",
        "$3 generics and lower office copays than the standardized Bronze ($40 primary care, $90 specialists, $50 urgent care), in exchange for a $9,350 deductible and coinsurance instead of copays for brand drugs (45%) and specialty drugs (50%) after it. Its out-of-pocket maximum is $1,000 lower than the standardized Bronze's."),
    "AMB|Elite Bronze": ("people who want office visits and generics covered without a deductible and rarely use the emergency room",
        "No medical deductible: office visits are copays ($55 primary care, $120 specialists, $60 urgent care) and imaging and hospital stays are 50% coinsurance from the first dollar. The catches are a $4,000 emergency room copay, $195 preferred brand drugs, and a separate $4,850 deductible before non-preferred and specialty drugs are covered (then 45% and 50%). Generics are $3."),
    "AMB|Streamlined Silver": ("subsidized households who mostly see doctors and take generics",
        "Strong on everyday care: $20 primary care, $60 specialists, $55 urgent care and $3 generics from day one. Preferred brand drugs are $30 after the deductible; non-preferred and specialty drugs, imaging and hospital care are 30% to 45% coinsurance after it."),
    "AMB|Clear Silver with $0 Insulin Options": ("subsidized households expecting a big year (a surgery, a birth) who want the lowest possible ceiling",
        "It works like a high-deductible plan: office visits are copays from day one ($50 primary care, $100 specialists, $75 urgent care), but prescriptions, imaging and hospital care are yours to pay until the $7,900 deductible, and after that the plan pays 100%. As the name says, some insulins are $0."),
    "AMB|Signature Silver": ("anyone taking a preferred brand-name drug, and subsidized households who want flat copays",
        "The federally standardized Silver: $40 primary care, $80 specialists, $60 urgent care, $20 generics and $40 preferred brand drugs as copays from day one, with no deductible. Non-preferred brands ($80) and specialty drugs ($350) come after the deductible, and hospital care is 40% coinsurance after it."),
    "AMB|Enhanced CHF Heart Care Silver $0 Rx Options": ("people managing heart failure",
        "Designed for people with congestive heart failure, with $0 options for some related prescriptions (check the plan's drug list for yours). Otherwise a mid-deductible Silver with low office copays ($25 primary care, $55 specialists, $40 urgent care), $3 generics and $75 preferred brands; imaging and hospital care are 50% after the deductible."),
    "AMB|Enhanced Asthma/COPD Care Silver $0 Rx Options": ("people managing asthma or COPD",
        "Designed for people with asthma or COPD, with $0 options for some related prescriptions (check the drug list for your inhalers). $40 primary care, $60 specialists, $50 urgent care, $3 generics and $75 preferred brands; imaging and hospital care are 50% after the deductible. Its $9,400 out-of-pocket maximum is lower than any other Ambetter Silver except Clear Silver."),
    "AMB|Signature Gold": ("specialty drugs, regular specialist care, or a planned surgery or pregnancy",
        "The federally standardized Gold, with flat copays and no deductible for office visits ($30 primary care, $60 specialists, $45 urgent care) and for every drug tier ($15 generics, $30 preferred brand, $60 non-preferred, $250 specialty). Hospital care is 25% coinsurance after the deductible."),
    "AMB|Complete Gold": ("frequent doctor visits with generic or preferred-brand prescriptions",
        "Richer everyday benefits than Signature Gold: $15 primary care, $35 specialists and urgent care, $3 generics and $30 preferred brands, with 20% coinsurance for imaging and hospital care after a $1,450 deductible. The trade-offs are a higher out-of-pocket maximum ($9,500 against $8,600) and coinsurance (25% and 30%) rather than copays for non-preferred and specialty drugs."),
    # AmeriHealth Caritas Next
    "AMH|Bronze Signature": ("Bronze buyers who want copays for office visits",
        "The federally standardized Bronze: $50 primary care, $100 specialists and $75 urgent care from day one, $25 generics, and after the deductible flat copays of $50 (preferred brand), $100 (non-preferred) and $500 (specialty). Imaging, the emergency room and hospital stays are 50% coinsurance after the deductible."),
    "AMH|Bronze Enhanced": ("Bronze buyers who want a lower deductible and take generics",
        "A $4,500 deductible, low for a Bronze plan, with $50 primary care, $110 specialists and $15 generics from day one. Preferred brands are $60 after the deductible; non-preferred and specialty drugs are 35% and 40% coinsurance after it, and hospital care is 50%. Urgent care is $150 a visit, so the free virtual urgent care matters."),
    "AMH|Bronze Essential": ("people who want protection against a catastrophe at the lowest AmeriHealth price",
        "A $12,000 deductible equal to the out-of-pocket maximum: apart from preventive care, $25 generics and the free primary care visits the plan's name promises, you pay the full negotiated price of care and drugs until $12,000, and then nothing."),
    "AMH|Silver Signature 70": ("anyone taking a preferred brand-name drug who wants AmeriHealth's network",
        "The federally standardized Silver: $40 primary care, $80 specialists, $60 urgent care, $20 generics and $40 preferred brands from day one; non-preferred ($80) and specialty drugs ($350) after the deductible, and 40% for hospital care after it."),
    "AMH|Silver Essential 70": ("generic and preferred-brand users who see a primary care doctor often",
        "A $5,000 deductible with $30 primary care (and free visits per the plan's name), $5 generics and $60 preferred brands from day one, but $100 specialists and $150 urgent care. Hospital care is 35% and non-preferred and specialty drugs are 35% and 40% after the deductible, up to a $12,000 out-of-pocket maximum."),
    "AMH|Gold Signature": ("specialty drugs or a planned surgery on AmeriHealth's network",
        "The federally standardized Gold: $30 primary care, $60 specialists, $45 urgent care and every drug tier as copays with no deductible ($15, $30, $60 and $250 for specialty drugs); hospital care is 25% after the deductible, up to $8,600."),
    "AMH|Gold Enhanced": ("frequent care with mostly generic or preferred-brand drugs",
        "A $1,000 deductible, $35 primary care, $80 specialists, $5 generics and $60 preferred brands. Hospital care, imaging and the emergency room are 25% after the deductible; non-preferred and specialty drugs are 35% and 40% after it. Urgent care is $120."),
    "AMH|Gold Copay Focus": ("people who want every price known in advance",
        "No deductible: primary care is free, specialists are $35, urgent care $60, imaging $300, the emergency room $1,000 and a hospital stay $1,500 a day, up to a $9,000 out-of-pocket maximum. Generics are $5 and preferred brands $60; non-preferred and specialty drugs are 35% and 40% coinsurance."),
    # Blue Cross NC
    "BCBS|Bronze Basic": ("a Blue Cross network at the lowest Blue Cross price, mainly as protection against a large bill",
        "Three primary care visits a year are free, then $95; specialists are $175; preferred generics are $25. Everything else, including brand drugs, imaging, the emergency room and hospital stays, is 50% coinsurance after the $7,000 deductible."),
    "BCBS|Bronze Standard": ("Bronze buyers who want copays rather than coinsurance on a Blue Cross network",
        "The federally standardized Bronze: $50 primary care and $100 specialist copays from day one, $25 generics, and after the deductible flat copays of $50 (preferred brand), $100 (non-preferred) and $500 (specialty). Children's dental is included."),
    "BCBS|Bronze Complete": ("Bronze buyers with one or two brand-name prescriptions",
        "The lowest medical deductible among Blue Cross's Bronze plans. Primary care is $60, specialists $120, generics $20. Brand drugs become $75 (preferred) or $150 (non-preferred) copays once you have met the separate $1,000 drug deductible. Hospital care is 50% after the $4,000 medical deductible."),
    "BCBS|Bronze HSA Eligible Plus": ("disciplined HSA savers who want the lowest worst-case cost on a Bronze plan",
        "A true high-deductible plan: you pay everything except preventive care until you reach $8,700, and then the plan pays 100%. There are no copays to track, and the ceiling is $3,300 lower than the $12,000 maximum on most Bronze plans."),
    "BCBS|Silver Preferred": ("subsidized households who want a Blue Cross network and take mostly generics",
        "Three free primary care visits then $35, specialists $75, generics $15. Every brand and specialty drug is 50% coinsurance after the deductible, so it suits generic users; with cost-sharing reductions its deductible is among the lowest of any plan."),
    "BCBS|Silver Standard": ("anyone on a preferred brand-name drug who wants a Blue Cross network",
        "The federally standardized Silver: $40 primary care, $80 specialist, $20 generic and $40 preferred brand copays from day one; non-preferred brands ($80) and specialty drugs ($350) after the deductible, and 40% for hospital care after it."),
    "BCBS|Silver Choice A": ("Blue Cross members who want a lower medical deductible than Silver Standard and take at most one or two brand drugs",
        "Three free primary care visits then $45, specialists $95, generics $15, and brand drugs at $35 (preferred) or $70 (non-preferred) copays after a small $200 drug deductible. Specialty drugs and hospital care are 50% after the deductibles."),
    "BCBS|Gold Premier A": ("frequent doctor visits and brand-name (not specialty) prescriptions on a Blue Cross network",
        "Three free primary care visits then $15, specialists $45, generics $10, brand drugs $35 or $60 after the $400 drug deductible. Hospital and emergency care are 30% after the $1,800 deductible, and specialty drugs are 50% after the deductible: strong for doctor visits and ordinary prescriptions, weak for specialty medications."),
    "BCBS|Gold Standard A": ("anyone on a specialty drug who wants a Blue Cross network",
        "The federally standardized Gold: primary care $30, specialists $60, generics $15, preferred brand $30, non-preferred $60 and specialty $250, all copays with no deductible; hospital care is 25% after the deductible."),
    "BCBS|Gold All Copay A": ("people who want to know the price of every visit in advance, and those expecting a hospital stay",
        "No deductible at all. Every service is a fixed copay: $30 primary care, $60 specialist, $10 generic, $60 preferred brand, $120 non-preferred, $220 specialty, $1,500 emergency room and $2,500 per hospital stay. You give up the lower out-of-pocket maximum of Gold Standard A in exchange for never having to meet a deductible."),
    # UnitedHealthcare
    "UHC|UHC Bronze Essential": ("HSA savers who want UnitedHealthcare's network and rarely use care",
        "A pure high-deductible plan: apart from preventive care (and the $0 virtual urgent care and $0 insulin in the plan's name), you pay the full negotiated price of care and drugs until you reach $11,750, and then nothing."),
    "UHC|UHC Bronze Standard": ("people with diabetes who use insulin; families who want children's dental included",
        "The standardized Bronze benefits ($50 primary care, $100 specialists, $25 generics, and $50/$100/$500 brand and specialty copays after the deductible) plus UnitedHealthcare's $0 insulin and children's dental."),
    "UHC|UHC Bronze Copay Focus $0 Indiv Med Ded": ("people who want to know what each visit costs in advance and take only generics",
        "No medical deductible: every medical service is a copay from day one, including $55 primary care, $115 specialists, $80 urgent care, $300 imaging, $2,000 for an emergency room visit and $3,000 a day in the hospital, all capped by the $12,000 out-of-pocket maximum. Generics are $20; brand and specialty drugs are 40% to 50% coinsurance after the separate $4,000 drug deductible."),
    "UHC|UHC Silver Standard": ("insulin users and families who want UnitedHealthcare's network",
        "The standardized Silver benefits ($40 primary care, $80 specialists, $20 generics, $40 preferred brands with no deductible) with UnitedHealthcare's $0 insulin and children's dental."),
    "UHC|UHC Silver Value": ("generic-drug users who want a lower deductible on UnitedHealthcare's network",
        "A lower deductible than the standardized Silver, with $5 generics, $40 primary care and $60 urgent care, but $110 specialist visits and preferred brand drugs at $100 after the deductible. Imaging and hospital care are 40% after the deductible; non-preferred and specialty drugs are 40% and 50% coinsurance after it."),
    "UHC|UHC Silver Copay Focus $0 Indiv Med Ded": ("people who want no medical deductible on a Silver plan",
        "Copays for every medical service from day one: $40 primary care, $100 specialists, $60 urgent care, $300 imaging, $1,500 for an emergency room visit and $2,500 a day in the hospital. Generics are $10; preferred brands are $85 after the $2,500 drug deductible, and non-preferred and specialty drugs are 40% and 50% coinsurance."),
    "UHC|UHC Gold Standard": ("insulin users and families who want Gold coverage on UnitedHealthcare's network",
        "The standardized Gold benefits (flat copays with no deductible for office visits and every drug tier, including $250 specialty drugs) with $0 insulin and children's dental."),
    "UHC|UHC Gold Copay Focus $0 Ded": ("people expecting frequent care who want every price known in advance",
        "No deductible at all: $20 primary care, $60 specialists, $30 urgent care, $300 imaging, $750 for the emergency room, $2,000 a day in the hospital, $5 generics and $50 preferred brands. Non-preferred and specialty drugs are 40% and 50% coinsurance."),
    "UHC|UHC Gold Advantage": ("frequent doctor visits and generic or preferred-brand drugs on UnitedHealthcare's network",
        "Low copays ($15 primary care, $50 specialists, $20 urgent care, $1 generics, $30 preferred brands) and 20% coinsurance for the emergency room and hospital after an $850 deductible. Non-preferred and specialty drugs are 30% and 40% coinsurance after the deductible."),
    # Oscar
    "OSC|Bronze Classic Standard": ("people whose doctors are in Oscar's network",
        "The standardized Bronze benefits: $50 primary care, $100 specialists, $25 generics, and $50/$100/$500 brand and specialty copays after the deductible."),
    "OSC|Bronze Classic 4700": ("Bronze buyers who want a lower deductible and take generics",
        "A lower deductible than most Bronze plans, $4 generics and $40 urgent care, but $70 primary care and $125 specialist visits, and 50% coinsurance for brand drugs, imaging and hospital care."),
    "OSC|Bronze Simple Diabetes": ("people with diabetes whose doctors are in Oscar's network",
        "Designed for people with diabetes: $50 primary care (the first three visits free), $150 specialists, $40 urgent care and $4 generics from day one, preferred brands at $75 after the deductible, insulin capped at $100 for a 30-day supply, and 50% coinsurance for imaging, hospital care and other brand drugs."),
    "OSC|Bronze Elite + PCP Saver Plus": ("generic-only Bronze buyers who want no medical deductible",
        "Copays for medical care from day one: $50 primary care, $125 specialists, $40 urgent care, $750 imaging, $2,500 for the emergency room and $3,000 a day in the hospital. Generics are $4; preferred brands are $125 after the $7,500 drug deductible, and other brand and specialty drugs are 50% after it."),
    "OSC|Silver Classic Standard": ("people whose doctors are in Oscar's network and who take a preferred brand drug",
        "The standardized Silver benefits: $40 primary care, $80 specialists, $20 generics and $40 preferred brands with no deductible."),
    "OSC|Silver Simple PCP Saver": ("frequent primary care visits on Oscar's network",
        "$20 primary care, $80 specialists, $35 urgent care and $4 generics from day one; preferred brand drugs are $145, and imaging and hospital care are 40% after the deductible. Other brand and specialty drugs are 50% after the deductible."),
    "OSC|Silver Core Plan": ("subsidized households under about $31,900 (one person) who use Oscar's network",
        "A $9,000 deductible at full price, with $50 primary care, $90 specialists, $4 generics and $150 preferred brands; imaging and hospital care are 50% after the deductible. Cost-sharing reductions change it more than most Silver plans."),
    "OSC|Silver Simple Diabetes": ("people with diabetes whose doctors are in Oscar's network",
        "Designed for people with diabetes: primary care visits and the lowest-tier generics are free, specialists are $40 and urgent care $35, preferred brands are $75 after the deductible, insulin is capped at $100 for a 30-day supply, and imaging and hospital care are 45% after it."),
    "OSC|Gold Classic Standard": ("people whose doctors are in Oscar's network and who need Gold coverage",
        "The standardized Gold benefits: flat copays with no deductible for office visits and every drug tier, including $250 specialty drugs."),
}
assert set(TEXT) == set(Z["designs"]), set(TEXT) ^ set(Z["designs"])


def m(x):
    return money(x)


def dm(a, b):
    """Difference of two prices as printed (rounded first, so the page's arithmetic adds up)."""
    return money(round(a) - round(b))


def join(items, conj="and"):
    items = list(items)
    if len(items) <= 1:
        return "".join(items)
    if len(items) == 2:
        return f"{items[0]} {conj} {items[1]}"
    return ", ".join(items[:-1]) + f" {conj} " + items[-1]


PLURAL_H = {"WAKEMED_RAL", "CFV_BJ"}  # display names that cover two hospitals
NUMW = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten"}


def ded_text(dd):
    if "combined" in dd:
        return f"{m(dd['combined'])} deductible"
    med, drug = dd.get("medical"), dd.get("drug")
    if med == 0 and drug:
        return f"$0 medical deductible &middot; separate {m(drug)} drug deductible"
    if drug:
        return f"{m(med)} medical deductible plus a separate {m(drug)} drug deductible"
    return f"{m(med)} deductible"


def ded_amount(dd):
    return dd["combined"] if "combined" in dd else dd.get("medical")


class County:
    def __init__(self, g):
        self.g = g
        self.slug, self.name, self.fips = g["slug"], g["name"], g["fips"]
        self.full = f"{self.name} County"
        self.path = f"/counties/{self.slug}/"
        self.cfg = CFG[self.slug]
        d = Z["counties"][self.fips]
        self.d = d
        self.P = d["plans"]
        for pid, p in self.P.items():
            p["id"] = pid
            p["key"] = f"{p['ins']}|{p['design']}"
            p["p45"] = p["p"]["s45_100k"]
        self.N = len(self.P)
        self.nets = [n for n in NET_ORDER if any(p["net"] == n for p in self.P.values())]
        self.ins = [i for i in INS_ORDER if any(p["ins"] == i for p in self.P.values())]
        self.designs = sorted({p["key"] for p in self.P.values()})
        self.D = len(self.designs)
        silv = sorted((p for p in self.P.values() if p["metal"] == "silver"), key=lambda p: p["p45"])
        self.bench = silv[1]["id"]
        self.hosp = d.get("hosp", {})
        self.listed = d.get("hosp_listed", {})
        # every Bronze plan is HSA-eligible and nothing else is (2027 rule), and no plan needs referrals: checked in prep
        assert all(p["hsa"] == (p["metal"] == "bronze") for p in self.P.values()), self.name

    # ---- lookups ----
    def by_net(self, n):
        return [p for p in self.P.values() if p["net"] == n]

    def count_ins(self, i):
        return sum(1 for p in self.P.values() if p["ins"] == i)

    def std(self, net, metal):
        hits = [p for p in self.by_net(net) if p["std"] and p["metal"] == metal and not p["adent"]]
        assert len(hits) <= 1, (self.name, net, metal, [h["name"] for h in hits])
        return hits[0]["id"] if hits else None

    def cheapest(self, metal=None, sc="s45_100k", net=None, nets=None, key="p", std=False, cdent=None):
        c = [p for p in self.P.values() if (metal is None or p["metal"] == metal) and (net is None or p["net"] == net)
             and (nets is None or p["net"] in nets) and (not std or (p["std"] and not p["adent"])) and (cdent is None or p["cdent"] == cdent)]
        if not c:
            return None
        return min(c, key=lambda p: (round(p[key][sc], 2), p["p45"], p["adent"], p["name"]))["id"]

    def full45(self, pid):
        return m(self.P[pid]["p45"])

    def net_(self, pid, sc):
        return m(self.P[pid]["n"][sc])

    def label(self, pid, short=False):
        p = self.P[pid]
        extra = " with adult dental and vision" if p["adent"] else ""
        if p["ins"] == "BCBS":
            return f"{p['net']} {p['design']}{extra}"
        if p["ins"] == "UHC":
            return f"{p['design']}{extra}" if short else f"UnitedHealthcare {p['design'].replace('UHC ', '')}{extra}"
        if p["ins"] == "AMH":
            return f"AmeriHealth {p['design']}{extra}" if short else f"AmeriHealth Caritas Next {p['design']}{extra}"
        return f"{INS_SHORT[p['ins']]} {p['design']}{extra}"

    def csr(self, pid, lvl):
        dd, moop = self.P[pid][lvl]
        return m(ded_amount(dd)), m(moop)

    def hstat(self, k, n):
        ids = [p["id"] for p in self.by_net(n)]
        cov = set(self.hosp.get(k, []))
        hit = sum(1 for i in ids if i in cov)
        if hit == len(ids):
            return "in"
        if hit == 0:
            return "out" if self.listed.get(n) else "unlisted"
        return "some"

    def hname(self, k):
        return Z["hospitals"][k]["name"]

    def nets_with(self, k):
        return [n for n in self.nets if self.hstat(k, n) == "in"]

    def net_label(self, n):
        return NET_LONG.get(n, n)

    def nlist(self, nets):
        """Network names for prose; 'every network' when it is all of them."""
        if set(nets) == set(self.nets) and len(self.nets) > 1:
            return "every network"
        return join(nets) if nets else "no network"

    def ptype(self, n):
        return self.by_net(n)[0]["type"]

    def quality(self, n):
        q = {p["quality"] for p in self.by_net(n)}
        assert len(q) == 1, (self.name, n, q)
        q = q.pop()
        return f"{q} stars" if q else "Not yet rated"

    def cdent(self, n):
        v = {p["cdent"] for p in self.by_net(n)}
        assert len(v) == 1, (self.name, n)
        return v.pop()

    def metal_range(self, metal):
        v = [p["p45"] for p in self.P.values() if p["metal"] == metal]
        return f"{m(min(v))} to {m(max(v))}"

    def count_metal(self, metal):
        return sum(1 for p in self.P.values() if p["metal"] == metal)


def coverage_example(pid, which):
    s = Z["designs"][f"{C.P[pid]['ins']}|{C.P[pid]['design']}"]["sbc"][which]
    return m(s["deductible"] + s["copay"] + s["coinsurance"] + s["limit"])


C = None  # the county being built (used by coverage_example)


def build(g):
    global C
    c = County(g)
    C = c
    P, NAME, FULL = c.P, c.name, c.full
    multi_ins = len(c.ins) > 1
    multi_net = len(c.nets) > 1
    bench = c.bench
    bp = P[bench]
    zone = c.d["zone"]
    ins_names = [INS_FULL[i] for i in c.ins]

    # standardized plan prices by network
    STD = {(n, mt): c.std(n, mt) for n in c.nets for mt in METALS}
    std_nets = [n for n in c.nets if all(STD[(n, mt)] for mt in METALS)]
    std_sorted = sorted(std_nets, key=lambda n: P[STD[(n, "silver")]]["p45"])
    s_lo, s_hi = (std_sorted[0], std_sorted[-1]) if std_sorted else (None, None)

    cb = {mt: c.cheapest(mt) for mt in METALS}                      # cheapest at each metal, age 45
    bronze_free_30k = P[cb["bronze"]]["n"]["s45_30k"] == 0
    has_ba = "Blue Advantage" in c.nets
    has_uhc = "UHC" in c.ins
    has_amb = "AMB" in c.ins
    has_osc = "OSC" in c.ins
    no_cdent = [n for n in c.nets if not c.cdent(n)]
    with_cdent = [n for n in c.nets if c.cdent(n)]
    hosp_keys = [k for k in c.hosp]
    unlisted = [n for n in c.nets if hosp_keys and not c.listed.get(n)]

    # ---------- plan counts by insurer ----------
    def ins_count_phrase(i):
        n = c.count_ins(i)
        if i == "BCBS":
            bn = [x for x in c.nets if NET_INS[x] == "BCBS"]
            nd = len({p["design"] for p in P.values() if p["ins"] == "BCBS"})
            return f"Blue Cross NC {n}" + (f" ({nd} designs in {NUMW[len(bn)]} networks)" if len(bn) > 1 else "")
        return f"{INS_SHORT[i]} {n}"

    # ---------- hospital summary sentences ----------
    def hosp_sentence(k):
        nm = c.hname(k)
        ins = c.nets_with(k)
        out = [n for n in c.nets if c.hstat(k, n) == "out"]
        unl = [n for n in c.nets if c.hstat(k, n) == "unlisted"]
        some = [n for n in c.nets if c.hstat(k, n) == "some"]
        if not multi_net:
            st = c.hstat(k, c.nets[0])
            return nm + {"in": " was in network", "out": " was not in network", "unlisted": " was not listed", "some": " was in network on some plans"}[st]
        if not out and not unl and not some:
            return f"{nm} was in network on every plan"
        if ins:
            s = f"{nm} was in network on {join(ins)} plans"
            if out:
                s += f" and not on {join(out)} plans"
        elif out:
            s = f"{nm} was not in network on {join(out)} plans"
        else:
            s = f"{nm} was not listed for any network"
        if some:
            s += f" (on some {join(some)} plans)"
        if unl and (ins or out):
            s += f"; {join(unl)}'s hospital network is not listed in the lookup"
        return s

    key_hosp = hosp_keys

    def hosp_groups():
        groups = {}
        for k in hosp_keys:
            groups.setdefault(tuple(c.hstat(k, n) for n in c.nets), []).append(k)
        return list(groups.items())

    def group_sentence(sig, ks):
        H = join([c.hname(k) for k in ks])
        was = "was" if len(ks) == 1 and ks[0] not in PLURAL_H else "were"
        ins_ = [n for n, st in zip(c.nets, sig) if st == "in"]
        out_ = [n for n, st in zip(c.nets, sig) if st == "out"]
        some_ = [n for n, st in zip(c.nets, sig) if st == "some"]
        if not multi_net:
            return f"{H} {was} " + {"in": "in network", "out": "not in network", "unlisted": "not listed", "some": "in network on some plans"}[sig[0]]
        if ins_ and not out_ and not some_ and len(ins_) == len(c.nets):
            return f"{H} {was} in network on every plan"
        if ins_ and not out_ and not some_:
            unl_ = [n for n, st in zip(c.nets, sig) if st == "unlisted"]
            return f"{H} {was} in network on every plan except " + join([f"{n}'s" for n in unl_])
        if ins_ and out_ and len(out_) < len(ins_) and not [n for n, st in zip(c.nets, sig) if st == "unlisted"]:
            t = f"{H} {was} in network on every plan except " + join([f"{n}'s" for n in out_])
        elif ins_:
            t = f"{H} {was} in network on {join(ins_)} plans" + (f" and not on {join(out_, 'or')} plans" if out_ else "")
        elif out_:
            t = f"{H} {was} not in network on {join(out_, 'or')} plans" if len(out_) < len(c.nets) else f"{H} {was} not in network on any plan"
        else:
            t = f"{H} {was} not listed as in network on any plan"
        if some_:
            t += f" (in network on some {join(some_)} plans)"
        return t

    unl_note = (f" {join(unlisted)}'s hospital network is not listed in the lookup; ask the insurer which hospitals it uses." if unlisted else "")
    hosp_sentences = [group_sentence(sig, ks) for sig, ks in hosp_groups()]

    # ---------- title and description ----------
    TITLE = f"{FULL}, NC Health Insurance for 2027: All {c.N} Marketplace Plans Explained"
    if multi_ins:
        DESC = (f"Every 2027 Marketplace plan in {FULL}, NC ({g['short']}): {c.N} plans from {join([INS_SHORT[i] for i in c.ins])}, "
                f"prices by age and income, and which networks include {c.hname(hosp_keys[0])}.")
    else:
        DESC = (f"Every 2027 Marketplace plan in {FULL}, NC ({g['short']}): {c.N} Blue Cross plans in {NUMW[len(c.nets)]} network{'s' if multi_net else ''}, "
                f"prices by age and income, and which hospitals are in network.")
    CRUMBS = [("/", "Home"), ("/counties/", "County Guides"), (None, FULL)]

    ptypes = sorted({c.ptype(n) for n in c.nets})
    hmo_txt = ", including the HMOs" if "HMO" in ptypes else ""
    type_txt = ("an " + join(ptypes, "or")) if ptypes else "a plan"
    # ---------- FAQ ----------
    FAQ = []
    if multi_ins:
        FAQ.append((f"Which insurers sell Marketplace plans in {FULL} for 2027?",
                    f"{NUMW[len(c.ins)].capitalize()}: " + join([f"{INS_FULL[i]} ({c.count_ins(i)} plans)" for i in c.ins]) + f", for {c.N} plans in all. "
                    + ("Blue Cross sells each of its designs in " + join([x for x in c.nets if NET_INS[x] == 'BCBS']) + ", and " if len([x for x in c.nets if NET_INS[x] == 'BCBS']) > 1 else "")
                    + ((lambda who: (who if len([x for x in c.nets if NET_INS[x] == 'BCBS']) > 1 else who[0].upper() + who[1:]) + (" sells" if " and " not in who else " sell") + f" some designs both with and without adult dental and vision, so the {c.N} plans come down to {c.D} distinct designs.")(join([INS_SHORT[i] for i in c.ins if any(p["adent"] for p in P.values() if p["ins"] == i)]))
                       if any(p["adent"] for p in P.values()) else f"The {c.N} plans come down to {c.D} distinct designs.")))
    else:
        FAQ.append((f"Why is Blue Cross the only insurer in {FULL}?",
                    f"For 2027, Blue Cross and Blue Shield of North Carolina is the only carrier offering individual Marketplace plans in {FULL}. The other insurers that sell Marketplace plans elsewhere in North Carolina (Ambetter, AmeriHealth Caritas Next, Oscar and UnitedHealthcare) do not include {NAME} in their 2027 service areas. "
                    + (f"Blue Cross sells its 10 designs in {join(c.nets)}, for {c.N} plans." if multi_net else f"Blue Cross sells its 10 designs in one network here, {c.net_label(c.nets[0])}.")))
    if hosp_keys:
        k0 = hosp_keys[0]
        FAQ.append((f"Is {c.hname(k0)} in network?",
                    f"When we checked HealthCare.gov's doctor and hospital lookup on {CHECKED_H}, " + "; ".join(hosp_sentences) + "." + unl_note
                    + " Networks change, and a hospital being in network does not mean every doctor who works there is, so check the specific doctors and facilities you use before you enroll."))
    if multi_net:
        FAQ.append(("Why do plans with the same benefits cost so differently after the subsidy?",
                    f"Because the tax credit is a fixed dollar amount based on the second-cheapest Silver plan in your county, which in {NAME} is {c.label(bench)} ({c.full45(bench)} a month at age 45). The credit makes that plan cost the same share of your income wherever you live; any plan that costs more at full price costs exactly that much more after the credit. "
                    + (f"That is why the standardized Silver, identical in benefits {'from every insurer' if multi_ins else 'in every network'}, costs a 45-year-old earning $30,000 {c.net_(STD[(s_lo, 'silver')], 's45_30k')} a month from {s_lo} and {c.net_(STD[(s_hi, 'silver')], 's45_30k')} from {s_hi}." if s_lo and s_lo != s_hi else "")))
    if len(std_nets) > 1:
        FAQ.append(("What are the standardized \"Easy Pricing\" plans?",
                    f"Plans whose deductibles, copays and coinsurance are set by the federal government, so a standardized plan at a given metal level has the same benefits whichever insurer sells it. HealthCare.gov labels them Easy Pricing. In {NAME} they are "
                    + join([f"{INS_SHORT[i]}'s {STD_NAME[i]} plans" for i in c.ins]) + f". Because the benefits match, the comparison comes down to price, network and extras such as children's dental: at age 45 the standardized Silver ranges from {c.full45(STD[(s_lo, 'silver')])} ({s_lo}) to {c.full45(STD[(s_hi, 'silver')])} ({s_hi})."))
    FAQ.append(("Do I need a referral to see a specialist?",
                f"No. None of the plans sold here requires a referral from a primary care doctor to see a specialist{hmo_txt}."))
    if has_ba:
        ba_txt = ""
        if "Blue Care" in c.nets:
            pairs = [(P[a], P[b]) for a in P for b in P if P[a]["net"] == "Blue Advantage" and P[b]["net"] == "Blue Care" and P[a]["design"] == P[b]["design"]]
            add45 = [round(a["p45"]) - round(b["p45"]) for a, b in pairs]
            add60 = [round(a["p"]["s60_100k"]) - round(b["p"]["s60_100k"]) for a, b in pairs]
            pct = 100 * (sum(a["p45"] for a, b in pairs) / sum(b["p45"] for a, b in pairs) - 1)
            ba_txt = f"It costs about {pct:.0f}% more than the same Blue Care design: {m(min(add45))} to {m(max(add45))} a month at age 45, {m(min(add60))} to {m(max(add60))} at 60. "
        FAQ.append(("Which plans work outside North Carolina?",
                    "Only Blue Advantage, Blue Cross's PPO, gives you in-network access to doctors nationwide, through the BlueCard network. " + ba_txt
                    + "The other plans are built around North Carolina providers. Every plan covers emergency care anywhere."))
    else:
        FAQ.append(("Which plans work outside North Carolina?",
                    f"None of the plans sold in {NAME} has a nationwide network: " + ("Blue Cross's Blue Advantage PPO, which uses the national BlueCard network, is not sold here, and " if "BCBS" in c.ins else "")
                    + f"every plan is {type_txt} built around North Carolina providers. Every plan covers emergency care anywhere, but routine care out of state is not covered. A college student out of state may be better served by the school's student health plan."))
    FAQ.append((f"Is there a catastrophic plan in {FULL}?",
                f"No. For 2027 no catastrophic plan is offered in {FULL}, even for people under 30. The Bronze plans are the lowest-premium options, starting at {m(P[c.cheapest('bronze', 'a27_35k')]['p']['a27_35k'])} a month at age 27 before any subsidy."))
    adent_ins = [i for i in c.ins if any(p["adent"] for p in P.values() if p["ins"] == i)]
    def adent_delta(i):
        out = []
        for p in P.values():
            if p["ins"] == i and p["adent"]:
                base = [q for q in P.values() if q["ins"] == i and q["design"] == p["design"] and not q["adent"]]
                if base:
                    out.append(round(p["p45"]) - round(base[0]["p45"]))
        return out
    dent = (("Children's dental is included in every " + join(with_cdent) + " plan" + (", but not in " + join(no_cdent) + " plans; families choosing those should add a stand-alone dental plan for the children." if no_cdent else ".")) if with_cdent
            else "None of the plans here includes children's dental, so families should add a stand-alone dental plan for the children.")
    if adent_ins:
        parts = []
        for i in adent_ins:
            dl = adent_delta(i)
            rng = m(min(dl)) if min(dl) == max(dl) else f"{m(min(dl))} to {m(max(dl))}"
            parts.append(f"{INS_SHORT[i]} (about {rng} a month more at age 45)")
        dent += " Adult dental and vision come only with the versions that say so, from " + join(parts) + "."
    else:
        dent += " Adult dental and vision are not included in any plan sold here; buy them separately if you want them."
    FAQ.append(("Do the plans include dental and vision?", dent))
    FAQ.append(("What happens if my income is under about $22,000?",
                "North Carolina expanded Medicaid in December 2023. A single adult with income under roughly 138% of the federal poverty level (about $22,000 for one person, $29,900 for a couple, $45,500 for a family of four in 2027) is directed to NC Medicaid rather than receiving a Marketplace subsidy. The Marketplace application checks this automatically."))
    FAQ.append(("When can I enroll?",
                "Open Enrollment for 2027 coverage runs November 1, 2026 through January 15, 2027 on HealthCare.gov. Enroll by December 15 for coverage starting January 1. Outside Open Enrollment you need a qualifying event, such as losing other coverage, moving, marriage or a new baby."))

    # ---------- tables ----------
    net_sorted = sorted(c.nets, key=lambda n: (P[STD[(n, "silver")]]["p45"] if STD[(n, "silver")] else 1e9, n))

    def cheapest_cell(n, mt):
        pid = c.cheapest(mt, net=n)
        return m(P[pid]["p45"]) if pid else "&ndash;"

    net_rows = "".join(
        f'<tr><td><strong>{c.net_label(n)}</strong><br>{c.ptype(n)}, {len(c.by_net(n))} plans</td>'
        + "".join(f'<td class="num">{cheapest_cell(n, mt)}</td>' for mt in METALS)
        + f'<td>{"Included" if c.cdent(n) else "Not included"}</td><td>{c.quality(n)}</td></tr>'
        for n in net_sorted)

    def hcell(k, n):
        s = c.hstat(k, n)
        return {"in": "In network", "out": "<strong>Not in network</strong>", "unlisted": "Not listed", "some": "Some plans"}[s]

    hosp_table = ""
    if hosp_keys:
        hosp_rows = "".join(
            f'<tr><td><strong>{c.hname(k)}</strong><br>{Z["hospitals"][k]["city"]}</td>' + "".join(f"<td>{hcell(k, n)}</td>" for n in net_sorted) + "</tr>"
            for k in hosp_keys)
        unl = (f" &ldquo;Not listed&rdquo;: HealthCare.gov's lookup showed none of the hospitals we checked as in network for {join(unlisted)}, which usually means the insurer's hospital data is missing from the lookup rather than that it has no hospitals; ask the insurer which hospitals its network uses." if unlisted else "")
        note = (" " + c.cfg["hosp_note"]) if c.cfg.get("hosp_note") else ""
        hosp_table = f"""
<div class="table-wrap">
<table class="data">
<caption>Hospital network status on every plan in each network, from HealthCare.gov's doctor and hospital lookup, {CHECKED_H}.{unl}{note} Networks change; confirm before you enroll.</caption>
<thead><tr><th>Hospital</th>{''.join(f'<th>{c.net_label(n)}</th>' for n in net_sorted)}</tr></thead>
<tbody>{hosp_rows}</tbody>
</table>
</div>"""

    std_table = ""
    if len(std_nets) > 1:
        std_label = lambda n: f"{c.net_label(n)}" + ("" if NET_INS[n] == "BCBS" else f" {STD_NAME[NET_INS[n]]}")
        best = std_sorted[0]
        best_attr = {n: (' class="best"' if n == best else "") for n in std_sorted}
        std_rows = "".join(
            f'<tr{best_attr[n]}><td>{std_label(n)}</td>' + "".join(f'<td class="num">{c.full45(STD[(n, mt)])}</td>' for mt in METALS) + "</tr>"
            for n in std_sorted)
        r30 = sum(P[STD[(n, "silver")]]["p"]["s30_100k"] for n in std_nets) / sum(P[STD[(n, "silver")]]["p45"] for n in std_nets)
        r60 = sum(P[STD[(n, "silver")]]["p"]["s60_100k"] for n in std_nets) / sum(P[STD[(n, "silver")]]["p45"] for n in std_nets)
        std_table = f"""
<p>The clearest way to compare the {'insurers' if multi_ins else 'networks'} is through the standardized plans, whose deductibles, copays and out-of-pocket maximums are set by the federal government. Every network sells one at each metal level, so the only differences are the network, the price and extras such as children's dental:</p>

<div class="table-wrap">
<table class="data">
<caption>Standardized ("Easy Pricing") plans in {FULL}: identical benefits, monthly premium at age 45, full price, 2027. Bronze: $7,500 deductible, $12,000 out-of-pocket max. Silver: $6,400 deductible, $10,300 max. Gold: $2,500 deductible, $8,600 max. Multiply by about {r30:.2f} for a 30-year-old and {r60:.2f} for a 60-year-old. Source: HealthCare.gov Marketplace API.</caption>
<thead><tr><th>Insurer and network</th><th class="num">Bronze</th><th class="num">Silver</th><th class="num">Gold</th></tr></thead>
<tbody>{std_rows}</tbody>
</table>
</div>"""
        # every standardized design really has the federal benefits
        for n in std_nets:
            for mt, (ded, moop) in {"bronze": (7500, 12000), "silver": (6400, 10300), "gold": (2500, 8600)}.items():
                dz = Z["designs"][P[STD[(n, mt)]]["key"]]
                assert ded_amount(dz["ded"]) == ded and dz["moop"] == moop, (NAME, n, mt)

    # subsidy table: cheapest Bronze, cheapest Silver, the benchmark, the standardized Silver and Gold at their cheapest, Blue Cross's standardized Silver
    cols = []
    for pid in [cb["bronze"], cb["silver"], bench, c.cheapest("silver", std=True), c.cheapest("gold", std=True),
                c.cheapest("silver", std=True, nets=[n for n in c.nets if NET_INS[n] == "BCBS"])]:
        if pid and pid not in cols:
            cols.append(pid)
    cols = cols[:6]
    def col_head(pid):
        p = P[pid]
        tags = []
        if pid == bench:
            tags.append("benchmark")
        return f'<th class="num">{c.net_label(p["net"]) if p["ins"] == "BCBS" else INS_SHORT[p["ins"]]}<br>{p["design"].replace("UHC ", "")}' + (f'<br>({", ".join(tags)})' if tags else "") + "</th>"
    ROWS = [("Single, 45, $30,000", "s45_30k", True), ("Single, 45, $45,000", "s45_45k", False), ("Single, 45, $100,000", "s45_100k", False),
            ("Single, 27, $35,000", "a27_35k", True), ("Couple, 62 and 60, $58,000", "c62_60_58k", False), ("Family of four (45, 43, 12, 9), $90,000", "fam90k", False)]
    sub_rows = "".join(
        f"<tr><td>{lab}</td>" + "".join(f'<td class="num">{c.net_(pid, sc)}{" (CSR)" if csr and P[pid]["metal"] == "silver" else ""}</td>' for pid in cols) + "</tr>"
        for lab, sc, csr in ROWS)
    silver_cols = [pid for pid in cols if P[pid]["metal"] == "silver"]
    seen, csr_parts87, csr_parts73 = set(), [], []
    for pid in silver_cols:
        if P[pid]["key"] in seen:
            continue
        seen.add(P[pid]["key"])
        same = [c.label(q, short=True) for q in silver_cols if P[q]["key"] == P[pid]["key"]]
        d87, x87 = c.csr(pid, "csr87")
        d73, x73 = c.csr(pid, "csr73")
        csr_parts87.append(f"{d87} and {x87} on {join(same)}")
        csr_parts73.append(f"{d73} and {x73} on {join(same)}")
    csr_note = ("Cells marked CSR include cost-sharing reductions, which also lower the deductible and out-of-pocket maximum. At $30,000 for one person, the deductible and out-of-pocket maximum drop to "
                + join(csr_parts87, "and") + "; at $35,000 (age 27) they drop to " + join(csr_parts73, "and") + ".")

    # things to notice
    notice = []
    if s_lo and s_lo != s_hi:
        notice.append(f"the credit is the same dollar amount whichever plan you choose, so the full-price gaps between {'insurers' if multi_ins else 'networks'} pass straight through to what you pay: the standardized Silver has identical benefits everywhere, yet at $30,000 it costs {c.net_(STD[(s_lo, 'silver')], 's45_30k')} a month from {s_lo} and {c.net_(STD[(s_hi, 'silver')], 's45_30k')} from {s_hi}")
    if bronze_free_30k:
        nfree = sum(1 for p in P.values() if p["metal"] == "bronze" and p["n"]["s45_30k"] == 0)
        nb = c.count_metal("bronze")
        how_many = f"all {NUMW.get(nb, nb)} Bronze plans" if nfree == nb else f"{nfree} of the {nb} Bronze plans, including {c.label(cb['bronze'])}"
        notice.append(f"subsidized households get Bronze plans very cheaply: a 45-year-old earning $30,000 pays $0 for {how_many}")
    else:
        gap = round(bp["p45"]) - round(P[cb["bronze"]]["p45"])
        notice.append(f"no plan here is free at $30,000. At age 45 the cheapest Bronze costs only {m(gap)} a month less than the benchmark, so the credit does not cover it and a 45-year-old earning $30,000 still pays {c.net_(cb['bronze'], 's45_30k')}")
    if no_cdent and with_cdent:
        notice.append(f"families should mind children's dental: {join(no_cdent)} plans leave it out, while {join(with_cdent)} plans include it")
    elif no_cdent:
        notice.append("families should add a stand-alone dental plan for the children, because no plan here includes children's dental")
    ordinals = ["First", "Second", "Third", "Fourth"]
    if len(notice) == 1:
        notice_txt = notice[0][0].upper() + notice[0][1:] + "."
        things = "One thing"
    else:
        notice_txt = " ".join(f"{ordinals[i]}, {t}." for i, t in enumerate(notice))
        things = {2: "Two things", 3: "Three things", 4: "Four things"}[len(notice)]

    # ---------- plan cards ----------
    def card(key):
        dz = Z["designs"][key]
        best, text = TEXT[key]
        plans = sorted([p for p in P.values() if p["key"] == key], key=lambda p: (NET_ORDER.index(p["net"]), p["adent"]))
        metal = dz["metal"]
        if dz["ins"] == "BCBS":
            price = " / ".join(c.full45(p["id"]) for p in plans)
        else:
            base = [p for p in plans if not p["adent"]]
            ext = [p for p in plans if p["adent"]]
            price = c.full45(base[0]["id"]) + (" / " + c.full45(ext[0]["id"]) if ext else "")
        bits = [ded_text(dz["ded"]), f"{m(dz['moop'])} out-of-pocket max"]
        if dz["hsa"]:
            bits.append("HSA-eligible")
        if dz["std"]:
            bits.append("standardized design")
        p0 = [p for p in plans if not p["adent"]][0]
        if metal == "silver":
            d87, x87 = c.csr(p0["id"], "csr87")
            bits.append(f"with cost-sharing reductions at $30,000 income: {d87} deductible, {x87} max")
        extra = []
        if any(p["id"] == bench for p in plans):
            extra.append(f"In {NAME} this is the benchmark plan: your tax credit is calculated from its price.")
        cheapest_here = [p for p in plans if p["id"] == cb[metal]]
        if cheapest_here and c.count_metal(metal) > 1:
            extra.append(f"It is the cheapest {metal.capitalize()} plan in the county.")
        if dz["std"] and len(std_nets) > 1:
            mine = STD.get((p0["net"], metal))
            if mine:
                others = [n for n in std_nets if n != p0["net"] and NET_INS[n] != dz["ins"]]
                if others:
                    by_ins = {}
                    for n in others:
                        by_ins.setdefault(INS_SHORT[NET_INS[n]], []).append(round(P[STD[(n, metal)]]["p45"]) - round(P[mine]["p45"]))
                    def amt(v):
                        lo, hi = min(v), max(v)
                        if lo >= 0:
                            return (m(lo) if lo == hi else f"{m(lo)} to {m(hi)}") + " more"
                        if hi <= 0:
                            return (m(-hi) if lo == hi else f"{m(-hi)} to {m(-lo)}") + " less"
                        return f"{m(-lo)} less to {m(hi)} more"
                    anchor = f" than {p0['net']}'s" if dz["ins"] == "BCBS" and len([x for x in c.nets if NET_INS[x] == "BCBS"]) > 1 else ""
                    extra.append("Identical standardized plans cost " + join([f"{amt(v)} from {who}" for who, v in sorted(by_ins.items(), key=lambda kv: min(kv[1]))]) + f" a month at age 45{anchor}.")
        if metal == "silver" and key in ("AMB|Clear Silver with $0 Insulin Options",):
            extra.append(f"With cost-sharing reductions the deductible and maximum fall to {c.csr(p0['id'], 'csr87')[0]} at $30,000 for one person and {c.csr(p0['id'], 'csr73')[0]} at $35,000.")
        body = text + (" " + " ".join(extra) if extra else "")
        return f"""<details class="plan {metal}">
<summary><span class="plan-name">{dz['design']}</span> <span class="plan-price">{price}</span><span class="plan-best">Best for: {best}</span></summary>
<p class="plan-meta">{' &middot; '.join(bits)}</p>
<p>{body}</p>
</details>"""

    def insurer_section(i):
        keys = sorted({p["key"] for p in P.values() if p["ins"] == i},
                      key=lambda k: (METALS.index(Z["designs"][k]["metal"]), min(p["p45"] for p in P.values() if p["key"] == k)))
        n = c.count_ins(i)
        nets_i = [x for x in c.nets if NET_INS[x] == i]
        if i == "BCBS":
            head = f"Blue Cross NC ({n} plans" + (": " + join([f"{c.net_label(x)} {c.ptype(x)}" for x in nets_i]) if len(nets_i) > 1 else f", {c.ptype(nets_i[0])}") + ")"
            parts = []
            if len(nets_i) > 1:
                parts.append(f"The same 10 designs and benefits in {NUMW[len(nets_i)]} networks; prices are " + " / ".join(nets_i) + ".")
            else:
                parts.append(f"All 10 designs are sold in one network here, {c.net_label(nets_i[0])}.")
        else:
            head = f"{INS_SHORT[i]} ({n} plans, {c.ptype(nets_i[0])})"
            parts = []
        def facts(x):
            ins_h = [c.hname(k) for k in key_hosp if c.hstat(k, x) == "in"]
            out_h = [c.hname(k) for k in key_hosp if c.hstat(k, x) == "out"]
            hp = []
            if ins_h:
                hp.append(join(ins_h) + " in network")
            if out_h:
                hp.append("<strong>" + join(out_h) + " not in network</strong>")
            if key_hosp and not ins_h and not out_h:
                hp.append("hospital network not listed in HealthCare.gov's lookup")
            return hp + ["children's dental included" if c.cdent(x) else "children's dental not included"]
        grouped = {}
        for x in nets_i:
            grouped.setdefault(tuple(facts(x)), []).append(x)
        for f, xs in grouped.items():
            pre = ("" if len(nets_i) == 1 else ("All " + NUMW[len(xs)] + " networks: " if len(xs) == len(nets_i) else join(xs) + ": "))
            parts.append(pre + "; ".join(f) + ".")
        qs = {}
        for x in nets_i:
            qs.setdefault(c.quality(x), []).append(x)
        if len(qs) == 1:
            parts.append(f"HealthCare.gov quality rating: {list(qs)[0].lower() if list(qs)[0] == 'Not yet rated' else list(qs)[0]}.")
        else:
            parts.append("HealthCare.gov quality rating: " + "; ".join(f"{join(xs)} {q.lower() if q == 'Not yet rated' else q}" for q, xs in qs.items()) + ".")
        if i in ("AMB", "UHC", "OSC") and any(p["adent"] for p in P.values() if p["ins"] == i):
            parts.append("Where two prices are shown, the second is the same plan with adult dental and vision added.")
        if i == "UHC":
            parts.insert(0, "$0 insulin on every plan, and $0 virtual urgent care on most.")
        if i == "AMH":
            parts.insert(0, "Free 24/7 virtual primary and urgent care through AmeriHealth's telehealth provider on every plan.")
        cards = "\n".join(card(k) for k in keys)
        return f'<h3 id="plans-{i.lower()}">{head}</h3>\n<p>{" ".join(parts)}</p>\n{cards}\n'

    plans_html = "".join(insurer_section(i) for i in c.ins)

    # ---------- decision 1: networks ----------
    NET_DESC = {
        "Ambetter": "Ambetter of North Carolina's network. As an HMO it covers out-of-network care only in emergencies, but no referrals are needed for specialists. Children's dental is not included.",
        "AmeriHealth Caritas Next": "AmeriHealth Caritas Next's network, with free 24/7 virtual primary and urgent care through its telehealth provider and no referrals. Out-of-network care is covered only in emergencies, and children's dental is not included.",
        "Blue Care": "Blue Cross NC's statewide network. No referrals; out-of-network care is covered only in emergencies. Children's dental is included.",
        "Blue Advantage": "Blue Cross's nationwide option: it adds the national BlueCard network, so you are in network at Blue Cross doctors in every state. Its out-of-network benefit is thin, so treat it as a nationwide in-network plan. Children's dental is included.",
        "Blue Value": "a narrower statewide Blue Cross network. Its out-of-network benefit is thin, so treat it as an in-network plan. Children's dental is included.",
        "Blue Home": "built around UNC Health's hospitals and doctors (the UNC Health Alliance). It covers out-of-network care only in emergencies. Children's dental is included.",
        "UnitedHealthcare": "UnitedHealthcare's network, with $0 insulin on every plan and children's dental included. Out-of-network care is covered only in emergencies.",
        "Oscar": "Oscar's network. Out-of-network care is covered only in emergencies, and children's dental is not included.",
    }

    def net_bullet(n):
        s = f"<li><strong>{c.net_label(n)}</strong> ({len(c.by_net(n))} plans, {c.ptype(n)}) is {NET_DESC[n]}"
        if STD[(n, "silver")] and len(std_nets) > 1:
            rank = std_sorted.index(n)
            if rank == 0:
                s += f" Its standardized plans are the cheapest in the county ({c.full45(STD[(n, 'silver')])} for Silver at age 45)."
            else:
                s += f" Its standardized Silver costs {c.full45(STD[(n, 'silver')])} at age 45, {dm(P[STD[(n, 'silver')]]['p45'], P[STD[(s_lo, 'silver')]]['p45'])} a month more than {s_lo}'s."
        if key_hosp:
            ins_h = [c.hname(k) for k in key_hosp if c.hstat(k, n) == "in"]
            out_h = [c.hname(k) for k in key_hosp if c.hstat(k, n) == "out"]
            if ins_h and out_h:
                s += f" {join(ins_h)} {'was' if len(ins_h) == 1 else 'were'} in network when we checked; <strong>{join(out_h)} {'was' if len(out_h) == 1 else 'were'} not</strong>."
            elif ins_h:
                s += f" {join(ins_h)} {'was' if len(ins_h) == 1 else 'were'} in network when we checked."
            elif out_h:
                s += f" <strong>{join(out_h)} {'was' if len(out_h) == 1 else 'were'} not in network</strong> when we checked."
            else:
                s += " None of the hospitals we checked was listed as in network in HealthCare.gov's lookup; ask the insurer which hospitals it uses."
        return s + "</li>"

    choose = []
    if multi_net and s_lo:
        choose.append(f"<strong>Choose {s_lo} if</strong> your doctors and hospital are in its network: the same benefits cost less there than anywhere else in the county.")
    for sig, ks in hosp_groups():
        w = [n for n, st in zip(c.nets, sig) if st == "in"]
        if multi_net and w and "out" in sig:
            choose.append(f"<strong>If you want to keep using {join([c.hname(k) for k in ks], 'or')}</strong>, look at {join(w, 'or')}.")
    if has_ba:
        choose.append("<strong>Choose Blue Advantage if</strong> you need in-network care outside North Carolina (months away each year, a student at an out-of-state college, frequent travel); it is the only nationwide network sold here.")
    elif multi_net or c.nets:
        choose.append(f"<strong>No plan sold in {NAME} has a nationwide network</strong>, so if you spend months out of state, routine care there will not be covered; every plan still covers emergencies anywhere.")
    if has_uhc:
        choose.append("<strong>Look at UnitedHealthcare if</strong> you use insulin.")

    dirs = ", ".join(f'<a href="{c.d["net_url"][n]}" target="_blank" rel="noopener">{c.net_label(n)}</a>' for n in c.nets if c.d["net_url"].get(n))
    if multi_net:
        dec1_intro = (f"Where Blue Cross is the only insurer, this decision is between two versions of the same plan. In {NAME} it is the decision that matters most, because the networks really differ and the prices differ far more than the benefits do. Start with the doctors and the hospital you want to keep."
                      if multi_ins else
                      f"Blue Cross sells the same 10 designs, with identical benefits, in {NUMW[len(c.nets)]} networks here, so the choice is about doctors and price. Start with the doctors and the hospital you want to keep.")
        dec1 = f"""<h2 id="network">Decision 1: Which {'insurer and network' if multi_ins else 'Blue Cross network'}?</h2>
<p>{dec1_intro}</p>
<ul>
{''.join(net_bullet(n) for n in net_sorted)}
</ul>
<p>{' '.join(choose)}</p>"""
    else:
        n0 = c.nets[0]
        dec1 = f"""<h2 id="network">The network: {c.net_label(n0)}</h2>
<p>Every plan in {NAME} uses one network, so the network decision is made for you. Before you enroll, make sure the doctors and hospital you use are in it.</p>
<ul>
{net_bullet(n0)}
</ul>
<p>{' '.join(choose)}</p>"""
    dec1 += f"""
<p>Before enrolling, check each doctor and your hospital in the plan's own directory ({dirs}), or add them in <a href="{PREVIEW}" target="_blank" rel="noopener">HealthCare.gov's plan preview</a>, which marks every plan as in or out of network for them. In {FULL}, {c.cfg['hospitals']}.</p>"""

    # ---------- decision 2: metal ----------
    bronze = [p for p in P.values() if p["metal"] == "bronze"]
    bded = [ded_amount(Z["designs"][p["key"]]["ded"]) for p in bronze]
    zero_med = sorted({p["key"] for p in bronze if Z["designs"][p["key"]]["ded"].get("medical") == 0})
    gold = [p for p in P.values() if p["metal"] == "gold"]
    gded = [ded_amount(Z["designs"][p["key"]]["ded"]) for p in gold]
    cg = cb["gold"]
    gold_gap = round(P[cg]["p45"]) - round(P[cb["bronze"]]["p45"])
    below = sorted({p["net"] for p in bronze if p["p45"] > P[cg]["p45"]})
    nets_all_bronze_above = [n for n in c.nets if all(p["p45"] > P[cg]["p45"] for p in bronze if p["net"] == n) and any(p["net"] == n for p in bronze)]
    std_silver_any = c.cheapest("silver", std=True)
    d87, x87 = c.csr(std_silver_any, "csr87") if std_silver_any else ("", "")
    seller = P[cg]["net"] if P[cg]["ins"] == "BCBS" else INS_SHORT[P[cg]["ins"]]
    if gold_gap < 150 and multi_net:
        gold_line = f"Gold is unusually affordable here if you buy it from {seller}: {c.label(cg)} costs {m(gold_gap)} a month more than the cheapest Bronze at age 45"
        gold_line += (f", and less than every Bronze plan from {join(nets_all_bronze_above)}." if nets_all_bronze_above else ".")
        gold_line += " It is worth a look if you take brand-name or specialty drugs, see specialists regularly, or are planning surgery or a pregnancy."
    else:
        gold_line = (f"The cheapest Gold, {c.label(cg)}, costs {m(gold_gap)} a month more than the cheapest Bronze at age 45, which is worth it if you take brand-name or specialty drugs, "
                     "see specialists regularly, or are planning surgery or a pregnancy.")
    dec2 = f"""<h2 id="metal">Decision 2: How much coverage do you expect to use?</h2>
<p>Bronze, Silver and Gold describe how costs are split between you and the plan: roughly 60%, 70% and 80% paid by the plan for an average person. In {NAME} the practical differences are these:</p>
<ul>
<li><strong>Bronze</strong> ({c.count_metal("bronze")} plans, {c.metal_range("bronze")} at 45): deductibles up to {m(max(bded))}, so you pay for most care yourself until something serious happens{(', although ' + ('one Bronze design has' if len(zero_med) == 1 else NUMW[len(zero_med)] + ' Bronze designs have') + ' no medical deductible (copays or coinsurance apply from the first dollar instead)') if zero_med else ''}. All {c.count_metal("bronze")} Bronze plans are <strong>HSA-eligible for 2027</strong> under the 2025 federal tax law, which lets you set aside up to $4,500 (single) or $9,000 (family) pre-tax, plus $1,000 if you are 55 or older.</li>
<li><strong>Silver</strong> ({c.count_metal("silver")} plans, {c.metal_range("silver")}): the plans to look at first if you qualify for a subsidy, because incomes under about $39,900 (single) or $82,500 (family of four) unlock <strong>cost-sharing reductions</strong> that only apply to Silver plans. At $30,000 for one person the standardized Silver's deductible drops from $6,400 to {d87} and its out-of-pocket maximum from $10,300 to {x87}. Without a cost-sharing reduction, Silver is a middle ground that often loses to either Bronze or Gold on total cost.</li>
<li><strong>Gold</strong> ({c.count_metal("gold")} plans, {c.metal_range("gold")}): {m(min(gded))} to {m(max(gded))} deductibles and flat copays for most care. {gold_line}</li>
</ul>"""

    # ---------- decision 3: drugs ----------
    special = []
    if has_uhc:
        special.append("UnitedHealthcare includes $0 insulin on every plan")
    if has_amb:
        special.append("Ambetter's Clear Silver has $0 insulin options, and its Enhanced CHF Heart Care and Asthma/COPD Silver plans have $0 options for related prescriptions")
    if has_osc:
        special.append("Oscar has Simple Diabetes plans at the Bronze and Silver levels, with insulin capped at $100 for a 30-day supply")
    diab = ""
    std_b = [(n, STD[(n, "bronze")]) for n in std_nets]
    if len({P[pid]["ins"] for n, pid in std_b}) > 1:
        seen_i, ex = set(), []
        for n, pid in sorted(std_b, key=lambda x: INS_ORDER.index(P[x[1]]["ins"])):
            if P[pid]["ins"] in seen_i:
                continue
            seen_i.add(P[pid]["ins"])
            ex.append((INS_SHORT[P[pid]["ins"]], coverage_example(pid, "diabetes")))
        vals = {v for _, v in ex}
        if len(vals) > 1:
            diab = (" In the official coverage example for a year of managing type 2 diabetes, the estimated cost to you on the standardized Bronze is "
                    + join([f"{v} with {who}" for who, v in ex]) + ": same deductible and copays, different drug lists and insulin terms.")
    dec3 = f"""<h2 id="drugs">Decision 3: How are your prescriptions priced?</h2>
<p>{'Each insurer has its own drug list, so check every prescription against the plans you are considering; our Covanu tool checks a list of medications against every plan in the county at once. (For Blue Cross, the finding from our other county guides holds here: its two drug lists covered the same 48 common drugs.)' if multi_ins else 'Blue Cross uses two drug lists, a 4-tier list on its Standard plans and a 5-tier list on the rest, and the finding from our other county guides holds here: they covered the same 48 common drugs. Our Covanu tool checks a list of medications against every plan at once.'} Beyond coverage, the plan design decides what you pay:</p>
<ul>
<li>On the <strong>standardized plans</strong>, preferred brand drugs are flat copays with no deductible on Silver ($40) and Gold ($30), and specialty drugs are $350 after the deductible on Silver or $250 with no deductible on Gold.</li>
<li>Most <strong>other designs</strong> charge 25% to 50% coinsurance for non-preferred and specialty drugs, usually after a deductible, and several put brand drugs behind the deductible or a separate drug deductible. Someone on an expensive brand drug can pay thousands before the plan contributes.</li>
{('<li><strong>Insulin and condition-specific plans.</strong> ' + '; '.join(special) + '.' + diab + '</li>') if special else ''}
</ul>
<p>The arithmetic for brand and specialty drugs is in <a href="/questions/bronze-vs-silver-medications/">Bronze vs. Silver when you take medications</a>. The short version: one brand-name prescription is often enough to make a standardized Silver cheaper than Bronze over a year, and a specialty drug makes a standardized Gold the cheapest plan on the shelf.</p>"""

    # ---------- situations ----------
    lb = c.cheapest("bronze", "s30_100k")
    low_moop_b = min(bronze, key=lambda p: (Z["designs"][p["key"]]["moop"], p["p45"]))
    fam_b = c.cheapest("bronze", "fam90k", key="n")
    fam_s = c.cheapest("silver", "fam90k", key="n", std=True)
    fam_cd = c.cheapest("bronze", "fam90k", key="n", cdent=True)
    s30 = c.cheapest("silver", "s45_30k", key="n")
    s30_std = c.cheapest("silver", "s45_30k", key="n", std=True)
    r_b, r_s, r_g = c.cheapest("bronze", "c62_60_58k", key="n"), c.cheapest("silver", "c62_60_58k", key="n"), c.cheapest("gold", "c62_60_58k", key="n", std=True)
    g_std = c.cheapest("gold", std=True)
    rows = []
    rows.append(("Healthy 30-year-old, no prescriptions, $100,000 income",
                 f"{c.label(lb)} ({c.net_(lb, 's30_100k')})" + (f" or {c.label(low_moop_b['id'])} ({c.net_(low_moop_b['id'], 's30_100k')})" if low_moop_b["id"] != lb else ""),
                 "No subsidy at this income; the lowest premium in the county, HSA-eligible." + (f" {c.label(low_moop_b['id'])} caps a bad year at {m(Z['designs'][low_moop_b['key']]['moop'])}." if low_moop_b["id"] != lb else "")))
    fam_why = ""
    if not P[fam_b]["cdent"]:
        fam_why = "Add a stand-alone dental plan for the children." + (f" {c.label(fam_cd)} ({c.net_(fam_cd, 'fam90k')}) includes children's dental." if fam_cd else "")
    else:
        fam_why = "Children's dental is included."
    rows.append(("Self-employed, family of four, $90,000",
                 f"{c.label(fam_b)} ({c.net_(fam_b, 'fam90k')}) if everyone is healthy; {c.label(fam_s)} ({c.net_(fam_s, 'fam90k')}) if anyone takes a brand drug", fam_why))
    s30_b = c.cheapest("bronze", "s45_30k", key="n")
    rows.append(("Single, 45, $30,000, sees a doctor a few times a year",
                 f"{c.label(s30)} ({c.net_(s30, 's45_30k')})" + (f" or {c.label(s30_std)} ({c.net_(s30_std, 's45_30k')})" if s30_std != s30 else ""),
                 f"Cost-sharing reductions cut the deductible to {c.csr(s30, 'csr87')[0]}" + (f" or {c.csr(s30_std, 'csr87')[0]}" if s30_std != s30 else "")
                 + f". The cheapest Bronze ({c.net_(s30_b, 's45_30k')}) keeps a {m(ded_amount(Z['designs'][P[s30_b]['key']]['ded']))} deductible."))
    rows.append(("Early retirees, 62 and 60, $58,000 investment and part-time income",
                 f"{c.label(r_b)} ({c.net_(r_b, 'c62_60_58k')}) if you can self-insure the deductible; {c.label(r_s)} ({c.net_(r_s, 'c62_60_58k')}) or {c.label(r_g)} ({c.net_(r_g, 'c62_60_58k')}) if you expect regular care",
                 'Keep income under $86,560 or the subsidy disappears. See <a href="/questions/retiring-before-65-north-carolina/">Retiring before 65 in NC</a>.'))
    if has_ba:
        rows.append(("Spends January through March in Florida, or has a student at an out-of-state college", "Blue Advantage version of whichever Blue Cross design fits",
                     'The only nationwide network in the county. See <a href="/questions/blue-care-vs-blue-advantage-eastern-nc/">Blue Care vs. Blue Advantage</a>.'))
    else:
        rows.append(("Spends months out of state, or has a student at an out-of-state college", "Any plan here covers only emergencies out of state",
                     "No nationwide network is sold in the county. A college's student health plan can cover the student; long stays elsewhere need planning."))
    for sig, ks in hosp_groups():
        w = [n for n, st in zip(c.nets, sig) if st == "in"]
        o = [n for n, st in zip(c.nets, sig) if st == "out"]
        if multi_net and w and "out" in sig:
            it = "It was" if len(ks) == 1 and ks[0] not in PLURAL_H else "They were"
            rows.append((f"Wants to keep doctors at {join([c.hname(k) for k in ks], 'or')}", join(w, "or"),
                         (f"{it} not in network on {join(o, 'or')} plans when we checked. " if o else "") + "Check each doctor too, not just the hospital."))
    ss, sg = c.cheapest("silver", std=True), g_std
    rows.append(("Takes Eliquis, Jardiance or another preferred brand drug", f"{c.label(ss)} or {c.label(sg)}",
                 f"$40 / $30 brand copays with no deductible{(', for less than the same designs cost ' + ('elsewhere in the county' if multi_ins else 'in the other networks')) if len(std_nets) > 1 and P[ss]['net'] == s_lo else ''}. Confirm the drug is on the insurer's list."))
    ins_rows = []
    if has_uhc:
        ins_rows.append("UnitedHealthcare plans")
    if has_amb:
        ins_rows.append("Ambetter Clear Silver")
    if has_osc:
        ins_rows.append("Oscar's Simple Diabetes plans")
    if ins_rows:
        rows.append(("Uses insulin", join(ins_rows, "or"), "Compare the whole year's cost, not just the insulin."))
    rows.append(("Takes a specialty drug (Dupixent, Skyrizi, Enbrel, Rinvoq)", c.label(sg),
                 "$250 specialty copay with no deductible and an $8,600 maximum. Confirm the drug is on the list."))
    big = f"{c.label(sg)} ($8,600 max)"
    if has_amb:
        cl = [p for p in P.values() if p["design"] == "Clear Silver with $0 Insulin Options" and not p["adent"]][0]["id"]
        big += f" or Ambetter Clear Silver ($7,900 max; {c.csr(cl, 'csr87')[0]} with cost-sharing reductions at $30,000, single)"
    rows.append(("Planning surgery or a pregnancy next year", big, "You will reach the deductible anyway; buy the plan with the lowest ceiling."))
    rows.append(("Income near $22,000 (single) or $45,500 (family of four)", "Apply through HealthCare.gov and let it check Medicaid",
                 "NC Medicaid may cover you at no premium; the Marketplace cannot subsidize you below the line."))
    sit_rows = "".join(f"<tr><td>{a}</td><td>{b}</td><td>{w}</td></tr>" for a, b, w in rows)

    # ---------- takeaways ----------
    tk = []
    if multi_ins:
        tk.append(f"<li><strong>{c.N} plans, {NUMW[len(c.ins)]} insurers, {c.D} designs.</strong> " + join([ins_count_phrase(i) for i in c.ins]) + "." + (" Many are one design sold twice, with and without adult dental and vision." if any(p['adent'] for p in P.values()) else "") + "</li>")
    elif multi_net:
        tk.append(f"<li><strong>{c.N} plans, one insurer, {c.D} designs.</strong> Blue Cross sells each of its 10 designs in {NUMW[len(c.nets)]} networks with identical benefits: {join([c.net_label(n) for n in c.nets])}.</li>")
    else:
        tk.append(f"<li><strong>{c.N} plans, one insurer, one network.</strong> Every plan uses Blue Cross's {c.net_label(c.nets[0])} network, an {c.ptype(c.nets[0])} built around UNC Health; the choice is how much coverage you want.</li>")
    if s_lo and s_lo != s_hi:
        tk.append(f"<li><strong>Same benefits, very different prices.</strong> Every network sells the federally standardized Bronze, Silver and Gold designs (marked Easy Pricing on HealthCare.gov). At age 45 {s_lo}'s standardized Silver costs {c.full45(STD[(s_lo, 'silver')])} a month; the identical design costs up to {c.full45(STD[(s_hi, 'silver')])} from {s_hi}.</li>")
    if multi_net:
        tk.append(f"<li><strong>Your subsidy is set by {c.label(bench)}</strong>, the second-cheapest Silver plan ({c.full45(bench)} at full price, age 45). The credit is the same dollar amount whatever you buy, so a 45-year-old earning $30,000 pays {c.net_(bench, 's45_30k')} for that plan and {c.net_(STD[(s_hi, 'silver')], 's45_30k')} for {s_hi}'s standardized Silver.</li>" if s_hi else "")
    if key_hosp:
        tk.append(f"<li><strong>Check the hospital first.</strong> In HealthCare.gov's lookup on {CHECKED_H}, " + "; ".join(hosp_sentences) + "." + unl_note + "</li>")
    r60 = sum(p["p"]["s60_100k"] for p in P.values()) / sum(p["p45"] for p in P.values())
    r30 = sum(p["p"]["s30_100k"] for p in P.values()) / sum(p["p45"] for p in P.values())
    tk.append(f"<li><strong>Full-price premiums for a 45-year-old</strong> run {c.metal_range('bronze')} for Bronze, {c.metal_range('silver')} for Silver and {c.metal_range('gold')} for Gold. A 60-year-old pays about {r60:.1f} times that; a 30-year-old about {r30:.1f} times.</li>")
    if not has_ba:
        tk.append(f"<li><strong>No nationwide network.</strong> Every plan sold in {NAME} is built around North Carolina providers and covers only emergencies out of state.</li>")
    tk.append(f"<li><strong>No referrals and no catastrophic plan.</strong> None of the plans requires a referral to see a specialist, and no catastrophic plan is offered in {NAME} for 2027.</li>")
    takeaways = "\n".join(t for t in tk if t)

    # ---------- market paragraph ----------
    if multi_ins:
        market_p = (f"{NAME} has {NUMW[len(c.ins)]} Marketplace insurers, but the number of plans overstates how hard the choice is. The {c.N} plans are {c.D} designs, many of them sold more than once, and they come in {NUMW[len(c.nets)]} networks. "
                    f"That makes three decisions, in order: <a href=\"#network\">which insurer and network</a> (start with your doctors and hospital), <a href=\"#metal\">how much coverage</a>, and <a href=\"#drugs\">how your prescriptions are priced</a>. "
                    f"The designs are then <a href=\"#plans\">described insurer by insurer</a>, and a <a href=\"#situations\">situations table</a> maps common {NAME} households to the plans worth a close look.")
    elif multi_net:
        market_p = (f"{NAME} has one Marketplace insurer, Blue Cross NC, which sells its 10 designs in {NUMW[len(c.nets)]} networks, so the {c.N} plans are really {c.D} choices of coverage and {NUMW[len(c.nets)]} choices of network. "
                    f"That makes three decisions, in order: <a href=\"#network\">which network</a> (start with your doctors and hospital), <a href=\"#metal\">how much coverage</a>, and <a href=\"#drugs\">how your prescriptions are priced</a>. "
                    f"The designs are then <a href=\"#plans\">described one by one</a>, and a <a href=\"#situations\">situations table</a> maps common {NAME} households to the plans worth a close look.")
    else:
        market_p = (f"{NAME} has one Marketplace insurer and one network for 2027: Blue Cross NC's {c.net_label(c.nets[0])}. The {c.N} plans are Blue Cross's 10 designs, so the choices are <a href=\"#metal\">how much coverage</a> and <a href=\"#drugs\">how your prescriptions are priced</a>, after you confirm that <a href=\"#network\">the network</a> includes your doctors. "
                    f"The designs are <a href=\"#plans\">described one by one</a>, and a <a href=\"#situations\">situations table</a> maps common {NAME} households to the plans worth a close look.")

    # ---------- related links ----------
    same_zone = [x for x in MULTI_GUIDES + ZONE_EXTRA + [x for x in COUNTIES if x["ra"] == "ra14"] if x["ra"] == f"ra{zone}" and x["slug"] != c.slug]
    same_zone_links = join([f'<a href="/counties/{x["slug"]}/">{x["name"]}</a>' for x in sorted(same_zone, key=lambda x: x["name"])])
    share = "county shares" if len(same_zone) == 1 else "counties share"
    related = (f'<p class="related"><strong>Same rating area:</strong> {same_zone_links} {share} {NAME}&rsquo;s rating area ({zone}), so a plan sold in both costs the same, but the plans on offer differ from county to county. '
               f'<strong>Other county guides:</strong> <a href="/counties/">all county guides</a>.</p>') if same_zone else '<p class="related"><a href="/counties/">All county guides</a>.</p>'

    lede = (f"If you buy your own health insurance in {FULL} ({c.cfg['towns']}) you have {NUMW[len(c.ins)]} insurers and {c.N} Marketplace plans to choose from for 2027: {join(ins_names)}. "
            f"This guide uses the official HealthCare.gov plan data for {FULL} to explain what the plans cost, how the insurers and their networks differ, and which plan fits which situation.") if multi_ins else (
            f"If you buy your own health insurance in {FULL} ({c.cfg['towns']}) you have one insurer, Blue Cross and Blue Shield of North Carolina, and {c.N} Marketplace plans for 2027"
            + (f": its 10 designs, each sold in {NUMW[len(c.nets)]} networks ({join([c.net_label(n) for n in c.nets])})." if multi_net else f", all in one network: {c.net_label(c.nets[0])}, an EPO built around UNC Health.")
            + f" This guide uses the official HealthCare.gov plan data for {FULL} to explain what the plans cost, how the {'networks differ' if multi_net else 'plans differ'}, and which plan fits which situation.")

    toc_net = "which insurer and network" if multi_ins else ("which Blue Cross network" if multi_net else "the network")
    body = f"""
<h1>Health Insurance in {FULL}, NC for 2027: All {c.N} Plans Explained</h1>
{byline_multi("{READING}")}

<p class="lede">{lede}</p>

<nav class="toc" aria-label="In this guide">
<strong>In this guide</strong>
<ol>
<li><a href="#market">The market at a glance</a> and <a href="#subsidies">what subsidies do</a></li>
<li><a href="#network">{'Decision 1: ' if multi_net else ''}{toc_net}</a></li>
<li><a href="#metal">Decision 2: how much coverage</a></li>
<li><a href="#drugs">Decision 3: how prescriptions are priced</a></li>
<li><a href="#plans">The {c.D} plan designs</a> (click a plan to expand)</li>
<li><a href="#situations">If you are&hellip; look at&hellip;</a></li>
<li><a href="#faq">Questions</a></li>
</ol>
</nav>

<div class="takeaways">
<h2>Key takeaways</h2>
<ul>
{takeaways}
</ul>
</div>

<h2 id="market">The {FULL} market at a glance</h2>
<p>{market_p}</p>

<div class="table-wrap">
<table class="data">
<caption>The {NUMW[len(c.nets)] + ' networks' if multi_net else 'network'} in {FULL}, 2027. Cheapest full-price monthly premium at age 45 at each metal level, no subsidy. Quality rating is HealthCare.gov's star rating. Source: HealthCare.gov Marketplace API.</caption>
<thead><tr><th>Network</th><th class="num">Cheapest<br>Bronze</th><th class="num">Cheapest<br>Silver</th><th class="num">Cheapest<br>Gold</th><th>Children's dental</th><th>Quality rating</th></tr></thead>
<tbody>{net_rows}</tbody>
</table>
</div>
{hosp_table}
{std_table}

<h3 id="subsidies">What subsidies do to those numbers</h3>
<p>The premium tax credit is a fixed dollar amount based on your income and the price of the second-cheapest Silver plan, which in {NAME} is {c.label(bench)} ({c.full45(bench)} a month at age 45). You can spend the credit on any plan. Because the enhanced credits of 2021&ndash;2025 have expired, the credit stops entirely at 400% of the federal poverty level ($63,840 for one person, $86,560 for a couple, $132,000 for a family of four), and the Marketplace now recovers any overpaid credit in full at tax time, so your income estimate matters. Here is what {NUMW[len(cols)]} plans cost real {NAME} households after the credit:</p>

<div class="table-wrap">
<table class="data">
<caption>Net monthly premium after the premium tax credit, {FULL}, 2027. "CSR": cost-sharing reductions apply (see below). Source: HealthCare.gov Marketplace API.</caption>
<thead><tr><th>Household and income</th>{''.join(col_head(pid) for pid in cols)}</tr></thead>
<tbody>{sub_rows}</tbody>
</table>
</div>

<p>{csr_note}</p>

<p>{things} to notice. {notice_txt} And as everywhere in North Carolina, a single adult under about $22,000 or a couple under about $29,900 is sent to NC Medicaid instead of receiving a Marketplace credit; the application sorts this out.</p>

{dec1}

{dec2}

{dec3}

<h2 id="plans">The {c.D} plan designs{', insurer by insurer' if multi_ins else ''}</h2>
<p>Prices are full-price monthly premiums for a 45-year-old in {FULL}. Click a plan to expand its details. Benefit amounts are in-network, individual coverage, no cost-sharing reduction unless noted.</p>
{plans_html}

<h2 id="situations">If you are&hellip; look at&hellip;</h2>
<div class="table-wrap">
<table class="data">
<caption>Starting points, not recommendations. Prices are monthly in {FULL} after any subsidy. Confirm your doctors and drugs and run your own numbers before deciding.</caption>
<thead><tr><th>Situation</th><th>Start with</th><th>Why</th></tr></thead>
<tbody>
{sit_rows}
</tbody>
</table>
</div>

<div class="callout caution">
<p><strong>About the prices on this page.</strong> Premiums, tax credits, cost-sharing reductions and benefits come from the HealthCare.gov Marketplace API for {FULL} (ZIP {c.d['zip']}, FIPS {c.fips}), plan year 2027, non-tobacco users, retrieved {CHECKED_H}; every price on this page is HealthCare.gov's own figure for that household. Every ZIP code in the county returned the same {c.N} plans. Your own price depends on each household member's age, your income estimate and whether anyone uses tobacco. Confirm benefits in the plan's Summary of Benefits and Coverage before you enroll.</p>
</div>

{related}

{cta(f"See every {FULL} plan with your subsidy applied")}

{author_box()}

{sources([
    f'<a href="{API}" target="_blank" rel="noopener">HealthCare.gov Marketplace API</a>, plan year 2027, {FULL} (ZIP {c.d["zip"]}, FIPS {c.fips}), retrieved {CHECKED_H}: plans, premiums and tax credits for each household, cost-sharing reductions, benefits and coverage examples.',
    f'HealthCare.gov doctor and hospital lookup (provider coverage), every plan in {FULL}, {CHECKED_H}.' if hosp_keys else '',
    '<a href="https://aspe.hhs.gov/topics/poverty-economic-mobility/poverty-guidelines" target="_blank" rel="noopener">HHS 2026 Poverty Guidelines</a> (used for 2027 Marketplace eligibility).',
    '<a href="https://kff.org/affordable-care-act/9-things-to-watch-for-the-2027-aca-open-enrollment-period/" target="_blank" rel="noopener">KFF, 9 Things to Watch for the 2027 ACA Open Enrollment Period</a> (expiration of enhanced credits, repayment caps, catastrophic plan eligibility).',
    'IRS Rev. Proc. 2026-24 (2027 HSA limits) and IRS Notice 2026-5 (Bronze and catastrophic Marketplace plans treated as HSA-eligible high-deductible plans).',
] if True else [])}
"""
    body = body.replace("<li></li>", "")
    import re as _re
    words = len(_re.sub(r"<[^>]+>", " ", body).split()) + sum(len((q + " " + a).split()) for q, a in FAQ)
    reading = f"{max(5, round(words / 335))} minute read"
    body = body.replace("{READING}", reading)
    saved = fbsite.UPDATED
    fbsite.UPDATED = CHECKED
    try:
        page(c.path, TITLE, DESC, "/counties/", CRUMBS, body, faq=FAQ, reading=reading)
    finally:
        fbsite.UPDATED = saved
    return c


def byline_multi(reading):
    return (f'<p class="byline">By <a href="/#about">Kurt Conger</a>, independent licensed NC health insurance agent (NPN 21720013) '
            f'&middot; Updated {CHECKED_H} &middot; {reading} &middot; Plan data: HealthCare.gov Marketplace API, 2027 plan year</p>')


# New Hanover is listed with its rating area's guides in the related links
ZONE_EXTRA = [dict(slug="new-hanover", name="New Hanover", ra="ra15")]

if __name__ == "__main__":
    for g in MULTI_GUIDES:
        build(g)
