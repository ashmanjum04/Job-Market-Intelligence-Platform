from database.queries import fetch_all_jobs

df = fetch_all_jobs()

print(df.head())

print()

print(df.columns)

print()

print(df.shape)