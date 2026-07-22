"""
=========================================================
Resume Parser
=========================================================
Converts extracted resume text into structured
Python dictionary using the configured LLM.
=========================================================
"""

import json
import re

from rag.llm import ResumeLLM


print("=" * 80)
print("USING PARSER:", __file__)
print("=" * 80)


class ResumeParser:

    def __init__(self):
        self.llm = ResumeLLM()

    def parse(self, resume_text: str) -> dict:
        """
        Parse resume into structured information.
        """

        print("=" * 80)
        print("ResumeParser.parse() called")
        print("=" * 80)

        prompt = self._build_prompt(resume_text)

        response = self.llm.generate(prompt)

        print("=" * 80)
        print("RAW RESPONSE")
        print(response)
        print("=" * 80)

        cleaned_response = self._clean_response(response)

        print("=" * 80)
        print("CLEANED RESPONSE")
        print(cleaned_response)
        print("=" * 80)

        try:

            parsed_resume = json.loads(cleaned_response)

            print("=" * 80)
            print("JSON PARSED SUCCESSFULLY")
            print("=" * 80)

            return self._validate_output(parsed_resume)

        except json.JSONDecodeError as e:

            print("=" * 80)
            print("JSON ERROR")
            print(e)
            print("=" * 80)

            return {
                "error": str(e),
                "raw_response": cleaned_response
            }

    # -----------------------------------------------------
    # Prompt
    # -----------------------------------------------------

    def _build_prompt(self, resume_text: str) -> str:

        return f"""
You are an expert Resume Parser.

Extract information from the resume.

IMPORTANT RULES

- Return ONLY valid JSON.
- Do NOT explain anything.
- Do NOT use markdown.
- Do NOT wrap the response inside ```json.
- Do NOT write any text before or after the JSON.
- If something is missing, use "" or [].

Return exactly this structure:

{{
    "name": "",
    "email": "",
    "phone": "",
    "location": "",

    "summary": "",

    "skills": [],

    "education": [],

    "experience": [],

    "projects": [],

    "certifications": [],

    "languages": []
}}

Resume:

{resume_text}
"""

    # -----------------------------------------------------
    # Clean LLM Response
    # -----------------------------------------------------

    def _clean_response(self, response: str) -> str:

        print("=" * 80)
        print("INSIDE _clean_response()")
        print("=" * 80)

        response = response.strip()

        response = response.replace("```json", "")
        response = response.replace("```", "")
        response = response.strip()

        match = re.search(r"\{.*\}", response, re.DOTALL)

        if match:
            print("JSON OBJECT FOUND")
            return match.group(0)

        print("NO JSON OBJECT FOUND")

        return response

    # -----------------------------------------------------
    # Validate Output
    # -----------------------------------------------------

    def _validate_output(self, data: dict) -> dict:

        required_keys = {
            "name": "",
            "email": "",
            "phone": "",
            "location": "",
            "summary": "",
            "skills": [],
            "education": [],
            "experience": [],
            "projects": [],
            "certifications": [],
            "languages": []
        }

        for key, default in required_keys.items():
            data.setdefault(key, default)

        return data