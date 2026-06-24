from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

#as we want dynamic prompts we used prompt template class 
load_dotenv()
#tiny llma cannot give structured output by default
llm = HuggingFaceEndpoint(repo_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",task = "text-generation")
model = ChatHuggingFace(llm =  llm)

#to make a schema of pydantic modal
class Person(BaseModel):
    name : str = Field(description= "Name of the person")
    age : int = Field(gt = 18 , description="Age of the person")
    city : str = Field(description="Name of the city the person resides")
    
#making pydanticoutputparser
parser = PydanticOutputParser(pydantic_object=Person)

#writing prompt template
template = PromptTemplate(
    template="Generate the name, age and city  of a fictonal {place} person \n  {format_instruction}",
    input_variables=["place"],
    partial_variables={"format_instruction":parser.get_format_instructions()}
)
'''
prompt = template.invoke({"place":"india"})
result = model.invoke(prompt)
final_result = parser.parse(result.content)
print(final_result)
'''
chain = template | model | parser
result = chain.invoke({'place':'nepal'})
print(result)