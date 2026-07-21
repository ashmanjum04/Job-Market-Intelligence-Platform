# Job Market Intelligence Platform

An end-to-end Job Market Intelligence Platform that combines **Data Engineering, Business Intelligence, and Generative AI** to help job seekers analyze the job market, discover in-demand skills, evaluate resumes, and receive AI-powered career guidance.

---

## Project Architecture

```text
                    Multiple Job Datasets
          (CSV Files / APIs / Future Integrations)
                            │
                            ▼
                    Python ETL Pipeline
                            │
          ┌─────────────────┼─────────────────┐
          │                 │                 │
          ▼                 ▼                 ▼
     Data Cleaning    Data Transformation   Feature Engineering
          │
          ▼
                  PostgreSQL Data Warehouse
          (Star Schema - Fact & Dimension Tables)
                            │
          ┌─────────────────┼─────────────────┐
          │                 │                 │
          ▼                 ▼                 ▼
      SQL Analytics     Power BI        Streamlit Web App
                                          │
                                          ▼
                          AI Resume Analyzer (RAG)
                                          │
          ┌───────────────────────────────┼───────────────────────────────┐
          │                               │                               │
          ▼                               ▼                               ▼
 Resume Upload                    Job Filters                    PostgreSQL Query
(PDF Resume)               (Role, Location, Experience)     (Relevant Job Retrieval)
          │                               │
          └───────────────┬───────────────┘
                          ▼
              Build Job Documents
(Job Title + Skills + Education + Experience + Description)
                          │
                          ▼
           Hugging Face Embedding Model
             (Sentence Transformer)
                          │
                          ▼
                FAISS Vector Store
                          │
                          ▼
             Resume Embedding Generation
                          │
                          ▼
             Semantic Similarity Search
                  (Top Matching Jobs)
                          │
                          ▼
          LangChain Prompt Construction
                          │
                          ▼
          Hugging Face Large Language Model
                          │
                          ▼
        ATS Match Score • Missing Skills
      Resume Feedback • Career Suggestions
       Learning Roadmap • Interview Tips
```

---

# Project Workflow

## 1. Data Collection

Job market data is collected from multiple sources such as CSV datasets and external APIs (future enhancement).

The dataset contains information including:

- Job Title
- Company
- Company Type
- Industry
- Skills Required
- Education Required
- Experience Level
- Salary
- Work Mode
- Job Description
- Applicants
- Openings
- Company Rating
- Location

---

## 2. ETL Pipeline

Python is used to perform:

- Data Cleaning
- Missing Value Handling
- Duplicate Removal
- Data Transformation
- Feature Engineering
- Data Normalization
- Primary & Foreign Key Generation

---

## 3. PostgreSQL Data Warehouse

The transformed data is loaded into PostgreSQL using SQLAlchemy.

### Star Schema

**Fact Table**

- Job Details
- Salary
- Applicants
- Openings
- Ratings

**Dimension Tables**

- Company
- Location

The warehouse supports efficient SQL queries for analytical reporting.

---

## 4. Power BI Dashboard

Interactive dashboards provide insights for different stakeholders.

### Job Seeker Hub

- Hiring Trends
- Salary Analysis
- Skills Demand
- Experience Distribution
- Work Mode Analysis
- Company Ratings

### Recruiter Hub

- Hiring Analytics
- Applicant Trends
- Company Hiring
- Recruitment Metrics
- Location Insights
- Education Analysis

---

## 5. Streamlit Application

A user-friendly web application allows users to:

- Explore job market trends
- Filter jobs
- Analyze companies
- View hiring insights
- Upload resumes for AI analysis

---

# AI Resume Analyzer (RAG)

The Resume Analyzer combines PostgreSQL, LangChain, Hugging Face, and FAISS to generate personalized resume feedback.

## Step 1

The user uploads a resume (PDF).

---

## Step 2

The user selects filters such as:

- Target Role
- Experience Level
- Preferred Location

---

## Step 3

A dynamic SQL query retrieves only the relevant job postings from PostgreSQL.

---

## Step 4

Each retrieved job posting is converted into a document containing:

- Job Title
- Skills Required
- Education
- Experience
- Job Description

---

## Step 5

The documents are converted into vector embeddings using a Hugging Face Sentence Transformer.

---

## Step 6

The embeddings are indexed using FAISS for fast semantic retrieval.

---

## Step 7

The uploaded resume is converted into text and embedded using the same embedding model.

---

## Step 8

FAISS performs semantic similarity search to retrieve the most relevant job postings.

---

## Step 9

LangChain constructs a prompt using:

- Resume Content
- Retrieved Job Documents

---

## Step 10

A Hugging Face Large Language Model analyzes the resume and generates:

- ATS Match Score
- Resume Strengths
- Missing Skills
- Skill Gap Analysis
- Resume Improvement Suggestions
- Personalized Learning Roadmap
- Career Recommendations

---

# Tech Stack

### Programming

- Python

### Data Processing

- Pandas
- NumPy

### Database

- PostgreSQL
- SQLAlchemy

### Business Intelligence

- Power BI

### Web Application

- Streamlit

### AI & RAG

- LangChain
- Hugging Face
- Sentence Transformers
- FAISS

### Version Control

- Git
- GitHub

---

# Future Enhancements

- Live Job API Integration
- Resume Parsing Improvements
- Skill Gap Visualization
- Interview Question Generator
- Personalized Learning Resources
- Multi-Resume Comparison
- Job Recommendation Engine
- Resume Version Tracking
- Company-wise Hiring Prediction

---

# Project Highlights

- End-to-End ETL Pipeline
- PostgreSQL Data Warehouse
- Star Schema Design
- Interactive Power BI Dashboards
- Streamlit Analytics Application
- AI-Powered Resume Analyzer
- Retrieval-Augmented Generation (RAG)
- Semantic Job Matching
- ATS Compatibility Analysis
- Personalized Career Guidance
