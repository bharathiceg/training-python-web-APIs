from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

def build_knowledge_base(docs, model_name='all-MiniLM-L6-v2'):
    model = SentenceTransformer(model_name)
    embeddings = model.encode(docs, convert_to_tensor=True)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings.cpu().numpy())
    return model, index, embeddings

def retrieve(query, model, index, docs, top_k=3):
    query_emb = model.encode([query])[0]
    D, I = index.search(np.array([query_emb]), top_k)
    return [docs[i] for i in I[0]]
