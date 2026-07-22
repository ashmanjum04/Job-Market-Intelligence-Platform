import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

from rag.llm import ResumeLLM

llm = ResumeLLM()

response = llm.generate(
    "What is Data Engineering? Explain in 5 lines."
)

print(response)