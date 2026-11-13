from fbsite import *

# Kurt's answer to "Are there cheaper options than an ACA plan?" (text supplied by Kurt, November 13, 2026).
# Facts checked November 13, 2026: the $12,000 per-person cap matches the highest 2027 out-of-pocket maximum in the
# HealthCare.gov Marketplace API data for North Carolina (zones_2027.json); NC DOI Bulletin 25-B-11 (August 29, 2025)
# keeps the federal short-term definition (3 months, 4 with renewal) in force in NC until a new federal rule is final.

PATH = "/questions/cheaper-alternatives-to-aca-plans/"
QUESTION = "Are there cheaper options than an ACA plan, and what do I give up?"
TITLE = "Cheaper Than an ACA Plan? Health Sharing, Short-Term and Indemnity Plans in NC, and What You Give Up (2027)"
DESC = ("Health care sharing plans, short-term plans, hospital indemnity plans and discount cards can cost a third of a Marketplace premium. "
        "What an ACA-qualified plan guarantees, what each alternative lacks under North Carolina rules, and five real stories.")
CRUMBS = [("/", "Home"), ("/questions/", "Common Questions"), (None, "Cheaper alternatives to ACA plans")]
DATE, DATE_H = "2026-11-13", "November 13, 2026"

NBC_SHARING = "https://www.nbcchicago.com/news/national-international/health-care-cost-sharing-ministries-maternity-childbirth/3630557/"
KFF_JUNK = "https://kffhealthnews.org/news/junk-insurance-plans-health-consumers-beware/"
SCRIPPS = "https://www.10news.com/us-news/family-feels-scammed-after-birth-isnt-covered-by-hospital-indemnity-insurance"
NBC_POPE = "https://www.aol.com/news/insurance-denied-800-000-drug-001716254.html"
DOI_BULLETIN = "https://www.ncdoi.gov/25-b-11-short-term-limited-duration-health-insurance-policies/open"


def story(title, text, source_name, source_url, good=False):
    cls = "story story-good" if good else "story"
    return (f'<div class="{cls}">\n<h3>{title}</h3>\n<p>{text}</p>\n'
            f'<p class="story-source">Source: <a href="{source_url}" target="_blank" rel="noopener">{source_name}</a></p>\n</div>')


body = f"""
<h1>{QUESTION}</h1>
{byline("7 minute read", DATE_H, None)}

<p class="lede">Yes, and the ads for them get louder every Open Enrollment: health care sharing plans, short-term plans, hospital indemnity or &ldquo;fixed indemnity&rdquo; plans, discount cards. Some cost a third of a Marketplace premium. The savings are real; so is what you give up. I don&rsquo;t sell these products, because selling them as a substitute for health insurance is, in my view, unethical. Here is what &ldquo;ACA-qualified&rdquo; actually means, so you can judge the alternatives yourself.</p>

<h2>What an ACA-qualified plan guarantees</h2>
<ul>
<li><strong>It covers the 10 essential health benefits.</strong> Hospital care, emergency care, doctor visits, prescriptions, maternity and newborn care, mental health, lab work, rehab, pediatric care and preventive care. Every plan, no exceptions.</li>
<li><strong>Your yearly cost has a ceiling.</strong> In 2027 you cannot be charged more than $12,000 per person ($24,000 per family) for covered, in-network care in a year, no matter what happens. After that the plan pays 100%.</li>
<li><strong>No pre-existing-condition games.</strong> The plan must take you, must cover conditions you already have, and cannot cancel you because you got sick.</li>
<li><strong>A referee.</strong> ACA plans are licensed by the NC Department of Insurance. If a claim is denied, you have the right to an outside review through the state&rsquo;s Smart NC program, and the decision binds the insurer. If the insurer fails, a state guaranty fund stands behind your claims.</li>
</ul>

<h2>What the alternatives are, and what each one lacks</h2>
<p><strong>Health care sharing plans (Medi-Share, Samaritan, Sedera, Zion, Liberty and others).</strong> Members send money in each month, and the plan decides which members&rsquo; bills get &ldquo;shared.&rdquo; It is not insurance, and the fine print says so. There is no legal obligation to pay, pregnancy and pre-existing conditions usually carry waiting periods or first-year exclusions, many have annual or lifetime caps, and if a plan runs out of money the bills stay with you. Some of these plans are faith-based and some are not; the rules are the same either way, and the NC Department of Insurance has said it has no authority over them.</p>
<p><strong>Short-term, limited-duration plans.</strong> These are real, state-licensed insurance, but they are sold outside the ACA rules, and in North Carolina they are limited to 3 months (4 with a renewal); the NC Department of Insurance confirmed in August 2025 that it will keep enforcing that limit even though the federal government has stopped. Within the term, the insurer can ask about your health, exclude anything pre-existing (often for 12 months, on a 4-month policy), skip prescriptions or maternity, and cap total benefits. Most have an out-of-pocket limit, but it resets every term, sits on top of a deductible that can run $10,000 or more, and does not apply to anything the plan excludes. One more thing the ads don&rsquo;t say: when a short-term plan ends, that does not qualify you for a Special Enrollment Period, because the government doesn&rsquo;t count it as real coverage. If you get sick on a short-term plan in February, you may have no insurance at all until the following January 1.</p>
<p><strong>Hospital indemnity and fixed indemnity plans.</strong> These pay you a flat amount, say $200 a day in the hospital, regardless of the bill. They are designed to sit on top of real insurance, not replace it. Sold alone, a six-day hospital stay that bills $140,000 pays you $1,200.</p>
<p><strong>Discount cards and &ldquo;MEC&rdquo; plans.</strong> Preventive-only or discount-only products that satisfy a technicality and almost nothing else.</p>

<h2>What happens when it goes wrong</h2>
<p>Each of the four stories below would have been prevented by an ACA plan.</p>

{story("Asheville-area couple&rsquo;s childbirth denied outright &mdash; Sedera (NBC News, Dec 2024)",
       "Rachel Kaplan and Andrew Sheffield joined Sedera for about $147 a month. Their first child was born in August 2023 after an induction, 40 hours of labor and a C-section. Sedera declined to share any of it, citing a rule on page 44 of its 49-page member guidelines: childbirth during the first year of membership is &ldquo;not shareable.&rdquo; The couple hadn&rsquo;t misstated anything; they simply hadn&rsquo;t found the sentence. They paid roughly $7,000 for the delivery and $2,800 for anesthesia themselves, still owe about $2,500, and are now uninsured.",
       "NBC News", NBC_SHARING)}

{story("Broker moved landscaper to short-term plans; lymphoma claims of $800,000+ denied &mdash; UnitedHealthcare / Golden Rule (KFF Health News/NPR, Dec 2020)",
       "Sam Bloechl, 31, ran a landscaping company and had a Marketplace plan until a broker moved him to a bundle of three-month short-term policies from UnitedHealthcare&rsquo;s Golden Rule to save money. A month later he was diagnosed with stage 4 non-Hodgkin lymphoma and needed a stem-cell transplant. He had no diagnosis and no symptoms he recognized when he bought the plan. What he didn&rsquo;t know is how these plans work: the medical underwriting happens after you get sick. The insurer went back through his records, found a chiropractor visit for back pain before the policy started, called the cancer a pre-existing condition, and denied more than $800,000 in claims. His appeals failed. He was treated only because his own company qualified for a small-group plan and the hospital wrote off the rest as charity care.",
       "KFF Health News", KFF_JUNK)}

{story("Family&rsquo;s prenatal and delivery bills never reimbursed after paperwork ran out the clock &mdash; Liberty HealthShare (NBC News, Dec 2024)",
       "Warren Walborn joined Liberty HealthShare on a friend&rsquo;s recommendation, &ldquo;looking for alternatives to not get killed on the premiums.&rdquo; When his wife became pregnant he did everything the plan asked: submitted every bill within Liberty&rsquo;s 180-day window and kept, in his words, &ldquo;fastidious records of all of these codes and everything.&rdquo; Liberty responded with requests for itemized charges, then more documentation, then more. When the back-and-forth ran past the 180-day limit, Liberty told him he was no longer eligible because the deadline had passed. He was never reimbursed for his wife&rsquo;s prenatal care or for the 2021 delivery of their daughter.",
       "NBC News", NBC_SHARING)}

{story("Hospital indemnity plan pays nothing for a birth, calling pregnancy a &ldquo;pre-existing sickness&rdquo; &mdash; MetLife (Scripps News, Jan 2025)",
       "McClinton and Brie Heil signed up for a MetLife hospital indemnity plan during their employer&rsquo;s open enrollment in November 2023, prompted by MetLife&rsquo;s own pitch: &ldquo;Hey, are you pregnant? You should sign up for this for next year.&rdquo; Their son was born in June 2024. MetLife paid nothing. Its denial letter said the claim &ldquo;was caused by or resulted from a pre-existing condition,&rdquo; because the pregnancy began before the plan did, and MetLife&rsquo;s policy defines pregnancy as a &ldquo;sickness.&rdquo; Their complaint was rejected.",
       "Scripps News", SCRIPPS)}

{story("And one with an ACA plan: Davidson, NC teen&rsquo;s $800,000-a-year drug denied twice, then overturned by the state (NBC News, Dec 2025)",
       "Paxton Pope, 13, was twice denied the drug his doctors prescribed for his seizures. Because his family&rsquo;s plan was ACA-regulated, they had a right the plans above don&rsquo;t offer: an external review through Smart NC at the NC Department of Insurance. The state overturned the denial, the insurer had to pay, and Paxton&rsquo;s seizures fell from about 12 an hour to 8 a day.",
       "NBC News", NBC_POPE, good=True)}

<h2>When might one of these make sense?</h2>
<p><strong>Short-term coverage</strong> can make sense for a short gap between jobs, with eyes open, when you have the savings to absorb a worst case.</p>
<p><strong>Indemnity plans</strong> can make sense alongside an ACA plan, not instead of one. A hospital indemnity plan, for example, can pay a fixed amount toward a hospital stay before your ACA deductible, which can be high, is met. Whether the premium is worth it depends on your deductible, your health and your budget, and I&rsquo;m glad to help you do that math.</p>

<p class="reviewed-note">Last reviewed: November 2026. The North Carolina short-term plan limit is set by federal rule and may change; see <a href="{DOI_BULLETIN}" target="_blank" rel="noopener">NC DOI Bulletin 25-B-11</a>.</p>

{cta("See what a real ACA plan costs you", "Enter your county, ages and income and our Covanu tool shows every ACA-qualified plan with your subsidy applied, checks your medications against each plan's drug list, and estimates your total yearly cost. If you are weighing an indemnity plan on top of one, book a call and we will do the math together. Our help is free.")}

{author_box()}

{sources([
    f'<a href="{NBC_SHARING}" target="_blank" rel="noopener">NBC News, &ldquo;Faith-based cost-sharing seemed like an alternative to health insurance, until the childbirth bills arrived&rdquo;</a> (December 22, 2024): the Sedera and Liberty HealthShare stories.',
    f'<a href="{KFF_JUNK}" target="_blank" rel="noopener">KFF Health News</a> (December 4, 2020, also on NPR): the Golden Rule short-term plan story.',
    f'<a href="{SCRIPPS}" target="_blank" rel="noopener">Scripps News</a> (January 21, 2025): the MetLife hospital indemnity story.',
    f'<a href="{NBC_POPE}" target="_blank" rel="noopener">NBC News</a> (December 2025): the Smart NC external review.',
    f'<a href="{DOI_BULLETIN}" target="_blank" rel="noopener">NC Department of Insurance Bulletin 25-B-11</a> (August 29, 2025): short-term, limited-duration health insurance in North Carolina.',
    '<a href="https://www.healthcare.gov/developers/" target="_blank" rel="noopener">HealthCare.gov Marketplace API</a>: 2027 out-of-pocket maximums of North Carolina Marketplace plans, retrieved November 10, 2026.',
])}
"""

page(PATH, TITLE, DESC, "/questions/", CRUMBS, body, reading="7 minute read", date=DATE)
