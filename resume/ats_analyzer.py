"""
=========================================================
ATS Analyzer
=========================================================
Analyzes a parsed resume against the selected job role
using the configured LLM.
=========================================================
"""

import json
import re

from rag.llm import ResumeLLM


class ATSAnalyzer:

    def __init__(self):

        self.llm = ResumeLLM()

    # -----------------------------------------------------
    # Main Function
    # -----------------------------------------------------

    def analyze(
        self,
        parsed_resume: dict,
        job_role: str,
        experience: str
    ) -> dict:

        prompt = self._build_prompt(
            parsed_resume,
            job_role,
            experience
        )

        response = self.llm.generate(prompt)

        cleaned_response = self._clean_response(response)

        try:

            return json.loads(cleaned_response)

        except Exception:

            return {
                "error": "Failed to parse ATS response.",
                "raw_response": response
            }

    # -----------------------------------------------------
    # Prompt
    # -----------------------------------------------------

    def _build_prompt(
        self,
        parsed_resume: dict,
        job_role: str,
        experience: str
    ) -> str:

        return f"""
You are an expert Applicant Tracking System (ATS).

Evaluate the following resume for the target job.

Target Job Role:
{job_role}

Experience Level:
{experience}

Resume:

{json.dumps(parsed_resume, indent=4)}

----------------------------------------------------

Score the resume out of 100 using the following criteria.

1. Skills Match (30 points)
2. Relevant Projects (20 points)
3. Experience Match (20 points)
4. Education (10 points)
5. Certifications (10 points)
6. Keywords & Overall ATS Optimization (10 points)

The final ATS Score MUST be between 0 and 100.

Do NOT give extremely low scores unless the resume is completely unrelated.

Typical scoring guideline:

90-100 = Excellent match

80-89 = Very Good

70-79 = Good

60-69 = Average

Below 60 = Needs Improvement

----------------------------------------------------

Return ONLY valid JSON.

Do NOT use markdown.

Do NOT explain anything.

Return exactly this structure.

{{
    "ats_score": 0,

    "strengths": [],

    "missing_skills": [],

    "missing_keywords": [],

    "suggestions": [],

    "summary": ""
}}
"""

    # -----------------------------------------------------
    # Clean Response
    # -----------------------------------------------------

    def _clean_response(self, response: str) -> str:

        response = response.strip()

        response = response.replace("```json", "")
        response = response.replace("```", "")

        response = response.strip()

        match = re.search(r"\{.*\}", response, re.DOTALL)

        if match:
            return match.group(0)

        return response