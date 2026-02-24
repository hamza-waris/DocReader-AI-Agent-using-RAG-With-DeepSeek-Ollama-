import streamlit as st

def inject_custom_css():
    st.markdown("""
    <style>
        /* Your CSS styles here */
    </style>
    """, unsafe_allow_html=True)

def render_title():
    st.title("📘 DocuMind AI")
    st.markdown("### Your Intelligent Document Assistant")
    st.markdown("---")
