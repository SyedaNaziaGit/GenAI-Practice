from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain.output_parsers import ResponseSchema, StructuredOutputParser

#as we want dynamic prompts we used prompt template class 
load_dotenv()
#tiny llma cannot give structured output by default
llm = HuggingFaceEndpoint(repo_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",task = "text-generation")
model = ChatHuggingFace(llm =  llm)
#generating schema objects- response  schema
schema = [
    ResponseSchema(name = "fact_1", description = "Fact1 about this topic"),
    ResponseSchema(name = "fact_2", description = "Fact2 about this topic"),
    ResponseSchema(name = "fact_3", description = "Fact3 about this topic"),
    ResponseSchema(name = "fact_4", description = "Fact4 about this topic"),
]

parser = StructuredOutputParser.from_response_schemas(schema)

#creating template
template = PromptTemplate(
    template= "Give 4 facts about {topic} \n {format_instruction}",
    input_variables=["topic"],
    partial_variables={"format_instruction": parser.get_format_instruction()}
)
#without chain
'''
#making prompt
prompt = template.invoke({"topic":"blackhole"})
result = model.invoke(prompt)
final_result  =  parser.parse(result.content)

print(final_result)
'''
#using chain
chain = template | model | parser 
result = chain.invoke({'topic':'blackhole'})
print(result)

#disadvantage of using structred output parser is - we cannot do the data validation 