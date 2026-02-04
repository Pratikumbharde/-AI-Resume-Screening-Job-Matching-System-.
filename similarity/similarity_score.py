from sklearn.metrics.pairwise import cosine_similarity


def compute_similarity(e1, e2):
    score = cosine_similarity([e1], [e2])[0][0]
    return float(score)
