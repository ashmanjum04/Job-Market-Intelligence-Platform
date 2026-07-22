"""
=========================================================
Resume Text Extraction Module
=========================================================

This module extracts text from uploaded PDF resumes
using LangChain's PyPDFLoader.

Output:
    - Raw resume text
    - LangChain Documents (optional)

=========================================================
"""

from langchain_community.document_loaders import PyPDFLoader


class ResumeExtractor:

    @staticmethod
    def extract_text(pdf_path: str) -> str:
        """
        Extract complete text from a PDF resume.

        Parameters
        ----------
        pdf_path : str
            Path of uploaded PDF

        Returns
        -------
        str
            Complete resume text
        """

        loader = PyPDFLoader(pdf_path)

        documents = loader.load()

        resume_text = "\n".join(
            document.page_content
            for document in documents
        )

        return resume_text.strip()