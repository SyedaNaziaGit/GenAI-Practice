from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embedding = OpenAIEmbeddings(model = "text-embedding-3-large",dimensions = 32)
documents = ["Delhi is capital of india","Banglore  is capital of Karnataka","Gauhati is capital of Assam"]
result = embedding.embed_documents(documents)
print(str(result))