"""
=========================================================
Project Configuration
=========================================================
Loads all project configuration from .env
=========================================================
"""

import os
from dotenv import load_dotenv
from urllib.parse import quote_plus

# =========================================================
# Load Environment Variables
# =========================================================

load_dotenv()

# =========================================================
# PostgreSQL Configuration
# =========================================================

DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("DB_PORT"))
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

DATABASE_URL = (
    f"postgresql+psycopg2://"
    f"{DB_USER}:{quote_plus(DB_PASSWORD)}@"
    f"{DB_HOST}:{DB_PORT}/"
    f"{DB_NAME}"
)

# =========================================================
# Hugging Face Configuration
# =========================================================

HF_TOKEN = os.getenv("HF_TOKEN")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
LLM_MODEL = os.getenv("LLM_MODEL")

# =========================================================
# RAG Configuration
# =========================================================

TOP_K = int(os.getenv("TOP_K", 5))

# =========================================================
# Project Paths
# =========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

RESUME_DIR = os.path.join(BASE_DIR, "resume")

DATABASE_DIR = os.path.join(BASE_DIR, "database")

RAG_DIR = os.path.join(BASE_DIR, "rag")

UI_DIR = os.path.join(BASE_DIR, "ui")