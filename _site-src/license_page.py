r"""/license/ : how a client can verify Kurt Conger's North Carolina insurance license.

Not linked from the menu (Kurt, Nov 13, 2026); listed in the sitemap. The certificate image is
/images/kurt-conger-nc-insurance-license.jpg (1200 x 1000): only the bordered certificate, cropped from the NC DOI
license PDF Kurt sent Nov 13, 2026 (rendered at 200 dpi). The PDF's top half, with his mailing address and the
wallet card, is deliberately left out. Facts checked Nov 13, 2026 against
the NC statutes and NC DOI pages in the sources list; the NAIC link opens the lookup with North Carolina,
Licensee, Individual and license number 21720013 filled in, and the visitor adds the last name.
"""
from fbsite import *

PATH = "/license/"
NAIC = "https://sbs.naic.org/solar-external-lookup/lookup?jurisdiction=NC&searchType=Licensee&entityType=IND&licenseNumber=21720013"
TITLE = "Verify Kurt Conger's NC Insurance License (NPN 21720013) | Fact-Based Healthcare Decisions"
DESC = ("Check Kurt Conger's North Carolina health insurance license in the NAIC's official lookup, "
        "and see what the license covers and the background check behind it.")
UPDATED_LIC = "November 13, 2026"
CRUMBS = [("/", "Home"), (None, "Verify Kurt's license")]

body = f"""<h1>Verify Kurt Conger&rsquo;s North Carolina insurance license</h1>
{byline(None, UPDATED_LIC, None)}
<p class="lede">Before you share your income, health and family details with someone who helps with your health insurance, it is worth confirming that they are licensed. Kurt Conger holds a North Carolina insurance producer license for health insurance, number 21720013. You can confirm it yourself in about a minute in the license lookup that the National Association of Insurance Commissioners (NAIC) runs for the North Carolina Department of Insurance.</p>

<section class="callout verify-box">
<h2>How to verify the license</h2>
<ol>
<li>Click this <a href="{NAIC}" target="_blank" rel="noopener">NAIC Link</a>. It opens the lookup with North Carolina, Licensee, Individual and license number 21720013 already filled in.</li>
<li>Type <strong>CONGER</strong> in the <strong>Last Name</strong> box.</li>
<li>Check that the box agreeing to the NAIC&rsquo;s Terms and Conditions is ticked, then click <strong>Search</strong>.</li>
<li>Look at the result. It should show Kurt Conger&rsquo;s license 21720013 as active, with the Accident &amp; Health or Sickness line of authority, matching the certificate below.</li>
</ol>
</section>

<figure class="license-cert">
<a href="/images/kurt-conger-nc-insurance-license.jpg" target="_blank" rel="noopener"><img src="/images/kurt-conger-nc-insurance-license.jpg" width="1200" height="1000" alt="North Carolina Department of Insurance license certificate for Kurt Conger: license number 21720013, NPN 21720013, license type Insurance Producer, line of authority Accident and Health or Sickness, effective September 19, 2025."></a>
<figcaption>Kurt&rsquo;s license certificate from the North Carolina Department of Insurance (click to enlarge). The NAIC lookup shows the license&rsquo;s current status.</figcaption>
</figure>

<h2>What a North Carolina health insurance license is</h2>
<p>The North Carolina Department of Insurance licenses insurance agents as <em>insurance producers</em>. Each license lists the kinds of insurance the agent may sell, called <em>lines of authority</em>, and state law forbids selling, soliciting or negotiating any kind of insurance without a license for that line.</p>
<p>Kurt&rsquo;s license carries the <strong>Accident &amp; Health or Sickness</strong> line, North Carolina&rsquo;s health insurance license. State law defines it as insurance coverage for sickness, bodily injury or accidental death, which may include disability income benefits. It is the license an agent needs to sell health insurance in North Carolina, including the ACA Marketplace plans covered on this site.</p>
<p>To earn it, an applicant must be at least 18, pass the state licensing exam for that line of authority (North Carolina&rsquo;s exams are given by Pearson VUE), complete the background check described below, and apply to the Department of Insurance, which decides whether to issue the license.</p>
<p>To keep it, a North Carolina agent must complete 24 hours of approved continuing education every two years, including 3 hours of ethics. If an agent misses the deadline, the license expires. As the certificate says, the license stays valid until it is cancelled, surrendered or revoked.</p>

<h2>The license includes a criminal background check</h2>
<p>Every first-time applicant for a North Carolina resident insurance producer license must be fingerprinted for a state and federal criminal history check, as required by North Carolina General Statute 58-33-48. The Department of Insurance reviews the criminal history record, along with the applicant&rsquo;s answers to the application&rsquo;s background questions, before it decides whether to issue the license.</p>
<p>Kurt completed this background check before North Carolina issued his license on September 19, 2025.</p>

<p class="license-contact">Questions about Kurt&rsquo;s license or your coverage? {CONTACT_BTN}</p>

{sources([
    f'<a href="{NAIC}" target="_blank" rel="noopener">NAIC State Based Systems license lookup</a> for North Carolina, license 21720013.',
    '<a href="https://house.ncleg.gov/EnactedLegislation/Statutes/HTML/ByArticle/Chapter_58/Article_33.html">N.C. General Statutes, Chapter 58, Article 33</a>: &sect; 58-33-5 (license required for each line of authority).',
    '<a href="https://ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_58/GS_58-33-26.html">N.C.G.S. &sect; 58-33-26</a>: lines of authority, including accident and health or sickness.',
    '<a href="https://ncleg.net/EnactedLegislation/Statutes/PDF/BySection/Chapter_58/GS_58-33-48.pdf">N.C.G.S. &sect; 58-33-48</a>: criminal history record checks for insurance producer applicants.',
    '<a href="https://www.ncdoi.gov/licensees/agent-and-adjuster-licensing/become-insurance-agent/resident-fingerprint-requirements">NC Department of Insurance: Resident Fingerprint Requirements</a>.',
    '<a href="https://pdb.nipr.com/html/SSR/North_Carolina_ERL.htm">NIPR: North Carolina licensing requirements</a> (minimum age, fingerprints, Department review of background records).',
    '<a href="https://www.ncdoi.gov/documents/agent-services/ple-packet-october-2025/open">NC Department of Insurance: Pre-Licensing Education Information Packet, October 2025</a> (Pearson VUE as the exam vendor).',
    '<a href="https://www.ncdoi.gov/licensees/agent-and-adjuster-licensing/continuing-education-agents-and-adjusters">NC Department of Insurance: Continuing Education for Insurance Producers and Adjusters</a>.',
])}
"""

person = {"@context": "https://schema.org", **PERSON,
          "hasCredential": {
              "@type": "EducationalOccupationalCredential",
              "credentialCategory": "license",
              "name": "North Carolina Insurance Producer License, Accident & Health or Sickness",
              "identifier": "21720013",
              "url": BASE + PATH,
              "recognizedBy": {"@type": "GovernmentOrganization", "name": "North Carolina Department of Insurance", "url": "https://www.ncdoi.gov/"},
          }}
page_ld = {"@context": "https://schema.org", "@type": "WebPage", "name": "Verify Kurt Conger's North Carolina insurance license",
           "url": BASE + PATH, "description": DESC, "about": {"@type": "Person", "name": "Kurt Conger", "url": BASE + "/#about"}}

ld = [page_ld, person, breadcrumb_ld(CRUMBS)]
doc = head(TITLE, DESC, PATH, ld, "website") + nav(None)
doc += '    <div class="container">\n' + breadcrumb(CRUMBS) + '<article class="article">\n' + body
doc += '\n<p class="back-home"><a href="/">&larr; Back to the home page</a></p>'
doc += '\n</article>\n    </div>\n' + footer()
write(PATH, doc)
