# Job Market Intelligence Platform – ETL Pipeline

## ETL Architecture

```text
                   Job Listings Dataset (CSV)
                              │
                              ▼
                    Data Extraction (Python)
                              │
                              ▼
                  Data Cleaning & Validation
      • Handle missing values
      • Remove duplicates
      • Standardize data types
      • Validate data consistency
                              │
                              ▼
                  Data Transformation (Pandas)
      • Create Company Dimension
      • Create Location Dimension
      • Generate Surrogate Keys
      • Replace descriptive columns with IDs
      • Prepare Fact Table
                              │
                              ▼
                   Star Schema Data Model
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
        ▼                     ▼                     ▼
  company_table        location_table         fact_table
        │                     │                     │
        └───────────────Foreign Keys───────────────┘
                              │
                              ▼
                 PostgreSQL Data Warehouse
```

---

# ETL Workflow

## 1. Extract

The raw job listings dataset is loaded into Python using **Pandas**.

**Input**

- Job Listings CSV Dataset

**Output**

- Raw DataFrame

---

## 2. Transform

The raw dataset is transformed into a dimensional data model suitable for analytics.

### Company Dimension

Extract unique company information:

- Company ID
- Company Name
- Company Type
- Industry

---

### Location Dimension

Extract unique location information:

- Location ID
- City
- Location Tier

---

### Fact Table

The fact table stores transactional job information along with foreign keys to the dimension tables.

Columns include:

- Job ID
- Job Title
- Experience Level
- Job Type
- Work Mode
- Salary (LPA)
- Skills Required
- Education Required
- Openings
- Applicants
- Company Rating
- Date Posted
- Job Description
- Company ID (FK)
- Location ID (FK)

---

## 3. Load

The transformed tables are loaded into a PostgreSQL Data Warehouse.

### Dimension Tables

- company_table
- location_table

### Fact Table

- fact_table

Primary Keys and Foreign Key relationships are maintained to support analytical queries and Power BI reporting.

---

# Star Schema

```text
              company_table
             ───────────────
             company_id (PK)
             company
             company_type
             industry
                   │
                   │
                   │
            company_id (FK)
                   │
                   ▼
              fact_table
        ─────────────────────
        job_id (PK)
        job_title
        experience_level
        job_type
        work_mode
        salary_lpa
        skills_required
        education_required
        openings
        applicants
        company_rating
        date_posted
        job_description
        company_id (FK)
        location_id (FK)
                   ▲
                   │
            location_id (FK)
                   │
                   │
             location_table
            ────────────────
            location_id (PK)
            city
            location_tier
```

---

# Technologies Used

- **Python**
- **Pandas**
- **SQLAlchemy**
- **PostgreSQL**
- **pgAdmin 4**

---

# Project Status

- ✅ Data Extraction
- ✅ Data Cleaning
- ✅ Data Transformation
- ✅ Star Schema Design
- ✅ PostgreSQL Data Warehouse
- ⏳ Power BI Dashboard
- ⏳ Streamlit Web Application
- ⏳ Resume Analyzer
- ⏳ AI Career Assistant
