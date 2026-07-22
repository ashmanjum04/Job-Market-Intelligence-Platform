"""
=========================================================
Retriever Module
=========================================================
Creates an in-memory FAISS index from filtered jobs and
retrieves the most relevant jobs for an uploaded resume.
=========================================================
"""

from langchain_community.vectorstores import FAISS

from rag.documents import create_documents
from rag.embeddings import load_embedding_model


class JobRetriever:

    def __init__(self):

        self.embedding_model = load_embedding_model()

    def retrieve_jobs(self, dataframe, resume_text, top_k=5):
        """
        Parameters
        ----------
        dataframe : pandas.DataFrame
            Filtered jobs from PostgreSQL

        resume_text : str
            Extracted resume text

        top_k : int

        Returns
        -------
        list[Document]
        """

        print("=" * 60)
        print("Creating Documents...")
        print("=" * 60)

        documents = create_documents(dataframe)

        print(f"Documents Created : {len(documents)}")

        print("\nBuilding Temporary FAISS Index...")

        vectorstore = FAISS.from_documents(
            documents,
            self.embedding_model
        )

        print("Searching Similar Jobs...\n")

        results = vectorstore.similarity_search_with_score(
            resume_text,
            k=top_k
        )

        return results