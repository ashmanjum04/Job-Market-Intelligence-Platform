from database.queries import fetch_filtered_jobs

from resume.extractor import ResumeExtractor

from rag.retriever import JobRetriever

from rag.llm import ResumeLLM

from rag.prompt import PromptBuilder

from rag.chat import CareerChatAssistant


# Resume
resume = ResumeExtractor.extract_text("Ashmanjum_resume.pdf")

# SQL
df = fetch_filtered_jobs(
    job_role="Data Analyst",
    experience_level="Junior (1-3 yrs)"
)

# Retrieval
retriever = JobRetriever()

jobs = retriever.retrieve_jobs(
    dataframe=df,
    resume_text=resume,
    top_k=5
)

# First generate ATS analysis
analysis_prompt = PromptBuilder.build_analysis_prompt(
    resume_text=resume,
    retrieved_jobs=jobs
)

analysis = ResumeLLM().generate(analysis_prompt)

print("=" * 70)
print("ATS ANALYSIS GENERATED")
print("=" * 70)

# Chat
assistant = CareerChatAssistant()

answer = assistant.ask(
    resume_text=resume,
    retrieved_jobs=jobs,
    analysis=analysis,
    question="Which company should I target first and why?"
)

print()
print("=" * 70)
print("CHAT RESPONSE")
print("=" * 70)
print(answer)