"""
=========================================================
Prompt Builder
=========================================================
Builds prompts for the LLM.

1. Resume Analysis Prompt
2. Career Chat Prompt
=========================================================
"""


class PromptBuilder:

    @staticmethod
    def build_analysis_prompt(resume_text, retrieved_jobs):
        """
        Build prompt for Resume Analysis.

        retrieved_jobs:
            List of tuples
            (Document, similarity_percentage)
        """

        jobs_context = ""

        for index, (job, similarity) in enumerate(retrieved_jobs, start=1):

            jobs_context += f"""
==================================================
Job {index}
==================================================

Similarity Score:
{similarity:.2f}%

Job ID:
{job.metadata['job_id']}

Job Title:
{job.metadata['job_title']}

Company:
{job.metadata['company']}

Location:
{job.metadata['city']}

Experience:
{job.metadata['experience_level']}

Salary:
{job.metadata['salary_lpa']} LPA

Job Description:
{job.page_content}

"""

        prompt = f"""
You are an expert ATS Resume Reviewer and Career Coach.

You will receive:

1. Candidate Resume
2. Top Matching Job Descriptions

Your task is to compare the resume against the retrieved jobs and return ONLY valid JSON.

==================================================
Candidate Resume
==================================================

{resume_text}

==================================================
Top Matching Job Descriptions
==================================================

{jobs_context}

==================================================
Instructions
==================================================

- Compare the resume with ALL retrieved jobs.
- Give an ATS Score out of 100.
- Write a short candidate summary.
- Identify resume strengths.
- Identify missing skills.
- Suggest resume improvements.
- Recommend projects.
- Recommend certifications.
- Suggest a learning roadmap.
- Recommend ONLY ONE best matching job.
- The similarity scores are already calculated.
- Do NOT calculate similarity.
- Do NOT rank jobs.
- Do NOT include top_matching_jobs.
- Return ONLY valid JSON.
- Do NOT use Markdown.
- Do NOT use triple backticks.
- Do NOT explain anything outside the JSON.

==================================================
Return ONLY this JSON
==================================================

{{
    "ats_score": 0,

    "candidate_summary": "",

    "strengths": [],

    "missing_skills": [],

    "resume_improvements": [],

    "recommended_projects": [],

    "recommended_certifications": [],

    "learning_roadmap": [],

    "best_matching_job": {{
        "job_id": "",
        "job_title": "",
        "company": "",
        "reason": ""
    }}
}}
"""

        return prompt.strip()

    @staticmethod
    def build_chat_prompt(
        resume_text,
        retrieved_jobs,
        ats_analysis,
        question,
        chat_history=""
    ):
        """
        Build prompt for Career Chat Assistant.

        retrieved_jobs:
            List of tuples
            (Document, similarity_percentage)
        """

        jobs_context = ""

        for index, (job, similarity) in enumerate(retrieved_jobs, start=1):

            jobs_context += f"""
==================================================
Job {index}
==================================================

Similarity Score:
{similarity:.2f}%

Job ID:
{job.metadata['job_id']}

Job Title:
{job.metadata['job_title']}

Company:
{job.metadata['company']}

Location:
{job.metadata['city']}

Experience:
{job.metadata['experience_level']}

Salary:
{job.metadata['salary_lpa']} LPA

Job Description:
{job.page_content}

"""

        prompt = f"""
You are an AI Career Assistant.

You already know:

1. The candidate's resume.
2. The ATS analysis.
3. The retrieved job descriptions.

Answer ONLY using the information below.

If the answer cannot be determined from the resume,
ATS analysis,
or retrieved jobs,
say so honestly.

==================================================
Candidate Resume
==================================================

{resume_text}

==================================================
ATS Analysis
==================================================

{ats_analysis}

==================================================
Retrieved Jobs
==================================================

{jobs_context}

==================================================
Previous Conversation
==================================================

{chat_history}

==================================================
User Question
==================================================

{question}

==================================================
Instructions
==================================================

- Answer professionally.
- Be concise.
- Compare jobs when appropriate.
- Explain why one job is a better fit.
- Recommend missing skills when asked.
- Recommend projects if relevant.
- Recommend certifications if relevant.
- Recommend learning resources if relevant.
- Never invent information.
- Base every answer only on the provided resume, ATS analysis and retrieved jobs.
"""

        return prompt.strip()