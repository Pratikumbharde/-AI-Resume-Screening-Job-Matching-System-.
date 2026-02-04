import streamlit as st
import tempfile

from preprocessing.resume_parser import extract_resume_text
from preprocessing.text_cleaner import clean_text
from preprocessing.skill_extractor import extract_skills
from embeddings.embedding_generator import generate_embedding
from similarity.similarity_score import compute_similarity


def generate_advice(missing_skills):
    if not missing_skills:
        return "Resume already matches job requirements well."

    advice = []
    for skill in missing_skills:
        advice.append(
            f"Add projects or experience demonstrating {skill} skills."
        )

    advice.append(
        "Highlight backend or real-world deployment experience."
    )

    return "\n".join(advice)


st.title("📄 AI Resume Screening System")

st.write("Upload resume and compare with job description.")

uploaded_file = st.file_uploader("Upload Resume (PDF/DOCX)", type=["pdf", "docx"])

job_description = st.text_area("Paste Job Description")

if st.button("Analyze Resume"):

    if uploaded_file is None or job_description.strip() == "":
        st.warning("Please upload resume and provide job description.")
        st.stop()

    # Save uploaded resume temporarily
    file_suffix = uploaded_file.name.split(".")[-1]

with tempfile.NamedTemporaryFile(delete=False, suffix=f".{file_suffix}") as tmp:
    tmp.write(uploaded_file.read())
    resume_path = tmp.name


    # Pipeline
    raw_resume = extract_resume_text(resume_path)
    clean_resume = clean_text(raw_resume)
    clean_jd = clean_text(job_description)

    resume_skills = extract_skills(clean_resume)
    jd_skills = extract_skills(clean_jd)

    missing_skills = list(set(jd_skills) - set(resume_skills))

    resume_skill_text = " ".join(resume_skills)
    jd_skill_text = " ".join(jd_skills)

    resume_emb = generate_embedding(resume_skill_text)
    jd_emb = generate_embedding(jd_skill_text)

    match_score = compute_similarity(resume_emb, jd_emb)
    match_percent = round(match_score * 100, 2)

    advice = generate_advice(missing_skills)

    st.subheader("📊 Match Score")
    st.progress(min(int(match_percent), 100))
    st.write(f"Match Score: **{match_percent}%**")

    st.subheader("🧠 Candidate Skills")
    st.write(resume_skills)

    st.subheader("📋 Required Skills")
    st.write(jd_skills)

    st.subheader("⚠ Missing Skills")
    st.write(missing_skills if missing_skills else "None")

    st.subheader("💡 Advice")
    st.write(advice)
