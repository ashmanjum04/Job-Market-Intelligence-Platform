from resume.extractor import ResumeExtractor

resume_text = ResumeExtractor.extract_text("Ashmanjum_resume.pdf")

print("\n========== RESUME TEXT ==========\n")
print(resume_text)