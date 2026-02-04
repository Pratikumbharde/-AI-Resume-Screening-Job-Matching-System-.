from transformers import pipeline

generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    device=-1
)


def analyze_resume_fit(similarity_score, missing_skills):

    missing = ", ".join(missing_skills) if missing_skills else "none"

    prompt = f"""
Question: How can a candidate improve their resume if they lack skills in {missing}?

Answer:
"""

    result = generator(
        prompt,
        max_new_tokens=80,
        do_sample=False
    )

    return result[0]["generated_text"].replace("Answer:", "").strip()

