from database.queries import fetch_filtered_jobs

from resume.extractor import ResumeExtractor

from rag.retriever import JobRetriever

from rag.analyzer import ResumeAnalyzer


resume = ResumeExtractor.extract_text(
    "Ashmanjum_resume.pdf"
)

df = fetch_filtered_jobs(
    job_role="Data Analyst",
    experience_level="Junior (1-3 yrs)"
)

retriever = JobRetriever()

jobs = retriever.retrieve_jobs(
    dataframe=df,
    resume_text=resume,
    top_k=5
)

analyzer = ResumeAnalyzer()

analysis = analyzer.analyze(
    resume,
    jobs
)

print(type(analysis))

print()

print(analysis)