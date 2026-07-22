"""
=========================================================
LLM Module
=========================================================
Uses LangChain + Groq
=========================================================
"""

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

from config import GROQ_API_KEY, LLM_MODEL


class ResumeLLM:

    def __init__(self):

        self.llm = ChatGroq(
            groq_api_key=GROQ_API_KEY,
            model=LLM_MODEL,
            temperature=0.2
        )

    def generate(self, prompt: str) -> str:

        response = self.llm.invoke(
            [
                HumanMessage(content=prompt)
            ]
        )

        return response.content