from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")
text = "delhi is capital of india"
vector = embedding.embed_query(text)
print(str(vector))
#for multiple docs
documents =["Delhi is capital of india",
            "Banglore  is capital of Karnataka",
            "Gauhati is capital of Assam"]
vector2 = embedding.embed_documents(documents)
print(str(vector2))
