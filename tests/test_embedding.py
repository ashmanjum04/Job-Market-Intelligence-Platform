from rag.embeddings import load_embedding_model

embedding_model = load_embedding_model()

vector = embedding_model.embed_query(
    "Python SQL Power BI Data Analysis"
)

print(type(vector))

print(len(vector))

print(vector[:10])