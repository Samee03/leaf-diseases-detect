from frontend.theme import html, COMPANY, CONTACT_ADDRESS, CONTACT_EMAIL, page_footer, page_header, page_hero

EFFECTIVE_DATE = "October 8, 2026"

page_header("privacy")
page_hero("Privacy <span class='vl-green-text'>Policy</span>", f"Effective {EFFECTIVE_DATE}")

html(
    f"""
    <div class="vl-prose">
        <p>This Privacy Policy explains how {COMPANY} ("we", "us", "our") handles information
        when you use the Leaf Disease AI application (the "Service").</p>

        <h2>1. Information we collect</h2>
        <ul>
            <li><b>Images you upload.</b> The leaf photo you submit for analysis, including any
            metadata embedded in the file (for example EXIF data such as camera model or GPS
            location, if your device recorded it).</li>
            <li><b>Technical data.</b> Standard server and hosting logs such as IP address,
            browser type, request time and error information.</li>
        </ul>
        <p>We do not ask you to create an account, and we do not knowingly collect names,
        email addresses or payment details through the Service.</p>

        <h2>2. How we use your information</h2>
        <ul>
            <li>To analyze your image and return a diagnosis.</li>
            <li>To operate, secure, troubleshoot and improve the Service.</li>
        </ul>

        <h2>3. How your image is processed</h2>
        <p>Uploaded images are processed in memory and are not saved to our own storage.
        To produce a diagnosis, the image is sent to our third-party AI inference provider,
        Groq, Inc., which runs the vision model on our behalf. Groq processes the image under
        its own terms and privacy policy. We do not sell your images or use them for
        advertising.</p>

        <h2>4. Third-party services</h2>
        <p>The Service relies on the following providers, each of which may receive technical
        data such as your IP address when your browser or our servers contact them:</p>
        <ul>
            <li>Groq: AI model inference</li>
            <li>Our hosting provider: serving the application and API</li>
            <li>Google Fonts and image CDNs: loading fonts and images on these pages</li>
        </ul>

        <h2>5. Cookies</h2>
        <p>The Service uses only the technical session mechanisms needed for the app to work.
        We do not use advertising or cross-site tracking cookies, and usage statistics
        collection in the app framework is disabled.</p>

        <h2>6. Data retention</h2>
        <p>Images are not retained by us after the analysis completes. Server logs are kept
        only as long as needed for security and troubleshooting, and are then deleted.</p>

        <h2>7. Security</h2>
        <p>We use reasonable technical and organisational measures to protect information in
        transit and in processing. No method of transmission over the internet is 100% secure,
        so please avoid uploading images that contain personal or sensitive content.</p>

        <h2>8. Your rights</h2>
        <p>Depending on where you live (for example under GDPR or CCPA), you may have rights to
        access, correct, delete or restrict the processing of your personal information. To
        make a request, contact us using the details below.</p>

        <h2>9. Children</h2>
        <p>The Service is not directed to children under 13, and we do not knowingly collect
        their personal information.</p>

        <h2>10. Changes to this policy</h2>
        <p>We may update this policy from time to time. The "Effective" date above shows when it
        was last revised.</p>

        <h2>11. Contact us</h2>
        <p>{COMPANY}<br>{CONTACT_ADDRESS}<br>
        <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a></p>
    </div>
    """,
)

page_footer()
