"""
Streamlit frontend entry point: `streamlit run main.py`.

Routes between the detector and the footer pages. Page content lives in
frontend/views/, shared styling, header and footer in frontend/theme.py.
"""

import streamlit as st

st.set_page_config(
    page_title="AI Crop Advisor | Vibrant Logics",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed"
)

pages = [
    st.Page("frontend/views/detect.py", title="AI Crop Advisor", default=True),
    st.Page("frontend/views/about.py", title="About Us", url_path="about"),
    st.Page("frontend/views/privacy.py", title="Privacy Policy", url_path="privacy"),
    st.Page("frontend/views/terms.py", title="Terms & Conditions", url_path="terms"),
]

# Navigation is drawn by our own header and footer, so hide Streamlit's sidebar menu.
st.navigation(pages, position="hidden").run()
