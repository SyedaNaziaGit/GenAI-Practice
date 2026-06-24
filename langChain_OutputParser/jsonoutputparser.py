from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
#as we want dynamic prompts we used prompt template class 

load_dotenv()
#tiny llma cannot give structured output by default
llm = HuggingFaceEndpoint(repo_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",task = "text-generation")
model = ChatHuggingFace(llm =  llm)
parser = JsonOutputParser()
#creating prompt
template = PromptTemplate(
    template="Give me the name , age and city of a fictional person \n {format_instruction}",
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)
#without using chains
'''
#prompt
prompt = template.format()

result  = model.invoke(prompt)

final_result = parser.parse(result.content)
'''
#using chains
chain = template | model | parser
result = chain.invoke({})
#biggest drawback of jsonoutputparser is it cannot  enforce schema
print(result)