import streamlit as st


def render_sidebar():

    st.sidebar.title("📊 Job Market Intelligence")

    st.sidebar.markdown("---")

    st.sidebar.markdown(
        """
### Features

- Resume Analysis

- ATS Match Score

- Job Recommendations

- AI Career Assistant
"""
    )

    st.sidebar.markdown("---")

    st.sidebar.info(
        "Upload your resume and receive personalized career insights."
    )