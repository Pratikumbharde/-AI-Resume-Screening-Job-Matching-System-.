from preprocessing.resume_parser import extract_resume_text
from preprocessing.text_cleaner import clean_text
from embeddings.embedding_generator import generate_embedding
from similarity.similarity_score import compute_similarity
from llm.llama import analyze_resume_fit
from preprocessing.skill_extractor import extract_skills


resume_path = "data/resumes/sample_resume.pdf"

job_description = """
Looking for a full-stack developer with MERN stack,
backend APIs, and basic ML understanding.
"""

raw_text = extract_resume_text(resume_path)
clean_resume = clean_text(raw_text)
clean_jd = clean_text(job_description)
resume_skills = extract_skills(clean_resume)
jd_skills = extract_skills(clean_jd)

missing_skills = list(set(jd_skills) - set(resume_skills))

resume_skill_text = " ".join(resume_skills)
jd_skill_text = " ".join(jd_skills)

resume_emb = generate_embedding(resume_skill_text)
jd_emb = generate_embedding(jd_skill_text)


match_score = compute_similarity(resume_emb, jd_emb)

print("\nMATCH SCORE:", match_score)

analysis = analyze_resume_fit(
    match_score,
    missing_skills
)



print("\n=== ANALYSIS REPORT ===")

print("Match Score:", round(match_score * 100, 2), "%")

print("\nCandidate Skills:", resume_skills)
print("Required Skills:", jd_skills)
print("Missing Skills:", missing_skills)

print("\nLLM Advice:")
print(analysis)

