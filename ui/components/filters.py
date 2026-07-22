import streamlit as st


def job_filters():

    col1, col2 = st.columns(2)

    with col1:

        job_role = st.selectbox(
            "Target Job Role",
            [
                "Android Developer","QA Engineer","Business Analyst","Cybersecurity Analyst","Python Developer","Backend Developer","Power BI Developer","Java Developer","Technical Lead","UI/UX Designer","Data Analyst","Software Engineer","Machine Learning Engineer","Data Engineer","Node.js Developer","Computer Vision Engineer","MLOps Engineer","DevOps Engineer","Product Manager","Frontend Developer","Full Stack Developer","Cloud Engineer","React Developer","Blockchain Developer","AI Engineer","Research Scientist","iOS Developer","NLP Engineer","Data Scientist","Engineering Manager"
            ]
        )

    with col2:

        experience = st.selectbox(
            "Experience Level",
            [
                "Fresher (0-1 yr)",
                "Junior (1-3 yrs)",
                "Mid (3-6 yrs)",
                "Senior (6-10 yrs)",
                "Lead (10+ yrs)"
            ]
        )

    return job_role, experience