from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

def rank_candidates(jd_text, resume_texts, names):
    jd_embedding = model.encode([jd_text])
    resume_embeddings = model.encode(resume_texts)
    scores = cosine_similarity(jd_embedding, resume_embeddings)[0]
    
    results = []
    for i, score in enumerate(scores):
        results.append({'Rank': i+1, 'Name': names[i], 'Score': round(score * 100, 2)})
    
    results.sort(key=lambda x: x['Score'], reverse=True)
    for i, res in enumerate(results): res['Rank'] = i+1
    return results