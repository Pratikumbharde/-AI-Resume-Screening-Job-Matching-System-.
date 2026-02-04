import re

SKILL_PATTERNS = {
    "python": r"\bpython\b",
    "java": r"\bjava\b",
    "javascript": r"\bjavascript\b|\bjs\b",
    "react": r"\breact\b",
    "node": r"\bnode\b",
    "express": r"\bexpress\b",
    "mongodb": r"\bmongodb\b",
    "machine learning": r"machine learning|\bml\b",
    "deep learning": r"deep learning|\bdl\b",
    "nlp": r"\bnlp\b",
    "tensorflow": r"\btensorflow\b",
    "pytorch": r"\bpytorch\b",
    "sql": r"\bsql\b",
    "mysql": r"\bmysql\b",
    "docker": r"\bdocker\b",
    "aws": r"\baws\b|amazon web services",
    "api": r"\bapi\b|\bapis\b|\brest api\b|\brestful\b",
    "html": r"\bhtml\b",
    "css": r"\bcss\b",
}


def extract_skills(text):
    text = text.lower()
    found = []

    for skill, pattern in SKILL_PATTERNS.items():
        if re.search(pattern, text):
            found.append(skill)

    return sorted(set(found))
