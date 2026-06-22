from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
#teparature range from 0-2 
#if deterministic use - then 0 temperature , if vivid unique response >1.5 and normal responses- around 0 to 1
model =  ChatOpenAI(model = "gpt-5.5",temperature =  0,max_completion_tokens=10)
result = model.invoke("What is capital of korea?")
model =  ChatOpenAI(model = "gpt-5.5",temperature =  1.6)
result = model.invoke("Suggest me 5 indian names for male")
model =  ChatOpenAI(model = "gpt-5.5",temperature =  1.8)
result = model.invoke("Write a poem on travel")
print(result.content)