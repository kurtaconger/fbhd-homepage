from fbsite import *

# "Is there any way to measure the quality of ACA plans?" (written November 13, 2026).
# North Carolina 2027 star ratings: HealthCare.gov Marketplace API, plan details for one plan per insurer and plan type
# (covanu-insure/Research/zones-2027/quality.mjs -> quality.json, run November 13, 2026). CMS rates each insurer's
# product type in a state ("reporting unit"), so every plan of that insurer and type carries the same stars.

PATH = "/questions/aca-plan-quality-ratings/"
QUESTION = "Is there any way to measure the quality of ACA plans?"
TITLE = "Is There a Way to Measure the Quality of ACA Plans? Star Ratings for North Carolina's 2027 Insurers"
DESC = ("What HealthCare.gov's 1-to-5-star quality ratings measure, how each North Carolina Marketplace insurer rates for 2027, "
        "and the other yardsticks: claim denial rates, complaint records and NCQA, plus what matters more than the stars.")
CRUMBS = [("/", "Home"), ("/questions/", "Common Questions"), (None, "Measuring plan quality")]
DATE, DATE_H = "2026-11-13", "November 13, 2026"

KFF_DENIALS = "https://www.kff.org/patient-consumer-protections/claims-denials-and-appeals-in-aca-marketplace-plans-in-2024/"
CMS_QRS = "https://www.cms.gov/marketplace/about/health-insurance-quality-initiatives/quality-rating-system"
CMS_QRS101 = "https://www.cms.gov/files/document/health-insurance-exchange-quality-ratings-system-101-py2024.pdf"
CMS_BULLETIN = "https://www.cms.gov/files/document/quality-rating-information-bulletin-march-2026.pdf"
CMS_PUF = "https://www.cms.gov/marketplace/resources/data/public-use-files"
NAIC_CIS = "https://content.naic.org/cis_consumer_information.htm"
NCQA_METHOD = "https://wpcdn.ncqa.org/www-prod/2025-HPR-Methodology_December-2024-Posting.pdf"

# (insurer and network, plan type, overall, medical care, member experience, plan administration); None = not rated
NR = None
RATINGS = [
    ("Blue Cross NC: Blue Advantage", "PPO", 4, 4, 5, 4),
    ("Blue Cross NC: Blue Home and Blue Local", "EPO", 4, 4, 5, 4),
    ("Blue Cross NC: Blue Value", "POS", 4, 4, 5, 3),
    ("Ambetter of North Carolina", "HMO", 3, 2, 5, 4),
    ("UnitedHealthcare", "HMO", 3, 2, NR, 4),
    ("Oscar", "HMO", 2, 2, NR, 5),
    ("AmeriHealth Caritas Next", "HMO", 2, 2, NR, 3),
]


def stars(n):
    if n is None:
        return '<td class="num">Not rated*</td>'
    return f'<td class="num"><span class="stars" aria-hidden="true">{"&#9733;" * n}{"&#9734;" * (5 - n)}</span> {n}</td>'


rows = "\n".join(f"<tr><td>{name}</td><td>{typ}</td>{stars(o)}{stars(m)}{stars(e)}{stars(a)}</tr>" for name, typ, o, m, e, a in RATINGS)
rows += '\n<tr><td>Blue Cross NC: Blue Care</td><td>HMO</td><td class="num" colspan="4">New plan &ndash; not rated</td></tr>'

FAQ = [
    ("Where do I see a plan's star rating on HealthCare.gov?",
     "The Overall rating appears with each plan in the list of plans for your area. Open a plan's details to see the three category ratings: Medical Care, Member Experience and Plan Administration. "
     "Plans without enough history show “New plan – Not rated” or “Not rated” instead."),
    ("Why does a plan say “New plan – Not rated”?",
     "CMS rates a product only after it has been sold on the Marketplace for three years in a row and has more than 500 members. For 2027, that means a product sold in 2024, 2025 and 2026. "
     "In North Carolina, Blue Cross NC's Blue Care HMO plans show as new for 2027. Not rated means there is not yet enough data, not that the plan is poor."),
    ("Is a 4-star plan always better than a 3-star plan?",
     "No. The stars describe an insurer's whole product in the state, every metal level alike, using data from a year or more earlier. A 3-star plan that includes your doctors and covers your prescriptions "
     "will usually serve you better than a 4-star plan that does not. Use the ratings to choose between plans that already fit."),
    ("Do star ratings change my premium or my subsidy?",
     "No. Your premium tax credit is set by the price of the second-lowest-cost Silver plan in your area and your income. The quality rating has no effect on either."),
]

body = f"""
<h1>{QUESTION}</h1>
{byline("8 minute read", DATE_H, "Ratings: HealthCare.gov Marketplace API, 2027 plan year")}

<p class="lede">Yes, partly. HealthCare.gov gives every Marketplace plan a quality rating from 1 to 5 stars, built by the federal government from medical-care measures and a survey of each plan's own members. Federal data also show how often each insurer denies claims, and insurance regulators track complaints. None of these tell you what matters most for your own care: whether your doctors, your hospital and your prescriptions are covered. Here is what each measure means, how North Carolina's insurers rate for 2027, and how to use the ratings without over-reading them.</p>

<div class="takeaways">
<h2>Key takeaways</h2>
<ul>
<li><strong>The official measure is CMS's star rating,</strong> shown next to every plan on HealthCare.gov: an Overall rating plus Medical Care, Member Experience and Plan Administration.</li>
<li><strong>In North Carolina for 2027,</strong> Blue Cross NC's Blue Advantage, Blue Home, Blue Local and Blue Value plans have 4 stars; Ambetter and UnitedHealthcare have 3; Oscar and AmeriHealth Caritas Next have 2. Blue Cross NC's Blue Care HMO plans are new and not rated.</li>
<li><strong>The stars describe an insurer's product, not a single plan:</strong> every metal level of the same insurer and plan type carries the same rating, and the data are a year or more old.</li>
<li><strong>Claim denials vary widely.</strong> HealthCare.gov insurers denied 19% of in-network claims in 2024, from 3% at one insurer to 36% at another.</li>
<li><strong>Network and drugs come first.</strong> Pick the plans that include your doctors and cover your medications, then let quality break the tie.</li>
</ul>
</div>

<h2>HealthCare.gov's star ratings</h2>
<p>The Affordable Care Act requires a quality rating for every Marketplace plan. The Centers for Medicare &amp; Medicaid Services (CMS) builds it each year through its <a href="{CMS_QRS}" target="_blank" rel="noopener">Quality Rating System</a> and shows it on HealthCare.gov on a scale of 1 to 5 stars, 5 being the best. You see an Overall rating in the plan list and three category ratings in each plan's details:</p>
<ul>
<li><strong>Medical Care:</strong> how well the plan's network doctors manage members' care, such as regular screenings, vaccines and diabetes care. This category counts the most in the Overall rating.</li>
<li><strong>Member Experience:</strong> a CMS survey of the plan's own members about their doctors and care and how easy it is to get appointments and services.</li>
<li><strong>Plan Administration:</strong> how well the plan is run, including customer service, access to needed information, and whether network doctors order appropriate tests and treatment.</li>
</ul>
<p>Three details change how you should read them:</p>
<ul>
<li><strong>Ratings belong to a product, not a plan.</strong> CMS rates each insurer's plan type in a state, its HMO, PPO, EPO or POS plans, so a Bronze and a Gold plan from the same product carry the same stars.</li>
<li><strong>New and small products are not rated.</strong> A product must have been sold on the Marketplace for three years in a row with more than 500 members. For 2027 that means 2024, 2025 and 2026; otherwise HealthCare.gov shows &ldquo;New plan &ndash; Not rated.&rdquo;</li>
<li><strong>They look backward.</strong> The 2027 ratings were calculated in 2026, mostly from care delivered in 2025. They describe how a product performed recently, not a promise about next year.</li>
</ul>

<h2>How North Carolina's insurers rate for 2027</h2>
<p>These are the ratings HealthCare.gov shows for every 2027 Marketplace plan in North Carolina, by insurer and plan type.</p>
<div class="table-wrap">
<table class="data">
<thead><tr><th>Insurer and network</th><th>Plan type</th><th class="num">Overall</th><th class="num">Medical Care</th><th class="num">Member Experience</th><th class="num">Plan Administration</th></tr></thead>
<tbody>
{rows}
</tbody>
</table>
</div>
<p class="table-note">* Not enough member survey data to score. Source: HealthCare.gov Marketplace API, 2027 plan year, retrieved {DATE_H}.</p>
<p>What the table shows:</p>
<ul>
<li><strong>Medical Care separates the insurers most.</strong> Every rated Blue Cross NC product scores 4; every other insurer scores 2.</li>
<li><strong>Members like Ambetter as much as Blue Cross.</strong> Both get 5 stars for Member Experience, the highest score possible. UnitedHealthcare, Oscar and AmeriHealth Caritas Next did not have enough survey data to be scored.</li>
<li><strong>Oscar scores best on administration.</strong> Its 5-star Plan Administration rating is the highest in the state, but its Overall rating is 2 because Medical Care counts the most.</li>
<li><strong>Not rated is not a warning.</strong> Blue Care HMO plans show as new for 2027, which reflects how CMS counts products, not a judgment on their quality.</li>
</ul>

<h2>Other ways to measure an insurer</h2>
<h3>Claim denial rates</h3>
<p>Marketplace insurers must report to CMS how many claims they deny and how appeals turn out. KFF's analysis of that data found that insurers on HealthCare.gov denied 19% of in-network claims in 2024, with individual insurers ranging from 3% to 36%, and that members appealed fewer than 1% of denials. Read the numbers with care: many denials are duplicate or incomplete claims that are fixed and paid later, and CMS itself says denial counts are not necessarily a measure of plan quality. A denial rate far above the average is still worth asking about. The insurer-by-insurer figures are in <a href="{KFF_DENIALS}" target="_blank" rel="noopener">KFF's report</a> and in CMS's <a href="{CMS_PUF}" target="_blank" rel="noopener">Transparency in Coverage public use file</a>.</p>

<h3>Complaint records</h3>
<p>State insurance regulators record the complaints they confirm against each company, and the National Association of Insurance Commissioners publishes them in its <a href="{NAIC_CIS}" target="_blank" rel="noopener">Consumer Insurance Search</a>. The complaint index compares a company's share of complaints with its share of the business: 1.00 is average, 2.00 means twice the complaints you would expect for its size. Search for the company named on the plan (for example, Blue Cross and Blue Shield of North Carolina), choose North Carolina and health insurance, and look at more than one year. If you have a problem with your own insurer, you can file a complaint with the NC Department of Insurance.</p>

<h3>NCQA ratings and accreditation</h3>
<p>The National Committee for Quality Assurance publishes its own health plan ratings, but <a href="{NCQA_METHOD}" target="_blank" rel="noopener">NCQA does not rate Marketplace plans</a>; its ratings cover employer, Medicare Advantage and Medicaid plans. An insurer's rating for its employer plans says something about the company, not about the Marketplace product you would buy. Accreditation does not separate Marketplace insurers either, because every one of them must be accredited to sell on the Marketplace.</p>

<h3>Your right to appeal</h3>
<p>One protection is the same on every ACA plan, whatever its stars: if a claim is denied you can appeal to the insurer and then ask for an independent outside review through the state's Smart NC program, and the reviewer's decision binds the insurer. That right is one of the things you give up with the alternatives described in <a href="/questions/cheaper-alternatives-to-aca-plans/">Are there cheaper options than an ACA plan?</a></p>

<h2>What matters more than the stars</h2>
<ol>
<li><strong>Your doctors and hospital.</strong> A 4-star plan that leaves out your cardiologist is a worse plan for you. Our <a href="/counties/">county guides</a> show which of your area's hospitals each network includes.</li>
<li><strong>Your prescriptions.</strong> Check that each medication is on the plan's drug list and which tier it is on; see <a href="/questions/bronze-vs-silver-medications/">Bronze vs. Silver when you take medications</a>.</li>
<li><strong>Your total yearly cost.</strong> Premium plus what you would pay in deductibles, copays and coinsurance for the care you expect.</li>
<li><strong>Then quality.</strong> Among the plans that pass the first three tests, prefer the higher Medical Care and Member Experience ratings, and look up the insurer's complaint record.</li>
</ol>

{cta("Compare plans with your doctors and drugs", "Enter your county, ages and income and our Covanu tool shows every plan with your subsidy applied, checks your medications against each plan's drug list, and estimates your total yearly cost. Then book a call and we'll weigh the ratings together. Our help is free.")}

{author_box()}

{sources([
    '<a href="https://www.healthcare.gov/developers/" target="_blank" rel="noopener">HealthCare.gov Marketplace API</a>: 2027 quality ratings of North Carolina Marketplace plans, retrieved ' + DATE_H + '.',
    f'<a href="{CMS_QRS}" target="_blank" rel="noopener">CMS, About the Quality Rating System</a>.',
    f'<a href="{CMS_QRS101}" target="_blank" rel="noopener">CMS, Health Insurance Exchange Quality Rating System 101</a>: categories, weighting, reporting units and the 500-member threshold.',
    f'<a href="{CMS_BULLETIN}" target="_blank" rel="noopener">CMS bulletin on the display of quality ratings for plan year 2027</a> (March 2026): &ldquo;New plan &ndash; Not Rated.&rdquo;',
    f'<a href="{KFF_DENIALS}" target="_blank" rel="noopener">KFF, Claims Denials and Appeals in ACA Marketplace Plans in 2024</a> (March 24, 2026).',
    f'<a href="{CMS_PUF}" target="_blank" rel="noopener">CMS Exchange public use files</a>: Transparency in Coverage data and disclaimer.',
    f'<a href="{NAIC_CIS}" target="_blank" rel="noopener">NAIC Consumer Insurance Search</a>: complaint index.',
    f'<a href="{NCQA_METHOD}" target="_blank" rel="noopener">NCQA 2025 Health Plan Ratings methodology</a>.',
])}
"""

page(PATH, TITLE, DESC, "/questions/", CRUMBS, body, faq=FAQ, reading="8 minute read", date=DATE)
