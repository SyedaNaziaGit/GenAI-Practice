#problem stmt : User gives a text doc -from this we generate notes and a quiz and combinely show to the user 

from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()
#model for  notes generation
model1 = ChatOpenAI()
#model for mcq generation
model2 = ChatAnthropic(model_name="claude-3-7-sonnet-20250219")
#prompt to create notes
prompt1 = PromptTemplate(
    template= "Generate short and simple notes from the following text \n {text}",
    input_variables= ["text"]
)
#prompt to create mcqs
prompt2 = PromptTemplate(
    template=" Generate 5 short  MCQs from the following text \n {text}",
    input_variables=["text"]
)
#prompt to merge both above results
prompt3 = PromptTemplate(
    template= "Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz}",
    input_variables=["notes","quiz"]
)

parser = StrOutputParser()
#parallel chain can be made using runnable parallel
parallel_chain = RunnableParallel({
    "notes" : prompt1 | model1 | parser ,
    "quiz" : prompt2 | model2 | parser
})

#merging both the parallel chains
merge_chain = prompt3 | model1 | parser

#finalchain - chaining those above chains for any complex operations
chain = parallel_chain | merge_chain

text = """
LangChain is an open-source orchestration framework that simplifies building applications powered by Large Language Models (LLMs).
It provides a standardized, modular set of tools and abstractions that allow developers to easily connect LLMs to external data sources,
memory systems, and software APIs
Core Concepts and ComponentsLangChain provides multiple built-in abstractions that handle the complexities of interacting with language 
models. Its core features include
Models: A standard, model-agnostic interface that allows developers to interact with hundreds of LLMs (e.g., OpenAI, Anthropic, 
Google Gemini) without rewriting vast amounts of code.Prompt Management: Tools to design, construct, and manage prompts using templates. 
This ensures the LLM receives inputs in the exact format and context required.
Chains (LCEL): Sequences of actions or steps where the 
output of one step becomes the input to the next. LangChain uses a declarative language known as LCEL, making composition highly efficient.
Memory Systems: Solutions for short-term and long-term memory. This allows AI applications to remember past interactions and maintain 
context across multiple turns or conversation threads.
Agents: Autonomous, LLM-driven components that analyze a user's request, reason through the problem, and decide which tools or APIs to
use to achieve the goal.
Data Connections: Interfaces that pull external data. This involves Document Loaders, Text Splitters, and Vector Databases to efficiently 
feed proprietary documents into the LLM.
"""

result = chain.invoke({"text":text})
print(result)
#shows the chain
chain.get_graph().print_ascii()