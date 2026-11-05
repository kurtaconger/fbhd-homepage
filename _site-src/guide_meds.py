from fbsite import *

PATH = "/questions/bronze-vs-silver-medications/"
TITLE = "Bronze vs. Silver When You Take Medications: Estimated Total Cost, Not Just Premium (NC, 2027)"
DESC = "A $0 Bronze plan can cost thousands more than a $150 Silver plan once you fill a brand-name prescription. Year-long cost comparisons for generic, brand and specialty drug users, using real 2027 Blue Cross NC plans."
CRUMBS = [("/", "Home"), ("/questions/", "Common Questions"), (None, "Bronze vs. Silver with medications")]

FAQ = [
    ("Is a $0 Bronze plan ever a bad deal?",
     "Yes, whenever you expect to use care. The subsidy that makes Bronze free is the same dollar amount you could put toward Silver, and below 250% of the poverty level Silver plans also come with cost-sharing reductions that cut the deductible to a few hundred dollars. If you take any brand-name drug or see a doctor more than a couple of times a year, a $150-a-month Silver plan with an $800 deductible usually costs less over the year than a free Bronze with a $7,000 deductible."),
    ("How do I find out what tier my drug is on?",
     "Every Marketplace plan publishes its drug list (formulary). HealthCare.gov lets you enter your prescriptions when you compare plans and flags whether each is covered. Our Covanu tool goes a step further and estimates what each drug will cost you on each plan, including whether the deductible applies."),
    ("What is the difference between a copay and coinsurance for drugs?",
     "A copay is a fixed amount ($40 for a preferred brand drug, say) regardless of the drug's price. Coinsurance is a percentage of the price (50% of a $650 drug is $325). On most Bronze plans and some Silver and Gold plans, brand-name drugs are coinsurance after the deductible, which means you pay the full price until the deductible is met. Plans labeled Standard, and the Gold All Copay plan, use copays instead."),
    ("Does the deductible apply to generic drugs?",
     "Rarely. On every 2027 Blue Cross NC Marketplace plan except Bronze HSA Eligible Plus, generic drugs are a flat copay ($10 to $25) from the first fill. The deductible question is about brand-name and specialty drugs."),
    ("Are GLP-1 drugs like Ozempic and Wegovy covered?",
     "On the 2027 Blue Cross NC Marketplace drug lists we checked, Ozempic, Mounjaro, Trulicity and Rybelsus are covered (for diabetes; prior authorization usually applies). Wegovy and Zepbound, the weight-loss versions, are not covered. Coverage can change during the year, so confirm on the plan's drug list."),
    ("What if my drug is not covered at all?",
     "You can ask the insurer for a formulary exception with your doctor's support, use a manufacturer coupon or patient-assistance program, or compare cash prices at discount pharmacies. Tell us the drug before you enroll; the right plan sometimes depends on it."),
]

body = f"""
<h1>Bronze vs. Silver When You Take Medications: Estimated Total Cost, Not Just Premium</h1>
{byline("9 minute read")}

<p class="lede">The cheapest premium is rarely the cheapest plan once you fill a prescription. This guide adds up what a year actually costs (premiums plus deductibles, copays and coinsurance) for three kinds of medication users, using the real 2027 Blue Cross NC plans sold in <a href="/counties/carteret/">Carteret County</a>. The same plan designs are sold across North Carolina, so the pattern applies wherever you live; only the premiums change.</p>

<div class="takeaways">
<h2>Key takeaways</h2>
<ul>
<li><strong>Generics only:</strong> Bronze wins. A $7,000 deductible never comes into play when your drugs are $15&ndash;$25 copays.</li>
<li><strong>One brand-name drug:</strong> the picture flips. A single preferred brand prescription (Eliquis, Jardiance, Xarelto) costs about $7,400 a year on Bronze Basic but $480 on Silver Standard, enough to make Silver Standard about $3,400 cheaper over the year despite a $300 higher monthly premium.</li>
<li><strong>A specialty drug:</strong> Gold is cheapest. On Gold All Copay A or Gold Standard A a $3,900-a-month biologic is a $220&ndash;$250 copay; on most other plans you hit the out-of-pocket maximum by spring.</li>
<li><strong>If you qualify for a subsidy,</strong> compare the free Bronze plan to the $150 Silver plan with cost-sharing reductions. The Silver plan's deductible drops to $325&ndash;$800 and its worst case to $3,600&ndash;$4,000, which usually beats "free" with a $7,000 deductible.</li>
<li><strong>The plan design matters more than the drug list.</strong> Blue Cross NC's two drug lists cover the same drugs; what differs is whether your brand drug is a flat copay or coinsurance after the deductible.</li>
</ul>
</div>

<h2>Why the premium is the wrong number to compare</h2>
<p>Your yearly cost has two parts: 12 months of premium, which you know in advance, and what you pay when you use the plan, which depends on the plan's rules. For medications the rule that matters is simple to state: <strong>does the deductible apply to this drug?</strong></p>
<ul>
<li>If the drug is a <strong>copay</strong>, you pay the copay every fill from the first one. Silver Standard charges $40 for a preferred brand drug whether it costs $200 or $2,000.</li>
<li>If the drug is <strong>coinsurance after the deductible</strong>, you pay its full negotiated price until you have spent the deductible, then a percentage. On Bronze Basic that is $7,000 first, then 50%.</li>
</ul>
<p>Brand-name drugs cost $500 to $5,000 a month, so a plan that makes you pay the deductible first turns one prescription into most of a year's out-of-pocket maximum. Generic drugs are $10&ndash;$25 copays on nearly every plan, so for generics the deductible never matters.</p>

<h2>How each 2027 Blue Cross NC plan prices prescriptions</h2>
<div class="table-wrap">
<table class="data">
<caption>In-network drug cost sharing, individual coverage, no cost-sharing reduction. Blue Care and Blue Advantage versions are identical. Premiums are full price for a 45-year-old in Carteret County on the Blue Care network. Source: HealthCare.gov Marketplace API, 2027.</caption>
<thead><tr><th>Plan</th><th class="num">Premium /mo</th><th class="num">Deductible</th><th>Generic</th><th>Preferred brand</th><th>Non-preferred brand</th><th>Specialty</th></tr></thead>
<tbody>
<tr><td>Bronze Basic</td><td class="num">$825</td><td class="num">$7,000</td><td>$25</td><td>50% after ded.</td><td>50% after ded.</td><td>50% after ded.</td></tr>
<tr><td>Bronze Standard</td><td class="num">$847</td><td class="num">$7,500</td><td>$25</td><td>$50 after ded.</td><td>$100 after ded.</td><td>$500 after ded.</td></tr>
<tr><td>Bronze Complete</td><td class="num">$859</td><td class="num">$4,000 + $1,000 Rx</td><td>$20</td><td>$75 after Rx ded.</td><td>$150 after Rx ded.</td><td>50% after ded.</td></tr>
<tr><td>Bronze HSA Eligible Plus</td><td class="num">$888</td><td class="num">$8,700</td><td>after ded.</td><td>after ded.</td><td>after ded.</td><td>after ded.</td></tr>
<tr><td>Silver Preferred</td><td class="num">$1,116</td><td class="num">$2,700</td><td>$15</td><td>50% after ded.</td><td>50% after ded.</td><td>50% after ded.</td></tr>
<tr><td>Silver Standard</td><td class="num">$1,125</td><td class="num">$6,400</td><td>$20</td><td><strong>$40, no ded.</strong></td><td>$80 after ded.</td><td>$350 after ded.</td></tr>
<tr><td>Silver Choice A</td><td class="num">$1,140</td><td class="num">$3,500 + $200 Rx</td><td>$15</td><td>$35 after Rx ded.</td><td>$70 after Rx ded.</td><td>50% after ded.</td></tr>
<tr><td>Gold Premier A</td><td class="num">$1,149</td><td class="num">$1,800 + $400 Rx</td><td>$10</td><td>$35 after Rx ded.</td><td>$60 after Rx ded.</td><td>50% after ded.</td></tr>
<tr><td>Gold Standard A</td><td class="num">$1,160</td><td class="num">$2,500</td><td>$15</td><td><strong>$30, no ded.</strong></td><td><strong>$60, no ded.</strong></td><td><strong>$250, no ded.</strong></td></tr>
<tr><td>Gold All Copay A</td><td class="num">$1,175</td><td class="num">$0</td><td>$10</td><td><strong>$60</strong></td><td><strong>$120</strong></td><td><strong>$220</strong></td></tr>
</tbody>
</table>
</div>
<p>Notice the three plans with bold entries. Silver Standard and Gold Standard A are the federally standardized designs, and Gold All Copay A is Blue Cross NC's no-deductible plan. They are the only plans where a brand-name drug is a predictable copay from day one.</p>

<h2>Three people, one year, every plan</h2>
<p>The estimates below use these assumptions: a 45-year-old in Carteret County paying full price; brand drugs priced at approximate list price (Eliquis about $650 a month, Dupixent about $3,900 a month), which is close to what counts toward the deductible; generics at the plan copay; and a modest number of doctor visits. Totals are premium plus everything paid at the pharmacy and the doctor, capped at the plan's out-of-pocket maximum.</p>

<h3>Person 1: two generic prescriptions, two doctor visits</h3>
<p>Lisinopril and atorvastatin, say, plus two primary care visits. Nothing touches the deductible, so the ranking is simply the premium ranking.</p>
<div class="table-wrap">
<table class="data">
<thead><tr><th>Plan</th><th class="num">Premiums</th><th class="num">Drugs</th><th class="num">Visits</th><th class="num">Year total</th></tr></thead>
<tbody>
<tr class="best"><td>Bronze Basic</td><td class="num">$9,897</td><td class="num">$600</td><td class="num">$0 (3 free visits)</td><td class="num">$10,497</td></tr>
<tr><td>Bronze Standard</td><td class="num">$10,166</td><td class="num">$600</td><td class="num">$100</td><td class="num">$10,866</td></tr>
<tr><td>Silver Preferred</td><td class="num">$13,392</td><td class="num">$360</td><td class="num">$0 (3 free visits)</td><td class="num">$13,752</td></tr>
<tr><td>Silver Standard</td><td class="num">$13,498</td><td class="num">$480</td><td class="num">$80</td><td class="num">$14,058</td></tr>
<tr><td>Gold Standard A</td><td class="num">$13,915</td><td class="num">$360</td><td class="num">$60</td><td class="num">$14,335</td></tr>
<tr><td>Gold All Copay A</td><td class="num">$14,102</td><td class="num">$240</td><td class="num">$60</td><td class="num">$14,402</td></tr>
</tbody>
</table>
</div>
<p><strong>Verdict:</strong> Bronze, by about $3,500 a year over the cheapest Silver. The only argument for Silver here is insurance against a bad year, and Bronze HSA Eligible Plus (year total about $11,254 with an $8,700 ceiling) answers that more cheaply.</p>

<h3>Person 2: one preferred brand drug, one generic, four primary care visits, one specialist</h3>
<p>Eliquis (a blood thinner, about $650 a month) plus metoprolol, four primary care visits and one specialist visit. This is an ordinary 50-something, and it is where the ranking turns upside down.</p>
<div class="table-wrap">
<table class="data">
<thead><tr><th>Plan</th><th class="num">Premiums</th><th class="num">Eliquis</th><th class="num">Generic</th><th class="num">Visits</th><th class="num">Year total</th></tr></thead>
<tbody>
<tr class="best"><td>Bronze Complete</td><td class="num">$10,304</td><td class="num">$1,750 ($1,000 Rx ded., then $75)</td><td class="num">$240</td><td class="num">$360</td><td class="num">$12,654</td></tr>
<tr><td>Silver Standard</td><td class="num">$13,498</td><td class="num">$480 ($40 copay)</td><td class="num">$240</td><td class="num">$240</td><td class="num">$14,458</td></tr>
<tr><td>Gold Standard A</td><td class="num">$13,915</td><td class="num">$360 ($30 copay)</td><td class="num">$180</td><td class="num">$180</td><td class="num">$14,635</td></tr>
<tr><td>Gold All Copay A</td><td class="num">$14,102</td><td class="num">$720 ($60 copay)</td><td class="num">$120</td><td class="num">$180</td><td class="num">$15,122</td></tr>
<tr><td>Bronze Basic</td><td class="num">$9,897</td><td class="num">$7,400 ($7,000 ded., then 50%)</td><td class="num">$300</td><td class="num">$270</td><td class="num">$17,867</td></tr>
<tr><td>Silver Preferred</td><td class="num">$13,392</td><td class="num">$5,250 ($2,700 ded., then 50%)</td><td class="num">$180</td><td class="num">$110</td><td class="num">$18,932</td></tr>
</tbody>
</table>
</div>
<p><strong>Verdict:</strong> the two plans with the lowest premiums, Bronze Basic and Silver Preferred, finish last, and Silver Preferred, the cheapest Silver, is the worst plan on the list for this person. Silver Standard beats Bronze Basic by about $3,400 a year. The surprise winner is Bronze Complete: its separate $1,000 drug deductible is met in the second month, after which Eliquis is a $75 copay. That holds for two or three preferred brand drugs too, because the $1,000 drug deductible is paid once. The catch is on the medical side: Bronze Complete pays 50% after a $4,000 deductible for a hospital stay, surgery or an MRI, with a $12,000 ceiling, where Gold Standard A pays 75% after $2,500 with an $8,600 ceiling. It is the right plan for a brand-drug user who is otherwise healthy, and the wrong one for someone who expects a procedure.</p>

<h3>Person 3: a specialty drug</h3>
<p>Dupixent (about $3,900 a month for eczema or asthma), one generic, four primary care and four specialist visits. Any biologic (Enbrel, Skyrizi, Rinvoq, Stelara) produces the same shape.</p>
<div class="table-wrap">
<table class="data">
<thead><tr><th>Plan</th><th class="num">Premiums</th><th class="num">Dupixent</th><th class="num">Other care</th><th class="num">Year total</th></tr></thead>
<tbody>
<tr class="best"><td>Gold All Copay A</td><td class="num">$14,102</td><td class="num">$2,640 ($220 copay)</td><td class="num">$480</td><td class="num">$17,222</td></tr>
<tr><td>Gold Standard A</td><td class="num">$13,915</td><td class="num">$3,000 ($250 copay)</td><td class="num">$540</td><td class="num">$17,455</td></tr>
<tr><td>Bronze HSA Eligible Plus</td><td class="num">$10,654</td><td class="num" colspan="2">$8,700 (out-of-pocket max)</td><td class="num">$19,354</td></tr>
<tr><td>Bronze Basic</td><td class="num">$9,897</td><td class="num" colspan="2">$12,000 (out-of-pocket max)</td><td class="num">$21,897</td></tr>
<tr><td>Silver Standard</td><td class="num">$13,498</td><td class="num" colspan="2">$10,300 (out-of-pocket max; $6,400 ded., then $350)</td><td class="num">$23,798</td></tr>
<tr><td>Gold Premier A</td><td class="num">$13,783</td><td class="num" colspan="2">$12,000 (out-of-pocket max; 50% after ded.)</td><td class="num">$25,783</td></tr>
</tbody>
</table>
</div>
<p><strong>Verdict:</strong> Gold, and specifically the two Gold plans with specialty copays. Gold Premier A, the cheapest Gold, is the most expensive plan of all for this person because its specialty benefit is 50% coinsurance. The cheapest-premium plan (Bronze Basic) costs $4,700 more than the best Gold. If you cannot afford Gold, Bronze HSA Eligible Plus is the fallback: its $8,700 ceiling is the lowest among the Bronze plans, and HSA contributions can fund part of it pre-tax.</p>

<h2>If you get a subsidy: free Bronze vs. $150 Silver</h2>
<p>Most people who buy on HealthCare.gov qualify for a premium tax credit, and for them the comparison is different and usually easier. Take the same 45-year-old in Carteret with $30,000 of income. Bronze Basic costs $0 a month. Silver Standard costs $154 a month, and because this income is under 250% of the poverty level the plan comes with <strong>cost-sharing reductions</strong>: the deductible falls from $6,400 to $800 and the out-of-pocket maximum from $10,300 to $3,600.</p>
<div class="table-wrap">
<table class="data">
<thead><tr><th>Person</th><th class="num">Bronze Basic ($0/mo)</th><th class="num">Silver Standard with CSR ($154/mo)</th></tr></thead>
<tbody>
<tr><td>Person 1 (generics only)</td><td class="num">about $600</td><td class="num">about $2,150 (premiums $1,846 + $10 generics)</td></tr>
<tr><td>Person 2 (Eliquis)</td><td class="num">about $7,970</td><td class="num">no more than $5,446 (premiums + $3,600 cap), likely well under</td></tr>
<tr><td>Person 3 (Dupixent)</td><td class="num">$12,000</td><td class="num">$5,446 (premiums + $3,600 cap)</td></tr>
</tbody>
</table>
</div>
<p>For anyone on a brand or specialty drug, the "free" plan is the expensive one. Only a generics-only household should take the free Bronze, and even then a Silver plan with an $800 deductible is cheap insurance against a surprise. One more subtlety: cost-sharing reductions only apply to Silver plans, so a subsidized Gold plan (Gold Standard A at $189 a month for this person) keeps its full $2,500 deductible and is rarely the best buy below 250% of the poverty level.</p>

<h2>A quick method for your own situation</h2>
<ol>
<li>List your prescriptions and look up each one's tier on the plan's drug list (or let our tool do it).</li>
<li>For each brand or specialty drug, note whether the plan charges a copay or coinsurance after the deductible. If it is after the deductible, assume you will pay the deductible in full.</li>
<li>Add 12 months of premium to the drug costs and your usual visits. Cap the non-premium part at the out-of-pocket maximum.</li>
<li>Do it for two or three candidate plans, not one. The winner is usually obvious once the numbers are side by side.</li>
</ol>
<p>Or skip the spreadsheet: our Covanu tool checks your medications against every plan's drug list and prices them with the plan's own cost-sharing rules.</p>

{cta("Price your prescriptions on every plan")}

{author_box()}

{sources([
    '<a href="https://www.healthcare.gov/developers/" target="_blank" rel="noopener">HealthCare.gov Marketplace API</a>: 2027 plan benefits, premiums and drug coverage for Carteret County, retrieved ' + UPDATED_H + '.',
    'Drug list prices are approximate 2026 wholesale list prices and are used only to illustrate deductible mechanics; negotiated prices vary by pharmacy and plan.',
    '<a href="https://www.healthcare.gov/lower-costs/save-on-out-of-pocket-costs/" target="_blank" rel="noopener">HealthCare.gov: cost-sharing reductions</a>.',
])}
"""

page(PATH, TITLE, DESC, "/questions/", CRUMBS, body, faq=FAQ, reading="9 minute read")
