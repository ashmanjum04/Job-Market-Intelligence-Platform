"""
=========================================================
Job Market Intelligence Platform
=========================================================
Main Streamlit Application
=========================================================
"""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

import streamlit as st
import tempfile
import os
import json

from components.sidebar import render_sidebar
from components.uploader import resume_uploader
from components.filters import job_filters

from resume.extractor import ResumeExtractor
from resume.parser import ResumeParser
from resume.ats_analyzer import ATSAnalyzer

from database.queries import fetch_filtered_jobs
from rag.retriever import JobRetriever
from rag.chat import CareerChatAssistant
# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------

st.set_page_config(
    page_title="Job Market Intelligence Platform",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# Sidebar
# ---------------------------------------------------------

render_sidebar()

# ---------------------------------------------------------
# Page Title
# ---------------------------------------------------------

st.title("📊 Job Market Intelligence Platform")

st.write(
    """
Upload your resume, choose your target job role,
and receive an AI-powered ATS analysis along with
the best matching jobs.
"""
)

st.divider()

# ---------------------------------------------------------
# Upload Resume
# ---------------------------------------------------------

uploaded_resume = resume_uploader()

# ---------------------------------------------------------
# Job Filters
# ---------------------------------------------------------

job_role, experience = job_filters()

st.divider()

# ---------------------------------------------------------
# Analyze Button
# ---------------------------------------------------------

# ---------------------------------------------------------
# Session State Initialization
# ---------------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "resume_text" not in st.session_state:
    st.session_state.resume_text = None

if "parsed_resume" not in st.session_state:
    st.session_state.parsed_resume = None

if "ats_result" not in st.session_state:
    st.session_state.ats_result = None

if "recommended_jobs" not in st.session_state:
    st.session_state.recommended_jobs = None


# ---------------------------------------------------------
# Analyze Button
# ---------------------------------------------------------

analyze = st.button(
    "🚀 Analyze Resume",
    type="primary",
    use_container_width=True
)


# ---------------------------------------------------------
# Resume Analysis
# ---------------------------------------------------------

if analyze or st.session_state.resume_text is not None:

    if analyze and uploaded_resume is None:

        st.warning("Please upload your resume.")

    elif analyze:

        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:

            temp_file.write(uploaded_resume.getbuffer())
            temp_pdf_path = temp_file.name

        try:

            # ---------------------------------------------
            # Step 1: Extract Resume Text
            # ---------------------------------------------

            with st.spinner("📄 Extracting resume text..."):

                resume_text = ResumeExtractor.extract_text(temp_pdf_path)

            # ---------------------------------------------
            # Step 2: Parse Resume
            # ---------------------------------------------

            with st.spinner("🤖 Parsing resume using AI..."):

                parser = ResumeParser()

                parsed_resume = parser.parse(resume_text)

            # ---------------------------------------------
            # Step 3: ATS Analysis
            # ---------------------------------------------

            with st.spinner("🎯 Performing ATS Analysis..."):

                analyzer = ATSAnalyzer()

                ats_result = analyzer.analyze(
                    parsed_resume=parsed_resume,
                    job_role=job_role,
                    experience=experience
                )

            # ---------------------------------------------
            # Step 4: Retrieve Recommended Jobs
            # ---------------------------------------------

            with st.spinner("🔍 Finding matching jobs..."):

                jobs_df = fetch_filtered_jobs(
                    job_role=job_role,
                    experience_level=experience
                )

                if jobs_df.empty:

                    recommended_jobs = []

                else:

                    retriever = JobRetriever()

                    recommended_jobs = retriever.retrieve_jobs(
                        dataframe=jobs_df,
                        resume_text=resume_text,
                        top_k=5
                    )

            st.session_state.resume_text = resume_text
            st.session_state.parsed_resume = parsed_resume
            st.session_state.ats_result = ats_result
            st.session_state.recommended_jobs = recommended_jobs
            st.session_state.messages = []
        
        except Exception as e:

            st.error(f"Error: {e}")
            st.stop()


        finally:

            if os.path.exists(temp_pdf_path):
                os.remove(temp_pdf_path)


    # Load previous analysis after Streamlit rerun

    resume_text = st.session_state.resume_text
    parsed_resume = st.session_state.parsed_resume
    ats_result = st.session_state.ats_result
    recommended_jobs = st.session_state.recommended_jobs
    # ---------------------------------------------
    # Display Results
    # ---------------------------------------------

    if analyze:
        st.success("✅ Resume analyzed successfully!")

    # Resume Text
    with st.expander("📄 Extracted Resume Text", expanded=False):

        st.text_area(
            label="",
            value=resume_text,
            height=350
        )

    # Parsed Resume
    with st.expander("📌 Parsed Resume", expanded=False):

        st.json(parsed_resume)

    st.divider()

    # -------------------------------------------------
    # ATS Dashboard
    # -------------------------------------------------

    st.header("🎯 ATS Analysis Report")

    st.metric(
        label="ATS Score",
        value=f"{ats_result['ats_score']}/100"
    )

    st.divider()

    # -------------------------------------------------
    # Strengths
    # -------------------------------------------------

    st.subheader("✅ Strengths")

    if ats_result["strengths"]:

        st.markdown(
            "\n".join(
                f"- {strength}"
                for strength in ats_result["strengths"]
            )
        )

    else:

        st.write("No strengths identified.")

    # -------------------------------------------------
    # Missing Skills
    # -------------------------------------------------

    st.subheader("❌ Missing Skills")

    if ats_result["missing_skills"]:

        st.markdown(
            "\n".join(
                f"- {skill}"
                for skill in ats_result["missing_skills"]
            )
        )

    else:

        st.write("No missing skills identified.")

    # -------------------------------------------------
    # Missing Keywords
    # -------------------------------------------------

    st.subheader("🔑 Missing Keywords")

    if ats_result["missing_keywords"]:

        st.markdown(
            "\n".join(
                f"- {keyword}"
                for keyword in ats_result["missing_keywords"]
            )
        )

    else:

        st.write("No missing keywords identified.")

    # -------------------------------------------------
    # Suggestions
    # -------------------------------------------------

    st.subheader("💡 Suggestions")

    if ats_result["suggestions"]:

        st.markdown(
            "\n".join(
                f"- {suggestion}"
                for suggestion in ats_result["suggestions"]
            )
        )

    else:

        st.write("No suggestions.")

    # -------------------------------------------------
    # Recruiter Summary
    # -------------------------------------------------

    st.subheader("📝 Recruiter Summary")

    st.write(ats_result["summary"])

    st.divider()

    st.header("💼 Top 5 Recommended Jobs")

    if not recommended_jobs:

        st.warning("No matching jobs found.")

    else:

        for i, (doc, score) in enumerate(recommended_jobs, start=1):

            metadata = doc.metadata

            with st.expander(
                f"{i}. {metadata['job_title']} | {metadata['company']}"
            ):

                st.write(f"**Company:** {metadata['company']}")
                st.write(f"**Location:** {metadata['city']}")
                st.write(f"**Experience:** {metadata['experience_level']}")
                st.write(f"**Work Mode:** {metadata['work_mode']}")
                st.write(f"**Salary (LPA):** {metadata['salary_lpa']}")
                st.write(f"**Industry:** {metadata['industry']}")

                st.write("**Skills Required:**")
                st.write(metadata["skills_required"])

                st.write("**Job Description:**")
                st.write(doc.page_content)

    st.divider()

    st.header("💬 AI Career Assistant")

    # Show previous chat
    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    question = st.chat_input(
        "Ask anything about your resume, ATS score or recommended jobs..."
    )

    if question:

        # Show user message
        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        with st.chat_message("user"):
            st.markdown(question)

        chatbot = CareerChatAssistant()

        with st.spinner("Thinking..."):

            answer = chatbot.ask(
                resume_text=resume_text,
                retrieved_jobs=recommended_jobs,
                ats_analysis=json.dumps(
                    ats_result,
                    indent=4
                ),
                question=question,
                chat_history="\n".join(
                    f"{m['role']}: {m['content']}"
                    for m in st.session_state.messages
                )
            )

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        with st.chat_message("assistant"):
            st.markdown(answer)
