import os
from datetime import datetime
from html import escape

import requests
import streamlit as st

from frontend.theme import html, page_footer, page_header

api_url = os.environ.get("API_URL", "http://localhost:8001")

STEPS = [
    ("📤", "Upload", "Snap or upload a clear photo of a single leaf in good light."),
    ("🧠", "Analyze", "Our vision AI inspects colour, texture, spots and lesions."),
    ("🔬", "Diagnose", "Get the likely disease, its type, severity and a confidence score."),
    ("🌱", "Treat", "Follow practical treatment steps to protect your crop."),
]


def _bullets(items) -> str:
    return "".join(f"<li>{escape(str(item))}</li>" for item in items or [])


def _list_section(icon: str, title: str, items) -> str:
    if not items:
        return ""
    return f"<div class='vl-list-title'>{icon} {title}</div><ul class='vl-list'>{_bullets(items)}</ul>"


def _confidence(result) -> tuple[str, float]:
    try:
        value = max(0.0, min(100.0, float(result.get("confidence"))))
        return f"{value:g}%", value
    except (TypeError, ValueError):
        return "N/A", 0.0


def _severity_badge(severity: str) -> str:
    tone = {"mild": "green", "moderate": "amber", "severe": "red"}.get(severity.lower(), "")
    return f"<span class='vl-badge {tone}'>Severity: {escape(severity.title())}</span>"


def render_result(result: dict) -> None:
    conf_label, conf_value = _confidence(result)
    timestamp = str(result.get("analysis_timestamp", "N/A"))
    try:
        timestamp = datetime.fromisoformat(timestamp).strftime("%b %d, %Y · %I:%M %p")
    except ValueError:
        pass
    timestamp = escape(timestamp)

    if result.get("disease_type") == "invalid_image":
        markup = f"""
        <div class='tone-warn'>
            <div class='vl-result-head'>
                <div class='vl-result-icon'>⚠️</div>
                <div><div class='vl-result-title'>Invalid Image</div>
                <div class='vl-result-sub'>Please upload a clear image of a plant leaf for accurate disease detection.</div></div>
            </div>
            {_list_section('🔎', 'Issue', result.get('symptoms'))}
            {_list_section('✅', 'What to do', result.get('treatment'))}
        </div>
        """
    elif result.get("disease_detected"):
        name = escape(str(result.get("disease_name") or "Unknown disease"))
        disease_type = escape(str(result.get("disease_type", "N/A")).title())
        markup = f"""
        <div class='tone-danger'>
            <div class='vl-result-head'>
                <div class='vl-result-icon'>🦠</div>
                <div><div class='vl-result-title'>{name}</div>
                <div class='vl-result-sub'>Disease detected</div></div>
            </div>
            <div class='vl-badges'>
                <span class='vl-badge'>Type: {disease_type}</span>
                {_severity_badge(str(result.get('severity', 'N/A')))}
            </div>
            <div class='vl-result-sub'>Confidence: <b>{conf_label}</b></div>
            <div class='vl-meter'><span style='width:{conf_value}%'></span></div>
            {_list_section('🔎', 'Symptoms', result.get('symptoms'))}
            {_list_section('🌦️', 'Possible Causes', result.get('possible_causes'))}
            {_list_section('💊', 'Treatment', result.get('treatment'))}
            <div class='vl-disclaimer'>AI-generated guidance. For high-value crops, confirm the diagnosis with a local agronomist before applying treatments.</div>
            <div class='vl-timestamp'>🕒 {timestamp}</div>
        </div>
        """
    else:
        status = escape(str(result.get("disease_type", "healthy")).title())
        markup = f"""
        <div class='tone-ok'>
            <div class='vl-result-head'>
                <div class='vl-result-icon'>✅</div>
                <div><div class='vl-result-title'>Healthy Leaf</div>
                <div class='vl-result-sub'>No disease detected in this leaf. The plant appears to be healthy!</div></div>
            </div>
            <div class='vl-badges'><span class='vl-badge green'>Status: {status}</span></div>
            <div class='vl-result-sub'>Confidence: <b>{conf_label}</b></div>
            <div class='vl-meter'><span style='width:{conf_value}%'></span></div>
            <div class='vl-timestamp'>🕒 {timestamp}</div>
        </div>
        """
    html(markup)


page_header("home")

html(
    """
    <div class="vl-hero">
        <h1>AI Crop <span class="vl-green-text">Advisor</span><br>
        for Healthier <span class="vl-green-text">Harvests</span></h1>
        <p>Upload a leaf photo and get an instant diagnosis, severity assessment
        and treatment plan, powered by vision AI.</p>
    </div>
    """,
)

steps_html = "".join(
    f"<div class='vl-step'><span class='num'>{i}</span><div class='icon'>{icon}</div>"
    f"<h3>{title}</h3><p>{text}</p></div>"
    for i, (icon, title, text) in enumerate(STEPS, start=1)
)
html(f"<div class='vl-steps'>{steps_html}</div>")

html(
    """
    <div class="vl-section" id="detect">
        <div class="vl-eyebrow">Try it now</div>
        <h2>Check your <span class="vl-purple-text">leaf</span> in seconds</h2>
    </div>
    """,
)

col1, col2 = st.columns([1, 1.35], gap="large")

with col1:
    with st.container(border=True):
        html(
            "<span class='vl-panel-marker'></span>"
            "<div class='vl-panel-title'>1. Upload a leaf image</div>"
            "<div class='vl-panel-sub'>JPG or PNG, one leaf, well lit and in focus.</div>",
        )
        uploaded_file = st.file_uploader(
            "Upload Leaf Image", type=["jpg", "jpeg", "png"], label_visibility="collapsed")
        if uploaded_file is not None:
            st.image(uploaded_file, width="stretch")
            detect_clicked = st.button("🔍 Detect Disease", width="stretch")
        else:
            detect_clicked = False

with col2:
    with st.container(border=True):
        html(
            "<span class='vl-panel-marker'></span>"
            "<div class='vl-panel-title'>2. Diagnosis</div>",
        )

        # Drop a stale result when the user removes or swaps the image.
        current_file = uploaded_file.file_id if uploaded_file is not None else None
        if st.session_state.get("result_file") != current_file:
            st.session_state.pop("result", None)

        if detect_clicked:
            with st.spinner("Analyzing image and contacting API..."):
                try:
                    files = {
                        "file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
                    response = requests.post(
                        f"{api_url}/disease-detection-file", files=files)
                    if response.status_code == 200:
                        st.session_state["result"] = response.json()
                        st.session_state["result_file"] = current_file
                    else:
                        st.error(f"API Error: {response.status_code}")
                        st.write(response.text)
                except Exception as e:
                    st.error(f"Error: {str(e)}")

        if "result" in st.session_state:
            render_result(st.session_state["result"])
        elif not detect_clicked:
            html(
                "<div class='vl-empty'><div class='big'>🍃</div>"
                "Upload a leaf image and click <b>Detect Disease</b><br>to see the diagnosis here.</div>",
            )

html(
    """
    <div class="vl-cta">
        <h2>Need AI built for your business?</h2>
        <p>Vibrant Logics designs and ships custom software and AI solutions like this one.</p>
        <a class="vl-btn vl-btn-green" href="https://vibrantlogics.com/contact" target="_blank">Book Your Free Appointment →</a>
    </div>
    """,
)

page_footer()
