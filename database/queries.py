"""
=========================================================
Database Queries
=========================================================
Contains reusable SQL queries
=========================================================
"""

import pandas as pd
from sqlalchemy import text

from database.db import engine


def fetch_filtered_jobs(
    job_role=None,
    experience_level=None,
    location=None,
    work_mode=None,
    min_salary=None
):
    """
    Fetch jobs based on user-selected filters.

    Parameters
    ----------
    job_role : str
    experience_level : str
    location : str
    work_mode : str
    min_salary : float

    Returns
    -------
    pandas.DataFrame
    """

    query = """
        SELECT

            f.job_id,
            f.job_title,
            f.experience_level,
            f.job_type,
            f.work_mode,
            f.salary_lpa,
            f.skills_required,
            f.education_required,
            f.openings,
            f.applicants,
            f.company_rating,
            f.date_posted,
            f.job_description,

            c.company,
            c.company_type,
            c.industry,

            l.city,
            l.location_tier

        FROM fact_table f

        INNER JOIN company_table c
            ON f.company_id = c.company_id

        INNER JOIN location_table l
            ON f.location_id = l.location_id

        WHERE 1 = 1
    """

    params = {}

    if job_role:
        query += " AND f.job_title = :job_role"
        params["job_role"] = job_role

    if experience_level:
        query += " AND f.experience_level = :experience_level"
        params["experience_level"] = experience_level

    if location:
        query += " AND l.city = :location"
        params["location"] = location

    if work_mode:
        query += " AND f.work_mode = :work_mode"
        params["work_mode"] = work_mode

    if min_salary is not None:
        query += " AND f.salary_lpa >= :min_salary"
        params["min_salary"] = min_salary

    return pd.read_sql(
        text(query),
        engine,
        params=params
    )