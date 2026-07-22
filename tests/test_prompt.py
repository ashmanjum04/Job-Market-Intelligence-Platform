from database.queries import fetch_filtered_jobs

from resume.extractor import ResumeExtractor

from rag.retriever import JobRetriever

from rag.prompt import PromptBuilder


resume_text = ResumeExtractor.extract_text("Ashmanjum_resume.pdf")

df = fetch_filtered_jobs(
    job_role="Data Analyst",
    experience_level="Junior (1-3 yrs)"
)

retriever = JobRetriever()

results = retriever.retrieve_jobs(
    dataframe=df,
    resume_text=resume_text,
    top_k=5
)

prompt = PromptBuilder.build_prompt(
    resume_text,
    results
)

print(prompt)