from langchain_core.prompts import ChatPromptTemplate
#from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from dotenv import load_dotenv

load_dotenv()
#making dynamic set of messages in prompt 
chat_template =  ChatPromptTemplate.from_messages([
    ("system","You are a helpful {domain} expert"),
    ("human","Explain in simple  terms, what is {topic}")
    #SystemMessage(content="You are a helpful {domain} expert"),
    #HumanMessage(content="Explain in simple  terms, what is {topic}")
])

prompt = chat_template.invoke({"domain":"cricket", "topic":"Any"})
print(prompt)