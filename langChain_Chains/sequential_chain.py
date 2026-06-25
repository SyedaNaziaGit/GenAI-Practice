from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
#problem stmt: user gives input topic to LLM and LLM gives detailed report  and that is sent to parser and then from that report - 
# to get summary llm passes op to another llm to get summary of the detailed report- this is a sequential chain -longchain

prompt1 = PromptTemplate(
    template="Generate detailed report on {topic}",
    input_variables= ["topic"]
)
prompt2 = PromptTemplate(
    template= "Generate a 5 pointer summary from the following text \n ,{text}",
    input_variables=["text"]
)

model = ChatOpenAI()

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({"topic":"Politics"})
print(result)

chain.get_graph().print_ascii()