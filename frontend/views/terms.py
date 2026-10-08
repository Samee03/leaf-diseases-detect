from frontend.theme import html, COMPANY, CONTACT_EMAIL, page_footer, page_header, page_hero

EFFECTIVE_DATE = "October 8, 2026"

page_header("terms")
page_hero("Terms &amp; <span class='vl-green-text'>Conditions</span>", f"Effective {EFFECTIVE_DATE}")

html(
    f"""
    <div class="vl-prose">
        <p>These Terms &amp; Conditions ("Terms") govern your use of the AI Crop Advisor
        application (the "Service") provided by {COMPANY} ("we", "us", "our"). By using the
        Service you agree to these Terms. If you do not agree, please do not use it.</p>

        <h2>1. The Service</h2>
        <p>The Service lets you upload an image of a plant leaf and receive an AI-generated
        assessment of possible diseases, severity, symptoms, causes and suggested treatments.
        We may change, suspend or discontinue any part of the Service at any time.</p>

        <h2>2. Not professional advice</h2>
        <div class="vl-callout">Results are produced automatically by an AI model and may be
        incomplete or incorrect. They are provided for general information only and are
        <b>not</b> a substitute for advice from a qualified agronomist, plant pathologist or
        other professional. You are solely responsible for any decisions you make, including
        the purchase or application of fungicides, pesticides, fertilisers or other
        treatments. Always follow product labels and local regulations.</div>

        <h2>3. Acceptable use</h2>
        <p>You agree not to:</p>
        <ul>
            <li>upload content you do not have the right to share, or content that is unlawful,
            offensive or contains other people's personal information;</li>
            <li>attempt to disrupt, overload, reverse engineer or gain unauthorised access to
            the Service or its infrastructure;</li>
            <li>use automated means to access the Service at a volume beyond normal personal use
            without our written permission;</li>
            <li>resell or commercially redistribute the Service or its outputs as your own product
            without a separate agreement with us.</li>
        </ul>

        <h2>4. Your content</h2>
        <p>You keep ownership of the images you upload. You grant us a limited licence to
        process them, including through our AI inference provider, solely to deliver the
        Service to you. See our <a href="./privacy" target="_self">Privacy Policy</a> for details.</p>

        <h2>5. Intellectual property</h2>
        <p>The Service, including its software, design, text and branding, is owned by
        {COMPANY} and protected by intellectual property laws. Except for your own content,
        nothing in these Terms grants you any rights in it.</p>

        <h2>6. Disclaimer of warranties</h2>
        <p>The Service is provided "as is" and "as available", without warranties of any kind,
        express or implied, including accuracy, fitness for a particular purpose,
        non-infringement or uninterrupted availability.</p>

        <h2>7. Limitation of liability</h2>
        <p>To the fullest extent permitted by law, {COMPANY} will not be liable for any
        indirect, incidental, special or consequential damages, or for any loss of crops,
        yield, revenue or data, arising from your use of, or reliance on, the Service.</p>

        <h2>8. Changes to these Terms</h2>
        <p>We may update these Terms from time to time. Continued use of the Service after
        changes take effect means you accept the revised Terms.</p>

        <h2>9. Governing law</h2>
        <p>These Terms are governed by the laws of the State of New York, USA, without regard
        to its conflict-of-law rules.</p>

        <h2>10. Contact</h2>
        <p>Questions about these Terms? Email
        <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a>.</p>
    </div>
    """,
)

page_footer()
