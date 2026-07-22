from database.queries import fetch_filtered_jobs

from resume.extractor import ResumeExtractor

from rag.retriever import JobRetriever


resume_path = "Ashmanjum_resume.pdf"

resume_text = ResumeExtractor.extract_text(resume_path)

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

print("=" * 60)
print(f"Retrieved {len(results)} jobs")
print("=" * 60)

for i, (job, score) in enumerate(results, start=1):

    print(f"\nMatch {i}")

    print(f"Similarity Score : {score:.4f}")

    print(job.metadata)

    print("-" * 50)

    print(job.page_content[:400])

    print()