import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

from resume.ats_analyzer import ATSAnalyzer

analyzer = ATSAnalyzer()

parsed_resume = {
    "name": "John Doe",
    "skills": [
        "Python",
        "SQL",
        "Pandas",
        "Power BI"
    ]
}

result = analyzer.analyze(
    parsed_resume=parsed_resume,
    job_role="Data Engineer",
    experience="Fresher"
)

print(result)