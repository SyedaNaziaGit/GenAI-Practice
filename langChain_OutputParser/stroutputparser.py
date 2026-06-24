from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
#as we want dynamic prompts we used prompt template class 
load_dotenv()
#tiny llma cannot give structured output by default
llm = HuggingFaceEndpoint(repo_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",task = "text-generation")
model = ChatHuggingFace(llm =  llm)

#prompt1- detailed report
template1 = PromptTemplate(
    template= "Write a detailed report on {topic}",
    input_variables=["topic"]
)
#prompt2 - summary 
template2 = PromptTemplate(
    template="Write a 5  line summary on given text . /n {text}",
    input_variables=["text"]
)

prompt1 = template1.invoke({"topic":"blackhole"})

result =  model.invoke(prompt1)

prompt2 =  template2.invoke({"text":result.content})

result2 = model.invoke(prompt2)

print(result2)