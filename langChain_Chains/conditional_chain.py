#problem_stmt: user gives a feedback -analyze the sentiment of the review - if positive- then reply with thanku  and give user the feedbackform rate 5 star
# else negative then sorry for inconvience and sends an email to  the customer support
# this is an example for the conditional chains

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
from langchain_core.runnables import RunnableBranch ,RunnableParallel,RunnableLambda

load_dotenv()

model = ChatOpenAI()
parser = StrOutputParser()
#as the output can b positive or negative in caps or small the op should b consistent so we are using structured output using Pydanticoutput parser
class Feedback(BaseModel):
    sentiment : Literal['positive','negative'] = Field(description="Give the sentiment of feedback")
    
parser2 = PydanticOutputParser(pydantic_object=Feedback)
prompt1 = PromptTemplate(
    template= " Classify the sentiment of the feedback into positive or negative \n {feedback} \n {format_instruction}",
    input_variables=["feedback"],
    partial_variables= {'format_instruction': parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser2
#result = classifier_chain.invoke({'feedback':'This is a terrible smart phone'}).sentiment

prompt2 = PromptTemplate(
    template= "Write appropriate response to this positive feedback \n {feedback}",
    input_variables=['feedback']
)
prompt3 = PromptTemplate(
    template= "Write appropriate response to this negative feedback \n {feedback}",
    input_variables=['feedback']
)
#to make the  branching we use runnable branch from runnables we can use if else conditions using this- swnd tuples 
# here inside tuple first arg is condition and second arg is its execution chain and a default condition chain in tuple is executed 
#Runnable Lambda it converts lambda function into runnable then we can use as a chain
branch_chain = RunnableBranch(
    (lambda x : x.sentiment == "positive" , prompt2 | model | parser),
    (lambda x : x.sentiment == "negative" , prompt3 | model | parser),
    RunnableLambda(lambda  x :"could not find sentiment")
   )
   
#merging both chains
chain =  classifier_chain |  branch_chain
result = chain.invoke({'feedback':" this is a terrible smart phone"})

print(result)
chain.get_graph().print_ascii()