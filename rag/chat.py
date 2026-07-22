"""
=========================================================
Career Chat Assistant
=========================================================
Uses:

1. Resume
2. ATS Analysis
3. Retrieved Jobs
4. User Question

to generate intelligent career guidance.
=========================================================
"""

from rag.prompt import PromptBuilder
from rag.llm import ResumeLLM


class CareerChatAssistant:

    def __init__(self):

        self.llm = ResumeLLM()

    def ask(
        self,
        resume_text,
        retrieved_jobs,
        ats_analysis,
        question,
        chat_history=""
    ):
        """
        Ask a career-related question.

        Parameters
        ----------
        resume_text : str

        retrieved_jobs : list

        ats_analysis : str

        question : str

        chat_history : str

        Returns
        -------
        str
        """

        prompt = PromptBuilder.build_chat_prompt(
            resume_text=resume_text,
            retrieved_jobs=retrieved_jobs,
            ats_analysis=ats_analysis,
            question=question,
            chat_history=chat_history
        )

        answer = self.llm.generate(prompt)

        return answer