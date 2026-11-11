from fbsite import *

PATH = "/questions/blue-care-vs-blue-advantage/"
TITLE = "Blue Care vs. Blue Advantage: Is Blue Cross NC's Nationwide PPO Worth It? (2027)"
DESC = "In 90 North Carolina counties Blue Cross NC sells each Marketplace plan on Blue Care, a statewide HMO, and on Blue Advantage, a nationwide PPO with identical benefits that costs 2.7% to 5.5% more depending on the county. What the PPO actually buys, what it costs where you live, how it compares with the cheaper Blue Home, Blue Local and Blue Value networks, and how to get a PPO in the Triangle."
CRUMBS = [("/", "Home"), ("/questions/", "Common Questions"), (None, "Blue Care vs. Blue Advantage")]

FAQ = [
    ("Are the benefits really identical?",
     "Yes. For each of the 10 plan designs Blue Cross NC sells on HealthCare.gov, the version on Blue Care, Blue Advantage, Blue Home, Blue Local or Blue Value has the same deductible, out-of-pocket maximum, copays, coinsurance, drug tiers and HSA eligibility. The HealthCare.gov data differs only in network, premium and the out-of-network rows. Around Charlotte, Winston-Salem and Greensboro, Blue Home and Blue Local sell six of the ten designs; Blue Care and Blue Advantage sell all ten."),
    ("Does Blue Care cover me if I get sick on vacation?",
     "Emergency care, yes, anywhere in the United States, at the in-network cost sharing. Urgent care and follow-up visits outside North Carolina are not covered on Blue Care. On Blue Advantage they are in network at any provider that participates with the local Blue Cross plan."),
    ("Does Blue Advantage pay for any doctor I want?",
     "Not in a useful way. Out-of-network care on Blue Advantage is 50% to 80% coinsurance after the deductible with no out-of-network out-of-pocket maximum, and the plan pays its share of an allowed amount, not the provider's bill. Treat it as a nationwide in-network plan. The question to ask about any doctor is whether they are in the Blue Advantage (BlueCard) network, not whether they will take out-of-network patients."),
    ("I live in Currituck and use Sentara in Norfolk. Which plan?",
     "Blue Advantage. Norfolk and Chesapeake hospitals are outside North Carolina, so on Blue Care only emergencies there are covered. On Blue Advantage, providers that participate with Anthem Blue Cross in Virginia are in network through BlueCard. Confirm the specific hospital and doctors in the Blue Advantage directory before enrolling."),
    ("Do I need a referral on the HMO?",
     "No. Blue Care does not require referrals to see a specialist, and you do not have to pick a primary care doctor. In that respect it works like a PPO within North Carolina."),
    ("Can I get a PPO in Raleigh or Durham?",
     "Not on HealthCare.gov. In the 10 Triangle counties Blue Cross's only Marketplace network for 2027 is Blue Home with UNC Health Alliance, and the other insurers sell HMOs. A Blue Cross NC PPO plan is available there off-exchange, through licensed agents like us. Off-exchange plans get no premium tax credit, so you pay full price; it usually makes sense only above 400% of the poverty level, or when a nationwide network is worth more to you than the credit."),
    ("Can I switch from Blue Care to Blue Advantage mid-year?",
     "Only with a qualifying life event (a move, marriage, loss of other coverage). Otherwise you choose during Open Enrollment, November 1 to January 15, for the coming year. If you are planning to spend next winter out of state, decide now."),
    ("My child's college offers a student health plan. Does that change the decision?",
     "It can. Most universities sell a student health insurance plan (SHIP), typically $2,000 to $4,000 a year, built around the campus health center and usually with a nationwide network for care away from school. If the student is the only reason you would buy Blue Advantage, compare the two: the PPO upgrade adds 2.7% to 5.5% to every family member's premium for the whole year (20% or more if the alternative is a narrower network), while a SHIP covers just the student. For a family of four on Gold Standard A the upgrade from Blue Care runs about $1,150 to $1,350 a year in most of the state, $1,800 in the mountains and $2,200 on the coast, so a SHIP can be the cheaper way to cover an out-of-state student while the rest of the family stays on Blue Care. Check that the SHIP is ACA-compliant (most are), what it covers during summers at home, and whether it is required (some schools require proof of coverage and charge for the SHIP unless you waive it). Children can stay on your Marketplace plan until 26 either way."),
    ("Does the PPO cost more if I get a subsidy?",
     "The premium tax credit is a fixed dollar amount, so the PPO costs the same extra dollars whether or not you are subsidized: 2.7% to 5.5% of the full premium, depending on the area. For households whose credit already exceeds the Bronze premium, that extra can be partly or fully absorbed; in Carteret County a family of four at $90,000 pays $0 for Blue Care Bronze Standard and about $1 for Blue Advantage Bronze Standard."),
]

body = f"""
<h1>Blue Care vs. Blue Advantage: Is Blue Cross NC's Nationwide PPO Worth It?</h1>
{byline("9 minute read")}

<p class="lede">In 90 of North Carolina's 100 counties, every Blue Cross NC Marketplace plan comes in two versions with identical benefits: <strong>Blue Care</strong>, an HMO with a statewide network, and <strong>Blue Advantage</strong>, a PPO with a nationwide network that costs 2.7% to 5.5% more, depending on where you live. Around Charlotte, the Triad, Hickory, Gastonia and Wilmington, Blue Cross adds cheaper versions on narrower networks, and in the Triangle it sells only one of those. Because the benefits do not change, this is the cleanest decision in the whole process, and the one people most often get wrong, in both directions.</p>

<div class="takeaways">
<h2>Key takeaways</h2>
<ul>
<li><strong>Same deductible, copays, drug tiers and out-of-pocket maximum</strong> for each plan design, whichever Blue Cross network it is sold on. You are paying for the network, nothing else.</li>
<li><strong>What Blue Advantage buys is nationwide in-network access</strong> through BlueCard, not meaningful out-of-network coverage. Its out-of-network benefit is 50&ndash;80% coinsurance after the deductible with no cap.</li>
<li><strong>Blue Care already covers emergencies anywhere</strong> in the country and needs no referrals. If you live in North Carolina year-round and your doctors are here, it is the same plan for less.</li>
<li><strong>The PPO's price depends on where you live:</strong> 5.2&ndash;5.5% over Blue Care on the coast, 4.4&ndash;4.6% in the mountains and 2.7&ndash;3.4% everywhere else it is sold. Where Blue Cross also sells Blue Home, Blue Local or Blue Value, those cost 13&ndash;33% less than Blue Care, and the PPO costs 20&ndash;53% more than they do.</li>
<li><strong>Pay for the PPO if</strong> you winter out of state, have a student at an out-of-state college, use a hospital across the state line, work on the road or the water, or want a specific out-of-state hospital.</li>
<li><strong>In the Triangle there is no Blue Advantage on HealthCare.gov.</strong> A Blue Cross NC PPO is available there only off-exchange, through a licensed agent like us, and off-exchange plans get no premium tax credit.</li>
</ul>
</div>

<h2>What is actually different</h2>
<p>Here is everything the HealthCare.gov plan data shows as different between Blue Care Gold Standard A and Blue Advantage Gold Standard A in Carteret County. The other nine designs, and every other county where both networks are sold, follow the same pattern; only the premiums change.</p>
<div class="table-wrap">
<table class="data">
<caption>Blue Cross NC Gold Standard A, 2027, Carteret County rating area. Source: HealthCare.gov Marketplace API.</caption>
<thead><tr><th></th><th>Blue Care (HMO)</th><th>Blue Advantage (PPO)</th></tr></thead>
<tbody>
<tr><td>Premium, age 45, full price</td><td class="num">$1,160</td><td class="num">$1,220</td></tr>
<tr><td>Deductible / out-of-pocket max</td><td>$2,500 / $8,600</td><td>$2,500 / $8,600</td></tr>
<tr><td>Primary care / specialist</td><td>$30 / $60</td><td>$30 / $60</td></tr>
<tr><td>Generic / preferred brand / specialty drug</td><td>$15 / $30 / $250</td><td>$15 / $30 / $250</td></tr>
<tr><td>Hospital stay (in network)</td><td>25% after deductible</td><td>25% after deductible</td></tr>
<tr><td>In-network area</td><td>North Carolina (Blue Care network)</td><td>North Carolina plus every state (BlueCard)</td></tr>
<tr><td>Emergency room out of state</td><td>Covered, 25% after deductible</td><td>Covered, 25% after deductible</td></tr>
<tr><td>Doctor visit out of network</td><td>Not covered</td><td>55% coinsurance after deductible</td></tr>
<tr><td>Hospital stay out of network</td><td>Not covered</td><td>55% coinsurance after deductible</td></tr>
<tr><td>Out-of-network out-of-pocket maximum</td><td>None (not covered)</td><td>None listed</td></tr>
<tr><td>Referral needed for specialists</td><td>No</td><td>No</td></tr>
</tbody>
</table>
</div>
<p>Two rows deserve emphasis. Blue Care covers the emergency room anywhere, so a heart attack in Florida is handled the same on either plan. And Blue Advantage's out-of-network rows are poor enough that they should not drive the decision: 55% coinsurance of an allowed amount, after the deductible, with no ceiling, is close to being uninsured. The PPO is worth buying for its in-network map, not its out-of-network benefit.</p>

<h2>What it costs where you live</h2>
<p>Blue Advantage's premium is a fixed percentage above the same design on Blue Care, and the percentage is set by rating area. The differences below are full-price premiums; a premium tax credit does not shrink them, because the credit is the same dollar amount whichever network you pick.</p>
<div class="table-wrap">
<table class="data">
<caption>Blue Advantage minus Blue Care, same design, full-price monthly premium, 2027. Ranges cover the 10 plan designs. Source: HealthCare.gov Marketplace API, all 100 counties.</caption>
<thead><tr><th>Rating area</th><th class="num">Counties</th><th>Blue Advantage costs</th><th class="num">Extra per month, age 45</th><th class="num">Extra per month, age 60</th></tr></thead>
<tbody>
<tr><td>12: Albemarle and the northeast (Elizabeth City, Roanoke Rapids)</td><td class="num">11</td><td>5.2&ndash;5.5% more</td><td class="num">$44&ndash;$63</td><td class="num">$82&ndash;$119</td></tr>
<tr><td>16: Crystal Coast, New Bern, Kinston, Outer Banks</td><td class="num">10</td><td>5.2&ndash;5.5% more</td><td class="num">$44&ndash;$64</td><td class="num">$83&ndash;$120</td></tr>
<tr><td>15: Wilmington and Jacksonville</td><td class="num">6</td><td>5.2&ndash;5.5% more</td><td class="num">$44&ndash;$64</td><td class="num">$83&ndash;$120</td></tr>
<tr><td>1: Asheville and the mountains</td><td class="num">17</td><td>4.4&ndash;4.6% more</td><td class="num">$36&ndash;$53</td><td class="num">$68&ndash;$99</td></tr>
<tr><td>14: Greenville, Rocky Mount, Wilson, Goldsboro</td><td class="num">6</td><td>3.2&ndash;3.4% more</td><td class="num">$27&ndash;$40</td><td class="num">$51&ndash;$76</td></tr>
<tr><td>2: Hickory, Morganton, Statesville</td><td class="num">5</td><td>2.9&ndash;3.2% more</td><td class="num">$25&ndash;$38</td><td class="num">$47&ndash;$71</td></tr>
<tr><td>3: Boone and the High Country</td><td class="num">4</td><td>2.9&ndash;3.2% more</td><td class="num">$25&ndash;$37</td><td class="num">$47&ndash;$70</td></tr>
<tr><td>4: Charlotte</td><td class="num">6</td><td>2.9&ndash;3.2% more</td><td class="num">$26&ndash;$38</td><td class="num">$48&ndash;$72</td></tr>
<tr><td>5: Gastonia and Shelby</td><td class="num">3</td><td>2.9&ndash;3.2% more</td><td class="num">$27&ndash;$40</td><td class="num">$50&ndash;$75</td></tr>
<tr><td>6: Winston-Salem</td><td class="num">6</td><td>2.9&ndash;3.2% more</td><td class="num">$24&ndash;$37</td><td class="num">$46&ndash;$69</td></tr>
<tr><td>7: Greensboro and High Point</td><td class="num">3</td><td>2.9&ndash;3.2% more</td><td class="num">$23&ndash;$35</td><td class="num">$44&ndash;$66</td></tr>
<tr><td>8: Pinehurst and the Sandhills</td><td class="num">2</td><td>2.9&ndash;3.2% more</td><td class="num">$25&ndash;$37</td><td class="num">$46&ndash;$69</td></tr>
<tr><td>10: Oxford and Henderson</td><td class="num">3</td><td>2.9&ndash;3.2% more</td><td class="num">$26&ndash;$39</td><td class="num">$49&ndash;$73</td></tr>
<tr><td>9: Fayetteville and Lumberton</td><td class="num">8</td><td>2.7&ndash;2.9% more</td><td class="num">$23&ndash;$35</td><td class="num">$44&ndash;$65</td></tr>
<tr><td>11 and 13: the Triangle (Raleigh, Durham, Chapel Hill, Burlington)</td><td class="num">10</td><td>Not sold on HealthCare.gov</td><td class="num">&ndash;</td><td class="num">&ndash;</td></tr>
</tbody>
</table>
</div>
<p>Over a year that is roughly $280 to $770 for a 45-year-old and $530 to $1,440 for a 60-year-old, per person, depending on the area and the design. Your <a href="/counties/">county guide</a> shows the exact price of every plan on every network sold there.</p>

<h3>Example: by design and age in Carteret County</h3>
<div class="table-wrap">
<table class="data">
<caption>Monthly premium difference, Blue Advantage minus Blue Care, same design, full price, 2027, Carteret County rating area. Albemarle-area counties (rating area 12) are about 1% lower on both.</caption>
<thead><tr><th>Design</th><th class="num">Age 30</th><th class="num">Age 45</th><th class="num">Age 60</th><th class="num">Family of four, $90,000, after subsidy</th></tr></thead>
<tbody>
<tr><td>Bronze Basic</td><td class="num">+$35</td><td class="num">+$45</td><td class="num">+$84</td><td class="num">$0 vs $0</td></tr>
<tr><td>Bronze Standard</td><td class="num">+$35</td><td class="num">+$44</td><td class="num">+$83</td><td class="num">$0 vs $1</td></tr>
<tr><td>Silver Standard</td><td class="num">+$46</td><td class="num">+$59</td><td class="num">+$110</td><td class="num">$702 vs $878</td></tr>
<tr><td>Gold Standard A</td><td class="num">+$48</td><td class="num">+$61</td><td class="num">+$114</td><td class="num">$806 vs $988</td></tr>
<tr><td>Gold All Copay A</td><td class="num">+$50</td><td class="num">+$64</td><td class="num">+$120</td><td class="num">$853 vs $1,044</td></tr>
</tbody>
</table>
</div>
<p>The family column shows the subsidy effect: a credit large enough to zero out Bronze absorbs the PPO premium too, but on Silver and Gold the extra dollars are the same as for anyone else.</p>

<h2>If your county also sells Blue Home, Blue Local or Blue Value</h2>
<p>In 31 counties Blue Cross sells one or two narrower networks alongside Blue Care and Blue Advantage. They carry the same plan designs and benefits for 13% to 33% less than Blue Care because they include fewer doctors and hospitals: Blue Home and Blue Local are each built around one health system's hospitals and doctors and cover out-of-network care only in emergencies, and Blue Value is a narrower statewide network whose out-of-network benefit is thin. Around Charlotte, Winston-Salem and Greensboro, Blue Home and Blue Local sell six of the ten designs (not Bronze Complete, Bronze HSA Eligible Plus, Silver Choice A or Gold All Copay A).</p>
<div class="table-wrap">
<table class="data">
<caption>Narrower Blue Cross networks, 2027: full-price premium compared with the same design on Blue Care, and what Blue Advantage costs by comparison. Source: HealthCare.gov Marketplace API.</caption>
<thead><tr><th>Rating area</th><th>Network</th><th>Sold in</th><th>Compared with Blue Care</th><th>Blue Advantage costs</th></tr></thead>
<tbody>
<tr><td>2: Hickory, Morganton, Statesville</td><td>Blue Value</td><td>All 5 counties</td><td>15% less</td><td>21% more</td></tr>
<tr><td>3: Boone and the High Country</td><td>Blue Local with Atrium Health</td><td>Wilkes</td><td>21% less</td><td>31% more</td></tr>
<tr><td>4: Charlotte</td><td>Blue Local with Atrium Health</td><td>All 6 counties</td><td>15% less</td><td>22% more</td></tr>
<tr><td>4: Charlotte</td><td>Blue Home with Novant Health</td><td>Cabarrus, Mecklenburg, Rowan, Union</td><td>33% less</td><td>53% more</td></tr>
<tr><td>5: Gastonia and Shelby</td><td>Blue Local with Atrium Health</td><td>All 3 counties</td><td>15% less</td><td>22% more</td></tr>
<tr><td>5: Gastonia and Shelby</td><td>Blue Value</td><td>All 3 counties</td><td>21% less</td><td>31% more</td></tr>
<tr><td>6: Winston-Salem</td><td>Blue Local with Atrium Health</td><td>All but Surry</td><td>23% less</td><td>34&ndash;35% more</td></tr>
<tr><td>6: Winston-Salem</td><td>Blue Home with Novant Health</td><td>Davidson, Forsyth, Stokes, Yadkin</td><td>22% less</td><td>32% more</td></tr>
<tr><td>6: Winston-Salem</td><td>Blue Value</td><td>Surry</td><td>15% less</td><td>21% more</td></tr>
<tr><td>7: Greensboro and High Point</td><td>Blue Local with Atrium Health</td><td>Guilford, Randolph</td><td>25% less</td><td>38% more</td></tr>
<tr><td>7: Greensboro and High Point</td><td>Blue Home with Cone Health</td><td>All 3 counties</td><td>14% less</td><td>20% more</td></tr>
<tr><td>14: Greenville, Rocky Mount, Wilson, Goldsboro</td><td>Blue Home with UNC Health Alliance</td><td>Nash</td><td>18% less</td><td>26% more</td></tr>
<tr><td>15: Wilmington and Jacksonville</td><td>Blue Value</td><td>All 6 counties</td><td>13% less</td><td>21% more</td></tr>
<tr><td>11 and 13: the Triangle</td><td>Blue Home with UNC Health Alliance</td><td>All 10 counties</td><td>The only Blue Cross network on HealthCare.gov</td><td>Not sold</td></tr>
</tbody>
</table>
</div>
<p>Where a narrower network is sold, the decision has one more step. First check whether your doctors and hospital are in it; each county guide shows which of the area's hospitals every network includes. If they are, and your care stays in North Carolina, the narrower network is the same plan for less. If they are not, Blue Care is the statewide version, and Blue Advantage the nationwide one for the reasons below.</p>

<h2>In the Triangle: no PPO on HealthCare.gov</h2>
<p>In Wake, Durham, Orange, Johnston, Franklin, Chatham, Alamance, Lee, Person and Caswell counties (rating areas 11 and 13), Blue Cross sells only Blue Home with UNC Health Alliance on HealthCare.gov for 2027: no Blue Care and no Blue Advantage. The other insurers there sell HMOs, so no Marketplace plan in the Triangle has a nationwide network.</p>
<p>If you need one, a Blue Cross NC PPO plan is available in the Triangle off-exchange, sold directly by Blue Cross through licensed agents. It is not listed on HealthCare.gov, so you need an agent like us to enroll in it. The trade-off is the subsidy: the premium tax credit applies only to plans bought through HealthCare.gov, so an off-exchange plan is full price. It makes the most sense if your income is over 400% of the poverty level, where there is no credit anyway, or if a nationwide network is worth more to you than the credit.</p>

<h2>Who should pay for Blue Advantage</h2>
<ul>
<li><strong>Second-home owners.</strong> Three months in Florida or Arizona means three months in which only the emergency room is covered on Blue Care. Any ongoing condition, a prescription refill that needs a visit, physical therapy after a fall: all in network on Blue Advantage, all out of pocket on Blue Care.</li>
<li><strong>People who use a hospital across the state line.</strong> If you live in Currituck, Camden, Pasquotank, Gates or Perquimans and your cardiologist is at Sentara Norfolk or your hospital is Chesapeake Regional, those are out of state; so is a practice or hospital in Virginia, Tennessee, Georgia or South Carolina near any of North Carolina's borders. Blue Advantage puts them in network through that state's Blue plan; Blue Care does not.</li>
<li><strong>Parents of out-of-state college students.</strong> The student's routine care near campus is in network on the PPO only. (Students at UNC, NC State, ECU, App State or any other North Carolina school are fine on Blue Care's statewide network; on a narrower network such as Blue Home or Blue Local, check the network near campus.) Compare the PPO upgrade with the college's own student health plan, which covers just the student; see the question below.</li>
<li><strong>People who work on the road or the water.</strong> If you spend the season moving down the Intracoastal from Oriental or Beaufort, drive a truck, or consult in other states, you want in-network care wherever you stop.</li>
<li><strong>Anyone who wants a specific out-of-state hospital.</strong> MUSC in Charleston, Mayo, Johns Hopkins, MD Anderson. On Blue Advantage they are typically in network; on Blue Care they are out of network except for emergencies.</li>
</ul>

<h2>Who should keep the difference</h2>
<ul>
<li><strong>You live here year-round and your doctors are in North Carolina.</strong> That describes most people. Check your doctors in the <a href="https://healthnav.bcbsnc.com/?ci=COMMERCIAL&network_id=6" target="_blank" rel="noopener">Blue Care directory</a>; your county guide shows which of the area's hospitals each network includes.</li>
<li><strong>Your travel is vacations, not residence.</strong> A week in the mountains or a cruise is an emergency-only situation, and emergencies are covered.</li>
<li><strong>You are buying the cheapest Bronze as catastrophic protection.</strong> The PPO's value is in routine out-of-state care; a $7,000-deductible plan is not where you will use much routine care anyway.</li>
</ul>

<h2>A three-question test</h2>
<ol>
<li><strong>Where Blue Home, Blue Local or Blue Value is sold: are your doctors and hospital in it?</strong> If yes, and the answer to the next question is no, the narrower network is the cheapest way to buy the same plan.</li>
<li><strong>Will I need a non-emergency doctor, hospital or pharmacy visit outside North Carolina in the next year, for myself or a dependent on the plan?</strong> If no, Blue Care (or the narrower network).</li>
<li><strong>If yes, is the provider I would use in the Blue Advantage (BlueCard) network?</strong> Check the <a href="https://healthnav.bcbsnc.com/?ci=COMMERCIAL&network_id=3" target="_blank" rel="noopener">Blue Advantage directory</a>. If yes, Blue Advantage is worth the difference; in the Triangle, that means an off-exchange PPO through an agent. If no, the PPO's out-of-network benefit will not save you either; find an in-network alternative or reconsider.</li>
</ol>
<p>Make the network decision first, then choose the design (Bronze, Silver or Gold) on total cost using your medications; the county guides walk through that step county by county.</p>

{cta("Compare the networks with your numbers")}

{author_box()}

{sources([
    '<a href="https://www.healthcare.gov/developers/" target="_blank" rel="noopener">HealthCare.gov Marketplace API</a>: 2027 plan benefits, networks and premiums for all 100 North Carolina counties, retrieved November 5 and 10, 2026.',
    'Blue Cross NC provider directories: <a href="https://healthnav.bcbsnc.com/?ci=COMMERCIAL&network_id=6" target="_blank" rel="noopener">Blue Care</a>, <a href="https://healthnav.bcbsnc.com/?ci=COMMERCIAL&network_id=3" target="_blank" rel="noopener">Blue Advantage</a>.',
    '<a href="https://www.bcbs.com/bluecard" target="_blank" rel="noopener">Blue Cross Blue Shield Association: BlueCard program</a>.',
    '<a href="https://www.irs.gov/affordable-care-act/individuals-and-families/the-premium-tax-credit-the-basics" target="_blank" rel="noopener">IRS: The Premium Tax Credit, the basics</a> (the credit requires coverage bought through the Marketplace).',
])}
"""

page(PATH, TITLE, DESC, "/questions/", CRUMBS, body, faq=FAQ, reading="9 minute read")
