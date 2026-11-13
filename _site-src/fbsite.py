import json, os, html

import os
OUT = os.environ.get("FBHD_OUT", os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
BASE = "https://factbasedhealthcaredecisions.com"
UPDATED = "2026-11-05"
UPDATED_H = "November 5, 2026"
APP = "https://app.covanu.com/agent/21720013"
CAL = "https://calendly.com/kurt-conger"
EMAIL = "kurt.conger@gmail.com"
PHONE = "252-570-7239"
PHONE_TEL = "+12525707239"

# "Contact Us" button: opens the contact popup (email, phone, calendar) that footer() adds to every page
CONTACT_BTN = '<button class="contact-btn" type="button" data-contact aria-haspopup="dialog" aria-controls="contact-dialog">Contact Us</button>'

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
        items.append(f'<li><a class="nav-link" href="{href}"{cur}>{label}</a></li>')
    return f"""    <nav class="site-nav" aria-label="Main">
        <div class="nav-inner">
            <a class="nav-brand" href="/"><img src="/MFHD_LOGO.png" alt=""> <span class="nav-brand-text">Fact-Based Healthcare Decisions</span></a>
            <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-menu" aria-label="Menu"><span></span><span></span><span></span></button>
            <ul id="site-menu">
                {''.join(items)}
                <li><button class="nav-cta" type="button" data-contact aria-haspopup="dialog" aria-controls="contact-dialog">Contact Us</button></li>
            </ul>
        </div>
        <script>
            (function () {{
                var nav = document.querySelector(".site-nav"), btn = nav.querySelector(".nav-toggle");
                function setOpen(open) {{ nav.classList.toggle("nav-open", open); btn.setAttribute("aria-expanded", open ? "true" : "false"); }}
                btn.addEventListener("click", function () {{ setOpen(!nav.classList.contains("nav-open")); }});
                document.addEventListener("keydown", function (e) {{ if (e.key === "Escape") setOpen(false); }});
                document.addEventListener("click", function (e) {{ if (!nav.contains(e.target)) setOpen(false); }});
            }})();
        </script>
    </nav>
"""


def footer():
    return f"""    <footer class="site-footer">
        <div class="footer-inner">
            <div>
                <h4>Fact-Based Healthcare Decisions</h4>
                <p>Independent, licensed ACA health insurance guidance for North Carolina individuals, families, the self-employed and early retirees. Our help is free; insurers pay our commissions.</p>
                <p style="margin-top:8px">Kurt Conger &middot; NC Health Producer, NPN 21720013</p>
                <p class="footer-contact">{CONTACT_BTN}</p>
            </div>
            <div>
                <h4>Common questions</h4>
                <ul>
                    <li><a href="/questions/cheaper-alternatives-to-aca-plans/">Cheaper alternatives to ACA plans</a></li>
                    <li><a href="/questions/bronze-vs-silver-medications/">Bronze vs. Silver with medications</a></li>
                    <li><a href="/questions/self-employed-north-carolina-2027/">Self-employed in NC (2027)</a></li>
                    <li><a href="/questions/retiring-before-65-north-carolina/">Retiring before 65 in NC</a></li>
                    <li><a href="/questions/blue-care-vs-blue-advantage/">Blue Care vs. Blue Advantage</a></li>
                    <li><a href="/questions/aca-plan-quality-ratings/">Measuring plan quality</a></li>
                    <li><a href="/counties/">County guides</a></li>
                </ul>
            </div>
            <div>
                <h4>Tools</h4>
                <ul>
                    <li><a href="{APP}" target="_blank" rel="noopener">Compare plans (Covanu)</a></li>
                    <li><a href="{CAL}" target="_blank" rel="noopener">Schedule a meeting</a></li>
                    <li><a href="/about/">How we work</a></li>
                </ul>
            </div>
        </div>
        <div class="legal">
            <p>Plan details and premiums on this site come from the HealthCare.gov Marketplace API for the 2027 plan year and are shown for comparison; your price depends on your age, household, income and county. Verify benefits in the plan's Summary of Benefits and Coverage before enrolling. This site is not affiliated with HealthCare.gov or any insurer. Nothing here is tax or legal advice.</p>
        </div>
    </footer>
{CONTACT_DIALOG}
</body>
</html>
"""


# Contact popup shared by every page. Plain string (not an f-string) so the script's braces need no escaping.
_ICON = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">%s</svg>'
_ICON_MAIL = _ICON % '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>'
_ICON_PHONE = _ICON % '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/>'
_ICON_TEXT = _ICON % '<path d="M4 5h16v11H9l-5 4z"/><path d="M8 9h8M8 12h5"/>'
_ICON_CAL = _ICON % '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M16 3v4M8 3v4M3 10h18"/>'
CONTACT_DIALOG = """    <dialog class="contact-dialog" id="contact-dialog" aria-labelledby="contact-dialog-title">
        <div class="contact-dialog-body">
            <button class="contact-dialog-close" type="button" aria-label="Close" data-contact-close>&times;</button>
            <h2 id="contact-dialog-title">Contact Us</h2>
            <p class="contact-dialog-sub">Kurt Conger, independent licensed NC health insurance agent</p>
            <a class="contact-option" href="mailto:""" + EMAIL + """">""" + _ICON_MAIL + """<span><strong>Email</strong><span>""" + EMAIL + """</span></span></a>
            <a class="contact-option" href="tel:""" + PHONE_TEL + """">""" + _ICON_PHONE + """<span><strong>Call</strong><span>""" + PHONE + """</span></span></a>
            <a class="contact-option phone-only" href="sms:""" + PHONE_TEL + """">""" + _ICON_TEXT + """<span><strong>Text</strong><span>""" + PHONE + """</span></span></a>
            <a class="contact-option" href=\"""" + CAL + """\" target="_blank" rel="noopener">""" + _ICON_CAL + """<span><strong>Schedule a meeting</strong><span>Pick a time on my calendar</span></span></a>
        </div>
    </dialog>
    <script>
        (function () {
            var phone = /Android|iPhone|iPod|Mobi/i.test(navigator.userAgent || "") || (window.matchMedia && window.matchMedia("(pointer: coarse) and (max-width: 900px)").matches);
            if (phone) document.documentElement.classList.add("is-phone");
            var dlg = document.getElementById("contact-dialog");
            if (!dlg) return;
            function openContact(e) {
                if (e) e.preventDefault();
                var nav = document.querySelector(".site-nav.nav-open");
                if (nav) {
                    nav.classList.remove("nav-open");
                    var t = nav.querySelector(".nav-toggle");
                    if (t) t.setAttribute("aria-expanded", "false");
                }
                if (typeof dlg.showModal === "function") dlg.showModal(); else dlg.setAttribute("open", "");
            }
            function closeContact() {
                if (typeof dlg.close === "function") dlg.close(); else dlg.removeAttribute("open");
            }
            Array.prototype.forEach.call(document.querySelectorAll("[data-contact]"), function (b) {
                b.addEventListener("click", openContact);
            });
            dlg.querySelector("[data-contact-close]").addEventListener("click", closeContact);
            dlg.addEventListener("click", function (e) { if (e.target === dlg) closeContact(); });
        })();
    </script>"""


# Shared county-guide text, 2027 plan year. Insulin prices: Lilly, Novo Nordisk and Sanofi list prices and $35 programs;
# children's dental: Marketplace stand-alone dental plans for an 8-year-old in six NC counties (API pull, Nov 11, 2026);
# Ambetter and Oscar extras: the insurers' North Carolina member pages and 2027 announcements.
INSULIN_COST = ("It is priced like any brand-name drug: a preferred brand is a $40 copay with no deductible on the standardized Silver and $30 on the standardized Gold, "
                "while on most Bronze plans you pay the pharmacy price, about $66 to $72 for a vial of Humalog or NovoLog since the 2023&ndash;2024 list-price cuts, until you meet the deductible. "
                "Lilly, Novo Nordisk and Sanofi each cap their insulins at $35 a month for people with commercial coverage, which includes Marketplace plans, "
                "so a two-insulin routine usually costs $35 to $80 a month without a $0 benefit, about $400 to $1,000 a year. That is roughly what $0 insulin is worth to someone who uses those programs.")
DENT_VALUE = ("Included children's dental is worth about $250 to $700 a year per child, what a stand-alone children's dental plan costs in North Carolina for 2027 ($21 to $58 a month). "
              "It pays for checkups in full; on most plans, fillings and other treatment count toward the medical deductible, while a stand-alone plan has a $25 to $155 deductible and caps a child's costs at $350 to $450 a year, so a child who needs fillings can come out ahead with one.")
DENT_COST = "about $21 to $58 a month per child"
AMB_EXTRAS = ("a free YMCA membership at participating North Carolina Ys, including YMCA360 online classes; the Ambetter Perks discount program (groceries, gym memberships, travel); "
              "up to $500 in My Health Pays rewards for healthy activities, which can go toward premiums and household bills; free Virtual 24/7 Care visits on every plan except the standardized Signature plans; "
              "and, in some counties, DispatchHealth urgent care at home")
OSC_EXTRAS = "$0 virtual urgent care on every plan, $4 generic drugs on most plans, and a Care Team and an AI guide (Oswell) in the Oscar app that help you find doctors, estimate costs and understand bills"


def byline(reading=None, updated=None, data="Plan data: HealthCare.gov Marketplace API, 2027 plan year"):
    r = f" &middot; {reading}" if reading else ""
    d = f" &middot; {data}" if data else ""
    return f'<p class="byline">Content drafted by Generative AI tools and reviewed and edited by <a href="/#about">Kurt Conger</a>, independent licensed NC health insurance agent (NPN 21720013) &middot; Updated {updated or UPDATED_H}{r}{d}</p>'


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


def article_ld(title, desc, path, faq=None, date=None):
    ld = [{
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "description": desc,
        "url": BASE + path,
        "datePublished": date or UPDATED,
        "dateModified": date or UPDATED,
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
        <p><strong>About this Content.</strong> The first draft of this content was created by a Gen AI tool. The content was reviewed and edited by Kurt Conger, an independent, licensed North Carolina health insurance agent (NPN 21720013) and a co-founder of Fact-Based Healthcare Decisions and <a href="https://covanu.com" target="_blank" rel="noopener">Covanu</a>, a plan-selection tool built on HealthCare.gov data. Kurt lives in Carteret County and helps North Carolinians who need health insurance.</p>
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


def page(path, title, desc, current, crumbs, body, faq=None, extra_ld=None, reading=None, og_type="article", date=None):
    ld = article_ld(title, desc, path, faq, date) + [breadcrumb_ld(crumbs)] + (extra_ld or [])
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
    legend = """<div class="map-legend">Every county has a guide. The shades and numbers mark the 16 rating areas; insurers set prices by rating area.</div>"""
    return f'<div class="map-wrap">{MAP_SVG}{legend}</div>'
