from database.queries import fetch_all_jobs
from rag.documents import create_documents

df = fetch_all_jobs()

documents = create_documents(df)

print(f"Total Documents : {len(documents)}")

print("\n==============================\n")

print(documents[0].page_content)

print("\n==============================\n")

print(documents[0].metadata)