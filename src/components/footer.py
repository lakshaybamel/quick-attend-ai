import streamlit as st

GITHUB_URL = "https://github.com/lakshaybamel"


def footer_home():
    st.markdown(
        f"""
        <div style="margin-top: 2rem; display: flex; gap: 8px; justify-content: center; align-items: center;">
            <p style="font-weight: bold; color: black; margin: 0;">
                Built by
            </p>
            <a href="{GITHUB_URL}"><p style="font-weight: bold; color: white; margin: 0;">Lakshay Bamel</p></a>
        </div>
        """,
        unsafe_allow_html=True,
    )


def footer_dashboard():
    st.markdown(
        f"""
        <div style="margin-top: 2rem; display: flex; gap: 8px; justify-content: center; align-items: center;">
            <p style="font-weight: bold; color: black; margin: 0;">
                Built by
            </p>
            <a href="{GITHUB_URL}"><p style="font-weight: bold; color: #5865F2; margin: 0;">Lakshay Bamel</p></a>
        </div>
        """,
        unsafe_allow_html=True,
    )
