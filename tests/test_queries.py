from database.queries import fetch_filtered_jobs

df = fetch_filtered_jobs(
    job_role="Data Analyst",
    experience_level="Junior (1-3 yrs)",
    location="Hyderabad"
)

print(df.head())
print(df.shape)