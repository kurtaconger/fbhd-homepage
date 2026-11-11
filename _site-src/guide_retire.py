from fbsite import *

PATH = "/questions/retiring-before-65-north-carolina/"
TITLE = "Retiring Before 65 in North Carolina: Bridging to Medicare With a Marketplace Plan (2027)"
DESC = "COBRA or the Marketplace? How early retirees in NC keep premiums down by managing taxable income, what a 64-year-old really pays in 2027, the subsidy cliff that can cost a couple $22,000 to $46,000 a year, and how to hand off to Medicare without a gap or a penalty."
CRUMBS = [("/", "Home"), ("/questions/", "Common Questions"), (None, "Retiring before 65 in NC")]

FAQ = [
    ("Should I take COBRA or go to the Marketplace when I retire?",
     "Compare two numbers: your COBRA premium (the full employer rate plus 2%) and your Marketplace premium after the credit, which depends on the income you will have in retirement, not what you earned while working. If your retirement MAGI is under 400% of the poverty level, the Marketplace is almost always cheaper. COBRA makes sense when you are mid-treatment with doctors who are not in Marketplace networks, or when you retire late in the year and have already met your deductible. Decide at retirement: once you elect COBRA you generally cannot switch to the Marketplace until Open Enrollment or until COBRA runs out."),
    ("Do my savings or home equity affect the subsidy?",
     "No. The premium tax credit is based only on modified adjusted gross income. A retiree with $1 million in a brokerage account and $50,000 of income qualifies the same as anyone else with $50,000 of income. What does count is the income those assets generate: dividends, interest (including tax-exempt interest), capital gains you realize, and withdrawals from traditional IRAs and 401(k)s."),
    ("Do Social Security benefits count as income?",
     "Yes, all of them, including the part that is not taxed. Social Security is added back into modified adjusted gross income for Marketplace purposes. Many early retirees delay claiming until 65 or later partly for this reason."),
    ("What happens to my Marketplace plan when I turn 65?",
     "You enroll in Medicare during your 7-month initial enrollment period (the three months before your birthday month, the month itself, and three months after). Once you are eligible for premium-free Part A you can no longer receive a premium tax credit, so you cancel the Marketplace plan effective the day Medicare starts. A Marketplace plan is not employer coverage, so it does not let you delay Part B without a lifetime penalty."),
    ("My spouse is younger. What happens to her coverage when I go on Medicare?",
     "She stays on the Marketplace plan as a household of two with one person enrolled. The credit is recalculated on your joint income for her premium alone. Report the change to the Marketplace the month you enroll in Medicare."),
    ("Can I keep contributing to an HSA?",
     "Until the month your Medicare coverage begins. If you delay Medicare past 65 and later enroll while claiming Social Security, Part A is backdated up to six months, and HSA contributions during those months become excess contributions. Stop contributing six months before you plan to enroll in that case."),
    ("What if my income is very low in early retirement?",
     "North Carolina's Medicaid expansion covers adults under about 138% of the poverty level ($22,025 for one, $29,863 for a couple) with no premium and no asset test. A retiree living on savings with little taxable income may be routed there. If you would rather have a Marketplace plan, realizing enough income (a Roth conversion, for instance) to exceed the line is a legitimate choice to discuss with your tax adviser."),
]

body = f"""
<h1>Retiring Before 65 in North Carolina: Bridging to Medicare With a Marketplace Plan</h1>
{byline("11 minute read")}

<p class="lede">The years between leaving a job and turning 65 are the most expensive years to buy health insurance, and the ones where good planning pays off most. A 64-year-old in Carteret County pays three times what a 21-year-old pays for the same plan, but with the right income strategy the premium can fall to a few hundred dollars, or zero. This guide covers the COBRA-or-Marketplace decision, how the 2027 subsidy treats retirement income, the cliff that can cost a couple $22,000 to $46,000 a year depending on the county, and the hand-off to Medicare.</p>

<div class="takeaways">
<h2>Key takeaways</h2>
<ul>
<li><strong>Age rating is 3 to 1.</strong> In Carteret County the cheapest Bronze plan is $571 a month at 21 and $1,713 at 64; Gold runs $2,400 and up for a 64-year-old at full price.</li>
<li><strong>The subsidy looks at income, not wealth.</strong> IRA withdrawals, Roth conversions, capital gains, dividends and all of Social Security count. Roth withdrawals, HSA withdrawals and spending down cash do not.</li>
<li><strong>Keep MAGI under 400% of the poverty level</strong> ($63,840 single, $86,560 couple) and the same 64-year-old's monthly premium after the credit is $0 for Bronze Basic and about $500 for Silver; a couple of 64 and 62 at $85,000 likewise pays $0 a month for Bronze Basic and about $700 for Silver, because the credit at that age is larger than the Bronze premium. Cross the line by a dollar and the premium is full price: a $21,900-a-year swing for one person, $46,200 for a couple. Those are eastern North Carolina numbers, the largest in the state. Where Ambetter sets the benchmark, as in Wake County, the cheapest Bronze costs the same person about $345 a month and the swing is about $9,800 ($22,500 for the couple); the benchmark Silver costs about $500 (single) or $700 (couple) everywhere.</li>
<li><strong>COBRA is rarely the better bridge</strong> unless your retirement income is over the line or you are mid-treatment with out-of-network doctors.</li>
<li><strong>Medicare at 65 ends the credit.</strong> Enroll in Parts A and B during the 7-month window, cancel the Marketplace plan the day Medicare starts, and stop HSA contributions in time.</li>
</ul>
</div>

<h2>Your three options when the employer plan ends</h2>
<p>Losing employer coverage, including by retiring, opens a 60-day special enrollment period for Marketplace coverage. In that window you can choose among:</p>
<ul>
<li><strong>COBRA</strong>: keep the employer plan for up to 18 months. The shock is the price: while you were working, your employer paid most of the premium (on average 83% for single coverage and 72% for family coverage, per KFF's 2025 employer survey); on COBRA you pay the entire premium plus a 2% administrative fee. For a couple that is typically $1,800 to $2,800 a month in 2027. No income test, same doctors, same deductible progress for the rest of the year.</li>
<li><strong>A Marketplace plan</strong>: priced by age and county, reduced by a premium tax credit based on your retirement income. Deductibles reset on January 1 and whenever you switch plans.</li>
<li><strong>A spouse's employer plan</strong>, if there is one; usually the cheapest option and it also blocks the Marketplace credit if it is affordable.</li>
</ul>
<p>The common mistake is electing COBRA because it is familiar, then discovering in February that a Marketplace plan would have cost a third as much. COBRA's one real advantage is timing: if you retire in October with your deductible met, three months of COBRA to year-end and a Marketplace plan from January 1 avoids paying two deductibles. Plan that switch during Open Enrollment (November 1 to January 15); voluntarily dropping COBRA mid-year does not create a special enrollment period, although COBRA running out does.</p>

<h2>What a 64-year-old pays in 2027</h2>
<p>These are real Carteret County prices on the Blue Care (HMO) network. Full price applies above 400% of the poverty level; the subsidized columns show what the same plans cost at incomes under the line.</p>

<div class="table-wrap">
<table class="data">
<caption>Monthly premiums, Carteret County, Blue Care network, 2027. Blue Advantage (PPO, nationwide network) is about 5.5% more here and 2.7% to 4.6% more in most of the state. Source: HealthCare.gov Marketplace API.</caption>
<thead><tr><th>Plan</th><th class="num">Single, 64, full price</th><th class="num">Single, 64, $60,000 income</th><th class="num">Couple 64 and 62, full price</th><th class="num">Couple, $85,000</th><th class="num">Couple, $50,000</th></tr></thead>
<tbody>
<tr><td>Bronze Basic</td><td class="num">$1,713</td><td class="num">$0</td><td class="num">$3,354</td><td class="num">$0</td><td class="num">$0</td></tr>
<tr><td>Bronze HSA Eligible Plus</td><td class="num">$1,845</td><td class="num">$19</td><td class="num">$3,611</td><td class="num">$0</td><td class="num">$0</td></tr>
<tr><td>Silver Preferred</td><td class="num">$2,319</td><td class="num">$493</td><td class="num">$4,539</td><td class="num">$687</td><td class="num">$295 (with CSR)</td></tr>
<tr><td>Silver Standard</td><td class="num">$2,337</td><td class="num">$511</td><td class="num">$4,575</td><td class="num">$723</td><td class="num">$331 (with CSR)</td></tr>
<tr><td>Gold Standard A</td><td class="num">$2,409</td><td class="num">$583</td><td class="num">$4,716</td><td class="num">$864</td><td class="num">$472</td></tr>
<tr><td>Gold All Copay A</td><td class="num">$2,441</td><td class="num">$615</td><td class="num">$4,780</td><td class="num">$928</td><td class="num">$536</td></tr>
</tbody>
</table>
</div>
<p>Read across the Silver Standard row: $2,337 at full price, $511 at $60,000 of income. The credit for a 64-year-old at that income is about $1,826 a month, $21,900 a year, and it disappears entirely at $63,841. For the couple the credit at $85,000 is about $3,852 a month, $46,200 a year, gone at $86,561. These are the largest cliffs in the tax code, and they fall on exactly the people most able to plan around them.</p>

<h3>The same household in other counties</h3>
<p>Carteret County is the expensive end of the state. The credit is the benchmark premium minus your expected contribution, and the contribution is the same in every county, so the benchmark Silver costs this household about $511 a month (single) or $723 (couple) wherever it lives. In the eastern counties where Blue Cross is the only insurer, the benchmark is expensive and the credit covers the whole Bronze premium. Where a cheaper Ambetter Silver plan sets the benchmark, the credit is smaller, Bronze is not free, and the cliff is about half to two-thirds as large:</p>
<div class="table-wrap">
<table class="data">
<caption>Cheapest Bronze plan (any insurer) per month after the credit, and yearly cost of crossing 400% of the poverty level, 2027: single, 64, at $60,000; couple, 64 and 62, at $85,000. Source: HealthCare.gov Marketplace API, retrieved November 10, 2026.</caption>
<thead><tr><th>County</th><th class="num">Cheapest Bronze, single</th><th class="num">Cliff, single</th><th class="num">Cheapest Bronze, couple</th><th class="num">Cliff, couple</th></tr></thead>
<tbody>
<tr><td>Carteret, Craven, Pitt, Pasquotank and 22 other eastern counties</td><td class="num">$0</td><td class="num">$21,600&ndash;$21,900</td><td class="num">$0</td><td class="num">$45,700&ndash;$46,200</td></tr>
<tr><td>Buncombe (Asheville)</td><td class="num">$283</td><td class="num">$13,500</td><td class="num">$277</td><td class="num">$29,700</td></tr>
<tr><td>New Hanover (Wilmington)</td><td class="num">$321</td><td class="num">$12,100</td><td class="num">$350</td><td class="num">$27,100</td></tr>
<tr><td>Mecklenburg (Charlotte)</td><td class="num">$232</td><td class="num">$11,500</td><td class="num">$177</td><td class="num">$25,800</td></tr>
<tr><td>Cumberland (Fayetteville)</td><td class="num">$328</td><td class="num">$11,400</td><td class="num">$365</td><td class="num">$25,700</td></tr>
<tr><td>Durham</td><td class="num">$333</td><td class="num">$10,300</td><td class="num">$374</td><td class="num">$23,500</td></tr>
<tr><td>Forsyth (Winston-Salem)</td><td class="num">$310</td><td class="num">$10,100</td><td class="num">$329</td><td class="num">$23,000</td></tr>
<tr><td>Wake (Raleigh)</td><td class="num">$345</td><td class="num">$9,800</td><td class="num">$397</td><td class="num">$22,500</td></tr>
<tr><td>Guilford (Greensboro)</td><td class="num">$337</td><td class="num">$9,600</td><td class="num">$382</td><td class="num">$22,000</td></tr>
</tbody>
</table>
</div>
<p>A $0 Bronze plan is available to this single 64-year-old in 33 counties and to the couple in 36; elsewhere the cheapest Bronze runs about $80 to $345 a month for the single person. Your <a href="/counties/">county guide</a> has the benchmark and every plan's price.</p>

<h2>What counts as income in retirement</h2>
<p>The Marketplace uses modified adjusted gross income: your adjusted gross income plus tax-exempt interest, the untaxed part of Social Security, and excluded foreign income. For a retiree that means:</p>
<div class="table-wrap">
<table class="data">
<thead><tr><th>Counts toward MAGI</th><th>Does not count</th></tr></thead>
<tbody>
<tr><td>Withdrawals from traditional IRAs, 401(k)s, 403(b)s</td><td>Withdrawals from Roth IRAs and Roth 401(k)s (after 59&frac12; and 5 years)</td></tr>
<tr><td>Roth conversions, in the year converted</td><td>Spending from checking, savings or a brokerage account's principal</td></tr>
<tr><td>Pension payments</td><td>HSA withdrawals for medical expenses</td></tr>
<tr><td>Social Security, including the untaxed portion</td><td>Return of basis on annuity payments; life insurance cash value loans</td></tr>
<tr><td>Interest, including municipal bond interest; dividends; realized capital gains</td><td>Unrealized gains; the excluded gain on selling your home ($250,000 single, $500,000 couple)</td></tr>
<tr><td>Rental and part-time or consulting income (net of expenses)</td><td>Gifts and inheritances</td></tr>
</tbody>
</table>
</div>

<h2>Income planning for the bridge years</h2>
<p>Because you choose which accounts to draw from, you largely choose your MAGI. The standard playbook for the years before 65:</p>
<ol>
<li><strong>Spend from cash and taxable accounts first.</strong> Only the gain portion of a brokerage sale is income, and you can pick lots with little gain.</li>
<li><strong>Keep traditional IRA withdrawals and Roth conversions small,</strong> or do them before you retire or after you are on Medicare. A $50,000 Roth conversion in a bridge year can cost a couple $22,000 to $46,000 of premium credit, depending on the county, on top of the income tax.</li>
<li><strong>Delay Social Security</strong> if you can. Every dollar of benefit counts toward MAGI, and delaying also increases the benefit permanently.</li>
<li><strong>Use the 250% line as a second target.</strong> Under $39,900 (single) or $54,100 (couple) a Silver plan comes with cost-sharing reductions that cut the deductible to a few hundred dollars. The couple at $50,000 above pays $295 a month for Silver Preferred with a $4,000 family deductible instead of $5,400.</li>
<li><strong>Do not aim too low.</strong> Under 138% of the poverty level ($22,025 single, $29,863 couple) the Marketplace sends you to NC Medicaid. That is free coverage with a narrower network; if you prefer a Marketplace plan, realize enough income to clear the line.</li>
<li><strong>Fund an HSA on a Bronze plan.</strong> Every 2027 Bronze plan is HSA-eligible. A couple over 55 can contribute $11,000 ($9,000 plus two $1,000 catch-ups, which requires two HSAs), reducing MAGI by the same amount, and the money can later pay Medicare premiums tax-free.</li>
</ol>

<div class="callout caution">
<p><strong>The repayment cap is gone.</strong> Through 2025, a retiree who underestimated income repaid at most $1,500 to $3,500 of excess credit at tax time. Starting with the 2026 tax year, the full excess is repaid. A year-end capital gains distribution from a mutual fund, a required minimum distribution from an inherited IRA, or a Roth conversion done without checking the line can trigger repayment of the entire year's credit. Review MAGI in October, before the fund distributions, and report changes to the Marketplace.</p>
</div>

<h2>Which plan for the bridge years</h2>
<ul>
<li><strong>Income under 250%:</strong> Silver Preferred or Silver Standard with cost-sharing reductions. The low deductible matters more at 62 than at 32.</li>
<li><strong>Income between 250% and 400%, healthy, with savings:</strong> Bronze Basic or Bronze HSA Eligible Plus, with the HSA funded. In Carteret County they cost $0 to $19 a month at this income; where Ambetter sets the benchmark, the cheapest Bronze is closer to $230 to $350 (see the table above). You are self-insuring the $7,000 to $8,700 deductible from money you would have spent on premiums.</li>
<li><strong>Taking brand-name or specialty drugs, or expecting a joint replacement:</strong> Gold Standard A ($8,600 out-of-pocket maximum, $250 specialty copay) or Gold All Copay A ($2,500 per hospital stay). See <a href="/questions/bronze-vs-silver-medications/">Bronze vs. Silver when you take medications</a>.</li>
<li><strong>Travelers, and anyone who wants access to nationally known specialists:</strong> the Blue Advantage version of any design, for nationwide in-network doctors at 2.7% to 5.5% more than Blue Care, depending on the area (more than that over Blue Cross's narrower networks; see <a href="/questions/blue-care-vs-blue-advantage/">Blue Care vs. Blue Advantage</a>). If you travel often, or want the option of being seen at Mayo Clinic, Memorial Sloan Kettering, MD Anderson or Johns Hopkins, those providers need to be in network, and only Blue Advantage puts them there. Blue Care covers only emergencies outside North Carolina. In the Triangle, Blue Advantage is not sold on HealthCare.gov; a Blue Cross NC PPO plan is available there off-exchange through a licensed agent like us, at full price, because off-exchange plans get no premium tax credit.</li>
<li><strong>Over 400% and unable to get under:</strong> compare off-exchange Blue Cross plans sold through agents (same prices, a few additional designs) and consider whether a part-time business with a SEP-IRA could bring MAGI down; our <a href="/questions/self-employed-north-carolina-2027/">self-employed guide</a> covers the levers.</li>
</ul>

<h2>The hand-off to Medicare</h2>
<ol>
<li><strong>Three months before your 65th birthday month,</strong> apply for Medicare Parts A and B at ssa.gov (or by phone). Your initial enrollment period runs seven months: three before, the birthday month, three after. Enrolling in the first three months starts coverage on the first day of your birthday month; enrolling later starts it the first of the following month, so apply early.</li>
<li><strong>Choose how to fill the gaps</strong>: Original Medicare with a Medigap policy and a Part D drug plan, or a Medicare Advantage plan. Medigap has a guaranteed-issue window of six months from your Part B start date; after that, insurers in North Carolina can underwrite you.</li>
<li><strong>Cancel the Marketplace plan</strong> effective the last day of the month before Medicare starts, and no later. Medicare always begins on the first of a month, whatever your birthday: enroll during the three months before your birthday month and Part A and B start on the first day of that month (if your birthday is the 1st, they start on the first day of the month before). So a July 18 birthday means Medicare on July 1 and a Marketplace end date of June 30. Set that end date with the Marketplace at least two weeks ahead; there is no gap and no overlap. Once you are eligible for premium-free Part A, the premium tax credit stops; a Marketplace plan kept alongside Medicare is full price and pays second.</li>
<li><strong>If your spouse is younger,</strong> update the Marketplace application to remove you. Her credit is recalculated for a household of two with one enrolled.</li>
<li><strong>Stop HSA contributions</strong> the month Medicare begins. If you delay Part A past 65 and later claim Social Security, Part A is backdated up to six months, so stop six months ahead in that case.</li>
<li><strong>Do not rely on the Marketplace plan to delay Part B.</strong> Only current employer coverage (yours or a spouse's, from an employer with 20 or more workers) lets you delay Part B without a 10%-per-year lifetime penalty.</li>
</ol>


{cta("See what your bridge-year plan would cost", "Enter your county, ages and the income you expect in retirement and our Covanu tool shows every plan with the credit applied, flags the 250% and 400% lines, and checks your medications against each plan's drug list. Then book a call and we will map the years to 65 together. Our help is free.")}

{author_box()}

{sources([
    '<a href="https://www.healthcare.gov/developers/" target="_blank" rel="noopener">HealthCare.gov Marketplace API</a>: 2027 premiums for the Carteret County examples, retrieved ' + UPDATED_H + '; other counties retrieved November 10, 2026.',
    '<a href="https://aspe.hhs.gov/topics/poverty-economic-mobility/poverty-guidelines" target="_blank" rel="noopener">HHS 2026 Poverty Guidelines</a>.',
    '<a href="https://kff.org/affordable-care-act/9-things-to-watch-for-the-2027-aca-open-enrollment-period/" target="_blank" rel="noopener">KFF, 9 Things to Watch for the 2027 ACA Open Enrollment Period</a>: expiration of enhanced credits and elimination of repayment caps.',
    '<a href="https://www.healthcare.gov/medicare/" target="_blank" rel="noopener">HealthCare.gov: Medicare and the Marketplace</a>.',
    '<a href="https://www.medicare.gov/basics/get-started-with-medicare/sign-up/when-does-medicare-coverage-start" target="_blank" rel="noopener">Medicare.gov: initial enrollment period and coverage start dates</a>.',
    '<a href="https://www.healthcare.gov/unemployed/cobra-coverage/" target="_blank" rel="noopener">HealthCare.gov: COBRA and the Marketplace</a>.',
    '<a href="https://www.kff.org/health-costs/report/2025-employer-health-benefits-survey/" target="_blank" rel="noopener">KFF 2025 Employer Health Benefits Survey</a> (employer share of premiums).',
    'IRS Rev. Proc. 2026-24 (2027 HSA limits); IRS Notice 2026-5 (Bronze Marketplace plans treated as HDHPs).',
])}
"""

page(PATH, TITLE, DESC, "/questions/", CRUMBS, body, faq=FAQ, reading="11 minute read")
