"""
Shared look and feel for the Streamlit frontend, matched to vibrantlogics.com.

Every page calls `page_header()` at the top and `page_footer()` at the bottom.
"""

from datetime import date

import streamlit as st

COMPANY = "Vibrant Logics"
COMPANY_URL = "https://vibrantlogics.com"
CONTACT_URL = f"{COMPANY_URL}/contact"
CONTACT_EMAIL = "info@vibrantlogics.com"
CONTACT_PHONE = "+1 934 203 2603"
CONTACT_ADDRESS = "29-21 24th Ave, Astoria, NY 11102, USA"
LOGO_URL = f"{COMPANY_URL}/images/home/logo.png"

# Relative links so the app also works when served under a sub-path.
NAV_LINKS = [
    ("home", "Home", "./"),
    ("about", "About Us", "./about"),
    ("privacy", "Privacy Policy", "./privacy"),
    ("terms", "Terms & Conditions", "./terms"),
]

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Inter+Tight:wght@600;700;800&display=swap');

:root {
    --vl-purple: #792884;
    --vl-purple-dark: #5e1f67;
    --vl-purple-soft: #f5ecf6;
    --vl-green: #4aba6a;
    --vl-green-dark: #3a9a56;
    --vl-green-soft: #eaf7ee;
    --vl-ink: #2e2e38;
    --vl-muted: #6b6b78;
    --vl-line: #ececf1;
    --vl-amber: #e08a1e;
    --vl-amber-soft: #fdf3e6;
    --vl-red: #d64545;
    --vl-red-soft: #fcecec;
}

html, body, .stApp, .stApp p, .stApp li, .stApp span:not([data-testid="stIconMaterial"]), .stApp small,
.stApp label, .stApp input, .stApp textarea {
    font-family: 'Inter', sans-serif;
}
.stApp { background: #ffffff; color: var(--vl-ink); }
h1, h2, h3, h4, .vl-display { font-family: 'Inter Tight', 'Inter', sans-serif !important; color: var(--vl-ink); }

/* Hide default Streamlit chrome */
#MainMenu, header[data-testid="stHeader"], footer, [data-testid="stToolbar"],
[data-testid="stDecoration"], [data-testid="stSidebarCollapsedControl"],
[data-testid="stHeaderActionElements"] { display: none !important; }
.block-container { padding-top: 0 !important; padding-bottom: 0 !important; max-width: 1200px; }

/* Header */
.vl-nav {
    display: flex; align-items: center; justify-content: space-between; gap: 1.5rem;
    padding: 1.1rem 0; border-bottom: 1px solid var(--vl-line); flex-wrap: wrap;
}
.vl-brand { display: flex; align-items: center; gap: .75rem; text-decoration: none !important; }
.vl-brand img { height: 52px; width: auto; }
.vl-brand-product {
    font-family: 'Inter Tight', sans-serif; font-weight: 700; font-size: .95rem; color: var(--vl-green);
    border-left: 1px solid var(--vl-line); padding-left: .75rem;
}
.vl-links { display: flex; gap: 1.75rem; flex-wrap: wrap; align-items: center; }
.vl-links a {
    color: var(--vl-ink) !important; text-decoration: none !important; font-weight: 500; font-size: 15px;
    padding-bottom: 4px; border-bottom: 2px solid transparent;
}
.vl-links a:hover { color: var(--vl-purple) !important; }
@media (max-width: 700px) {
    .vl-nav { gap: .6rem; padding: .8rem 0; }
    .vl-brand img { height: 40px; }
    .vl-links { gap: .4rem 1rem; }
    .vl-links a { font-size: 13px; }
    .vl-nav > .vl-btn { display: none; }
}
.vl-links a.active { color: var(--vl-purple) !important; border-bottom-color: var(--vl-purple); }

/* Pills */
.vl-btn {
    display: inline-flex; align-items: center; gap: .4rem; border-radius: 999px; padding: .75rem 1.6rem;
    font-weight: 600; font-size: 15px; text-decoration: none !important; transition: background .2s;
}
.vl-btn-green { background: var(--vl-green); color: #fff !important; }
.vl-btn-green:hover { background: var(--vl-green-dark); }
.vl-btn-purple { background: var(--vl-purple); color: #fff !important; }
.vl-btn-purple:hover { background: var(--vl-purple-dark); }

/* Hero */
.vl-hero {
    margin: 0 calc(50% - 50vw); padding: 4.5rem 1.5rem 7rem; text-align: center; color: #fff;
    background:
        linear-gradient(rgba(30, 24, 40, .78), rgba(30, 24, 40, .82)),
        url('https://images.unsplash.com/photo-1530836369250-ef72a3f5cda8?auto=format&fit=crop&w=2000&q=60') center/cover;
}
.vl-hero h1 { color: #fff !important; font-size: clamp(2.2rem, 5vw, 3.6rem); font-weight: 800; line-height: 1.12; margin: 0 0 1rem; padding: 0; }
.vl-hero p { color: rgba(255,255,255,.88); font-size: 1.2rem; max-width: 720px; margin: 0 auto; }
.vl-green-text { color: var(--vl-green); }
.vl-purple-text { color: var(--vl-purple); }

/* Small page hero for content pages */
.vl-page-hero { margin: 0 calc(50% - 50vw); padding: 3.5rem 1.5rem; text-align: center; background: var(--vl-purple-soft); }
.vl-page-hero h1 { font-size: clamp(2rem, 4vw, 2.8rem); font-weight: 800; margin: 0; padding: 0; }
.vl-page-hero p { color: var(--vl-muted); margin: .6rem 0 0; }

/* Step cards (like the Collaborate / Innovate row on the site) */
.vl-steps { display: grid; grid-template-columns: repeat(4, 1fr); gap: 1.25rem; margin-top: -4.5rem; position: relative; }
@media (max-width: 900px) { .vl-steps { grid-template-columns: repeat(2, 1fr); } }
@media (max-width: 520px) { .vl-steps { grid-template-columns: 1fr; } }
.vl-step {
    background: #fff; border-radius: 16px; padding: 1.6rem 1.5rem; position: relative; overflow: hidden;
    box-shadow: 0 10px 30px rgba(46,46,56,.10);
}
.vl-step::before {
    content: ""; position: absolute; top: 0; left: 0; width: 34px; height: 34px;
    background: var(--vl-green); clip-path: polygon(0 0, 100% 0, 0 100%);
}
.vl-step .num { position: absolute; top: 1rem; right: 1.3rem; font-family: 'Inter Tight'; font-weight: 800; font-size: 2.2rem; color: #e6e6ec; }
.vl-step .icon { font-size: 1.6rem; }
.vl-step h3 { color: var(--vl-purple) !important; font-size: 1.25rem; margin: .8rem 0 .35rem; padding: 0; }
.vl-step h3 a { color: var(--vl-purple) !important; text-decoration: none !important; }
.vl-step h3 a:hover { color: var(--vl-green-dark) !important; text-decoration: underline !important; text-underline-offset: 4px; }
html { scroll-behavior: smooth; }
.vl-step p { color: var(--vl-muted); font-size: .95rem; margin: 0; line-height: 1.55; }

/* Section headings */
.vl-section { padding: 3.5rem 0 1rem; text-align: center; }
.vl-eyebrow { color: var(--vl-green); font-weight: 600; letter-spacing: .12em; text-transform: uppercase; font-size: .8rem; }
.vl-section h2 { font-size: clamp(1.7rem, 3vw, 2.2rem); font-weight: 700; margin: .4rem 0 0; padding: 0; }

/* Detector panels */
[data-testid="stVerticalBlockBorderWrapper"]:has(> div > [data-testid="stVerticalBlock"] .vl-panel-marker) {
    border-radius: 16px !important; border-color: var(--vl-line) !important; box-shadow: 0 6px 24px rgba(46,46,56,.06);
}
.vl-panel-title { font-family: 'Inter Tight'; font-weight: 700; font-size: 1.15rem; margin-bottom: .2rem; }
.vl-panel-sub { color: var(--vl-muted); font-size: .92rem; margin-bottom: .6rem; }
[data-testid="stFileUploaderDropzone"] { border: 2px dashed #d9c3dc; background: var(--vl-purple-soft); border-radius: 12px; }
[data-testid="stImage"] img { border-radius: 12px; }

.stButton > button {
    background: var(--vl-purple) !important; color: #fff !important; border: none !important;
    border-radius: 999px !important; padding: .7rem 1.5rem !important; font-weight: 600 !important;
}
.stButton > button:hover { background: var(--vl-purple-dark) !important; }
.stButton > button p { color: #fff !important; font-size: 15px !important; }

.vl-empty { text-align: center; padding: 3rem 1rem; color: var(--vl-muted); }
.vl-empty .big { font-size: 2.6rem; }

/* Result card */
.vl-result-head { display: flex; align-items: center; gap: .9rem; margin-bottom: 1rem; }
.vl-result-icon { width: 52px; height: 52px; border-radius: 14px; display: grid; place-items: center; font-size: 1.6rem; flex-shrink: 0; }
.vl-result-title { font-family: 'Inter Tight'; font-weight: 800; font-size: 1.6rem; line-height: 1.2; margin: 0; }
.vl-result-sub { color: var(--vl-muted); font-size: .92rem; }
.tone-danger .vl-result-icon { background: var(--vl-red-soft); }
.tone-danger .vl-result-title { color: var(--vl-purple); }
.tone-ok .vl-result-icon { background: var(--vl-green-soft); }
.tone-ok .vl-result-title { color: var(--vl-green-dark); }
.tone-warn .vl-result-icon { background: var(--vl-amber-soft); }
.tone-warn .vl-result-title { color: var(--vl-amber); }

.vl-badges { display: flex; flex-wrap: wrap; gap: .5rem; margin-bottom: .6rem; }
.vl-badge { border-radius: 999px; padding: .3rem .85rem; font-size: .85rem; font-weight: 600; background: var(--vl-purple-soft); color: var(--vl-purple); }
.vl-badge.green { background: var(--vl-green-soft); color: var(--vl-green-dark); }
.vl-badge.amber { background: var(--vl-amber-soft); color: var(--vl-amber); }
.vl-badge.red { background: var(--vl-red-soft); color: var(--vl-red); }

.vl-meter { height: 8px; background: var(--vl-line); border-radius: 999px; overflow: hidden; margin: .3rem 0 1.1rem; }
.vl-meter > span { display: block; height: 100%; background: var(--vl-green); border-radius: 999px; }

.vl-list-title { font-family: 'Inter Tight'; font-weight: 700; font-size: 1.02rem; margin: 1rem 0 .4rem; display: flex; align-items: center; gap: .45rem; }
.vl-list { margin: 0; padding-left: 1.2rem; }
.vl-list li { margin-bottom: .35rem; line-height: 1.55; color: var(--vl-ink); }
.vl-list li::marker { color: var(--vl-green); }
.vl-timestamp { color: var(--vl-muted); font-size: .82rem; margin-top: 1.2rem; text-align: right; }
.vl-disclaimer { font-size: .82rem; color: var(--vl-muted); background: #fafafc; border-radius: 10px; padding: .7rem .9rem; margin-top: 1rem; }

/* Prose for About / Terms / Privacy */
.vl-prose { max-width: 820px; margin: 0 auto; padding: 2.5rem 0 3rem; line-height: 1.7; }
.vl-prose h2 { font-size: 1.45rem; font-weight: 700; margin: 2rem 0 .5rem; padding: 0; color: var(--vl-purple) !important; }
.vl-prose p, .vl-prose li { color: var(--vl-ink); }
.vl-prose a { color: var(--vl-purple) !important; }
.vl-callout { background: var(--vl-green-soft); border-left: 4px solid var(--vl-green); padding: 1rem 1.2rem; border-radius: 8px; }

.vl-cta {
    margin: 2.5rem 0 3.5rem; border-radius: 20px; padding: 2.5rem 2rem; text-align: center; color: #fff;
    background: linear-gradient(120deg, var(--vl-purple) 0%, #5a1e63 100%);
}
.vl-cta h2 { color: #fff !important; font-size: 1.8rem; margin: 0 0 .5rem; padding: 0; }
.vl-cta p { color: rgba(255,255,255,.85); margin: 0 0 1.4rem; }

/* Footer */
.vl-footer { margin: 0 calc(50% - 50vw); background: var(--vl-ink); color: rgba(255,255,255,.78); padding: 3.5rem 1.5rem 0; }
.vl-footer-inner { max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: 1.5fr 1fr 1.3fr; gap: 2.5rem; }
@media (max-width: 800px) { .vl-footer-inner { grid-template-columns: 1fr; } }
.vl-footer img { height: 54px; background: #fff; border-radius: 8px; padding: 6px 10px; }
.vl-footer h4 { color: #fff !important; font-size: .85rem; letter-spacing: .12em; text-transform: uppercase; margin: 0 0 1rem; padding: 0; }
.vl-footer p { margin: .9rem 0 0; font-size: .93rem; line-height: 1.6; }
.vl-footer ul { list-style: none; padding: 0 !important; margin: 0 !important; }
.vl-footer li { margin-left: 0 !important; padding-left: 0 !important; }
.vl-footer li { margin-bottom: .55rem; font-size: .93rem; }
.vl-footer a { color: rgba(255,255,255,.78) !important; text-decoration: none !important; }
.vl-footer a:hover { color: var(--vl-green) !important; }
.vl-footer-bottom {
    max-width: 1200px; margin: 2.5rem auto 0; border-top: 1px solid rgba(255,255,255,.12);
    padding: 1.2rem 0; display: flex; justify-content: space-between; gap: 1rem; flex-wrap: wrap; font-size: .85rem;
}
</style>
"""


def html(markup: str) -> None:
    """Render raw HTML. Lines are flattened so Markdown never mistakes indentation for a code block."""
    st.markdown(
        "\n".join(line.strip() for line in markup.splitlines() if line.strip()),
        unsafe_allow_html=True,
    )


def page_header(active: str) -> None:
    """Inject the theme and draw the top navigation bar."""
    html(CSS)
    links = "".join(
        f"<a href='{href}' target='_self' class='{'active' if key == active else ''}'>{label}</a>"
        for key, label, href in NAV_LINKS
    )
    html(
        f"""
        <div class="vl-nav">
            <a class="vl-brand" href="./" target="_self">
                <img src="{LOGO_URL}" alt="{COMPANY}">
                <span class="vl-brand-product">AI Crop Advisor</span>
            </a>
            <div class="vl-links">{links}</div>
            <a class="vl-btn vl-btn-green" href="{CONTACT_URL}" target="_blank">Talk to us</a>
        </div>
        """,
    )


def page_hero(title_html: str, subtitle: str) -> None:
    """Simple banner used at the top of content pages."""
    html(
        f"<div class='vl-page-hero'><h1>{title_html}</h1><p>{subtitle}</p></div>",
    )


def page_footer() -> None:
    quick_links = "".join(
        f"<li><a href='{href}' target='_self'>{label}</a></li>" for _, label, href in NAV_LINKS
    )
    html(
        f"""
        <div class="vl-footer">
            <div class="vl-footer-inner">
                <div>
                    <img src="{LOGO_URL}" alt="{COMPANY}">
                    <p>{COMPANY} is a next-generation software development company focused on
                    delivering innovative digital solutions. AI Crop Advisor is one of our
                    applied-AI products for agriculture.</p>
                </div>
                <div>
                    <h4>Quick Links</h4>
                    <ul>{quick_links}</ul>
                </div>
                <div>
                    <h4>Contact</h4>
                    <ul>
                        <li>📞 <a href="tel:{CONTACT_PHONE.replace(' ', '')}">{CONTACT_PHONE}</a></li>
                        <li>✉️ <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a></li>
                        <li>📍 {CONTACT_ADDRESS}</li>
                        <li>🌐 <a href="{COMPANY_URL}" target="_blank">vibrantlogics.com</a></li>
                    </ul>
                </div>
            </div>
            <div class="vl-footer-bottom">
                <span>Copyright © {date.today().year} {COMPANY}. All Rights Reserved.</span>
                <span><a href="./privacy" target="_self">Privacy Policy</a> &nbsp;·&nbsp;
                      <a href="./terms" target="_self">Terms &amp; Conditions</a></span>
            </div>
        </div>
        """,
    )
