from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
load_dotenv()

embedding = OpenAIEmbeddings(model_name = "text-embedding-3-large", dimensions=300)

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]
query = "Tell me about MS Dhoni"
#getting the embedding vector for query
query_embedding  = embedding.embed_query(query)
#getting embedding vector which is 300 d for documents
documents_embedding = embedding.embed_documents(documents)

#getting the similarity
similarity_scores = cosine_similarity([query_embedding],documents_embedding)[0]
#sorted list for highest score , sort on basis of score-  ascending order sort- extracting highest similarity score for the query
index, score = sorted(list(enumerate(similarity_scores),key = lambda x:x[1]))[-1]

print(query)
print(documents[index])
print("Similarity score  is:",score)
#hence embedding models are used to find the semantic search

