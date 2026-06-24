from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

#using string output parser - they usually work with chains
#as we want dynamic prompts we used prompt template class 

load_dotenv()

model = ChatOpenAI()

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

#creating a parser
parser = StrOutputParser()

#forming a chain /pipeline to execute the flow
chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({"topic":"blackhole"})

print(result)