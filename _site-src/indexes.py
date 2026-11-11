from fbsite import *
from counties import COUNTIES, OTHER_GUIDES, ZONES, LIVE_ZONES

ALL_GUIDES = COUNTIES + OTHER_GUIDES

GUIDES = [
    ("/questions/bronze-vs-silver-medications/", "Bronze vs. Silver when you take medications",
     "Premium is often the wrong number. Year-long cost comparisons for generic, brand-name and specialty drug users on real 2027 Blue Cross NC plans, including the free (or nearly free) Bronze vs. $154 Silver question for subsidized households."),
    ("/questions/self-employed-north-carolina-2027/", "Health insurance for the self-employed in NC (2027)",
     "How the subsidy treats business income, the 400% cliff in dollars, and the four levers (SEP-IRA, HSA, timing, the premium deduction) that keep you under the line."),
    ("/questions/retiring-before-65-north-carolina/", "Retiring before 65 in NC: bridging to Medicare",
     "COBRA or the Marketplace, what a 64-year-old really pays, which retirement income counts, a cliff that can cost a couple $22,000 to $46,000 a year, and the hand-off to Medicare."),
    ("/questions/blue-care-vs-blue-advantage/", "Blue Care vs. Blue Advantage: is the nationwide PPO worth it?",
     "Same benefits, different network. What the PPO actually buys (college students, families with second homes, frequent travelers), what it costs where you live, the cheaper Blue Home, Blue Local and Blue Value networks, and how to get a PPO in the Triangle."),
]


def cards(items):
    out = ['<div class="card-grid">']
    for href, title, desc in items:
        out.append(f'<div class="card"><h3><a href="{href}">{title}</a></h3><p>{desc}</p><a class="more" href="{href}">Read the answer &rarr;</a></div>')
    out.append("</div>")
    return "\n".join(out)


def county_cards():
    return nc_map()


def simple_page(path, title, desc, current, crumbs, body, ld_extra=None, og="website"):
    ld = [breadcrumb_ld(crumbs)] + (ld_extra or [])
    doc = head(title, desc, path, ld, og) + nav(current)
    doc += '    <div class="container">\n' + breadcrumb(crumbs) + '<article class="article">\n' + body + '\n</article>\n    </div>\n' + footer()
    write(path, doc)


# ---------- /questions/ ----------
body = f"""
<h1>Common questions about North Carolina health insurance</h1>
{byline()}
<p class="lede">Most plan-comparison tools answer "which plan is cheapest?" These answer the question that actually decides it: "cheapest for someone in my situation?" Each one is built on the official 2027 HealthCare.gov plan data for North Carolina and is updated every plan year.</p>
{cards(GUIDES)}
<h2>Plans in your county</h2>
<p>Plans, carriers and prices differ by county. The county guides describe every Marketplace plan sold where you live.</p>
<p><a class="more" href="/counties/">See the county guides &rarr;</a></p>
{cta()}
"""
simple_page("/questions/", "Common Questions: NC Health Insurance Answered (2027) | Fact-Based Healthcare Decisions",
            "Plain-English answers to the questions that decide which ACA Marketplace plan is right for you in North Carolina: medications, self-employment income, early retirement, built on HealthCare.gov data.",
            "/questions/", [("/", "Home"), (None, "Common Questions")], body,
            [{"@context": "https://schema.org", "@type": "CollectionPage", "name": "Common questions about North Carolina health insurance", "url": BASE + "/questions/",
              "hasPart": [{"@type": "Article", "headline": t, "url": BASE + h} for h, t, _ in GUIDES]}])

# ---------- /counties/ ----------
body = f"""
<h1>North Carolina county health insurance guides (2027)</h1>
{byline()}
<p class="lede">Marketplace plans are sold county by county, and insurers price them by CMS rating area, 16 of them in North Carolina. Click your county. Each guide lists every plan sold there, with that county's prices by age and income, the network choices, and which plan fits which situation. In much of eastern North Carolina Blue Cross NC is the only Marketplace insurer; around Charlotte, the Triad, the Triangle, Asheville and Wilmington up to five insurers compete, and each guide shows which of the area's hospitals every network includes.</p>
{county_cards()}
<p>Every North Carolina county now has a guide. Our Covanu tool uses the same data to compare the plans with your own subsidy, medications and doctors, and we are glad to walk through your county's plans on a call.</p>
{cta("See every plan in your county")}
"""
simple_page("/counties/", "North Carolina County Health Insurance Guides (2027) | Fact-Based Healthcare Decisions",
            "County-by-county reviews of every 2027 ACA Marketplace plan in all 100 North Carolina counties, with prices by age and income, networks, hospitals and plan-by-plan explanations.",
            "/counties/", [("/", "Home"), (None, "County Guides")], body,
            [{"@context": "https://schema.org", "@type": "CollectionPage", "name": "North Carolina county health insurance guides", "url": BASE + "/counties/",
              "hasPart": [{"@type": "Article", "headline": c["name"] + " County, NC health insurance 2027", "url": BASE + "/counties/" + c["slug"] + "/"} for c in ALL_GUIDES]}])

# ---------- /about/ ----------
body = f"""
<h1>How we work</h1>
<p class="lede">Fact-Based Healthcare Decisions is an independent, licensed North Carolina health insurance agency. We use data and software to compare every plan available to you, then meet with you to finish the choice and enroll. Our help is free; insurers pay our commissions, and they pay the same whichever plan you choose.</p>

<h2>We recommend ACA-compliant plans only</h2>
<h3>On-Exchange plans</h3>
<p>Available through the Marketplace at HealthCare.gov. We check whether you qualify for subsidies that lower your monthly premium and your costs when you get care.</p>
<h3>Off-Exchange plans</h3>
<p>Sold directly by insurers and available only through licensed health insurance agents. Some of the best options, such as select Blue Cross NC PPO plans, are only available this way.</p>
<div class="callout caution">
<p><strong>What we don't recommend.</strong> Some agents sell other kinds of coverage, such as fixed indemnity plans and health care sharing ministries ("health share" plans). These are not ACA-compliant. They often leave out essential health benefits like prescription drugs, maternity care and mental health care, and they have no out-of-pocket maximum. That maximum is what caps your total costs for the year if you face a serious illness or accident.</p>
</div>

<h2>How we are different</h2>
<ul class="features-list">
<li><strong>AI assistance</strong> &mdash; Harriette, the AI assistant in our <a href="{APP}" target="_blank" rel="noopener">Covanu</a> ACA Selector, guides you through a short questionnaire about your goals and care needs, then selects the plans from the leading carriers in your area that best fit them.</li>
<li><strong>Mobile-friendly data collection</strong> &mdash; Use your phone's camera to scan your medication labels and your list of preferred doctors. We check each one against the official HealthCare.gov drug and provider lists before using it to select your plans.</li>
<li><strong>Total cost, not premium</strong> &mdash; Our tools search the drug lists of every insurer offering ACA plans in North Carolina to estimate what your medications will actually cost on each plan, not just whether they're covered.</li>
<li><strong>Seamless enrollment</strong> &mdash; We guide you through the application so everything is set up correctly, including subsidy eligibility.</li>
<li><strong>Year-round support</strong> &mdash; Questions about policy terms, claims or network issues down the road? We are here throughout the year.</li>
<li><strong>Unbiased</strong> &mdash; We don't earn more by steering you toward expensive plans. Our sole focus is the smartest financial and coverage decision for your family or business.</li>
</ul>

<h2 id="about">About Kurt Conger</h2>
<p>Kurt Conger is an independent, licensed North Carolina health insurance agent (NC Health Producer, NPN 21720013) and the founder of Fact-Based Healthcare Decisions and <a href="https://covanu.com" target="_blank" rel="noopener">Covanu</a>, software that selects ACA plans from the official HealthCare.gov plan, drug-list and provider data. Before founding the agency he spent his career in consulting, including Deloitte, working with healthcare and life-sciences clients. He lives on the Crystal Coast in Carteret County and works with self-employed North Carolinians, small business owners and early retirees across the state. Every guide on this site is written by Kurt from the current plan year's HealthCare.gov data and carries the date it was last checked.</p>
<p>Agents and brokers interested in the Covanu tools: see <a href="/agents">the agent page</a>.</p>

{cta("Two ways to start")}
"""
simple_page("/about/", "How We Work | Fact-Based Healthcare Decisions",
            "An independent, licensed NC health insurance agency that compares every ACA plan with data and software, recommends ACA-compliant plans only, and charges you nothing. About Kurt Conger, NPN 21720013.",
            "/about/", [("/", "Home"), (None, "How We Work")], body,
            [{"@context": "https://schema.org", **ORG}, {"@context": "https://schema.org", **PERSON}])

# ---------- homepage ----------
home_body = f"""
        <header class="header">
            <img src="/MFHD_LOGO.png" alt="Fact-Based Healthcare Decisions logo" class="logo">
            <div class="header-text">
                <h1>Fact-Based Healthcare Decisions</h1>
                <p class="tagline">Health insurance guidance for North Carolinians</p>
            </div>
        </header>

        <section class="intro">
            <p>Starting a business, retiring early, or losing coverage? We use data and software from <a href="{APP}" target="_blank" rel="noopener" class="brand-link">Covanu</a> to compare every ACA plan available to you on total yearly cost, then meet with you to finish the choice and enroll. Independent, licensed in North Carolina, and free to you.</p>
        </section>

        <section class="ways">
            <div class="ways-grid">
                <div class="way-card">
                    <h3>Start on my own</h3>
                    <p>Answer a questionnaire about your goals, family size and care needs, enter or scan your medications and preferred providers, and see the plans that best fit your situation. When you're ready, we finish it together.</p>
                    <div class="way-actions">
                        <a class="btn" href="{APP}" target="_blank" rel="noopener">Compare plans with Covanu</a>
                    </div>
                </div>
                <div class="way-card">
                    <h3>Review plans together</h3>
                    <p>Book a time and we'll go through your goals and care needs by phone or in a video meeting where I share my screen.</p>
                    <div class="way-actions">
                        <a class="btn" href="{CAL}" target="_blank" rel="noopener">Schedule a meeting</a>
                        <a class="btn btn-outline" href="mailto:kurt.conger@gmail.com?subject=Time%20to%20review%20health%20plans&amp;body=Here%20are%20some%20times%20that%20work%20for%20me%3A%20">Email me a time</a>
                        <a class="btn btn-outline phone-only" href="sms:+19734418505">Text me a time</a>
                    </div>
                </div>
            </div>
        </section>

        <section class="guides-home">
            <h2 class="section-heading">Common questions</h2>
            <p class="section-sub">Answers built on the official 2027 HealthCare.gov plan data for North Carolina.</p>
            {cards(GUIDES)}
        </section>

        <section class="guides-home geo-gate">
            <h2 class="section-heading">County guides</h2>
            <p class="section-sub">Every 2027 plan sold in your county, with local prices, explained plan by plan. Click your county.</p>
            {county_cards()}
        </section>

        <section class="why-us">
            <h2>How we work</h2>
            <ul class="features-list">
                <li><strong>ACA-compliant plans only</strong> &mdash; on-exchange through HealthCare.gov, and off-exchange plans sold only through licensed agents. No health shares or fixed-indemnity plans.</li>
                <li><strong>Total cost, not premium</strong> &mdash; our tools price your medications on every plan's drug list and estimate what a year actually costs.</li>
                <li><strong>Free, and unbiased</strong> &mdash; insurers pay our commission, and it's the same whichever plan you choose.</li>
            </ul>
            <p style="margin-top:12px"><a class="more" href="/about/">More about how we work and about Kurt Conger &rarr;</a></p>
        </section>

        <section class="contact" id="about">
            <p><strong>Kurt Conger</strong> &middot; Independent licensed NC health insurance agent, NPN 21720013</p>
            <a href="mailto:kurt.conger@gmail.com">kurt.conger@gmail.com</a>
        </section>
"""

home_ld = [
    {"@context": "https://schema.org", **ORG},
    {"@context": "https://schema.org", "@type": "WebSite", "name": "Fact-Based Healthcare Decisions", "url": BASE, "publisher": {"@id": BASE + "/#org"}},
]
doc = head("Fact-Based Healthcare Decisions | ACA Health Insurance Guidance for North Carolina",
           "Independent, licensed ACA health insurance guidance for North Carolina individuals, families, the self-employed and early retirees. Compare every Marketplace plan with Covanu, then enroll with a licensed agent. Free.",
           "/", home_ld, "website") + nav("/")
doc += '    <div class="container">\n' + home_body + '    </div>\n'
doc += """    <script>
        (function () {
            var phone = /Android|iPhone|iPod|Mobi/i.test(navigator.userAgent || "") || (window.matchMedia && window.matchMedia("(pointer: coarse) and (max-width: 900px)").matches);
            if (phone) document.documentElement.classList.add("is-phone");
        })();
    </script>
"""
doc += footer()
write("/index.html", doc)

# ---------- 404 ----------
doc = head("Page not found | Fact-Based Healthcare Decisions", "That page does not exist.", "/404.html", None, "website") + nav("")
doc += f"""    <div class="container"><article class="article">
<h1>That page isn't here</h1>
<p>The address may have changed. Try one of these:</p>
<ul>
<li><a href="/">Home</a></li>
<li><a href="/counties/">County guides</a></li>
<li><a href="/questions/">Common questions</a>: <a href="/questions/bronze-vs-silver-medications/">medications</a>, <a href="/questions/self-employed-north-carolina-2027/">self-employed</a>, <a href="/questions/retiring-before-65-north-carolina/">retiring before 65</a></li>
<li><a href="{APP}" target="_blank" rel="noopener">Compare plans with Covanu</a></li>
</ul>
</article></div>
""" + footer()
write("/404.html", doc)

# ---------- sitemap, robots, llms.txt ----------
urls = ["/", "/questions/", "/counties/", "/about/"] + [h for h, _, _ in GUIDES] + [f"/counties/{c['slug']}/" for c in ALL_GUIDES] + [f"/counties/zone-{z}/" for z in sorted(ZONES, key=int) if z not in LIVE_ZONES] + ["/agents"]
sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
lastmod = {f"/counties/{g['slug']}/": g["updated"] for g in ALL_GUIDES if "updated" in g}
for u in urls:
    pri = "1.0" if u == "/" else ("0.9" if u.count("/") >= 3 else "0.7")
    sm.append(f"  <url><loc>{BASE}{u}</loc><lastmod>{lastmod.get(u, UPDATED)}</lastmod><changefreq>monthly</changefreq><priority>{pri}</priority></url>")
sm.append("</urlset>\n")
write("/sitemap.xml", "\n".join(sm))

write("/robots.txt", f"""User-agent: *
Allow: /
Disallow: /unsubscribe.html
Disallow: /planoptions.html
Disallow: /primarycare.html
Disallow: /local_healtcare.html

Sitemap: {BASE}/sitemap.xml
""")

county_lines = "\n".join(f"- [{c['name']} County, NC health insurance 2027]({BASE}/counties/{c['slug']}/): {c['short']}." for c in sorted(COUNTIES, key=lambda c: c["name"]))
other_lines = "\n".join(f"- [{c['name']} County, NC health insurance 2027]({BASE}/counties/{c['slug']}/): {c['short']}." for c in sorted(OTHER_GUIDES, key=lambda c: c["name"]) if c["slug"] != "new-hanover")
nh = [c for c in OTHER_GUIDES if c["slug"] == "new-hanover"][0]
nh_line = f"- [New Hanover County, NC health insurance 2027]({BASE}/counties/new-hanover/): {nh['short']}."
import json as _json, os as _os
_Z = _json.load(open(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "zones_2027.json"), encoding="utf-8"))
_tot = {c["county"]: c["total"] for c in _Z["counties"].values()}
_lo, _hi = min(_tot.values()), max(_tot.values())
plan_range = f"from {_lo} plans in {' and '.join(sorted(k for k, v in _tot.items() if v == _lo))} County to {_hi} in {', '.join(sorted(k for k, v in _tot.items() if v == _hi))}"
write("/llms.txt", f"""# Fact-Based Healthcare Decisions

> Independent, licensed ACA (Affordable Care Act) health insurance guidance for North Carolina individuals, families, self-employed people and early retirees, written by Kurt Conger (NC Health Producer, NPN 21720013). Guides are built from the official HealthCare.gov Marketplace API data for the current plan year (2027) and state the date they were last checked. Help is free to consumers; insurers pay agent commissions.

## Common questions (2027 plan year)

- [Bronze vs. Silver when you take medications]({BASE}/questions/bronze-vs-silver-medications/): year-long total cost (premium plus deductible, copays, coinsurance) for generic, brand-name and specialty drug users on real Blue Cross NC plans; why a $0 Bronze plan often costs more than a $150 Silver plan with cost-sharing reductions; for a 45-year-old at $30,000 the benchmark Silver costs about $154 a month in every county, while the cheapest Bronze is free in 37 counties and $20 to $74 a month in the other 63.
- [Health insurance for the self-employed in North Carolina (2027)]({BASE}/questions/self-employed-north-carolina-2027/): how premium tax credits use MAGI, the 400% federal-poverty-level cliff in dollars (from about $240 a year for a 40-year-old in Guilford County to $46,000 for a couple in their sixties in eastern NC), the self-employed health insurance deduction, SEP-IRA and HSA levers, elimination of repayment caps.
- [Retiring before 65 in North Carolina]({BASE}/questions/retiring-before-65-north-carolina/): COBRA vs. Marketplace, what a 64-year-old pays, which retirement income counts toward MAGI, income planning for the bridge years, the hand-off to Medicare; a 64-year-old at $60,000 can get a $0 Bronze plan in 33 counties and pays about $80 to $345 a month for the cheapest Bronze elsewhere, and the cliff is $9,600 to $21,900 for one person and $22,000 to $46,200 for a couple, depending on the county.
- [Blue Care vs. Blue Advantage]({BASE}/questions/blue-care-vs-blue-advantage/): in 90 counties each Blue Cross NC plan comes as a Blue Care HMO and a Blue Advantage PPO with identical benefits; the PPO costs 2.7% to 5.5% more depending on the rating area and buys nationwide in-network access (BlueCard), not meaningful out-of-network coverage; in 31 counties the narrower Blue Home, Blue Local and Blue Value networks cost 13% to 33% less than Blue Care; in the Triangle no PPO is sold on HealthCare.gov, and a Blue Cross NC PPO is available only off-exchange through licensed agents, without premium tax credits; who should pay for it.

## County guides

The counties from the Crystal Coast to the Albemarle Sound and the Virginia line (CMS rating areas 12 and 16) share the same 20 Blue Cross NC Marketplace plans for 2027 (10 designs x Blue Care HMO / Blue Advantage PPO) and have no other carrier; Edgecombe, Greene, Pitt, Wayne and Wilson counties (rating area 14) have the same 10 designs and two networks under their own plan numbers and prices. Each guide gives that county's premiums by age and income, HMO vs. PPO analysis, drug-list analysis, plan-by-plan descriptions and a situations table.

{county_lines}

The counties in every other rating area (1 to 11, 13 and 15) and Nash County have more than one insurer or more than one Blue Cross network ({plan_range}). Each guide is built from the HealthCare.gov Marketplace API (retrieved November 10, 2026) and compares the networks, the standardized "Easy Pricing" plans across insurers, the subsidy benchmark, every plan design, and the network status of the area's main hospitals in HealthCare.gov's doctor and hospital lookup.

{other_lines}

New Hanover County (Wilmington, CMS rating area 15) has four Marketplace carriers for 2027 (Ambetter, Blue Cross NC, UnitedHealthcare, Oscar) and 75 plans (38 designs). Its guide compares the six networks, the standardized "Easy Pricing" plans across carriers, subsidies pegged to an Ambetter benchmark, and which networks include Novant Health New Hanover Regional Medical Center.

{nh_line}

## Key facts stated on this site (2027)

- 2027 Marketplace income thresholds use 2026 federal poverty guidelines: $15,960 (1 person), $21,640 (2), $33,000 (4). 400% = $63,840 / $86,560 / $132,000. NC Medicaid expansion line (138%) = $22,025 / $29,863 / $45,540.
- Enhanced premium tax credits expired after 2025; the 400% FPL cliff applies for 2027. Repayment caps on excess credits are eliminated from the 2026 tax year.
- 2027 applicable percentages (IRS Rev. Proc. 2026-26) run from 2.15% of income below 133% of the poverty level to 10.22% at 300% to 400%; the employer-coverage affordability threshold is also 10.22%.
- All Bronze Marketplace plans are HSA-eligible from 2026 under the 2025 federal tax law; 2027 HSA limits are $4,500 self-only / $9,000 family plus $1,000 catch-up at 55+.
- In the rating area 12 and 16 counties above there is one Marketplace carrier (Blue Cross and Blue Shield of NC) and no catastrophic plan in 2027. Blue Advantage (PPO) costs about 5.5% more than the identical Blue Care (HMO) design; neither requires specialist referrals. Elsewhere Blue Advantage costs 5.2% to 5.5% more than Blue Care in rating area 15, 4.4% to 4.6% in rating area 1, 3.2% to 3.4% in rating area 14 and 2.7% to 3.2% in the other rating areas where it is sold; it is not sold in rating areas 11 and 13.
- Around the Triangle (rating areas 11 and 13: Alamance, Caswell, Chatham, Durham, Franklin, Johnston, Lee, Orange, Person and Wake counties) Blue Cross sells only Blue Home with UNC Health Alliance, an EPO, and no Blue Advantage PPO, so no Marketplace plan there has a nationwide network; a Blue Cross NC PPO plan is available there off-exchange through licensed agents, without premium tax credits. In HealthCare.gov's lookup on November 10, 2026, in Wake County, WakeMed, Duke Raleigh Hospital and Duke University Hospital were in network on Ambetter plans and not on Blue Home or UnitedHealthcare plans, while UNC Health Rex and UNC Medical Center were in network on Blue Home and UnitedHealthcare plans and not on Ambetter plans. Chatham County's 10 plans are all Blue Home.
- Around Charlotte and the Triad (rating areas 3 to 7) Blue Cross adds narrow EPO networks: Blue Local with Atrium Health, Blue Home with Novant Health and, in Guilford, Randolph and Rockingham counties, Blue Home with Cone Health; Ambetter and Oscar sell plans "with Atrium Health" there. In HealthCare.gov's lookup on November 10, 2026, in Mecklenburg County, Atrium Health Carolinas Medical Center was in network on every plan except Blue Home's, and Novant Health Presbyterian Medical Center was in network on Blue Home, Blue Care and Blue Advantage plans and not on Ambetter, Blue Local or UnitedHealthcare plans.
- Insulin: UnitedHealthcare includes $0 insulin on every 2027 North Carolina plan, but its standardized Silver costs $145 to $552 a month more than the cheapest identical standardized Silver at age 45 in the 37 counties where it sells; Ambetter's Clear Silver with $0 Insulin Options is the benchmark (second-lowest-cost) Silver in all 47 counties where it is sold; Oscar's Simple Diabetes plans cap insulin at $100 for a 30-day supply. Lilly, Novo Nordisk and Sanofi cap their insulins at $35 a month for people with commercial coverage, including Marketplace plans, so without a $0 benefit a two-insulin routine usually costs $35 to $80 a month. North Carolina has no state insulin copay cap.
- Children's dental: included in Blue Cross NC and UnitedHealthcare Marketplace plans (checkups covered in full; other care after the medical deductible on most plans), not in Ambetter, AmeriHealth Caritas Next or Oscar plans. Stand-alone children's dental plans on the North Carolina Marketplace cost about $21 to $58 a month per child for 2027, with $25 to $155 deductibles and $350 to $450 yearly out-of-pocket limits per child.
- In New Hanover County the 2027 benchmark (second-lowest-cost Silver) is Ambetter Clear Silver with $0 Insulin Options ($732 a month at age 45). Ambetter's standardized Silver costs $740 at 45; the identical standardized design costs $978 to $1,184 from Blue Cross, Oscar and UnitedHealthcare. Novant Health New Hanover Regional Medical Center was in network on every Ambetter, Blue Cross and UnitedHealthcare plan and on no Oscar plan (HealthCare.gov lookup, November 10, 2026). No catastrophic plan is offered.

## About

- [How we work]({BASE}/about/)
- [Covanu plan selector]({APP}): compares every plan in a county with the user's subsidy, medications and doctors.
- [Schedule a call]({CAL})
- Contact: Kurt Conger, kurt.conger@gmail.com
""")
