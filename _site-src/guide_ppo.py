from fbsite import *

PATH = "/questions/blue-care-vs-blue-advantage-eastern-nc/"
TITLE = "Blue Care vs. Blue Advantage in Eastern NC: Is the PPO Worth 5.5% More? (2027)"
DESC = "In 21 eastern North Carolina counties every Blue Cross plan comes as a Blue Care HMO or a Blue Advantage PPO with identical benefits. What the PPO actually buys you (nationwide network, not real out-of-network coverage), what it costs by age, and who should pay for it: snowbirds, Virginia hospital users, parents of college students, cruisers."
CRUMBS = [("/", "Home"), ("/questions/", "Common Questions"), (None, "Blue Care vs. Blue Advantage")]

FAQ = [
    ("Are the benefits really identical?",
     "Yes. For each of the 10 plan designs sold in these counties, the Blue Care and Blue Advantage versions have the same deductible, out-of-pocket maximum, copays, coinsurance, drug tiers and HSA eligibility. The HealthCare.gov data for all 20 plans differs only in network, premium and the out-of-network rows."),
    ("Does Blue Care cover me if I get sick on vacation?",
     "Emergency care, yes, anywhere in the United States, at the in-network cost sharing. Urgent care and follow-up visits outside North Carolina are not covered on Blue Care. On Blue Advantage they are in network at any provider that participates with the local Blue Cross plan."),
    ("Does Blue Advantage pay for any doctor I want?",
     "Not in a useful way. Out-of-network care on Blue Advantage is 50% to 80% coinsurance after the deductible with no out-of-network out-of-pocket maximum, and the plan pays its share of an allowed amount, not the provider's bill. Treat it as a nationwide in-network plan. The question to ask about any doctor is whether they are in the Blue Advantage (BlueCard) network, not whether they will take out-of-network patients."),
    ("I live in Currituck and use Sentara in Norfolk. Which plan?",
     "Blue Advantage. Norfolk and Chesapeake hospitals are outside North Carolina, so on Blue Care only emergencies there are covered. On Blue Advantage, providers that participate with Anthem Blue Cross in Virginia are in network through BlueCard. Confirm the specific hospital and doctors in the Blue Advantage directory before enrolling."),
    ("Do I need a referral on the HMO?",
     "No. Blue Care does not require referrals to see a specialist, and you do not have to pick a primary care doctor. In that respect it works like a PPO within North Carolina."),
    ("Can I switch from Blue Care to Blue Advantage mid-year?",
     "Only with a qualifying life event (a move, marriage, loss of other coverage). Otherwise you choose during Open Enrollment, November 1 to January 15, for the coming year. If you are planning to spend next winter out of state, decide now."),
    ("Does the PPO cost more if I get a subsidy?",
     "The premium tax credit is a fixed dollar amount, so the PPO costs the same extra dollars whether or not you are subsidized: about 5.5% of the full premium. For households whose credit already exceeds the Bronze premium, that extra can be partly or fully absorbed; a family of four at $90,000 pays $0 for Blue Care Bronze Basic and about $1 for Blue Advantage Bronze Standard."),
]

body = f"""
<h1>Blue Care vs. Blue Advantage in Eastern NC: Is the PPO Worth 5.5% More?</h1>
{byline("7 minute read")}

<p class="lede">In the 21 eastern North Carolina counties where Blue Cross NC is the only Marketplace carrier, every plan comes in two versions with identical benefits: <strong>Blue Care</strong>, an HMO with a statewide network, and <strong>Blue Advantage</strong>, a PPO with a nationwide network that costs about 5.5% more. Because nothing else differs, this is the cleanest decision in the whole process, and the one people most often get wrong, in both directions.</p>

<div class="takeaways">
<h2>Key takeaways</h2>
<ul>
<li><strong>Same deductible, copays, drug tiers and out-of-pocket maximum.</strong> You are paying 5.5% for the network, nothing else.</li>
<li><strong>What the 5.5% buys is nationwide in-network access</strong> through BlueCard, not meaningful out-of-network coverage. Blue Advantage's out-of-network benefit is 50&ndash;80% coinsurance after the deductible with no cap.</li>
<li><strong>Blue Care already covers emergencies anywhere</strong> in the country and needs no referrals. If you live in North Carolina year-round and your doctors are here, it is the same plan for less.</li>
<li><strong>Pay for the PPO if</strong> you winter out of state, have a student at an out-of-state college, use a Virginia hospital (Albemarle counties), cruise the Intracoastal, or want a specific out-of-state hospital.</li>
<li><strong>The cost is $45&ndash;$64 a month at 45 and $84&ndash;$120 at 60</strong> at full price. With a large subsidy it can be a few dollars.</li>
</ul>
</div>

<h2>What is actually different</h2>
<p>Here is everything the HealthCare.gov plan data shows as different between Blue Care Gold Standard A and Blue Advantage Gold Standard A. The other nine designs follow the same pattern.</p>
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

<h2>What it costs</h2>
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
<p>Over a year that is roughly $540 to $770 for a 45-year-old and $1,000 to $1,440 for a 60-year-old, per person. The family column shows the subsidy effect: a credit large enough to zero out Bronze absorbs the PPO premium too, but on Silver and Gold the extra dollars are the same as for anyone else.</p>

<h2>Who should pay for Blue Advantage</h2>
<ul>
<li><strong>Snowbirds and second-home owners.</strong> Three months in Florida or Arizona means three months in which only the emergency room is covered on Blue Care. Any ongoing condition, a prescription refill that needs a visit, physical therapy after a fall: all in network on Blue Advantage, all out of pocket on Blue Care.</li>
<li><strong>Albemarle counties that use Virginia hospitals.</strong> If you live in Currituck, Camden, Pasquotank, Gates or Perquimans and your cardiologist is at Sentara Norfolk or your hospital is Chesapeake Regional, those are out of state. Blue Advantage puts them in network through the Virginia Blue plan; Blue Care does not.</li>
<li><strong>Parents of out-of-state college students.</strong> The student's routine care near campus is in network on the PPO only. (Students at UNC, NC State, ECU, App State or any other North Carolina school are fine on Blue Care.)</li>
<li><strong>Cruisers and people who work on the water or the road.</strong> If you spend the season moving down the Intracoastal from Oriental or Beaufort, drive a truck, or consult in other states, you want in-network care wherever you stop.</li>
<li><strong>Anyone who wants a specific out-of-state hospital.</strong> MUSC in Charleston, Mayo, Johns Hopkins, MD Anderson. On Blue Advantage they are typically in network; on Blue Care they are out of network except for emergencies.</li>
</ul>

<h2>Who should keep the 5.5%</h2>
<ul>
<li><strong>You live here year-round and your doctors are in North Carolina.</strong> That describes most people on the coast and in the Albemarle counties east of the Virginia commuters. Blue Care's network already includes the state's major systems; check yours in the <a href="https://healthnav.bcbsnc.com/?ci=COMMERCIAL&network_id=6" target="_blank" rel="noopener">Blue Care directory</a>.</li>
<li><strong>Your travel is vacations, not residence.</strong> A week in the mountains or a cruise is an emergency-only situation, and emergencies are covered.</li>
<li><strong>You are buying the cheapest Bronze as catastrophic protection.</strong> The PPO's value is in routine out-of-state care; a $7,000-deductible plan is not where you will use much routine care anyway.</li>
</ul>

<h2>A two-question test</h2>
<ol>
<li><strong>Will I need a non-emergency doctor, hospital or pharmacy visit outside North Carolina in the next year, for myself or a dependent on the plan?</strong> If no, Blue Care.</li>
<li><strong>If yes, is the provider I would use in the Blue Advantage (BlueCard) network?</strong> Check the <a href="https://healthnav.bcbsnc.com/?ci=COMMERCIAL&network_id=3" target="_blank" rel="noopener">Blue Advantage directory</a>. If yes, Blue Advantage is worth the 5.5%. If no, the PPO's out-of-network benefit will not save you either; find an in-network alternative or reconsider.</li>
</ol>
<p>Make the network decision first, then choose the design (Bronze, Silver or Gold) on total cost using your medications; the county guides walk through that step for each of the 21 counties.</p>

{cta("Compare both networks with your numbers")}

{author_box()}

{sources([
    '<a href="https://www.healthcare.gov/developers/" target="_blank" rel="noopener">HealthCare.gov Marketplace API</a>: 2027 plan benefits, networks and premiums for the 21 counties, retrieved ' + UPDATED_H + '.',
    'Blue Cross NC provider directories: <a href="https://healthnav.bcbsnc.com/?ci=COMMERCIAL&network_id=6" target="_blank" rel="noopener">Blue Care</a>, <a href="https://healthnav.bcbsnc.com/?ci=COMMERCIAL&network_id=3" target="_blank" rel="noopener">Blue Advantage</a>.',
    '<a href="https://www.bcbs.com/bluecard" target="_blank" rel="noopener">Blue Cross Blue Shield Association: BlueCard program</a>.',
])}
"""

page(PATH, TITLE, DESC, "/questions/", CRUMBS, body, faq=FAQ, reading="7 minute read")
