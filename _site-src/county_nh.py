"""New Hanover County (Wilmington) guide: 75 Marketplace plans from four insurers, 2027 plan year.

Data: nh_2027.json, collected from the HealthCare.gov plan preview (window shopping) for ZIP 28401 /
FIPS 37129 on November 10, 2026. Age-45 prices, after-credit prices for the single and family
households, cost-sharing reductions and the hospital network check are HealthCare.gov's own figures;
ages 27, 30 and 60 and some couple prices are calculated with the federal default age curve, which
reproduced HealthCare.gov's prices to within 3 cents wherever we compared.
"""
import json, os, re
import fbsite
from fbsite import *
from counties import money, NET_HMO, NET_PPO

HERE = os.path.dirname(os.path.abspath(__file__))
D = json.load(open(os.path.join(HERE, "nh_2027.json"), encoding="utf-8"))
P = D["plans"]
APTC = D["aptc"]

NAME = "New Hanover"
FULL = "New Hanover County"
PATH = "/counties/new-hanover/"
CHECKED = "2026-11-10"
CHECKED_H = "November 10, 2026"
HOSPITAL = "Novant Health New Hanover Regional Medical Center"
HOSPITALS = ("Novant Health New Hanover Regional Medical Center in Wilmington is the hospital most residents use, "
             "and Novant's Scotts Hill Medical Center, a satellite of New Hanover Regional, opened north of town in June 2026")
PREVIEW = "https://www.healthcare.gov/see-plans/"
SCOTTS_HILL = "https://www.novanthealth.org/scotts-hill-medical-center/"
ZONE15_OTHERS = ["Brunswick", "Columbus", "Duplin", "Onslow", "Pender"]

INS_NAME = {"AMB": "Ambetter", "BCBS": "Blue Cross NC", "UHC": "UnitedHealthcare", "OSC": "Oscar"}


def network(p):
    if p["ins"] == "BCBS":
        return " ".join(p["name"].split(" ")[:2])  # Blue Value / Blue Care / Blue Advantage
    return INS_NAME[p["ins"]]


def design(p):
    n = p["name"]
    if p["ins"] == "BCBS":
        return re.sub(r"^Blue (Value|Care|Advantage) ", "", n.split(" | ")[0].split(" {P} ")[0])
    if p["ins"] == "AMB":
        return n.replace(" + Vision + Adult Dental", "")
    if p["ins"] == "UHC":
        return re.sub(r"\s*\(.*\)$", "", n).replace("+", "").strip()
    return n.replace(" with Adult Dental & Vision", "")


for _p in P.values():
    _p["network"] = network(_p)
    _p["design"] = design(_p)

METALS = ["bronze", "silver", "gold"]


def m(x):
    return money(x)


def dm(a, b):
    """Difference of two prices as shown on the page (rounded first, so the arithmetic adds up)."""
    return money(round(a) - round(b))


def full45(pid):
    return m(P[pid]["p45"])


def net(pid, sc):
    return m(P[pid]["net"][sc])


def find(ins, dname, network_name=None, extras=False):
    """The plan of a design (without adult dental/vision unless extras=True)."""
    hits = [p for p in P.values() if p["ins"] == ins and p["design"] == dname
            and (network_name is None or p["network"] == network_name) and bool(p["adult_dental"]) == extras]
    assert len(hits) == 1, (ins, dname, network_name, extras, len(hits))
    return hits[0]["id"]


# key plans
SEB = find("AMB", "Signature Expanded Bronze")
EVB = find("AMB", "Everyday Bronze")
STS = find("AMB", "Streamlined Silver")
CLS = find("AMB", "Clear Silver with $0 Insulin Options")
SGS = find("AMB", "Signature Silver")
SGG = find("AMB", "Signature Gold")
CMG = find("AMB", "Complete Gold")
CHF = find("AMB", "Enhanced CHF Heart Care Silver $0 Rx Options")
BC_SS = find("BCBS", "Silver Standard", "Blue Care")
BC_SP = find("BCBS", "Silver Preferred", "Blue Care")
BV_BB = find("BCBS", "Bronze Basic", "Blue Value")
BV_SP = find("BCBS", "Silver Preferred", "Blue Value")
BV_HSA = find("BCBS", "Bronze HSA Eligible Plus", "Blue Value")
UHC_BS = find("UHC", "UHC Bronze Standard")
OSC_BS = find("OSC", "Bronze Classic Standard")

# the benchmark (second-lowest-cost Silver) at age 45
_silvers = sorted((p for p in P.values() if p["metal"] == "silver"), key=lambda p: p["p45"])
assert _silvers[1]["id"] == CLS, "benchmark plan changed"

# ---------- derived figures ----------
NETWORKS = ["Ambetter", "Blue Value", "Blue Care", "UnitedHealthcare", "Oscar", "Blue Advantage"]
NET_TYPE = {"Ambetter": "HMO", "Blue Value": "POS", "Blue Care": "HMO", "UnitedHealthcare": "HMO", "Oscar": "HMO", "Blue Advantage": "PPO"}
by_net = {n: [p for p in P.values() if p["network"] == n] for n in NETWORKS}
assert sum(len(v) for v in by_net.values()) == len(P) == 75


def cheapest(n, metal, key="p45"):
    return min(p[key] for p in by_net[n] if p["metal"] == metal)


def metal_range(metal):
    v = [p["p45"] for p in P.values() if p["metal"] == metal]
    return f"{m(min(v))} to {m(max(v))}"


def count_metal(metal):
    return sum(1 for p in P.values() if p["metal"] == metal)


def one(vals):
    vals = set(vals)
    assert len(vals) == 1, vals
    return vals.pop()


def quality(n):
    q = one(p["quality"] for p in by_net[n])
    return f"{q} stars" if q else "Not yet rated"


def standardized(n, metal):
    hits = [p for p in by_net[n] if p["easy"] and p["metal"] == metal and not p["adult_dental"]]
    assert len(hits) == 1, (n, metal, [h["name"] for h in hits])
    return hits[0]


STD = {(n, mt): standardized(n, mt)["p45"] for n in NETWORKS for mt in METALS}


def std_gap(metal):
    base = round(STD[("Ambetter", metal)])
    others = [round(STD[(n, metal)]) - base for n in NETWORKS if n != "Ambetter"]
    return m(min(others)), m(max(others))


# Blue Cross network price relationships (same design, different network), age 45 and 60
_bc_designs = sorted({p["design"] for p in by_net["Blue Care"]})


def _bc(net_name, d):
    return P[find("BCBS", d, net_name)]


bv_save = [round(_bc("Blue Care", d)["p45"]) - round(_bc("Blue Value", d)["p45"]) for d in _bc_designs]
ba_add45 = [round(_bc("Blue Advantage", d)["p45"]) - round(_bc("Blue Care", d)["p45"]) for d in _bc_designs]
ba_add60 = [round(_bc("Blue Advantage", d)["p60"]) - round(_bc("Blue Care", d)["p60"]) for d in _bc_designs]
bv_pct = round(100 * (1 - sum(_bc("Blue Value", d)["p45"] for d in _bc_designs) / sum(_bc("Blue Care", d)["p45"] for d in _bc_designs)))

# extra cost of the adult dental + vision versions at 45
def extras_delta(ins):
    out = []
    for d in {p["design"] for p in P.values() if p["ins"] == ins and p["adult_dental"]}:
        out.append(P[find(ins, d, extras=True)]["p45"] - P[find(ins, d)]["p45"])
    return min(out), max(out), len(out)


AMB_X, UHC_X, OSC_X = extras_delta("AMB"), extras_delta("UHC"), extras_delta("OSC")

gold_gap = round(P[SGG]["p45"]) - round(P[SEB]["p45"])
hsa_all_bronze = all(p["hsa"] for p in P.values() if p["metal"] == "bronze") and not any(p["hsa"] for p in P.values() if p["metal"] != "bronze")
assert hsa_all_bronze
nhrmc = {n: one(p["nhrmc"] for p in by_net[n]) for n in NETWORKS}
child_dental = {n: one(p["child_dental"] for p in by_net[n]) for n in NETWORKS}
assert nhrmc == {"Ambetter": True, "Blue Value": True, "Blue Care": True, "UnitedHealthcare": True, "Oscar": False, "Blue Advantage": True}
bronze_below_sgg = sorted({p["network"] for p in P.values() if p["metal"] == "bronze" and p["p45"] < P[SGG]["p45"]})
assert bronze_below_sgg == ["Ambetter", "Blue Value"], bronze_below_sgg
n_designs = len({(p["ins"], p["design"]) for p in P.values()})
assert n_designs == 38, n_designs


def csr(pid, level):
    c = P[pid][level]
    return c["ded"].split(" ;")[0], c["moop"]


def coverage_example(pid, which):
    """SBC coverage examples from HealthCare.gov: having a baby / managing type 2 diabetes / simple fracture."""
    return P[pid]["details"]["ex"].split(" / ")[{"baby": 0, "diabetes": 1, "fracture": 2}[which]]


# ---------- plan cards ----------
# (meta line, description, best for). Benefits are in-network, individual coverage, no cost-sharing reduction.
s_lo, s_hi = std_gap("silver")
b_lo, b_hi = std_gap("bronze")
g_lo, g_hi = std_gap("gold")

TEXT = {
    # ---- Ambetter ----
    ("AMB", "Signature Expanded Bronze"): (
        "$7,500 deductible (medical and drugs combined) &middot; $12,000 out-of-pocket max &middot; HSA-eligible &middot; standardized design",
        f"The federally standardized Bronze at the lowest price in the county. Primary care is $50, specialists $100 and urgent care $75 from day one; generics are $25; after the deductible, brand drugs are flat copays of $50 (preferred), $100 (non-preferred) and $500 (specialty). Imaging, the emergency room and hospital stays are 50% coinsurance after the deductible. Blue Cross, Oscar and UnitedHealthcare sell exactly the same benefits for {b_lo} to {b_hi} more a month at age 45.",
        "the lowest premium in the county with copays for office visits; HSA savers"),
    ("AMB", "Everyday Bronze"): (
        "$9,350 deductible &middot; $11,000 out-of-pocket max &middot; HSA-eligible",
        f"$3 generics and lower office copays than the standardized Bronze ($40 primary care, $90 specialists, $50 urgent care), in exchange for a $9,350 deductible and coinsurance instead of copays for brand drugs (45%) and specialty drugs (50%) after it. It costs about {dm(P[EVB]['p45'], P[SEB]['p45'])} a month more than Signature Expanded Bronze at age 45 and has a $1,000 lower out-of-pocket maximum.",
        "healthy adults who take only inexpensive generics"),
    ("AMB", "Elite Bronze"): (
        "$0 medical deductible &middot; separate $4,850 drug deductible &middot; $11,900 out-of-pocket max &middot; HSA-eligible",
        "No medical deductible: office visits are copays ($55 primary care, $120 specialists, $60 urgent care) and imaging and hospital stays are 50% coinsurance from the first dollar. The catches are a $4,000 emergency room copay, $195 preferred brand drugs, and a separate $4,850 deductible before non-preferred and specialty drugs are covered (then 45% and 50%). Generics are $3.",
        "people who want office visits and generics covered without a deductible and rarely use the emergency room"),
    ("AMB", "Streamlined Silver"): (
        "$4,700 deductible &middot; $11,300 out-of-pocket max &middot; with cost-sharing reductions at $30,000 income: {} deductible, {} max".format(*csr(STS, "csr87")),
        "The cheapest Silver in the county, and strong on everyday care: $20 primary care, $60 specialists, $55 urgent care and $3 generics from day one. Preferred brand drugs are $30 after the deductible; non-preferred and specialty drugs, imaging and hospital care are 30% to 45% coinsurance after it. With cost-sharing reductions at $30,000 for one person, primary care drops to $10 and specialists to $30.",
        "subsidized households who mostly see doctors and take generics"),
    ("AMB", "Clear Silver with $0 Insulin Options"): (
        "$7,900 deductible equal to the out-of-pocket max &middot; the county's benchmark plan &middot; with cost-sharing reductions at $30,000 income: {} deductible and max".format(csr(CLS, "csr87")[0]),
        "The plan your tax credit is calculated from, because it is the second-cheapest Silver in the county. It works like a high-deductible plan: office visits are copays from day one ($50 primary care, $100 specialists, $75 urgent care), but prescriptions, imaging and hospital care are yours to pay until the $7,900 deductible, and after that the plan pays 100%. As the name says, some insulins are $0. With cost-sharing reductions the deductible and the maximum fall together: to {} at $30,000 for one person and {} at $35,000.".format(csr(CLS, "csr87")[0], csr(CLS, "csr73")[0]),
        "subsidized households expecting a big year (a surgery, a birth) who want the lowest possible ceiling"),
    ("AMB", "Signature Silver"): (
        "$6,400 deductible &middot; $10,300 out-of-pocket max &middot; standardized design &middot; with cost-sharing reductions at $30,000 income: {} deductible, {} max".format(*csr(SGS, "csr87")),
        f"The federally standardized Silver: $40 primary care, $80 specialists, $60 urgent care, $20 generics and $40 preferred brand drugs as copays from day one, with no deductible. Non-preferred brands ($80) and specialty drugs ($350) come after the deductible, and hospital care is 40% coinsurance after it. Blue Cross, Oscar and UnitedHealthcare sell exactly the same benefits for {s_lo} to {s_hi} more a month at age 45.",
        "anyone taking a preferred brand-name drug, and subsidized households who want flat copays"),
    ("AMB", "Enhanced CHF Heart Care Silver $0 Rx Options"): (
        "$5,200 deductible &middot; $10,300 out-of-pocket max &middot; with cost-sharing reductions at $30,000 income: {} deductible, {} max".format(*csr(CHF, "csr87")),
        "Designed for people with congestive heart failure, with $0 options for some related prescriptions (check the plan's drug list for yours). Otherwise a mid-deductible Silver with low office copays ($25 primary care, $55 specialists, $40 urgent care), $3 generics and $75 preferred brands; imaging and hospital care are 50% after the deductible. It is the only Silver plan in the county whose deductible drops to $0 with cost-sharing reductions at $30,000 income.",
        "people managing heart failure"),
    ("AMB", "Enhanced Asthma/COPD Care Silver $0 Rx Options"): (
        "$5,900 deductible &middot; $9,400 out-of-pocket max &middot; with cost-sharing reductions at $30,000 income: {} deductible, {} max".format(*csr(find("AMB", "Enhanced Asthma/COPD Care Silver $0 Rx Options"), "csr87")),
        "Designed for people with asthma or COPD, with $0 options for some related prescriptions (check the drug list for your inhalers). $40 primary care, $60 specialists, $50 urgent care, $3 generics and $75 preferred brands; imaging and hospital care are 50% after the deductible. Its $9,400 out-of-pocket maximum is lower than any other Ambetter Silver except Clear Silver.",
        "people managing asthma or COPD"),
    ("AMB", "Signature Gold"): (
        "$2,500 deductible &middot; $8,600 out-of-pocket max &middot; standardized design",
        f"The federally standardized Gold, with flat copays and no deductible for office visits ($30 primary care, $60 specialists, $45 urgent care) and for every drug tier ($15 generics, $30 preferred brand, $60 non-preferred, $250 specialty). Hospital care is 25% coinsurance after the deductible. At {full45(SGG)} a month at age 45 it costs less than every Bronze plan from Blue Care, Blue Advantage, UnitedHealthcare and Oscar, and only {m(gold_gap)} more than the cheapest Bronze in the county.",
        "specialty drugs, regular specialist care, or a planned surgery or pregnancy"),
    ("AMB", "Complete Gold"): (
        "$1,450 deductible &middot; $9,500 out-of-pocket max",
        f"Richer everyday benefits than Signature Gold: $15 primary care, $35 specialists and urgent care, $3 generics and $30 preferred brands, with 20% coinsurance for imaging and hospital care after a $1,450 deductible. The trade-offs are about {dm(P[CMG]['p45'], P[SGG]['p45'])} a month more at age 45, a higher out-of-pocket maximum ($9,500 against $8,600) and coinsurance (25% and 30%) rather than copays for non-preferred and specialty drugs.",
        "frequent doctor visits with generic or preferred-brand prescriptions"),

    # ---- Blue Cross NC (same 10 designs and benefits as the eastern-county guides) ----
    ("BCBS", "Bronze Basic"): (
        "$7,000 deductible (medical and drugs combined) &middot; $12,000 out-of-pocket max &middot; HSA-eligible",
        f"Three primary care visits a year are free, then $95; specialists are $175; preferred generics are $25. Everything else, including brand drugs, imaging, the emergency room and hospital stays, is 50% coinsurance after the $7,000 deductible. It is Blue Cross's cheapest plan, but even its Blue Value version costs {dm(P[BV_BB]['p45'], P[SEB]['p45'])} a month more at age 45 than Ambetter's standardized Bronze.",
        "a Blue Cross network at the lowest Blue Cross price, mainly as protection against a large bill"),
    ("BCBS", "Bronze Standard"): (
        "$7,500 deductible &middot; $12,000 out-of-pocket max &middot; HSA-eligible &middot; standardized design",
        "The federally standardized Bronze: $50 primary care and $100 specialist copays from day one, $25 generics, and after the deductible flat copays of $50 (preferred brand), $100 (non-preferred) and $500 (specialty). Ambetter, Oscar and UnitedHealthcare sell the same benefits; the Blue Cross version adds children's dental, which Ambetter and Oscar plans do not include.",
        "Bronze buyers who want copays rather than coinsurance on a Blue Cross network"),
    ("BCBS", "Bronze Complete"): (
        "$4,000 medical deductible plus a separate $1,000 drug deductible &middot; $12,000 out-of-pocket max &middot; HSA-eligible",
        "The lowest medical deductible among Blue Cross's Bronze plans. Primary care is $60, specialists $120, generics $20. Brand drugs become $75 (preferred) or $150 (non-preferred) copays once you have met the separate $1,000 drug deductible, which is reached quickly on any brand medication. Hospital care is 50% after the $4,000 medical deductible.",
        "Bronze buyers with one or two brand-name prescriptions"),
    ("BCBS", "Bronze HSA Eligible Plus"): (
        "$8,700 deductible equal to the out-of-pocket max &middot; HSA-eligible",
        "A true high-deductible plan: you pay everything except preventive care until you reach $8,700, and then the plan pays 100%. There are no copays to track. The appeal is the hard ceiling, $3,300 lower than the $12,000 maximum on most Bronze plans. Pair it with the maximum HSA contribution and the deductible is partly funded with pre-tax dollars.",
        "disciplined HSA savers who want the lowest worst-case cost on a Bronze plan"),
    ("BCBS", "Silver Preferred"): (
        "$2,700 deductible &middot; $12,000 out-of-pocket max &middot; with cost-sharing reductions at $30,000 income: {} deductible, {} max".format(*csr(BC_SP, "csr87")),
        f"Three free primary care visits then $35, specialists $75, generics $15. Every brand and specialty drug is 50% coinsurance after the deductible. Its $325 deductible with cost-sharing reductions at $30,000 income is among the lowest in the county, but here the premium after the credit is not: a 45-year-old earning $30,000 pays {net(BV_SP, 's45_30k')} a month for the Blue Value version and {net(BC_SP, 's45_30k')} for Blue Care, against {net(STS, 's45_30k')} for Ambetter's Streamlined Silver.",
        "subsidized households who want a Blue Cross network and take mostly generics"),
    ("BCBS", "Silver Standard"): (
        "$6,400 deductible &middot; $10,300 out-of-pocket max &middot; standardized design &middot; with cost-sharing reductions at $30,000 income: {} deductible, {} max".format(*csr(BC_SS, "csr87")),
        f"The federally standardized Silver: $40 primary care, $80 specialist, $20 generic and $40 preferred brand copays from day one; non-preferred brands ($80) and specialty drugs ($350) after the deductible. In counties where Blue Cross is the only insurer this is the benchmark plan; here the benchmark is Ambetter's Clear Silver, so the identical Ambetter Signature Silver costs {dm(P[find('BCBS', 'Silver Standard', 'Blue Value')]['p45'], P[SGS]['p45'])} to {dm(P[find('BCBS', 'Silver Standard', 'Blue Advantage')]['p45'], P[SGS]['p45'])} a month less at age 45.",
        "anyone on a preferred brand-name drug who wants a Blue Cross network"),
    ("BCBS", "Silver Choice A"): (
        "$3,500 medical deductible plus $200 drug deductible &middot; $12,000 out-of-pocket max",
        "A middle path between the two other Blue Cross Silvers: three free primary care visits then $45, specialists $95, generics $15, and brand drugs at $35 (preferred) or $70 (non-preferred) copays after a small $200 drug deductible. Specialty drugs and hospital care are 50% after the deductibles.",
        "Blue Cross members who want a lower medical deductible than Silver Standard and take at most one or two brand drugs"),
    ("BCBS", "Gold Premier A"): (
        "$1,800 medical deductible plus $400 drug deductible &middot; $12,000 out-of-pocket max",
        "Blue Cross's cheapest Gold. Three free primary care visits then $15, specialists $45, generics $10, brand drugs $35 or $60 after the $400 drug deductible. Hospital and emergency care are 30% after the $1,800 deductible, and specialty drugs are 50% after the deductible, which is the catch: strong for doctor visits and ordinary prescriptions, weak for specialty medications.",
        "frequent doctor visits and brand-name (not specialty) prescriptions on a Blue Cross network"),
    ("BCBS", "Gold Standard A"): (
        "$2,500 deductible &middot; $8,600 out-of-pocket max &middot; standardized design",
        f"The federally standardized Gold: primary care $30, specialists $60, generics $15, preferred brand $30, non-preferred $60 and specialty $250, all copays with no deductible; hospital care is 25% after the deductible. Ambetter sells the identical design, as Signature Gold, for {dm(P[find('BCBS', 'Gold Standard A', 'Blue Value')]['p45'], P[SGG]['p45'])} a month less than Blue Value and {dm(P[find('BCBS', 'Gold Standard A', 'Blue Care')]['p45'], P[SGG]['p45'])} less than Blue Care at age 45.",
        "anyone on a specialty drug who wants a Blue Cross network"),
    ("BCBS", "Gold All Copay A"): (
        "$0 deductible &middot; $12,000 out-of-pocket max",
        "No deductible at all. Every service is a fixed copay: $30 primary care, $60 specialist, $10 generic, $60 preferred brand, $120 non-preferred, $220 specialty, $1,500 emergency room and $2,500 per hospital stay. You give up the lower out-of-pocket maximum of Gold Standard A in exchange for never having to meet a deductible.",
        "people who want to know the price of every visit in advance, and those expecting a hospital stay"),

    # ---- UnitedHealthcare ----
    ("UHC", "UHC Bronze Essential"): (
        "$11,750 deductible equal to the out-of-pocket max &middot; HSA-eligible",
        "A pure high-deductible plan: apart from preventive care (and the $0 virtual urgent care and $0 insulin in the plan's name), you pay the full negotiated price of care and drugs until you reach $11,750, and then nothing. The ceiling is only slightly below the $12,000 maximum on most Bronze plans; Blue Cross's Bronze HSA Eligible Plus works the same way with an $8,700 ceiling.",
        "HSA savers who want UnitedHealthcare's network and rarely use care"),
    ("UHC", "UHC Bronze Standard"): (
        "$7,500 deductible &middot; $12,000 out-of-pocket max &middot; HSA-eligible &middot; standardized design",
        f"The standardized Bronze benefits ($50 primary care, $100 specialists, $25 generics, and $50/$100/$500 brand and specialty copays after the deductible) plus UnitedHealthcare's $0 insulin and children's dental. In the official coverage example for a year of managing type 2 diabetes, the estimated cost to you on this plan is {coverage_example(UHC_BS, 'diabetes')}, against {coverage_example(SEB, 'diabetes')} for Ambetter's Signature Expanded Bronze and {coverage_example(OSC_BS, 'diabetes')} for Oscar's version of the same design. The example prices insulin at the plan's own rate, before any manufacturer program.",
        "insulin users who want UnitedHealthcare's network; families who want children's dental included"),
    ("UHC", "UHC Bronze Copay Focus $0 Indiv Med Ded"): (
        "$0 medical deductible &middot; separate $4,000 drug deductible &middot; $12,000 out-of-pocket max &middot; HSA-eligible",
        "No medical deductible: every medical service is a copay from day one, including $55 primary care, $115 specialists, $80 urgent care, $150 imaging, $2,000 for an emergency room visit and $3,000 a day in the hospital, all capped by the $12,000 out-of-pocket maximum. Generics are $20; brand and specialty drugs are 40% to 50% coinsurance after the separate $4,000 drug deductible.",
        "people who want to know what each visit costs in advance and take only generics"),
    ("UHC", "UHC Silver Standard"): (
        "$6,400 deductible &middot; $10,300 out-of-pocket max &middot; standardized design &middot; with cost-sharing reductions at $30,000 income: {} deductible, {} max".format(*csr(find("UHC", "UHC Silver Standard"), "csr87")),
        f"The standardized Silver benefits ($40 primary care, $80 specialists, $20 generics, $40 preferred brands with no deductible) with UnitedHealthcare's $0 insulin and children's dental, for {dm(STD[('UnitedHealthcare', 'silver')], STD[('Ambetter', 'silver')])} a month more than Ambetter's identical Signature Silver at age 45.",
        "insulin users and families who want UnitedHealthcare's network"),
    ("UHC", "UHC Silver Value"): (
        "$3,550 deductible &middot; $11,200 out-of-pocket max",
        "A lower deductible than the standardized Silver, with $5 generics, $40 primary care and $60 urgent care, but $110 specialist visits and preferred brand drugs at $100 after the deductible. Imaging and hospital care are 40% after the deductible; non-preferred and specialty drugs are 40% and 50% coinsurance after it.",
        "generic-drug users who want a lower deductible on UnitedHealthcare's network"),
    ("UHC", "UHC Silver Copay Focus $0 Indiv Med Ded"): (
        "$0 medical deductible &middot; separate $2,500 drug deductible &middot; $12,000 out-of-pocket max",
        "Copays for every medical service from day one: $40 primary care, $100 specialists, $60 urgent care, $65 imaging, $1,500 for an emergency room visit and $2,500 a day in the hospital. Generics are $10; preferred brands are $85 after the $2,500 drug deductible, and non-preferred and specialty drugs are 40% and 50% coinsurance.",
        "people who want no medical deductible on a Silver plan"),
    ("UHC", "UHC Gold Standard"): (
        "$2,500 deductible &middot; $8,600 out-of-pocket max &middot; standardized design",
        f"The standardized Gold benefits (flat copays with no deductible for office visits and every drug tier, including $250 specialty drugs) with $0 insulin and children's dental, at {dm(STD[('UnitedHealthcare', 'gold')], STD[('Ambetter', 'gold')])} a month more than Ambetter's identical Signature Gold at age 45.",
        "insulin users and families who want Gold coverage on UnitedHealthcare's network"),
    ("UHC", "UHC Gold Copay Focus $0 Ded"): (
        "$0 deductible &middot; $10,000 out-of-pocket max",
        "No deductible at all: $20 primary care, $60 specialists, $30 urgent care, $65 imaging, $750 for the emergency room, $2,000 a day in the hospital, $5 generics and $50 preferred brands. Non-preferred and specialty drugs are 40% and 50% coinsurance.",
        "people expecting frequent care who want every price known in advance"),
    ("UHC", "UHC Gold Advantage"): (
        "$850 deductible &middot; $10,400 out-of-pocket max",
        "Low copays ($15 primary care, $50 specialists, $20 urgent care, $1 generics, $30 preferred brands) and 20% coinsurance for the emergency room and hospital after an $850 deductible. Non-preferred and specialty drugs are 30% and 40% coinsurance after the deductible.",
        "frequent doctor visits and generic or preferred-brand drugs on UnitedHealthcare's network"),

    # ---- Oscar ----
    ("OSC", "Bronze Classic Standard"): (
        "$7,500 deductible &middot; $12,000 out-of-pocket max &middot; HSA-eligible &middot; standardized design",
        f"The standardized Bronze benefits ($50 primary care, $100 specialists, $25 generics, $50/$100/$500 brand and specialty copays after the deductible) at {dm(STD[('Oscar', 'bronze')], STD[('Ambetter', 'bronze')])} a month more than Ambetter's identical plan at age 45.",
        "people whose doctors are in Oscar's network and who do not need New Hanover Regional"),
    ("OSC", "Bronze Classic 4700"): (
        "$4,700 deductible &middot; $12,000 out-of-pocket max &middot; HSA-eligible",
        "A lower deductible than most Bronze plans, $4 generics and $40 urgent care, but $70 primary care and $125 specialist visits, and 50% coinsurance for brand drugs, imaging and hospital care.",
        "Bronze buyers who want a lower deductible and take generics"),
    ("OSC", "Bronze Simple Diabetes"): (
        "$5,500 deductible &middot; $12,000 out-of-pocket max &middot; HSA-eligible",
        "Designed for people with diabetes: free endocrinologist visits and diabetic eye and foot exams, $50 primary care, $150 other specialists, $40 urgent care and $4 generics from day one, preferred brands at $75 after the deductible, insulin capped at $100 for a 30-day supply, and 50% coinsurance for imaging, hospital care and other brand drugs.",
        "people with diabetes whose doctors are in Oscar's network"),
    ("OSC", "Bronze Elite + PCP Saver Plus"): (
        "$0 medical deductible &middot; separate $7,500 drug deductible &middot; $12,000 out-of-pocket max &middot; HSA-eligible",
        "Copays for medical care from day one: $50 primary care, $125 specialists, $40 urgent care, $150 imaging, $2,500 for the emergency room and $3,000 a day in the hospital. Generics are $4; preferred brands are $125 after the $7,500 drug deductible, and other brand and specialty drugs are 50% after it.",
        "generic-only Bronze buyers who want no medical deductible"),
    ("OSC", "Silver Classic Standard"): (
        "$6,400 deductible &middot; $10,300 out-of-pocket max &middot; standardized design &middot; with cost-sharing reductions at $30,000 income: {} deductible, {} max".format(*csr(find("OSC", "Silver Classic Standard"), "csr87")),
        f"The standardized Silver benefits ($40 primary care, $80 specialists, $20 generics, $40 preferred brands with no deductible) at {dm(STD[('Oscar', 'silver')], STD[('Ambetter', 'silver')])} a month more than Ambetter's identical Signature Silver at age 45.",
        "people whose doctors are in Oscar's network and who take a preferred brand drug"),
    ("OSC", "Silver Simple PCP Saver"): (
        "$5,750 deductible &middot; $10,000 out-of-pocket max",
        "$20 primary care, $80 specialists, $35 urgent care and $4 generics from day one; preferred brand drugs are $145, and imaging and hospital care are 40% after the deductible. Other brand and specialty drugs are 50% after the deductible.",
        "frequent primary care visits on Oscar's network"),
    ("OSC", "Silver Core Plan"): (
        "$9,000 deductible &middot; $10,300 out-of-pocket max &middot; with cost-sharing reductions at $30,000 income: {} deductible, {} max".format(*csr(find("OSC", "Silver Core Plan"), "csr87")),
        "The highest Silver deductible in the county at full price ($9,000), with $50 primary care, $90 specialists, $4 generics and $150 preferred brands; imaging and hospital care are 50% after the deductible. Cost-sharing reductions change it more than most: at $30,000 income for one person the deductible falls to $300.",
        "subsidized households under about $31,900 (one person) who use Oscar's network"),
    ("OSC", "Silver Simple Diabetes"): (
        "$6,500 deductible &middot; $10,600 out-of-pocket max",
        "Designed for people with diabetes: primary care and endocrinologist visits, diabetic eye and foot exams and the lowest-tier generics are free, other specialists are $40 and urgent care $35, preferred brands are $75 after the deductible, insulin is capped at $100 for a 30-day supply, and imaging and hospital care are 45% after it.",
        "people with diabetes whose doctors are in Oscar's network"),
    ("OSC", "Gold Classic Standard"): (
        "$2,500 deductible &middot; $8,600 out-of-pocket max &middot; standardized design",
        f"The standardized Gold benefits (flat copays with no deductible for office visits and every drug tier, including $250 specialty drugs) at {dm(STD[('Oscar', 'gold')], STD[('Ambetter', 'gold')])} a month more than Ambetter's identical Signature Gold at age 45.",
        "people whose doctors are in Oscar's network and who need Gold coverage"),
}


def groups(ins):
    g = {}
    for pid in D["order"]:
        p = P[pid]
        if p["ins"] == ins:
            g.setdefault(p["design"], []).append(p)
    out = sorted(g.items(), key=lambda kv: (METALS.index(kv[1][0]["metal"]), min(p["p45"] for p in kv[1])))
    return out


def card(ins, dname, plans):
    meta, text, best = TEXT[(ins, dname)]
    metal = plans[0]["metal"]
    if ins == "BCBS":
        price = " / ".join(full45(find("BCBS", dname, n)) for n in ("Blue Value", "Blue Care", "Blue Advantage"))
    else:
        price = full45(find(ins, dname))
        if any(p["adult_dental"] for p in plans):
            price += " / " + full45(find(ins, dname, extras=True))
    return f"""<details class="plan {metal}">
<summary><span class="plan-name">{dname}</span> <span class="plan-price">{price}</span><span class="plan-best">Best for: {best}</span></summary>
<p class="plan-meta">{meta}</p>
<p>{text}</p>
</details>"""


def insurer_section(ins, heading, note):
    gs = groups(ins)
    cards = "\n".join(card(ins, d, ps) for d, ps in gs)
    return f'<h3 id="plans-{ins.lower()}">{heading}</h3>\n<p>{note}</p>\n{cards}\n'


assert set(TEXT) == {(p["ins"], p["design"]) for p in P.values()}, set(TEXT) ^ {(p["ins"], p["design"]) for p in P.values()}


def nh_byline(reading):
    return (f'<p class="byline">By <a href="/#about">Kurt Conger</a>, independent licensed NC health insurance agent (NPN 21720013) '
            f'&middot; Updated {CHECKED_H} &middot; {reading} &middot; Plan data: HealthCare.gov plan preview, 2027 plan year</p>')


def build():
    TITLE = f"{FULL}, NC Health Insurance for 2027: All 75 Marketplace Plans Explained"
    DESC = (f"Every 2027 Marketplace plan in {FULL}, NC (Wilmington): 75 plans from Ambetter, Blue Cross, UnitedHealthcare and Oscar, "
            "prices by age and income, and which networks include New Hanover Regional.")
    CRUMBS = [("/", "Home"), ("/counties/", "County Guides"), (None, FULL)]

    a_lo, a_hi, a_n = AMB_X
    u_lo, u_hi, u_n = UHC_X
    o_lo, o_hi, o_n = OSC_X

    FAQ = [
        (f"Which insurers sell Marketplace plans in {FULL} for 2027?",
         f"Four: Ambetter of North Carolina ({len(by_net['Ambetter'])} plans), Blue Cross and Blue Shield of North Carolina (30), UnitedHealthcare ({len(by_net['UnitedHealthcare'])}) and Oscar ({len(by_net['Oscar'])}), for 75 plans in all. Blue Cross sells each of its 10 designs in three networks (Blue Value, Blue Care and Blue Advantage), and Ambetter, UnitedHealthcare and Oscar sell several designs both with and without adult dental and vision, so the 75 plans come down to {n_designs} distinct designs."),
        (f"Is {HOSPITAL} in network?",
         f"When we checked HealthCare.gov's doctor and hospital lookup on {CHECKED_H}, New Hanover Regional Medical Center was listed as in network on all {len(by_net['Ambetter'])} Ambetter plans, all 30 Blue Cross plans and all {len(by_net['UnitedHealthcare'])} UnitedHealthcare plans, and as out of network on all {len(by_net['Oscar'])} Oscar plans. Networks change, and a hospital being in network does not mean every doctor who works there is, so check the specific doctors and facilities you use before you enroll."),
        ("Why do Blue Cross plans cost so much more after the subsidy here than in Craven or Carteret County?",
         f"Because the tax credit is based on the second-cheapest Silver plan in your county, and it is designed to make that benchmark plan cost the same share of your income wherever you live. A 45-year-old earning $30,000 pays about {net(CLS, 's45_30k')} a month for the benchmark both here and in Craven County. In Craven the benchmark is Blue Care Silver Standard; in {NAME} it is Ambetter's Clear Silver, which costs {full45(CLS)} at full price against {full45(BC_SS)} for Blue Care Silver Standard. Choosing Blue Cross here means paying that full price difference yourself, which is why Blue Care Silver Standard costs that same person {net(BC_SS, 's45_30k')} a month."),
        ("What are the standardized \"Easy Pricing\" plans?",
         f"Plans whose deductibles, copays and coinsurance are set by the federal government, so a standardized plan at a given metal level has the same benefits whichever insurer sells it. HealthCare.gov labels them Easy Pricing. In {NAME} they are Ambetter's Signature plans, Blue Cross's Standard plans (Gold Standard A for Gold), UnitedHealthcare's Standard plans and Oscar's Classic Standard plans. Because the benefits match, the comparison comes down to price, network and extras such as children's dental: at age 45 the standardized Silver ranges from {m(STD[('Ambetter', 'silver')])} (Ambetter) to {m(STD[('Blue Advantage', 'silver')])} (Blue Advantage)."),
        ("Do I need a referral to see a specialist?",
         "No. None of the plans we checked requires a referral from a primary care doctor to see a specialist, including the HMOs."),
        ("Which plans work outside North Carolina?",
         f"Only Blue Advantage, Blue Cross's PPO, gives you in-network access to doctors nationwide, through the BlueCard network. It costs about 5% more than the same Blue Care design: {m(min(ba_add45))} to {m(max(ba_add45))} a month at age 45, {m(min(ba_add60))} to {m(max(ba_add60))} at 60. The Ambetter, Blue Care, UnitedHealthcare and Oscar plans are HMOs built around North Carolina providers, and Blue Value's out-of-network benefit comes with a $35,000 deductible. Every plan covers emergency care anywhere."),
        (f"Is there a catastrophic plan in {FULL}?",
         f"No. For 2027 no catastrophic plan is offered in {FULL}, even for people under 30. The Bronze plans are the lowest-premium options, starting at {m(P[SEB]['p27'])} a month at age 27 before any subsidy."),
        ("Do the plans include dental and vision?",
         f"Children's dental is included in every Blue Cross and UnitedHealthcare plan, but not in Ambetter or Oscar plans; families choosing those should add a stand-alone dental plan for the children. {DENT_VALUE} Adult dental and vision come only with the versions that say so: Ambetter's \"+ Vision + Adult Dental\" plans (about {m(a_lo)} to {m(a_hi)} a month more at age 45), UnitedHealthcare's \"+\" plans (about {m(u_hi)} more) and two Oscar plans \"with Adult Dental & Vision\" (about {m(o_hi)} more)."),
        ("What happens if my income is under about $22,000?",
         "North Carolina expanded Medicaid in December 2023. A single adult with income under roughly 138% of the federal poverty level (about $22,000 for one person, $29,900 for a couple, $45,500 for a family of four in 2027) is directed to NC Medicaid rather than receiving a Marketplace subsidy. The Marketplace application checks this automatically."),
        ("When can I enroll?",
         "Open Enrollment for 2027 coverage runs November 1, 2026 through January 15, 2027. Enroll by December 15 for coverage starting January 1. Outside Open Enrollment you need a qualifying event, such as losing other coverage, moving, marriage or a new baby."),
    ]

    # ---- tables ----
    def yes(b, y="In network", n="<strong>Not in network</strong>"):
        return y if b else n

    net_rows = "".join(
        f'<tr><td><strong>{n}</strong><br>{NET_TYPE[n]}, {len(by_net[n])} plans</td>'
        f'<td class="num">{m(cheapest(n, "bronze"))}</td><td class="num">{m(cheapest(n, "silver"))}</td><td class="num">{m(cheapest(n, "gold"))}</td>'
        f'<td>{yes(nhrmc[n])}</td><td>{"Included" if child_dental[n] else "Not included"}</td><td>{quality(n)}</td></tr>'
        for n in NETWORKS)

    std_label = {"Ambetter": "Ambetter Signature", "Blue Value": "Blue Value (Blue Cross)", "Blue Care": "Blue Care (Blue Cross)",
                 "UnitedHealthcare": "UnitedHealthcare Standard", "Oscar": "Oscar Classic Standard", "Blue Advantage": "Blue Advantage (Blue Cross)"}
    best_attr = {n: (' class="best"' if n == "Ambetter" else "") for n in NETWORKS}
    std_rows = "".join(
        f'<tr{best_attr[n]}><td>{std_label[n]}</td>' + "".join(f'<td class="num">{m(STD[(n, mt)])}</td>' for mt in METALS) + "</tr>"
        for n in sorted(NETWORKS, key=lambda n: STD[(n, "silver")]))

    assert csr(SGS, "csr87") == csr(BC_SS, "csr87") and csr(SGS, "csr73") == csr(BC_SS, "csr73")
    csr_note = ("Cells marked CSR include cost-sharing reductions, which also lower the deductible and out-of-pocket maximum. "
                "At $30,000 for one person, the deductible and out-of-pocket maximum drop to {} and {} on the standardized Silver plans (Ambetter Signature Silver and Blue Care Silver Standard) and to {} and {} on Streamlined Silver; "
                "at $35,000 they drop to {} and {}, and to {} and {} on Streamlined Silver.").format(
        *csr(SGS, "csr87"), *csr(STS, "csr87"), *csr(SGS, "csr73"), *csr(STS, "csr73"))
    sub_rows = "".join([
        f'<tr><td>Single, 45, $30,000</td><td class="num">{net(SEB,"s45_30k")}</td><td class="num">{net(STS,"s45_30k")} (CSR)</td><td class="num">{net(SGS,"s45_30k")} (CSR)</td><td class="num">{net(SGG,"s45_30k")}</td><td class="num">{net(BC_SS,"s45_30k")} (CSR)</td></tr>',
        f'<tr><td>Single, 45, $45,000</td><td class="num">{net(SEB,"s45_45k")}</td><td class="num">{net(STS,"s45_45k")}</td><td class="num">{net(SGS,"s45_45k")}</td><td class="num">{net(SGG,"s45_45k")}</td><td class="num">{net(BC_SS,"s45_45k")}</td></tr>',
        f'<tr><td>Single, 45, $100,000</td><td class="num">{net(SEB,"s45_100k")}</td><td class="num">{net(STS,"s45_100k")}</td><td class="num">{net(SGS,"s45_100k")}</td><td class="num">{net(SGG,"s45_100k")}</td><td class="num">{net(BC_SS,"s45_100k")}</td></tr>',
        f'<tr><td>Single, 27, $35,000</td><td class="num">{net(SEB,"a27_35k")}</td><td class="num">{net(STS,"a27_35k")} (CSR)</td><td class="num">{net(SGS,"a27_35k")} (CSR)</td><td class="num">{net(SGG,"a27_35k")}</td><td class="num">{net(BC_SS,"a27_35k")} (CSR)</td></tr>',
        f'<tr><td>Couple, 62 and 60, $58,000</td><td class="num">{net(SEB,"c62_60_58k")}</td><td class="num">{net(STS,"c62_60_58k")}</td><td class="num">{net(SGS,"c62_60_58k")}</td><td class="num">{net(SGG,"c62_60_58k")}</td><td class="num">{net(BC_SS,"c62_60_58k")}</td></tr>',
        f'<tr><td>Family of four (45, 43, 12, 9), $90,000</td><td class="num">{net(SEB,"fam90k")}</td><td class="num">{net(STS,"fam90k")}</td><td class="num">{net(SGS,"fam90k")}</td><td class="num">{net(SGG,"fam90k")}</td><td class="num">{net(BC_SS,"fam90k")}</td></tr>',
    ])

    plans_html = (
        insurer_section("AMB", f"Ambetter ({len(by_net['Ambetter'])} plans, HMO)",
                        f"Ambetter of North Carolina. Extras: {AMB_EXTRAS}. New Hanover Regional in network; children's dental not included; HealthCare.gov quality rating {quality('Ambetter')}. Where two prices are shown, the second is the same plan with adult dental and vision added (\"+ Vision + Adult Dental\").")
        + insurer_section("BCBS", "Blue Cross NC (30 plans: Blue Value POS, Blue Care HMO, Blue Advantage PPO)",
                          f"The same 10 designs and benefits Blue Cross sells elsewhere in eastern North Carolina, each sold here in three networks with identical benefits. Prices are Blue Value / Blue Care / Blue Advantage. New Hanover Regional in network on all three; children's dental included; quality rating {quality('Blue Value')} for Blue Value and Blue Advantage, Blue Care {quality('Blue Care').lower()}.")
        + insurer_section("UHC", f"UnitedHealthcare ({len(by_net['UnitedHealthcare'])} plans, HMO)",
                          f"$0 insulin on every plan, and $0 virtual urgent care on most. New Hanover Regional in network; children's dental included; quality rating {quality('UnitedHealthcare')}. Where two prices are shown, the second is the \"+\" version with adult dental and vision.")
        + insurer_section("OSC", f"Oscar ({len(by_net['Oscar'])} plans, HMO)",
                          f"Extras: {OSC_EXTRAS}. <strong>New Hanover Regional Medical Center showed as out of network on every Oscar plan</strong> when we checked. Children's dental not included; quality rating {quality('Oscar')}. Where two prices are shown, the second is the version with adult dental and vision.")
    )

    zl = [f'<a href="/counties/{z.lower()}/">{z}</a>' for z in ZONE15_OTHERS]
    zone_links = ", ".join(zl[:-1]) + " and " + zl[-1]

    body = f"""
<h1>Health Insurance in {FULL}, NC for 2027: All 75 Plans Explained</h1>
{nh_byline("{READING}")}

<p class="lede">If you buy your own health insurance in {FULL} (Wilmington, Carolina Beach, Kure Beach, Wrightsville Beach, Ogden and Castle Hayne) you have four insurers and 75 Marketplace plans to choose from for 2027: Ambetter, Blue Cross and Blue Shield of North Carolina, UnitedHealthcare and Oscar. This guide uses the official HealthCare.gov plan data for {FULL} to explain what the plans cost, how the insurers and their networks differ, and which plan fits which situation.</p>

<nav class="toc" aria-label="In this guide">
<strong>In this guide</strong>
<ol>
<li><a href="#market">The market at a glance</a> and <a href="#subsidies">what subsidies do</a></li>
<li><a href="#network">Decision 1: which insurer and network</a></li>
<li><a href="#metal">Decision 2: how much coverage</a></li>
<li><a href="#drugs">Decision 3: how prescriptions are priced</a></li>
<li><a href="#plans">The {n_designs} plan designs</a> (click a plan to expand)</li>
<li><a href="#situations">If you are&hellip; look at&hellip;</a></li>
<li><a href="#faq">Questions</a></li>
</ol>
</nav>

<div class="takeaways">
<h2>Key takeaways</h2>
<ul>
<li><strong>75 plans, four insurers, {n_designs} designs.</strong> Ambetter sells {len(by_net['Ambetter'])} plans, Blue Cross NC 30 (10 designs in three networks), UnitedHealthcare {len(by_net['UnitedHealthcare'])} and Oscar {len(by_net['Oscar'])}. Many are one design sold twice, with and without adult dental and vision.</li>
<li><strong>Same benefits, very different prices.</strong> All four insurers sell the federally standardized Bronze, Silver and Gold designs (marked Easy Pricing on HealthCare.gov). At age 45 Ambetter's standardized Silver costs {m(STD[('Ambetter', 'silver')])} a month; the identical design costs {m(STD[('Blue Value', 'silver')])} to {m(STD[('Blue Advantage', 'silver')])} from the other insurers.</li>
<li><strong>Your subsidy is set by Ambetter's prices.</strong> The benchmark plan is Ambetter's Clear Silver, so subsidized households pay little for Ambetter plans and a lot for Blue Cross: a 45-year-old earning $30,000 pays {net(BC_SS, 's45_30k')} a month for Blue Care Silver Standard here, against about $154 in Craven County, where Blue Cross is the only insurer.</li>
<li><strong>Check the hospital first.</strong> {HOSPITAL} was in network on every Ambetter, Blue Cross and UnitedHealthcare plan and on no Oscar plan when we checked HealthCare.gov on {CHECKED_H}.</li>
<li><strong>Full-price premiums for a 45-year-old</strong> run {metal_range("bronze")} for Bronze, {metal_range("silver")} for Silver and {metal_range("gold")} for Gold. A 60-year-old pays about 1.9 times that; a 30-year-old about 0.8 times.</li>
<li><strong>No referrals and no catastrophic plan.</strong> None of the plans we checked requires a referral to see a specialist, and no catastrophic plan is offered in {NAME} for 2027.</li>
</ul>
</div>

<h2 id="market">The {FULL} market at a glance</h2>
<p>{NAME} has four Marketplace insurers, but the number of plans overstates how hard the choice is. The 75 plans are {n_designs} designs, many of them sold more than once, and they come in six networks. That makes three decisions, in order: <a href="#network">which insurer and network</a> (start with your doctors and hospital), <a href="#metal">how much coverage</a>, and <a href="#drugs">how your prescriptions are priced</a>. The designs are then <a href="#plans">described insurer by insurer</a>, and a <a href="#situations">situations table</a> maps common {NAME} households to the plans worth a close look.</p>

<div class="table-wrap">
<table class="data">
<caption>The six networks in {FULL}, 2027. Cheapest full-price monthly premium at age 45 at each metal level, no subsidy. Hospital status from HealthCare.gov's doctor and hospital lookup, {CHECKED_H}. Quality rating is HealthCare.gov's star rating. Source: HealthCare.gov plan preview.</caption>
<thead><tr><th>Network</th><th class="num">Cheapest<br>Bronze</th><th class="num">Cheapest<br>Silver</th><th class="num">Cheapest<br>Gold</th><th>New Hanover Regional</th><th>Children's dental</th><th>Quality rating</th></tr></thead>
<tbody>{net_rows}</tbody>
</table>
</div>

<p>The clearest way to compare the insurers is through the standardized plans, whose deductibles, copays and out-of-pocket maximums are set by the federal government. Every network sells one at each metal level, so the only differences are the network, the price and extras such as children's dental:</p>

<div class="table-wrap">
<table class="data">
<caption>Standardized ("Easy Pricing") plans in {FULL}: identical benefits, monthly premium at age 45, full price, 2027. Bronze: $7,500 deductible, $12,000 out-of-pocket max. Silver: $6,400 deductible, $10,300 max. Gold: $2,500 deductible, $8,600 max. Multiply by about 0.79 for a 30-year-old and 1.88 for a 60-year-old. Source: HealthCare.gov plan preview.</caption>
<thead><tr><th>Insurer and network</th><th class="num">Bronze</th><th class="num">Silver</th><th class="num">Gold</th></tr></thead>
<tbody>{std_rows}</tbody>
</table>
</div>

<h3 id="subsidies">What subsidies do to those numbers</h3>
<p>The premium tax credit is a fixed dollar amount based on your income and the price of the second-cheapest Silver plan, which in {NAME} is Ambetter's Clear Silver with $0 Insulin Options ({full45(CLS)} a month at age 45). You can spend the credit on any plan. Because the enhanced credits of 2021&ndash;2025 have expired, the credit stops entirely at 400% of the federal poverty level ($63,840 for one person, $86,560 for a couple, $132,000 for a family of four), and the Marketplace now recovers any overpaid credit in full at tax time, so your income estimate matters. Here is what five plans cost real {NAME} households after the credit:</p>

<div class="table-wrap">
<table class="data">
<caption>Net monthly premium after the premium tax credit, {FULL}, 2027. Ambetter's Signature Silver and Blue Care Silver Standard have identical benefits. "CSR": cost-sharing reductions apply (see below). Source: HealthCare.gov plan preview.</caption>
<thead><tr><th>Household and income</th><th class="num">Ambetter<br>Signature<br>Expanded Bronze</th><th class="num">Ambetter<br>Streamlined<br>Silver</th><th class="num">Ambetter<br>Signature<br>Silver</th><th class="num">Ambetter<br>Signature<br>Gold</th><th class="num">Blue Care<br>Silver<br>Standard</th></tr></thead>
<tbody>{sub_rows}</tbody>
</table>
</div>

<p>{csr_note}</p>

<p>Three things to notice. First, the credit is the same dollar amount whichever plan you choose, so the full-price gaps between insurers pass straight through to what you pay: the two standardized Silver plans in the table have identical benefits, yet at $30,000 one costs {net(SGS, 's45_30k')} a month and the other {net(BC_SS, 's45_30k')}. Second, no plan in the table is free. At age 45 the cheapest Bronze costs only {dm(P[CLS]['p45'], P[SEB]['p45'])} a month less than the benchmark, so the credit does not cover it and a 45-year-old earning $30,000 still pays {net(SEB, 's45_30k')}; in Craven County, where the gap is about $300, the same person gets every Bronze plan for $0. Third, families should mind children's dental. Ambetter and Oscar plans leave it out, and because the benchmark is an Ambetter plan, the family's credit is a little larger to help pay for a stand-alone children's dental plan ({DENT_COST}); Blue Cross and UnitedHealthcare plans already include it, a difference worth about $250 to $700 a year per child. And as everywhere in North Carolina, a single adult under about $22,000 or a couple under about $29,900 is sent to NC Medicaid instead of receiving a Marketplace credit; the application sorts this out.</p>

<h2 id="network">Decision 1: Which insurer and network?</h2>
<p>Where Blue Cross is the only insurer, this decision is between two versions of the same plan. In {NAME} it is the decision that matters most, because the networks really differ and the prices differ far more than the benefits do. Start with the doctors and the hospital you want to keep.</p>
<ul>
<li><strong>Ambetter</strong> ({len(by_net['Ambetter'])} plans, HMO) has the lowest prices at every metal level, and New Hanover Regional is in network. As an HMO it covers out-of-network care only in emergencies, but no referrals are needed for specialists. Children's dental is not included. Members get a free YMCA membership at participating North Carolina Ys, the Ambetter Perks discount program and up to $500 in My Health Pays rewards for healthy activities.</li>
<li><strong>Blue Cross NC</strong> (30 plans) sells the same 10 designs it offers elsewhere in eastern North Carolina, each in three networks. <strong>Blue Value</strong> is a narrower statewide network, sold as a POS plan and about {bv_pct}% cheaper than Blue Care ({m(min(bv_save))} to {m(max(bv_save))} a month at age 45); its out-of-network benefit comes with a $35,000 deductible, so treat it as in-network only. <strong>Blue Care</strong> is the statewide HMO. <strong>Blue Advantage</strong> is a PPO that adds the national BlueCard network for about 5% more than Blue Care ({m(min(ba_add45))} to {m(max(ba_add45))} a month at 45, {m(min(ba_add60))} to {m(max(ba_add60))} at 60). All three include children's dental.</li>
<li><strong>UnitedHealthcare</strong> ({len(by_net['UnitedHealthcare'])} plans, HMO) includes $0 insulin on every plan, $0 virtual urgent care on most, and children's dental, and New Hanover Regional is in network. Its Bronze and Silver prices are close to Blue Care's; its Gold plans are the most expensive in the county.</li>
<li><strong>Oscar</strong> ({len(by_net['Oscar'])} plans, HMO) is priced close to Blue Care and includes $0 virtual urgent care on every plan and a Care Team in the Oscar app, but does not include children's dental, has HealthCare.gov's lowest quality rating in the county ({quality('Oscar')}), and <strong>did not have New Hanover Regional in network on any plan</strong> when we checked.</li>
</ul>
<p><strong>Choose Ambetter if</strong> your doctors are in its network: the same benefits cost less there than anywhere else in the county. <strong>Choose Blue Advantage if</strong> you need in-network care outside North Carolina (months away each year, a student at an out-of-state college, frequent travel); it is the only nationwide network sold here. <strong>Look at Blue Value if</strong> you want Blue Cross at a lower price and your doctors are in its narrower network. <strong>If you use insulin</strong>, weigh UnitedHealthcare's $0 insulin against its higher premiums before choosing it; Decision 3 has the numbers.</p>
<p>Before enrolling, check each doctor and your hospital in the plan's own directory, or add them in <a href="{APP}" target="_blank" rel="noopener">our Covanu tool</a>, which checks them against every plan's network. Blue Cross directories: <a href="{NET_HMO}" target="_blank" rel="noopener">Blue Care</a> and <a href="{NET_PPO}" target="_blank" rel="noopener">Blue Advantage</a>. In {FULL}, {HOSPITALS}; check the one you would use.</p>

<h2 id="metal">Decision 2: How much coverage do you expect to use?</h2>
<p>Bronze, Silver and Gold describe how costs are split between you and the plan: roughly 60%, 70% and 80% paid by the plan for an average person. In {NAME} the practical differences are these:</p>
<ul>
<li><strong>Bronze</strong> ({count_metal("bronze")} plans, {metal_range("bronze")} at 45): deductibles up to $11,750, so you pay for most care yourself until something serious happens, although three Bronze designs have no medical deductible (copays or coinsurance apply from the first dollar instead). All {count_metal("bronze")} Bronze plans are <strong>HSA-eligible for 2027</strong> under the 2025 federal tax law, which lets you set aside up to $4,500 (single) or $9,000 (family) pre-tax, plus $1,000 if you are 55 or older.</li>
<li><strong>Silver</strong> ({count_metal("silver")} plans, {metal_range("silver")}): the plans to look at first if you qualify for a subsidy, because incomes under about $39,900 (single) or $82,500 (family of four) unlock <strong>cost-sharing reductions</strong> that only apply to Silver plans. At $30,000 for one person the standardized Silver's deductible drops from $6,400 to $800 and its out-of-pocket maximum from $10,300 to $3,600. Without a cost-sharing reduction, Silver is a middle ground that often loses to either Bronze or Gold on total cost.</li>
<li><strong>Gold</strong> ({count_metal("gold")} plans, {metal_range("gold")}): $0 to $2,500 deductibles and flat copays for most care. Gold is unusually affordable here if you buy it from Ambetter: Signature Gold costs {m(gold_gap)} a month more than the cheapest Bronze at age 45, and less than every Bronze plan from Blue Care, Blue Advantage, UnitedHealthcare and Oscar. It is worth a look if you take brand-name or specialty drugs, see specialists regularly, or are planning surgery or a pregnancy.</li>
</ul>

<h2 id="drugs">Decision 3: How are your prescriptions priced?</h2>
<p>Each insurer has its own drug list, so check every prescription against the plans you are considering; our Covanu tool checks a list of medications against all 75 plans at once. (For Blue Cross, the finding from our other county guides holds here: its two drug lists covered the same 48 common drugs.) Beyond coverage, the plan design decides what you pay:</p>
<ul>
<li>On the <strong>standardized plans</strong> (Ambetter Signature, Blue Cross Standard and Gold Standard A, UnitedHealthcare Standard, Oscar Classic Standard), preferred brand drugs are flat copays with no deductible on Silver ($40) and Gold ($30), and specialty drugs are $350 after the deductible on Silver or $250 with no deductible on Gold.</li>
<li>Most <strong>other designs</strong>, from every insurer, charge 25% to 50% coinsurance for non-preferred and specialty drugs, usually after a deductible, and several put brand drugs behind the deductible or a separate drug deductible. Someone on an expensive brand drug can pay thousands before the plan contributes.</li>
<li><strong>Insulin and condition-specific plans.</strong> UnitedHealthcare includes $0 insulin on every plan; Ambetter's Clear Silver has $0 insulin options, its Enhanced CHF Heart Care Silver has $0 options for certain heart-failure drugs, and its Enhanced Asthma/COPD Care Silver makes listed asthma and COPD drugs and pulmonologist visits free; Oscar's Simple Diabetes plans, at the Bronze and Silver levels, cover endocrinologist visits and diabetic eye and foot exams in full and cap insulin at $100 for a 30-day supply. In the official coverage example for a year of managing type 2 diabetes, the estimated cost to you on UnitedHealthcare's standardized Bronze is {coverage_example(UHC_BS, 'diabetes')}, against {coverage_example(SEB, 'diabetes')} for Ambetter's and {coverage_example(OSC_BS, 'diabetes')} for Oscar's version of the same design. The example prices insulin at the plan's own rate, before any manufacturer program.</li>
<li><strong>What insulin costs without a $0 benefit.</strong> {INSULIN_COST} Here UnitedHealthcare's standardized Silver costs {dm(STD[('UnitedHealthcare', 'silver')], STD[('Ambetter', 'silver')])} a month more than Ambetter's identical Signature Silver at age 45, {m(12 * (round(STD[('UnitedHealthcare', 'silver')]) - round(STD[('Ambetter', 'silver')])))} a year, so for most insulin users a cheaper plan plus a maker's $35 program costs less over the year. Ambetter's Clear Silver is the benchmark Silver your credit is based on, so its $0 insulin options carry no extra premium; check that your insulin is on its $0 list, and weigh its $7,900 deductible ({csr(CLS,"csr87")[0]} with cost-sharing reductions at $30,000, single).</li>
</ul>
<p>The arithmetic for brand and specialty drugs is in <a href="/questions/bronze-vs-silver-medications/">Bronze vs. Silver when you take medications</a>. The short version: one brand-name prescription is often enough to make a standardized Silver cheaper than Bronze over a year, and a specialty drug makes a standardized Gold the cheapest plan on the shelf.</p>

<h2 id="plans">The {n_designs} plan designs, insurer by insurer</h2>
<p>Prices are full-price monthly premiums for a 45-year-old in {FULL}. Click a plan to expand its details. Benefit amounts are in-network, individual coverage, no cost-sharing reduction unless noted.</p>
{plans_html}

<h2 id="situations">If you are&hellip; look at&hellip;</h2>
<div class="table-wrap">
<table class="data">
<caption>Starting points, not recommendations. Prices are monthly in {FULL} after any subsidy. Confirm your doctors and drugs and run your own numbers before deciding.</caption>
<thead><tr><th>Situation</th><th>Start with</th><th>Why</th></tr></thead>
<tbody>
<tr><td>Healthy 30-year-old, no prescriptions, $100,000 income</td><td>Ambetter Signature Expanded Bronze ({net(SEB,"s30_100k")}) or Everyday Bronze ({net(EVB,"s30_100k")})</td><td>No subsidy at this income; the two lowest premiums in the county, both HSA-eligible. Blue Value Bronze HSA Eligible Plus ({net(BV_HSA,"s30_100k")}) caps a bad year at $8,700.</td></tr>
<tr><td>Self-employed, family of four, $90,000</td><td>Ambetter Signature Expanded Bronze ({net(SEB,"fam90k")}) if everyone is healthy; Ambetter Signature Silver ({net(SGS,"fam90k")}) if anyone takes a brand drug</td><td>Add a stand-alone dental plan for the children ({DENT_COST}). Blue Value Bronze Basic ({net(BV_BB,"fam90k")}) includes children's dental.</td></tr>
<tr><td>Single, 45, $30,000, sees a doctor a few times a year</td><td>Ambetter Streamlined Silver ({net(STS,"s45_30k")}) or Signature Silver ({net(SGS,"s45_30k")})</td><td>Cost-sharing reductions cut the deductible to {csr(STS,"csr87")[0]} or {csr(SGS,"csr87")[0]}. The cheapest Bronze ({net(SEB,"s45_30k")}) keeps a $7,500 deductible.</td></tr>
<tr><td>Early retirees, 62 and 60, $58,000 investment and part-time income</td><td>Ambetter Signature Expanded Bronze ({net(SEB,"c62_60_58k")}) if you can self-insure the deductible; Streamlined Silver ({net(STS,"c62_60_58k")}) or Signature Gold ({net(SGG,"c62_60_58k")}) if you expect regular care</td><td>Keep income under $86,560 or the subsidy disappears. See <a href="/questions/retiring-before-65-north-carolina/">Retiring before 65 in NC</a>.</td></tr>
<tr><td>Spends January through March in Florida, or has a student at an out-of-state college</td><td>Blue Advantage version of whichever Blue Cross design fits</td><td>The only nationwide network in the county; the others are built around North Carolina providers. See <a href="/questions/blue-care-vs-blue-advantage/">Blue Care vs. Blue Advantage</a>.</td></tr>
<tr><td>Wants to keep doctors at New Hanover Regional</td><td>Ambetter, Blue Cross or UnitedHealthcare</td><td>The hospital was out of network on every Oscar plan. Check each doctor too, not just the hospital.</td></tr>
<tr><td>Takes Eliquis, Jardiance or another preferred brand drug</td><td>Ambetter Signature Silver or Signature Gold</td><td>$40 / $30 brand copays with no deductible, for less than the same designs cost from the other insurers. Confirm the drug is on Ambetter's list.</td></tr>
<tr><td>Uses insulin</td><td>Ambetter Clear Silver, or UnitedHealthcare plans if you want its network</td><td>Clear Silver's $0 insulin options come without a premium penalty. Without a $0 benefit, the makers' $35-a-month programs cap most insulins, so compare the whole year's cost, not just the insulin.</td></tr>
<tr><td>Takes a specialty drug (Dupixent, Skyrizi, Enbrel, Rinvoq)</td><td>Ambetter Signature Gold</td><td>$250 specialty copay with no deductible and an $8,600 maximum, for less than most Bronze plans elsewhere. Confirm the drug is on the list.</td></tr>
<tr><td>Planning surgery or a pregnancy next year</td><td>Ambetter Signature Gold ($8,600 max) or Clear Silver ($7,900 max; {csr(CLS,"csr87")[0]} with cost-sharing reductions at $30,000, single)</td><td>You will reach the deductible anyway; buy the plan with the lowest ceiling.</td></tr>
<tr><td>Income near $22,000 (single) or $45,500 (family of four)</td><td>Apply for Marketplace coverage and let the application check Medicaid</td><td>NC Medicaid may cover you at no premium; the Marketplace cannot subsidize you below the line.</td></tr>
</tbody>
</table>
</div>

<div class="callout caution">
<p><strong>About the prices on this page.</strong> Premiums and benefits come from HealthCare.gov's plan preview for {FULL} (ZIP 28401, FIPS 37129), plan year 2027, non-tobacco users, checked {CHECKED_H}. Prices at age 45, the after-credit prices for the single households and the family, and the cost-sharing reductions are HealthCare.gov's own figures; prices at ages 27, 30 and 60 and some couple prices are calculated from them with the federal age-rating curve North Carolina uses, which matched HealthCare.gov to within a few cents wherever we compared. Your own price depends on each household member's age, your income estimate and whether anyone uses tobacco. Confirm benefits in the plan's Summary of Benefits and Coverage before you enroll.</p>
</div>

<p class="related"><strong>Same rating area:</strong> {zone_links} counties share {NAME}'s rating area (15), so a plan sold in both costs the same, but not every insurer sells in every county. <strong>Other county guides:</strong> <a href="/counties/craven/">Craven</a> and <a href="/counties/carteret/">Carteret</a>, where Blue Cross is the only insurer, and <a href="/counties/">all county guides</a>.</p>

{cta(f"See every {FULL} plan with your subsidy applied")}

{author_box()}

{sources([
    f'HealthCare.gov plan preview, {FULL} (ZIP 28401, FIPS 37129), plan year 2027, retrieved {CHECKED_H}: premiums, tax credits, benefits, cost-sharing reductions and coverage examples.',
    f'HealthCare.gov doctor and hospital lookup (in the plan preview), {HOSPITAL}, all 75 plans, {CHECKED_H}.',
    '<a href="https://aspe.hhs.gov/topics/poverty-economic-mobility/poverty-guidelines" target="_blank" rel="noopener">HHS 2026 Poverty Guidelines</a> (used for 2027 Marketplace eligibility).',
    '<a href="https://kff.org/affordable-care-act/9-things-to-watch-for-the-2027-aca-open-enrollment-period/" target="_blank" rel="noopener">KFF, 9 Things to Watch for the 2027 ACA Open Enrollment Period</a> (expiration of enhanced credits, repayment caps, catastrophic plan eligibility).',
    'IRS Rev. Proc. 2026-24 (2027 HSA limits) and IRS Notice 2026-5 (Bronze and catastrophic Marketplace plans treated as HSA-eligible high-deductible plans).',
    f'<a href="{SCOTTS_HILL}" target="_blank" rel="noopener">Novant Health, Scotts Hill Medical Center</a>.',
    'Blue Cross NC provider directories: <a href="' + NET_HMO + '" target="_blank" rel="noopener">Blue Care</a>, <a href="' + NET_PPO + '" target="_blank" rel="noopener">Blue Advantage</a>.',
])}
"""
    words = len(re.sub(r"<[^>]+>", " ", body).split()) + sum(len((q + " " + a).split()) for q, a in FAQ)
    reading = f"{max(1, round(words / 335))} minute read"  # same rate as the other county guides (about 4,000 words = 12 minutes)
    body = body.replace("{READING}", reading)

    saved = fbsite.UPDATED
    fbsite.UPDATED = CHECKED  # article dates in the structured data
    try:
        page(PATH, TITLE, DESC, "/counties/", CRUMBS, body, faq=FAQ, reading=reading)
    finally:
        fbsite.UPDATED = saved
    return words


if __name__ == "__main__":
    print("words", build())
