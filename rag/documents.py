"""
=========================================================
Document Creation Module
=========================================================
Converts filtered PostgreSQL job records into LangChain Documents.
=========================================================
"""

from langchain_core.documents import Document


def create_documents(df):
    """
    Convert DataFrame rows into LangChain Documents.

    Parameters
    ----------
    df : pandas.DataFrame

    Returns
    -------
    list[Document]
    """

    documents = []

    for _, row in df.iterrows():

        # Only embed the job description
        page_content = row["job_description"]

        # Store remaining information as metadata
        metadata = {
            "job_id": row["job_id"],
            "job_title": row["job_title"],
            "company": row["company"],
            "company_type": row["company_type"],
            "industry": row["industry"],
            "city": row["city"],
            "location_tier": row["location_tier"],
            "experience_level": row["experience_level"],
            "job_type": row["job_type"],
            "work_mode": row["work_mode"],
            "salary_lpa": row["salary_lpa"],
            "skills_required": row["skills_required"],
            "education_required": row["education_required"]
        }

        documents.append(
            Document(
                page_content=page_content,
                metadata=metadata
            )
        )

    return documents