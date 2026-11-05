import json, os, html

import os
OUT = os.environ.get("FBHD_OUT", os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
BASE = "https://factbasedhealthcaredecisions.com"
UPDATED = "2026-11-05"
UPDATED_H = "November 5, 2026"
APP = "https://app.covanu.com/agent/21720013"
CAL = "https://calendly.com/kurt-conger"

NAV = [("/", "Home"), ("/counties/", "County Guides"), ("/questions/", "Common Questions"), ("/about/", "How We Work")]

PERSON = {
    "@type": "Person",
    "name": "Kurt Conger",
    "jobTitle": "Independent Licensed NC Health Insurance Agent",
    "url": BASE + "/#about",
    "identifier": {"@type": "PropertyValue", "propertyID": "NPN", "value": "21720013"},
    "worksFor": {"@type": "Organization", "name": "Fact-Based Healthcare Decisions", "url": BASE},
}

ORG = {
    "@type": "InsuranceAgency",
    "@id": BASE + "/#org",
    "name": "Fact-Based Healthcare Decisions",
    "url": BASE,
    "logo": BASE + "/MFHD_LOGO.png",
    "email": "kurt.conger@gmail.com",
    "areaServed": {"@type": "State", "name": "North Carolina"},
    "founder": PERSON,
    "knowsAbout": ["ACA Marketplace health insurance", "North Carolina individual health insurance", "Blue Cross NC plans", "premium tax credits", "self-employed health insurance"],
}


def head(title, desc, path, jsonld=None, og_type="article"):
    url = BASE + path
    ld = ""
    if jsonld:
        ld = "\n".join(f'<script type="application/ld+json">{json.dumps(j, ensure_ascii=False)}</script>' for j in jsonld)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{html.escape(title)}</title>
    <meta name="description" content="{html.escape(desc)}">
    <link rel="canonical" href="{url}">
    <meta property="og:type" content="{og_type}">
    <meta property="og:title" content="{html.escape(title)}">
    <meta property="og:description" content="{html.escape(desc)}">
    <meta property="og:url" content="{url}">
    <meta property="og:image" content="{BASE}/MFHD_LOGO.png">
    <meta property="og:site_name" content="Fact-Based Healthcare Decisions">
    <meta name="twitter:card" content="summary">
    <link rel="icon" type="image/png" href="/favicon.png">
    <link rel="apple-touch-icon" href="/favicon.png">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Merriweather:wght@400;700&family=Open+Sans:wght@400;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/Styles.css">
    {ld}
</head>
<body>
"""


def nav(current):
    items = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == current else ""
        gate = ' class="geo-gate"' if href == "/counties/" and current not in ("/counties/",) else ""
        items.append(f'<li{gate}><a class="nav-link" href="{href}"{cur}>{label}</a></li>')
    return f"""    <nav class="site-nav" aria-label="Main">
        <div class="nav-inner">
            <a class="nav-brand" href="/"><img src="/MFHD_LOGO.png" alt=""> Fact-Based Healthcare Decisions</a>
            <ul>
                {''.join(items)}
                <li><a class="nav-cta" href="{CAL}" target="_blank" rel="noopener">Schedule a call</a></li>
            </ul>
        </div>
    </nav>
"""


def footer():
    return f"""    <footer class="site-footer">
        <div class="footer-inner">
            <div>
                <h4>Fact-Based Healthcare Decisions</h4>
                <p>Independent, licensed ACA health insurance guidance for North Carolina individuals, families, the self-employed and early retirees. Our help is free; insurers pay our commissions.</p>
                <p style="margin-top:8px">Kurt Conger &middot; NC Health Producer, NPN 21720013<br><a href="mailto:kurt.conger@gmail.com">kurt.conger@gmail.com</a></p>
            </div>
            <div>
                <h4>Common questions</h4>
                <ul>
                    <li><a href="/questions/bronze-vs-silver-medications/">Bronze vs. Silver with medications</a></li>
                    <li><a href="/questions/self-employed-north-carolina-2027/">Self-employed in NC (2027)</a></li>
                    <li><a href="/questions/retiring-before-65-north-carolina/">Retiring before 65 in NC</a></li>
                    <li><a href="/questions/blue-care-vs-blue-advantage-eastern-nc/">Blue Care vs. Blue Advantage</a></li>
                    <li><a href="/counties/">County guides (21 eastern NC counties)</a></li>
                </ul>
            </div>
            <div>
                <h4>Tools</h4>
                <ul>
                    <li><a href="{APP}" target="_blank" rel="noopener">Compare plans (Covanu)</a></li>
                    <li><a href="{CAL}" target="_blank" rel="noopener">Schedule a meeting</a></li>
                    <li><a href="/about/">How we work</a></li>
                    <li><a href="https://www.healthcare.gov/" target="_blank" rel="noopener">HealthCare.gov</a></li>
                </ul>
            </div>
        </div>
        <div class="legal">
            <p>Plan details and premiums on this site come from the HealthCare.gov Marketplace API for the 2027 plan year and are shown for comparison; your price depends on your age, household, income and county. Verify benefits in the plan's Summary of Benefits and Coverage before enrolling. This site is not affiliated with HealthCare.gov or Blue Cross and Blue Shield of North Carolina. Nothing here is tax or legal advice.</p>
        </div>
    </footer>
    <script src="/geo.js" defer></script>
</body>
</html>
"""


def byline(reading=None):
    r = f" &middot; {reading}" if reading else ""
    return f'<p class="byline">By <a href="/#about">Kurt Conger</a>, independent licensed NC health insurance agent (NPN 21720013) &middot; Updated {UPDATED_H}{r} &middot; Plan data: HealthCare.gov Marketplace API, 2027 plan year</p>'


def breadcrumb(items):
    parts = [f'<a href="{h}">{t}</a>' if h else html.escape(t) for h, t in items]
    return '<nav class="breadcrumb" aria-label="Breadcrumb">' + " &rsaquo; ".join(parts) + "</nav>"


def breadcrumb_ld(items):
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": t, **({"item": BASE + h} if h else {})}
            for i, (h, t) in enumerate(items)
        ],
    }


def article_ld(title, desc, path, faq=None):
    ld = [{
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "description": desc,
        "url": BASE + path,
        "datePublished": UPDATED,
        "dateModified": UPDATED,
        "author": PERSON,
        "publisher": {"@type": "Organization", "name": "Fact-Based Healthcare Decisions", "url": BASE, "logo": {"@type": "ImageObject", "url": BASE + "/MFHD_LOGO.png"}},
        "mainEntityOfPage": BASE + path,
        "about": {"@type": "Thing", "name": "North Carolina ACA Marketplace health insurance"},
    }]
    if faq:
        ld.append({
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq],
        })
    return ld


def faq_html(faq):
    out = ['<section class="faq"><h2 id="faq">Frequently asked questions</h2>']
    for q, a in faq:
        out.append(f"<details><summary>{html.escape(q)}</summary><p>{a}</p></details>")
    out.append("</section>")
    return "\n".join(out)


def cta(heading="See your own prices in two minutes", text=None):
    text = text or "Enter your county, ages and income and our Covanu tool shows every plan with your subsidy applied, checks your medications against each plan's drug list, and estimates your total yearly cost. Then book a call and we'll finish it together. Our help is free."
    return f"""<section class="cta-block">
    <h2>{heading}</h2>
    <p>{text}</p>
    <div class="way-actions">
        <a class="btn" href="{APP}" target="_blank" rel="noopener">Compare plans with your numbers</a>
        <a class="btn btn-outline" href="{CAL}" target="_blank" rel="noopener">Schedule a call with Kurt</a>
    </div>
</section>"""


def author_box():
    return """<div class="author-box">
    <img src="/MFHD_LOGO.png" alt="">
    <div>
        <p><strong>About the author.</strong> Kurt Conger is an independent, licensed North Carolina health insurance agent (NPN 21720013) and the founder of Fact-Based Healthcare Decisions and <a href="https://covanu.com" target="_blank" rel="noopener">Covanu</a>, a plan-selection tool built on HealthCare.gov data. He lives in Carteret County and helps North Carolinians who are starting a business, retiring early or losing coverage compare every ACA plan available to them on total yearly cost, then finish the choice and enroll.</p>
    </div>
</div>"""


def sources(items):
    lis = "".join(f"<li>{s}</li>" for s in items)
    return f'<section class="sources"><strong>Sources</strong><ul>{lis}</ul></section>'


def write(path, content):
    full = os.path.join(OUT, path.lstrip("/"))
    if path.endswith("/"):
        full = os.path.join(full, "index.html")
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print("wrote", full)


def page(path, title, desc, current, crumbs, body, faq=None, extra_ld=None, reading=None, og_type="article"):
    ld = article_ld(title, desc, path, faq) + [breadcrumb_ld(crumbs)] + (extra_ld or [])
    doc = head(title, desc, path, ld, og_type) + nav(current)
    doc += '    <div class="container">\n'
    doc += breadcrumb(crumbs)
    doc += '<article class="article">\n'
    doc += body
    if faq:
        doc += "\n" + faq_html(faq)
    doc += '\n<p class="back-home"><a href="/">&larr; Back to the home page</a></p>'
    doc += "\n</article>\n    </div>\n"
    doc += footer()
    write(path, doc)


MAP_SVG = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "nc_map.svg"), encoding="utf-8").read()


def nc_map(intro=True):
    legend = """<div class="map-legend"><span class="sw live"></span> Guides available (rating areas 12 and 16) <span class="sw soon"></span> Coming soon</div>"""
    return f'<div class="map-wrap">{MAP_SVG}{legend}</div>'
