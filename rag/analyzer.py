"""
=========================================================
Resume Analyzer
=========================================================
Generates ATS analysis and combines it with
Python-generated job rankings.
=========================================================
"""

from rag.prompt import PromptBuilder
from rag.llm import ResumeLLM
from rag.parser import AnalysisParser


class ResumeAnalyzer:

    def __init__(self):

        self.llm = ResumeLLM()

    def analyze(
        self,
        resume_text,
        retrieved_jobs
    ):
        """
        Parameters
        ----------
        resume_text : str

        retrieved_jobs : list[(Document, distance)]

        Returns
        -------
        dict
        """

        jobs_with_similarity = []

        for job, distance in retrieved_jobs:

            similarity = max(0, (1 - distance)) * 100

            jobs_with_similarity.append(
                (
                    job,
                    similarity
                )
            )

        # Highest similarity first
        jobs_with_similarity.sort(
            key=lambda x: x[1],
            reverse=True
        )

        prompt = PromptBuilder.build_analysis_prompt(
            resume_text,
            jobs_with_similarity
        )

        response = self.llm.generate(prompt)

        analysis = AnalysisParser.parse(response)

        # ----------------------------------------
        # Build Top Matching Jobs using Python
        # ----------------------------------------

        top_jobs = []

        for rank, (job, similarity) in enumerate(
            jobs_with_similarity,
            start=1
        ):

            top_jobs.append({

                "rank": rank,

                "job_id": job.metadata["job_id"],

                "job_title": job.metadata["job_title"],

                "company": job.metadata["company"],

                "location": job.metadata["city"],

                "experience": job.metadata["experience_level"],

                "salary": job.metadata["salary_lpa"],

                "similarity": round(similarity, 2)

            })

        # Attach Python-generated ranking

        analysis["top_matching_jobs"] = top_jobs

        return analysis