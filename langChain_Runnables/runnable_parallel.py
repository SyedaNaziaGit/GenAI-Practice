from langchain_openai import  ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import  load_dotenv
from langchain_core.runnables import RunnableSequence,RunnableParallel

load_dotenv()
#problem statmt: runnables- first llm is giving tweet for the topic and other is generating post on the same topic for linkedin 
# they both are working parallely

prompt1 = PromptTemplate(
    template= " Generate a tweet about {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Generate a linkedin post about {topic}",
    input_variables=["topic"]
)

model = ChatOpenAI()
parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'tweet':RunnableSequence(prompt1,model,parser),
    'linkedin': RunnableSequence(prompt2,model,parser)
})

result = parallel_chain.invoke({'topic':'AI'})
print(result['tweet'])
print(result['linkedin'])