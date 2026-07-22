import streamlit as st


def resume_uploader():

    uploaded_file = st.file_uploader(
        "Upload Resume (PDF)",
        type=["pdf"]
    )

    return uploaded_file